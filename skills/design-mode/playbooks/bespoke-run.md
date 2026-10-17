### Bespoke run

**You own the workflow before the work. When no playbook fits, design one, then run it.**

Use it when the task matches none of the playbooks and composing two of them would leave gaps: a cross-product redesign, an ambitious multi-part change, or design work a human reviews after stepping away.

1. **Frame.** State the definition of done as a check someone could fail, with the evidence tier it needs (**principle-prove-it-with-evidence**). Quantify the scope in screens, flows, components, or states. Name the riskiest assumption (**principle-riskiest-assumption-first**). Pick the rigor level and bias it high for anything users or the shared library depend on. Rigor means gates and artifacts, not effort.
2. **Borrow before you invent.** List the existing playbooks whose steps cover parts of the task. Reuse those steps verbatim where they fit and design only the gaps.
3. **Design the phases.** Break the work into units that each end in a check. Put the verification harness first: the baseline screenshots, the state matrix, the contrast and target-size checks. Put the riskiest unit next. Decide what fans out, and give each subagent its own scratch directory.
4. **Write the phase list into the todo list** between this step and step 6, and into the evidence pack. That list is what the human reviews.
5. **Run each unit as an experiment.** State the hypothesis, make the smallest change, check it on the rendered artifact, keep it or revert it. A verdict is verified, not verified, or inconclusive, and inconclusive is not a pass. Use **diverge** for a choice between designs and **critique** before any handoff.
6. **Keep the trail.** Log each decision with the **design-log** skill as it happens, not at the end.
7. **Verify the whole** against the step 1 check on the real product, not only the harness. Turn any correction you made twice into a token, component, rule, or lint (**principle-encode-decisions-in-the-system**).
8. A design-producing run ends in **Design handoff** (playbooks/design-handoff.md). An evaluation run ends in its report and pauses before it leaves the session.

**Reply:** the phases you designed and which playbook steps you borrowed, the rigor level and why, the decision log path, what is verified against the step 1 check, the pending user-evidence gates, and what is still open.

**Grounded in:** pstack's figure-it-out skill, adapted (see NOTICE.md).
