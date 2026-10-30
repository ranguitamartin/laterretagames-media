---
name: revisar-post
description: Review a social post text against brand/voice.md and the Instagram skill-pack scripts (hook score, caption lint, humanizer). Use before approving or editing any post text.
---
Given a post text (file or pasted):
1. Read `brand/voice.md` and `brand/products.md`. Check: max 1 emoji; hashtag count (1-2, or 5 on Instagram); no competitors or politics; no banned words; only shipped features; no invented numbers; UTMs present on links (see CLAUDE.md).
2. If the Instagram skill pack is cloned (https://github.com/Jakeschincariol/instagram-agent-skill, MIT, scripts have no network access), run with `python3 -I`, passing paths as arguments: `skills/ig-reel/hookscore.py` on the hook, `skills/ig-caption/caption.py` on Instagram captions, `skills/ig-human/humanize.py <file> --report` then `skills/ig-human/detect.py`. Never let cleanup alter URLs, numbers or verified facts.
3. Reply in Spanish: verdict (OK / ajustar), a table of findings, and the corrected text in English.
