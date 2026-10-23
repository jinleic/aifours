#!/usr/bin/env python3
"""make_dm_controls_v1.py (ContinueCFR21; stdlib only). Writes control inputs for check_dm_mols_cfr_v1.py into a NEW
directory (exclusive creates) plus manifest.json with expected verdicts. No search; deterministic constructions:
 POSITIVES: linear rows i*x over Z_7 and Z_13 (k = 7, prime fields); Sage database DM_21_6_1, DM_33_6_1, DM_39_6_1,
 DM_51_6_1 re-implemented from the pinned Sage source (expanded per Sage's own loops, transposed to k x n);
 the first pinned P21 Z_21 six-row DM.
 NEGATIVES (expected FAIL): one transposition inside a row of each positive; a duplicated row; Z_9 rows {0,x,2x,4x};
 Z_21 rows {0,x,2x,5x} (non-unit differences).
Args: out_dir sage_source sage_sha p21_json p21_sha"""
import sys, os, json, hashlib, re
out_dir, sage_path, sage_sha, p21_path, p21_sha = sys.argv[1:6]
def pinned(p, w):
    raw = open(p, 'rb').read(); h = hashlib.sha256(raw).hexdigest()
    if h != w: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "path": p, "got": h})); sys.exit(2)
    return raw
pinned(sage_path, sage_sha)
p21 = json.loads(pinned(p21_path, p21_sha))
os.makedirs(out_dir, exist_ok=False)
def cols_to_rows(cols, n):
    k = len(cols[0]); return [[cols[c][i] % n for c in range(len(cols))] for i in range(k)]
def dm21():
    M = [[8,17,20,2],[9,16,4,15],[11,5,10,6],[14,1,3,13],[18,19,12,7]]
    Mb = [[0,0,0,0,0,0]]
    for a,b,c,d,e in zip(*M):
        Mb.append([a,b,c,d,e,0]); Mb.append([b,c,d,e,a,0]); Mb.append([c,d,e,a,b,0]); Mb.append([d,e,a,b,c,0]); Mb.append([e,a,b,c,d,0])
    return 21, Mb
def dm33():
    M = [[0,0,0,0,0,0],[15,11,22,4,17,8],[19,7,14,32,22,18],[22,19,8,24,21,6],[9,12,15,7,26,14],[14,28,23,2,19,3]]
    Mb = [[0,0,0,0,0,0],[1,4,16,31,25,22],[7,28,13,19,10,0]]
    for R in zip(*M):
        a,b,c,d,e,f = R
        for i in range(5):
            Mb.append([a,b,c,d,e,f]); a,b,c,d,e,f = 4*e,4*a,4*b,4*c,4*d,4*f
    return 33, Mb
def dm39():
    n = 39
    M = [[0,0,0,0,0,0],[4,23,13,5,12,11],[25,11,22,34,23,6],[13,4,20,17,15,29],[27,21,8,16,19,26],[16,19,34,38,26,21]]
    Mb = [[0,0,0,0,0,0],[1,16,22,17,38,23],[-1,-16,-22,-17,-38,-23]]
    for R in zip(*M):
        a,b,c,d,e,f = (x % n for x in R)
        for i in range(3):
            Mb.append([a,b,c,d,e,f]); Mb.append([-a,-b,-c,-d,-e,-f])
            a,b,c,d,e,f = ((16*x) % n for x in [c,a,b,f,d,e])
    return n, Mb
def dm51():
    M = [[5,33,29,30,1],[8,3,47,10,13],[14,27,6,12,28],[9,16,44,49,11],[34,32,36,26,20]]
    Mb = [[0,0,0,0,0]]
    for R in zip(*M):
        R = list(R)
        for i in range(5):
            Mb.extend([list(R), [-x for x in R]])
            R = R[1:] + R[:1]   # cyclic_shift(R,1): Sage shifts left by one (checked by the control verdict)
    for R in Mb: R.append(0)
    return 51, Mb
cases = []
def emit(name, rows, n, expect):
    k = len(rows); p = os.path.join(out_dir, name + '.raw')
    with open(p, 'x') as f: f.write('\n'.join(' '.join(str(x % n) for x in r) for r in rows) + '\n')
    cases.append({"name": name, "file": p, "n": n, "k": k, "expected_overall": expect,
                  "sha256": hashlib.sha256(open(p, 'rb').read()).hexdigest()})
for q in (7, 13):
    emit("pos_linear_z%d_k7" % q, [[(i * x) % q for x in range(q)] for i in range(7)], q, "PASS")
for fn in (dm21, dm33, dm39, dm51):
    n, Mb = fn(); rows = cols_to_rows(Mb, n)
    emit("pos_sage_dm%d_k6" % n, rows, n, "PASS_IF_SAGE_TRANSCRIPTION_CORRECT")
    mut = [r[:] for r in rows]; mut[2][3], mut[2][7] = mut[2][7], mut[2][3]
    emit("neg_sage_dm%d_k6_swap" % n, mut, n, "FAIL")
p = p21["dms"][0]["rows"]
emit("pos_p21_sol1_k6", p, 21, "PASS")
mut = [r[:] for r in p]; mut[4][1], mut[4][2] = mut[4][2], mut[4][1]
emit("neg_p21_sol1_swap", mut, 21, "FAIL")
dup = [r[:] for r in p]; dup[5] = dup[4][:]
emit("neg_p21_sol1_duprow", dup, 21, "FAIL")
emit("neg_z9_rows_0_1_2_4", [[(a * x) % 9 for x in range(9)] for a in (0, 1, 2, 4)], 9, "FAIL")
emit("neg_z21_rows_0_1_2_5", [[(a * x) % 21 for x in range(21)] for a in (0, 1, 2, 5)], 21, "FAIL")
lin = [[(i * x) % 13 for x in range(13)] for i in range(7)]; lin[6][0], lin[6][1] = lin[6][1], lin[6][0]
emit("neg_linear_z13_k7_swap", lin, 13, "FAIL")
with open(os.path.join(out_dir, 'manifest.json'), 'x') as f:
    json.dump({"generator": "make_dm_controls_v1.py", "sage_source_sha256": sage_sha, "p21_sha256": p21_sha, "cases": cases}, f, indent=1)
print(json.dumps({"status": "OK", "cases": len(cases)}))
