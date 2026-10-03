# Decisions and reviews

Enter `HUMAN_REVIEW` for:

- `DIRECTION_CHANGE`: changing an approved goal, solution path or design baseline.
- `CORE_REMOVAL`: deleting key content, major capabilities or necessary evidence.
- `HUMAN_INPUT_BLOCK`: intent, tradeoffs or authorization only the user can provide. The main chat handles technically resolvable blockers.
- `DESIGN_APPROVAL`: a formal design review has ended, or its revision is ready for adoption; even PASS requires user approval.
- `FORMAL_REVIEW_FAIL`: any formal FAIL, including a late result for an old revision. Preserve original evidence and freeze affected scope.

Register review type, revision, scope and gates before a formal review begins. Do not retroactively downgrade a design review or FAIL. A later PASS, new revision or renamed review does not release the gate. Before approval, affected scope permits only read-only evidence organization; independent work may continue under existing authorization.

The main chat presents a short decision packet: the required decision, verified facts, artifacts and revision, options and costs, a recommendation, and necessary designs, previews or evidence. The user interacts only with the main chat.

Record each gate separately with `gate_id`, reason, task, scope and dependencies, revision, content identity, status and original review. Record a user decision with `decision_id`, source instruction reference, explicitly covered gates/scope/revision, permitted actions, budget changes and limits. Close only covered gates; others stay frozen. Staffing approval does not release a design FAIL; old approval does not cover a new baseline. Reuse an existing valid approval for the same revision and scope rather than asking again.

On recovery, read all unresolved gates before checking the next action's dependencies. A single status must not hide multiple approvals. If the user accepts a failed artifact with limits, retain FAIL and record `ACCEPTED_WITH_LIMITS` and its conditions. Ordinary quality, factual or delivery PASS may be handled under existing authorization. Mark an unreceived review pending; do not invent FAIL or overall acceptance. Program recovery, cancellation and deadlines do not substitute for a user decision.

When the user authorizes only continued repair, check exactly which scope the instruction covers. Uncovered design-change or re-review gates remain frozen; deadlines and sunk costs do not expand authorization. Only the main chat asks for clarification. Explicitly permitted actions independent of other gates may continue.

Decision-message format: begin with "There is a question for you to answer." Explain the decision, then number each option with its action, main impact and recommendation rationale. Mark unknowns when evidence is insufficient. Submit an available question card afterward using the same options; do not replace body options with "see the card below." Escalate only the scope requiring a user decision; independent work continues.

If the user chooses archive or stop, preserve the draft, original FAIL, source message, scope/revision, evidence hashes and disposition receipt. Close the corresponding wait and end that task. Record repair, re-review and adoption permissions according to the actual decision. Recollection or report generation must merge the latest decision rather than lose the selection or reopen an already handled gate. Do not turn the original FAIL into PASS.
