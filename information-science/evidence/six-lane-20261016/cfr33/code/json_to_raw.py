#!/usr/bin/env python3
"""Convert a JSON object with key "rows" (list of integer lists) into cfr-raw-v1 text (lane cfr33).
Usage: json_to_raw.py IN_JSON OUT_RAW   (OUT written with mode 'x'; no validity assumed)."""
import hashlib, json, sys

rows = json.load(open(sys.argv[1]))["rows"]
text = "".join(" ".join(str(int(x)) for x in r) + "\n" for r in rows)
with open(sys.argv[2], "x") as fh:
    fh.write(text)
print("wrote %s rows %d sha256 %s" % (sys.argv[2], len(rows), hashlib.sha256(text.encode()).hexdigest()))
