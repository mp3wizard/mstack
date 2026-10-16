### Investigation

**You own the answer. Walk, read, cite.** Investigation is read-only. It produces a cited explanation or a recommendation, never a design change.

Use it for "how does this flow work", "why was it designed this way", "why do people drop at this step", and "are we sure".

1. Walk the live UI yourself on the matching surface, with the built-in browser or the Playwright MCP if installed. Capture a screenshot for every step and every state you reach. Write the flow as numbered steps, the way an 18F task flow analysis does.
2. Read the design files and the decision history. Read Figma frames, annotations, comments, and version history per references/figma.md (Figma MCP or Figma Console MCP), else use exported frames or screenshots the user supplies. Read specs, tickets, decision records, research reports, and commit history for the why. For a metric symptom, read the funnel and analytics (tier 2) to find the step where users drop and the group it hits.
3. For a "how" question, run a cognitive walkthrough over each step as the evaluator, asking CW-1 to CW-4 from ../critique/references/lenses.md, and note where a first-time user would stall. For a "why" question, cite the decision record. When no record exists, say so and label the reason inferred.
4. Label every inspection finding as a hypothesis per the evidence-tier rule in **design-mode**. Cite tier 2 evidence where it exists. Never fill a gap with imagined user reactions (**principle-never-fabricate-user-evidence**).
5. Answer with the evidence and the tradeoffs. A choice between alternatives gets a tradeoffs table, not a prototype. A rationale that leans on a UX law states the law's original scope (**principle-cite-the-law-in-scope**).
6. For "are we sure", give your real judgment with reasons. Push back when the premise is wrong.
7. Change nothing. If a change should follow, name the playbook and do not start it. A broken flow goes to **UX defect fix** (playbooks/ux-defect-fix.md). A new or changed flow goes to **Feature design** (playbooks/feature-design.md). A broad quality question goes to **Heuristic review** (playbooks/heuristic-review.md).
8. Write the answer up with its screenshots and sources. Pause before sharing the report outside the session (see Autonomy in the router).

**Reply:** the answer first. Then the walked flow with screenshot paths, the sources cited, the tradeoffs, which claims are hypotheses, and the playbook a change would need.

**Grounded in:** [ISO 9241-210:2019](https://www.iso.org/standard/77520.html), [NN/g cognitive walkthroughs](https://www.nngroup.com/articles/cognitive-walkthroughs/), [Figma Dev Mode guide](https://help.figma.com/hc/en-us/articles/15023124644247-Guide-to-Dev-Mode), [18F Methods](https://github.com/18F/guides/tree/main/content/methods).
