#!/usr/bin/env python3
"""End-to-end check of Theorem P's mechanism for D_2p (left convention).

For a cyclic word (rotated to end with a reflection) with F reflections and
gap sizes n_t, Theorem P asserts: if F + sum_t floor(n_t/2) >= 3p-1 and the
length is <= 4p-1, the PAIRED family contains an identity 2p-subword, where the
paired family = colourings u (u_1 = 0) x pair-marks; in each gap the rotations
are split into consecutive pairs (both selected or neither) plus at most one
singleton that is never selected.

This script enumerates the paired family exhaustively per word and checks:
  (a) every found identity selection has size exactly 2p (never p or 3p);
  (b) at least one exists whenever the hypothesis holds;
  (c) the Chevalley-Warning signed count over the paired family is 0 mod p.
Words: random words of length 4p-1 (and shorter) over D_2p, biased toward the
hypothesis region and toward few distinct values (degenerate cases).
"""
import itertools
import random
import sys


def run(p, word):
    F = sum(1 for (_, e) in word if e == -1)
    if F == 0 or word[-1][1] != -1:
        return None
    gaps = [[] for _ in range(F + 1)]  # gaps[t] rotations before f_t, t=1..F
    t = 1
    refl = []
    for i, (x, e) in enumerate(word):
        if e == 1:
            gaps[t].append(i)
        else:
            refl.append(i)
            t += 1
    pairs = []  # (gap, i1, i2)
    singles = []
    for t in range(1, F + 1):
        g = gaps[t]
        for k in range(0, len(g) - 1, 2):
            pairs.append((t, g[k], g[k + 1]))
        if len(g) % 2:
            singles.append((t, g[-1]))
    hyp = F + len(pairs) >= 3 * p - 1
    nv = (F - 1) + len(pairs)
    found_sizes = set()
    cw = 0
    for bits in itertools.product((0, 1), repeat=nv):
        u = [None, 0] + list(bits[:F - 1])
        mk = bits[F - 1:]
        sel = []
        for j, i in enumerate(refl):
            tt = j + 1
            un = u[tt + 1] if tt < F else u[1]
            if u[tt] != un:
                sel.append(i)
        for k, (tt, i1, i2) in enumerate(pairs):
            if mk[k] ^ u[tt]:
                sel += [i1, i2]
        sel.sort()
        v, e = 0, 1
        for i in sel:
            x, f = word[i]
            v = (v + e * x) % p
            e *= f
        assert e == 1
        size = len(sel)
        assert size % 2 == 0
        if v == 0 and size % p == 0:
            cw += pow(p - 1, sum(bits), p)
            if size > 0:
                found_sizes.add(size)
    return hyp, nv, found_sizes, cw % p


def main():
    p = int(sys.argv[1])
    trials = int(sys.argv[2])
    rng = random.Random(int(sys.argv[3]) if len(sys.argv) > 3 else 0)
    stats = {'hyp': 0, 'hyp_ok': 0, 'bad_size': 0, 'cw_bad': 0, 'skipped': 0}
    for _ in range(trials):
        N = 4 * p - 1
        k = rng.choice((2, 3, 4, 2 * p))
        alph = [(rng.randrange(p), rng.choice((1, -1))) for _ in range(k)]
        # bias: many reflections / even rotation runs
        w = []
        while len(w) < N - 1:
            a = rng.choice(alph)
            run_len = rng.choice((1, 2, 2, 4)) if a[1] == 1 else 1
            w += [a] * run_len
        w = w[:N - 1] + [(rng.randrange(p), -1)]
        r = run(p, w) if (sum(1 for (_, e) in w if e == -1) - 1 + sum(1 for (_, e) in w if e == 1) // 2) <= 22 else None
        if r is None:
            stats['skipped'] += 1
            continue
        hyp, nv, sizes, cw = r
        if any(s != 2 * p for s in sizes):
            stats['bad_size'] += 1
        if hyp:
            stats['hyp'] += 1
            if 2 * p in sizes:
                stats['hyp_ok'] += 1
            else:
                print('HYPOTHESIS HOLDS BUT NO SOLUTION', w)
            if cw != 0:
                stats['cw_bad'] += 1
    print('p', p, stats)


if __name__ == '__main__':
    main()
