#!/usr/bin/env python3
"""tetrad_facts.py -- exhaustive check of the finite facts used in notes/case-split-r1.md Lemma T (stdlib).

F1 Two different splits of a 4-set into two pairs: every part of one meets every part of the other in 1 point.
F2 Seed: on 7 points X = {1,2,3,4,a,b,d}, T = 1234, T1 = 12ab, T2 = 13ad span a 3-dimensional code whose 7 nonzero
   words all have weight 4 (listed in the note); its dual on X is a [7,4] code with weight distribution
   {0:1, 3:7, 4:7, 7:1}; its weight-4 words are the 7 seed-span words; its weight-3 words form a Fano plane
   (7 triples, every pair of points in exactly one).
F3 For every weight-3 dual word L and a new point y: the span of the seed words and L+{y} is a self-dual [8,4] code
   with weight distribution {0:1, 4:14, 8:1} whose 14 weight-4 words are the 7 seed words and the 7 sets L'+{y}.
F4 The enumeration's e7 (complements of the Fano lines 012 034 056 135 146 236 245, code/e_multisets.py) is the image
   of the seed e7 under an explicit point bijection; the enumeration's e8 (planes of AG(3,2)) is the image of the F3
   e8 under an explicit bijection.  (Found by brute force; printed.)
Usage: tetrad_facts.py OUT.json   (exclusive)
"""
import itertools
import json
import sys


def span(words, n):
    S = {0}
    for w in words:
        S |= {s ^ w for s in S}
    return S


def wt(x):
    return bin(x).count("1")


def mask(pts, idx):
    m = 0
    for p in pts:
        m |= 1 << idx[p]
    return m


def dual(S, n):
    return {x for x in range(1 << n) if all(wt(x & s) % 2 == 0 for s in S)}


def dist(S):
    out = {}
    for s in S:
        out[wt(s)] = out.get(wt(s), 0) + 1
    return dict(sorted(out.items()))


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    rep, ok = {}, True
    # F1
    q = [0, 1, 2, 3]
    splits = [({0, 1}, {2, 3}), ({0, 2}, {1, 3}), ({0, 3}, {1, 2})]
    f1 = all(len(P & Q) == 1 for s1, s2 in itertools.combinations(splits, 2) for P in s1 for Q in s2)
    rep["F1"] = f1
    ok &= f1
    # F2
    X = ["1", "2", "3", "4", "a", "b", "d"]
    idx = {p: i for i, p in enumerate(X)}
    T, T1, T2 = mask("1234", idx), mask("12ab", idx), mask("13ad", idx)
    E7 = span([T, T1, T2], 7)
    nz = sorted(E7 - {0})
    named = sorted("".join(X[i] for i in range(7) if w >> i & 1) for w in nz)
    f2a = len(E7) == 8 and all(wt(w) == 4 for w in nz)
    H = dual(E7, 7)
    f2b = dist(H) == {0: 1, 3: 7, 4: 7, 7: 1}
    f2c = {w for w in H if wt(w) == 4} == set(nz)
    lines = [w for w in H if wt(w) == 3]
    f2d = len(lines) == 7 and all(sum(1 for L in lines if (L >> i & 1) and (L >> j & 1)) == 1
                                  for i, j in itertools.combinations(range(7), 2))
    rep["F2"] = {"seed_span_words": named, "nonzero_all_weight4": f2a, "dual_distribution": dist(H),
                 "dual_w4_equals_seed_words": f2c, "dual_w3_is_fano": f2d}
    ok &= f2a and f2b and f2c and f2d
    # F3
    f3 = True
    for L in lines:
        e8 = span(nz + [L | 1 << 7], 8)
        w4 = {w for w in e8 if wt(w) == 4}
        expect = set(nz) | {Lp | 1 << 7 for Lp in lines}
        f3 &= dist(e8) == {0: 1, 4: 14, 8: 1} and dual(e8, 8) == e8 and w4 == expect
    rep["F3"] = f3
    ok &= f3
    # F4
    FANO = [(0, 1, 2), (0, 3, 4), (0, 5, 6), (1, 3, 5), (1, 4, 6), (2, 3, 6), (2, 4, 5)]
    enum_e7 = {sum(1 << p for p in set(range(7)) - set(Lf)) for Lf in FANO}
    bij7 = None
    for perm in itertools.permutations(range(7)):
        img = {sum(1 << perm[i] for i in range(7) if w >> i & 1) for w in nz}
        if img == enum_e7:
            bij7 = perm
            break
    enum_e8 = {sum(1 << x for x in range(8) if bin(a & x).count("1") % 2 == b) for a in range(1, 8) for b in (0, 1)}
    seed_e8_w4 = {w for w in span(nz + [lines[0] | 1 << 7], 8) if wt(w) == 4}
    bij8 = None
    for perm in itertools.permutations(range(8)):
        img = {sum(1 << perm[i] for i in range(8) if w >> i & 1) for w in seed_e8_w4}
        if img == enum_e8:
            bij8 = perm
            break
    rep["F4"] = {"e7_bijection_seed_point_i_to": bij7, "e8_bijection_point_i_to": bij8}
    ok &= bij7 is not None and bij8 is not None
    rep["all_pass"] = ok
    with open(argv[1], "x") as f:
        json.dump(rep, f, indent=1)
    print(json.dumps(rep))
    print("TETRAD-FACTS", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
