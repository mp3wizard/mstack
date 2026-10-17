---
name: design-reflect
description: "Retro on a design session: three parallel reviewers read the transcript and the evidence pack, a synthesizer turns their findings into proposed edits to the mstack skills that ran, and nothing is applied without approval. Use for /design-reflect, 'reflect', 'retro', or after a design run that went wrong or taught something reusable."
disable-model-invocation: true
---

# Design reflect

Mine the current session for durable design-process learnings, then route each one to a concrete edit on a skill or playbook that ran.

Skip when the session was trivial, off-topic, or already followed a skill correctly. A one-off is not a learning. This is a retro on how the work was done. It is not a critique of the design itself, which is the **critique** skill's job.

## 1. Gather the inputs

- **Transcript.** Find this session's transcript in the current project's folder under `~/.claude/projects/`, the folder named after the working directory with every character other than a letter or digit turned into `-`. List its `*.jsonl` files newest first and take the one whose first user message matches this session's opening request. Never read another project's folder. If nothing matches, write a tight digest of the session instead.
- **Trail.** The decision log at `.mstack/<slug>/decisions.tsv` if the **design-log** skill kept one, the evidence pack, and the handoff draft.
- **Models.** Read `~/.mstack/models.md` if **setup-mstack** wrote one, and use its `judgment` and `reflect tooling` lines and its `budget`. Without it, use the defaults in the table.

## 2. Spawn three reviewers in parallel

One message, three Agent calls, `run_in_background: true`. Pass each prompt template verbatim, with the transcript path or digest and the trail paths filled in where marked. Reviewers return findings in their final message and write nothing.

| Lens | Agent | Default model | Prompt |
|---|---|---|---|
| Judgment | `general-purpose` | `opus` | `references/judgment-reviewer.md` |
| Process and tooling | `general-purpose` | `sonnet` | `references/tooling-reviewer.md` |
| Divergent | `codex-bridge:codex-second-opinion` when installed, else `general-purpose` | its own, else `opus` | `references/divergent-reviewer.md` |

The divergent seat is the only one that can sit on another model family. When it falls back to `general-purpose`, say the retro ran on one model family. If the Agent tool rejects a model, run that seat on the parent model and say so.

## 3. Synthesize

One Agent call, `general-purpose` on the judgment model, with `references/synthesizer.md` verbatim and each reviewer's full output pasted where marked. It returns an Accepted, Rejected, and Backlog list.

## 4. Prefer a mechanism

Move any Accepted item that a check would enforce more reliably to Backlog: a new `FOLK` row or structure check in `../../scripts/check-plugin.py`, a `--self-test` case, a lint, or a token rule (**principle-encode-decisions-in-the-system**). Prose is for what a mechanism cannot enforce.

## 5. Apply only what the user approves

Show the full Accepted, Rejected, and Backlog output, then stop. Skill edits change every future design run, so never auto-apply. The user picks rows and may redirect a routing.

For each approved row:

- **Small edit** (a sentence, a bullet, a corrected fact): make it directly.
- **Larger edit** (a new section, a new playbook, more than about ten lines): draft it, show the diff, and apply after approval. A new playbook also needs its router entry and its line in `../design-mode/references/routes.txt`.
- **`tune description: <skill>`**: rewrite the description so its trigger words come first.
- **`new skill: <name>`**: draft it with the same frontmatter shape as the other mstack skills. Use the **plugin-dev:skill-development** skill if installed.

After every edit, run `python3 ../../scripts/check-plugin.py`, the plugin's own checker, and fix what it reports. Report Backlog items in the reply. Filing them in a tracker is an outward action, so do it only when the user asks.

## 6. Summarize

Short list, no preamble:

- Edits applied: the file path and what changed, one line each.
- New skills or playbooks: one line each.
- Backlog: one line each, with the mechanism it needs.
- Dropped: one line per rejected finding with its reason.

Adapted from pstack's reflect skill (see NOTICE.md).
