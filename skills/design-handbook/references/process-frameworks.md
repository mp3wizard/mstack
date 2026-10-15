# Process frameworks

Which framework fits which job, and where each one hands off to engineering. Pick one spine per project and borrow methods from the rest. Every framework here gates on evidence from real users. That evidence is tier 3, so the agent prepares the study and never supplies the verdict (**principle-never-fabricate-user-evidence**).

## Contents

- [Which framework when](#which-framework-when)
- [GOV.UK service phases](#govuk-service-phases)
- [GOV.UK Service Standard](#govuk-service-standard)
- [Double Diamond and the Framework for Innovation](#double-diamond-and-the-framework-for-innovation)
- [Systemic Design Framework](#systemic-design-framework)
- [ISO 9241-210:2019](#iso-9241-2102019)
- [18F Methods](#18f-methods)
- [USDS Digital Services Playbook](#usds-digital-services-playbook)
- [Lean UX](#lean-ux)
- [Continuous discovery and opportunity solution trees](#continuous-discovery-and-opportunity-solution-trees)
- [Shape Up](#shape-up)
- [GV Design Sprint](#gv-design-sprint)
- [Continuous discovery and delivery (formerly dual-track agile)](#continuous-discovery-and-delivery-formerly-dual-track-agile)

## Which framework when

| Situation | Use | Handoff to engineering |
|---|---|---|
| Public or regulated service with assessment gates | GOV.UK phases and Service Standard | Alpha to beta. Engineers sit in the team throughout. |
| The problem is unclear and needs framing first | Double Diamond (Framework for Innovation) | None formal. Deliver ends at small-scale tested solutions. |
| Complex, cross-sector, or climate challenge | Systemic Design Framework | Catalyse scales change. It is not a build spec. |
| Conformance language or an audit trail is required | ISO 9241-210:2019 | Clause 7.4.5 |
| One step needs a method | 18F Methods | Make produces testable designs. Validate tests them. |
| Assessing a team's service practice | USDS Digital Services Playbook | Play 4, an MVP within three months |
| Agile team testing hypotheses | Lean UX | Smallest experiment inside the sprint |
| Ongoing discovery against one outcome | Continuous discovery and opportunity solution trees | A winning idea refined for delivery |
| Fixed time budgets and shaped bets | Shape Up | The pitch, then one six-week cycle |
| One critical question in one week | GV Design Sprint | None. The output is test data. |
| Discovery and delivery run in parallel | Continuous discovery and delivery (formerly dual-track agile) | The validated prototype is the spec |

## GOV.UK service phases

OGL v3.0, adaptable with attribution. The most fully gated lifecycle here, and stopping is a legitimate outcome at every gate.

- **Discovery.** Typically 4 to 8 weeks. Learn the users, constraints, and policy intent. Restate any pre-set solution as a user problem and write what is out of scope. Consider options that need no build (content, partners, better staff information, open data). Do not build the service. Exit to alpha only if a viable, cost-effective service exists. Carry forward the wider context, a ranked list of ideas to test, a team shape, and success measures.
- **Alpha.** Typically 6 to 8 weeks. Prototype only enough to test the riskiest assumptions (user, technical, legal, integration). Keep it non-public and expect to throw the code away. Exit to beta only with confidence that user needs can be met cost-effectively, with the budget and people to do it (research budget included), explained against the success metrics. Otherwise stop or repeat.
- **Beta.** Build it for real. Run a private beta first, then pass a beta assessment to open a public beta. Test accessibility regularly and research with disabled people. Fix audit issues and publish an accessibility statement before public beta. Keep any legacy service running.
- **Live.** Keep iterating. Check the metrics still tell you what you need. Test changes across devices and channels. Retire the service when it is no longer needed.
- **Handoff.** Engineers are in the multidisciplinary team in every phase. The real build transition is alpha to beta. New patterns go back to the GOV.UK Design System.

Contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). Sources. [Discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works), [alpha](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works), [beta](https://www.gov.uk/service-manual/agile-delivery/how-the-beta-phase-works), [live](https://www.gov.uk/service-manual/agile-delivery/how-the-live-phase-works).

## GOV.UK Service Standard

OGL v3.0. Fourteen points. Services are assessed against them at the alpha, beta, and live assessments ([alpha](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works), [beta](https://www.gov.uk/service-manual/agile-delivery/how-the-beta-phase-works), [live](https://www.gov.uk/service-manual/agile-delivery/how-the-live-phase-works)). Use it as a ready-made assessment rubric. [Source](https://www.gov.uk/service-manual/service-standard).

1. Understand users and their needs
2. Solve a whole problem for users
3. Provide a joined up experience across all channels
4. Make the service simple to use
5. Make sure everyone can use the service
6. Have a multidisciplinary team
7. Use agile ways of working
8. Iterate and improve frequently
9. Create a secure service which protects users' privacy
10. Define what success looks like and publish performance data
11. Choose the right tools and technology
12. Make new source code open
13. Use and contribute to open standards, common components and patterns
14. Operate a reliable service

Contains public sector information licensed under the Open Government Licence v3.0.

## Double Diamond and the Framework for Innovation

Design Council, CC BY 4.0, adaptable with attribution. The Double Diamond launched in 2004. Two diamonds alternate wide exploration with focused convergence. [Source](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/).

- **Discover** (diverge). Find out what the problem really is by spending time with the people affected.
- **Define** (converge). Reframe the challenge from what discovery found.
- **Develop** (diverge). Generate several different answers, borrowing ideas and co-designing.
- **Deliver** (converge). Test candidates at small scale, drop what fails, improve what works.
- **Not linear.** Learning can send a team back to an earlier diamond. Early prototypes are allowed in discovery. Products keep iterating after launch.
- **Four principles.** Put people first. Communicate visually and inclusively. Collaborate and co-create. Iterate repeatedly.
- **Around it.** A methods bank grouped as Explore, Shape, and Build, and a culture layer of leadership and engagement.
- **Handoff.** None formal. Pair it with GOV.UK gates or Shape Up for the build.

Adapted from Design Council, Framework for Innovation, licensed under CC BY 4.0. [Double Diamond](https://www.designcouncil.org.uk/our-resources/the-double-diamond/).

## Systemic Design Framework

Design Council, CC BY 4.0. For complex, cross-sector, and climate-related challenges. It keeps the diverge and converge premise with four stages, Explore, Reframe, Create, and Catalyse. Catalyse (scaling and sustaining change) sits where the Double Diamond has Deliver. Four invisible activities surround the stages (orientation and vision setting, connections and relationships, leadership and storytelling, continuing the journey). Four roles carry it (systems thinker, connector or convener, designer or maker, leader or storyteller). Its Designing for Legacy series covers closing a project so later work can build on it. [Source](https://www.designcouncil.org.uk/our-resources/systemic-design-framework/).

Adapted from Design Council, Systemic Design Framework, licensed under CC BY 4.0.

## ISO 9241-210:2019

Human-centred design for interactive systems. Paywalled and all rights reserved, so cite clause numbers and write the content in your own words. It is the only framework here with conformance language. [Source](https://www.iso.org/standard/77520.html).

| Clause | Topic, in our words |
|---|---|
| 5.2 to 5.7 | Six principles. Documented understanding of users, tasks, and environments. Users involved throughout. Evaluation drives refinement. Iteration. The whole user experience. Multidisciplinary skills. |
| 6 | Planning human-centred design into the project plan |
| 7.2 | Understanding and specifying the context of use |
| 7.3 | Specifying user requirements |
| 7.4 | Producing design solutions |
| 7.4.5 | Communicating the design solution to the people who implement it (title read from the contents only) |
| 7.5 | Evaluating the design |
| 7.5.4, 7.5.5 | User-based testing and inspection-based evaluation as separate routes |
| 7.5.6 | Long-term monitoring after release |
| Annex B | Conformance checklist |

The 7.5.4 and 7.5.5 split grounds the evidence tiers in **design-mode**. Inspection never stands in for user-based testing.

## 18F Methods

CC0 and US public domain, so method cards may be adapted directly. Cite them anyway. `methods.18f.gov` and `guides.18f.gov` no longer resolve, and the `18F/methods` repo was archived on 2024-05-31. Use `18F/guides`. [Source](https://github.com/18F/guides/tree/main/content/methods).

- **Discover.** Understand the problem and the people. Contextual inquiry, stakeholder and user interviews, cognitive walkthrough, heuristic evaluation.
- **Decide.** Turn research into insights and design hypotheses. Affinity mapping, journey mapping, service blueprint, task flow analysis. Personas only from real research.
- **Make.** Produce testable designs. Prototyping, wireframing, a design pattern library.
- **Validate.** Test design hypotheses with users. Usability testing, card sorting, multivariate testing.
- **Fundamentals.** Recruiting, privacy, participant compensation.

Each card gives what, why, time required, and how to do it. Some also add an 18F example, further resources, and government considerations.

## USDS Digital Services Playbook

CC0 and US public domain. Thirteen plays, each with a checklist and key questions, so it works as an assessment rubric. The repo moved from `whitehouse/playbook` to [`usds/playbook`](https://github.com/usds/playbook). [Source](https://playbook.usds.gov/).

1. Understand what people need
2. Address the whole experience, from start to finish
3. Make it simple and intuitive
4. Build the service using agile and iterative practices
5. Structure budgets and contracts to support delivery
6. Assign one leader and hold that person accountable
7. Bring in experienced teams
8. Choose a modern technology stack
9. Deploy in a flexible hosting environment
10. Automate testing and deployments
11. Manage security and privacy through reusable processes
12. Use data to drive decisions
13. Default to open

Handoff. Play 4 asks for a functioning MVP that solves a core user need within three months of the project start, with frequent usability tests.

## Lean UX

All rights reserved. Link and paraphrase. Hypothesis-driven, outcome-focused design inside agile teams. Lean UX defines no formal stage gates. This plugin treats a falsifiable hypothesis plus the smallest experiment that tests the riskiest assumption as the gate. The Lean UX Canvas has been replaced by the Lean Product Canvas and the Lean Strategy Canvas, so start new work from those. [Source](https://jeffgothelf.com/blog/leanuxcanvas-v2/).

Handoff. Experiments run inside the sprint. NN/g's study of agile teams advises design to work one step ahead of the development sprint, and finds skipped research is the main failure mode. [Source](https://www.nngroup.com/articles/doing-ux-agile-world/).

## Continuous discovery and opportunity solution trees

Teresa Torres, Product Talk. No open license, so paraphrase. The team that builds the product talks with customers at least weekly. [Source](https://www.producttalk.org/2021/08/continuous-discovery/).

- The tree's root is one desired outcome. Below it sits the opportunity space (needs, pain points, desires from real interviews), then solutions for one target opportunity, then assumption tests.
- It needs a defined outcome and a few story-based interviews first. Without real interview input the tree means nothing.
- Exit by refining a winning idea for delivery, or by picking a new target opportunity.

[Source](https://www.producttalk.org/opportunity-solution-trees/).

## Shape Up

Basecamp (37signals). All rights reserved, free to read. Senior people shape work before anyone bets on it. They set an appetite (a time budget, not an estimate), sketch at low fidelity, remove rabbit holes, and write a pitch. A betting table during a two-week cool-down chooses pitches. A team then builds for one uninterrupted six-week cycle. By default a circuit breaker cancels work that does not ship within the cycle. Handoff is the pitch. [Source](https://basecamp.com/shapeup).

## GV Design Sprint

All rights reserved. A five-day, time-boxed process that answers one critical business question with a realistic prototype tested with customers on the last day. It needs the right challenge, a decider, a cross-functional team, and cleared calendars. The output is test data, not a build spec. The customer test is tier 3, so the agent prepares the kit and a human runs it. See **Design sprint** (../../design-mode/playbooks/design-sprint.md). [Source](https://www.gv.com/sprint/).

## Continuous discovery and delivery (formerly dual-track agile)

SVPG, all rights reserved. Marty Cagan stopped using "dual-track agile" from INSPIRED V2 onward. He now says continuous discovery and continuous delivery. Discovery yields validated backlog items while delivery yields releasable software, in parallel. The product manager, designer, and lead engineer work together instead of relaying artifacts. Handoff is the validated prototype, which serves as the spec for delivery. [Source](https://www.svpg.com/dual-track-agile/).
