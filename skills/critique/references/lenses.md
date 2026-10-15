# Lenses

This file is the plugin's single finding-ID scheme. Every other skill and playbook cites these IDs.

Each seat gets one section. Check only the items that apply to the surface. Do not force a lens. Cite the item ID in every finding. Rate severity on the 0-4 scale in design-handbook's heuristics.md (`../../design-handbook/references/heuristics.md`), in a separate pass after the findings list exists.

## A. Heuristics

Jakob Nielsen's ten usability heuristics ([10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)), credited and linked as NN/g permits. The checks below are our own wording.

- **H1** Visibility of system status. After every action, can people tell what the system is doing, in time to act on it?
- **H2** Match between system and the real world. Do labels use the users' vocabulary and order things the way their work runs, not the way the database does?
- **H3** User control and freedom. Is there an obvious way back out of a state people entered by mistake?
- **H4** Consistency and standards. Does the same thing look and behave the same everywhere, and match the platform?
- **H5** Error prevention. Does the design remove the conditions that cause slips, and check before a costly commit?
- **H6** Recognition rather than recall. Are the options and facts a step needs on screen, not held in memory from an earlier screen?
- **H7** Flexibility and efficiency of use. Can frequent users go faster without the shortcut getting in a newcomer's way?
- **H8** Aesthetic and minimalist design. Does anything on screen compete with the task without serving it? This is about relevance, not flat styling.
- **H9** Help users recognize, diagnose, and recover from errors. Does each error name the problem in plain words and point to the fix?
- **H10** Help and documentation. Where help is needed, is it easy to find and shaped around the task?

