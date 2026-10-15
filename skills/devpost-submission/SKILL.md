---
name: devpost-submission
description: Generates a complete, paste-ready Devpost submission packet from the project repo, plus a pre-submit audit against the event's rules. Use when submitting a hackathon project on Devpost.
---

# Devpost Submission

Use this skill when a hackathon project needs to be submitted on Devpost.
It reads the project repo, drafts every submission field, and audits the
packet against the event's rules so nothing disqualifying slips through. It
works with any AI agent; adapt the tool names to whatever your agent
provides.

## Gather the project facts

- Read the repo first: README, demo script, and the main code paths. Draft
  the facts yourself and present them for correction instead of
  interrogating the builder.

- Collect the six things Devpost needs: project title, tagline, the full
  story, the tech stack, the links (repo, live demo, video), and the team.
  If the video is not recorded yet, leave its slot marked and keep going.

- Never invent results, metrics, or team members. Every claim in the packet
  must trace back to something in the repo or something the builder told
  you.

## Draft the packet

- Title: short, memorable, and searchable. Avoid puns that need explaining.

- Tagline: one line, 200 characters maximum. What it is plus who it is for.

- Description, in Devpost's standard sections:
  - Inspiration: the human problem, one paragraph.
  - What it does: the product in plain language, two paragraphs maximum.
  - How we built it: the stack and the interesting technical choice.
  - Challenges we ran into: one honest obstacle and how it was handled.
  - Accomplishments that we're proud of: the quantified result goes here.
  - What we learned: one real lesson, not a platitude.
  - What's next: the six-month vision in three lines.

- Built With: the real tech stack as tags, matching what the repo actually
  imports. Add sponsor technologies by their exact product names when the
  build qualifies for a sponsor track.

- Links: public repo URL, live demo URL, and the public YouTube video URL.
  Mark any missing link clearly instead of omitting it silently.

## Run the discrepancy audit

- Check each item against the event's published rules and mark it READY or
  NEEDS-USER:
  - Repo is public and the link works.
  - Demo video is uploaded, public, under the length cap, and has audio.
  - A thumbnail or cover image is attached.
  - The correct track or prize categories are selected.
  - The project is submitted to the hackathon itself, not just published
    standalone on Devpost.
  - Every required field in the event's form has a value.

- A single NEEDS-USER item can mean disqualification. Present the audit as a
  checklist with the fixes, ordered by what blocks submission first.

## Write DEVPOST.md

- Save the full packet as `DEVPOST.md` in the project repo: every field
  with its paste-ready value, in the order the Devpost form asks for it.

- Keep the audit checklist at the top of the file so the team sees blockers
  before they start pasting.

- After the team submits, update the file: replace NEEDS-USER marks with
  confirmation and note the submission time.

## External plugins and skills

- If your agent has a plugin marketplace, look for a markdown or
  form-filling helper when the Devpost form is long. Otherwise the packet
  file plus copy-paste is the whole workflow.

- Reference: the event's Devpost page and its Rules tab are the source of
  truth for required fields. Re-read them the day of submission; organizers
  edit rules mid-event.

- Further reading on what judges reward in submissions: the hackathon
  judging-reality notes at
  https://github.com/crisiswastaken/skills/blob/HEAD/hackathon-idea-generator/references/judging-reality.md
  and the Devpost judging-tips collection at https://info.devpost.com/blog/hackathon-judging-tips
