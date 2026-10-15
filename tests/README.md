# Evaluation

This project distinguishes authored demonstrations, automated tooling checks, and actual model evaluation. The project has conducted no community survey, user interview, or user study.

## Authored examples

[Seven showcases](../references/examples.md) demonstrate the intended behavior using original fictional inputs. Each revision draws its factual content from the displayed draft. The project authored these examples for teaching.

[showcases.json](../examples/showcases.json) supplies the README and gallery. The generator checks protected literal anchors and quantities. These checks cannot determine whether the revised inference remains faithful.

The [long-form example](../references/long-form-example.md) follows a complete argument through its objection and conditional conclusion. Its preservation review explains a local expansion of the reasoning.

## Automated tooling checks

Run the commands in [development](../docs/development.md). The regression suite deliberately breaks fixtures to exercise quotation anchors, numbers, document synchronization, metadata, links, packaging exclusions and reproducibility.

One test deliberately changes an inference while preserving all literal anchors. The mechanical checker passes that fixture. That test records a known limit: semantic review must catch the changed claim.

The validator does not award a writing-quality score. Passing these tests does not show that an agent follows the skill.

## Behavioral protocol

The [48 cases](cases.json) contain prompts and expected invariants. For an isolated evaluation, use a fresh agent session with the installed skill and provide only the input. Keep expected invariants out of the generation prompt. If cases share a session, report that grouping.

Record the host, available model identifier, skill version, date, full input and complete response. A reviewer then checks each expected invariant against the actual response and supplied evidence. Mark pass, fail, or blocked and explain the reason. A clarification can pass a case that requires one. Preserve failed responses and the original criteria when a development run leads to a correction.

Review in this order:

1. **Fidelity:** no added or lost fact, changed commitment, altered attribution or damaged quotation.
2. **Argument:** interpretation follows from supplied evidence and each paragraph contributes.
3. **Strict compliance:** resolve mandatory bans without silent exceptions.
4. **Readability:** the intended reader can follow the reference and the relationship between claims.

A fluent response that changes meaning fails. A matched phrase alone cannot establish a violation of a use-dependent rule.

For comparative claims, preserve actual baseline and skill-enabled runs under comparable conditions. Report the sample, failures and limitations. Do not substitute a model's self-rating, word-count reduction or invented community feedback for this record.

## Recorded runs

The [version 0.4.0 development evaluation](runs/v0.4.0-behavioral.json) contains 51 actual responses covering all 48 current inputs across three guidance checkpoints. Three long-form inputs exercise an academic argument, a decision memo, and the original course inquiry. Separate review agents compared the responses with their inputs and expected invariants.

The initial 44-input run produced one residual long-form repetition and two failures against overly prescriptive test criteria. The project retained those responses and reviews, strengthened the paragraph-ending check, and revised the two criteria with recorded reasons. A focused follow-up covered those cases plus a supported participial revision. A subsequent example audit corrected three remaining demonstrations of judgment deletion and added three corresponding cases. One of those responses exposed another overly restrictive criterion: the supplied evidence allowed a faithful warrant, while the criterion demanded clarification. The record preserves that literal failure and the criterion correction.

These runs used fresh-context Codex agents. Each long-form input had its own generation session; short inputs shared a session within their recorded batch. The final guidance received focused checks rather than a full rerun of every input. Reviewers were AI agents, and the host exposed no model identifiers or generation settings. There was no baseline, independent human evaluation, community study, or cross-host comparison. This record supports inspection of the observed responses; it supplies no comparative improvement estimate.

The earlier [long-form smoke check](runs/long-form-smoke.json), run with version 0.2.0 under the Better AI Writer name, remains unchanged. The [validation report](validation-report.md) summarizes executed checks and remaining gaps.
