# Prompt Loop

This project defines a reusable agent skill for iterative task completion. The agent understands a task, improves the execution prompt, executes the prompt, evaluates the output, and repeats the cycle until the task meets its completion criteria.

**Project status:** The initial skill is implemented and installed. Structural validation and three controlled active-agent exercises are complete. External execution integrations are not implemented.

## Install

Copy the `skills/prompt-loop` directory into your Codex skills directory, normally `~/.codex/skills`. If `CODEX_HOME` is configured, use its `skills` directory.

The package contains the skill instructions, interface metadata, and record template. Keep all three files together.

## Use the skill

Invoke `$prompt-loop` with the task to complete. For example:

```text
Use $prompt-loop to repair this function. Refine the execution
prompt from observed failures and continue until the required checks pass.
```

The editable [source package](skills/prompt-loop/SKILL.md) is retained in this repository. When updating an installation, copy the complete package from this source.

The skill uses the active agent and available tools. It records prompts, evaluates results against required criteria, and stops at completion or a defined limit. It does not create a separate model process.

## Project records

Read the [design specification](docs/design-specification.md) for the requirements, workflow, proposed defaults, and validation plan.

Read the [five pre-development checks](docs/pre-development-checks.md) for the final review before implementation. The [first review](docs/design-review.md), [second review](docs/design-review-pass-2.md), and [third review](docs/design-review-pass-3.md) record the earlier passes.

Read [implementation and validation](docs/implementation-validation.md) for executed checks and limitations. The [exercise record](validation/exercise-record.md) includes the corrective prompt and raw evidence. The full set of 34 planned behavioral scenarios has not been executed.
