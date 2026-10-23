#!/usr/bin/env python3
"""Exact controls of the G6 singleton same-ray implication; no numerical vectors.

Use unnormalised integer vectors for the printed non-classical QLS(4), since
normalisation cannot change Gram zero/nonzero. Also use three classical QLS(7)
and both exact Gram supports of the published (Psi(f),Phi(m)) pair.
Usage: g6_controls.py OUT.json
"""
import datetime
import hashlib
import itertools
import json
import sys


def check(points, frame, gram):
    anchors, violations = [], []
    for p in points:
        if p in frame:
            continue
        neighbours = [q for q in frame if gram(p, q)]
        if len(neighbours) != 1:
            continue
        q = neighbours[0]
        anchors.append((p, q))
        for t in points:
            if t not in (p, q) and gram(p, t) != gram(q, t):
                violations.append((p, q, t))
    return anchors, violations


def run_control(name, n, gram):
    points = [(i, j) for i in range(n) for j in range(n)]
    frame = [(0, j) for j in range(n)]
    anchors, bad = check(points, frame, gram)
    assert not bad, name
    rejected = 0
    for p, q in anchors:
        # Change one Gram predicate involving q but not another frame point,
        # so the chosen anchor at p remains singleton. Only G6 is evaluated.
        t = next(t for t in points if t not in frame and t not in (p, q))
        edge = frozenset((q, t))
        altered = lambda x, y: (not gram(x, y)) if frozenset((x, y)) == edge else gram(x, y)
        _, failures = check(points, frame, altered)
        assert failures, (name, p, q, t)
        rejected += 1
    return {"name": name, "order": n, "singleton_anchors": len(anchors), "G6_violations": 0,
            "single_predicate_mutations": len(anchors), "mutations_rejected_by_G6": rejected}


def main(out):
    results = []
    for a in (1, 2, 3):
        results.append(run_control("classical linear QLS7 slope %d" % a, 7,
                                   lambda p, q: (a * p[0] + p[1]) % 7 == (a * q[0] + q[1]) % 7))
    e = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
    vp, vm = (1, 1, 0, 0), (1, -1, 0, 0)
    Q = [[e[0], e[1], e[2], e[3]], [e[1], e[0], e[3], e[2]],
         [e[2], e[3], vp, vm], [e[3], e[2], vm, vp]]
    dot = lambda p, q: sum(x * y for x, y in zip(Q[p[0]][p[1]], Q[q[0]][q[1]])) != 0
    results.append(run_control("printed non-classical QLS4 (integer representatives)", 4, dot))
    H = {1, 2, 4}
    f0 = [x if x in H else 0 for x in range(7)]
    is_perm = lambda seq: len({x % 7 for x in seq}) == 7
    M = [m for m in range(7) if is_perm([f0[x] - m * x for x in range(7)])]
    m0 = M[0]
    f = [(f0[x] - m0 * x) % 7 for x in range(7)]
    m = next((t - m0) % 7 for t in M if t != m0)
    def psi_gram(p, q):
        return not is_perm([(q[0] - p[0]) * f[x] + (q[1] - p[1]) * x for x in range(7)])
    results.append(run_control("published Psi(f) QLS7 (exact roots-of-unity zero criterion)", 7, psi_gram))
    results.append(run_control("published Phi(m) mate", 7,
                               lambda p, q: (m * p[0] + p[1]) % 7 == (m * q[0] + q[1]) % 7))
    with open(__file__, "rb") as file:
        code_hash = hashlib.sha256(file.read()).hexdigest()
    record = {"recorded_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
              "code_sha256": code_hash, "status": "PASS", "controls": results,
              "scope": "G6 implication and its own mutation controls, not cube search coverage or full vector existence"}
    with open(out, "x") as file:
        json.dump(record, file, indent=2)
        file.write("\n")
    print(json.dumps(record))


if __name__ == "__main__":
    main(sys.argv[1])
