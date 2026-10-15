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

The [36 cases](cases.json) contain realistic prompts and expected invariants. To run a case, use a fresh agent session with the installed skill and provide only its input. Keep expected invariants out of the model prompt.

Record the host, model identifier, skill version, date, full input and complete response. A reviewer then checks each expected invariant against the actual response and the supplied evidence. Mark pass, fail, or blocked and explain the reason with a rule ID. A clarification can pass a case that requires one.

Review in this order:

1. **Fidelity:** no added or lost fact, changed commitment, altered attribution or damaged quotation.
2. **Argument:** interpretation follows from supplied evidence and each paragraph contributes.
3. **Strict compliance:** resolve mandatory bans without silent exceptions.
4. **Readability:** the intended reader can follow the reference and the relationship between claims.

A fluent response that changes meaning fails. A matched phrase alone cannot establish a violation of a use-dependent rule.

For comparative claims, preserve actual baseline and skill-enabled runs under comparable conditions. Report the sample, failures and limitations. Do not substitute a model's self-rating, word-count reduction or invented community feedback for this record.

## Current status

The project has not completed the full 36-case behavioral evaluation for 0.2.0. One [recorded long-form smoke check](runs/long-form-smoke.json) includes an actual response from a fresh-context agent and the implementing assistant's review. Its unknown model identifier and lack of a baseline limit the conclusions. Authored examples establish intended behavior only. The [validation report](validation-report.md) describes the executed checks and remaining gaps.
