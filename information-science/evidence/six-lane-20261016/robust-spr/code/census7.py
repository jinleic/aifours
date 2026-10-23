"""Regenerate the regular alternation configurations surviving the prior dossier's necessary
filters (multiplicity <= floor(n/2) contacts per corner; unwrapped phase/region order, Lemma L)
and list them explicitly with corners and denominator regions.  Bookkeeping only.

Conventions (prior dossier Lemma L): numerator quadrant index q_i in 0..n-1 (deg b = n,
b(0) != 0), orientation sigma_i = kappa_sign * (-1)^(m-i), m = n+1; the touching corner's actual
quadrant index is k_i = q_i - sigma_i; the corner selected in numerator quadrant q is
C_{q mod 4} with C_0 = '--', C_1 = '+-', C_2 = '++', C_3 = '-+'.  Denominator regions r in
0..2(n-1): even r = gap region where every corner has index r/2; odd r = band (r+1)/2 where a
corner has index (r-1)/2 or (r+1)/2.  Region indices must be nondecreasing along the nodes.
"""
from __future__ import annotations

import itertools
import json
import sys

CORNER = {0: '--', 1: '+-', 2: '++', 3: '-+'}


def lifted_regions(indices, n):
    r, regions = 0, []
    for index in indices:
        if not 0 <= index < n:
            return None
        while r <= 2 * (n - 1):
            allowed = {r // 2} if r % 2 == 0 else {(r - 1) // 2, (r + 1) // 2}
            if index in allowed:
                break
            r += 1
        if r > 2 * (n - 1):
            return None
        regions.append(r)
    return regions


def regular(n):
    m = n + 1
    out = []
    for sign in (1, -1):
        for seq in itertools.combinations_with_replacement(range(n), m):
            if max(sum(q % 4 == v for q in seq) for v in range(4)) > n // 2:
                continue
            sig = [sign * (-1) ** (m - i) for i in range(1, m + 1)]
            k = [q - s for q, s in zip(seq, sig)]
            reg = lifted_regions(k, n)
            if reg is None:
                continue
            out.append({'kappa': sign, 'q': list(seq), 'sigma': sig, 'k': k, 'regions': reg,
                        'corners': [CORNER[q % 4] for q in seq]})
    return out


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    rows = regular(n)
    print(len(rows))
    for r in rows:
        print(r['kappa'], ''.join(map(str, r['q'])), ' '.join(r['corners']), r['regions'])
    if len(sys.argv) > 2:
        json.dump(rows, open(sys.argv[2], 'w'), indent=0)
