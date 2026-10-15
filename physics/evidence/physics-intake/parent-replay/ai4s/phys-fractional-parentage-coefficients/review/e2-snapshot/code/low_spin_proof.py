"""Universal derivation of E2 squared CFPs, without interpolation or large-v tables.

Spin 2, seniority v, multiplicity-free parent L <= 5. W[(L,lambda)][J]
means the sum of |r(v,L;v-1,alpha',J)|^2 over the daughter block. lambda
fixes v modulo 3. All formulas are derived in Q(v) from:
  sum_J W_J = 1,
  sum_J J(J+1) W_J = 6 + (v-2)L(L+1)/v,
  harmonic principal-parent projection into a unique (v,L) block:
    W_J = [1+(v-1) sum_K A(L,J,K) W_d(K)
             - 2(v-1)(2J+1) W_d(L)/((2v+1)(2L+1))]/v.
A is the finite four-CG exchange contraction below; W_d is an already
derived daughter row at seniority v-1. No fitted or conjectured expressions
are used in derive(). compare_registered() imports the old formulas only
AFTER the independent derivation is complete.

Run from this folder: $PY code/low_spin_proof.py
Proof and boundary cases: RESULTS.md, section I.
"""
from functools import cache
import json
from pathlib import Path

import sympy as sp
from sympy.physics.wigner import clebsch_gordan

v = sp.Symbol('v', positive=True)


@cache
def cg(a, b, c, ma, mb, mc):
    if ma + mb != mc or abs(ma) > a or abs(mb) > b or abs(mc) > c:
        return sp.S.Zero
    if not abs(a-b) <= c <= a+b:
        return sp.S.Zero
    return clebsch_gordan(a, b, c, ma, mb, mc)


@cache
def exchange(L, J, K):
    """< [particle 1 x (particle 2 x spin K)_J]_L | swap12 | same >.

    M=L, daughter projections M_m=L-m. Insert an orthonormal degree-(v-2)
    basis of spin K in <d,J,M_m|a_n^dagger a_m|d,J,M_n>.
    All spins here are fixed integers independent of v.
    """
    total = sp.S.Zero
    for m in range(-2, 3):
        for n in range(-2, 3):
            q = L-m-n
            total += (cg(2, J, L, m, L-m, L)
                      * cg(2, J, L, n, L-n, L)
                      * cg(2, K, J, n, q, L-m)
                      * cg(2, K, J, m, q, L-n))
    total = sp.simplify(total)
    assert total.is_Rational, (L, J, K, total)
    return total


def principal_weight(L, J, daughter):
    """Harmonic projection identity. daughter: block weights at degree v-1."""
    create_norm = 1+(v-1)*sum(exchange(L, J, K)*w for K, w in daughter.items())
    trace_norm = ((v-1)*sp.Rational(2*J+1, 2*L+1)*daughter.get(L, sp.S.Zero))
    return sp.factor((create_norm-2*trace_norm/(2*v+1))/v)


def moments(L, spins, anchors):
    """Solve the two sum rules for exactly two remaining daughter-block weights."""
    unknown = [J for J in spins if J not in anchors]
    assert len(unknown) == 2, (L, spins, anchors)
    a, b = unknown
    A, B = a*(a+1), b*(b+1)
    mass = 1-sum(anchors.values())
    moment = 6+(v-2)*L*(L+1)/v-sum(J*(J+1)*x for J, x in anchors.items())
    out = dict(anchors)
    out[a] = sp.factor((B*mass-moment)/(B-A))
    out[b] = sp.factor((moment-A*mass)/(B-A))
    assert sp.cancel(sum(out.values())-1) == 0
    assert sp.cancel(sum(J*(J+1)*x for J, x in out.items())-6-(v-2)*L*(L+1)/v) == 0
    return dict(sorted(out.items()))


def derive():
    """Acyclic universal construction; no registered formulas or finite tables used."""
    W = {(0, 0): {2: sp.S.One}}
    ledger = [{'parent': [0, 0], 'anchors': [], 'method': 'single allowed daughter J=2'}]

    def add(L, lam, spins, parents):
        anchors = {}
        dependencies = []
        for J, daughter_lam in parents:
            key = (J, daughter_lam)
            assert key in W, ('unproved dependency', key)
            assert (lam-1-daughter_lam) % 3 == 0, ('wrong residue', L, lam, key)
            daughter = {K: w.subs(v, v-1) for K, w in W[key].items()}
            anchors[J] = principal_weight(L, J, daughter)
            dependencies.append({'daughter': list(key), 'weight': str(anchors[J]),
                                 'exchange': {str(K): str(exchange(L, J, K)) for K in daughter}})
        W[(L, lam)] = moments(L, spins, anchors)
        ledger.append({'parent': [L, lam], 'anchors': dependencies,
                       'remaining': [J for J in spins if J not in anchors],
                       'method': 'principal-parent anchors plus two moment equations'})

    add(2, 1, [0, 3, 4], [(0, 0)])
    add(2, 2, [2, 4], [])
    add(3, 3, [2, 4, 5], [(2, 2)])
    add(4, 4, [3, 4, 6], [(3, 3)])
    add(4, 2, [2, 4, 5, 6], [(2, 1), (4, 4)])
    add(4, 3, [2, 4, 5, 6], [(2, 2), (4, 2)])
    add(5, 4, [3, 4, 6, 7], [(3, 3), (4, 3)])
    add(5, 5, [4, 5, 6, 7], [(4, 4), (5, 4)])
    return W, ledger


def compare_registered(W):
    from verify_bottom_conjectures import CONJ, BLOCK, v as old_v
    count = 0
    for (L, lam, J, daughter_lam), (expected, _) in CONJ.items():
        assert (lam-1-daughter_lam) % 3 == 0
        actual = W[(L, lam)][J]
        assert sp.cancel(actual-expected.subs(old_v, v)) == 0, (L, lam, J, actual, expected)
        count += 1
    expected_blocks = {(4, 4, 6): BLOCK[(4, 4, 6)].subs(old_v, v),
                       (5, 4, 6): 4*(92*v**2-92*v-285)/(385*v*(2*v+1))}
    for (L, lam, J), expected in expected_blocks.items():
        assert sp.cancel(W[(L, lam)][J]-expected) == 0, (L, lam, J)
    return count, len(expected_blocks)


def main():
    W, ledger = derive()
    nc, nb = compare_registered(W)
    for key, weights in W.items():
        print(f'(L,lambda)={key}: ' + ', '.join(f'J={J}: {w}' for J, w in weights.items()))
    print(f'UNIVERSAL IDENTITIES: {nc}/26 product formulas + {nb}/2 block weights derived exactly in Q(v).')
    print('Dependency order: 0 -> 2/1 -> 2/2 -> 3/3 -> 4/4 -> 4/2 -> 4/3 -> 5/4 -> 5/5.')
    print('No interpolation, no finite-v data used in derive(); signs not asserted by this squared-weight proof.')
    report = {'method': 'acyclic harmonic projection and angular-momentum moments',
              'uses_finite_data_in_derivation': False, 'product_identities': nc, 'block_identities': nb,
              'signed_coefficients_proved': False, 'dependency_ledger': ledger,
              'weights': {f'{L},{lam}': {str(J): str(w) for J, w in weights.items()}
                          for (L, lam), weights in W.items()}}
    path = Path(__file__).resolve().parents[1]/'results'/'low_spin_universal_derivation.json'
    path.write_text(json.dumps(report, indent=2)+'\n')


if __name__ == '__main__':
    main()
