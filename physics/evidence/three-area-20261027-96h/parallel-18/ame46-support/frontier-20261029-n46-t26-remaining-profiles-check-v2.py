#!/usr/bin/env python3
"""Exact finite controls for the remaining N=46, t=26 residual-alphabet profiles (v2).

Supersedes v1 only by adding per-pair compatibility counts and a second,
independently coded triple count by integer matrix products (numpy int64).
Written from the mathematical normal form; no earlier program is imported.
Bounded exact controls only; not a substitute for the written proof.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import itertools
import json
from pathlib import Path
import sys

import numpy as np

N_RES = 10
FIBERS = 5
PAIRS4 = list(itertools.combinations(range(4), 2))


class CheckError(ValueError):
    pass


def popcount(x):
    return bin(x).count('1')


def f2_rank(rows):
    basis = {}
    for v in rows:
        while v:
            h = v.bit_length() - 1
            if h not in basis:
                basis[h] = v
                break
            v ^= basis[h]
    return len(basis)


def profiles():
    return [p for p in itertools.combinations_with_replacement(range(2, 6), 4)
            if all(p[i] * p[j] >= N_RES for i, j in PAIRS4)]


def cube_subsets():
    cube = list(itertools.product((0, 1), repeat=3))
    bal = [S for S in itertools.combinations(cube, 4) if all(sum(q[i] for q in S) == 2 for i in range(3))]
    ind = [S for S in bal if all(sum(a != b for a, b in zip(x, y)) != 1 for x, y in itertools.combinations(S, 2))]
    for S in ind:
        if len({sum(q) % 2 for q in S}) != 1:
            raise CheckError('distance-one-free balanced subset is not a parity class')
        for i, j in itertools.combinations(range(3), 2):
            if len({(q[i], q[j]) for q in S}) != 4:
                raise CheckError('parity class without full pair projection')
    return len(bal), len(ind)


def family(r):
    pairs = list(itertools.combinations(range(r), 2))
    out = []
    for rows in itertools.product(pairs, repeat=FIBERS):
        M = np.zeros((FIBERS, r), dtype=np.int64)
        for g, (a, b) in enumerate(rows):
            M[g, a] = M[g, b] = 1
        if M.sum(axis=0).min() < 2:
            continue
        cols = tuple(int(sum(int(M[g, s]) << g for g in range(FIBERS))) for s in range(r))
        compat = 0
        for gamma in range(1, 1 << FIBERS):
            if all(popcount(gamma & c) in (0, 2) for c in cols):
                compat |= 1 << gamma
        colset = 0
        for c in cols:
            colset |= 1 << c
        rowbits = tuple((1 << a) | (1 << b) for a, b in rows)
        out.append({'M': M, 'cols': cols, 'compat': compat, 'colset': colset,
                    'deg': tuple(sorted(int(x) for x in M.sum(axis=0))), 'rank': f2_rank(rowbits)})
    return out


def mask_pairs(fj, fk):
    groups = defaultdict(list)
    for idx, u in enumerate(fk):
        groups[u['colset']].append(idx)
    pairs = []
    for i, u in enumerate(fj):
        for s, idxs in groups.items():
            if s & ~u['compat'] == 0:
                pairs.extend((i, k) for k in idxs)
    return pairs


def matmul_pairs(fj, fk):
    # Stack all matrices; integer products U_j^T U_k must have every entry in {0,2}.
    pairs = []
    Mk = np.stack([u['M'] for u in fk])              # (K, 5, rk)
    for i, u in enumerate(fj):
        P = np.einsum('gb,kgc->kbc', u['M'], Mk)      # (K, rj, rk)
        ok = np.all((P == 0) | (P == 2), axis=(1, 2))
        pairs.extend((i, int(k)) for k in np.nonzero(ok)[0])
    return pairs


def triples_from_pairs(pBC, pBD, pCD):
    bd = defaultdict(set)
    for b, d in pBD:
        bd[b].add(d)
    cd = defaultdict(set)
    for c, d in pCD:
        cd[c].add(d)
    total = 0
    for b, c in pBC:
        total += len(bd[b] & cd[c])
    return total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('out', type=Path)
    args = ap.parse_args()
    if args.out.exists():
        raise SystemExit('refusing to overwrite existing output')
    profs = profiles()
    if len(profs) != 10:
        raise CheckError('profile count')
    nbal, nind = cube_subsets()
    if (nbal, nind) != (8, 2):
        raise CheckError('cube subset counts')
    fam = {r: family(r) for r in (2, 3, 4, 5)}
    if [len(fam[r]) for r in (2, 3, 4, 5)] != [1, 210, 2580, 2040]:
        raise CheckError('family sizes')
    for u in fam[5]:
        if u['deg'] != (2, 2, 2, 2, 2) or u['rank'] not in (3, 4):
            raise CheckError('size-5 family claim')
    for u in fam[4]:
        if u['deg'] == (2, 2, 2, 4) and u['rank'] != 3:
            raise CheckError('X rank')
        if u['deg'] == (2, 2, 3, 3) and u['rank'] == 2 and (1 << FIBERS) - 1 not in {a ^ b for a, b in itertools.combinations(u['cols'], 2)}:
            raise CheckError('rank-2 Y without all-ones in column span')
    out = {}
    for p in profs:
        if 5 not in p:
            continue
        o = sorted(list(p[:p.index(5)] + p[p.index(5) + 1:]))
        fB, fC, fD = (fam[x] for x in o)
        rec = {'other_sizes': o}
        res = {}
        for name, (fx, fy) in {'BC': (fB, fC), 'BD': (fB, fD), 'CD': (fC, fD)}.items():
            a = sorted(mask_pairs(fx, fy))
            b = sorted(matmul_pairs(fx, fy))
            if a != b:
                raise CheckError(f'method disagreement on {p} {name}')
            res[name] = a
            rec[f'compatible_{name}_pairs'] = len(a)
        tri = triples_from_pairs(res['BC'], res['BD'], res['CD'])
        if tri != 0:
            raise CheckError(f'surviving triple for {p}')
        rec['triples_all_three_conditions'] = tri
        out[','.join(map(str, p))] = rec
    result = {'profiles': [list(p) for p in profs], 'binary_cube_balanced_four_subsets': nbal,
              'distance_one_free_balanced_subsets': nind,
              'family_sizes': {str(r): len(fam[r]) for r in fam},
              'family_rank_histograms': {str(r): {str(k): v for k, v in sorted(Counter(u['rank'] for u in fam[r]).items())} for r in fam},
              'family_degree_multisets': {str(r): {','.join(map(str, k)): v for k, v in sorted(Counter(u['deg'] for u in fam[r]).items())} for r in fam},
              'size5_profiles': out,
              'methods': 'compatible-column bitmask test and numpy integer U_j^T U_k products; required to agree pair by pair',
              'scope': 'Exact bounded controls of the written normal form; no AME state, proof certificate or review.'}
    blob = json.dumps(result, indent=2, sort_keys=True) + '\n'
    with args.out.open('x', encoding='utf-8') as f:
        f.write(blob)
    print(json.dumps(out, indent=2))
    print('receipt_sha256', hashlib.sha256(blob.encode()).hexdigest())


if __name__ == '__main__':
    try:
        main()
    except CheckError as exc:
        print('CHECK FAILED:', exc, file=sys.stderr)
        sys.exit(1)
