# Compact Cycle Record

Use this format in host context. Write a durable file only when requested or useful within the authorized task. The record contains observable instructions and findings, not private reasoning.

## Task contract

```text
Contract version:
Original request or source reference:
Objective:
Context:
Constraints:
Required outputs:
Assumptions:
Executor: active agent, unless another authorized executor is actually used
Limits: execution attempts 8; verification rounds 8; stagnation 3
Supplied time or cost limits and enforcement method:

Criterion | Required or optional | Acceptance condition | Verification method
```

Replace the default limits when the task supplies valid alternatives. Include at least one required criterion. Cover every required output and applicable constraint.

## Execution prompt

```text
Attempt number and contract version:
Objective:
Relevant context and candidate reference:
Constraints to preserve:
Required output:
Observed gaps and criterion identifiers:
Specific correction or recovery:
Evidence expected after execution:
```

For the first attempt, describe the required result instead of inventing a prior failure. Record the actual prompt before execution. A recovery can retain a suitable prompt unchanged.

## Candidate evaluation

```text
Candidate reference and version:
Started execution attempts:
Started verification rounds:
Consecutive attempts without improvement:

Planned verification round:
Finite checks and expected evidence:
Observed check results or errors:

Criterion | pass, fail, or unverified | Evidence reference | Remaining gap

Best candidate reference:
Comparison with previous best:
Material prompt revision:
Current outcome:
Next action or stop reason:
```

Do not create an execution entry for verification-only work. Do not reset counters on candidate changes, contract changes, or conversation continuation.

## Final report or context checkpoint

```text
Contract version and current outcome:
Current result and artifact references:
Best candidate reference, if different:
Required criteria and evidence:
Unresolved criteria or invalidated evidence:
Execution attempts / limit:
Verification rounds / limit:
Stagnation / limit:
Material prompt changes:
Next action or condition needed to resume:
```

When returning a previous best candidate, distinguish its retained reference from current files. State whether the candidate was actually restored and verified.
