---
name: principle-honest-design
description: "Apply when designing sign-up, consent, pricing, cancellation, upsell, notification, or AI-driven flows. The interface serves the user's own decision, so nothing tricks, pressures, hides, or overstates."
disable-model-invocation: true
---

# Honest Design

The interface serves the user's decision, not the conversion metric. Nothing tricks, pressures, hides, or overstates.

- **No deceptive patterns.** Check whole flows, not single screens, because patterns stacked in one flow do more harm than any one alone (FTC 2022). Use the deceptive.design catalogue and the six EDPB categories (overloading, skipping, stirring, obstructing, fickle, left in the dark) as the checklist. EDPB wrote them for social media, and they apply to any consent or privacy screen.
- **Leaving is as easy as joining.** Cancelling takes no more steps than subscribing. Hard to cancel has the most recorded examples in the deceptive.design catalogue.
- **Equal choices get equal weight.** Accept and reject sit at the same level with the same prominence. Never re-ask a choice the user already made.
- **Nothing that benefits the business is preselected.** Opt-ins start unchecked. Price, recurring charges, and extras appear up front, not at the last step.
- **Children get the child's best interest.** For services likely to be used by under-18s, privacy defaults start high and nothing nudges toward weaker privacy (ICO Children's code).
- **Never overstate capability.** Claims, labels, and previews match what the product does ([Rams' honesty principle](https://www.vitsoe.com/us/about/good-design), link only).
- **AI features admit their limits.** At first use, say what the system can do and how well. When it is wrong, the user can dismiss and correct it, and the UI explains why it acted (Microsoft HAX). This plugin also requires undo for any change the AI makes. [PAIR](https://pair.withgoogle.com/guidebook/) covers the same ground (link only).

**Why:** Deceptive patterns work. The FTC report cites a study where they doubled sign-ups for a dubious service compared with a neutral interface. They also carry legal exposure. The EDPB applies the GDPR to them, the DSA bars online platforms from deceptive interfaces, and the FTC ties common patterns to enforcement cases.

## Misuse caveats

- DSA Article 25 applies to online platforms only and excludes practices already covered by the UCPD or the GDPR. Its third paragraph names prominence, re-asking, and hard cancelling as areas where the Commission may issue guidance. Cite it as context, not as a universal rule, and send legal calls to a human.
- Do not cite the FTC click-to-cancel rule. Its legal status is unverified.
- Honest does not mean no defaults. A default is fine when it serves the user and is easy to change.

## Grounded in

- [Types of deceptive pattern](https://deceptive.design/types/) (Testimonium Ltd, all rights reserved, link only), the pattern catalogue.
- [EDPB Guidelines 03/2022 v2.0](https://www.edpb.europa.eu/documents/guideline/guidelines-032022-on-deceptive-design-patterns-in-social-media-platform_en) (EDPB, reuse with acknowledgment), the six categories and whole-lifecycle review.
- [Bringing Dark Patterns to Light](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf) (FTC staff report 2022, public-domain status unconfirmed), stacking and the sign-up study.
- [DSA Article 25](https://www.eu-digital-services-act.com/Digital_Services_Act_Article_25.html) (Regulation (EU) 2022/2065, page license unknown), prominence, re-asking, and cancelling.
- [ICO Age appropriate design code](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/) (ICO, OGL v3), 15 standards, best interests, high-privacy defaults.
- [Microsoft HAX Toolkit](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/) (Microsoft, license unknown), 18 guidelines for human-AI interaction.
