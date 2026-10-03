# Staffing, state and runtime capabilities

Activate only necessary responsibilities. A lead may also execute; the main chat coordinates everyone. Ordinary reading and similar execution default to one employee. Independent review uses a different author with relevant expertise.

Assess staffing immediately when substantial similar work appears. Compare one employee with multiple employees for scale, differences, duration, shared bottlenecks, and handoff, duplicate work, communication, merging and verification costs. Make a grounded estimate from available information and record benefits, limits and staffing decisions. Without evidence, retain one employee; do not create an employee merely to estimate staffing costs. Reuse first; create the minimum additional staff only within human-authorized headcount, concurrency and budgets. Employees cannot recursively create employees.

Keep persistent employee profiles, separating project facts from decisions. New employees receive only their current responsibility, necessary evidence, approved baseline and work unit. Core files have one writer. Register scope, owner and capacity for exclusive resources such as compute or running instances, then queue users. A review does not release a resource reservation.

Instance records include task ID/scope, employee ID/role/chat ID/required host ID and verification status, authorization for each message direction, creation/staffing/wakeups, tool capabilities, overall parameter limits, department-pair round limits and their scopes. Unknown does not mean deployed, free or unlimited.

The main chat is the sole writer of the total ledger and overall task state. Employees write only their own artifacts, reports and receipts. Persist before acting, using consistent snapshots and append-only events. At minimum retain:

- Work-unit contracts, status, input/artifact revisions and content identities, checkpoints and next actions.
- Processed and pending messages, in-flight actions, authorization, reservations and tool receipts.
- All pending gates, original reviews and user decisions.
- `limit/spent/reserved`, allocation owner/direction/status, and major-issue and completion reserves.
- Employee/device bindings, resource reservations, read cursors, latest valid progress and external-job identities.

On recovery, first check stop instructions and every pending gate, then verify revisions, artifacts, in-flight actions, budgets, reservations and runtime status. Continue only authorized, unfrozen stages; do not repeat completed stages. Check receipts for unknown sends. Do not assign another writer to the same artifact while the previous executor's termination is unknown. Record ownership revision during handoff; verify old results before publishing them.

Default to one device and main-chat report collection; separately verify authorization and capabilities for active push. Keep the main chat active through authorized execution, official wait/read collection and acceptance while the host permits continuation. A routine progress message or work-unit completion is not a reason to end the turn. Checks after its turn ends require an authorized, verified host wakeup configuration. An unavoidable host handoff preserves pending work and its next action rather than marking the task complete. Receiving a notification is not processing it. Wakeups retain the original task and budget; scope awaiting a user decision remains frozen. Check counts, time windows, tokens and costs also count toward runtime budgets. Stop checks when nothing is pending; retain employee chats.

Prefer ordinary programs for fixed checks and wake the main chat only for judgment. Local scheduling depends on the execution device being available. Application crashes require host recovery; the skill cannot wake itself. If a capability is not connected, save pending state only.

Cross-device operation, recovery of running model tasks and whole-application crash recovery are host extensions. Verify them separately when required by the project; ordinary one-device operation does not depend on them. For an actual failure, preserve state, verify owners and processes, and recover through mechanisms already validated.

Prefer native client question notifications for pending answers. Body options and available question cards must remain visible; the host handles focus detection, notification permissions and system alerts. Distinguish unconfigured, user-confirmed enabled and actual delivery evidence; enabled settings do not prove delivery. Do not repeatedly remind for the same question or create extra polling automation. Scope awaiting adjudication remains frozen. [Official notification guide](https://learn.chatgpt.com/docs/notifications).
