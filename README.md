# operating-model

A skill for persistent chat coordination. The user communicates only with the main chat, which assigns work, handles decisions and accepts the overall result. Employee chats retain their identities and context. Implementation, ongoing operations, transport and detailed verification have explicit owners. Use it for tasks with multiple substantive requirements, independent deliverables and review needs.

## Core rules

- The main chat derives work units from the requested outcome and records each owner, deliverable, acceptance criteria, dependencies, writable scope and next action. Users need not enumerate requirements or request assignment.
- First invocation and handoff include identity/authorization checks and actual dispatch of ready authorized units before substantial implementation. A saved staffing proposal does not complete startup.
- Dispatch employees only when a task has at least three substantive requirements and a worthwhile division of work. The main chat still organizes and completes smaller tasks.
- Activate research, design, engineering, visual/media and review responsibilities as needed. Reuse the minimum staff.
- Escalate major decisions, formal design reviews and any formal FAIL to the user. Freeze only affected scope.
- Form internal reports immediately for major issues and completed units. The main chat verifies them, updates dependencies and continues authorized work. Batch three small issues within the same task; coordinate real blockers earlier.
- Keep routine progress in records. Required visible progress updates remain brief and non-final. Deliver the final result after overall acceptance, or seek user input for an actual decision, authorization or blocker. Record unavoidable host handoffs accurately.
- Employees save artifacts and the main chat collects them. Instance settings govern communication, budgets, models, deadlines and recovery.
- Assign deadline-sensitive operations and bulk checks to authorized owners and qualified programs. Before dependent expensive jobs, verify the actual transfer/acknowledgement path, process lifetime, monitoring, capacity and recovery; source checks alone do not qualify unattended operation.
- Plan allocations for implementation, tests, transfer, review, repair and closure. Soft checkpoints prompt inspection; actual authorized hard stops remain binding. Forecast exhaustion and reserve completion capacity rather than relying on repeated tiny extensions.
- Present user choices in the main chat's message body. Available question cards and native notifications support that exchange.

## Usage

Place the complete `operating-model` directory in your host's Skills directory, preserving its internal paths. Invoke `$operating-model` in the main chat and describe the task.

Copy the [instance template](operating-model/assets/instance.template.json) into the project workspace. Configure model choices, chat bindings, budgets and runtime parameters as needed. Null values mean unconfigured. Skill files and templates do not authorize chat creation, message sending or budget increases.

Read [execution.md](operating-model/references/execution.md) for first dispatch and operational ownership, and [planning.md](operating-model/references/planning.md) before allocating long work. Instance schema 1.1 adds startup, service and lifecycle records. Existing instances retain their human-approved limits; the legacy soft-deadline field is a checkpoint unless a real hard cap was separately authorized. These fields do not install a supervisor or enforce scheduling.

The host must supply persistent chats, official read/wait tools and project state storage. Active return messages, background wakeups and notifications depend on host capabilities and valid authorization. Default operation uses one device; verify cross-device operation and application recovery separately when the project requires them.

Start with [SKILL.md](operating-model/SKILL.md); read files under `references/` only for the relevant action. The helpers use the Python 3.9+ standard library for model-choice resolution, report verification and deduplication. They do not include a chat scheduler.

## Validation

Run component tests:

```sh
python -B -m unittest discover -s operating-model/scripts -p test_runtime_support.py -v
```

See [VALIDATION.md](VALIDATION.md) for package and component checks. Per-file checksums are in `manifest.json`.
