# Installation and use

## Repository installation in Codex

From the project where the skill should apply:

```bash
git clone https://github.com/Sixpennvir/better-ai-writer.git .agents/skills/better-ai-writer
```

This preview requires access to the private repository. Authenticate Git with an account that has access first. Do not embed access tokens in a clone URL or paste them into a prompt. If the destination already exists, inspect it before installing another copy.

Codex's [official local skills guide](https://learn.chatgpt.com/docs/build-skills) documents repository discovery under `.agents/skills/` and personal discovery under `~/.agents/skills/`. Install the repository root as the skill folder. Preserve its `references/` and `agents/` directories; copying only SKILL.md leaves required references missing.

## Manual ZIP installation

Download the repository through GitHub's Code menu while signed in, or use a locally built skill ZIP. Extract the skill into `.agents/skills/better-ai-writer/` in your working project. Confirm that SKILL.md sits directly inside that directory.

For personal installation, place the same folder under your home directory's `.agents/skills/`. Do not install duplicate copies at several scopes unless you intend to manage them separately.

Invoke `$better-ai-writer` in a Codex request. If discovery does not refresh, restart the host. Other Agent Skills hosts may use different installation paths; consult their documentation. This project has not run cross-host compatibility tests.

## Update a clone

```bash
git -C .agents/skills/better-ai-writer pull --ff-only
```

This preserves a clear failure when local edits and upstream history diverge. Inspect any local changes before resolving that conflict. ZIP installations require replacing the skill files deliberately; keep any edits you want to retain.

## Revision

```text
Use $better-ai-writer to revise this English passage.
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
Use $better-ai-writer to draft an email from these notes.
Recipient: Rosa.
Request: send the agenda by Thursday noon.
Reason: I need to check it before Friday's meeting.
If the room is unconfirmed, label its location provisional.
Return only the email.
```

Drafting permits selection and organization of the supplied facts. It does not permit invented context or commitments.

## Diagnosis without rewriting

```text
Use $better-ai-writer to diagnose this English draft.
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
