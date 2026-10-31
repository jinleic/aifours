#!/usr/bin/env python3
"""Positive control for the reviewer's exact-cover DFS used in active-count-controls-v2.py.

Builds a random set P0 of 29 pairwise pair-distinct words in 6^4 (a partial OA(.,4,6,2)),
defines the forbidden pair sets as the complements of P0's six projections (7 pairs each),
and checks that the identical DFS routine FINDS a 29-word cover. This shows the DFS is not
trivially returning 'infeasible'. Usage: python3 -B <script> <new-output.json>
"""
import argparse
import itertools
import json
import random
import sys
import time
from pathlib import Path

PAIRS = list(itertools.combinations(range(4), 2))


def random_partial_oa(size, seed):
    rng = random.Random(seed)
    words = list(itertools.product(range(6), repeat=4))
    best = []
    for _ in range(4000):
        rng.shuffle(words)
        used = {p: set() for p in PAIRS}
        chosen = []
        for w in words:
            keys = [(p, (w[p[0]], w[p[1]])) for p in PAIRS]
            if all(k[1] not in used[k[0]] for k in keys):
                chosen.append(w)
                for p, v in keys:
                    used[p].add(v)
                if len(chosen) == size:
                    return chosen
        if len(chosen) > len(best):
            best = chosen
    return best


def exact_cover(forbidden, target, node_cap=200000):
    cands = [w for w in itertools.product(range(6), repeat=4)
             if all((w[i], w[j]) not in forbidden[(i, j)] for i, j in PAIRS)]
    slots = {(p, v): [] for p in PAIRS for v in itertools.product(range(6), repeat=2) if v not in forbidden[p]}
    for idx, w in enumerate(cands):
        for p in PAIRS:
            slots[(p, (w[p[0]], w[p[1]])).append(idx)
    covered = set()
    nodes = [0]
    sol = []

    def rec():
        nodes[0] += 1
        if nodes[0] > node_cap:
            raise TimeoutError
        if len(covered) == len(slots):
            return True
        best, bestlist = None, None
        for s, lst in slots.items():
            if s in covered:
                continue
            avail = [idx for idx in lst if all(((p, (cands[idx][p[0]], cands[idx][p[1]])) not in covered) for p in PAIRS)]
            if best is None or len(avail) < len(bestlist):
                best, bestlist = s, avail
                if not avail:
                    return False
        for idx in bestlist:
            w = cands[idx]
            keys = [(p, (w[p[0]], w[p[1]])) for p in PAIRS]
            covered.update(keys)
            sol.append(w)
            if rec():
                return True
            sol.pop()
            covered.difference_update(keys)
        return False

    try:
        found = rec()
    except TimeoutError:
        return 'capped', nodes[0], len(cands), []
    return ('found' if found else 'infeasible'), nodes[0], len(cands), sol


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('out', type=Path)
    a = ap.parse_args()
    if a.out.exists():
        sys.exit('refusing to overwrite')
    out = {'runs': []}
    for seed in (1, 2, 3):
        P0 = random_partial_oa(29, seed)
        if len(P0) < 29:
            out['runs'].append({'seed': seed, 'status': 'could_not_build_P0', 'size': len(P0)})
            continue
        forb = {p: {v for v in itertools.product(range(6), repeat=2)} - {(w[p[0]], w[p[1]]) for w in P0} for p in PAIRS}
        assert all(len(f) == 7 for f in forb.values())
        t0 = time.time()
        status, nodes, ncand, sol = exact_cover(forb, 29)
        ok = status == 'found' and len(sol) == 29 and all(
            len({(w[i], w[j]) for w in sol}) == 29 for i, j in PAIRS) and all(
            (w[i], w[j]) not in forb[(i, j)] for w in sol for i, j in PAIRS)
        out['runs'].append({'seed': seed, 'status': status, 'nodes': nodes, 'candidate_words': ncand,
                            'solution_verified': ok, 'seconds': round(time.time() - t0, 2)})
    out['scope'] = 'Positive control only: forbidden sets here are complements of a random partial OA, not a residual geometry.'
    with a.out.open('x', encoding='utf-8') as f:
        json.dump(out, f, indent=2)
        f.write('\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
