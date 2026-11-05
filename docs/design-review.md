# Design Review

This file records the first review. See the [second design review](design-review-pass-2.md) for the latest findings against version 0.2 and corrections in version 0.3.

Review date: 6 November 2026  
Reviewed baseline: Design specification version 0.1 and the project overview  
Corrected specification: Version 0.2  
Review type: Requirements and workflow review by the authoring agent

## 1. Review conclusion

Version 0.1 described the intended cycle but left several execution rules undefined. Those gaps could cause premature completion, unnecessary retries, or incorrect final reports.

Version 0.2 addresses the findings below. The documentation is ready for implementation of the proposed active-agent execution mode. This conclusion does not establish that the skill works. No skill has been implemented or executed.

The meaning of external prompt dispatch remains a product decision. Section 4 records the current assumption and its effect on implementation.

## 2. Review method

The review compared the documents with the user's requested sequence. The review then examined each workflow transition, completion decision, retry condition, and final result.

The review covered these areas:

- Preservation of the original task and constraints.
- Execution prompt visibility and executor identity.
- Required criteria, optional preferences, and verification evidence.
- Attempt accounting, stagnation, and limits.
- User input, authorization, cancellation, and continuation.
- Candidate selection, current artifact state, and evidence validity.
- Skill discovery, context retention, and behavioral validation.
- Terminology and requirement words under the selected Controlled Technical English skill.

The review used document inspection and scenario walkthroughs. It did not use an independent reviewer, external model, or implemented executor.

## 3. Findings and corrections

Severity describes the expected effect on this workflow. `High` means the gap can invalidate task completion or defeat an execution boundary. `Medium` means the gap can produce inconsistent execution or reporting.

### R01. Task contract changes could weaken requirements

Severity: High  
Baseline location: Section 6  
Status: Corrected in specification Sections 6 and 7.5

Version 0.1 permitted a contract change through a "stated correction based on new evidence." That rule did not distinguish factual assumptions from user requirements.

An executor could discover that a requirement is difficult, remove the requirement, and then report success against the weaker contract.

Version 0.2 preserves user requirements. New evidence can correct an assumption, but it cannot authorize removal of a requirement. Contract changes have versions, sources, and stated effects.

### R02. Failed attempts could bypass the execution limit

Severity: High  
Baseline location: Section 8, maximum iterations  
Status: Corrected in specification Sections 3, 7.3, and 8

Version 0.1 counted attempts that "reach evaluation." Timeouts, dispatch failures, and unusable output had no explicit counting rule.

Repeated executor failures could therefore continue without reaching the configured attempt limit.

Version 0.2 counts every started attempt. The specification separates candidate generation from checks of an existing result. The specification also defines baseline and stagnation accounting.

### R03. The workflow omitted checks before the first attempt

Severity: High  
Baseline location: Section 7, workflow diagram  
Status: Corrected in specification Sections 7 and 8

The diagram went directly from prompt construction to execution. The prose required a limit check before each attempt, but the diagram showed a continuation decision only after evaluation.

Version 0.2 places an execution gate before the first attempt and each repeat attempt. Verification and recovery also remain subject to supplied time and cost limits.

### R04. Evidence was not tied to the evaluated artifact

Severity: High  
Baseline location: Sections 7.4 and 9  
Status: Corrected in specification Sections 6, 7.4, and 9

Version 0.1 required evidence but did not define when that evidence expires. A check of an earlier artifact could be reported as evidence for a changed artifact.

Version 0.2 links findings to criterion identifiers, contract versions, and candidate references. Changes require rechecking affected criteria.

### R05. Missing evidence could cause unnecessary regeneration

Severity: Medium  
Baseline location: Sections 7 and 7.4  
Status: Corrected in specification Sections 7 and 8

The original flow sent every incomplete evaluation toward another prompt revision. It did not distinguish a defective candidate from a candidate that still needed verification.

Version 0.2 adds a path for checking an existing result. A missing check alone does not require another candidate or consume another execution attempt. An unchanged check that produces no new evidence cannot repeat against unchanged state.

Version 0.2 also distinguishes required criteria from optional preferences. Optional preferences cannot prevent completion after all required criteria pass.

### R06. Best-candidate selection and restoration were undefined

Severity: Medium  
Baseline location: Sections 3, 7.4, and 9  
Status: Corrected in specification Section 7.4

Version 0.1 required the agent to retain the best candidate without defining a comparison rule. It also did not distinguish a retained artifact reference from the current working state.

Version 0.2 compares candidates under the same contract. A candidate must preserve verified required behavior while making meaningful improvement on a required gap to be clearly better.

When a previous candidate is selected, the agent must inspect the current state. The agent cannot claim restoration without verifying the resulting state.

### R07. Waiting and continuation rules were incomplete

Severity: Medium  
Baseline location: Sections 7, 8, and 9  
Status: Corrected in specification Sections 6, 7.3, 8, and 9

