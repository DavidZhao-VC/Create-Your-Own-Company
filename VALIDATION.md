# Validation

- Official skill structure validation passed.
- All 14 local component tests passed, covering model choices, report verification, deduplication, conflicts and preservation of review status.
- UTF-8, JSON, Python syntax and internal file references were checked.
- The release package includes a per-file SHA-256 manifest. The ZIP was reopened, extracted and compared byte for byte.

Component and package checks do not replace acceptance testing of persistent chats, active sends, wakeups or notifications in the target host.

## Coordination rule checks

The candidate was applied to ten hypothetical coordinator snapshots in a fresh evaluation context. The resulting task states and continuation choices matched the following expectations; concrete assignments and next actions were also inspected.

| Snapshot | Expected action |
| --- | --- |
| A predecessor unit completes | Verify its output and release the assigned successor. |
| A wait times out with valid progress | Continue permitted bounded waits within the deadline and allocation. |
| Requirements are not numbered | Derive verifiable work units and assign suitable authorized owners. |
| A task is below the dispatch threshold | Organize, execute and verify it in the main chat. |
| Three ordinary small issues are reported | Resolve scoped technical issues and continue, without inventing a user gate. |
| A formal design review ends with PASS | Request revision-bound human adoption approval; continue independent work. |
| A formal review returns FAIL | Preserve the verdict and freeze affected actions for human adjudication. |
| All unit reports exist but integration is unchecked | Verify original requirements, revisions and the combined deliverable. |
| Overall acceptance is complete | Deliver the result and stop unnecessary checks. |
| The host requires an authorized verified handoff | Preserve incomplete state and the actual continuation mechanism. |

These are simulated policy-application checks, not live host runs or a measured reduction in failure rate. The old-policy and no-skill controls also chose correct actions in this evaluation, so the reported live symptom was not reproduced. The revision makes previously inferred continuation, decomposition and overall-acceptance requirements explicit. Repeated independent trials and acceptance testing in a real project remain separate evidence.
