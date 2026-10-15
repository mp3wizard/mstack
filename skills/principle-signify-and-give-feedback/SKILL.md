---
name: principle-signify-and-give-feedback
description: "Apply when designing or reviewing any control, action, async operation, or layout grouping. Every control shows that it can be used and how, and every action shows at once that it registered and what it did."
disable-model-invocation: true
---

# Signify and Give Feedback

A control nobody can find does not exist. An action with no visible result looks broken.

- **Signify.** Give every interactive element a perceivable cue for where and how to act. Designers mostly add signifiers, not affordances (Norman). Give interactive elements distinct hover, focus, and active styles so they read as interactive (W3C designer tips).
- **Map naturally.** Make the relationship between a control and its effect obvious from the layout. A natural mapping needs no label (Norman).
- **Acknowledge at once.** Every action gets a visible response, scaled to how frequent and how major the action is (Shneiderman rule 3). Acknowledge immediately even when the work takes longer (Tognazzini).
- **Aim for sub-second.** Doherty and Thadhani (IBM, 1982) argued that productivity gains rise sharply once response drops below one second. Aim for sub-second completion. Past that, show progress and say what is happening (Nielsen H1). The loading state belongs in the state matrix (**principle-design-every-state**).
- **Close both gulfs.** At each task step ask whether users can tell what to do (execution) and tell what happened (evaluation). The cognitive walkthrough asks the same at every step (CW-1 to CW-4). Would they try for this result, notice the control, connect it to their goal, and see that it worked?
- **Group by meaning.** Visual grouping must match semantic grouping. Proximity and similarity make elements read as related, so related controls share a group and unrelated ones do not sit together.

**Why:** Norman frames use as two gaps, knowing what to do and telling what happened. A missing signifier leaves the first open. Missing feedback leaves the second open, and people cannot tell a slow system from a broken one.

## Misuse caveats

- Feedback scales with the action. A toast for every keystroke is noise, not visibility.
- Common region and element connectedness are later additions to grouping research, not original Gestalt laws. Cite the Wagemans review, not a blog list.
- The popular millisecond figure for the Doherty threshold is a later popularization. The 1982 text argues for sub-second response, so say sub-second.

## Grounded in

- [The Design of Everyday Things](https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/) (Don Norman, all rights reserved), signifiers, mapping, feedback, and the two gulfs.
- [10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) (NN/g, all rights reserved, use with credit and link), H1 visibility of system status.
- [The Economic Value of Rapid Response Time](https://jlelliotton.blogspot.com/p/the-economic-value-of-rapid-response.html) (Doherty and Thadhani 1982, © IBM, all rights reserved, reproduced with permission on Jim Elliott's blog), the case for sub-second response.
- [Cognitive walkthroughs](https://www.nngroup.com/articles/cognitive-walkthroughs/) (NN/g, all rights reserved), the per-step questions.
- [Wagemans et al. 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3482144/) (Psychological Bulletin, license unknown), classical and newer grouping principles.
- [Designing for Web Accessibility](https://www.w3.org/WAI/tips/designing/) (W3C WAI, cite and link), identifiable interactive elements.
