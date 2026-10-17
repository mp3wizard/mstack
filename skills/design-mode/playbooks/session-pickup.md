### Session pickup

**You own the resume point. Read the prior trail, don't redo it.**

Use it when you take over design work another session started: a transcript, a resume note, a decision log, an evidence pack, or a branch.

1. Locate the prior trail. Read `.mstack/<slug>/resume.md` if a Pause safely run wrote one, and `.mstack/<slug>/decisions.tsv` if the **design-log** skill kept one. Read the evidence pack and the handoff draft the run linked. For a transcript, read only the current project's transcripts under `~/.claude/projects/`, never other projects. Parse a long transcript in a subagent and keep the reduced timeline in the main thread.
2. Reconstruct the state. Which playbook ran, the step it reached, the object model and state matrix so far, the variants built and judged, the screenshots captured, the open decisions, and every `pending: user evidence` gate. The prior trail is authoritative input. Resist re-deriving it.
3. Check what changed since. Compare the live UI, the Figma file's version history (per references/figma.md, read-only), and the branch against what the trail recorded. A design that moved since the last screenshot invalidates those screenshots, not the decisions.
4. Diff done against pending. Name the resume point. Do not re-run a critique, a diverge, or an inspection that already has a verdict, unless step 3 found the design changed under it.
5. Route the remaining work to the playbook that owns it and copy its remaining steps into the todo list. Pickup ends here. The routed playbook owns the rest.
6. Re-verify each inherited claim you build on against the real artifact (**principle-prove-it-with-evidence**). A prior session's summary is not proof. Keep each claim's evidence tier as the trail labeled it (**principle-never-fabricate-user-evidence**).

**Reply:** where the prior session stopped, what you inherited and what you redid (ideally nothing), what changed since, the resume point, and the playbook now running.

**Grounded in:** pstack's Session pickup playbook, adapted (see NOTICE.md).
