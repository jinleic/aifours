#!/usr/bin/env python3
"""make_orbit_mutant_v1.py (ContinueCFR21, mols39 lane; frozen; stdlib only). Clause-level negative controls for
orbit_dm_cnf_v1.py: decompose a pinned known G-invariant DM into the model's orbit representatives (encoder's own
'evaluate' logic), add delta to coordinate (row) of the representative of orbit index r, regenerate the column set
from all representatives with the model group (so the output is G-invariant with the same orbit types), and write it
(exclusive create). The output is expected to violate only 'dm' clauses.
Args: encoder enc_sha model model_sha raw raw_sha orbit_index row delta out_raw"""
import sys, json, hashlib, importlib.util, io, contextlib
def pinned(p, w):
    raw = open(p, 'rb').read(); h = hashlib.sha256(raw).hexdigest()
    if h != w: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "path": p, "got": h})); sys.exit(2)
    return raw
pinned(sys.argv[1], sys.argv[2]); pinned(sys.argv[3], sys.argv[4]); pinned(sys.argv[5], sys.argv[6])
r_idx, row, delta, outp = int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9]), sys.argv[10]
spec = importlib.util.spec_from_file_location("orbenc", sys.argv[1]); mod = importlib.util.module_from_spec(spec)
sys.dont_write_bytecode = True; spec.loader.exec_module(mod)
buf = io.StringIO(); old = sys.argv
sys.argv = ["orbit_dm_cnf_v1.py", "evaluate", old[3], old[5]]
with contextlib.redirect_stdout(buf): rc = mod.main()
sys.argv = old
ev = json.loads(buf.getvalue())
if ev.get("verdict") != "SATISFIES_ALL": print(json.dumps({"status": "BASE_NOT_SATISFYING", "eval": ev})); sys.exit(3)
M = json.load(open(old[3])); enc = mod.Enc(M); n = enc.n
reps = [tuple(r) for r in ev["reps"]]
t = enc.types[enc.orbits[r_idx]]
if row in t["fixed"] or t["H"] != [(1, tuple(range(enc.k)))]:
    print(json.dumps({"status": "BAD_TARGET", "reason": "fixed coordinate or nontrivial stabiliser"})); sys.exit(3)
c = list(reps[r_idx]); c[row] = (c[row] + delta) % n; reps[r_idx] = tuple(c)
cols = enc.columns_from_reps(reps)
rows = [[col[x] for col in cols] for x in range(enc.k)]
with open(outp, 'x') as f: f.write("\n".join(" ".join(map(str, r)) for r in rows) + "\n")
print(json.dumps({"status": "OK", "out": outp, "sha256": hashlib.sha256(open(outp, 'rb').read()).hexdigest(), "distinct_columns": len(set(cols))}))
