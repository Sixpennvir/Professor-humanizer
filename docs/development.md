# Development

The skill itself runs through the agent host. Repository maintenance requires Python 3.10 or newer. Development scripts use the standard library.

## Verify a change

```text
python scripts/showcases.py
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/package.py
```

The validator checks required files, metadata, links, rule IDs, behavioral-case references and generated example consistency. The test suite uses deliberately broken fixtures to exercise release boundaries.

## Edit an example

Edit [showcases.json](../examples/showcases.json), then regenerate:

```text
python scripts/showcases.py --write
```

This updates the gallery and only the marked example block in the README. Each pair needs a complete draft, a revision, protected literal anchors, and editorial preservation checks. The draft must supply every fact the revision uses. A task note must not introduce facts absent from it.

The anchor checks can detect a changed quotation or quantity. They cannot detect every changed causal claim, attribution, or implication. Manually compare the complete pair after generation. Track each substantive judgment and qualification from the draft to the revision. If a claim lacks a warrant, the example must preserve its substance and identify the support gap; unsupported status alone does not authorize deletion.

Keep these authored examples distinct from [behavioral cases](../tests/cases.json). Cases contain prompts for actual model runs; their expected invariants should not enter the model's prompt.

## Package

The version in SKILL.md supplies the package version. The packager creates a reproducible ZIP under `dist/`, with a SHA-256 companion file.

The explicit runtime allowlist includes SKILL.md, LICENSE, UI metadata and required references. It excludes development fixtures, Git history, credentials, and unrelated workspace files. The extracted ZIP must pass structural validation without the development tree.

## Git workflow

Review the diff and complete verification before updating the default branch directly. Create a pull request only when the maintainer requests one. Publish each authorized release from its verified commit and attach the generated ZIP with its SHA-256 file.

Do not claim a community survey, user test, model benchmark, or improvement percentage without a recorded study that actually took place. Authored examples demonstrate intended behavior. Executed tooling tests establish only their defined checks.

## Behavioral evidence

Follow the [evaluation protocol](../tests/README.md). Store real input and output with the host, model, version and run date. Report failures and blocked cases. Evaluate substantive questions, useful parallel clauses, report structure and authorized research against their actual boundaries. An expected outcome must not reward deleting the author's position to satisfy a style rule.

For long-form revisions, compare the source claims with their revised locations and inspect non-adjacent paragraph functions. Report lost qualifications, changed inferences and repeated conclusions separately from literal-anchor checks. A run on one model does not establish cross-host compatibility.
