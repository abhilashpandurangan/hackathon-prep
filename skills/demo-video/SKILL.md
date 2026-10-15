---
name: demo-video
description: Generates a timed, shot-by-shot demo video script with spoken voiceover lines, a recording checklist, and export and upload specs. Use when a hackathon project needs its demo video.
---

# Demo Video

Use this skill when a hackathon project needs its demo video. Most
hackathons require one, and for async judging it is often the only thing
judges watch. The skill writes the script and the voiceover; the human
records the screen. It works with any AI agent; adapt the tool names to
whatever your agent provides.

## State the honest boundary up front

- The agent writes the script, the shot list, and the voiceover lines, and
  can generate the voiceover audio where it has text-to-speech capability.
  The human records the screen and uploads the video. Say this before
  starting so nobody waits on the agent for something it cannot do.

## Write VIDEO_SCRIPT.md

- Target 2 minutes 45 seconds total, safely under the common 3-minute cap.
  Structure it as timed beats in a table:
  - Time, shot description (exactly what is on screen), the voiceover lines
    to speak word for word, and on-screen caption cues.

- Beats in order: hook (the person and the number, 15 seconds), problem
  (20 seconds), three demo beats (about 100 seconds total), the quantified
  result (15 seconds), vision and ask (15 seconds).

- Write voiceover lines to be spoken, not read: short sentences, no
  jargon, numbers spelled out the way a human says them. Mark pauses with
  an ellipsis where the viewer needs a second to absorb the screen.

- Every beat names its fallback: which pre-recorded clip or screenshot
  covers it if the live demo stutters mid-take.

## Recording checklist

- 1080p screen capture at 30fps. Hide notifications, close unrelated tabs,
  and set the UI to a readable zoom before pressing record.

- Pre-seed all demo data. Nothing is typed live except what the script
  calls for; every input is rehearsed keystroke for keystroke.

- Record the voiceover separately from the screen capture when live
  narration rushes the demo. Silent screen recording plus a pasted AI
  voiceover is a legitimate, widely used shortcut.

- Do two full takes. Keep the better one; keep both until the upload
  confirms.

## Export and upload specs

- Export: MP4, H.264 video, 1920x1080 at 30fps, AAC audio at 128kbps or
  better. Keep the file under the platform's limit; re-export at a lower
  bitrate rather than trimming content.

- Upload to YouTube as public or unlisted per the event rules. Most events
  require public. Confirm the link plays signed out before pasting it into
  Devpost.

- No copyrighted music. This is a common rules violation and an easy
  disqualifier. Silence or a royalty-free bed is fine.

## External plugins and skills

- If your agent has a plugin marketplace, look for text-to-speech or
  voiceover plugins to generate the narration audio from the script's
  spoken lines. Verify the voice sounds natural on a 30-second sample
  before generating the full track.

- If your agent can generate video, use it only for the title card or B-roll
  segments. The product demo itself must be the real screen recording;
  judges discount anything else.

- Pair with the `devpost-submission` skill in this repo: the finished video
  URL fills the video slot in the submission packet.
