---
name: principle-user-outcome-first
description: "Apply when scoping a design, weighing tradeoffs, or setting success criteria. Name the users and the change in their behavior the design must produce, and solve their whole journey, not one screen."
disable-model-invocation: true
---

# User Outcome First

A design task is done when named people can do something they could not do before. Screens existing is not the finish line. Name the people and the change before designing.

- Name the users. Include everyone the design touches, not only the primary customer. Admins, buyers, and front-line staff count.
- State the outcome as a change in behavior. "People renew without calling support" is an outcome. "A renewal page" is an output. Keep user outcomes (what people gain) apart from business outcomes (what the organization measures).
- Make the outcome observable before building. Say which signal will show it moved (**principle-explain-the-metric**).
- Solve the whole problem. Scope the design to the user's journey from first need to done, across organizations, not to the one screen the ticket names.
- Join up the channels. The online, phone, paper, and in-person steps of one journey must agree.
- When the user's outcome and implementation convenience pull apart, the outcome wins. Existing processes are soft constraints. Change them instead of making users work around them.
- The people who build and maintain the design are users too. A spec the implementer cannot follow, or a component the next designer cannot extend, fails them. Say what they inherit.
- Ground the user description in explicit knowledge of users, tasks, and environments (tier 2 or tier 3 evidence). Where that is missing, the description is a hypothesis (**principle-never-fabricate-user-evidence**).

**Why:** Output is easy to count and says nothing about whether anyone is better off. A screen that works on its own can still break the journey around it.

## Grounded in

- [ISO 9241-210:2019](https://www.iso.org/standard/77520.html) (ISO, all rights reserved, clause names only), for clause 5.2 (explicit understanding of users, tasks and environments), 5.3 (users involved throughout), 5.6 (the whole user experience), and 7.4.5 (communicating the design solution to the people who implement it).
- [GOV.UK Service Standard](https://www.gov.uk/service-manual/service-standard) (GOV.UK, OGL v3), points 1 to 3 for understanding users and their needs, solving a whole problem, and a joined-up experience across all channels.
- [Lean UX Canvas v2](https://jeffgothelf.com/blog/leanuxcanvas-v2/) (Jeff Gothelf, all rights reserved), for outcomes defined as behavior change, user outcomes kept distinct from business outcomes, and users that include admins and buyers. The author has since replaced the canvas with the Lean Product Canvas.
- [How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) (GOV.UK Service Manual, OGL v3), for the wider journey across organizations and offline channels, and for changing soft constraints instead of working around them.
