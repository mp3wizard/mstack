---
name: principle-deprecate-through-a-lifecycle
description: "Apply when replacing a design-system component, pattern, or token. Retire the old one through named lifecycle states, migrate every usage, and remove it only when nothing uses it. Never keep old and new in parallel with no end date."
disable-model-invocation: true
---

# Deprecate Through a Lifecycle

When a component or pattern is replaced, the old one leaves through named states, in order.

1. **Flag the old one.** If it fails accessibility, usability, or build requirements, mark it use with caution. Advise against new uses either way.
2. **Ship the replacement** to the system's stable bar, with migration notes. Where consumers must change code, ship a codemod.
3. **Mark the old one deprecated** with a removal date. It stays available, gets no updates, and its docs point to the replacement. For a token, set the DTCG `$deprecated` property.
4. **Migrate every usage.** Inventory them in code and in design files. Diff each migrated screen against its pinned visual baseline.
5. **Remove it** once usage reaches zero. That is the end of its lifecycle.

- A deprecation period can be long. It cannot be open-ended.
- An adapter between old and new is temporary. It gets the same removal date.
- Never delete a token silently. `$deprecated` comes first.
- Never remove first and migrate later. Consumers find out from a broken screen.

**Why:** Two live versions of one component double every review, split the visual language, and make the system append-only. A removal without a migration breaks the people who build on it. The lifecycle orders the steps so neither happens.

## Grounded in

- [USWDS component lifecycle](https://designsystem.digital.gov/components/lifecycle/) (GSA, CC0 and US public domain), the four phases Proposal, Development, Released, and Deprecated, plus the use with caution flag on a released component.
- [Carbon component checklist](https://www.carbondesignsystem.com/getting-started/contributing/component-checklist) (IBM, Apache-2.0 via the carbon-website repo, paraphrased), the draft to stable status ladder, deprecate before removal, and codemods for breaking changes.
- [DTCG Format Module 2025.10](https://www.designtokens.org/tr/2025.10/format/) (W3C Design Tokens Community Group, Community Final Specification Agreement), the `$deprecated` token property.
