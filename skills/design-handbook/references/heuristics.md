# Heuristics and inspection frames

Inspection predicts likely problems. It does not prove usability. Label every inspection finding as a hypothesis until users confirm it. Evaluator counts and coverage numbers are in research-numbers.md. Finding IDs (H1 to H10, ISO110-1 to ISO110-7, SHN-1 to SHN-8, CW-1 to CW-4) follow [lenses.md](../../critique/references/lenses.md), the plugin's one ID scheme.

## Contents

- [Nielsen's 10 usability heuristics](#nielsens-10-usability-heuristics)
- [ISO 9241-110:2020 interaction principles](#iso-9241-1102020-interaction-principles)
- [Shneiderman's eight golden rules](#shneidermans-eight-golden-rules)
- [Norman's interaction concepts](#normans-interaction-concepts)
- [Tognazzini's First Principles](#tognazzinis-first-principles-of-interaction-design)
- [Rams's ten principles](#ramss-ten-principles)
- [Severity ratings](#severity-ratings), the plugin's one 0 to 4 scale
- [Cognitive walkthrough](#cognitive-walkthrough)

## Nielsen's 10 usability heuristics

Jakob Nielsen, Nielsen Norman Group. Refined in 1994 from a factor analysis of 249 usability problems. NN/g lets you apply the heuristics if you credit and link them. The article text stays theirs, so the lines below are our own. [Source](https://www.nngroup.com/articles/ten-usability-heuristics/).

| ID | Heuristic | In our words |
|---|---|---|
| H1 | Visibility of system status | Show what is happening now, with prompt feedback. |
| H2 | Match between system and the real world | Use the words and the order people already know from the world. |
| H3 | User control and freedom | Give a plain way back from any wrong turn (undo, cancel, back). |
| H4 | Consistency and standards | One meaning per word and control, and platform conventions honored. |
| H5 | Error prevention | Design out the setups that invite errors. Where you cannot, ask before acting. |
| H6 | Recognition rather than recall | Keep options and needed facts in view so nothing must be remembered. |
| H7 | Flexibility and efficiency of use | Fast paths for frequent users that beginners can ignore. Let people customize. |
| H8 | Aesthetic and minimalist design | Cut what competes with the content that matters. It is not a mandate for flat style. |
| H9 | Help users recognize, diagnose, and recover from errors | Error messages name the problem without codes and point to a fix. |
| H10 | Help and documentation | Ideally nobody needs it. When someone does, they find the answer fast and get steps for their task. |

## ISO 9241-110:2020 interaction principles

The international-standard counterpart to Nielsen's list. Paywalled and all rights reserved, so cite clause numbers and names only. The 2020 edition merged individualization into controllability and added user engagement. Use it as a second lens in regulated or enterprise work. [Source](https://www.iso.org/standard/75258.html).

| ID | Clause | Principle | In our words |
|---|---|---|---|
| ISO110-1 | 5.1 | Suitability for the user's tasks | Supports the task without needless steps or information. |
| ISO110-2 | 5.2 | Self-descriptiveness | What the system can do, and how, is evident where it is needed. |
| ISO110-3 | 5.3 | Conformity with user expectations | Behavior is predictable from context and convention. |
| ISO110-4 | 5.4 | Learnability | Supports discovery and exploration, with help while learning. |
| ISO110-5 | 5.5 | Controllability | The user sets pace, sequence, and individual settings. |
| ISO110-6 | 5.6 | Use error robustness | Helps avoid errors, tolerates the identifiable ones, supports recovery. |
| ISO110-7 | 5.7 | User engagement | Draws people in and keeps them motivated to use it. |

## Shneiderman's eight golden rules

From *Designing the User Interface*, 6th ed. (2016), section 3.3.4. The original list dates from 1985. License unknown, so names plus our own words. The author says the rules need validation and tuning for each domain. [Source](https://www.cs.umd.edu/users/ben/goldenrules.html).

- **SHN-1 Strive for consistency.** Like situations use the same words, steps, and look. Exceptions are rare and explainable.
- **SHN-2 Seek universal usability.** Serve novices and experts, all ages and abilities, locales, and devices.
- **SHN-3 Offer informative feedback.** Each action gets a visible response. Rare, weighty actions get a bigger one than routine ones.
- **SHN-4 Design dialogs to yield closure.** Group steps into units that finish with a clear sign of completion.
- **SHN-5 Prevent errors.** Block serious errors by design. When one gets through, show a precise, nearby way out.
- **SHN-6 Permit easy reversal of actions.** Undo makes trying things safe. Choose sensibly what one undo reverses.
- **SHN-7 Keep users in control.** People steer. The interface does not act on its own or shift habits under them.
- **SHN-8 Reduce short-term memory load.** The page still cites 7 ± 2. Keep the rule, use Cowan's 3 to 5 chunks (ux-laws.md).

## Norman's interaction concepts

From *The Design of Everyday Things*, revised and expanded edition (2013), which added signifiers. The book is all rights reserved. [Source](https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/).

- **Affordance.** The actions possible between an object and a particular person. A relationship, not a property.
- **Signifier.** A perceivable cue for where and how to act. Designers mostly add signifiers, not affordances.
- **Mapping.** How controls relate to their effects. A natural mapping needs no label.
- **Feedback.** Immediate, informative word on what an action did, without overload.
- **Constraints.** Physical, cultural, semantic, and logical limits that steer toward correct use.
- **Conceptual model.** A simplified account of how the system works, carried by the system image.
- **Discoverability.** People can work out what actions exist and how to perform them.
- **Gulfs of execution and evaluation.** Check both gaps, knowing what to do and telling what happened. The seven stages of action trace them.
- **Slips and mistakes.** Classify each error, then trace it to a design cause instead of blaming the user.

## Tognazzini's First Principles of Interaction Design

Copyright Bruce Tognazzini. Personal-use copies only, with the notice kept. Names only here. Its depth suits a thorough critique pass better than a fast inspection. [Source](https://asktog.com/atc/principles-of-interaction-design/).

Aesthetics, Anticipation, Autonomy, Color, Consistency, Defaults, Discoverability, Efficiency of the user, Explorable interfaces, Fitts's Law, Human interface objects, Latency reduction, Learnability, Metaphors, Protect users' work, Readability, Simplicity, State, Visible navigation.

## Rams's ten principles

Dieter Rams, published by Vitsoe under CC BY-NC-ND 4.0. Short paraphrased names only. A quality and ethics lens that complements usability heuristics. [Source](https://www.vitsoe.com/us/about/good-design).

Innovative. Useful. Aesthetic. Understandable. Unobtrusive. Honest. Long-lasting. Thorough to the last detail. Environmentally friendly. As little design as possible.

## Severity ratings

The plugin's one severity scale. Every file that rates a finding uses it and points here instead of restating it. Rate in a separate pass after the findings list exists, never during the hunt.

| Rating | Usability anchors | Harm anchors | design-qa label |
|---|---|---|---|
| 0 | Not a usability problem. | No harm. | Not logged |
| 1 | Cosmetic. Fix if time allows. | Mild annoyance. Seconds lost, nothing at stake. | Nit |
| 2 | Minor. Low priority. | Minutes lost, or a nudge the person can easily reverse. | Medium |
| 3 | Major. High priority. | Money, personal data, or consent taken without a clear choice, or a reversal that takes real effort. | High |
| 4 | Catastrophe. Fix before release. | Loss the person cannot easily undo, such as unwanted charges, data shared without consent, or no workable exit. | Blocker |

- **Usability anchors.** Nielsen's scale, for usability findings. [Source](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/).
- **Harm anchors.** This plugin's own anchors, for ethics and deceptive-pattern findings. They weigh money, data, consent, and time lost.
- **design-qa labels.** Blocker is 4, High is 3, Medium is 2, Nit is 1.

Nielsen's severity combines three factors, plus market impact.

- **Frequency.** How often the problem occurs. Inspection cannot see this. Without tier 2 data such as analytics or logs, mark the judgment "estimated, no tier 2 data".
- **Impact.** How hard it is to overcome when it does.
- **Persistence.** Whether people learn their way past it or hit it every time.

Each rater rates alone. One rater is unreliable, so NN/g uses the mean of about three. Parallel model passes share a model and prompts, so they are not independent raters. Report their spread and label their mean "model-panel mean, not independent raters". Where severity decides the next step, such as a 3 or 4 going to a usability test, the human designer rates it.

## Cognitive walkthrough

A task-based inspection for first-time learnability. A cross-functional team walks the correct action sequence of a predefined task. A recorder logs the answers. At each step the team checks four criteria. [Source](https://www.nngroup.com/articles/cognitive-walkthroughs/).

- **CW-1 Goal.** The user knows this step is needed for what they came to do.
- **CW-2 Visibility.** The control for the step is in view or easy to find.
- **CW-3 Association.** Its label and form tell the user it produces that result.
- **CW-4 Progress.** What follows the action shows the step worked.

A step that fails any criterion is a likely failure point. The walkthrough complements heuristic evaluation. Heuristics catch general violations, the walkthrough catches the step where a newcomer would not know what to do.
