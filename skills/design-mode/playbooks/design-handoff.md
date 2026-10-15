### Design handoff

**You own the package the builders work from. Every design-producing playbook ends here.**

Communicating the design to the people who build it is its own activity in ISO 9241-210 (clause 7.4.5). Write one package per change in the project and link it from the reply.

1. **Problem and outcome.** The user need, the behavioral outcome, and the success metric from **Discovery** (playbooks/discovery.md) or **Measure** (playbooks/measure.md). If neither exists, propose one per Measure step 1 and label it a proposal.
2. **Design and alternatives.** The chosen design, each alternative rejected, and why.
3. **Objects and flows.** The object model, the flows, and their entry and exit points.
4. **State matrix.** Screens by content state (ideal, empty, partial, error, loading) by breakpoint. Components by the interaction states in **principle-design-every-state**, at one breakpoint. A screenshot in each cell. Unreachable combinations get `n/a: <reason>`.
5. **Content.** Every string by screen and state, the error messages, and i18n and RTL notes, per **Content design** (playbooks/content-design.md).
6. **Tokens.** Every value by token name. A raw value is a defect (**principle-encode-decisions-in-the-system**).
7. **Behaviors.** Overflow and truncation, responsive rules, and motion with token durations and a `prefers-reduced-motion` alternative. Default to quick, task-focused motion.
8. **Accessibility.** The conformance target, gated on the pinned legal target and the current WCAG edition (see ../design-handbook/references/accessibility.md). Then the APG pattern, focus order, accessible names and labels, target sizes, and the computed contrast pairs (**principle-accessible-by-default**).
9. **Instrumentation.** The events per HEART signal from **Measure** (playbooks/measure.md), each with its name, properties, and trigger. Without a metrics plan, list them as a labeled proposal.
10. **Acceptance criteria.** Checkable statements per state, plus the baseline that **Design QA** (playbooks/design-qa.md) will diff against.
11. **Evidence pack.** Screenshots per state and viewport, the **critique** verdict, inspection findings labeled as hypotheses, and the decision log.
12. **Pending gates and open decisions.** Each missing piece of user evidence with its kit path. Each taste, brand, product, or risk call for a human, with its evidence pack and your recommendation (**principle-never-fabricate-user-evidence**, **principle-propose-and-proceed**).
13. **Format.** Use design:design-handoff, figma:figma-spec, or uxui-bcif-handoff:uxui-bcif-handoff if installed. Otherwise write markdown beside the design files.
14. **Pause before it leaves the session.** Sending, posting, sharing, marking Figma frames ready for dev, and publishing a library all wait for a human. List the open decisions in the reply. Use AskUserQuestion at most once, as the very last action, and never under a session override ("don't stop", "going to bed").

**Reply:** the package path, state matrix coverage, pending user-evidence gates, and open decisions with your recommendation.

**Grounded in:** [ISO 9241-210:2019](https://www.iso.org/standard/77520.html), [Carbon component checklist](https://www.carbondesignsystem.com/getting-started/contributing/component-checklist) (IBM, Apache-2.0 via the carbon-website repo, paraphrased), [The UI Stack](https://www.scotthurff.com/posts/why-your-user-interface-is-awkward-youre-ignoring-the-ui-stack/), [Figma Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247-Guide-to-Dev-Mode), [Carbon motion](https://carbondesignsystem.com/elements/motion/overview/) (IBM, Apache-2.0 via the carbon-website repo, paraphrased).
