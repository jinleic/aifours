#!/usr/bin/env python3
"""verify_lower42_r2.py: cross-checks for review/SUPPORT_LOWER42.r2.md (lane ame46-support). New file for r2; the
r1 verifier code/verify_lower42.py is unchanged. Standard library only, exact integers. Not load-bearing: r2's
proof is written.

Checks (addressing Claude review notes v1, v2, v4 on the r1 verifier):
 W   For each of the two written instances of r2 §4, the text's labels, blocks (reshaping, ordered rows r, r', ordered
     columns c, c'), forms and signed combination are reproduced literally:
       - each stated block is a connected component (2 rows, 2 columns, 4 points) of N in that reshaping, and each
         reshaping has exactly two components;
       - the stated form equals the Lemma 10 form phi(r,c) - phi(r,c') - phi(r',c) + phi(r',c') for the stated order;
       - the signed sum of the three forms, computed point by point (independently of how the blocks were found),
         is the zero form, and the signed right sides sum to an odd multiple of pi.
 SYM The group H = S_4 x (Z_2)^4 (coordinate permutations, value swaps) acts on {0,1}^4. The orbits of the two
     representatives are a two-set class and an eight-set class, and together they are the ten parity sets of §3.
     For every h in H and every one of the ten sets, h maps the components of N to the components of h(N), and maps
     each Lemma 10 form to plus or minus the form of the image block (the symmetry lemma, checked on all 3840 cases).
 F1  The ten parity sets are exactly the 8-subsets of {0,1}^4 with uniform 2-marginals (all 12870 subsets).
Writes evidence/verify_lower42_r2.json; exit status 0 iff all checks hold.
"""
import itertools
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESH = {"12|34": ((0, 1), (2, 3)), "13|24": ((0, 2), (1, 3)), "14|23": ((0, 3), (1, 2))}
PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def pt(s):
    return tuple(int(ch) for ch in s)


def comps(N, rows, cols):
    """Connected components as (frozenset of rows, frozenset of cols, frozenset of points)."""
    left = set(N)
    out = []
    while left:
        x = left.pop()
        R, C, P = {tuple(x[i] for i in rows)}, {tuple(x[i] for i in cols)}, {x}
        grew = True
        while grew:
            grew = False
            for y in list(left):
                if tuple(y[i] for i in rows) in R or tuple(y[i] for i in cols) in C:
                    R.add(tuple(y[i] for i in rows))
                    C.add(tuple(y[i] for i in cols))
                    P.add(y)
                    left.discard(y)
                    grew = True
        out.append((frozenset(R), frozenset(C), frozenset(P)))
    return out


def point(rows, cols, r, c):
    x = [0] * 4
    x[rows[0]], x[rows[1]] = r
    x[cols[0]], x[cols[1]] = c
    return tuple(x)


def lemma10_form(rows, cols, r, r2, c, c2):
    return {point(rows, cols, r, c): 1, point(rows, cols, r, c2): -1, point(rows, cols, r2, c): -1,
            point(rows, cols, r2, c2): 1}


WRITTEN = [
    {"name": "instance 1 (U = {1,2,3,4}, c = 0)",
     "labels": {"a": "4444", "b": "4455", "c": "4545", "d": "4554", "e": "5445", "f": "5454", "g": "5544",
                "h": "5555"},
     "blocks": [("12|34", ("44", "55"), ("44", "55"), {"a": 1, "b": -1, "g": -1, "h": 1}, 1),
                ("13|24", ("44", "55"), ("44", "55"), {"a": 1, "c": -1, "f": -1, "h": 1}, -1),
                ("14|23", ("45", "54"), ("45", "54"), {"b": 1, "c": -1, "f": -1, "g": 1}, 1)]},
    {"name": "instance 2 (U = {1,2,3}, c = 0)",
     "labels": {"a": "4444", "b": "4445", "c": "4554", "d": "4555", "e": "5454", "f": "5455", "g": "5544",
                "h": "5545"},
     "blocks": [("12|34", ("44", "55"), ("44", "45"), {"a": 1, "b": -1, "g": -1, "h": 1}, 1),
                ("13|24", ("44", "55"), ("44", "45"), {"a": 1, "b": -1, "e": -1, "f": 1}, -1),
                ("14|23", ("54", "55"), ("45", "54"), {"e": 1, "f": -1, "g": -1, "h": 1}, -1)]},
]


