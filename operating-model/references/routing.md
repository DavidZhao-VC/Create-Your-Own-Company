# Responsibilities and work units

Choose responsibilities from the current deliverable, not an industry, software name or fixed scenario that activates everyone. The main chat handles a few clear requirements, local edits and focused checks directly.

The main chat owns decomposition and assignment. Derive substantive requirements from the user's requested outcome even when the request is unnumbered. Include the checks needed to accept each deliverable, without inventing new objectives or counting formatting constraints as separate requirements. Record a lightweight work table in project state:

| Unit and covered requirements | Single accountable owner | Deliverable and acceptance | Inputs and dependencies | Writable scope | Status and next action |
| --- | --- | --- | --- | --- | --- |
| Stable unit ID and substantive requirement IDs | Main chat or a verified employee identity | Concrete output and observable checks | Required artifacts, revisions and predecessor units | Exact files or resource boundary | Current state, blocker if any, and next executable step |

Cover every substantive requirement and assign one accountable owner per unit. Include necessary operations, transport and verification; they are part of delivery rather than incidental main-chat chores. An employee may own several units; an independent review has a different author. Use the fewest suitable employees within existing authorization. For work below the dispatch threshold, the main chat owns and completes the units. A table is a working record: do not require the user to approve ordinary task organization or supply department names. Complete the first-call procedure in [execution.md](execution.md): when dispatch is justified and authorized, issue concrete contracts and start ready work rather than stopping after a proposed staffing plan. Missing authority blocks the affected dispatch, while independent authorized work continues.

## Main-chat execution loop

1. Check critical service alerts and earliest irreversible deadlines, then inventory outputs, authorization, gates, resource owners and remaining allocations. Required collection and acknowledgements take priority over routine coding.
2. Derive or update the work table, then execute or dispatch ready authorized units with concrete acceptance criteria.
3. Use bounded official waits and read cursors for active units. A wait timeout with valid progress within the deadline and budget keeps the task active; continue checks while the host permits them. Check on a useful cadence rather than repeatedly polling unchanged state.
4. Collect compact bound reports and detailed-verification receipts against the unit contract. Use assigned employees or verified programs for bulk transfer and full checks; the main chat assesses coverage, disputed evidence and adoption rather than becoming the serial executor of all checks. Record the accepted revision, resolve ordinary technical issues within authority, satisfy dependencies and start the next ready unit. Formal verdicts and human-only blockers follow the existing decision gates.
5. Before final delivery, verify coverage of every original requirement, intended revisions, necessary integrated checks and all applicable gate decisions. Mark overall completion only when required work and jobs are finished or explicitly disposed of by a covering user decision. Saved unit reports alone do not establish overall acceptance.

After a progress update, a technical coordination action or a unit report, continue from the next applicable step. Do not ask the user whether to continue a next step already covered by authority. If a genuine human decision is needed, present it promptly and freeze only dependent work. For an unavoidable host limit, save the incomplete state, current owners and next action; record a verified authorized handoff when one exists, otherwise state the actual continuation blocker. Do not promise background checks without a working authorized host mechanism.

| Responsibility | When needed and what to deliver |
| --- | --- |
| `research` | External sources, evidence or method verification: sources, facts, applicability and uncertainty. |
| `design` | Structure, solution paths or tradeoffs: goals, options, dependencies and approved revision. |
| `engineering` | Building, running or reproducing: usable artifacts and actual verification. |
| `visual_media` | Expression, presentation or media production: requested source files, finished output and presentation checks. |
| `review` | Independent acceptance review: explicit type, revision, scope, evidence and verdict. |

A work unit corresponds to one independently verifiable deliverable and its necessary checks. If too large, stage it within the same employee chat first and assign a feasible successor. Apply [planning.md](planning.md) before setting allocations. Parallelism or the number of units does not itself justify more employees. Register long external jobs separately with operational ownership and supervision rather than keeping a chat waiting idly.

Dispatch contracts use instance parameters and include:

- Stable `task_id`, `unit_id` and revision, goal, necessary inputs and authoritative artifact location.
- Owner, writable/operational scope, dependencies, resources, applicable authorization and design approval; assigned transfer and verification owners with handoff criteria.
- Deliverables and acceptance criteria; separate the report-summary limit from detailed artifact scope.
- Model and reasoning settings, message/token/API-equivalent cost limits with estimate/provenance, first progress check, soft checkpoint, hard stop and its authority, closure reserve, external-job/service deadlines and permitted recovery attempts. Plan the complete lifecycle and useful observation cadence, not only implementation.

Reuse verified parameters. Mark unknown values unconfigured and fill only what affects the next action. Use short summaries and evidence references for routine reports; preserve complete detailed artifacts. Acceptance depends on actual content, behavior or presentation, not just source-file existence. Inventory existing artifacts before starting new heavy jobs.
