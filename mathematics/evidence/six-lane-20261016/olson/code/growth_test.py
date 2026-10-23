#!/usr/bin/env python3
"""Exploratory test of a Cauchy-Davenport-type growth conjecture for ordered
products in D_2p (left convention (v,e)(v',e') = (v+e v', e e')):

  G(N,k):  for every word w of length N, either the identity is an ordered
           k-subword product, or |{rotation values of k-subword products}|
           >= min(p, N - k - p + 1).

Checked on random words, low-alphabet words, and run-structured words.
Reports violations (word, N, k, size) for inspection.
"""
import random
import sys


def products(p, w, K):
    # P[k] = set of (v, e) reachable with k selected letters
    P = [set() for _ in range(K + 1)]
    P[0].add((0, 1))
    for (x, e) in w:
        for k in range(K, 0, -1):
            src = P[k - 1]
            if src:
                P[k] |= {((v + ep * x) % p, ep * e) for (v, ep) in src}
    return P


def rand_word(p, N, rng):
    mode = rng.random()
    if mode < 0.3:
        return [(rng.randrange(p), rng.choice((1, -1))) for _ in range(N)]
    if mode < 0.7:
        alph = [(rng.randrange(p), rng.choice((1, -1))) for _ in range(rng.choice((2, 3)))]
        return [rng.choice(alph) for _ in range(N)]
    # run-structured: alternating runs of constant letters
    w = []
    t = rng.choice((1, -1))
    while len(w) < N:
        ln = rng.randint(1, max(1, N // 3))
        letter = (rng.choice((1, p - 1)) if t == 1 else rng.randrange(p), t)
        w += [letter] * ln
        t = -t
    return w[:N]


def main():
    p = int(sys.argv[1])
    trials = int(sys.argv[2])
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    rng = random.Random(seed)
    viol = 0
    for _ in range(trials):
        N = rng.randint(2 * p, 4 * p - 1)
        w = rand_word(p, N, rng)
        k = 2 * p
        P = products(p, w, k)
        if (0, 1) in P[k]:
            continue
        rot = {v for (v, e) in P[k] if e == 1}
        bound = min(p, N - k - p + 1)
        if len(rot) < bound:
            viol += 1
            if viol <= 15:
                print('VIOLATION N=%d k=%d |rot|=%d bound=%d word=%s' % (N, k, len(rot), bound, w))
    print('p', p, 'trials', trials, 'violations', viol)


if __name__ == '__main__':
    main()
