"""Exact check of the conjectured closed forms for the low-spin ('bottom') spin-2 sector.

Parent: seniority v, total spin L <= 5, missing label e = (v - lambda)/3 (states
proj(f^a H^b T^c j^e)); daughter: seniority v-1, spin L', lambda' (= lambda-1: boson taken from
the lambda-part, or lambda+2: boson taken from a trio).  Each conjectured r^2 below is a
rational function of v valid on the residue class v = lambda (mod 3); it is compared
exactly with every entry of the exact table (fpc_core engine), all v in the table.
For the two-dimensional daughter blocks (L' = 6 with lambda' in {3, 6}) only the
basis-independent block weight sum_alpha' r^2 is conjectured.
Run (from code/): $PY verify_bottom_conjectures.py ../results/spin2_r_table_v88_L5.json
"""
import json
import sys
from collections import defaultdict

import sympy as sp

v = sp.Symbol('v')
# (L, lambda) -> (L', lambda'): (r^2, sign)
CONJ = {
    (0, 0, 2, 2): (sp.Integer(1), 1),
    (2, 1, 0, 0): ((v + 2) * (2 * v + 3) / (5 * v * (2 * v + 1)), 1),
    (2, 1, 3, 3): ((v - 1) * (2 * v + 3) / (2 * v * (2 * v + 1)), 1),
    (2, 1, 4, 3): (3 * (v - 1) * (2 * v - 1) / (10 * v * (2 * v + 1)), 1),
    (2, 2, 2, 1): (2 * (2 * v + 3) / (7 * v), 1),
    (2, 2, 4, 4): (3 * (v - 2) / (7 * v), 1),
    (3, 3, 2, 2): (5 * (v + 3) / (14 * v), 1),
    (3, 3, 4, 2): (6 * (2 * v - 1) / (35 * v), -1),
    (3, 3, 5, 5): (3 * (v - 3) / (10 * v), 1),
    (4, 2, 2, 1): (5 * (v + 4) * (2 * v + 3) / (21 * v * (2 * v + 1)), 1),
    (4, 2, 4, 4): (64 * (v - 2) * (v + 4) / (385 * v * (2 * v + 1)), -1),
    (4, 2, 5, 4): (7 * (v - 2) * (2 * v + 3) / (15 * v * (2 * v + 1)), 1),
    (4, 2, 6, 4): (7 * (v - 2) * (2 * v - 3) / (33 * v * (2 * v + 1)), 1),
    (4, 3, 2, 2): ((v + 3) * (2 * v + 5) / (6 * v * (2 * v + 1)), 1),
    (4, 3, 4, 2): (2 * (2 * v - 1) * (2 * v + 5) / (11 * v * (2 * v + 1)), 1),
    (4, 3, 5, 5): ((v - 3) * (2 * v + 5) / (6 * v * (2 * v + 1)), 1),
    (4, 3, 6, 5): (10 * (v - 3) * (2 * v - 1) / (33 * v * (2 * v + 1)), 1),
    (4, 4, 3, 3): (2 * (2 * v + 3) * (2 * v + 5) / (15 * v * (2 * v + 1)), -1),
    (4, 4, 4, 3): (2 * (2 * v - 1) * (2 * v + 5) / (11 * v * (2 * v + 1)), 1),
    (5, 4, 3, 3): (21 * (v + 5) * (2 * v + 3) / (110 * v * (2 * v + 1)), 1),
    (5, 4, 4, 3): (3 * (v + 5) * (2 * v - 1) / (22 * v * (2 * v + 1)), 1),
    (5, 4, 7, 6): (15 * (v - 4) * (2 * v - 1) / (77 * v * (2 * v + 1)), 1),
    (5, 5, 4, 4): (21 * (v + 4) / (55 * v), 1),
    (5, 5, 5, 4): (6 * (2 * v + 3) / (65 * v), 1),
    (5, 5, 6, 4): (4 * (2 * v - 3) / (77 * v), -1),
    (5, 5, 7, 7): (30 * (v - 5) / (91 * v), 1),
}
# basis-independent weight into the two-dimensional block (v-1, L'=6, lambda' in {3,6})
BLOCK = {
    (4, 4, 6): (122 * v ** 2 - 427 * v - 180) / (165 * v * (2 * v + 1)),
    (5, 4, 6): None,   # filled below by the completeness relation
}


def main(path):
    rows = json.load(open(path))["rows"]
    seen = defaultdict(list)
    block = defaultdict(lambda: sp.Integer(0))
    exceptions = defaultdict(list)
    for r in rows:
        vv, L, e, Lp, ep = r["v"], r["L"], r["e"], r["Lp"], r["ep"]
        if L > 5:
            continue
        lam, lamp = vv - 3 * e, vv - 1 - 3 * ep
        r2 = sp.Rational(r["r2"])
        key = (L, lam, Lp, lamp)
        if key in CONJ:
            val, sg = CONJ[key]
            ok = (val.subs(v, vv) == r2) and (r2 == 0 or r["sign"] == sg)
            (seen if ok else exceptions)[key].append(vv)
        if Lp == 6 and lamp in (3, 6):
            block[(L, lam, vv)] += r2
    # block weights: (5,4) block = 1 - other conjectured weights
    BLOCK[(5, 4, 6)] = sp.factor(1 - sum(CONJ[k][0] for k in CONJ if k[:2] == (5, 4)))
    for (L, lam, vv), tot in sorted(block.items()):
        key = (L, lam, 6)
        if key in BLOCK and BLOCK[key] is not None:
            ok = BLOCK[key].subs(v, vv) == tot
            (seen if ok else exceptions)[("block",) + key].append(vv)
    n_formula = sum(len(vs) for key, vs in seen.items() if key[0] != "block")
    n_block = sum(len(vs) for key, vs in seen.items() if key[0] == "block")
    for key in sorted(seen, key=str):
        vs = seen[key]
        print(f"{key}: exact agreement at {len(vs)} values of v in [{min(vs)}, {max(vs)}]")
    for key in sorted(exceptions, key=str):
        print(f"{key}: NO agreement at v = {exceptions[key]}")
    covered = {k for k in seen if k[0] != "block"}
    print(f"product-formula checks: {n_formula} over {len(covered)}/{len(CONJ)} formulas; "
          f"block-weight checks: {n_block}; formulas with disagreements: {len(exceptions)}")
    print("block weight (5,4)->(6-block) implied by completeness:", BLOCK[(5, 4, 6)])
    assert not exceptions, "disagreements found"
    assert covered == set(CONJ), ("formulas without coverage", set(CONJ) - covered)
    assert all(len(seen[k]) >= 10 for k in CONJ), "fewer than 10 checks for some formula"


if __name__ == "__main__":
    main(sys.argv[1])