The diagram returned directly from a request for information to contract construction. The specification did not explicitly require a response before dependent work.

Version 0.2 requires the agent to wait for required input or authorization. Continuation preserves counters and checks current state. A task change does not silently reset limits.

The corrected specification also states that cancellation stops further actions. Success on the final permitted attempt remains a completed result.

### R08. External-action recovery lacked an uncertain-state rule

Severity: Medium  
Baseline location: Section 7.3  
Status: Corrected in specification Sections 7.3 and 8

Version 0.1 required current-state inspection before a repeated external action. It did not state what to do when inspection cannot establish whether the action occurred.

Version 0.2 stops the repeat attempt when the state remains uncertain. An error response is not proof that an external action had no effect.

This correction preserves existing authorization boundaries. It does not require new approval for ordinary reversible work that is already authorized.

### R09. Execution prompts and dispatch semantics were underspecified

Severity: Medium  
Baseline location: Sections 5 and 9  
Status: Clarified for the proposed first version. External dispatch remains open.

Version 0.1 selected the active agent as executor but did not require a distinct execution prompt record. Ordinary internal planning could therefore be described as prompt dispatch without an identifiable prompt.

Version 0.2 defines an execution prompt as an explicit instruction artifact. The record must identify the objective, correction, constraints, and expected output.

The corrected specification states that this mode does not guarantee a separate model invocation or a continuously running process.

### R10. Discovery and validation boundaries were incomplete

Severity: Medium  
Baseline location: Sections 4 and 11  
Status: Corrected in specification Sections 4, 9, and 11

Version 0.1 did not distinguish this cycle from a request to rewrite a prompt once. It also listed validation scenarios without specifying the evidence needed to claim behavioral validation.

Version 0.2 limits discovery to requests for repeated execution and evaluation. A prompt-only request does not start execution.

Behavioral validation now requires an actual request, observed execution, criterion evidence, and stated limitations. The specification also defines the minimum record needed when context is shortened.

## 4. Remaining decisions

These items are design choices rather than unresolved contradictions in version 0.2.

| Decision | Current proposal | Effect |
|---|---|---|
| Meaning of prompt dispatch | Execute through the active agent | A separate model endpoint or destination is not part of the first version |
| Numerical limits | Eight attempts and three consecutive attempts without improvement | Defaults remain provisional until representative use provides evidence |
| Persistent record | Retain a compact record in host context | Recovery across separate sessions is not guaranteed |
| Skill name | `iterative-task-completion` | Name remains a proposal until the skill is created |

If the user requires an external executor, the design must identify that executor before implementing its dispatch integration. That requirement would change the current first-version scope.

## 5. Scenario walkthroughs

These walkthroughs checked the corrected rules. They are design checks, not executed behavior tests.

| Scenario | Expected decision under version 0.2 |
|---|---|
| The first candidate passes every required criterion | Report `completed` after one attempt |
| The candidate needs a missing check | Check the same candidate within available limits |
| Three consecutive executor errors occur before a usable candidate exists | Count all three attempts and report `stagnated` under the proposed defaults |
| The baseline is followed by three attempts without improvement | Keep the baseline reference and report `stagnated` |
| Attempt eight resolves the last required failure | Report `completed` without attempt nine |
| A supplied limit prevents the first attempt | Report `limit_reached` without dispatch |
| A later edit changes a verified artifact | Recheck affected criteria before a completion claim |
| A required user decision is pending | Report `needs_input` and wait for the response |
| A response to an external action is unclear and current state is unavailable | Stop the repeat attempt and report the uncertainty |
| A user requirement conflicts with the executor output | Preserve the requirement and evaluate the output as evidence |

Document checks passed for all three Markdown files. Local links and specification section references resolve. Code fences are balanced, and no unfinished placeholders were found.

The revised specification contains 24 planned validation scenarios. Those scenarios remain implementation work and have not been executed.

## 6. Language and meaning review

The review used the user's requested sequence as the source requirement. The review used the selected Controlled Technical English skill for terminology and modal meaning.

The corrected specification preserves the sequence, objective, and completion goal. New conditions and accounting rules are identified as design proposals.

The review preserved the proposed values of eight maximum attempts and three consecutive attempts without improvement. The review clarified which events count toward those values.

The specification uses one defined term for each main concept. Requirements, recommendations, permissions, and capabilities use distinct modal words.

No user-supplied units, tolerances, or safety classifications required preservation. No claim of external controlled-language compliance is made.

## 7. Implementation readiness

The next work is to translate version 0.2 into concise skill instructions. The implementation should retain the task contract, evidence rules, execution boundaries, and stop conditions.

Structural checks and behavioral checks remain separate. The developer must exercise representative tasks before describing the skill as behaviorally validated.

This review completes the documentation stage requested in the current task. Skill development has not started.
