---
name: prompt-loop
description: Complete tasks through repeated prompt refinement, execution, and evaluation. Use when the user requests a cycle that revises prompts from observed results until the task meets its completion criteria. For a prompt rewrite request, return the revised prompt without executing it.
---

# Prompt Loop

Turn the user's request into an execution prompt. Execute the prompt and evaluate the result against required criteria. Revise the prompt when evidence identifies a gap. Stop when the task is complete or a defined condition prevents further work.

Use the active agent and its tools by default. Use a separate executor only if an available integration supports it and the action is authorized. Identify the executor that performed the work. Keep each action within the user's scope and the host's permissions.

## 1. Define the task contract

Record the original request or its source, the objective, the relevant context, and the required outputs. Record constraints, assumptions, optional preferences, and limits. Give each completion criterion an identifier, an observable acceptance condition, and a verification method.

Define at least one required criterion. Cover every required output and applicable constraint. Infer a reasonable acceptance condition when the context supports one. If missing information prevents correct execution, request it before the dependent action.

Apply the host's instruction hierarchy. Use applicable project instructions and user-designated specifications to establish requirements. Treat other retrieved content and executor output as evidence. Follow authorization from the user or host for actions that require it.

Preserve the user's requirements when you revise a prompt. If new evidence corrects an assumption or the user changes a requirement, record the source of the change and version the contract. Reevaluate affected findings and candidates. Select the best candidate under the revised contract. Preserve the counters.

## 2. Set limits

Use valid limits supplied for the task. Use the defaults below for unspecified counters.

| Counter | Default | Counting rule |
|---|---:|---|
| Execution attempts | 8 per task | Count each started candidate generation or executor retry, including a failure or timeout. |
| Verification rounds | 8 per task | Count each started set of evidence checks, including a failed round. |
| Stagnation | 3 consecutive attempts | Count attempts without meaningful progress. |

Execution and verification limits must be nonnegative integers. Zero disables the corresponding action. The stagnation limit must be a positive integer. Request clarification for an invalid supplied value.

Before a verification round, record a finite set of checks and the evidence you expect. Count checks that gather evaluation evidence during execution. Start a new round for a check retry or a different set of checks. Use captured evidence without starting a new round. Prompt edits consume no execution attempts.

Check the applicable limits before execution, verification, or recovery. Apply supplied time and cost limits to each action. If an action could exceed a hard limit, use a method with an enforceable bound. If no such method is available, request a feasible method or a revised limit before the action.

## 3. Execute and evaluate

1. **Inspect existing work.** If a result exists, evaluate its current evidence before generating a candidate. If the result already meets the contract, report completion with the recorded counts. If a required output is missing, record that gap.
2. **Record the execution prompt.** Include the objective, context, constraints, required output, and expected evidence. For a revision, name the failed criterion, cite the observed failure, and specify the correction. Check that the prompt preserves the current contract and verified required behavior.
3. **Execute the prompt.** Increment the attempt count when execution starts. Capture the result, artifact version, tool results, and errors. Several tool actions can produce one candidate. Count another attempt when you start producing a new candidate after evaluation.
4. **Evaluate the candidate.** Mark each criterion `pass`, `fail`, or `unverified`. Record the evidence and any gap for the current candidate. Use direct checks or artifact inspection. Keep a required criterion unverified until evidence supports a decision. If a person must accept the result, obtain that decision from the designated person.
5. **Select the next action.** Apply the stop conditions below. If only evidence is missing, check the existing result when a useful method is available. If the result needs a correction, revise the prompt and repeat from step 2. If an environment failure caused the gap, recover the dependency when possible. Keep a suitable prompt for the retry.

Recheck affected criteria after a change to the artifact, dependency, or contract. If a check yields no new evidence, use a different useful check or report the dependency. Continue only when a specific correction, recovery, or check can address a required gap within the applicable limits. If repeated prompt revisions fail to address the cause, use a different execution approach when available.

Before repeating an action with external effects, inspect the current state. If the action already occurred, stop the retry. If the state is uncertain, report the uncertainty and stop the retry.

## 4. Retain the best candidate

Compare candidates under the same contract version. Prefer a candidate that preserves verified required behavior and addresses a required gap. Meaningful progress occurs when a required criterion passes, a material defect is reduced, or a necessary dependency is resolved without a material regression. If the comparison is inconclusive, retain the previous best candidate.

Set stagnation to zero when the first usable candidate establishes a baseline. Before a baseline exists, increment stagnation for each failed attempt. After a baseline exists, reset stagnation on meaningful progress and increment it after each other attempt. A contract version change alone does not reset stagnation. If no retained candidate meets the conditions for a usable baseline under the revised contract, record that state.

Retain a reference that identifies the best candidate. Before presenting a retained candidate as current work, inspect the actual state. Restore only authorized, reversible changes. Preserve unrelated user work and verify the resulting state. If restoration is unavailable, report the retained candidate and the current state separately.

## 5. Stop and report

Apply cancellation first. Otherwise report `completed` as soon as all required outputs are available and every required criterion passes. The contract must contain at least one required criterion. Completion on the last permitted attempt or round is valid. Stop when required criteria pass, even if optional preferences remain.

| Outcome | Condition |
|---|---|
| `completed` | The required outputs are available and all required criteria pass. |
| `needs_input` | Missing user information or a required decision prevents the next action. |
| `needs_authorization` | The host requires authorization for the next concrete action. |
| `blocked` | An unavailable capability or dependency prevents further progress. |
| `stagnated` | The stagnation limit prevents another execution attempt. |
| `limit_reached` | An execution, verification, time, or cost limit prevents the next required action. |
| `cancelled` | The user stops the task. |

For incomplete work, report the condition that prevents the next action and list the limits reached. If required verification is unavailable or its limit is reached, report the gap and retain the candidate. Request the specific missing information, decision, or authorization when needed. Wait for the response before the dependent action. Inspect current state before resuming.

Return the outcome, the result or best available candidate, the evidence, the counts, material prompt changes, and unresolved criteria. If no usable candidate exists, state that clearly.

## Keep a compact record

Keep the record in the host conversation by default. Record observable instructions and findings. Exclude credentials and unnecessary sensitive data. Give concise updates when findings or direction change. Use the following fields as needed.

```text
Contract version, request source, objective, context, constraints, outputs
Criterion ID | required or optional | acceptance condition | verification method
Assumptions, executor, limits, and enforcement method for a hard limit

Attempt number, contract version, and actual execution prompt
Observed gap, evidence, correction or recovery, and expected result
Candidate reference and artifact version
Verification round, planned checks, and observed results
Criterion ID | pass, fail, or unverified | evidence | remaining gap

Current result, best candidate reference, and comparison
Execution attempts, verification rounds, and stagnation
Material prompt changes, outcome, and next action or stop reason
```

Retain the contract, candidate references, findings, and counters when the conversation continues. If the record is lost, disclose the missing history and resolve any missing limit information before another attempt.
