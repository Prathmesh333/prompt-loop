# Design Review: Pass 3

Review date: 6 November 2026  
Reviewed baseline: Design specification version 0.3  
Corrected specification: Version 0.4  
Review type: Follow-up requirements and workflow review by the authoring agent

## 1. Conclusion

This review found two further defects in the specification. Both affect decisions that control continuation or completion. Version 0.4 addresses both defects.

The review did not identify another confirmed documentation defect. This result does not prove reliable execution. The skill has not been implemented or tested.

The [first review](design-review.md) and [second review](design-review-pass-2.md) remain historical records. This pass was not an independent review.

## 2. Method

The review examined completion conditions, candidate comparison, counter updates, and continuation paths. The review compared the workflow diagram with the prose and checked the previous corrections for conflicts.

The review used two counterexamples. The first supplied no required criteria. The second repeated unsuccessful verification through different methods without starting another execution attempt.

The review also rechecked the rules for zero-attempt completion, contract changes, final-attempt success, unavailable verification, and user responses.

These checks were document walkthroughs. They were not executions of a skill or model integration.

## 3. Findings and corrections

Finding identifiers continue from the previous reviews. Both findings have medium severity because the undefined behavior can cause inconsistent continuation or completion.

### R16. Completion did not explicitly require a valid criteria list

Severity: Medium  
Baseline location: Sections 6, 7, and 8  
Status: Corrected in specification Sections 6, 7, and 8

Version 0.3 required a task contract and checked whether all required criteria passed. It did not explicitly reject an empty list or a list containing only optional preferences.

An implementation could therefore interpret the absence of failed criteria as successful completion. The same gap could leave a required output outside the completion checks.

Version 0.4 requires at least one required criterion. Required criteria must cover all required outputs and applicable constraints. An empty list requires contract correction or missing user information, not a completion claim.

### R17. Verification could bypass the execution-attempt limit

Severity: Medium  
Baseline location: Sections 7.4, 8, and 9  
Status: Corrected in specification Sections 3, 6, 7, 8, and 9

Version 0.3 counted new candidate requests and executor retries. It correctly excluded checks of an existing result from that count.

However, the verification path had no separate bound when the user supplied no time or cost limit. Repeatedly selecting different verification methods could continue without consuming an execution attempt or incrementing the stagnation count.

Version 0.4 introduces a verification round. Each round has a finite planned set of checks and expected evidence. Failed rounds count. Retries and newly selected check sets require another permitted round.

The proposed default is eight verification rounds per task. This is a new design proposal, not a user-supplied requirement or a validated performance threshold.

The verification counter persists across candidate changes, contract revisions, and continuation in the same task. Reviewing evidence already captured does not consume another round. Completion on the final permitted round remains valid.

## 4. Scenario walkthroughs

| Scenario | Decision under version 0.4 |
|---|---|
| The contract has no required criteria | Correct the contract or request missing information; do not report completion |
| The contract contains only optional preferences | Establish required criteria from the request before evaluating completion |
| A required output is missing while other checks pass | Keep the output requirement unresolved |
| Verification switches repeatedly between unsuccessful methods | Count the rounds and stop at the applicable limit or an earlier identified dependency |
| A check fails before returning evidence | Count the started round |
| A candidate changes after earlier verification rounds | Preserve the total verification-round count and invalidate affected evidence |
| A contract version changes | Preserve both execution and verification counts |
| The last permitted round supplies sufficient evidence | Report completion after reviewing that evidence |
| No useful verification method is available | Report the dependency without using all remaining rounds |
| Existing evidence already establishes completion | Report zero-attempt completion without another evidence-gathering round |

These walkthroughs check the design rules. They do not establish skill behavior.

## 5. Remaining limits and decisions

The execution mode remains the active agent in the host environment. External prompt dispatch still requires a defined destination and integration.

The proposed numerical limits now include eight execution attempts, three consecutive attempts without improvement, and eight verification rounds. Representative usage must validate these defaults.

The revised specification contains 34 planned behavioral scenarios. None has been executed against an implemented skill.

Document checks passed for all five Markdown files. Local links and specification section references resolve. Code fences are balanced, table column counts are consistent, and no unfinished placeholders were found.

A connectivity check confirmed that all 18 declared diagram nodes are reachable through the 21 edges. The diagram was not rendered or checked with a Mermaid parser. These document checks do not establish runtime behavior.

The review continues to use the user's selected Controlled Technical English skill. The corrections preserve the original objective and sequence. The verification limit is explicitly identified as a new proposal.

Skill development has not started.
