#!/usr/bin/env python3
"""Exact finite controls for the remaining N=46, t=26 residual-alphabet profiles.

Written from the mathematical normal form only; no earlier program is imported.
It checks
  1. the ten residual-alphabet profiles (sizes 2..5, every pair product >= 10);
  2. the balanced four-subsets of the binary 3-cube and their distance-one pairs;
  3. for every profile containing a 5, ALL labeled incidence triples over the five
     parity fibers of a size-5 party with every pair multiplicity in {0,2};
  4. the F2 ranks used by the written argument;
  5. the incidence-product multiplicity formula against directly built supports;
  6. the active-count arithmetic for the profile (3,4,4,4).
These are bounded exact controls, not a substitute for the written proof.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import itertools
import json
from pathlib import Path
import sys

N_RES = 10          # residual size n = 36 - t for t = 26
FIBERS = 5          # a size-5 residual party has five parity fibers
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
    out = []
    for p in itertools.combinations_with_replacement(range(2, 6), 4):
        if all(p[i] * p[j] >= N_RES for i, j in PAIRS4):
            out.append(p)
    return out


def cube_balanced_four_subsets():
    cube = list(itertools.product((0, 1), repeat=3))
    balanced, independent = [], []
    for S in itertools.combinations(cube, 4):
        if all(sum(q[i] for q in S) == 2 for i in range(3)):
            balanced.append(S)
            if all(sum(a != b for a, b in zip(x, y)) != 1 for x, y in itertools.combinations(S, 2)):
                independent.append(S)
    for S in independent:
        for i, j in itertools.combinations(range(3), 2):
            if len({(q[i], q[j]) for q in S}) != 4:
                raise CheckError('independent balanced subset without a full pair projection')
        if len({sum(q) % 2 for q in S}) != 1:
            raise CheckError('independent balanced subset is not a parity class')
    return balanced, independent


def incidence_family(r):
    """All 5 x r 0/1 matrices, rows of weight two, every column sum at least two."""
    rowmasks = [(1 << a) | (1 << b) for a, b in itertools.combinations(range(r), 2)]
    fam = []
    for rows in itertools.product(rowmasks, repeat=FIBERS):
        cols = tuple(sum(1 << g for g in range(FIBERS) if rows[g] >> s & 1) for s in range(r))
        if min(popcount(c) for c in cols) < 2:
            continue
        compat = 0
        for gamma in range(1, 1 << FIBERS):
            if all(popcount(gamma & c) in (0, 2) for c in cols):
                compat |= 1 << gamma
        colset = 0
        for c in cols:
            colset |= 1 << c
        fam.append({'rows': rows, 'cols': cols, 'colset': colset, 'compat': compat,
                    'degrees': tuple(sorted(popcount(c) for c in cols)),
                    'rank': f2_rank(rows)})
    return fam


def group_by_colset(fam):
    groups = defaultdict(list)
    for idx, u in enumerate(fam):
        groups[u['colset']].append(idx)
    return groups


def compatible(u, v):
    return (v['colset'] & ~u['compat']) == 0


def count_triples(fB, fC, fD, use_cd=True):
    gC, gD = group_by_colset(fC), group_by_colset(fD)
    pair_bc = triples = 0
    example = None
    for iB, uB in enumerate(fB):
        for sC, idxC in gC.items():
            if sC & ~uB['compat']:
                continue
            pair_bc += len(idxC)
            for iC in idxC:
                uC = fC[iC]
                allowed = uB['compat'] & (uC['compat'] if use_cd else -1)
                for sD, idxD in gD.items():
                    if (sD & ~allowed) == 0:
                        triples += len(idxD)
                        if example is None:
                            example = (iB, iC, idxD[0])
    return pair_bc, triples, example


def build_support(uB, uC, uD, parities):
    words = []
    for g in range(FIBERS):
        sets = []
        for u in (uB, uC, uD):
            sets.append(sorted(s for s in range(16) if u['rows'][g] >> s & 1))
        for i, j, k in itertools.product(range(2), repeat=3):
            if (i + j + k) % 2 == parities[g]:
                words.append((g, sets[0][i], sets[1][j], sets[2][k]))
    return words


def direct_cross_check(families, seed, samples):
    state = seed
    def rnd(m):
        nonlocal state
        state = (1103515245 * state + 12345) % (1 << 31)
        return state % m
    checked = 0
    for _ in range(samples):
        r = [rnd(4) + 2 for _ in range(3)]
        us = [families[x][rnd(len(families[x]))] for x in r]
        par = [rnd(2) for _ in range(FIBERS)]
        words = build_support(us[0], us[1], us[2], par)
        if len(words) != 20 or len(set(words)) != 20:
            raise CheckError('constructed support has wrong size')
        for x, y in itertools.combinations(words, 2):
            if x[0] == y[0] and sum(a != b for a, b in zip(x, y)) == 1:
                raise CheckError('parity fiber contains a distance-one pair')
        for (i, j) in PAIRS4:
            cnt = Counter((w[i], w[j]) for w in words)
            if i == 0:
                if set(cnt.values()) != {2}:
                    raise CheckError('A-pair multiplicity is not two')
                continue
            ui, uj = us[i - 1], us[j - 1]
            for (a, b), m in cnt.items():
                if m != popcount(ui['cols'][a] & uj['cols'][b]):
                    raise CheckError('multiplicity formula mismatch')
            for a in range(len(ui['cols'])):
                for b in range(len(uj['cols'])):
                    if popcount(ui['cols'][a] & uj['cols'][b]) != cnt.get((a, b), 0):
                        raise CheckError('multiplicity formula mismatch (zero cells)')
        checked += 1
    return checked


def active_count_3444():
    r = (3, 4, 4, 4)
    single = sum(6 * x - N_RES for x in r)
    pair = sum(r[i] * r[j] - N_RES for i, j in PAIRS4)
    sols = []
    for n4 in range(27):
        for n3 in range(27):
            for n2 in range(27):
                n1 = single - 2 * n2 - 3 * n3 - 4 * n4
                n0 = 26 - n1 - n2 - n3 - n4
                if min(n0, n1) < 0:
                    continue
                if n2 + 3 * n3 + 6 * n4 == pair:
                    sols.append((n0, n1, n2, n3, n4))
    if sols != [(0, 2, 24, 0, 0)]:
        raise CheckError(f'unexpected 3444 active-count solutions {sols}')
    size4_active = 6 * 4 - N_RES
    size4_pairs = (4 * 3 - N_RES) + 2 * (4 * 4 - N_RES)
    if size4_active != size4_pairs:
        raise CheckError('size-4 singleton count is not zero')
    # per-symbol singleton count (6-d) - sum_j (r_j - d) = 2d - 5 at a size-4 party
    per_symbol = {d: (6 - d) - ((3 - d) + 2 * (4 - d)) for d in range(2, 4)}
    if any(v == 0 for v in per_symbol.values()) or any(v != 2 * d - 5 for d, v in per_symbol.items()):
        raise CheckError('per-symbol singleton formula')
    return {'active_incidences': single, 'pair_incidences': pair, 'slack': 26 - (single - pair),
            'activity_vector_solutions': sols, 'size4_party_active_words': size4_active,
            'size4_party_pair_active_words': size4_pairs, 'size4_singletons': 0,
            'per_symbol_singleton_count_by_degree': per_symbol}


def allowed_degrees(profile):
    out = {}
    for i, r in enumerate(profile):
        cap = min(profile[j] for j in range(4) if j != i)
        out[str(i)] = [list(d) for d in itertools.combinations_with_replacement(range(2, cap + 1), r) if sum(d) == N_RES]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('out', type=Path)
    args = ap.parse_args()
    if args.out.exists():
        raise SystemExit('refusing to overwrite existing output')
    profs = profiles()
    expected = [(2, 5, 5, 5), (3, 4, 4, 4), (3, 4, 4, 5), (3, 4, 5, 5), (3, 5, 5, 5),
                (4, 4, 4, 4), (4, 4, 4, 5), (4, 4, 5, 5), (4, 5, 5, 5), (5, 5, 5, 5)]
    if profs != expected:
        raise CheckError('profile list mismatch')
    balanced, independent = cube_balanced_four_subsets()
    if len(balanced) != 8 or len(independent) != 2:
        raise CheckError('balanced cube subset counts')
    fam = {r: incidence_family(r) for r in (2, 3, 4, 5)}
    fam_summary = {}
    for r, F in fam.items():
        fam_summary[str(r)] = {'matrices': len(F),
            'degree_multisets': {','.join(map(str, k)): v for k, v in sorted(Counter(u['degrees'] for u in F).items())},
            'rank_histogram': {str(k): v for k, v in sorted(Counter(u['rank'] for u in F).items())}}
    # rank claims used in the written proof
    if {u['rank'] for u in fam[5]} != {3, 4} or any(u['degrees'] != (2, 2, 2, 2, 2) for u in fam[5]):
        raise CheckError('size-5 incidence claim')
    for u in fam[4]:
        if u['degrees'] == (2, 2, 2, 4) and u['rank'] != 3:
            raise CheckError('type X rank is not 3')
        if u['degrees'] == (2, 2, 3, 3) and u['rank'] not in (2, 3):
            raise CheckError('type Y rank')
        if u['degrees'] == (2, 2, 3, 3) and u['rank'] == 2:
            if (1 << FIBERS) - 1 not in {a ^ b for a, b in itertools.combinations(u['cols'], 2)}:
                raise CheckError('rank-two Y column space lacks all-ones')
    results = {}
    for p in expected:
        if 5 not in p:
            continue
        others = list(p)
        others.remove(5)
        others.sort()
        fB, fC, fD = (fam[x] for x in others)
        pair_bc, triples, example = count_triples(fB, fC, fD)
        relax_pair, relax_triples, relax_example = count_triples(fB, fC, fD, use_cd=False)
        if triples != 0:
            raise CheckError(f'unexpected surviving triple for profile {p}')
        rec = {'A_size': 5, 'other_sizes': others, 'compatible_BC_pairs': pair_bc,
               'all_three_pair_conditions_triples': triples,
               'control_without_CD_condition_triples': relax_triples}
        if relax_example is not None:
            iB, iC, iD = relax_example
            words = build_support(fB[iB], fC[iC], fD[iD], [0] * FIBERS)
            cd = Counter((w[2], w[3]) for w in words)
            rec['control_example_CD_multiplicities'] = dict(sorted(Counter(cd.values()).items()))
        results[','.join(map(str, p))] = rec
    checked = direct_cross_check(fam, seed=20261029, samples=3000)
    result = {
        'residual_size': N_RES, 'profiles': [list(p) for p in profs],
        'allowed_degree_multisets_by_profile': {','.join(map(str, p)): allowed_degrees(p) for p in profs},
        'binary_cube_balanced_four_subsets': len(balanced), 'distance_one_free_balanced_subsets': len(independent),
        'incidence_families': fam_summary, 'size5_profile_results': results,
        'direct_support_cross_checks': checked, 'profile_3444_active_count': active_count_3444(),
        'scope': 'Exact bounded controls of the written normal form; no AME state, no proof certificate, no review.'}
    blob = json.dumps(result, indent=2, sort_keys=True) + '\n'
    with args.out.open('x', encoding='utf-8') as out:
        out.write(blob)
    print(json.dumps({k: v for k, v in result.items() if k in ('profiles', 'size5_profile_results',
          'direct_support_cross_checks', 'incidence_families', 'binary_cube_balanced_four_subsets',
          'distance_one_free_balanced_subsets')}, indent=2))
    print('receipt_sha256', hashlib.sha256(blob.encode()).hexdigest())


if __name__ == '__main__':
    try:
        main()
    except CheckError as exc:
        print('CHECK FAILED:', exc, file=sys.stderr)
        sys.exit(1)
