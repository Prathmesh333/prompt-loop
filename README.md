# Prompt Loop

Prompt Loop is a Codex skill that revises an execution prompt based on the results of each attempt. The agent defines completion criteria, executes the prompt, and checks the result against those criteria. It stops when the required criteria pass or a limit or dependency prevents further work.

The complete skill is in [SKILL.md](SKILL.md).

## Install

Copy `SKILL.md` into a `prompt-loop` folder in your Codex skills directory. The default destination is `~/.codex/skills/prompt-loop/SKILL.md`. If you set `CODEX_HOME`, use its `skills` directory.

## Use

Invoke `$prompt-loop` with a task and any constraints or checks that define success.

```text
Use $prompt-loop to fix the failing parser test. Preserve the public API.
Run the parser tests to verify the fix.
```

The active agent performs the work with its available tools by default. It reports the result, the evidence, and any criteria that remain unresolved.

## Default limits

- 8 execution attempts per task.
- 8 verification rounds per task.
- 3 consecutive attempts without meaningful progress.

You can supply different limits in your request.
