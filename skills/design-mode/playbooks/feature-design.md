### Feature design

**You own the design. Model, diverge, converge, specify.** Delegate independent slices. Stay in the lead.

Use it for a new or changed flow. Start from the **Discovery** (playbooks/discovery.md) output, or write a one-line problem, user, and outcome metric first (**principle-frame-the-problem**, **principle-user-outcome-first**). A broken existing flow goes to **UX defect fix** (playbooks/ux-defect-fix.md).

1. Model the objects before any screen (**principle-model-the-objects**). Pull the recurring nouns from the brief and the research. For each object define its relationships, its actions, and its attributes, the way OOUX's ORCA does.
2. Map the flows. Write each task as steps across those objects. Reuse the system's existing patterns and tokens before inventing new ones (**principle-follow-conventions**, **principle-encode-decisions-in-the-system**).
3. Inventory the state matrix. Rows are screens or components by state. States are the UI Stack's ideal, empty, partial, error, and loading, plus the interaction states in **principle-design-every-state** wherever a control has them. Add recovery, undo, and destructive confirmation (**principle-design-for-error-and-reversal**). Columns are viewports. Every cell starts pending.
4. Write the throughput checkpoint as four todo items. A dimension that does not apply keeps its item with `n/a: <reason>`.
   - **Blocking first steps.** Objects, flows, and tokens settle before variant work fans out.
   - **Parallel workstreams.** Independent flows or screens go to separate design-stack:design-agent subagents.
   - **Shared files.** One owner per shared component, token file, or Figma page. Split the target before you serialize writes to it.
   - **Smallest safe decomposition.** If one owner is best, say why.
5. Diverge on the riskiest screen or interaction with the **diverge** skill (**principle-diverge-then-converge**). Variants sit behind one switcher.
6. Converge against written criteria. Use the outcome metric, state coverage, the accessibility target (**principle-accessible-by-default**), cognitive load (**principle-minimize-cognitive-load**), and the regimes from discovery. Record why each variant that lost, lost.
7. Design the chosen direction across every screen in the flows. Fill every matrix cell with a screenshot at each viewport, or `n/a: <reason>`. An empty cell is a defect. Apply the **Content design** (playbooks/content-design.md) rules to every string.
8. Run the **critique** skill on the full flow. Its findings are inspection hypotheses. A question only users can settle becomes a pending gate with a kit per **Usability test** (playbooks/usability-test.md).
9. Record taste and brand calls as open decisions, each with an evidence pack (screenshots per state and viewport, a recommendation, the alternatives). Proceed on the recommendation (**principle-propose-and-proceed**).
10. Write the spec. It covers objects, flows, the full state matrix, the tokens used, content, accessibility notes, and open decisions. Draft it with figma:figma-spec or design:design-handoff if installed.
11. Run **Design handoff** (playbooks/design-handoff.md).

**Reply:** what you designed and who it serves, the objects, and state matrix coverage. Then the variants and why the base won (a table), critique findings labeled as hypotheses, the throughput checkpoint, pending gates, and open decisions.

**Grounded in:** [OOUX ORCA](https://ooux.com/hi/orcaseries), [Object-Oriented UX, A List Apart](https://alistapart.com/article/object-oriented-ux/), [The UI Stack](https://www.scotthurff.com/posts/why-your-user-interface-is-awkward-youre-ignoring-the-ui-stack/), [Carbon component checklist](https://www.carbondesignsystem.com/getting-started/contributing/component-checklist) (IBM, Apache-2.0 via the carbon-website repo, paraphrased), [Double Diamond](https://www.designcouncil.org.uk/our-resources/the-double-diamond/).
