---
name: semana
description: Generate this week's Leonardo images and background video from inbox/<year>-wNN/prompts.json and push them. Use when the Monday Leonardo task failed or you want to run it by hand.
disable-model-invocation: true
---
1. `git pull origin main`. Compute the ISO year and week (<Y>-wNN).
2. Read `inbox/<Y>-wNN/prompts.json`. If missing, stop and say so.
3. Run `leonardo me`; if credits do not cover 3 images + 1 short video, stop and report the credits.
4. For each image item: `leonardo generate "<prompt>" -w <width> -h <height> -o inbox/<Y>-wNN/<file>`. For `sat-bg.mp4`: `leonardo video "<prompt>"`, wait and download.
5. Inspect every image (and a frame of the video): no text, logos or watermarks, empty space for the headline. Regenerate a failed one once.
6. `git add inbox/ && git commit -m "Leonardo: imágenes <Y>-wNN" && git push origin main`. Push only `inbox/`.
Never write the API key to any file, commit or reply.
