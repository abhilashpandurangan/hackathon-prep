# Hackathon Playbook

Use this skill when the user is attending, considering, or preparing for a
hackathon. It covers the full arc: researching the event, picking a winning
build, pre-event prep, a build-day runbook, the demo and pitch, and
follow-up.

## Research the event

- Open the event page with `browser.open` and extract the date, hours,
  venue, tracks, prizes, judging criteria, host, and sponsors. Never trust
  memory for dates.

- Read the host's own product story. When the host sells an observability or
  agent platform, the winning demo usually shows that platform's loop in
  action. Build the loop into the narrative, not just the stack.

- Find the track sponsors and their challenge briefs. They live on the event
  page, Discord, Builderbase, or Devpost. Sponsor staff are often the judges,
  so build to their brief and visit their desk early on the day.

- Look up the previous edition of the same event. Search for winner
  announcements, Devpost galleries, and repos to learn what the judges
  rewarded last time.

- Confirm the communication channels (Discord, Slack, Builderbase) and join
  them before the event. Track instructions, partner API credits, and venue
  details appear there first.

## Generate and pick the build

- Research each track separately with `browser.search`. Ground every idea in
  something real and current: a fresh product launch, a published stat, an
  industry pain point with a number attached.

- Write two concrete ideas per track. Each idea needs a name, a one-liner,
  why it can win, a day-build scope, and one jaw-drop moment: a single 10
  second beat the judges feel. Everything else is scaffolding for that beat.

- Score ideas on four axes: fit to the user's real skills, demoability in
  the time available, strength of the quantified story, and fit to the host's
  theme. Present the ideas, then give one clear recommendation with reasons.

- Scope the build to finish a working skeleton in the first quarter of the
  clock. A rough system running early beats a brilliant system that never
  runs.

- Pick a stack the user already knows. Never learn a new framework on build
  day.

## Prep before the event

- Scaffold the repo early: UI, backend, and one agent running end to end on
  sample data. Arrive with the skeleton alive.

- Generate the demo datasets in advance. Messy inputs with planted edge
  cases beat clean toy data, because the demo shows the system handling the
  hard parts.

- Sort out API keys and partner credits ahead of time. Keep a fallback for
  every external call, because venue WiFi fails during demos.

- Write the demo script before the event, not during it. Use
  `templates/demo-script.md` in this repo as the starting shape.

- Pack a checklist: laptop and charger, phone with hotspot, power strip,
  notebook, water and snacks, ID, and a LinkedIn QR ready.

## Run the build day

- First hour: arrive early, read the sponsor challenge briefs at their
  desks, ask what they want to see, and settle solo or team composition. If
  teaming up, recruit a designer or a storyteller, not a second backend dev.

- First quarter of the clock: get the skeleton running end to end. Ugly is
  fine. If it does not run, cut scope rather than cutting corners.

- Middle stretch: build depth on the demo path only. Every feature the
  judges never see is waste.

- Deliberately run the observe and improve loop. Break the agent, capture the
  failing trace, add the guardrail, capture the passing trace. This before
  and after sequence is the most persuasive two minutes of the pitch.

- Freeze new features with about 90 minutes left. Spend the rest on polish,
  rehearsal, and a demo-mode fallback with cached outputs in case APIs die.

- A demo that works with six features beats a demo that crashes with
  fifteen.

## Demo and pitch

- Open with one person and one number, never with the tech stack. Judges
  decide in the first 30 seconds whether they care.

- Demo live. Pre-run the inputs, use small data you control, and keep the
  fallback ready. Never show a recorded video unless the network is truly
  dead.

- Show real data with a real number: time saved, cost per case, accuracy,
  straight-through rate. Quantified beats adjectives.

- When the event centers on an observability platform, make the failure trace
  and the fix a formal act of the demo. It proves engineering honesty and
  matches the host's story.

- Generate the pitch deck with the `pitch-deck` skill in this repo. Keep it
  to five slides: hook, problem with one sourced number, the live demo, the
  quantified result, the vision and ask.

- Talk to sponsors and judges as people after the demo. The room remembers
  the builder more than the build.

## After the event

- Polish the repo the same week while the context is fresh: README with the
  demo video or GIF, setup instructions, and the architecture in one
  diagram.

- Follow up with every sponsor, judge, and teammate within 48 hours. One
  short message with the repo link beats a business card.

- Save what worked and what did not into the event's notes file. The next
  run of this playbook starts from those notes.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search`
  to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server
  and set it up with [Custom Connectors and
  MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom
  connector.

## Websites

- [Luma](https://luma.com/) for event pages, schedules, and registration
  status. Carry the event URL into any browser task and verify the date and
  venue there.

- [Devpost](https://devpost.com/) for past hackathon galleries, winning
  projects, and judging criteria. Good for researching what judges rewarded.

- [GitHub](https://github.com/) for past winners' repos and reusable starter
  scaffolds. Verify every repo link loads before citing it.

## Alternatives for better results

- Going solo keeps full control of scope and story, which suits a strong
  builder with a clear idea. Teaming up adds design and pitching strength,
  which matters when judging weights presentation.

- Keep one fallback idea in a different track. If the sponsor challenge
  brief on the day points elsewhere, switching tracks early beats forcing a
  mismatched build.

- If the event is remote or hybrid, rehearse the screen share and audio in
  advance and keep the demo entirely local so nothing depends on the stream.
