---
name: principle-diverge-then-converge
description: "Apply when a design decision has more than one plausible answer. Generate real alternatives before choosing, one of them deliberately rejecting the default look, then converge on criteria written down in advance."
disable-model-invocation: true
---

# Diverge, Then Converge

Never pick a design before real alternatives exist. Never generate alternatives without a convergence step whose criteria are written first.

- Diverge on purpose. Produce at least three alternatives that differ in structure or interaction, not only in color or copy.
- Make one variant reject the default. Left undirected, a model reaches for the most probable look in its training data. Write down what the generic answer would be, then build one variant that departs from it on every axis the brief leaves free. Where the brief fixes a direction, follow it, even when it names a common look.
- Draw variants from people, not only from aesthetics. A persona spectrum (one ability, taken as a permanent, a temporary, and a situational case) yields genuinely different designs.
- Borrow from elsewhere. Look at how adjacent services and other domains handle the same need.
- Write the convergence criteria before you look at the variants. Derive them from the framed problem, the user outcome, and the constraints.
- Converge against those criteria. Put the variants side by side behind one switcher, score each criterion with evidence (screenshots, a walkthrough, inspection findings), pick a base, and graft the strongest parts of the others onto it. The **diverge** skill runs this loop.
- Record what was rejected and why. A rejected variant is evidence for the next decision.
- When convergence shows the framing was wrong, go back to **principle-frame-the-problem**, not to more variants.

**Why:** A model's unprompted design is the most probable one, not the one this brief needs. Divergence without convergence yields a mood board, not a decision. Criteria written after seeing the options bend toward a favorite.

## Misuse caveats

- Variants on a settled decision are waste. If the system already has a pattern for this, reuse it (**principle-as-little-design-as-possible**).
- Choosing on taste alone is still taste. When the criteria tie, record the call as an open decision with its evidence pack and keep working (**principle-propose-and-proceed**).
- Diverge at the lowest fidelity that shows the difference (**principle-riskiest-assumption-first**).

## Grounded in

- [Framework for Innovation](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/) (Design Council, CC BY 4.0), for two diamonds that alternate wide exploration with focused convergence, and for Develop borrowing ideas from elsewhere.
- [Systemic Design Framework](https://www.designcouncil.org.uk/our-resources/systemic-design-framework/) (Design Council, CC BY 4.0), for keeping the diverge and converge premise in complex, cross-sector work.
- [Improving frontend design through Skills](https://claude.com/resources/articles/improving-frontend-design-through-skills) (Anthropic, license unknown), for distributional convergence as the source of the generic AI look.
- [frontend-design skill](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) (Anthropic, Apache-2.0), for reviewing a design plan against the generic default before building, with an explicit brief taking precedence.
- [Inclusive 101 guidebook](https://inclusive.microsoft.design/articles/inclusive-101-guidebook) (Microsoft, all rights reserved), for the persona spectrum across permanent, temporary, and situational cases.
