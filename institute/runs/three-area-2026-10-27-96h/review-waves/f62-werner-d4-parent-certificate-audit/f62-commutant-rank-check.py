#!/usr/bin/env python3
"""f62 reviewer: independent re-derivation of the finite commutant witness used to replace the
Schur-Weyl import at the local dimensions n=2 (auxiliary qubit) and n=4 (site) on four replicas.
Own construction of the torus-weight unknowns and of ALL commutator rows (R) for every ordered pair
(i,j), own sparse modular elimination (prime 999983, different from the owner's 65521), exact rank of
the 24 permutation columns over Z (python-flint fmpz_mat.rank), and a check that every constraint row
annihilates every permutation column. Conclusion logic: dim ker_C K <= N - rank_Fp K; span{V_p}
(dimension rank_Q P) is inside the U(n) commutant, which is inside ker_C K; equality of the two numbers
forces commutant = span{V_p}. Writes only into this review directory."""
import itertools, json, sys, time
from pathlib import Path
sys.dont_write_bytecode = True
OWN = Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart')
sys.path.insert(0, str(OWN / 'frontier-20261028-python-deps'))
import flint
OUT = Path(__file__).resolve().parent / 'f62-commutant-rank-check-results.json'
PERMS = list(itertools.permutations(range(4)))
PRIME = 999983


def is_prime(n):
    return n > 1 and all(n % q for q in range(2, int(n ** 0.5) + 1))


def weight(x, n):
    w = [0] * n
    for v in x: w[v] += 1
    return tuple(w)


def analyse(n, p, drop_pair=None, drop_index=None):
    t0 = time.monotonic()
    basis = list(itertools.product(range(n), repeat=4))
    byw = {}
    for x in basis: byw.setdefault(weight(x, n), []).append(x)
    unknowns = {}
    for xs in byw.values():
        for x in xs:
            for y in xs: unknowns[(x, y)] = len(unknowns)
    N = len(unknowns)
    cols = list(unknowns)
    Pflat = [int(all(x[q[j]] == y[j] for j in range(4))) for (x, y) in cols for q in PERMS]
    rankP = flint.fmpz_mat(N, 24, Pflat).rank()
    Prows = {unknowns[k]: [int(all(k[0][q[j]] == k[1][j] for j in range(4))) for q in PERMS] for k in cols}
    pivots, rank, nrows, violations = {}, 0, 0, 0
    for i in range(n):
        for j in range(n):
            if i == j or (i, j) == drop_pair or drop_index in (i, j): continue
            for y in basis:
                if j not in y: continue
                wx = list(weight(y, n)); wx[i] += 1; wx[j] -= 1
                for x in byw.get(tuple(wx), []):
                    row = {}
                    for t in range(4):
                        if y[t] == j:
                            c = unknowns[(x, y[:t] + (i,) + y[t + 1:])]; row[c] = (row.get(c, 0) + 1) % p
                        if x[t] == i:
                            c = unknowns[(x[:t] + (j,) + x[t + 1:], y)]; row[c] = (row.get(c, 0) - 1) % p
                    row = {c: v for c, v in row.items() if v}
                    nrows += 1
                    for q in range(24):
                        if sum(v * Prows[c][q] for c, v in row.items()) % p: violations += 1
                    while row:
                        c = min(row)
                        if c in pivots:
                            f = row[c]
                            for cc, vv in pivots[c].items():
                                nv = (row.get(cc, 0) - f * vv) % p
                                if nv: row[cc] = nv
                                else: row.pop(cc, None)
                        else:
                            inv = pow(row[c], -1, p)
                            pivots[c] = {cc: vv * inv % p for cc, vv in row.items()}; rank += 1
                            break
    return {'n': n, 'full_dimension': n ** 4, 'same_weight_unknowns_N': N, 'constraint_rows': nrows,
            'rank_mod_p_of_constraints': rank, 'kernel_dimension_upper_bound': N - rank,
            'rank_over_Z_of_24_permutation_columns': int(rankP),
            'rows_annihilate_permutation_columns': violations == 0,
            'commutant_equals_permutation_span': (N - rank) == int(rankP),
            'seconds': round(time.monotonic() - t0, 3)}


def main():
    t0 = time.monotonic()
    if not is_prime(PRIME): raise ValueError('prime')
    res = {'kind': 'f62_independent_four_replica_commutant_rank_witness', 'prime': PRIME,
           'results': {str(n): analyse(n, PRIME) for n in (2, 4)}}
    # control (in memory): drop every row of the ordered pair (0,1); the constraint rank must fall and the
    # kernel bound must then exceed the permutation rank, so the equality test must fail.
    ctl = {str(n): analyse(n, PRIME, drop_pair=(0, 1)) for n in (2, 4)}
    res['control_drop_pair_01'] = {k: {'rank_mod_p_of_constraints': v['rank_mod_p_of_constraints'],
                                       'kernel_dimension_upper_bound': v['kernel_dimension_upper_bound'],
                                       'commutant_equals_permutation_span': v['commutant_equals_permutation_span']} for k, v in ctl.items()}
    res['control_drop_pair_01_note'] = ('Did NOT reduce the rank: expected mathematically, because E_01 = [E_02, E_21] for n=4 and, for n=2, '
                                        'commuting with the weight operator and E_10 already forces commuting with E_01 on a finite-dimensional '
                                        'sl2-module. Recorded as an informative non-firing control, not as a defect.')
    res['control_drop_pair_01_reduced_rank'] = any(v['commutant_equals_permutation_span'] is False for v in ctl.values())
    # genuinely weakening control: drop every pair touching index 0 (constraints then only express U(1)xU(n-1)
    # invariance), so the kernel bound must exceed the permutation rank and the equality test must fail.
    ctl2 = {str(n): analyse(n, PRIME, drop_index=0) for n in (2, 4)}
    res['control_drop_all_pairs_with_index_0'] = {k: {'rank_mod_p_of_constraints': v['rank_mod_p_of_constraints'],
                                                      'kernel_dimension_upper_bound': v['kernel_dimension_upper_bound'],
                                                      'commutant_equals_permutation_span': v['commutant_equals_permutation_span']} for k, v in ctl2.items()}
    res['control_behaved'] = all(not v['commutant_equals_permutation_span'] for v in ctl2.values())
    res['flint_version'] = flint.__version__
    res['elapsed_seconds'] = round(time.monotonic() - t0, 3)
    ok = all(r['commutant_equals_permutation_span'] and r['rows_annihilate_permutation_columns'] for r in res['results'].values()) and res['control_behaved']
    res['scope'] = ('Finite replacement of the Schur-Weyl import for n in {2,4}, k=4 replicas: unitary commutant equals span of the 24 '
                    'permutation operators, conditional on this exact finite computation and the elementary torus/derivative argument. '
                    'No statement for other n.')
    res['verdict'] = 'PASS' if ok else 'FAIL'
    OUT.write_text(json.dumps(res, indent=2, sort_keys=True) + '\n')
    print(json.dumps(res, indent=2, sort_keys=True))
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
