### Prototype

**You own the design decision, not the artifact. The prototype is a throwaway instrument and never becomes production.**

Speed over polish. The rigor is in asking the right question at the lowest fidelity that can answer it.

1. Scope the one decision the prototype exists to make. Name the assumption it tests and the result that would change the decision. No decision means no prototype. Route to **Feature design** (playbooks/feature-design.md).
2. Pick the riskiest assumption and the lowest fidelity that answers it (**principle-riskiest-assumption-first**). A flow question may need only a breadboard or a rough sketch. A layout or density question needs rendered pixels. A timing or motion question needs the real interaction.
3. Build and cross-judge the variants through the **diverge** skill. It owns the fan-out (Phase B), the variant dirs, and the switcher page, so spawn no builders of your own. Give it the constraints. Plain HTML, CSS, and JS or the lightest stack that renders the idea, isolated from production source. No production framework, no tests, no abstractions. Every variant labeled.
4. Verify on the matching surface. Screenshot every variant in each state and viewport that matters, with the built-in browser or the Playwright MCP if installed. Drive the interaction yourself. This is tier 1 inspection, not a user test, so label what it shows as a hypothesis.
5. If only users can settle the assumption, prepare a kit against the prototype per **Usability test** (playbooks/usability-test.md) and record a pending gate. Report user reactions only from sessions a human ran (**principle-never-fabricate-user-evidence**).
6. Present the variants, the evidence, the tradeoffs, and a recommendation. Record the taste call as an open decision with the screenshots attached, and proceed on the recommendation (**principle-propose-and-proceed**).
7. Hand the recommended direction and the open decision to **Feature design** (playbooks/feature-design.md) for the real build, which ends in **Design handoff** (playbooks/design-handoff.md). Never promote prototype code.

**Reply:** the decision under test, the variants, the evidence (screenshot paths per variant and state), the tradeoffs, your recommendation, the open taste decision, any pending gate, and the scratch path. Say plainly that the prototype is throwaway.

**Grounded in:** [GOV.UK alpha phase](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works), [Lean UX Canvas v2](https://jeffgothelf.com/blog/leanuxcanvas-v2/) (the author has since replaced it with the Lean Product Canvas), [Shape Up](https://basecamp.com/shapeup).