def check_written(inst):
    lab = {k: pt(v) for k, v in inst["labels"].items()}
    N = set(lab.values())
    res = {"name": inst["name"], "blocks": []}
    total = {}
    rhs = 0
    ok = len(N) == 8
    for name, (r, r2), (c, c2), form, coef in inst["blocks"]:
        rows, cols = RESH[name]
        r, r2, c, c2 = pt(r), pt(r2), pt(c), pt(c2)
        cs = comps(N, rows, cols)
        two = len(cs) == 2 and all(len(R) == 2 and len(C) == 2 and len(P) == 4 for R, C, P in cs)
        is_comp = any(R == frozenset({r, r2}) and C == frozenset({c, c2}) for R, C, P in cs)
        f10 = lemma10_form(rows, cols, r, r2, c, c2)
        stated = {lab[k]: s for k, s in form.items()}
        same = f10 == stated
        res["blocks"].append({"reshaping": name, "two_components": two, "stated_block_is_component": is_comp,
                              "stated_form_equals_lemma10": same, "coefficient": coef})
        ok &= two and is_comp and same
        for x, s in stated.items():
            total[x] = total.get(x, 0) + coef * s
        rhs += coef
    res["signed_sum_is_zero_form"] = all(v == 0 for v in total.values())
    res["rhs_multiple_of_pi"] = rhs
    res["rhs_odd"] = rhs % 2 == 1
    res["ok"] = bool(ok and res["signed_sum_is_zero_form"] and res["rhs_odd"])
    return res


def parity_sets():
    return {(U, c): frozenset(x for x in itertools.product((0, 1), repeat=4) if sum(x[i] for i in U) % 2 == c)
            for k in (3, 4) for U in itertools.combinations(range(4), k) for c in (0, 1)}


def group():
    G = []
    for perm in itertools.permutations(range(4)):
        for flips in itertools.product((0, 1), repeat=4):
            G.append((perm, flips))
    return G


def act(g, x):
    perm, flips = g
    y = [0] * 4
    for i in range(4):
        y[perm[i]] = x[i] ^ flips[i]
    return tuple(y)


def act_line_value(g, P, z):
    """Image of the P-line value z: returns (image pair Q, image value w) with Q sorted."""
    perm, flips = g
    img = {perm[i]: z[k] ^ flips[i] for k, i in enumerate(P)}
    Q = tuple(sorted(img))
    return Q, tuple(img[q] for q in Q)


def main():
    out = {"W": [check_written(inst) for inst in WRITTEN]}
    ok = all(w["ok"] for w in out["W"])
    # SYM: orbits and symmetry lemma on {0,1}^4
    G = group()
    ps = parity_sets()
    rep1 = ps[((0, 1, 2, 3), 0)]
    rep2 = ps[((0, 1, 2), 0)]
    orb1 = {frozenset(act(g, x) for x in rep1) for g in G}
    orb2 = {frozenset(act(g, x) for x in rep2) for g in G}
    sym = {"group_order": len(G), "orbit1_size": len(orb1), "orbit2_size": len(orb2),
           "orbits_disjoint": not (orb1 & orb2), "union_is_ten_parity_sets": (orb1 | orb2) == set(ps.values())}
    lemma_ok = True
    for N in ps.values():
        for g in G:
            gN = {act(g, x) for x in N}
            for name, (rows, cols) in RESH.items():
                for R, C, P in comps(N, rows, cols):
                    imgP = frozenset(act(g, x) for x in P)
                    # the image block must be a component of gN in some reshaping
                    found = None
                    for name2, (rows2, cols2) in RESH.items():
                        for R2, C2, P2 in comps(gN, rows2, cols2):
                            if P2 == imgP:
                                found = (rows2, cols2, R2, C2)
                    if found is None:
                        lemma_ok = False
                        continue
                    rows2, cols2, R2, C2 = found
                    (r, r2), (c, c2) = sorted(R), sorted(C)
                    f = lemma10_form(rows, cols, r, r2, c, c2)
                    imgf = {act(g, x): s for x, s in f.items()}
                    (q, q2), (d, d2) = sorted(R2), sorted(C2)
                    f2 = lemma10_form(rows2, cols2, q, q2, d, d2)
                    if not (imgf == f2 or imgf == {x: -s for x, s in f2.items()}):
                        lemma_ok = False
    sym["symmetry_lemma_all_3840_cases"] = lemma_ok
    out["SYM"] = sym
    ok &= sym["orbit1_size"] == 2 and sym["orbit2_size"] == 8 and sym["orbits_disjoint"] and \
        sym["union_is_ten_parity_sets"] and lemma_ok
    # F1
    cube = list(itertools.product((0, 1), repeat=4))
    unif = set()
    for N in itertools.combinations(cube, 8):
        good = True
        for i, j in PAIRS:
            cnt = {}
            for x in N:
                cnt[(x[i], x[j])] = cnt.get((x[i], x[j]), 0) + 1
            if len(cnt) != 4 or any(v != 2 for v in cnt.values()):
                good = False
                break
        if good:
            unif.add(frozenset(N))
    out["F1"] = {"n_uniform": len(unif), "equals_parity_sets": unif == set(ps.values())}
    ok &= out["F1"]["equals_parity_sets"] and len(unif) == 10
    out["note"] = ("Phases are real unknowns phi_x = arg psi_x shared by the three reshapings; a zero signed form "
                   "with odd right side shows that no assignment of phases satisfies the congruences.")
    out["all_required_true"] = bool(ok)
    out["python"] = sys.version.split()[0]
    with open(os.path.join(HERE, "..", "evidence", "verify_lower42_r2.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps(out, indent=1))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
