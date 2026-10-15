---
name: principle-frame-the-problem
description: "Apply when a task arrives framed as a solution, or its problem statement has never been tested. Restate it as a user need with its evidence, say what is out of scope, and list the no-build options before any screen."
disable-model-invocation: true
---

# Frame the Problem

A request for a screen, a button, or a dashboard is a proposed solution. Before designing it, turn it back into the problem it is meant to solve, and test that framing.

- Restate the request as a user need. Name who has it, the circumstance they are in, and the progress they want to make. A need framed as progress in a circumstance beats a feature list.
- Attach the evidence to the statement. Cite tier 2 (existing research, analytics, support tickets) or tier 3 (new user evidence). With neither, label the statement a hypothesis and record the missing evidence as a pending gate (**principle-never-fabricate-user-evidence**). To close the gate, prepare the kit through the **Interview study** playbook (../design-mode/playbooks/interview-study.md).
- Write down what is out of scope. Reframing includes agreeing what is not part of the problem.
- Map the wider journey the request sits in. The problem often spans other teams, other organizations, and offline channels.
- Separate hard constraints (legislation, contracts) from soft ones (existing processes). Change a soft constraint instead of designing around it.
- List the no-build options before any screen. Published content, a campaign, a partner organization, better information for front-line staff, or open data and an API may solve it more cheaply than new UI.
- Write the premise in one sentence and name the observation that would prove it wrong. Then go and look for that observation.

Example. "Build an interactive map of our contact centres" becomes "help people who need a face-to-face appointment find their nearest centre". The second framing admits options the first rules out, including no new UI at all.

**Why:** A solution taken at face value fixes the scope before anyone has looked at the problem. Every later step then optimizes the wrong thing. Reframing costs least before the first sketch.

## Misuse caveats

- Framing is not a stall. When existing evidence already supports the request, say so in one line and move on.
- Never invent a need to justify the request. An unsupported framing stays a hypothesis.
- A problem with no viable option is a valid finding. Stopping at the end of discovery is a legitimate outcome.

Adapted in part from the GOV.UK Service Manual, Open Government Licence v3.0.

## Grounded in

- [How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) (GOV.UK Service Manual, OGL v3), for reframing a pre-defined solution as a problem, agreeing what is out of scope, hard and soft constraints, and alternatives to building.
- [Framework for Innovation](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/) (Design Council, CC BY 4.0), for Discover and Define, finding out what the problem really is and then reframing the challenge from that insight.
- [Jobs to Be Done](https://www.christenseninstitute.org/theory/jobs-to-be-done/) (Christensen Institute, all rights reserved), for framing a need as the progress a person wants in a particular circumstance.
- [Opportunity solution trees](https://www.producttalk.org/opportunity-solution-trees/) (Product Talk, all rights reserved), for starting from a desired outcome and opportunities taken from real interviews, never invented ones.
