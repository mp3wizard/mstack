---
name: principle-accessible-by-default
description: "Apply when a design, component, palette, or flow is specified or reviewed, starting in discovery. Pin the conformance target early and meet it in the design itself, with computed checks and real assistive-technology testing."
disable-model-invocation: true
---

# Accessible by Default

Accessibility is a requirement set in discovery, not a pass before launch.

- **Pin the target in discovery.** Write it into the todo list. Default to WCAG 2.2 Level AA. Record any legal floor that differs, such as EN 301 549 in the EU, Section 508 for US federal work, or the GOV.UK Service Manual. Gate on the pinned legal target and the current WCAG edition. Their current versions and legal status live in `../design-handbook/references/accessibility.md`. Read them there, never from memory.
  - Content that conforms to 2.2 also conforms to 2.1 and 2.0. When the pinned legal target is 2.0 or 2.1, record 4.1.1 Parsing per that edition, which 2.2 removed.
  - The laws also add requirements beyond WCAG, such as Section 508's functional performance criteria and hardware chapters ([Access Board](https://www.access-board.gov/ict/)) and EN 301 549's own clauses, such as clause 8 Hardware.
- **Native HTML before ARIA.** A role promises the full behavior, and wrong ARIA misleads more than none. For a custom widget, copy the matching APG pattern's keyboard model, roles, and states into the spec.
- **Compute contrast, never eyeball it.** Run `../design-mode/scripts/contrast.py <fg> <bg>` for every text and UI color pair in every state. Build its absolute path from this skill's base directory. Text needs 4.5:1, large text 3:1 (1.4.3, AA). Component boundaries and state indicators need 3:1 (1.4.11, AA).
- **Targets at least 24x24 CSS px** (2.5.8, AA), with exceptions for spacing, equivalent controls, inline text, user-agent controls, and essential cases. Per-platform sizes live in **principle-follow-conventions**.
- **Keep focus visible and unobscured.** Give every focusable element a visible focus style (W3C designer tips). Sticky headers, cookie banners, and chat widgets must not fully hide the focused item (2.4.11, AA).
- **Never rely on color alone.** Pair color with text, shape, or pattern (W3C designer tips).
- **Respect reduced motion.** Honor `prefers-reduced-motion` for motion the user triggers. That criterion (2.3.3) is AAA, so this plugin adopts it as a default, not as an AA requirement. Motion that starts on its own falls under 2.2.2 at Level A.
- **Research with disabled people.** Include disabled participants and assistive-technology users at every phase (GOV.UK). Recruiting is a human's job. Put it in the study kit and never stand in for those participants (**principle-never-fabricate-user-evidence**).
- **Automated checks are never sufficient.** axe-core finds on average 57% of WCAG issues automatically and flags others as incomplete for manual review ([axe-core](https://github.com/dequelabs/axe-core)). Whether alt text is meaningful, whether focus order makes sense, and how heavy the cognitive load is still need a person. Combine automated, manual, and assistive-technology testing (GOV.UK), and report automated results as partial coverage.

**Why:** Many accessibility failures, such as low contrast, color-only meaning, and invisible focus, are decided in the design. WAI's designer tips cover them ([W3C designer tips](https://www.w3.org/WAI/tips/designing/)). The design phase is where they get fixed or shipped.

## Misuse caveats

- design:accessibility-review, if installed, lists 2.5.5 as AA in its quick reference. 2.5.5 Target Size (Enhanced) is AAA. Cite WCAG directly for levels.
- APCA is not a gate. The [WCAG 3 Working Draft](https://www.w3.org/TR/wcag-3.0/) leaves its contrast algorithm undetermined, so APCA may appear as an advisory column only.
- A clean scan is not conformance. An evaluation statement follows WCAG-EM 2 in **Accessibility audit** (../design-mode/playbooks/accessibility-audit.md).
- [Inclusive Design Principles](https://inclusivedesignprinciples.info/) (CC BY-SA) are a critique lens. Link them, never adapt their text.

## Grounded in

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) (W3C Document License, cite and paraphrase), criteria and levels.
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) (W3C), native first and widget keyboard models.
- [GOV.UK, making your service accessible](https://www.gov.uk/service-manual/helping-people-to-use-your-service/making-your-service-accessible-an-introduction) and [Testing for accessibility](https://www.gov.uk/service-manual/helping-people-to-use-your-service/testing-for-accessibility) (Crown copyright, OGL v3), the 2.2 AA minimum, research with disabled people, three kinds of testing.
- [axe-core](https://github.com/dequelabs/axe-core) (Deque, MPL-2.0), about 57% of WCAG issues found automatically and the rest left for manual review.
- [EN 301 549 V4.1.1 update](https://accessible-eu-centre.ec.europa.eu/content-corner/news/european-accessibility-standard-en-301-549-has-been-updated-2026-09-07_en) (AccessibleEU Centre, European Commission, license not checked), the EU standard. Its current legal status lives in accessibility.md.
- [Revised Section 508 Standards](https://www.access-board.gov/ict/) (U.S. Access Board, federal work, no license stated), functional performance criteria and hardware requirements beyond WCAG.
- [WCAG 2.2 Understanding 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html) (W3C), reduced motion as a AAA criterion with a CSS technique.
