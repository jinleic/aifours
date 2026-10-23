#!/usr/bin/env python3
"""Coverage of the proved sufficient conditions on random/degenerate words over
D_2p (left convention), length 4p-1:
  EGZ        : R >= 3p-1
  ThmP       : F + sum floor(n_t/2) >= 3p-1
  Doubling(j): a stretch of 2j+1 consecutive gaps P M P ... M P such that
               p - 2j - sum_{M} n_M >= 0 rotations can be chosen from the
               P-gaps with  sum_M beta_M + (their sum) = 0 mod p,
               beta_M = y_left - y_right - (sum of rotations in gap M).
Words failing all tests are checked for an actual identity 2p-subword (exact
DP) and printed for structural inspection.
"""
import itertools
import random
import sys
from collections import Counter


def structure(word):
    # rotate to end with reflection; gaps[t] list of rotation values before f_t
    i0 = max(i for i, (_, e) in enumerate(word) if e == -1)
    w = word[i0 + 1:] + word[:i0 + 1]
    gaps, ys, cur = [], [], []
    for (x, e) in w:
        if e == 1:
            cur.append(x)
        else:
            gaps.append(cur)
            ys.append(x)
            cur = []
    return gaps, ys   # gap t is before reflection t (t = 0..F-1); cyclic


def ksums(vals, k, p):
    # set of sums of k-subsets (multiset) mod p
    S = [set() for _ in range(k + 1)]
    S[0].add(0)
    for v in vals:
        for c in range(k, 0, -1):
            S[c] |= {(s + v) % p for s in S[c - 1]}
    return S[k]


def doubling(p, gaps, ys):
    F = len(gaps)
    if F == 0:
        return False
    for j in range(0, (p - 1) // 2 + 1):
        if 2 * j + 1 > F:
            break
        for start in range(F):
            idx = [(start + i) % F for i in range(2 * j + 1)]
            if len(set(idx)) < 2 * j + 1:
                continue
            Pg = idx[0::2]
            Mg = idx[1::2]
            need = p - 2 * j - sum(len(gaps[t]) for t in Mg)
            if need < 0:
                continue
            beta = 0
            for t in Mg:
                # gap t lies between reflection t-1 and reflection t
                beta += ys[(t - 1) % F] - ys[t] - sum(gaps[t])
            pool = [x for t in Pg for x in gaps[t]]
            if need > len(pool):
                continue
            if (-beta) % p in ksums(pool, need, p):
                return True
    return False


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
    p = int(sys.argv[1]); trials = int(sys.argv[2]); rng = random.Random(int(sys.argv[3]))
    N = 4 * p - 1
    st = Counter()
    shown = 0
    for _ in range(trials):
        types = []
        t = rng.choice((1, -1))
        while len(types) < N:
            types += [t] * rng.choice((1, 1, 1, 2, 3, 5))
            t = -t
        types = types[:N]
        if -1 not in types:
            continue
        xa = rng.choice([[1], [1, p - 1], [1, 2], list(range(p))])
        ya = rng.choice([[0], [0, 1], list(range(p))])
        word = [((rng.choice(xa) if e == 1 else rng.choice(ya)), e) for e in types]
        R = sum(1 for (_, e) in word if e == 1)
        F = N - R
        gaps, ys = structure(word)
        if R >= 3 * p - 1:
            st['EGZ'] += 1; continue
        if F + sum(len(g) // 2 for g in gaps) >= 3 * p - 1:
            st['ThmP'] += 1; continue
        if doubling(p, gaps, ys):
            st['Doubling'] += 1; continue
        st['uncovered'] += 1
        if not has_solution(p, word):
            print('NO SOLUTION (counterexample candidate):', word)
            st['NO_SOLUTION'] += 1
        if shown < 15:
            shown += 1
            print('uncovered:', ' '.join(('r%d' % x if e == 1 else 's%d' % x) for x, e in word))
    print('p', p, dict(st))


if __name__ == '__main__':
    main()
