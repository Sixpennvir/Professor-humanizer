# Better AI Writer

**Revise English prose without losing the argument.**

Better AI Writer is an instruction-only writing skill built around close reading and careful revision. It helps an agent connect evidence to claims, give each paragraph a purpose, and remove formulaic phrasing while preserving the writer's position.

[Examples](references/examples.md) · [Install](docs/usage.md) · [Writing rules](references/rules.md) · [Pattern catalogue](references/patterns.md) · [Evaluation](tests/README.md)

> **Private preview · 0.2.0** — Repository access currently requires permission. No public release has been published.

## See the revision

The following teaching example uses a fictional passage. Everything needed for the revision appears in the draft. These are authored demonstrations, not results from an independent model benchmark.

<!-- showcase:start -->
**Before**

> The narrator's description is not merely a recollection of a room; it is a profound exploration of memory's complexity. She first claims, “I remember the room exactly” (4). Later she writes, “Perhaps the door opened onto the garden” (4). Why is this significant? The movement from “exactly” to “Perhaps” changes the certainty of the description. It is a movement from confidence to hesitation, highlighting the complex nature of remembering.
>
> The passage is important because the opening assurance encourages the reader to trust the description, while the later qualification gives the reader a reason to reconsider that trust. This shows that certainty in telling a memory cannot establish the accuracy of the memory. Yet the passage gives no independent account of where the door actually opened. It therefore leaves the description's accuracy unresolved. Ultimately, this uncertainty underscores the complexity of memory.

**After**

> The narrator qualifies her initial confidence. She first claims, “I remember the room exactly” (4). Later, “Perhaps the door opened onto the garden” (4) makes one detail tentative. The shift from “exactly” to “Perhaps” gives the reader a specific reason to reconsider the opening assurance.
>
> The passage offers no independent account of where the door opened. That absence leaves the memory's accuracy unresolved: the narrator's confidence alone cannot establish whether the description matches the room.

**What changed:** The first paragraph connects a precise word change to the reader's reason for revising trust. The second develops the evidentiary limit instead of repeating that memory is complex. The revision preserves the argument's scope while removing rhetorical staging.
<!-- showcase:end -->

[Explore seven complete examples](references/examples.md), including research summaries, conditional requests, authorial disagreement, protected quotations, narrative, and prose that needs no change.

## What the skill works on

| Layer | Editorial work |
| --- | --- |
| Evidence | Preserve the source's facts, attribution, uncertainty and limits |
| Argument | Connect a concrete detail to an inference through an explicit warrant |
| Paragraphs | Give each paragraph a contribution; remove repeated conclusions |
| Sentences | Replace formulaic constructions with precise relationships |
| Ending | Close at the actual result, next step or unresolved premise |

A shorter text can still lose the argument. This skill checks what survives each edit and allows necessary explanation to take more space.

## The strict profile

Finished English prose uses connected paragraphs, without subheadings or lists. Negative redefinition such as “not X but Y,” additive upgrades, rhetorical parallelism and question-led exposition are excluded. The [22-pattern catalogue](references/patterns.md) also covers unsupported significance, repeated sentence structures and paragraph loops.

The verb exercise attempts to remove original “to be” forms through faithful recasting. Exact quotations retain their source wording. If meaning and a mandatory style rule cannot coexist, the agent identifies the conflict instead of silently changing the claim.

These restrictions express the project's chosen style. They apply across scenarios. Ordinary grammar falls under the catalogue's specific boundaries; the project does not blacklist every participle, conjunction or technical term. Documentation and requested diagnostic reports may use headings and tables.

## Try it

For a repository-scoped Codex setup, run this from the project where you want to use the skill. Git must already have access to this private repository.

```bash
git clone https://github.com/Sixpennvir/better-ai-writer.git .agents/skills/better-ai-writer
```

Then invoke:

```text
Use $better-ai-writer to revise the draft below.
Audience: readers familiar with the source passage.
Preserve my interpretation, quotations, and qualifications.
Use only the material supplied here. Return the revised prose.

[Paste the complete draft and any source material.]
```

For ZIP installation, personal installation, updating, diagnosis and drafting, see the [usage guide](docs/usage.md). The installed skill requires no Python runtime, API key, or connection to another writing skill. Other Agent Skills hosts may use different discovery paths; compatibility has not been tested.

## Academic roots, broader use

The [course profile](references/course-profile.md) preserves the original consciousness assignment, including close reading, charitable interpretation and its citation conventions. Activate it explicitly for that assignment.

The general rules also apply to research summaries, emails, decision writing and narrative. A confirmed message can close directly. A recommendation needs its real conditions. An exploratory argument preserves a concrete unresolved issue.

The skill operates on user-supplied material. It does not browse for facts to insert into a writing task. A sample offered for voice calibration contributes expression only.

## Reviewable development

| Artifact | What you can inspect |
| --- | --- |
| [Source traceability](references/traceability.md) | Original requirements, approved overrides and current implementation |
| [Evidence record](references/evidence.md) | Research findings and their limits |
| [Design review](docs/design-review.md) | Lessons from the reference projects and independent implementation decisions |
| [Showcase source](examples/showcases.json) | Complete drafts, revisions, protected anchors and editorial checks |
| [Behavioral suite](tests/cases.json) | Prompts and invariants for model evaluation |
| [Validation report](tests/validation-report.md) | Executed checks and remaining gaps |

The README example and detailed gallery come from the same data. Checks catch documentation drift and changes to protected example anchors. They cannot certify semantic fidelity or model behavior. No authorship-detector score or word-count reduction serves as a quality result.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for the example contract and review process. Maintainer commands and packaging details live in [development](docs/development.md). Changes can be reviewed through pull requests before integration.

[MIT license](LICENSE). The instructional foundation comes from user-supplied course guidance. Related-project observations are attributed in the design review. Better AI Writer contains independently authored instructions and examples and has no Humanizer dependency.

## 中文说明

这是面向英文写作的严格修订 skill。它关注证据、论证和段落推进，保留事实、引文、限定条件及作者立场。首页和示例库中的每组修改都展示完整输入，避免通过未展示的材料制造改写效果。目前仓库保持私有预览；自动检查与实际模型评测分别记录。
