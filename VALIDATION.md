# Validation

This revision addresses observed gaps in a long project: a coordinator overloaded with operational/verification work, repeated small allowance extensions, a partial deadline-bound delivery, and failed external runs waiting for exact artifact acknowledgements. First-call delay was user-reported but was not reproduced in the inspected successor coordinator, which requested staffing shortly after creation. Startup completion is now observable; no measured first-call improvement is claimed.

## Package and component checks

- Official skill structure validation passed.
- All 14 existing component tests passed for model choices, bounded report verification, deduplication, conflicts and preservation of review status. On this Windows sandbox the runner needed a writable workspace temporary directory; tests and production helpers were unchanged.
- UTF-8, ASCII English public content, JSON, Python syntax and internal references were checked.
- The release manifest covers every package file except itself with byte counts and SHA-256. The ZIP was reopened and compared byte for byte.
- Formal decision rules, the license and existing Python helpers/tests remain byte-identical to the prior package. Instance schema 1.1 adds planning records without changing helper behavior.

## Bounded behavior regression

The installed policy was evaluated before editing and the candidate independently applied to the same five scenarios. An additional diagnostic inspected consistency and preserved boundaries.

| Scenario | Candidate expectation |
| --- | --- |
| First invocation with two already authorized persistent employees | Verify bindings and caps, derive assignments and actually dispatch ready units without duplicate permission requests. |
| A long job needs exact raw-file acknowledgement while the coordinator is overloaded | Assign operations and detailed verification, qualify the actual service lifecycle and timing, then decide dependent launch readiness. |
| 75 minutes implementation + 25 tests + 20 sealing under a proposed 60-minute cap | Reject the infeasible cap; use an authorized feasible window or independently acceptable stages, distinguishing checkpoints and hard stops. |
| 48 hours of observation every 15 minutes with only 20 checks | Calculate 192 periodic checks plus applicable startup/closure observations and form a covering bounded allocation. |
| Chat allocation ends while an external child may still run | Preserve incomplete and stop-unknown state, ownership and reservations; use only an authorized stop/recovery path. |

Additional pressure cases check missing operational permission, valid progress after a soft checkpoint, hard-cap closure, and hashes/self-reports without independent acceptance evidence. The previous policy already supported immediate authorized dispatch and honest stop-state handling; these are retained behavior, not newly demonstrated improvements.

These are bounded simulated decisions and consistency checks, not repeated statistical trials or live host acceptance. They do not prove persistent process survival, working transport/supervision, sufficient account token quota, maximum transfer latency, or prevention of future project failure. Verify those capabilities in actual deployment before dependent expensive work. A skill update does not automatically reconfigure existing chats or jobs.
