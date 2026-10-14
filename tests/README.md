# Evaluation

## Automated checks

Run the three development commands in the root README. Validation checks required files, metadata shape, local document links, ordered rule IDs, and case references. Regression tests exercise malformed fixtures, package exclusions, repeatability, and the extracted skill's self-contained references.

The validator deliberately does not score natural language with regular expressions. It cannot infer whether two paragraphs repeat an argument or whether a revision changed a promise.

## Behavioral protocol

For each case in [cases.json](cases.json), open a fresh agent session with the installed skill and supply the case input exactly. Record host, model identifier, skill version, date, prompt, and complete response. Do not supply the expected result to the model.

A human reviewer checks every expected invariant against the actual response and supplied evidence. Mark pass, fail, or blocked; explain the exact violation with a rule ID. Quoted violations do not count as original prose. A justified clarification can pass a case that requires one.

Evaluate source fidelity first, then strict style compliance, paragraph progress, and readability. A more fluent revision that changes meaning fails. A regex match alone cannot establish a violation of a use-dependent rule.

Run the same cases without the skill if making comparative improvement claims. Keep model and sampling settings comparable, preserve failures, and report the number and type of cases. Do not claim model-wide quality from this small suite.

## Current status

The examples and expected invariants have been authored for review. No separate model-run behavioral evaluation has been recorded for v0.1.0. Automated results, when available, validate the project tooling only. Add actual results in a dated report before announcing behavioral pass rates.
