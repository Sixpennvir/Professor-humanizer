# Validation report

Date: 2026-10-14. Version: 0.4.0. Local tooling: Windows, Python 3.12.13.

## Executed tooling checks

| Check | Result | Scope |
| --- | --- | --- |
| Showcase consistency | Passed | README and gallery match the authored example source |
| Repository validation | Passed | Required files, links, IDs, metadata and selected example anchors |
| Python regression suite | 19 passed | Malformed fixtures, protected anchors, packaging exclusions and reproducibility |
| Skill-creator format validation | Passed with UTF-8 mode | Skill metadata and entrypoint format |
| Skill ZIP generation | Passed | Versioned archive and SHA-256 companion file |
| Extracted package validation | Passed within the regression suite | Runtime references remain available without development files |
| Evaluation record integrity | Passed | Complete case coverage, exact task inputs, recorded response provenance, checkpoint guidance and reviewer criteria |

The archive includes the long-form teaching example. A passing structural check cannot establish semantic fidelity or writing quality.

## Version 0.4.0 behavioral evaluation

The [complete record](runs/v0.4.0-behavioral.json) contains 51 actual model responses for 48 distinct inputs. Generation agents received staged guidance and task inputs without expected answers. Review agents assessed each response against its input, applicable guidance and expected invariants.

| Checkpoint | Actual responses | Review result |
| --- | --- | --- |
| A: initial guidance | 44 | 41 cases passed; one long-form repetition remained and two cases failed overly prescriptive criteria |
| B: paragraph-ending check | 4 | All four passed, including the repeated long argument and a new supported participial revision |
| C: corrected judgment examples | 3 | Two passed all literal criteria; the quotation response exposed an overly restrictive clarification criterion |

The initial long-form failure concerned one redundant closing sentence. The revised workflow added a paragraph-ending deletion test. A new generation session then produced a revision that passed all seven invariants. Both responses and reviews remain available.

The two initial criterion failures concerned a mandatory authorization question and an explicit sentence-frame diagnosis. The actual responses had preserved the commitment and the unsupported judgments. The corrected criteria accept an adequate explanation of the limit and allow clarification to focus on the substantive blocker. Their focused follow-up passed.

At checkpoint C, the quotation response supplied a warrant through a conditional reading of the quoted scope. The reviewer found that inference consistent with R04 and the supplied evidence. The original criterion had required a question or an explicit support gap even when the evidence allowed a faithful repair. The record retains that literal failure and the corrected criterion; no further generation followed this criterion correction.

Three long-form inputs cover an academic argument, a decision memo and the original course inquiry. Initial review found no lost substantive judgment, qualification or objection in those responses. The decision memo retained its conditions and requested headings. The course inquiry retained meaningful questions, parallel reasoning and its open ending. These findings describe the observed sample.

## Scope and limitations

Each long-form input used an isolated generation session. Short inputs shared context within their recorded batch. Checkpoint A covered the initial 44 cases; B covered four inputs; C covered three. The final guidance has not received a complete 48-case rerun.

Inputs were authored for development, and some closely follow the worked examples. Separate AI agents conducted the reviews. No human evaluation, baseline comparison, repeated-sampling study, community survey or cross-host comparison took place. The host did not expose model identifiers or generation settings.

A passing clarification does not demonstrate a completed revision. One initial review also noted stiff wording in the unknown-actor verb exercise. The record supplies no overall readability gain or comparative quality estimate.

The earlier [version 0.2.0 smoke check](runs/long-form-smoke.json) remains unchanged under the project name used for that run. Its original limitations continue to apply to that single response.
