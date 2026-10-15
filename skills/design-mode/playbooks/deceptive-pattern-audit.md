### Deceptive pattern audit

**You own the flow walk and the honest alternative. The audit names the legal hook. Counsel owns the legal verdict.**

1. Walk the whole account lifecycle. That means sign-up, checkout, consent and privacy settings, subscription, cancel, and account deletion. Walk it on staging with test accounts and test payment methods. Never complete a real purchase, subscription, cancellation, or deletion. Where a step needs a real transaction, screenshot up to the commit control, record the rest as a gap, and pause per Autonomy in the router so a human can walk it. Screenshot every step. Count the steps to get in and the steps to get out (**principle-prove-it-with-evidence**).
2. Tag each finding with a deceptive.design type (hard to cancel, preselection, sneaking, confirmshaming, fake urgency, trick wording, and so on) and its ID in the critique lenses (../critique/references/lenses.md). Where personal data is involved, add an EDPB 03/2022 category (Overloading, Skipping, Stirring, Obstructing, Fickle, Left in the dark). Describe each in your own words and link the catalogue.
3. Attach the legal hook that fits, as a pointer for counsel (**principle-cite-the-law-in-scope**):
   - DSA Art. 25 for online platforms, except practices already covered by the GDPR or the Unfair Commercial Practices Directive. Art. 25(3) names unequal prominence of choices, re-asking a settled choice, and cancelling harder than subscribing.
   - The GDPR, read through the EDPB guidelines, when the pattern touches personal data or consent.
   - The ICO Age appropriate design code when under-18s are likely users. High-privacy defaults, no nudges toward weaker privacy.
   - The FTC 2022 staff report for US consumer-protection context.
4. Rate severity in a separate pass once the findings list is complete. Use the 0 to 4 scale with its harm anchors in the handbook's heuristics reference (../design-handbook/references/heuristics.md). Mark any reach judgment "estimated, no tier 2 data" unless you cite analytics. Rate stacked patterns above each one alone, since the FTC report finds combined patterns have stronger effects.
5. Propose the honest alternative for every finding, and prototype it when cheap (**principle-honest-design**). Cancel takes no more steps than sign-up. Optional boxes start unticked. Accept and refuse get equal weight. The full price, recurring charges included, shows before commitment. A choice once made is not asked again.
6. Report. Findings by flow with type, lens ID, EDPB category, hook, severity, screenshot, and the honest alternative, plus the gaps a human must walk.
7. Pause before sharing the report outside the session (see Autonomy in the router).

**Reply:** the flows walked with step counts in and out, the stacked patterns, and the gaps left for a human walk.

**Grounded in:** [deceptive.design: Types](https://deceptive.design/types/), [EDPB Guidelines 03/2022 v2.0](https://www.edpb.europa.eu/documents/guideline/guidelines-032022-on-deceptive-design-patterns-in-social-media-platform_en), [DSA Article 25](https://www.eu-digital-services-act.com/Digital_Services_Act_Article_25.html), [ICO Age appropriate design code](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/), [FTC: Bringing Dark Patterns to Light](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf).
