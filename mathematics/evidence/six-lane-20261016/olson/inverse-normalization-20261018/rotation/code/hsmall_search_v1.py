#!/usr/bin/env python3
"""Obligation HS (rotation slice, 2026-10-18): bounded falsification of ROT(p) in the regime NOT covered by the written
proofs: many odd blocks (o >= 4) and few reflection pairs (H = sum floor(l_i/2) over maximal constant blocks small).
A word is a cyclic sequence of k single reflections (consecutive reflections must differ, so every maximal constant
block has length 1 and H = 0; with hmax >= 1 some blocks may be lengthened) separated by rotation runs.
Local search minimising the exact number of identity 2p-subwords (raw ordered-product counting DP of
sharp_search_v1.count_identity), restricted to non-rigid words with odd-block count >= omin and H <= hmax.
A hit is re-verified by rawdp.witness and the unchanged olson/code/was_verify.py dp_has.  A miss is UNKNOWN.
Positive control (mode 'any'): same search without the non-rigid restriction.
Usage: hsmall_search_v1.py MODE p seed iters restarts hmax omin
"""
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rawdp, grx  # noqa: E402
from sharp_search_v1 import count_identity, nonrigid, verify  # noqa: E402


def shape(w, p):
    b = grx.blocks_of(w, p)
    if b is None:
        return None
    ys, ls, Xs = b
    return sum(l // 2 for l in ls), sum(l % 2 for l in ls)


def ok(w, p, mode, hmax, omin):
    s = shape(w, p)
    if s is None:
        return False
    H, o = s
    if H > hmax or o < omin:
        return False
    return nonrigid(w, p) if mode == 'search' else True


def main():
    mode, p, seed, iters, restarts, hmax, omin = (sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]),
                                                  int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]))
    N = 4 * p - 2
    rng = random.Random(seed)
    hits = 0
    best = None
    for r in range(restarts):
        while True:
            k = rng.randrange(max(omin, p), 3 * p - 1)
            w = []
            for _ in range(k):
                w.append(('s', rng.randrange(p)))
            for _ in range(N - k):
                w.insert(rng.randrange(len(w) + 1), ('r', rng.choice([1, 1, 1, p - 1, rng.randrange(p)])))
            if ok(w, p, mode, hmax, omin):
                break
        cur = count_identity(w, p)
        for it in range(iters):
            if cur == 0:
                break
            w2 = list(w)
            u = rng.random()
            j = rng.randrange(N)
            if u < 0.35:
                i = rng.randrange(N)
                x = w2.pop(i)
                w2.insert(j, x)
            elif u < 0.7:
                if w2[j][0] == 'r':
                    w2[j] = ('r', rng.randrange(p))
                else:
                    w2[j] = ('s', rng.randrange(p))
            else:
                i = rng.randrange(N)
                w2[i], w2[j] = w2[j], w2[i]
            if not ok(w2, p, mode, hmax, omin):
                continue
            c2 = count_identity(w2, p)
            if c2 <= cur or rng.random() < 0.02:
                w, cur = w2, c2
        best = cur if best is None else min(best, cur)
        if cur == 0:
            hits += 1
            H, o = shape(w, p)
            print(json.dumps({'restart': r, 'verified_avoider': verify(w, p), 'nonrigid': nonrigid(w, p), 'H': H,
                              'o': o, 'word': rawdp.fmt(w)}), flush=True)
    print(json.dumps({'summary': 1, 'mode': mode, 'p': p, 'N': N, 'seed': seed, 'iters': iters, 'restarts': restarts,
                      'hmax': hmax, 'omin': omin, 'hits': hits, 'best_last': best}), flush=True)


if __name__ == '__main__':
    main()
