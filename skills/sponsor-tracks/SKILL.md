---
name: sponsor-tracks
description: Maps the event's sponsor tracks, prizes, and APIs into a prize matrix and shows which sponsor bounties the build qualifies for. Use early in the event to aim the build at the most winnable prizes.
---

# Sponsor Tracks

Use this skill early in the event, before the build locks in. Sponsor
prizes often have fewer competitors than the grand prize, and a small pivot
can unlock an extra bounty. It works with any AI agent; adapt the tool
names to whatever your agent provides.

## Map the sponsors

- Read the event page and extract every sponsor: track or bounty name, the
  prize (cash, credits, or both), the required product, API, or integration,
  and any judging note about what they want to see.

- Note the constraints that matter: does it require their API key, their
  SDK in the repo, a demo using their product, or just a checkbox at
  submission. Rank each by effort to qualify: trivial, small, or significant.

- If the event has no meaningful sponsor tracks, say so in one line and
  stop. Do not manufacture a matrix from nothing.

## Build the prize matrix

- Output a table: sponsor, prize, what it takes to qualify, whether the
  current build qualifies, and the cheapest change that would unlock it.

- Recommend an aim: the one or two sponsor prizes with the best
  prize-to-effort ratio for this build. Name the trade-off explicitly when
  chasing a sponsor prize would weaken the main-track entry.

- Draft the two-line "built with [sponsor tech]" blurb for each targeted
  sponsor, for the Devpost Built-With field and the pitch.

## Track it through the day

- Recheck the matrix at the feature freeze: did the build drift away from a
  targeted sponsor's requirements. If yes, say what it costs to get back.

- After demos, note which sponsor judges saw the pitch. A sponsor prize is
  sometimes decided by a conversation, not the rubric.

## External plugins and skills

- The highest-value "plugin" here is the sponsor's own product: install
  their SDK, claim their API credits, and read their quickstart before
  writing code. Their docs beat any third-party summary.

- If your agent has a plugin marketplace, check whether the sponsor
  publishes an official plugin or integration for it. Prefer the sponsor's
  own integration over a community copy.

- Pair with the `devpost-submission` skill in this repo: sponsor tracks feed
  the track-selection and Built-With fields of the packet.
