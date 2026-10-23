#!/usr/bin/env python3
"""Falsification control for Corollary ROT-o2 (proof-ROT-lowodd-v1.md), rotation slice 2026-10-18.
Stochastic local search over words of length N = 4p-2 whose maximal constant reflection blocks contain at most two odd
blocks (o <= 2), minimising the exact number of identity 2p-subwords (counting raw DP of sharp_search_v1).
  mode 'nonrigid': additionally require non-rigid rotations; Corollary ROT-o2 predicts NO avoider (a hit refutes the
                   written proof and is printed after independent re-verification).
  mode 'any'     : positive control; rigid avoiders (rho_c^(2p-1) sigma_y^(2p-1), K2 shapes) should be found.
Usage: ctl_rot_o2_v1.py MODE p seed iters restarts
"""
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rawdp, grx  # noqa: E402
from sharp_search_v1 import count_identity, nonrigid, verify  # noqa: E402


def odd_blocks(w, p):
    b = grx.blocks_of(w, p)
    if b is None:
        return 0
    return sum(l % 2 for l in b[1])


def ok(w, p, mode):
    if odd_blocks(w, p) > 2 or not any(k == 's' for k, _ in w):
        return False
    return nonrigid(w, p) if mode == 'nonrigid' else True


def main():
    mode, p, seed, iters, restarts = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    N = 4 * p - 2
    rng = random.Random(seed)
    hits = []
    best_overall = None
    for r in range(restarts):
        # start: few reflection values so that o <= 2 is easy to satisfy
        while True:
            ys = [rng.randrange(p) for _ in range(2)]
            w = []
            for _ in range(N):
                if rng.random() < 0.5:
                    w.append(('s', rng.choice(ys)))
                else:
                    w.append(('r', rng.randrange(p)))
            if ok(w, p, mode):
                break
        cur = count_identity(w, p)
        for it in range(iters):
            if cur == 0:
                break
            w2 = list(w)
            j = rng.randrange(N)
            u = rng.random()
            if u < 0.3:
                i = rng.randrange(N)
                x = w2.pop(i)
                w2.insert(j, x)
            elif u < 0.6:
                w2[j] = ('r', rng.randrange(p))
            else:
                w2[j] = ('s', rng.randrange(p))
            if not ok(w2, p, mode):
                continue
            c2 = count_identity(w2, p)
            if c2 <= cur or rng.random() < 0.01:
                w, cur = w2, c2
        best_overall = cur if best_overall is None else min(best_overall, cur)
        if cur == 0:
            hits.append({'restart': r, 'verified_avoider': verify(w, p), 'nonrigid': nonrigid(w, p),
                         'odd_blocks': odd_blocks(w, p), 'word': rawdp.fmt(w)})
            print(json.dumps(hits[-1]), flush=True)
    print(json.dumps({'summary': 1, 'mode': mode, 'p': p, 'N': N, 'seed': seed, 'iters': iters, 'restarts': restarts,
                      'hits': len(hits), 'nonrigid_hits': sum(h['nonrigid'] for h in hits),
                      'min_count_last': best_overall}), flush=True)


if __name__ == '__main__':
    main()
