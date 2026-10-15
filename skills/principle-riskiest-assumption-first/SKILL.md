---
name: principle-riskiest-assumption-first
description: "Apply when sequencing design work or choosing what to prototype. Rank the assumptions by risk and test the one whose failure kills the idea first, at the lowest fidelity that answers it."
disable-model-invocation: true
---

# Riskiest Assumption First

Every design rests on assumptions about users, value, feasibility, and the rules around it. Test the one whose failure would kill the idea before polishing anything that depends on it.

- List the assumptions. Break each candidate solution into the beliefs that must hold for it to work. Collect the risks every discipline sees (user, technical, legal, integration).
- Rank them by risk. Early on, test value (does this solve a real problem anyone has) before feasibility (can we build it).
- Write each one as a falsifiable hypothesis. Name the users, the change, the predicted outcome, and the signal that would prove it wrong.
- Set an appetite. Decide how much time the question is worth before you start. If the risk is not retired inside that budget, stop and decide again instead of extending.
- Do the least work that answers it. Prototype only the part that carries the risk, not the whole journey.
- Climb the fidelity ladder one rung at a time and stop at the first rung that answers the question. Each rung ends in a check.
  1. Sketch. Check it against the framed problem and the object model.
  2. Wireframe. Walk the key task through it step by step.
  3. Clickable prototype. Drive the flow on the real surface and screenshot each state.
  4. High fidelity. Inspect contrast, every state, and worst-case content.
  5. Built. Verify the rendered artifact (**principle-prove-it-with-evidence**).
- Know what a rung proves. Every check above is inspection (tier 1), so its result is a hypothesis. When the answer needs users, prepare a study kit. A value question (does anyone have this problem) goes to the **Interview study** playbook (../design-mode/playbooks/interview-study.md). A usability question (can people use this design) goes to the **Usability test** playbook (../design-mode/playbooks/usability-test.md). Record the pending gate (**principle-never-fabricate-user-evidence**).
- Throw the prototype away. Prototype code never becomes production code without a rebuild. The validated prototype is the spec, not the codebase.
- Accept a no-go. If the riskiest assumption fails, stop, or go back to discovery. That result saves the build.

**Why:** Polish on a design whose core assumption is false is wasted. Testing the riskiest belief first, at the cheapest fidelity, keeps the work reversible while it is still cheap to change.

## Grounded in

- [How the alpha phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works) (GOV.UK Service Manual, OGL v3), for testing the riskiest assumptions with prototypes just complex enough to test them, expecting to throw the code away, and stopping or repeating as legitimate outcomes.
- [Lean UX Canvas v2](https://jeffgothelf.com/blog/leanuxcanvas-v2/) (Jeff Gothelf, all rights reserved), for picking the riskiest thing to learn first, value before feasibility early on, and the least work to learn it. The author has since replaced the canvas with the Lean Product Canvas.
- [Opportunity solution trees](https://www.producttalk.org/opportunity-solution-trees/) (Product Talk, all rights reserved), for breaking solutions into assumptions and testing the most important first.
- [Shape Up](https://basecamp.com/shapeup) (37signals, all rights reserved), for appetite as a time budget set before design, low-fidelity shaping, and the circuit breaker that cancels instead of extending.
- [Dual-Track Agile](https://www.svpg.com/dual-track-agile/) (SVPG, all rights reserved), for validating with prototypes before production code, with the validated prototype as the spec for delivery.
