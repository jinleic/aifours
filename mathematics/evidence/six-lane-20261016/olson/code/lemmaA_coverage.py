#!/usr/bin/env python3
"""For words over D_2p in type patterns NOT covered by EGZ / Option-alpha /
Theorem P, test whether the Cauchy-Davenport "Lemma A" certificate exists:
  exists an even set Phi of reflections (|Phi| = 2j <= 2p-2) such that the
  multiset S_Phi of SIGNED rotation values (sign fixed by Phi) satisfies
     sum_g min(k, mu(g)) - k + 1 >= p,   k = 2p - 2j,
  (then the k-subset sums of S_Phi cover Z_p, so an identity 2p-subword exists).
Also tests the exact (not bound-based) version: exists Phi, T with |T| = k and
signed sum = -V(Phi).  Words failing the CD-bound certificate are printed with
their rotation-value / reflection-value structure for inspection.
"""
import itertools
import random
import sys
from collections import Counter


def gaps_of_word(word):
    # word list of (val, eps); rotate to end with a reflection
    i0 = max(i for i, (_, e) in enumerate(word) if e == -1)
    w = word[i0 + 1:] + word[:i0 + 1]
    return w


def lemmaA(p, word):
    w = gaps_of_word(word)
    refl = [i for i, (_, e) in enumerate(w) if e == -1]
    rot = [i for i, (_, e) in enumerate(w) if e == 1]
    F = len(refl)
    best = None
    for j in range(1, p):
        k = 2 * p - 2 * j
        if 2 * j > F or k > len(rot):
            continue
        for Phi in itertools.combinations(range(F), 2 * j):
            phiset = set(refl[t] for t in Phi)
            # signs
            par = 0
            signed = []
            V = 0
            sgn = 1
            for i, (x, e) in enumerate(w):
                if e == -1:
                    if i in phiset:
                        V = (V + sgn * x) % p
                        sgn = -sgn
                else:
                    signed.append((sgn * x) % p)
            mu = Counter(signed)
            val = sum(min(k, c) for c in mu.values()) - k + 1
            if val >= p:
                return ('cd', 2 * j)
    return None


def has_solution(p, word):
    K = 2 * p
    P = [set() for _ in range(K + 1)]
    P[0].add((0, 1))
    for (x, e) in word:
        for k in range(K, 0, -1):
            if P[k - 1]:
                P[k] |= {((v + ep * x) % p, ep * e) for (v, ep) in P[k - 1]}
    return (0, 1) in P[K]


def main():
    p = int(sys.argv[1])
    trials = int(sys.argv[2])
    rng = random.Random(int(sys.argv[3]) if len(sys.argv) > 3 else 0)
    N = 4 * p - 1
    sys.path.insert(0, __file__.rsplit('/', 1)[0])
    from coverage_patterns import gaps_of, option_alpha_items, canon_cyclic
    stats = Counter()
    shown = 0
    for _ in range(trials):
        # random pattern
        mode = rng.random()
        if mode < 0.5:
            types = [rng.choice('RF') for _ in range(N)]
        else:
            types = []
            t = rng.choice('RF')
            while len(types) < N:
                types += [t] * rng.choice((1, 1, 1, 2, 3))
                t = 'F' if t == 'R' else 'R'
            types = types[:N]
        s = ''.join(types)
        if 'F' not in s:
            continue
        R = s.count('R')
        F = N - R
        if R >= 3 * p - 1:
            continue
        g = gaps_of(s)
        if F + sum(x // 2 for x in g) >= 3 * p - 1 or option_alpha_items(s) >= 2 * p - 1:
            continue
        stats['uncovered_pattern'] += 1
        # values: degenerate-biased
        xa = rng.choice([[1], [1, p - 1], list(range(p))])
        ya = rng.choice([[0], [0, 1], list(range(p))])
        word = [((rng.choice(xa) if ch == 'R' else rng.choice(ya)), 1 if ch == 'R' else -1) for ch in s]
        r = lemmaA(p, word)
        if r:
            stats['lemmaA_cd'] += 1
        else:
            stats['lemmaA_fail'] += 1
            if not has_solution(p, word):
                stats['NO_SOLUTION'] += 1
                print('COUNTEREXAMPLE?', word)
            if shown < 12:
                shown += 1
                print('fail:', ''.join(('r%d' % x if e == 1 else 's%d' % x) + ' ' for x, e in word))
    print('p', p, dict(stats))


if __name__ == '__main__':
    main()
