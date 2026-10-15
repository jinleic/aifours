"""Changed-path replay of the universal E2 proof, with independent kernels.

The new derivation uses four Clebsch-Gordan coefficients. This verifier uses
a factorial Racah sum with fractions.Fraction, no sympy Wigner/CG calls,
for (2J+1){K 2 J; L 2 J}. It checks the old candidate formulas against
all anchor identities and the two moment equations as identities in Q(v).
It also checks physical branching/minimal-v boundaries against the existing
Fock engine (only v <= 7), and reuses the existing v <= 88 evidence, without
extending it. Three deliberately wrong kernels/formulas must be rejected.
Run: $PY code/verify_low_spin_proof.py [--no-write]
"""
from collections import defaultdict
from fractions import Fraction
from math import factorial
import json
from pathlib import Path
import sys

import sympy as sp

from low_spin_proof import derive, exchange, v
from spin2_basis import Spin2, labels
from verify_bottom_conjectures import CONJ, BLOCK, v as registered_v


def triangle_square(a, b, c):
    if not abs(a-b) <= c <= a+b:
        return Fraction(0)
    return Fraction(factorial(a+b-c)*factorial(a-b+c)*factorial(-a+b+c),
                    factorial(a+b+c+1))


def racah_exchange(L, J, K):
    """(2J+1){K 2 J; L 2 J}, evaluated without a CG/Wigner library."""
    t1, t2 = triangle_square(K, 2, J), triangle_square(L, 2, J)
    if not t1 or not t2:
        return Fraction(0)
    a, b = K+2+J, L+2+J
    u, w, t = K+L+4, K+L+2*J, 4+2*J
    total = Fraction(0)
    for z in range(max(a, b), min(u, w, t)+1):
        den = factorial(z-a)**2*factorial(z-b)**2*factorial(u-z)*factorial(w-z)*factorial(t-z)
        total += Fraction((-1 if z % 2 else 1)*factorial(z+1), den)
    return (2*J+1)*t1*t2*total


def registered_weights():
    W = defaultdict(dict)
    for (L, lam, J, daughter_lam), (expr, _) in CONJ.items():
        assert (lam-1-daughter_lam) % 3 == 0
        assert J not in W[L, lam], ('not an individual daughter channel', L, lam, J)
        W[L, lam][J] = expr.subs(registered_v, v)
    W[4, 4][6] = BLOCK[4, 4, 6].subs(registered_v, v)
    W[5, 4][6] = 4*(92*v**2-92*v-285)/(385*v*(2*v+1))
    return dict(W)


def independent_anchor(L, J, row, projection_factor=2):
    daughter = {K: x.subs(v, v-1) for K, x in row.items()}
    norm = 1+(v-1)*sum(sp.Rational(racah_exchange(L, J, K))*x for K, x in daughter.items())
    trace = (v-1)*sp.Rational(2*J+1, 2*L+1)*daughter.get(L, 0)
    return sp.factor((norm-projection_factor*trace/(2*v+1))/v)


def main(write_output=True):
    candidate = registered_weights()
    derived, ledger = derive()
    kernel_set = set()
    anchor_count = 0
    for entry in ledger[1:]:
        L, lam = entry['parent']
        for anchor in entry['anchors']:
            J, daughter_lam = anchor['daughter']
            row = candidate[J, daughter_lam]
            for K in row:
                kernel_set.add((L, J, K))
                assert exchange(L, J, K) == sp.Rational(racah_exchange(L, J, K))
            assert sp.cancel(candidate[L, lam][J]-independent_anchor(L, J, row)) == 0
            anchor_count += 1
    for (L, lam), row in candidate.items():
        assert sp.cancel(sum(row.values())-1) == 0
        assert sp.cancel(sum(J*(J+1)*w for J, w in row.items())-6-(v-2)*L*(L+1)/v) == 0
        assert set(row) == set(derived[L, lam])
        assert all(sp.cancel(w-derived[L, lam][J]) == 0 for J, w in row.items())

    # Explicit low-v checks include the two exceptions to the generic anchor graph:
    # (v,L,lambda)=(1,2,1) has vacuum daughter only; (2,4,2) has J=2 only.
    S = Spin2()
    boundary_count = 0
    for n in range(1, 8):
        for (L, lam), row in candidate.items():
            if n < lam or (n-lam) % 3 or (L == 0 and n == 0):
                continue
            parents = S.orthogonal_basis(n, L)
            assert len(parents) == 1
            _, psi = parents[0]
            seen = {}
            for J in range(abs(L-2), L+3):
                total = sp.S.Zero
                for _, daughter in S.orthogonal_basis(n-1, J):
                    r2, _ = S.B.cfp_sq_sign(psi, n, L, daughter, J)
                    total += sp.Rational(int(r2.p), int(r2.q))
                seen[J] = total
            for J in set(row) | set(seen):
                expected = row.get(J, sp.S.Zero).subs(v, n)
                assert expected == seen.get(J, 0), (n, L, lam, J, expected, seen)
                if not labels(n-1, J):
                    assert expected == 0, ('absent daughter has nonzero weight', n, L, J)
                boundary_count += 1

    table_path = Path(__file__).resolve().parents[1]/'results'/'spin2_r_table_v88_L5.json'
    finite = defaultdict(lambda: sp.S.Zero)
    for r in json.loads(table_path.read_text())['rows']:
        finite[r['v'], r['L'], r['v']-3*r['e'], r['Lp']] += sp.Rational(r['r2'])
    for (n, L, lam, J), x in finite.items():
        assert candidate[L, lam][J].subs(v, n) == x

    # Falsification controls: each mutation must produce a nonzero rational-function residual.
    wrong_pair_trace = independent_anchor(2, 0, candidate[0, 0], projection_factor=0)
    assert sp.cancel(wrong_pair_trace-candidate[2, 1][0]) != 0
    wrong_normalization = independent_anchor(3, 2, candidate[2, 2])*v/(v-1)
    assert sp.cancel(wrong_normalization-candidate[3, 3][2]) != 0
    perturbed = dict(candidate[2, 2])
    perturbed[2] += 1/v
    perturbed[4] -= 1/v
    assert sp.cancel(sum(perturbed.values())-1) == 0
    assert sp.cancel(sum(J*(J+1)*x for J, x in perturbed.items())-6-(v-2)*6/v) != 0

    report = {'symbolic_anchor_identities': anchor_count,
              'independent_racah_kernel_checks': len(kernel_set),
              'symbolic_moment_identities': 2*len(candidate),
              'low_v_boundary_and_absent_channel_checks': boundary_count,
              'existing_v88_block_comparisons': len(finite),
              'negative_controls_detected': 3,
              'finite_data_used_in_universal_derivation': False,
              'verdict': 'all squared-weight identities passed; no universal sign claim'}
    print(json.dumps(report, indent=2))
    if write_output:
        out = table_path.parent/'low_spin_proof_replay.json'
        out.write_text(json.dumps(report, indent=2)+'\n')


if __name__ == '__main__':
    main(write_output='--no-write' not in sys.argv)
