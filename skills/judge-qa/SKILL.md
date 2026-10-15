---
name: judge-qa
description: Generates a judge Q&A bank from the event rubric and the project, with drafted answers and backup-slide content for the hard questions. Use the night before demos.
---

# Judge Q&A

Use this skill the night before demos. Q&A is where close calls are decided
and teams systematically underprepare for it. It works with any AI agent;
adapt the tool names to whatever your agent provides.

## Build the question bank

- Take the event's rubric, or the standard five axes when the rubric is not
  published: innovation, technical execution, impact, theme relevance, and
  presentation.

- For each axis, write the three questions a sharp judge is most likely to
  ask about this specific project. Ground every question in something real
  about the build, not in generic filler.

- Draft an answer for each question from the project facts: what the repo
  does, what the numbers are, what was actually built. Cap answers at three
  sentences; a judge interrupts a fourth.

- Mark each answer with its evidence: the file, the trace, the screenshot,
  or the number that backs it. An answer without evidence is a wish.

## Write the backup slides

- For questions the pitch does not cover, write one-pager backup slides:
  feasibility and what it would take to productionize, costs and timelines,
  the competitive landscape, how success would be measured, and what was
  faked or stubbed versus what is real.

- The "what was faked" slide is mandatory. Judges always probe it, and
  volunteering it first reads as confidence rather than confession.

- Keep backup slides out of the main deck. They are revealed only when the
  question comes.

## Red-team the submission

- Find the single weakest claim in the pitch, the README, or the Devpost
  packet. The one a skeptical judge would circle.

- Propose a fix: either strengthen it with evidence before the demo, or
  reframe it honestly so it stops being a target. Present both options and
  recommend one.

- End with the three questions the team least wants to hear, rehearsed with
  their answers. If those are comfortable, the rest is easy.

## External plugins and skills

- This skill is pure preparation and needs no plugins. If your agent has a
  plugin marketplace, there is nothing to install for this one; say so
  rather than inventing a need.

- Pair with the `pitch-deck` skill in this repo: backup slides extend the
  main deck. Pair with `repo-polish`: the README's known-limitations section
  is the source for the "what was faked" answers.

- Further reading on judge perspective: a judge-mentor-participant write-up
  at
  https://medium.com/thecapital/how-to-win-a-hackathon-from-a-judge-mentor-and-participant-perspective-b7bfe9cd20a1
  and a pitch-prep guide at
  https://medium.com/circleslife/creating-a-5-minute-kickass-hackathon-pitch-17cdcb42c3bc
