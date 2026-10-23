#!/usr/bin/env python3
"""Positive semantic control: the explicit point-cyclic resolution of a cyclic 2-(64,4,1) design printed in
Topalova-Zhelezova, Axioms 15 (2026) 762, PDF pp. 6-7 (sources/axioms-15-00762.pdf), transcribed verbatim
(1-based points, g = (1,2,...,64), i.e. i -> i+1 with 64 -> 1) and converted to Z_64 by x -> x-1.

Checks (stdlib, exact):
  C1 the developed design (base blocks under +1) has 336 distinct blocks and covers every pair of Z_64 exactly once;
  C2 the printed classes P1, P2, P3 are parallel classes (partitions of Z_64) consisting of design blocks;
  C3 the resolution {P1} u {P2+i : i<4} u {P3+i : i<16} has 21 pairwise disjoint classes covering all 336 blocks and
     is mapped to itself by x -> x+1 (point-cyclic in the sense of Definition 5); class orbit lengths 1, 4, 16;
  C4 the lemmas of PROOF.md specialised to v = 64 hold on this example: short blocks = the 16 cosets of <16>;
     each class contains 0 or 16 short blocks (type T1); stabilizer orders of the non-short classes lie in the
     admissible set {4, 8, 16}; no block of a class contains a pair whose difference lies in the class stabilizer;
     the intersection of the non-short class stabilizers is <16> = H4, so the 88-style contradiction does NOT arise
     (the forbidden differences 16, 32, 48 are exactly the short-block differences);
  C5 negative controls: four corruptions of the resolution, each must be rejected by C2/C3.
Writes controls/control64-receipt.json.
"""
import json
import os
import sys

V = 64
BASE_1 = [(1, 17, 33, 49), (1, 2, 4, 8), (1, 11, 25, 36), (1, 13, 28, 47), (1, 9, 29, 52), (1, 6, 39, 48)]
P1_1 = [(1, 17, 33, 49), (2, 18, 34, 50), (3, 19, 35, 51), (4, 20, 36, 52), (5, 21, 37, 53), (6, 22, 38, 54),
        (7, 23, 39, 55), (8, 24, 40, 56), (9, 25, 41, 57), (10, 26, 42, 58), (11, 27, 43, 59), (12, 28, 44, 60),
        (13, 29, 45, 61), (14, 30, 46, 62), (15, 31, 47, 63), (16, 32, 48, 64)]
P2_1 = [(1, 6, 39, 48), (5, 10, 43, 52), (9, 14, 47, 56), (13, 18, 51, 60), (17, 22, 55, 64), (21, 26, 59, 4),
        (25, 30, 63, 8), (29, 34, 3, 12), (33, 38, 7, 16), (37, 42, 11, 20), (41, 46, 15, 24), (45, 50, 19, 28),
        (49, 54, 23, 32), (53, 58, 27, 36), (57, 62, 31, 40), (61, 2, 35, 44)]
P3_1 = [(1, 2, 4, 8), (17, 18, 20, 24), (33, 34, 36, 40), (49, 50, 52, 56), (3, 11, 31, 54), (19, 27, 47, 6),
        (35, 43, 63, 22), (51, 59, 15, 38), (13, 23, 37, 48), (29, 39, 53, 64), (45, 55, 5, 16), (61, 7, 21, 32),
        (9, 28, 46, 58), (25, 44, 62, 10), (41, 60, 14, 26), (57, 12, 30, 42)]


def z(blocks):
    return [frozenset((x - 1) % V for x in b) for b in blocks]


def shift(blk, i):
    return frozenset((x + i) % V for x in blk)


def design():
    blocks = set()
    for b in z(BASE_1):
        for i in range(V):
            blocks.add(shift(b, i))
    return blocks


def pair_cover_ok(blocks):
    cnt = {}
    for b in blocks:
        s = sorted(b)
        for a in range(4):
            for c in range(a + 1, 4):
                cnt[(s[a], s[c])] = cnt.get((s[a], s[c]), 0) + 1
    return len(cnt) == V * (V - 1) // 2 and all(c == 1 for c in cnt.values())


def is_parallel_class(cls, blocks):
    pts = [x for b in cls for x in b]
    return len(cls) == V // 4 and sorted(pts) == list(range(V)) and all(b in blocks for b in cls)


def resolution(p1, p2, p3):
    classes = [frozenset(p1)]
    classes += [frozenset(shift(b, i) for b in p2) for i in range(4)]
    classes += [frozenset(shift(b, i) for b in p3) for i in range(16)]
    return classes


def check_resolution(classes, blocks):
    errs = []
    for k, c in enumerate(classes):
        if not is_parallel_class(c, blocks):
            errs.append("class %d is not a parallel class of design blocks" % k)
    allb = [b for c in classes for b in c]
    if len(classes) != 21 or len(set(classes)) != 21:
        errs.append("not 21 distinct classes")
    if len(allb) != 336 or set(allb) != blocks:
        errs.append("classes do not partition the 336 blocks")
    cset = set(classes)
    for c in classes:
        if frozenset(shift(b, 1) for b in c) not in cset:
            errs.append("x->x+1 does not map some class to a class")
            break
    return errs


