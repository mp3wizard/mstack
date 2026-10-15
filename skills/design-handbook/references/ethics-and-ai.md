# Ethics and AI

Deceptive patterns and the rules that reach them, children's privacy, AI-feature guidance, motion, and sustainability. Name the legal hook as a pointer for counsel. Counsel owns the legal verdict (**principle-cite-the-law-in-scope**, **principle-honest-design**).

## Deceptive pattern families

deceptive.design (formerly darkpatterns.org) is the standard catalogue. It is all rights reserved, so link it, describe each type in your own words, and never vendor it. Each type there links to the laws and enforcement actions that targeted it. [Source](https://deceptive.design/types/), [terms](https://deceptive.design/legal/terms-and-conditions/).

| Family | In our words |
|---|---|
| Hard to cancel | Joining is easy. Leaving is made deliberately hard. |
| Preselection | The option that serves the business is already ticked or selected. |
| Sneaking, hidden costs, hidden subscription | Price, recurring charges, or added items surface late or never. |
| Pressure | Confirmshaming, nagging, fake urgency, fake scarcity, and fake social proof push with emotion or invented cues. |
| Misdirection | Trick wording, visual interference, disguised ads, and comparison prevention mislead or hide what matters. |

## EDPB Guidelines 03/2022

European Data Protection Board, version 2.0, adopted 14 Feb 2023. Grounded in the GDPR. Written for social media, but it applies to any consent or privacy interface. Reuse is allowed with the source acknowledged. Assess the whole account lifecycle, sign-up to deletion, with an interdisciplinary team. [Source](https://www.edpb.europa.eu/documents/guideline/guidelines-032022-on-deceptive-design-patterns-in-social-media-platform_en), [PDF](https://www.edpb.europa.eu/system/files/2023-02/edpb_03-2022_guidelines_on_deceptive_design_patterns_in_social_media_platform_interfaces_v2_en_0.pdf).

| Category | In our words (named sub-types) |
|---|---|
| Overloading | A flood of requests, options, or text pushes users to share more (continuous prompting, privacy maze, too many options). |
| Skipping | The journey makes users forget about data protection (deceptive snugness, look over there). |
| Stirring | Emotion or visual nudges steer the choice (emotional steering, hidden in plain sight). |
| Obstructing | Getting informed or managing data is made hard or impossible (dead end, longer than necessary, misleading action). |
| Fickle | Inconsistent, unclear design hides privacy controls (lacking hierarchy, decontextualising, inconsistent interface, language discontinuity). |
| Left in the dark | Information or controls are hidden, or data use stays unclear (conflicting information, ambiguous wording). |

## FTC staff report (Sep 2022)

*Bringing Dark Patterns to Light*, FTC Bureau of Consumer Protection. A US government work, but its license was not confirmed, so paraphrase. [Source](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf).

- It treats dark patterns as interface designs that trick or manipulate people into choices they would not have made, with possible harm. It credits Harry Brignull with the term, in 2010.
- It cites a study where dark patterns doubled sign-ups for a dubious identity theft protection service compared with a neutral interface.
- Patterns stack. Combined patterns have stronger effects than any one alone, so audit whole flows, not single screens.
- The FTC click-to-cancel rule's legal status is unverified. Do not cite it.

## DSA Article 25

Regulation (EU) 2022/2065, online platforms. The text below is our gist. EUR-Lex blocked the fetch, so the research read a secondary transcription. [Source](https://www.eu-digital-services-act.com/Digital_Services_Act_Article_25.html), [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2065).

- **25(1).** Platforms may not design or run interfaces that deceive or manipulate users, or that otherwise seriously impair free and informed decisions.
- **25(2).** Practices already covered by the Unfair Commercial Practices Directive (2005/29/EC) or the GDPR (2016/679) fall outside it.
- **25(3).** The Commission may issue guidelines on (a) giving one choice more prominence when asking for a decision, (b) asking again for a choice already made, especially through interrupting pop-ups, and (c) making it harder to end a service than to subscribe.

## ICO Age appropriate design code (Children's code)

OGL v3.0, adaptable with attribution. A statutory UK code of 15 flexible standards for online services likely to be used by under-18s. The child's best interests come first. Privacy defaults are high. Nudges toward weaker privacy are out. Privacy information is concise, prominent, and pitched at the child's age. [Source](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/).

1. Best interests of the child
2. Data protection impact assessments
3. Age appropriate application
4. Transparency
5. Detrimental use of data
6. Policies and community standards
7. Default settings
8. Data minimisation
9. Data sharing
10. Geolocation
11. Parental controls
12. Profiling
13. Nudge techniques
14. Connected toys and devices
15. Online tools

Contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

## AI features

**Microsoft HAX Guidelines for Human-AI Interaction.** License unknown, so link only and add no guidance text. Eighteen guidelines synthesized from over 20 years of research and introduced in a CHI 2019 paper. They are grouped by when they apply (initially, during interaction, when the system is wrong, over time). The HAX Workbook helps a team prioritize them and the Design Library shows patterns. This plugin holds no guideline titles, so fetch the list from the source before walking them in **AI feature design** (../../design-mode/playbooks/ai-feature-design.md). [Source](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/).

**Google PAIR People + AI Guidebook.** CC BY-NC-SA 4.0, so link only and never blend its text into this plugin. Its chapters cover user needs and defining success, data collection and evaluation, mental models and expectations, explainability and trust, feedback and controls, and errors and graceful failure. It also asks whether AI belongs in the task at all. [Source](https://pair.withgoogle.com/guidebook/).

## Motion

- **Carbon productive vs expressive** (IBM, Apache-2.0 via the carbon-website repo, paraphrased). Productive motion is quick and subtle, for task flow and micro-interactions. It is the default. Expressive motion is vivid and kept for occasional important moments. Duration tokens run from fast-01 at 70 ms to slow-02 at 700 ms. Use the tokens, not ad hoc durations. [Source](https://carbondesignsystem.com/elements/motion/overview/).
- **Reduced motion by default.** WCAG 2.2 SC 2.3.3 Animation from Interactions is AAA. Follow it anyway. Honor `prefers-reduced-motion` (C39 in CSS, SCR40 in script) for any non-essential motion a user action triggers. Parallax is a common offender. Motion that starts by itself falls under 2.2.2 Pause, Stop, Hide (A). [Source](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html).
- **Implementation rules.** See the Vercel motion rules in design-systems.md. Delegate review to emil-design-eng or improve-animations if installed.

## Sustainability

W3C Web Sustainability Guidelines. A Group Note Draft dated 24 Sep 2026, not endorsed by W3C or its Members, under the permissive document license. Treat it as an advisory lens, never a gate. Section 2 (User Experience Design) holds 2.1 to 2.17. The ones that touch mstack's work are 2.4 efficient journeys, 2.5 assist rather than distract, 2.6 avoid manipulation and deception, 2.8 use a design system, 2.10 proportionate and controllable animation, and 2.12 no unwanted notifications. Use them to reinforce an honest-design or motion finding, not to fail a design. [Source](https://www.w3.org/TR/web-sustainability-guidelines/).
