# operating-model

A skill for persistent chat coordination. The user communicates only with the main chat, which assigns, collects and adjusts work. Employee chats retain their identities and context. Use it for tasks with multiple substantive requirements, independent deliverables and review needs.

## Core rules

- Dispatch only when a task has at least three substantive requirements and a worthwhile division of work. Handle ordinary small tasks in the main chat.
- Activate research, design, engineering, visual/media and review responsibilities as needed. Reuse the minimum staff.
- Escalate major decisions, formal design reviews and any formal FAIL to the user. Freeze only affected scope.
- Form reports immediately for major issues and completed work. Batch three small issues within the same task; coordinate real blockers earlier.
- Employees save artifacts and the main chat collects them. Instance settings govern communication, budgets, models, deadlines and recovery.
- Present user choices in the main chat's message body. Available question cards and native notifications support that exchange.

## Usage

Place the complete `operating-model` directory in your host's Skills directory, preserving its internal paths. Invoke `$operating-model` in the main chat and describe the task.

Copy the [instance template](operating-model/assets/instance.template.json) into the project workspace. Configure model choices, chat bindings, budgets and runtime parameters as needed. Null values mean unconfigured. Skill files and templates do not authorize chat creation, message sending or budget increases.

The host must supply persistent chats, official read/wait tools and project state storage. Active return messages, background wakeups and notifications depend on host capabilities and valid authorization. Default operation uses one device; verify cross-device operation and application recovery separately when the project requires them.

Start with [SKILL.md](operating-model/SKILL.md); read files under `references/` only for the relevant action. The helpers use the Python 3.9+ standard library for model-choice resolution, report verification and deduplication. They do not include a chat scheduler.

## Validation

Run component tests:

```sh
python -B -m unittest discover -s operating-model/scripts -p test_runtime_support.py -v
```

See [VALIDATION.md](VALIDATION.md) for package and component checks. Per-file checksums are in `manifest.json`.
