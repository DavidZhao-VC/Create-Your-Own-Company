# Lifecycle allocations and deadlines

Plan from the deliverable and dependency path before selecting limits. There is no universal 60-minute implementation, 30-minute review, message count or token allowance. Saved limits are binding when actually authorized; legacy short allocations do not establish feasibility for newly assigned scope.

## Form a feasible allocation

Estimate separately, from actual scale and available measurements:

1. Input preparation and implementation.
2. Tests and representative runtime qualification.
3. Transfer, reconstruction and integrity/content verification.
4. Independent review, expected scoped correction and re-review.
5. Checkpointing, sealing, collection, final integration and safe shutdown.

Include serial dependencies and shared resource contention. Record estimate source and uncertainty; historical measurements apply only to comparable configuration and concurrency. Use a justified margin and reserve closure/recovery time explicitly. Missing measurements remain unknown, not zero. Use authorized small qualification checks where they can resolve uncertainty; do not start expensive work to discover that its essential support path does not fit.

For a hard finish time, schedule backwards through the required dependency path, including collection and review. Compare each proposed unit's complete duration against its available window. For example, 75 minutes of implementation, 25 of tests and 20 of sealing need at least 120 minutes before any additional contingency; a 60-minute hard unit is infeasible. Either allocate a covering authorized window or define independently acceptable stages and arrange their successor. A partial stage is not the completed deliverable.

For long tasks, propose a bounded lifecycle envelope covering planned units, communications, useful observation, repair/review rounds and closure. Estimate the count of checks from the cadence and actual active horizon, including final collection. For example, observing a 48-hour job every 15 minutes requires 192 periodic checks plus startup/final checks if each observation is charged; 20 checks cannot cover that plan. An official bounded wait returning unchanged progress is still an observation when the budget counts it. Verified deterministic monitoring may use a different configured accounting unit; state it rather than pretending it is free.

Reserve allocation for major failures, closure and acceptance before routine updates. At each useful checkpoint forecast remaining effort against remaining authority. If a shortfall is predicted, first reorder, stage or reclaim unused allocation within the existing authorization. If an increase is needed, request one concrete extension early, with spent/reserved amounts, unfinished scope and the complete revised path; keep the existing cap until the human authorizes the change. Avoid designing a long project around repeated approvals for one or two checks. Recovery and revisions do not reset counters.

Message counts, elapsed time, tokens, subscription quota and actual money are separate units. When runtime token/billing data is unavailable, record unknown and bound observable staffing, dispatches, checks, time and recovery. Do not invent a large token limit or claim that a message envelope guarantees sufficient subscription quota. A user-selected model stays in force; changes require covering authorization.

If the host exposes remaining account quota, reset windows or a per-run token cap, check and record them before long dispatches and at useful checkpoints. Account-wide remaining quota is shared, not an allocation guaranteed to this project. Compare estimates from comparable work against actual remaining limits; identify the checkpoint that must be saved before the next bounded stage. When usage is unavailable, keep the uncertainty explicit and use resumable stages with artifact checkpoints rather than one unbounded chat run. Context capacity is separate: read bounded report slices and referenced evidence, persist task state before context handoff, and preserve counters and outstanding gates on resume.

## Make deadline semantics explicit

Every long-work contract records:

| Field | Meaning and action |
| --- | --- |
| `next_progress_check_at` | A coordinator observation, not a work stop. |
| `soft_checkpoint_at` | Save/inspect progress and revise the remaining forecast. Valid progress may continue within existing hard caps. |
| `hard_stop_at` and `hard_stop_source` | A real authorized execution limit or external lease constraint. Do not move or reset it without covering authority. |
| `closure_reserve_minutes` and `stop_new_work_at` | Time before the hard stop to save, seal, deliver and shut down safely; plan these actions before the ceiling. |
| `external_job_deadline` / `acknowledgement_window_seconds` | Separate process/service constraints that may be earlier than the chat's hard stop. |
| `estimate`, `remaining`, `spent`, `reserved`, `extension_trigger` | The forecast and actual budget state needed to decide before exhaustion. |

Do not interpret `unit_soft_deadline_minutes` in an old instance as a hard cancellation deadline. Preserve any genuinely human-approved hard cap during migration and label it with its source. A tool's polling timeout, a chat turn ending, a soft checkpoint and a server lease ending have different effects.

At a soft checkpoint, save a usable checkpoint and report actual progress; continue feasible authorized work. When the forecast exceeds the remaining hard window, stage or escalate before consuming the closure reserve. At `stop_new_work_at`, start closure so that the report and checkpoint can be saved before `hard_stop_at`. At a hard ceiling, stop additional affected work and use only an already reserved/authorized safe-stop path. Label unfinished output `PARTIAL` or `BLOCKED`, list exact missing work, and preserve its next owner/action. Never silently renew time or tokens.

A chat ceiling does not prove an external process has stopped. Check its supervisor/parent and child receipts separately; preserve `STOP_REQUESTED` or `STOP_UNKNOWN` until termination is confirmed. Do not introduce another writer or a duplicate job while the old owner may still run. A legitimately preauthorized external service may continue within its separate limits and verified supervision; an expired chat allocation does not extend them. Preserve originals and formal review gates during every handoff.
