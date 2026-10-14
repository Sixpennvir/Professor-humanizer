# Evaluation

This project distinguishes authored demonstrations, automated tooling checks, and actual model evaluation. No community survey, user interview, or user study has been conducted.

## Authored examples

[Seven showcases](../references/examples.md) demonstrate the intended behavior using original fictional inputs. Each revision draws its factual content from the displayed draft. They are not independent model outputs.

[showcases.json](../examples/showcases.json) supplies the README and gallery. The generator checks protected literal anchors and quantities. These checks cannot determine whether the revised inference remains faithful.

## Automated tooling checks

Run the commands in [development](../docs/development.md). The regression suite deliberately breaks fixtures to exercise quotation anchors, numbers, document synchronization, metadata, links, packaging exclusions and reproducibility.

One test deliberately changes an inference while preserving all literal anchors. The mechanical checker passes that fixture. That test records a known limit: semantic review must catch the changed claim.

The validator does not award a writing-quality score. Passing these tests does not show that an agent follows the skill.

## Behavioral protocol

The [32 cases](cases.json) contain realistic prompts and expected invariants. To run a case, use a fresh agent session with the installed skill and provide only its input. Keep expected invariants out of the model prompt.

Record the host, model identifier, skill version, date, full input and complete response. A reviewer then checks each expected invariant against the actual response and the supplied evidence. Mark pass, fail, or blocked and explain the reason with a rule ID. A clarification can pass a case that requires one.

Review in this order:

1. **Fidelity:** no added or lost fact, changed commitment, altered attribution or damaged quotation.
2. **Argument:** interpretation follows from supplied evidence and each paragraph contributes.
3. **Strict compliance:** mandatory bans are resolved without silent exceptions.
4. **Readability:** the intended reader can follow the reference and the relationship between claims.

A fluent response that changes meaning fails. A matched phrase alone cannot establish a violation of a use-dependent rule.

For comparative claims, preserve actual baseline and skill-enabled runs under comparable conditions. Report the sample, failures and limitations. Do not substitute a model's self-rating, word-count reduction or invented community feedback for this record.

## Current status

No independent model-run behavioral evaluation has been recorded for 0.2.0. Authored examples and their editorial review establish intended behavior only. The [validation report](validation-report.md) lists executed tooling checks and their scope.
