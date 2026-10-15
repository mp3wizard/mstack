---
name: principle-follow-conventions
description: "Apply when choosing a pattern, control, term, or size, or when porting a design to another platform. Follow the conventions users already know and the target platform's own numbers before inventing anything."
disable-model-invocation: true
---

# Follow Conventions

People arrive with habits learned in every other product they use. Design so what they already know works here.

- **External consistency first.** Use the controls, words, icons, and placements people know from other products and from the platform (Nielsen H4, the idea [Laws of UX](https://lawsofux.com/) calls Jakob's law). Invent a pattern only when the convention fails the task.
- **Use the target platform's numbers.** There is no single universal size. Apply each platform's own guidance to that platform.
  - On the web, pointer targets are at least 24x24 CSS px, with exceptions ([WCAG 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), AA). [Vercel's guidelines](https://github.com/vercel-labs/web-interface-guidelines/blob/main/README.md) ask for 44 px on mobile.
  - On iOS and iPadOS, Apple HIG sets a 44x44 pt default and a 28x28 pt minimum.
  - Material 3 asks for 48x48 dp touch targets, 44x44 dp pointer targets, and about 8 dp between targets.
  - For Fluent 2, read Fluent's current guidance. This plugin holds no verified target number for it.
- **Internal consistency.** The same action uses the same sequence, term, and treatment everywhere in the product (Shneiderman rule 1).
- **Different things look different.** A control that behaves differently must not borrow another control's look. Tognazzini grades how strict consistency must be by level, so consistency never means making everything identical.
- **Continuity across releases.** Prefer continuity over novelty in a redesign (Tognazzini, [USWDS principles](https://designsystem.digital.gov/maturity-model/)). Move a familiar control only when the gain outweighs relearning, and tell people what moved.

**Why:** ISO 9241-110 names conformity with user expectations as an interaction principle. Behavior should be predictable from context and convention. Breaking an expectation costs relearning and causes mistakes in NN/g's sense, errors from a mental model that no longer matches the design.

## Misuse caveats

- A pattern being common does not make it acceptable. Never copy a deceptive pattern because competitors use it (**principle-honest-design**).
- A convention that fails accessibility is not one to follow (**principle-accessible-by-default**).
- Platform numbers are not interchangeable. Cite the platform the design ships on.

## Grounded in

- [10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) (NN/g, all rights reserved, use with credit and link), H4 consistency and standards.
- [First Principles of Interaction Design](https://asktog.com/atc/principles-of-interaction-design/) (Bruce Tognazzini, personal-use copies only), levels of consistency and continuity.
- [ISO 9241-110:2020](https://www.iso.org/standard/75258.html) (ISO, all rights reserved, clause names only), conformity with user expectations.
- [Apple HIG, accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) (Apple, all rights reserved, link only), iOS and iPadOS control sizes.
- [Material Design 3, structure](https://m3.material.io/foundations/designing/structure) (Google, guideline text license unknown), touch and pointer targets.
- [Fluent 2 design tokens](https://fluent2.microsoft.design/design-tokens) (Microsoft Terms of Use for site text), Fluent's own system.
