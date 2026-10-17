# Discover and investigate before you design

Two playbooks run before any screen exists.

## Discovery

For a new problem space or feature request. It produces a problem framing and a go or no-go recommendation. Nothing gets built in discovery, and the go or no-go call stays with you.

It reframes the request as a user problem, inventories the evidence by tier, pins the accessibility and legal targets, maps the users and the current journey, ranks the assumptions by risk, defines the outcome metric with HEART, and prepares a study kit when a top assumption needs real users.

```
/mstack:design-mode we keep hearing that admins want bulk user import. is it worth building?
```

## Investigation

For a read-only question about an existing design: how a flow works, why it was built this way, why people drop at a step, or "are we sure". It never changes the design.

It walks the live UI and screenshots every step, reads the design files and decision history, runs a cognitive walkthrough for a "how" question, and cites the decision record for a "why" question. When no record exists, it says so and labels the reason inferred. A choice between alternatives gets a tradeoffs table, not a prototype. If a change should follow, it names the playbook and stops.

```
/mstack:design-mode why do people drop at step 3 of signup on mobile? read the funnel data and walk the flow. don't change anything yet.
```

## AI feature design

Any AI or agentic feature starts here, from whether AI is needed at all to how it fails gracefully.

Files: `skills/design-mode/playbooks/discovery.md`, `investigation.md`, `ai-feature-design.md`.

Next: [Design and prototype](04-design-and-prototype.md).