def class_stab(c):
    return [d for d in range(V) if frozenset(shift(b, d) for b in c) == c]


def main():
    rep = {}
    blocks = design()
    rep["C1"] = dict(blocks=len(blocks), pairs_once=pair_cover_ok(blocks))
    p1, p2, p3 = z(P1_1), z(P2_1), z(P3_1)
    rep["C2"] = dict(P1=is_parallel_class(p1, blocks), P2=is_parallel_class(p2, blocks), P3=is_parallel_class(p3, blocks))
    classes = resolution(p1, p2, p3)
    errs = check_resolution(classes, blocks)
    orbit_lengths = sorted({len({frozenset(frozenset(shift(b, i) for b in c)) for i in range(V)}) for c in classes})
    rep["C3"] = dict(errors=errs, class_orbit_lengths=orbit_lengths)
    H4 = frozenset({0, 16, 32, 48})
    cosets = {frozenset((a + t) % V for t in H4) for a in range(V)}
    short = {b for b in blocks if any(shift(b, d) == b for d in range(1, V))}
    stabs = [class_stab(c) for c in classes]
    m = [len([b for b in c if b in short]) for c in classes]
    nonshort = [k for k in range(21) if m[k] == 0]
    # Lemma (PROOF.md, Lemma 4 general form): if B in P, x, x+d in B and d in Stab(P), then d in Stab(B).
    # For full blocks (trivial stabilizer) this says: no pair difference of B lies in Stab(P) \ {0}.
    forbidden_ok = all(((y - x) % V) not in stabs[k] or shift(b, (y - x) % V) == b
                       for k in range(21) for b in classes[k] for x in b for y in b if x != y)
    forbidden_full_ok = all(((y - x) % V) not in stabs[k] for k in nonshort for b in classes[k] for x in b for y in b if x != y)
    forbidden_ok = forbidden_ok and forbidden_full_ok
    inter = set(range(V))
    for k in nonshort:
        inter &= set(stabs[k])
    rep["C4"] = dict(short_blocks_are_H4_cosets=(short == cosets), short_per_class=sorted(set(m)),
                     T1=(sorted(m).count(16) == 1 and sorted(m).count(0) == 20),
                     nonshort_stabilizer_orders=sorted({len(stabs[k]) for k in nonshort}),
                     forbidden_difference_lemma_holds=forbidden_ok,
                     intersection_of_nonshort_stabilizers=sorted(inter),
                     intersection_inside_H4=set(inter) <= set(H4))
    # negative controls
    neg = {}
    # (a) move one block from class 1 to class 2 (two classes stop being parallel classes)
    a = list(classes[1]); b2 = list(classes[2])
    neg["moved_block"] = check_resolution([classes[0], frozenset(a[1:]), frozenset(b2 + a[:1])] + classes[3:], blocks)
    # (b) swap two points between two blocks of P3 (the blocks are no longer design blocks)
    q = [set(x) for x in p3]
    u, w = sorted(q[4])[0], sorted(q[8])[0]
    q[4].discard(u); q[4].add(w); q[8].discard(w); q[8].add(u)
    neg["swapped_points"] = check_resolution(resolution(p1, p2, [frozenset(x) for x in q]), blocks)
    # (c) one class listed twice, another omitted
    neg["duplicated_class"] = check_resolution(classes[:5] + [classes[6]] + classes[6:], blocks)
    # (d) validity-preserving: reorder two classes (must be ACCEPTED)
    neg["reordered_classes"] = check_resolution(classes[:19] + [classes[20], classes[19]], blocks)
    rep["C5"] = {k: ("REJECTED: " + "; ".join(v)) if v else "ACCEPTED" for k, v in neg.items()}
    ok = (rep["C1"]["blocks"] == 336 and rep["C1"]["pairs_once"] and all(rep["C2"].values()) and not errs
          and orbit_lengths == [1, 4, 16] and rep["C4"]["short_blocks_are_H4_cosets"] and rep["C4"]["T1"]
          and rep["C4"]["forbidden_difference_lemma_holds"] and rep["C4"]["intersection_inside_H4"]
          and set(rep["C4"]["nonshort_stabilizer_orders"]) <= {4, 8, 16}
          and rep["C5"]["moved_block"].startswith("REJECTED") and rep["C5"]["swapped_points"].startswith("REJECTED")
          and rep["C5"]["duplicated_class"].startswith("REJECTED") and rep["C5"]["reordered_classes"] == "ACCEPTED")
    rep["verdict"] = "PASS" if ok else "FAIL"
    print(json.dumps(rep, indent=1, sort_keys=True))
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(here, "controls", "control64-receipt.json"), "w") as fh:
        json.dump(rep, fh, indent=1, sort_keys=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
