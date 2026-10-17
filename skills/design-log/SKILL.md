---
name: design-log
description: "Keep a reviewable decision trail for long, unattended, or multi-session design work: one TSV row per decision with its why, its evidence pointer, and the evidence tier. Use for /design-log, autonomous or step-away design runs, Bespoke run, or any design work a human reviews later."
disable-model-invocation: true
---

# Design log

Keep one canonical log per piece of work. It lets a human who stepped away trust the design without re-reading the session.

## The format

A single TSV file, one row per decision. Cells stay on one line. Evidence is a pointer, not prose. Start a log by copying `references/decision-log-template.tsv`, which holds the header row.

- **ts.** ISO 8601 timestamp, UTC.
- **phase.** The playbook step or workstream, such as `frame`, `state-matrix`, `diverge`, `critique`, `handoff`.
- **decision.** What was chosen or done, one line.
- **why.** The reason in plain words. Name a principle only when it changed the choice, as in "kept the native select, per follow-conventions".
- **evidence.** A path or pointer that proves it: a screenshot path, a variant dir, a critique verdict file, a Figma frame name, a commit SHA. Never a paragraph. Never a participant's name or contact detail.
- **tier.** The evidence tier from the **design-mode** router: `1` inspection, `2` existing evidence, `3` new user evidence, or `-` when the row records an action rather than a claim. A tier 1 row is a hypothesis however confident it reads.
- **result.** The outcome: `kept`, `reverted`, `contrast 4.6:1 pass`, `inconclusive`, `pending: user evidence`, `open`.

```
ts	phase	decision	why	evidence	tier	result
2026-06-02T09:10:00Z	frame	restated "add a filter button" as "find last month's failed payments"	the request named a solution, not a need	.mstack/reports-filter/frame.md	2	open
2026-06-02T10:05:00Z	diverge	built three filter layouts, one rejecting the default card grid	more than one plausible answer	.mstack/reports-filter/variants/	-	3 variants
2026-06-02T11:20:00Z	critique	kept variant B, inline chips	fewest steps on the primary task, cross-family seats agreed	.mstack/reports-filter/critique.md	1	kept
2026-06-02T11:40:00Z	a11y	darkened chip text to #595959	#767676 on the #e3e8f2 chip tint was 3.70:1 and failed 1.4.3	contrast.py output in critique.md	1	5.70:1 pass
2026-06-02T12:00:00Z	handoff	left chip order as a product call	taste call, belongs to a human	handoff.md#open-decisions	-	pending: product decision
```

## Logging a row

Write each row the way you would tell a teammate what you did. Plain words, concrete actions.

Use `scripts/log.sh <logfile> <phase> <decision> <why> <evidence> <tier> <result>`. It stamps `ts`, writes the header on first use, strips tabs and newlines from cells, and prefixes a cell that starts with `=`, `+`, `-`, or `@` with a single quote so a spreadsheet never runs it as a formula. Evidence often holds page titles and filenames from the analyzed product, so keep that guard even when you append by hand. `scripts/log.sh --self-test` checks it.

Log decision points and checkpoints, not every action: a fork chosen, a unit finished with its check, a revert and what triggered it, a blocker, a pending gate opened or closed, an open decision handed to a human. In a loop, one row per iteration.

A run is one conversation, including its later turns. A Session pickup or a new chat starts a new run. When a run adds to a log that already has rows, its first row has phase `start`. Its decision names the `ts` range of the rows before it that this run did not write, and its evidence names this run. A run that returns to a log in a later turn reads the last rows first, to see whether another run wrote since. Use phase `start` for nothing else.

## Where it lives

Keep the log at `.mstack/<slug>/decisions.tsv` in the project, beside the evidence pack. `.mstack/` is a working folder, so leave it out of git unless the user asks to commit the trail. Point to it from the handoff package's evidence pack.

## Rules

- **Append-only.** A wrong call gets a new row that supersedes it. Never edit or delete history.
- **No invented evidence.** A row about users cites tier 2 or 3 evidence that exists, or it says tier 1 (**principle-never-fabricate-user-evidence**).
- **Scripts over hand-made proof.** Prefer evidence a committed script produced, such as the output of design-mode's `contrast.py` or `sus.py`, over a one-off claim.

## Audit the log before handing back

Check that the log told the truth. Read this run's transcript among the current project's transcripts under `~/.claude/projects/`. Never read another project's transcripts. Walk this run's rows against what happened.

- Every row maps to a real decision or action.
- Every evidence pointer resolves and shows what the row claims.
- Every tier matches the evidence. A screenshot is tier 1, not tier 3.
- A fork, a revert, or an abandoned direction that shaped the design but has no row is a gap. Add the row.

Correct the log, not the story. When a row is wrong, append a row that supersedes it with what happened and a pointer that resolves.

## Cross-model review of the trail

Before handing back long or unattended work, spawn one reviewer on a different model family from the one that did the work. Prefer the **codex-bridge:codex-second-opinion** agent when installed. Otherwise use `general-purpose` on the other of `opus` and `sonnet` from the one that built most of the work, and say the review stayed in one family. Give it the log and the evidence pack paths. It flags, it does not redo:

- decisions with weak or missing evidence,
- tier labels stronger than their evidence,
- checks claimed but not shown in the evidence pack,
- choices that look risky in hindsight, such as a taste call made silently instead of recorded as open.

The reply for a run that kept a log ends with an **Attention** section. Its first line is `reviewed by <agent and model>`. Then one bullet per flag, pointing at a row. "No flags" is a valid list.

## Reading the trail

`column -s$'\t' -t .mstack/<slug>/decisions.tsv` renders it in a terminal. GitHub renders a committed TSV as a table.

Other mstack skills and playbooks route their audit trail here by name and do not restate the columns.

Adapted from pstack's show-me-your-work skill (see NOTICE.md).
