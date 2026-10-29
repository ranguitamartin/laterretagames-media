# tools

Reference scripts used to build the weekly media (week 44). They hard-code the week 44 texts and paths:
copy, adapt texts/paths, and run. Needs Python 3 with Pillow and numpy, ffmpeg and the Inter fonts.

- `cards_with_bg_image.py`: 1600x900 cards using an AI image (inbox/tue.png, thu.png) as background; dark left gradient, headline on the empty area.
- `reel_with_bg_video.py`: 1080x1920 Reel, 22 s: background video looped ping-pong and darkened (inbox/sat-bg.mp4), animated text scenes, progress bar, synthesized audio (pad, pulse, whooshes, ticks).
