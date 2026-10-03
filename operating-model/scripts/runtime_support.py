"""Small coordinator helpers; no chat dispatch, network, scheduler or approval override."""
from pathlib import Path
import hashlib,json,os,tempfile,datetime

def digest(data):
    return hashlib.sha256(data).hexdigest()

def resolve_path(path,owner):
    result=Path(path).resolve()
    if not result.is_relative_to(owner):
        raise ValueError('REPORT_PATH_OUTSIDE_OWNER')
    return result

def resolve_model(profile,operation,capabilities,host='local'):
    if operation not in ('create_thread','send_message_to_thread'):
        raise ValueError('MODEL_OPERATION_UNSUPPORTED')
    choice=profile.get('model_choice') or {}
    if choice.get('state') not in ('user_preselected','selected') or not choice.get('source_user_message_id'):
        raise ValueError('MODEL_SELECTION_REQUIRED: ask once in the main chat')
    model,thinking=choice.get('model'),choice.get('thinking')
    if thinking not in capabilities.get(host,{}).get(model,[]):
        raise ValueError('MODEL_UNAVAILABLE: return to main chat; do not substitute')
    return {'model':model,'thinking':thinking}

def save_state(path,state):
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=None
    try:
        with tempfile.NamedTemporaryFile(mode='w',encoding='utf-8',dir=path.parent,prefix='.inbox-',suffix='.tmp',delete=False) as f:
            temporary=Path(f.name)
            json.dump(state,f,ensure_ascii=False,indent=2)
            f.write('\n');f.flush();os.fsync(f.fileno())
        os.replace(temporary,path)
    finally:
        if temporary and temporary.exists():
            temporary.unlink()

def collect_report(binding,state_path):
    # The binding belongs to the coordinator, not the employee's report text.
    owner=Path(binding['owner_directory']).resolve()
    report_path=resolve_path(binding['report_path'],owner)
    raw=report_path.read_bytes()
    report=json.loads(raw.decode('utf-8',errors='strict'))
    report_id=report.get('report_id') or report.get('message_id')
    if report.get('task_id')!=binding['task_id'] or report_id!=binding['report_id']:
        raise ValueError('REPORT_IDENTITY_MISMATCH')
    for declared in report.get('artifacts',[]):
        p=declared.get('path') if isinstance(declared,dict) else declared
        if not isinstance(p,str): raise ValueError('REPORT_ARTIFACT_INVALID')
        resolve_path(p,owner)
    verified=[]
    for p,expected in binding['artifacts'].items():
        actual_path=resolve_path(p,owner)
        actual=digest(actual_path.read_bytes())
        if actual!=expected.lower():
            raise ValueError('ARTIFACT_HASH_MISMATCH')
        verified.append({'path':str(actual_path),'sha256':actual})
    # Transport metadata can acquire new receipts without changing the substantive report.
    excluded={'delivery','delivery_result','delivery_allocation','receipt','transport','received_at','collected_at'}
    substantive={k:v for k,v in report.items() if k not in excluded}
    identity=digest(json.dumps({'report':substantive,'bound_thread_id':binding['thread_id'],'host_id':binding['host_id'],'verified_artifacts':verified},ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8'))
    key='|'.join((binding['task_id'],binding['thread_id'],report_id))
    state_path=Path(state_path).resolve()
    if state_path.is_relative_to(owner):
        raise ValueError('INBOX_MUST_BE_COORDINATOR_OWNED')
    state=json.loads(state_path.read_text(encoding='utf-8')) if state_path.exists() else {'reports':{},'conflicts':[]}
    timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
    receipt={'key':key,'report_id':report_id,'task_id':binding['task_id'],'thread_id':binding['thread_id'],'host_id':binding['host_id'],'identity_sha256':identity,'source_report_sha256':digest(raw),'method':'main_read','push_delivery_confirmed':False,'active_message_delta':0,'user_adoption_approved':False,'collected_at':timestamp,'verified_artifacts':verified}
    previous=state['reports'].get(key)
    if previous:
        if previous['identity_sha256']==identity:
            return {**previous,'outcome':'already_collected'}
        conflict={**receipt,'outcome':'content_conflict','previous_identity_sha256':previous['identity_sha256'],'affected_scope_frozen':True,'preserved_report':report}
        if not any(x['key']==key and x['identity_sha256']==identity for x in state['conflicts']):
            state['conflicts'].append(conflict);save_state(state_path,state)
        return conflict
    formal_fail=str(report.get('status','')).upper()=='FAIL' or str(report.get('verdict','')).upper()=='FAIL'
    receipt.update(outcome='collected',affected_scope_frozen=formal_fail,report_status=report.get('status'),preserved_report=report)
    state['reports'][key]=receipt
    save_state(state_path,state)
    return receipt
