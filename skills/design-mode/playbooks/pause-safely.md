### Pause safely

**You own a clean stop. Leave a checkpoint a cold-start session can resume from.**

Only on an explicit pause, going offline, a restart, or imminent context compaction. On "keep going", "going to bed, keep going", or "don't stop", do not pause.

1. Stop at a safe boundary. Finish the current step or back out of it. Start nothing new, and stop any running subagents.
2. Take nothing outward to pause. No message to users or stakeholders, no shared library publish, no Figma write, no push. The Always-pause list in the router still holds.
3. Make the work durable. Save every variant, screenshot, kit, and draft to the evidence pack on disk. If the project is a git repo, commit local edits as one `wip:` commit on the current branch, and say in one line if the tree is broken.
4. Write the resume note to `.mstack/<slug>/resume.md`. Capture the intent, the playbook and the step reached, what is verified and its evidence tier, the open decisions, the pending user-evidence gates, the next three steps, the key file paths, and the gotchas. If the **design-log** skill kept a log, point to it instead of repeating it.

**Reply:** where you are in the playbook, what is on disk and what was only in your head (paths, no dumps), the commits you made, and the first action on resume. This is a pause, not a final report.

**Grounded in:** pstack's Pause safely playbook, adapted (see NOTICE.md).
