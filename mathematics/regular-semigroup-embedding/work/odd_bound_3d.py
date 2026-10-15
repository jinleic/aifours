"""Bound on the number of odd elements in a Z2-graded E-unitary orthodox extension of a band E.

For S E-unitary orthodox with S/sigma = Z2: sigma is injective on H-classes (Lemma 1), so each
H-class has at most one odd element, and m <= #H-classes of S.  D_S-related idempotents e, f have
isomorphic local submonoids eEe ~ fEf (x -> a'xa).  Hence D_E-classes whose local submonoids are
non-isomorphic lie in different D_S-classes, and
   m <= sum over groups of D_E-classes with isomorphic local submonoids of (sum rows)(sum cols).
If every group is a single D_E-class this is |E|, so enumerating m <= |E| is exhaustive.

Usage: python3 work/odd_bound_3d.py bands.json
"""
from __future__ import annotations

import itertools
import json
import sys


def dclasses(T):
    n = len(T)
    seen, cls = set(), []
    for a in range(n):
        if a in seen:
            continue
        c = [b for b in range(n) if T[T[a][b]][a] == a and T[T[b][a]][b] == b]
        cls.append(c)
        seen.update(c)
    return cls


def iso_type(T, els):
    n = len(els)
    best = None
    for p in itertools.permutations(range(n)):
        idx = {els[i]: p[i] for i in range(n)}
        U = [[0] * n for _ in range(n)]
        for a in els:
            for b in els:
                U[idx[a]][idx[b]] = idx[T[a][b]]
        key = tuple(map(tuple, U))
        if best is None or key < best:
            best = key
    return best


def main() -> None:
    bands = json.load(open(sys.argv[1]))
    for k, T in enumerate(bands):
        groups = {}
        for c in dclasses(T):
            r = len({frozenset(f for f in c if T[e][f] == f and T[f][e] == e) for e in c})
            l = len({frozenset(f for f in c if T[e][f] == e and T[f][e] == f) for e in c})
            t = iso_type(T, sorted({T[T[c[0]][x]][c[0]] for x in range(len(T))}))
            groups.setdefault(t, []).append((r, l))
        bound = sum(sum(r for r, _ in g) * sum(l for _, l in g) for g in groups.values())
        print(f"band {k}: |E|={len(T)}, D-classes (rows,cols) grouped by local-submonoid type "
              f"{list(groups.values())}, odd-element bound m <= {bound}")


if __name__ == "__main__":
    main()
