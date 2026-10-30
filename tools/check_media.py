#!/usr/bin/env python3
"""Check week media: sizes, dimensions and audio. Usage: check_media.py [folder ...]  (default: all <year>-wNN folders)
Exit 1 if a problem is found. Needs ffprobe."""
import glob, json, os, subprocess, sys
LIMIT = 10 * 1024 * 1024  # X media limit
OK_IMG = {(1600, 900)}; OK_VID = {(1080, 1920)}
def probe(p):
    r = subprocess.run(["ffprobe","-v","error","-show_streams","-of","json",p],capture_output=True,text=True)
    return json.loads(r.stdout or "{}").get("streams", [])
def check(p):
    out = []; ext = p.lower().rsplit(".",1)[-1]; size = os.path.getsize(p)
    st = probe(p); v = next((s for s in st if s.get("codec_type")=="video"), None)
    if not v: return [f"{p}: no video/image stream"]
    wh = (v["width"], v["height"])
    if ext == "png":
        if wh not in OK_IMG: out.append(f"{p}: {wh[0]}x{wh[1]}, expected 1600x900")
        if size > LIMIT: out.append(f"{p}: {size/1e6:.1f} MB > 10 MB (X limit)")
    elif ext == "mp4":
        if wh not in OK_VID: out.append(f"{p}: {wh[0]}x{wh[1]}, expected 1080x1920")
        if not any(s.get("codec_type")=="audio" for s in st): out.append(f"{p}: no audio track")
        if v.get("codec_name") != "h264": out.append(f"{p}: codec {v.get('codec_name')}, expected h264")
        d = float(v.get("duration") or 0)
        if d and not 18 <= d <= 28: out.append(f"{p}: {d:.0f}s, expected 20-25 s")
    return out
folders = sys.argv[1:] or sorted(glob.glob("20??-w??"))
probs = []
for f in folders:
    for p in sorted(glob.glob(os.path.join(f, "*.png")) + glob.glob(os.path.join(f, "*.mp4"))):
        probs += check(p)
print("\n".join(probs) if probs else "media OK")
sys.exit(1 if probs else 0)
