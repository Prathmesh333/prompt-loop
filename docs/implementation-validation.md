# Implementation and Validation

Date: 6 November 2026  
Skill version: Initial implementation against design specification 0.5

## Implemented scope

The skill supplies instructions for task contracts, prompt construction, active-agent execution, candidate evaluation, targeted prompt revision, and defined stop conditions.

The package contains three files:

- [SKILL.md](../skills/prompt-loop/SKILL.md): Discovery description and execution instructions.
- [openai.yaml](../skills/prompt-loop/agents/openai.yaml): Skill interface metadata and example invocation.
- [record-template.md](../skills/prompt-loop/references/record-template.md): Compact prompt, evaluation, and continuation records.

The package does not contain an autonomous runtime or a separate model integration. Counters and stop decisions are instructions followed by the host agent. Automatic discovery uses the host's normal skill discovery behavior.

## Pre-development review

The [five pre-development checks](pre-development-checks.md) were completed before skill initialization. The checks covered requirements, counters, workflow transitions, evidence, and implementation readiness.

One correction clarified valid counter ranges. The remaining four checks found no additional confirmed defect.

## Structural validation

The skill-creator `quick_validate.py` validator passed for the project source. The validator checks skill structure and frontmatter. It does not establish successful task completion.

Additional checks cover metadata parsing, the invocation reference, local document links, table structure, code fences, package references, and source-to-installed file hashes.

The installed package is `C:\Users\chu\.codex\skills\prompt-loop`. The project retains the editable source. All three installed files matched the source by SHA-256 comparison after installation. Later source edits require synchronization before the installed copy can reflect those edits.

The user selected **Prompt Loop** after the initial implementation. The package was renamed from `iterative-task-completion` to `prompt-loop`, including its identifier, interface name, invocation prompt, and directories. Historical review names and temporary exercise paths remain records of the original validation.

The skill-creator validator also passed for the installed copy. Final checks passed for all ten project Markdown files, metadata, local links, section references, code fences, and table column counts. All four JSON evidence reports matched the actual candidate hashes and recorded check totals.

## Executed exercises

The [exercise record](../validation/exercise-record.md) contains the task contract, corrective prompt, expected evidence, actual results, counters, and outcomes.

| Exercise | Result | Scope of evidence |
|---|---|---|
| Repair a seeded Python defect | Corrected artifact passed all eight acceptance checks | One corrective execution attempt and two verification rounds |
| Inspect already completed work | Existing artifact passed all eight acceptance checks | Zero execution attempts and one verification round |
| Stop with execution limit zero | Defective input remained incomplete; no correction was generated | Zero execution attempts and one verification round |

The [candidate checker](../validation/check_candidate.py) evaluates order, equality-based duplicate removal, unhashable input, mixed input, preservation of input, and retained object identity. It loads only local controlled exercise modules in these exercises.

The checker does not independently evaluate the agent's prompt quality, counters, or outcome selection. The authoring agent executed and evaluated these exercises. No separate reviewer or model was used.

## Reproduction

Use Python to run `validation/check_candidate.py` with a candidate module path and `--report` followed by a JSON output path. A successful candidate returns exit code zero. An acceptance failure returns exit code one and records individual results.

The supplied `validation/fixtures/dedupe_seed.py` is deliberately defective. Its failure is an expected exercise input. Python set ordering can change the seed's passing total between processes. It must not be used as a passing reference.

The corrected candidate was generated in an isolated temporary directory. Its location and content hash are recorded in the reports. Temporary files can be removed by system cleanup.

For repository reproduction, an identical copy is preserved as [dedupe_corrected.py](../validation/fixtures/dedupe_corrected.py). Its SHA-256 hash matches the original corrected candidate. The original evidence reports retain their capture paths and results.

From the repository root, run:

```text
python validation/check_candidate.py validation/fixtures/dedupe_corrected.py --report validation/local-reports/corrected.json
```

## Remaining validation

The specification contains 34 planned scenarios. The exercises provide limited evidence for correction, completion from existing work, and a zero execution limit. They do not establish that all 34 scenarios pass.

External dispatch, independent evaluation, multi-session recovery, repeated generated failures, and external-action recovery were not exercised. The numerical defaults remain provisional.
