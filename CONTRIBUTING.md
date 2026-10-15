# Contributing

Start with a concrete passage and the editing problem. Include the full input, desired behavior and relevant rule IDs. Remove private material and use examples you have permission to share.

## Example contract

Every before/after demonstration must expose all the facts needed for its revision inside the before text. Keep the recipient, quantities, conditions, attribution and substantive position. A shorter revision fails if it loses an independent claim.

Write original examples. Do not copy passages from other skills or their documentation. Attribute a design observation in the [design review](docs/design-review.md) when it influences this project. A reference project's policy does not override this project's mandatory rules.

For the featured examples, edit [showcases.json](examples/showcases.json) and regenerate with `python scripts/showcases.py --write`. Check protected anchors and perform a semantic comparison. Keep unchanged-output and clarification cases where an automatic rewrite would harm meaning.

## Rule changes

Describe the trigger, repair, and boundary. Distinguish research evidence from editorial preference. Use a primary source for an empirical claim and state its scope. Update traceability when a requirement changes.

Preserve the course profile and strict English-writing scope. A proposed exception to a mandatory ban needs an explicit policy decision; it cannot arrive disguised as a stylistic improvement.

## Verification and review

Follow [development](docs/development.md) for local checks and packaging. Add a behavioral case for a changed decision boundary. Keep model outputs and authored examples separate. Record only checks that actually ran; do not invent community research, user feedback or performance figures.

For the current private preview, the maintainer reviews and verifies changes before updating the default branch directly. Describe the concrete failure and resulting behavior with the actual verification and remaining limits. Create a pull request only when the owner requests one. Contributions follow the repository's MIT license.