ISO 9241-110:2020 interaction principles, cited by name only ([ISO 9241-110](https://www.iso.org/standard/75258.html)). Use them for enterprise or regulated products, or as a second heuristic set.

- **ISO110-1** Suitability for the user's tasks. Are there steps or fields the task does not need?
- **ISO110-2** Self-descriptiveness. Can people tell what each element does and where they are without outside help?
- **ISO110-3** Conformity with user expectations. Is behavior predictable from context and convention?
- **ISO110-4** Learnability. Can people discover features safely and get help while learning?
- **ISO110-5** Controllability. Do people set the pace and order, and adapt it to themselves? The 2020 edition folds individualization in here.
- **ISO110-6** Use error robustness. Does the design head off errors, absorb the ones it can detect, and make recovery easy?
- **ISO110-7** User engagement. Is the experience inviting enough that people keep using it? New in 2020.

Shneiderman's eight golden rules, cited by name with our own checks ([Eight Golden Rules](https://www.cs.umd.edu/users/ben/goldenrules.html), license unknown). Use them as a third heuristic set or where Nielsen's wording does not fit.

- **SHN-1** Strive for consistency. Do like situations use the same words, steps, and look?
- **SHN-2** Seek universal usability. Does it serve novices and experts, all abilities, locales, and devices?
- **SHN-3** Offer informative feedback. Does every action get a response scaled to how rare and weighty it is?
- **SHN-4** Design dialogs to yield closure. Does each group of steps end with a clear sign it is done?
- **SHN-5** Prevent errors. Are serious errors blocked by design, with a precise, nearby way out when one gets through?
- **SHN-6** Permit easy reversal of actions. Can people undo, at a sensible granularity?
- **SHN-7** Keep users in control. Does the interface avoid acting on its own or shifting habits under people?
- **SHN-8** Reduce short-term memory load. Does any step make people hold more than a few chunks in mind (LAW-WM)?

## B. Accessibility (WCAG 2.2 AA)

Gate on the pinned legal target and the current WCAG edition. Their status lives in design-handbook's accessibility.md (`../../design-handbook/references/accessibility.md`). Confirm each number and level in the [WCAG 2.2](https://www.w3.org/TR/WCAG22/) spec text before citing it. Never cite a criterion number from memory. AA is the gate. AAA items go to Noted unless the objective targets AAA. Against a 2.2 target, never cite 4.1.1 Parsing, which 2.2 removed. A legal target pinned to 2.0 or 2.1 follows accessibility.md.

- **1.4.3** Contrast (Minimum), AA. Text needs 4.5:1, large text 3:1. Large means at least 18pt, or 14pt bold. Compute it with the contrast script named in your prompt. A contrast finding without a computed ratio is not a 1.4.3 finding.
- **1.4.11** Non-text Contrast, AA. Control boundaries, state indicators, and graphics needed to understand content need 3:1 against adjacent colors.
- **1.4.10** Reflow, AA. At 320 CSS px wide, does content work without scrolling in two directions? Inherently two-dimensional content is exempt.
- **2.4.11** Focus Not Obscured (Minimum), AA. Is a focused element ever fully hidden by a sticky header, cookie banner, or chat widget?
- **2.5.7** Dragging Movements, AA. Does every drag have a single-pointer alternative, unless dragging is essential?
- **2.5.8** Target Size (Minimum), AA. Are pointer targets at least 24 by 24 CSS px, or covered by the spacing, equivalent, inline, user-agent, or essential exception ([Understanding 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html))? The 44 by 44 rule is 2.5.5, which is AAA.
- **3.2.6** Consistent Help, A. Does help that repeats across pages stay in the same relative order?
- **3.3.7** Redundant Entry, A. Does the flow ask again for something people already entered in the same process, with no prefill or selection? Re-entry that is essential, required for security, or replacing data no longer valid is exempt.
- **3.3.8** Accessible Authentication (Minimum), AA. Does sign-in demand a cognitive function test, such as remembering, transcribing, or solving a puzzle? It passes when an alternative method exists, a mechanism helps (paste and password managers work), or the test is recognizing objects or personal content the user supplied.
- **4.1.2** Name, Role, Value, A. In the accessibility snapshot, does every control expose a name, a role, and its state?
- **2.2.2 and 2.3.3** Motion. Moving, blinking, or scrolling content that starts on its own and lasts over five seconds, and auto-updating content, fall under 2.2.2 (A), which asks for a pause, stop, hide, or update-frequency control unless the content is essential. Motion triggered by interaction falls under 2.3.3 (AAA), where honoring prefers-reduced-motion is a sufficient technique ([Understanding 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)).

Designer-level checks from WAI's [Designing for Web Accessibility](https://www.w3.org/WAI/tips/designing/) tips. Each tip links its criteria. Look the number up there before citing one. Until then, cite the tip by name.

- **TIP-COLOR** Color is never the only cue. Pair it with text, shape, or pattern.
- **TIP-FOCUS** Hover, focus, and active states are distinct, and focus is visible on every interactive element.
- **TIP-LABEL** Every form field has a visible label placed next to it.
- **TIP-FEEDBACK** Confirmations and errors are noticeable and specific.
- **TIP-HIER** Headings and spacing make the hierarchy visible.
- **TIP-ALT** Alt text, captions, and transcripts are planned in the design.

Known gap. The research did not record the criterion numbers behind these tips, so this lens names them by tip.

Inspection limits. Automated rules such as [axe-core](https://github.com/dequelabs/axe-core) find on average 57% of WCAG issues and leave the rest for manual review, so alt-text quality, focus-order sense, and cognitive load need a human pass. GOV.UK pairs automated, manual, and assistive-technology testing ([Testing for accessibility](https://www.gov.uk/service-manual/helping-people-to-use-your-service/testing-for-accessibility)). Record any screen-reader pass you could not run as a pending gate.

## C. Cognition and laws in scope

Cite a law only inside the scope its source tested (**principle-cite-the-law-in-scope**). [Laws of UX](https://lawsofux.com/) is an index, not a source. Several of its one-liners repeat folk versions that the items below correct.

- **LAW-WM** Working memory. Does a step make people carry facts from one screen to the next? Current estimates put central capacity near 3 to 5 chunks ([Cowan 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/)). Menus rely on recognition, so the old Miller span is not a cap on menu length ([NN/g](https://www.nngroup.com/articles/short-term-memory-and-web-usability/)).
- **LAW-HICK** Hick-Hyman. Choice reaction time grows with the log of equally likely alternatives, measured by Hick with up to ten stimuli ([Hick 1952](https://cir.nii.ac.jp/crid/1361418518753603072)). Menu selection can be bound by visual scanning instead ([Landauer and Nachbar 1985](https://dl.acm.org/doi/10.1145/1165385.317470)). Never use it to cap a menu.
- **LAW-CHOICE** Choice overload. The meta-analytic mean effect is near zero, with high variance ([Scheibehenne et al. 2010](https://academic.oup.com/jcr/article/37/3/409/1827647)). Cutting options is a hypothesis to test, not a rule.
- **LAW-FITTS** Fitts. Movement time rises with the index of difficulty, log2(A/W + 1) in the Shannon form ([MacKenzie](https://www.yorku.ca/mack/hhci2018.html)). Are frequent targets small or far from where the pointer rests?
- **LAW-RESP** Response time. Does feedback arrive fast enough to keep people in the task? Aim for sub-second response ([Doherty and Thadhani 1982](https://jlelliotton.blogspot.com/p/the-economic-value-of-rapid-response.html)). Cite no stricter threshold.
- **LAW-AUE** Aesthetic-usability. Polish raises perceived ease more than measured ease ([NN/g](https://www.nngroup.com/articles/aesthetic-usability-effect/)). A beautiful screen is not evidence that it works.
- **LAW-GROUP** Grouping. Does visual grouping (proximity, similarity, common region, connectedness) match the real relationships in the content ([Wagemans et al. 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3482144/))?
First-use walkthrough. For a task a newcomer must complete, ask four questions at each step. Any no fails the step ([NN/g cognitive walkthrough](https://www.nngroup.com/articles/cognitive-walkthroughs/)). You run it as the evaluator, so it is tier 1 inspection.

- **CW-1** Goal. Will people try for this result, knowing the step is needed for what they came to do?
- **CW-2** Visibility. Will they notice that the right control is there?
- **CW-3** Association. Will they link that control to the result they want?
- **CW-4** Progress. After the action, will they see that it worked?

## D. Conventions and system consistency

- **SYS-CONV** Convention. Does the design break a pattern people know from the platform or from products like it? A break needs a reason the user would feel. Pair with H4 and ISO110-3.
- **SYS-TOKEN** Tokens. Does every color, type, and spacing value on screen map to a design-system token? Untokenized values are defects ([Carbon component checklist](https://www.carbondesignsystem.com/getting-started/contributing/component-checklist), IBM, Apache-2.0 via the carbon-website repo, paraphrased). Each one usually traces to a decision nobody wrote down ([@JeffWitters](https://x.com/JeffWitters/status/2109729064206364748)).
- **SYS-COMP** Components. Is the same job done by the same component, with no near-duplicate variants?
- **SYS-ISTATE** Interaction states. Does each component show the interaction states in **principle-design-every-state** that apply to it?
- **SYS-SSTATE** Screen states. Are the ideal, empty, partial, error, and loading states each designed ([The UI Stack](https://www.scotthurff.com/posts/why-your-user-interface-is-awkward-youre-ignoring-the-ui-stack/))?
- **SYS-WORST** Worst-case content. Does the layout survive long or unbreakable strings, missing fields, zero and huge counts, and non-Latin text ([emilkowalski/skills break-ui](https://github.com/emilkowalski/skills))?
- **SYS-WIG** Interface rules. On a live web UI, check focus rings that sticky UI covers, zoom disabled, state missing from the URL, and destructive actions with no confirm or undo ([Vercel Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines), MIT). Run Vercel's web-design-guidelines skill for file:line findings if installed.

## E. Content

Adapted from GOV.UK guidance under the Open Government Licence v3.0, and from Digital.gov guides (CC0, per the [site repository licence](https://github.com/GSA/digitalgov.gov/blob/main/LICENSE.md)).

- **CNT-NEED** User need. Can each piece of copy be traced to a need the user has at that moment ([Understand content design](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/understand-content-design/))?
- **CNT-EXPLAIN** Explaining the UI. Copy that explains how to work the interface signals an interface defect. Report the interface ([Writing for user interfaces](https://www.gov.uk/service-manual/design/writing-for-user-interfaces)).
- **CNT-ERR** Error messages. Does each error say what went wrong and how to fix it, with no jokes, and no apology in validation errors? GOV.UK keeps "sorry" for serious failures, such as the service being down.
- **CNT-SENSE** Sensory references. Does any instruction point by color or position alone?
- **CNT-WORDS** Plain words. Are things named in the audience's language, not the system's ([Digital.gov plain language](https://digital.gov/guides/plain-language))?
- **CNT-ACTION** Action names. Does each button say what it does, and does the action keep one name through the flow ([frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design))?
- **CNT-EMPTY** Empty states. Does an empty screen tell people what to do first?
- **CNT-I18N** Translation. Will the strings survive longer translations and right-to-left scripts where the product ships them ([W3C i18n quick tips](https://www.w3.org/International/quicktips/))?

## F. Ethics and deceptive patterns

Name the pattern and the source that describes it. Rate severity with the harm anchors (money, data, consent, time lost) in heuristics.md, not the usability anchors. Legal status is for counsel, so do not give legal advice. Patterns stack, so walk the whole flow, not one screen ([FTC 2022 staff report](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf)).

Types from the [deceptive.design catalogue](https://deceptive.design/types/), in our own words:

- **ETH-CANCEL** Leaving is harder than joining.
- **ETH-PRESELECT** The option that benefits the business is selected by default.
- **ETH-SNEAK** Price, recurring charges, or added items are hidden or revealed late.
- **ETH-PRESSURE** Shaming the decline, repeated nagging, or invented urgency, scarcity, or popularity.
- **ETH-WORDING** Wording, layout, or ad styling that misleads, hides information, or blocks comparison.

Regulatory hooks:

- **ETH-ART25** [DSA Article 25](https://www.eu-digital-services-act.com/Digital_Services_Act_Article_25.html) bars online platforms from deceptive or manipulative interfaces. It names three practices for Commission guidance: more prominence for one choice, re-asking a settled choice, and making cancelling harder than subscribing.
- **ETH-EDPB** For consent and privacy UI, use the six [EDPB 03/2022](https://www.edpb.europa.eu/documents/guideline/guidelines-032022-on-deceptive-design-patterns-in-social-media-platform_en) categories: Overloading, Skipping, Stirring, Obstructing, Fickle, and Left in the dark. Check the whole account lifecycle, from sign-up to deletion.
- **ETH-CHILD** If under-18s are likely users, are privacy defaults high, with no nudge toward weaker privacy ([ICO Children's code](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/))?

Known gap. The legal status of the FTC click-to-cancel rule was not verified. Do not cite it.
