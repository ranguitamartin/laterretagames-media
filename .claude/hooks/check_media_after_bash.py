#!/usr/bin/env python3
"""PostToolUse (Bash): after build/commit commands, validate week media. Feeds problems back to Claude (exit 2)."""
import json, subprocess, sys, os
d = json.load(sys.stdin); cmd = (d.get("tool_input") or {}).get("command", "")
if not any(k in cmd for k in ("ffmpeg", "git add", "git commit", "python")): sys.exit(0)
root = os.environ.get("CLAUDE_PROJECT_DIR", ".")
r = subprocess.run([sys.executable, os.path.join(root, "tools", "check_media.py")], cwd=root, capture_output=True, text=True)
if r.returncode != 0:
    print("MEDIA CHECK FAILED:\n" + r.stdout, file=sys.stderr); sys.exit(2)
