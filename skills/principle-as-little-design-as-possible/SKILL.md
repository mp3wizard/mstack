---
name: principle-as-little-design-as-possible
description: "Apply when tempted to add a screen, control, option, component, help text, or decoration. Reuse an existing pattern first, remove before adding, and fix the interface instead of explaining it."
disable-model-invocation: true
---

# As Little Design as Possible

Reach for new design only after reuse and removal have failed. The best change to a crowded screen is often a deletion.

- Reuse before you invent. Check the design system, the product, and the platform for a pattern that already solves this. A new component must do something no existing one does, backed by evidence that people need it (**principle-encode-decisions-in-the-system**).
- Remove before you add. Every element on a screen competes for attention with the ones that matter. Cut what does not serve the task first.
- Fix the interface, not the help text. If a screen needs instructions to be usable, the screen is the defect (**principle-fix-the-design-cause**). Keep labels and hints short.
- Spend boldness once. Give one element the distinctive treatment and hold the rest back. Ornament that does nothing for the brief comes out.
- Fix the time and let the scope flex. Set the time budget first, then cut scope to fit it. Mark the nice-to-haves so they go first.
- Every control and option earns its place or goes. "This does not earn its place" is a valid answer.

**Why:** Each added element costs attention for every user, upkeep for every implementer, and consistency for the whole system. Those costs recur. The benefit of an addition has to be shown.

## Misuse caveats

- Minimal does not mean flat or bare. Stripping signifiers, labels, or feedback to look clean breaks use (**principle-signify-and-give-feedback**). Nielsen's aesthetic and minimalist heuristic targets irrelevant information, not visual style.
- Never remove accessibility affordances such as focus indicators, text alternatives, or error text to simplify (**principle-accessible-by-default**).
- Removing a feature people use is a deprecation, not a cleanup (**principle-deprecate-through-a-lifecycle**).

Adapted in part from the GOV.UK Service Manual and GOV.UK Design System (Open Government Licence v3.0) and Anthropic's frontend-design skill (Apache-2.0).

## Grounded in

- [Ten principles for good design](https://www.vitsoe.com/us/about/good-design) (Dieter Rams via Vitsoe, CC BY-NC-ND 4.0, link only), for the principle this skill is named after.
- [10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) (Jakob Nielsen, NN/g, all rights reserved), heuristic 8 for cutting information that competes with what matters, and heuristic 10 for the ideal of needing no help.
- [Contribution criteria](https://design-system.service.gov.uk/community/contribution-criteria/) (GOV.UK Design System, OGL v3), for adding a component only when it is useful and unique, with evidence of need before any design or code.
- [Writing for user interfaces](https://www.gov.uk/service-manual/design/writing-for-user-interfaces) (GOV.UK Service Manual, OGL v3), for fixing an interface that needs explaining, and keeping help text and labels short.
- [Shape Up](https://basecamp.com/shapeup) (37signals, all rights reserved), for fixed time with variable scope, scope hammering, and marking nice-to-haves.
- [frontend-design skill](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) (Anthropic, Apache-2.0), for concentrating boldness in a single element and removing ornament the brief does not need.
