# Prompt Loop

Prompt Loop is a skill for AI agents and large language models. The agent defines completion criteria, executes a prompt, and checks the result. It revises the prompt based on the evidence and stops when the required criteria pass or a limit or dependency prevents further work.

The complete skill is in [SKILL.md](SKILL.md).

## Install

### Codex

Copy `SKILL.md` into a `prompt-loop` folder in your Codex skills directory. The default destination is `~/.codex/skills/prompt-loop/SKILL.md`. If you set `CODEX_HOME`, use its `skills` directory.

### Claude Code

Copy `SKILL.md` to the path for your preferred scope.

| Scope | Destination |
|---|---|
| Personal, across local projects | `~/.claude/skills/prompt-loop/SKILL.md` |
| One project | `.claude/skills/prompt-loop/SKILL.md` relative to the project root |

Run `/prompt-loop` with your task in Claude Code. [Claude Code skill documentation](https://code.claude.com/docs/en/skills)

### Other agents and models

Load `SKILL.md` through your agent's skill loader. If your interface accepts instructions directly, provide the file contents with your task.

## Use

Give Prompt Loop a task and any constraints or checks that define success. Use `$prompt-loop` to invoke it in Codex.

```text
Use Prompt Loop to fix the failing parser test. Preserve the public API.
Run the parser tests to verify the fix.
```

The active agent performs the work with its available tools by default. It reports the result, the evidence, and any criteria that remain unresolved.

## Default limits

- 8 execution attempts per task.
- 8 verification rounds per task.
- 3 consecutive attempts without meaningful progress.

You can supply different limits in your request.
