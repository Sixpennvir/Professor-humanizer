# Installation and use

## Repository installation in Codex

From the project where the skill should apply:

```bash
git clone https://github.com/Sixpennvir/professor-humanizer.git .agents/skills/professor-humanizer
```

Cloning the public repository requires no GitHub login. If the destination already exists, inspect it before installing another copy.

Codex's [official local skills guide](https://learn.chatgpt.com/docs/build-skills) documents repository discovery under `.agents/skills/` and personal discovery under `~/.agents/skills/`. Install the repository root as the skill folder. Preserve its `references/` and `agents/` directories; copying only SKILL.md leaves required references missing.

## Manual ZIP installation

Download [professor-humanizer-v0.3.0.zip](https://github.com/Sixpennvir/professor-humanizer/releases/download/v0.3.0/professor-humanizer-v0.3.0.zip) from the [release page](https://github.com/Sixpennvir/professor-humanizer/releases/tag/v0.3.0). The accompanying `.sha256` file contains the archive's SHA-256 checksum. Extract the `professor-humanizer/` folder into `.agents/skills/` in your working project. Confirm that `.agents/skills/professor-humanizer/SKILL.md` exists directly at that path.

For personal installation, place the same folder under your home directory's `.agents/skills/`. Do not install duplicate copies at several scopes unless you intend to manage them separately.

Invoke `$professor-humanizer` in a Codex request. If discovery does not refresh, restart the host. Other Agent Skills hosts may use different installation paths; consult their documentation. The project has not completed cross-host compatibility testing.

## Update a clone

```bash
git -C .agents/skills/professor-humanizer pull --ff-only
```

This preserves a clear failure when local edits and upstream history diverge. Inspect any local changes before resolving that conflict. ZIP installations require replacing the skill files deliberately; keep any edits you want to retain.

## Existing Better AI Writer installations

Update an existing clone before changing its folder name:

```bash
git -C .agents/skills/better-ai-writer remote set-url origin https://github.com/Sixpennvir/professor-humanizer.git
git -C .agents/skills/better-ai-writer pull --ff-only
```

Inspect local edits before updating. After a successful update, rename that installed folder to `professor-humanizer` and invoke `$professor-humanizer`. Apply the same steps to a personal installation at its actual path. Keep one active installation at the intended scope. The recorded v0.2.0 model test retains the project name and prompt used for that run.

## Revision

```text
Use $professor-humanizer to revise this English passage.
The reader already knows the assigned text.
Keep my argument and all quotations.
Use only the draft and supplied passage.
Return the final prose.

Source passage: [...]
Draft: [...]
```

The source passage supplies evidence; the draft supplies your interpretation. If they disagree on a consequential claim, the skill should identify that conflict.

## Drafting from supplied material

```text
Use $professor-humanizer to draft an email from these notes.
Recipient: Rosa.
Request: send the agenda by Thursday noon.
Reason: I need to check it before Friday's meeting.
If the room is unconfirmed, label its location provisional.
Return only the email.
```

Drafting permits selection and organization of the supplied facts. It does not permit invented context or commitments.

## Diagnosis without rewriting

```text
Use $professor-humanizer to diagnose this English draft.
Identify where the reader loses the argument.
For each finding, quote the passage, name the rule, and propose a repair.
Do not rewrite the complete draft or modify files.

[Draft]
```

A diagnostic may use structured findings. The prose deliverable itself retains the no-heading/no-list rule.

## Author samples

Label a sample explicitly as voice-only. The skill can use compatible diction and rhythm, while keeping all strict bans. Events or opinions in the sample cannot migrate into the target draft.

## Original course assignment

Request the original consciousness-course profile explicitly. Supply the passage, the needed surrounding context, the current Build stage and citation details. The profile should not appear automatically in an unrelated email or report.

## When the skill pauses

A tentative commitment cannot become a promise without clarification. Never invent missing quotations or source details. A file-format requirement can conflict with the strict prose format. In those cases, expect the agent to identify the precise decision it needs.

A clear paragraph may return unchanged. An unsupported thesis may require evidence before the agent can deliver a final revision.
