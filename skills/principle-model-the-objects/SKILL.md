---
name: principle-model-the-objects
description: "Apply before designing screens, flows, navigation, or information architecture. Model the objects users think in, with their relationships, actions, and attributes, and derive the screens from that model."
disable-model-invocation: true
---

# Model the Objects

Screens are views of things. Model the things first. A screen designed before its objects inherits whatever structure the first sketch happened to have.

- Find the objects. Pull the recurring nouns from the brief, research notes, support tickets, and existing content. Keep the words users use, not internal or database names.
- Map each object with ORCA. Record its relationships to other objects, the calls to action people take on it, and its attributes, ranked by importance.
- Separate the thing from the screens that show it. One object can appear as a card, a row, a detail page, and a search result. Each is a view of the same model.
- Write the conceptual model. Say in a few sentences how the system works from the user's side. The UI is the system image that has to convey it. Where evidence shows how users already think about the domain, compare the two and name the gaps.
- Derive screens, navigation, and IA from the model. Screens come from objects and their actions. Navigation comes from relationships.
- Validate the structure with users, not with yourself. Prepare an open card-sort kit from the real objects and content, with at least 15 participants per user group. Card sorting is generative, so follow it with a tree-test kit for the drafted structure. Humans run both through the **Usability test** playbook (../design-mode/playbooks/usability-test.md). Never simulate sorters (**principle-never-fabricate-user-evidence**).
- When the journey crosses channels or people, draw a service blueprint. Lay out customer actions, frontstage and backstage actions, support processes, and the evidence at each touchpoint. It exposes the handoffs and failpoints that screens hide.
- Then give every object its full state set (**principle-design-every-state**).

**Why:** A screen-first design buries its structure inside layout decisions where nobody can review it. An explicit object model makes the structure reviewable and testable before any pixel is placed.

## Misuse caveats

- The model is a design hypothesis until users confirm it. Label it.
- Service design method libraries are a known gap in this plugin's research. The blueprint guidance rests only on NN/g's definition.
- Do not stall on a perfect model. A rough object map that shapes the first screens beats a complete one that delays them.

## Grounded in

- [The ORCA series](https://ooux.com/hi/orcaseries) (Sophia Prater, OOUX, © SophiaVUX, LLC, all rights reserved, link and paraphrase), for objects, relationships, calls to action, and attributes, and attribute prioritization.
- [Object-Oriented UX](https://alistapart.com/article/object-oriented-ux/) (Sophia Prater, A List Apart, © A List Apart and its authors), for object discovery from recurring nouns and modeling objects before screens.
- [The Design of Everyday Things](https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/) (Don Norman, book all rights reserved), for the conceptual model and the system image that conveys it.
- [Card sorting, how many users to test](https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/) (NN/g, all rights reserved), for at least 15 participants (about 0.90 correlation, against about 0.75 at 5) and for testing the resulting structure after the sort.
- [How many test users in a usability study](https://www.nngroup.com/articles/how-many-test-users/) (NN/g, all rights reserved), for at least 15 card-sort participants per user group.
- [Service blueprints, definition](https://www.nngroup.com/articles/service-blueprints-definition/) (NN/g, all rights reserved), for the blueprint's lanes and the handoffs and failpoints it exposes.
- [18F Methods](https://github.com/18F/guides/tree/main/content/methods) (18F, CC0 and US public domain), for mental modeling, site mapping, and task flow analysis as decide-phase methods.
