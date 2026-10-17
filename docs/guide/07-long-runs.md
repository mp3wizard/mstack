# Run long work and come back to it

## Before you step away

Say "going to bed" or "stepping away" so the agent stops asking. The Always-pause list still holds, so it will not contact users, publish a library, or write to Figma without you. Write done as a check every iteration can run, and give `/loop` that predicate. A duration is not a check.

```
/mstack:design-mode redesign the account area across web and mobile. going to bed. keep a decision log, stop when every flow has a handoff package, and don't publish anything.
```

## Keep a decision trail

The `design-log` skill keeps one TSV row per decision at `.mstack/<slug>/decisions.tsv`: what was decided, why, a pointer to the evidence, the evidence tier, and the result. `scripts/log.sh` appends rows safely. It strips tabs and newlines and quotes any cell a spreadsheet would run as a formula. The log is append-only, and before handing back the agent audits it against the session transcript and has a reviewer on another model family flag weak rows. The reply ends with an Attention section.

`.mstack/` is a working folder, kept out of git unless you ask to commit the trail.

## Pause and resume

- **Pause safely** stops at a safe step, takes nothing outward, saves the evidence pack, and writes a resume note to `.mstack/<slug>/resume.md`. It runs only on an explicit pause, going offline, a restart, or imminent compaction. "Keep going" never triggers it.
- **Session pickup** reads the resume note, the decision log, and the evidence pack, checks what changed in the live UI or Figma since, names the resume point, and hands the rest to the playbook that owns it. It does not redo finished work unless the design changed under it.

## Work no playbook fits

**Bespoke run** frames the task with a check that can fail, borrows the nearest playbooks' steps, designs only the gaps as units that each end in a check, runs each as an experiment, and logs every decision with design-log.

Files: `skills/design-log/SKILL.md` and `skills/design-mode/playbooks/pause-safely.md`, `session-pickup.md`, `bespoke-run.md`.

Next: [Principles and evidence tiers](08-principles-and-evidence.md).
