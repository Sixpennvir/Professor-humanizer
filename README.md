# Better AI Writer

An English writing skill for eliminating formulaic AI prose through rigorous revision.

Better AI Writer turns a strict writing brief into a repeatable editing process. It checks the evidence behind an argument and removes repetition that survives ordinary word replacement. Its rules cover English academic writing, professional correspondence, explanations, reports, and narrative.

The project ships as an instruction-only skill. It requires a compatible agent host and no additional API key or service. It operates on the material you supply.

## A quick example

**Your material:** Maya must send a revised budget by Friday at noon for review before Monday's meeting.

**Before**

> In today's fast-paced environment, this is not simply a budget update; it is a vital step toward alignment. Can we make this happen? Your collaboration will pave the way for success.

**After**

> Maya, please send the revised budget by noon on Friday so I can review it before Monday's meeting.

See [worked examples](references/examples.md) for close reading, research summaries, decisions, quotation handling, and ambiguous commitments.

## What the strict profile requires

- Connected prose without subheadings, bullets, or numbered lists.
- No negative redefinition such as “not X but Y,” additive upgrades, rhetorical parallelism, or question-led exposition.
- Review of [22 prohibited pattern families](references/patterns.md), including repeated syntax and paragraph functions.
- Accurate use of supplied evidence, preserved uncertainty, and protected direct quotations.
- A deliberate attempt to replace every original “to be” form with faithful, precise phrasing.
- Endings suited to the task and supported by the material.

These restrictions apply to finished English prose. Documentation and separately requested diagnostic reports may use headings and lists. A necessary exact quotation keeps its original wording even when that wording contains a banned pattern.

The grammar rules target defined problematic uses. Ordinary factual coordination, necessary technical vocabulary, and isolated participles do not automatically violate them. Read the complete [rules](references/rules.md) for boundaries and conflict handling.

## Install locally

Download the repository ZIP through GitHub's **Code → Download ZIP**, or use the packaged skill ZIP when a release provides one. Extract it and name the skill folder `better-ai-writer`.

For a repository-scoped Codex installation, copy that folder to:

```text
your-project/
  .agents/
    skills/
      better-ai-writer/
        SKILL.md
        agents/
        references/
        LICENSE
```

For personal Codex discovery, use `~/.agents/skills/better-ai-writer/`. Codex documents these local discovery paths in its [official skills guide](https://learn.chatgpt.com/docs/build-skills). Other Agent Skills hosts may require a different installation directory; follow the host's instructions. Cross-host behavior has not been tested.

The repository root itself contains the installable skill. No build step or Python runtime is required to use it. Development scripts validate and package the project only.

## Use it

Invoke the installed skill in Codex with a prompt such as:

```text
Use $better-ai-writer to revise the English draft below.
Audience: a colleague who knows the project.
Preserve the deadline and my tentative commitment.
Use only the supplied material.
Return the revised prose.

Material: [...]
Draft: [...]
```

For analysis, request a diagnostic report with rule IDs before revision. For the original course assignment, explicitly request the consciousness-course profile and supply the passage, relevant context, and citation details.

The skill asks for clarification when a change would alter meaning or require missing evidence. It never treats web research about writing patterns as evidence for your subject.

## Project contents

| File | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Invocation instructions and workflow |
| [Core rules](references/rules.md) | Sixteen operational requirements |
| [Pattern catalogue](references/patterns.md) | Twenty-two prohibited uses with repair guidance |
| [Course profile](references/course-profile.md) | Assignment-specific requirements |
| [Traceability](references/traceability.md) | Source guidance and approved overrides |
| [Evidence record](references/evidence.md) | Research sources and their limits |
| [Evaluation guide](tests/README.md) | Behavioral cases and honest validation scope |
| [Contributing](CONTRIBUTING.md) | Rule changes and verification |

## Development

Use Python 3.10 or newer. The development tools use only the standard library.

```text
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/package.py
```

The packager writes a reproducible skill ZIP and SHA-256 checksum to `dist/`. It includes only an explicit list of runtime files. GitHub Actions runs the same structural checks and packaging tests.

Those checks verify packaging and rule references. They cannot establish semantic fidelity or prove that a model follows the style policy. The [behavioral cases](tests/cases.json) require actual model runs and human review before any quality claim.

## Scope and evidence

The strict bans express an editorial preference. Humans also use many of the excluded constructions. The [research record](references/evidence.md) explains which observations motivated review and where the project makes its own policy choice. This skill offers no AI-authorship diagnosis or detector score guarantee.

The instructional foundation comes from user-supplied academic writing guidance. The repository contains an operational paraphrase, a source mapping, and original examples. It does not redistribute the screenshots or linked course materials. The project has no dependency on another writing skill.

## License

[MIT](LICENSE). Contributions follow [CONTRIBUTING.md](CONTRIBUTING.md).

## 中文说明

Better AI Writer 是面向英文写作的严格修订 skill，重点处理空泛论述、重复句式和缺乏推进的段落。它保留原始材料、引文和作者立场，并将课程特定要求与跨场景规则分别记录。正文默认不使用小标题或列表；规则文档和诊断报告可以使用。它不依赖其他写作 skill，也不承诺通过 AI 检测。安装后提供英文草稿、目标读者和事实材料即可使用。
