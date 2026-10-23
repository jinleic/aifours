#!/usr/bin/env python3
"""make_fix_model_v1.py (ContinueCFR21, mols39 lane; frozen; stdlib only). Writes a NEW model JSON (exclusive) equal to a
pinned base model plus unit facts D_row(u) = value for EVERY label u, taken from a pinned known DM mapped into the base
model's labelling (zero-row normalisation and label pair exactly as in sym_dm_cnf_v1.py 'evaluate').
Purpose: exact-reproduction controls (the solver must complete the known object). Args:
  base_model base_sha raw_dm raw_sha row out_model new_name"""
import sys, json, hashlib
def pinned(p, w):
    raw = open(p, 'rb').read(); h = hashlib.sha256(raw).hexdigest()
    if h != w: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "path": p, "got": h})); sys.exit(2)
    return raw
M = json.loads(pinned(sys.argv[1], sys.argv[2])); rawb = pinned(sys.argv[3], sys.argv[4])
row = int(sys.argv[5]); outp = sys.argv[6]; name = sys.argv[7]
n, k, z = M["n"], M["k"], M.get("zero_row"); a, b = M["label"]
rows = [[int(t) % n for t in ln.split()] for ln in rawb.decode().splitlines() if ln.strip()]
if z is not None: rows = [[(rows[x][c] - rows[z][c]) % n for c in range(n)] for x in range(k)]
lab = [(rows[a][c] - rows[b][c]) % n for c in range(n)]
assert sorted(lab) == list(range(n))
col = {lab[c]: c for c in range(n)}
units = list(M.get("units", [])) + [[row, u, rows[row][col[u]]] for u in range(n)]
N = dict(M); N["units"] = units; N["name"] = name
N["notes"] = (M.get("notes", "") + " | exact-reproduction control: row %d fixed on all labels from %s (sha %s)" % (row, sys.argv[3], sys.argv[4]))
with open(outp, 'x') as f: f.write(json.dumps(N, indent=1) + "\n")
print(json.dumps({"status": "OK", "out": outp, "sha256": hashlib.sha256(open(outp, 'rb').read()).hexdigest(), "units": len(units)}))
