#!/usr/bin/env python3
"""PreToolUse (Write|Edit): block secrets in this PUBLIC repo."""
import json, re, sys
d = json.load(sys.stdin); ti = d.get("tool_input", {}) or {}
path = ti.get("file_path", "") or ""
text = (ti.get("content") or "") + "\n" + (ti.get("new_string") or "")
base = path.rsplit("/", 1)[-1]
if base == ".env" or base.startswith(".env.") and not base.endswith(".example"):
    print(f"BLOCKED: {base} must not live in this public repo. Keep secrets only on your computer.", file=sys.stderr); sys.exit(2)
pats = [r"\blk_[A-Za-z0-9]{16,}", r"\bsk-[A-Za-z0-9_-]{20,}", r"\bghp_[A-Za-z0-9]{30,}", r"github_pat_[A-Za-z0-9_]{30,}",
        r"\bAKIA[0-9A-Z]{16}\b", r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
        r"(?i)(api[_-]?key|secret|token|password)\s*[\"']?\s*[:=]\s*[\"'][A-Za-z0-9_\-/+=]{16,}[\"']"]
for p in pats:
    if re.search(p, text):
        print("BLOCKED: this looks like a secret/API key and the repo is public. Use an environment variable (LEONARDO_API_KEY) or `leonardo config set apiKey` on your computer instead.", file=sys.stderr); sys.exit(2)
