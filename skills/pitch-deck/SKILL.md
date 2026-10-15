---
name: pitch-deck
description: Automatically generates a hackathon pitch deck from project facts: five slides, speaker notes with timing, and a demo script. Use when a hackathon build needs a pitch deck.
---

# Pitch Deck

Use this skill when a hackathon build needs a pitch deck. Given a project
name, the problem, the demo beats, and the numbers, it produces a 5-slide
deck plus speaker notes and a timed demo script, ready to present. It works
with any AI agent; adapt the tool names to whatever your agent provides.

## Gather the inputs

- Ask for only what is missing. The six facts a deck needs: project name
  and one-liner, the problem with one sourced number, the three demo beats
  in order, the quantified result, the vision and ask, and the team.

- If given a repo, read its README first and draft the facts yourself.
  Present the draft for correction instead of interrogating the builder.

- Never invent numbers. If a metric is missing, mark the slide "TBD" and
  keep going. A deck with one honest gap beats a deck with one invented
  claim.

## Build the five slides

- Slide 1, Hook: one person and one number. A name, a photo-style
  description, the pain in one line. No logos, no tech stack.

- Slide 2, Problem: the one sourced number that makes the problem expensive,
  plus one line on who feels it daily. Cite the source in small type.

- Slide 3, Live demo: the three beats as three simple panels. Each panel is
  input on the left, output on the right, one caption. This slide is a
  visual cue card for the live demo, not a substitute for it.

- Slide 4, Result: the quantified outcome in the biggest type on the deck.
  Time saved, cost per case, accuracy, or throughput. One supporting line on
  how it was measured.

- Slide 5, Vision and ask: where this goes in six months, in three bullets,
  and one clear ask. End on the vision, never on a thank-you slide.

## Generate the deck

- Build the deck with the agent's document or presentation capability into
  an editable slide file (PowerPoint, Google Slides, or equivalent), or as a
  hosted web page when presenting from a link is preferred.

- Keep every slide under 25 words of body text. If a slide needs more
  words, the idea is not sharp enough yet. Say so and sharpen it before
  generating.

- Use one accent color, one font family, and generous whitespace. Dark
  backgrounds project better in bright demo rooms.

- Include speaker notes under each slide with the exact lines to say and the
  timing. Total talk time targets 3 minutes with 1 minute of buffer for the
  live demo.

## Add the demo script

- Write `DEMO_SCRIPT.md` next to the deck using
  `templates/demo-script.md` from this repo. Fill in the beats, the exact
  inputs to type, and the fallback plan if an API fails mid-demo.

- Rehearse the script twice against the clock before calling the deck done.
  Cut a beat if it runs long. Never add a slide to fix a timing problem.

## External plugins and skills

- If your agent has a plugin marketplace, look for slide-generation or
  presentation plugins (search "slides" or "presentation") and install one
  before generating. Otherwise the agent's document capability plus the
  structure in this skill is the whole workflow.

- For the architecture appendix slide, the `repo-polish` skill in this repo
  generates the Mermaid diagram from the actual code. Run it first when the
  diagram matters.

- Pair with the `demo-video` skill in this repo: the deck's demo beats and
  the video script share the same three beats, so write them once and reuse.

## Alternatives for better results

- When judges score heavily on technical depth, add one appendix slide with
  the architecture diagram. Keep it out of the main flow.

- When the team presents together, assign one speaker per slide in the
  speaker notes. Handoffs written down beat handoffs improvised.

- When the event forbids slide decks and wants live demos only, still
  generate the five slides as a one-page leave-behind. Judges deliberate
  from what they can re-read.
