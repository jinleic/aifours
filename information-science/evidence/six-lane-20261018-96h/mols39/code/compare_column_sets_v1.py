#!/usr/bin/env python3
"""compare_column_sets_v1.py (ContinueCFR21, mols39 lane; frozen; stdlib only). Compares two raw k x n arrays over Z_n
as SETS of exact column vectors (column order irrelevant). Prints one JSON object: equal (bool), size of intersection,
and both file hashes. Args: raw_a sha_a raw_b sha_b n"""
import sys, json, hashlib
def pinned(p, w):
    raw = open(p, 'rb').read(); h = hashlib.sha256(raw).hexdigest()
    if h != w: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "path": p, "got": h})); sys.exit(2)
    return raw
a = pinned(sys.argv[1], sys.argv[2]); b = pinned(sys.argv[3], sys.argv[4]); n = int(sys.argv[5])
def cols(raw):
    rows = [[int(t) % n for t in ln.split()] for ln in raw.decode().splitlines() if ln.strip()]
    return [tuple(r[c] for r in rows) for c in range(len(rows[0]))], len(rows)
ca, ka = cols(a); cb, kb = cols(b)
print(json.dumps({"status": "OK", "k": [ka, kb], "ncols": [len(ca), len(cb)], "equal_as_sets": set(ca) == set(cb) and len(set(ca)) == len(ca),
                  "common_columns": len(set(ca) & set(cb)), "sha_a": sys.argv[2], "sha_b": sys.argv[4]}))
