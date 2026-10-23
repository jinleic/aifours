#!/usr/bin/env python3
"""Control for the review finding on OlsonParity's Lemma H (review/olson-kbh-codex-review-v1.note.md,
item 1): replacing the empty/full-pattern conditions by min(A, B) <= kappa needs A, B <= 2p-1.
(1) The reviewer's word rho_1^10 sigma_0^8 at p = 5: the exact half-window form of ../hw.py (all
    patterns, including P = empty and P = [k]) declares it non-avoiding, the raw ordered-product DP
    finds an identity 2p-subword, while the simplified condition alone would accept it.
(2) The IL counterexample of ../mixdef/README.md Sec. 6 (p = 11): exact windows of P = empty and
    P = [k] (whose sums are phi = 0), to confirm that its stated empty-pattern avoidance is exact.
In-process only (no subprocesses)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from hw import windows, hw_avoids, dp_has, word_of  # noqa: E402


def contains0(lo, hi, p):
    return lo <= hi and (hi - lo + 1 >= p or (-lo) % p <= hi - lo)


def report(name, p, a, b, l, y):
    k = len(a); A, B = sum(a), sum(b); H = sum(x // 2 for x in l); kappa = p - 1 - H
    W = windows(a, b, l, p); full = (1 << k) - 1
    print(name)
    print('  p', p, 'k', k, 'A', A, 'B', B, 'H', H, 'kappa', kappa, 'N', A + B + sum(l),
          '| A, B <= 2p-1:', A <= 2 * p - 1 and B <= 2 * p - 1)
    print('  exact I(empty) =', W[0], 'contains 0 mod p:', contains0(*W[0], p))
    print('  exact I([k])   =', W[full], 'contains 0 mod p:', contains0(*W[full], p))
    print('  simplified condition min(A,B) <= kappa:', min(A, B) <= kappa)
    print('  exact HW avoids (all patterns):', hw_avoids(a, b, l, y, p))
    print('  raw DP finds identity 2p-subword:', dp_has(word_of(a, b, l, y, p), p))


report('(1) reviewer word rho_1^10 sigma_0^8', 5, [10], [0], [8], [0])
p = 11
a = [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1]
b = [1 - x for x in a]
l = [1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1]
phi = [1, 1, 1, 1, 1, 1, 0, 4, 5, 1, 1, 4, 5, 1, 4, 7, 1, 4, 1]
y = []; prev = 0
for t in range(len(a)):
    prev = (prev - 2 * phi[t]) % p; y.append(prev)
report('(2) IL counterexample (mixdef/README.md Sec. 6)', p, a, b, l, y)
