# laterretagames-media

Public repo of media and brand files for the La Terreta Games social accounts (X, Facebook, Instagram, LinkedIn). The account covers ALL studio products; AppWatch is the current campaign.

## SECURITY
This repo is PUBLIC. Never commit API keys, tokens or .env files (Leonardo key, kie.ai key, etc.). Keys live only on Roberto's computer. A hook blocks obvious secrets.

## Structure
- `brand/voice.md`: voice, words to avoid, hard rules. `brand/products.md`: products and the only facts we may state.
- `<year>-wNN/`: media of the current week, public raw URLs used by Metricool. Previous weeks are deleted every Monday.
- `inbox/<year>-wNN/`: AI/real material from Roberto (`tue.*`, `thu.*`, `sat.*`, `sat-bg.mp4`, `prompts.json`, `ideas.md`). Folders with other suffixes (e.g. `2026-w44-sensores`) belong to other campaigns: never delete them.
- `tools/`: reference scripts for the cards and the Reel; `tools/check_media.py` validates media.
- `calendario_publicaciones.xlsx`: one tab per week + Resumen + Estrategia.

## Weekly flow (Mon 08:50 cloud task -> 09:20 Roberto's Mac with Leonardo -> 10:07 cloud rebuild)
3 pieces per week: Tue 10:00 LinkedIn+X, Thu 10:00 LinkedIn+X+Facebook, Sat 11:00 Instagram Reel+Facebook. Mix: 1 AppWatch + 1 other product/studio + 1 audience piece. Everything is a DRAFT until Roberto says "aprobado".

## Rules
- Max 1 emoji; 1-2 hashtags (5 on Instagram); no competitors, no politics; only shipped features; never invent numbers, downloads or dates. Steam in AppWatch is live (not beta).
- UTMs: utm_source=<x|linkedin|facebook>, utm_medium=social, utm_campaign=<appwatch|sensores|foxyhops|retroloco|studio>, utm_content=<year>-wNN-<tue|thu|sat>.
- Media: cards 1600x900 PNG (X max 10 MB), Reel 1080x1920 h264 with real audio, 20-25 s. Style: bg #0B1220, accent #3B82F6, Inter fonts.
- Commits end with the attribution lines given by the session.
- Talk to Roberto in Spanish; post texts in English.
