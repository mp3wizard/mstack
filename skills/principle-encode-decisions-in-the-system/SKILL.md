---
name: principle-encode-decisions-in-the-system
description: "Apply when a raw color, type, spacing, radius, or motion value appears, or when the same review finding comes back a second time. Resolve every value to a token, and turn recurring findings into system rules, lints, or templates instead of more prose."
disable-model-invocation: true
---

# Encode Decisions in the System

A design decision lives in the system or it does not exist. Every color, type, spacing, radius, and motion value resolves to a named token. A raw value is a defect, even when it looks right.

- **Tokens before the brief.** Load the product's tokens and its DESIGN.md (or equivalent) before you describe or generate any screen. Without them the model drifts to its own default look.
- **One format, versioned.** Store tokens in the DTCG Format Module 2025.10 (`$value`, `$type`, aliases by curly-brace path, `.tokens.json`). Name the version. It is a stable Community Group report, not a W3C Standard.
- **Audit what renders.** Crawl the running UI, not only the source, and list every off-system value. Most trace to a decision nobody wrote down. Encode it as a token or remove it.
- **Recurring findings become structure.** A finding that comes back across reviews becomes a token, a component variant, a lint rule, or a template. One more paragraph in a style guide is the symptom, not the fix.
- **Judgment calls get prominence.** If a lesson needs judgment and cannot be encoded, make the rule prominent and add an example of the failure.
- **Contribute back.** A pattern you built because the system lacked it goes back with its evidence of need. It passes the system's contribution gate before anyone calls it a component.
- **Accessibility too.** Bake contrast-checked color pairs, focus styles, and target sizes into tokens and components, so each screen inherits them instead of rechecking by hand.

**Why:** Agents ignore written style guides and fall back on defaults. A token or a lint fails loudly every time. Prose fails silently.

## Misuse caveats

- Do not mint a token per one-off value. In new design, prefer the nearest existing token. In a refactor, snapping changes pixels, so route it per design-system-refactor step 4 (../design-mode/playbooks/design-system-refactor.md). A new token needs a second use or a named reason.
- DESIGN.md files extracted from other brands are format examples. Never ship them as your system.

## Grounded in

- [DTCG Format Module 2025.10](https://www.designtokens.org/tr/2025.10/format/) (W3C Design Tokens Community Group, Community Final Specification Agreement), token shape, aliases, file conventions, and the report's status.
- [Carbon component checklist](https://www.carbondesignsystem.com/getting-started/contributing/component-checklist) (IBM, Apache-2.0 via the carbon-website repo, paraphrased), specs and styles use only system tokens and no magic numbers.
- [GOV.UK Design System contribution criteria](https://design-system.service.gov.uk/community/contribution-criteria/) (Crown copyright, OGL v3), evidence of need before a component enters the system.
- [W3C Accessibility Maturity Model](https://www.w3.org/TR/maturity-model/) (W3C Group Note, cite and paraphrase), maturity as practice built into the development life cycle and backed by proof points.
- [@JeffWitters](https://x.com/JeffWitters/status/2109729064206364748) and [@tiennguyendev](https://x.com/tiennguyendev/status/2104745477308604733) on X (authors' copyright, link only), off-system values trace to unwritten decisions, and tokens loaded before the brief stop drift.
