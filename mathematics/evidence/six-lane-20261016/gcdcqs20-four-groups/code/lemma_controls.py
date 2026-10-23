#!/usr/bin/env python3
"""Exact controls for the frozen Lemma F note (sources/lemma-F-frozen.md).  Writes OUT.json.

C-F  (Lemma F, hypotheses met trivially): g = 8 design of C0b sample 0, rho = pi1 (fixes G0
     pointwise).  Checks: Fix(rho) ∩ (X minus x) ⊆ hole, so Lemma F gives no restriction; and the
     PASS certificate runs/c0b/g8_a4c8_c3/gcdcqs8_s0_a0.txt has a rho-invariant colouring at x.
C-F1 (Corollary F1): A4 x A5 KM sample 0 of E2a, rho = conj(c0).  Checks: |F| = 7, |F ∩ H| = 1,
     L is an STS(7) on F, r_L(p) = 3 for the six non-hole points, any two triples of L meet
     (chi'(L) = 7 > 3 + 1); the 11 recorded colouring models of that sample are UNSAT.
C-F2 (Corollary F2): A4 x AGL(1,4) x Z5: the element m_w (w-multiplication on the F4 part of the
     coordinate) has order 3 and fixes exactly 5 coordinates (k = 5); 4k-1 = 19 but k-1 = 4 is not
     ≡ 1,3 (mod 6), so no invariant CQS(20^4:0) exists; the recorded KM status is UNSAT.
Usage: lemma_controls.py OUT.json
"""
import lane_guard  # noqa: F401

import json
import os
import sys
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from lane_guard import xopen
import groups as grp
from derived_io import load_design
from pipeline import derived


def read_cert_colouring(path, x):
    cls, cur = [], None
    for raw in open(path):
        s = raw.split("#")[0].strip()
        if not s:
            continue
        t = s.split()
        if t[0] == "POINT":
            if cur == x:
                break
            cur = int(t[1])
        elif t[0] == "CLASS" and cur == x:
            cls.append(set())
        elif cur == x and len(t) == 3:
            cls[-1].add(tuple(sorted(int(z) for z in t)))
    return cls


def main():
    out = {}
    os.chdir(LANE)
    # C-F
    spec, v, g, blocks = load_design("A4xC", "runs/c0b/g8_a4c8_c3/summary.json:0")
    rho = spec["res"]["C3"][0]
    x = 0
    hole = {q for q in range(v) if spec["group_of"][q] == 0 and q != x}
    fixed = {q for q in range(v) if q != x and rho[q] == q}
    cls = read_cert_colouring("runs/c0b/g8_a4c8_c3/gcdcqs8_s0_a0.txt", x)
    keys = [frozenset(C) for C in cls]
    inv = all(frozenset(tuple(sorted(rho[p] for p in t)) for t in C) in keys for C in cls)
    out["C-F"] = {"design": "runs/c0b/g8_a4c8_c3/summary.json:0", "rho": "pi1", "fixed_points_in_D": len(fixed),
                  "fixed_subset_of_hole": fixed <= hole, "certificate": "runs/c0b/g8_a4c8_c3/gcdcqs8_s0_a0.txt",
                  "colouring_at_x_rho_invariant": inv, "pass": fixed <= hole and inv}
    # C-F1
    spec, v, g, blocks = load_design("A4xA5", "runs/e2a/A4xA5/summary.json:0")
    rho = spec["res"]["C3coord"][0]
    x = 0
    hole = {q for q in range(v) if spec["group_of"][q] == 0 and q != x}
    F = {q for q in range(v) if q != x and rho[q] == q}
    D = derived(blocks, x)
    L = [t for t in D if set(t) <= F]
    pairs = {}
    for t in L:
        for pr in combinations(t, 2):
            pairs[pr] = pairs.get(pr, 0) + 1
    sts7 = len(F) == 7 and len(L) == 7 and len(pairs) == 21 and set(pairs.values()) == {1}
    rL = {p: sum(1 for t in L if p in t) for p in F - hole}
    meet = all(set(s) & set(t) for s, t in combinations(L, 2))
    recs = [json.loads(l) for l in open("runs/e2a/A4xA5/progress.jsonl")]
    s0 = [r["col_status"] for r in recs if r.get("sample") == 0 and "colouring" in r]
    out["C-F1"] = {"design": "runs/e2a/A4xA5/summary.json:0", "rho": "conj(c0)", "F": sorted(F),
                   "F_size": len(F), "F_hole_points": len(F & hole), "L": L, "L_is_STS7": sts7,
                   "r_L_nonhole": sorted(set(rL.values())), "L_pairwise_meet": meet,
                   "recorded_sample0_colourings": s0,
                   "pass": sts7 and len(F & hole) == 1 and set(rL.values()) == {3} and meet and s0 and all(z == "UNSAT" for z in s0)}
    # C-F2
    spec = grp.build("A4xAGL4xZ5", 4, 20)
    mw = spec["res"]["C3coord"][0]
    order = 1
    p = list(mw)
    while p != list(range(80)):
        p = [mw[z] for z in p]
        order += 1
    k = sum(1 for a in range(20) if mw[a] == a)  # fixed coordinates (group 0 labels = coordinates)
    recs = [json.loads(l) for l in open("runs/e2a/A4xAGL4xZ5/progress.jsonl")]
    km = [r["km_status"] for r in recs if "km_status" in r]
    out["C-F2"] = {"group": "A4xAGL4xZ5", "element": "m_w", "order": order, "fixed_coordinates": k,
                   "k_minus_1_admissible": (k - 1) % 6 in (1, 3), "four_k_minus_1_admissible": (4 * k - 1) % 6 in (1, 3),
                   "recorded_km_status": km, "pass": order == 3 and k == 5 and km == ["UNSAT"]}
    with xopen(sys.argv[1]) as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({key: val["pass"] for key, val in out.items()}))


if __name__ == "__main__":
    main()
