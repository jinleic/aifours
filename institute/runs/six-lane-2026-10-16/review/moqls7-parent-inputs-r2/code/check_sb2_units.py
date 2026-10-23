"""Static check of the (SB2) symmetry-breaking clauses: the SB2 CNF must equal the non-SB2 CNF plus unit clauses only,
and those unit clauses, decoded through the variable map, must be exactly the README §2 addendum-A assignment.

python -B check_sb2_units.py --plain X.cnf --sb2 Y.cnf --map MAP.json --encoder A|B --classes K2|K3|K4 --out R.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys


def clauses(path):
    out = []
    with open(path) as fh:
        for line in fh:
            if line.startswith(("p", "c")):
                continue
            lits = tuple(int(t) for t in line.split()[:-1])
            out.append(lits)
    return out


def expected(cls):
    m = {"K2": 2, "K3": 3, "K4": 4}[cls]
    ncl = 4 - m
    exp = {}
    for t in range(ncl):
        exp[("L", t, 1, 0, t + 1)] = True                      # classical symbols 1, 2, ... at (1,0)
    free = list(range(1 + ncl, 7))
    parts = [free[:3]] + [[k] for k in free[3:]]
    for s, part in enumerate(parts, start=1):
        for k in range(7):
            exp[("S", s, 1, 0, k)] = k in part
    return exp


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plain", required=True)
    ap.add_argument("--sb2", required=True)
    ap.add_argument("--map", required=True)
    ap.add_argument("--encoder", choices=["A", "B"], required=True)
    ap.add_argument("--classes", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    P, Q = clauses(a.plain), clauses(a.sb2)
    from collections import Counter
    cp, cq = Counter(P), Counter(Q)
    removed = cp - cq
    added = cq - cp
    names = {}
    m = json.load(open(a.map))
    table = m["vars"] if a.encoder == "A" else m
    for key, v in table.items():
        names[v] = json.loads(key)
    ncl = 4 - {"K2": 2, "K3": 3, "K4": 4}[a.classes]
    m_q = 4 - ncl
    got = {}
    bad = []
    for cl, mult in added.items():
        if len(cl) != 1:
            bad.append(["non-unit added clause", list(cl)])
            continue
        lit = cl[0]
        nm = names.get(abs(lit))
        if nm is None:
            bad.append(["unmapped variable", lit])
            continue
        if a.encoder == "A":       # ("S1", [1,0], k) / ("L5", [1,0], x); classical labels start at m_q + 1
            kind = nm[0][0]
            lab = int(nm[0][1:])
            r, c = nm[1]
            val = nm[2]
            idx = lab if kind == "S" else lab - (m_q + 1)
        else:                      # ("S", s, r, c, k) / ("L", t, r, c, x); classical labels start at 3
            kind, lab, r, c, val = nm
            idx = lab if kind == "S" else lab - 3
        got[(kind, idx, r, c, val)] = lit > 0
    exp = expected(a.classes)
    # classical-symbol units only constrain the true literal; compare on the keys that the encoder fixes
    exp_cmp = {k: v for k, v in exp.items() if k[0] == "S" or v}
    ok = (not bad) and (not removed) and got == exp_cmp
    rec = {"argv": sys.argv, "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "plain_sha256": hashlib.sha256(open(a.plain, "rb").read()).hexdigest(),
           "sb2_sha256": hashlib.sha256(open(a.sb2, "rb").read()).hexdigest(),
           "removed_clauses": len(removed), "added_clauses": sum(added.values()), "problems": bad,
           "decoded_units": sorted([list(k) + [v] for k, v in got.items()]), "matches_expected": ok}
    with open(a.out, "x") as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps({k: rec[k] for k in ("removed_clauses", "added_clauses", "matches_expected")}))
    if not ok:
        sys.exit("SB2 UNIT CHECK FAILED")


if __name__ == "__main__":
    main()
