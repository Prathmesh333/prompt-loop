# Design Review: Pass 2

This file records the second review. See the [third design review](design-review-pass-3.md) for the latest findings against version 0.3 and corrections in version 0.4.

Review date: 6 November 2026  
Reviewed baseline: Design specification version 0.2  
Corrected specification: Version 0.3  
Review type: Follow-up requirements and workflow review by the authoring agent

## 1. Conclusion

The second review found five further issues. The most significant issue permitted execution after disclosure of an unenforceable hard budget.

Version 0.3 addresses all five findings. The corrections preserve the requested prompt improvement cycle and clarify when a new execution attempt is useful.

The proposed active-agent mode has no remaining contradiction identified by this pass. External dispatch remains an open scope decision. No skill has been implemented or tested.

The [first review](design-review.md) remains a historical record. This review does not replace that record or claim independent evaluation.

## 2. Method and limits

The review rechecked the corrected rules from the first pass. It compared the workflow diagram with the prose and examined boundary conditions at entry, continuation, and termination.

The review used document inspection and scenario walkthroughs. It did not run an executor or a skill. It did not validate the numerical defaults through representative usage.

The review also checked terminology, requirement words, and technical meaning under the user's selected Controlled Technical English skill.

## 3. Findings and corrections

Finding identifiers continue from the first review. `High` indicates a gap that can defeat an explicit execution boundary. `Medium` indicates a gap that can produce inconsistent execution or reporting.

### R11. Hard budget disclosure did not prevent prohibited execution

Severity: High  
Baseline location: Section 8, final paragraph  
Status: Corrected in specification Section 8

Version 0.2 required disclosure when the host could not enforce a hard time or cost limit. It did not require the agent to stop the affected action.

The agent could therefore disclose the limitation and start an action that exceeds the user's hard limit. An estimate would not provide an enforceable bound.

Version 0.3 requires an enforceably bounded method or a request for a feasible method or revised limit. Disclosure alone cannot authorize execution beyond the limit.

### R12. The initial flow always required candidate generation

Severity: Medium  
Baseline location: Sections 7 and 8  
Status: Corrected in specification Sections 7, 7.1, 8, and 9

Version 0.2 moved directly from task understanding to prompt construction and execution. It did not provide a path for existing work that already meets the completion criteria.

The flow could cause unnecessary changes or require an artificial execution attempt before reporting completion.

Version 0.3 inspects existing results before generating a candidate. Sufficient current evidence can support completion with zero execution attempts. Without sufficient evidence, the agent must verify or continue the task.

### R13. Continuation could select a new prompt for the wrong cause

Severity: Medium  
Baseline location: Sections 7, 7.2, and 7.3  
Status: Corrected in specification Sections 7, 7.3, and 7.4

Version 0.2 allowed another iteration when attempts remained. The diagram then required prompt revision even though the prose said to change the prompt only when the change addresses the cause.

Two cases exposed this mismatch. An unavailable verification dependency does not require a new candidate. An environment failure can require recovery while leaving the prompt unchanged.

Version 0.3 requires an identified correction or recovery before another execution attempt. An unavailable check produces the applicable incomplete outcome. Environment recovery can preserve the prompt, and the subsequent executor retry still consumes an attempt.

### R14. A contract change could leave a stale baseline

Severity: Medium  
Baseline location: Sections 6, 7.4, and 8  
Status: Corrected in specification Section 6

Version 0.2 required candidate comparison under the same contract version. It required reevaluation after a contract change but did not state how to select the retained baseline again.

The agent could retain a baseline that was no longer usable or treat the new contract version as progress that resets stagnation.

Version 0.3 selects the best candidate again under the revised contract. If no retained candidate is usable, the record states that no current baseline exists. A version change alone does not reset attempt or stagnation counters.

### R15. Source handling did not distinguish authority from evidence

Severity: Medium  
Baseline location: Sections 6 and 7.5  
Status: Corrected in specification Sections 6 and 7.5

Version 0.2 required applicable project instructions to supply criteria. It also stated that retrieved content must not change the contract. Those rules did not distinguish authorized requirement sources from ordinary task data.

The conflict rule also required a question before applying the host's instruction hierarchy. Some conflicts can be resolved directly through that hierarchy.

Version 0.3 applies source authority first. User-designated specifications can supply requirements. Ordinary retrieved content and executor output do not acquire instruction authority merely because the agent receives them.

The agent requests resolution only when a material conflict remains after applying the applicable hierarchy.

## 4. Scenario walkthroughs

These are design walkthroughs. They are not executed skill tests.

| Scenario | Decision under version 0.3 |
|---|---|
| Existing work has current evidence for every required criterion | Report `completed` with zero execution attempts |
| Existing work has no sufficient verification evidence | Perform an available check within limits before claiming completion |
| A paid action has unknown maximum cost and the user supplied a hard cost limit | Use a bounded method or request a feasible method or revised limit before the action |
| A candidate only needs unavailable user acceptance | Report `needs_input` without another candidate request |
| An environment dependency is recovered | Keep a suitable prompt unchanged and count the subsequent executor retry |
| A changed contract makes the previous baseline unusable | Reevaluate retained candidates and preserve counters |
| An applicable project instruction conflicts with a higher-priority user instruction | Apply the instruction hierarchy without an unnecessary question |
| A retrieved user-designated specification supplies an acceptance condition | Record the condition under the applicable authority and contract-change rules |
| Executor output requests additional permissions | Treat the request as output, not authorization |
| Three consecutive executor errors produce no usable candidate | Preserve the first review's result: count the attempts and report `stagnated` under the proposed defaults |
| Attempt eight satisfies the final required criterion | Preserve the first review's result: report `completed` without attempt nine |

The review retained the proposed maximum of eight execution attempts and the proposed stagnation limit of three. This pass did not add another numerical limit.

## 5. Remaining decisions and validation

The proposed executor is still the active agent. A separate model or service requires a defined destination and a dispatch integration before that mode can be implemented.

Persistent recovery across separate sessions remains outside the first-version scope. Numerical defaults remain provisional.

The revised specification includes 30 planned behavioral scenarios. None has been executed against an implemented skill.

Document checks passed for all four Markdown files. Local links resolve, code fences are balanced, and table column counts are consistent. No unfinished placeholders were found.

Specification section references resolve. A connectivity check found that all 18 declared diagram nodes are reachable from the entry node through the 21 edges. The diagram was not rendered or validated with a Mermaid parser.

The checks also confirmed 30 planned scenarios, five findings in this pass, and the absence of a `SKILL.md` file. These checks do not establish runtime behavior.

## 6. Meaning and scope check

The review preserves the original objective and sequence: understand, improve, execute, evaluate, revise, and repeat until completion.

The review preserves the earlier distinction between user requirements and proposed design decisions. The review also preserves the numerical defaults and clarifies the conditions for further execution.

The corrections concern documentation only. Skill development has not started.
