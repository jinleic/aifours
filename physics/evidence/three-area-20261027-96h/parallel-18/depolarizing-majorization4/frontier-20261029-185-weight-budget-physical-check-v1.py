#!/usr/bin/env python3
"""Exact finite checks for the common-projector weighted Pauli bound.

The theorem is a written all-variable claim; this program checks only the one
specified physical input and one specified rank-three projector at two physical
channel parameters. Standard-library integer/Fraction arithmetic only.
"""
import itertools
import json
from fractions import Fraction as F

# psi=(3|0000>+|0011>+|0101>+|1110>)/sqrt(12).
AMPS = {0: 3, 3: 1, 5: 1, 14: 1}
QSET = {0, 3, 5}


def bit(x, i):
    return (x >> (3-i)) & 1


def pauli_rho(labels):
    """Exact real Pauli expectation in the normalized real pure input."""
    flip = sum(1 << (3-i) for i, a in enumerate(labels) if a in (1, 2))
    y_count = labels.count(2)
    raw = sum(
        amp * AMPS.get(x ^ flip, 0) * (-1)**sum(bit(x, i) for i, a in enumerate(labels) if a in (2, 3))
        for x, amp in AMPS.items()
    )
    if y_count % 2:
        assert raw == 0
        return F(0)
    return F((-1)**(y_count//2) * raw, 12)


def pauli_q(labels):
    if any(a in (1, 2) for a in labels):
        return F(0)
    return F(sum((-1)**sum(bit(x, i) for i, a in enumerate(labels) if a == 3) for x in QSET))


def channel_trace(s):
    # Diagonal expectation for Q: off-diagonal rho matrix units stay off-diagonal.
    a, b = (1+s)/2, (1-s)/2
    return sum(F(amp*amp, 12) * a**(4-(x ^ y).bit_count()) * b**((x ^ y).bit_count())
               for x in QSET for y, amp in AMPS.items())


def nonzero_minor(left):
    right = tuple(i for i in range(4) if i not in left)
    rows, cols = 2**len(left), 2**len(right)
    mat = [[0 for _ in range(cols)] for _ in range(rows)]
    for x, amp in AMPS.items():
        row = sum(bit(x, i) << (len(left)-1-j) for j, i in enumerate(left))
        col = sum(bit(x, i) << (len(right)-1-j) for j, i in enumerate(right))
        mat[row][col] = amp
    for a, b in itertools.combinations(range(rows), 2):
        for c, d in itertools.combinations(range(cols), 2):
            det = mat[a][c]*mat[b][d]-mat[a][d]*mat[b][c]
            if det:
                return {'rows': [a,b], 'cols': [c,d], 'det_unnormalized': det}
    raise AssertionError('Schmidt rank less than 2 across cut ' + str(left))


def main():
    assert sum(a*a for a in AMPS.values()) == 12
    assert len(QSET) == 3 and len(set(QSET)) == 3
    assert all((x ^ y).bit_count() != 1 for x, y in itertools.combinations(AMPS, 2))
    radii = [F(1)-2*sum(F(a*a,12)*bit(x,i) for x,a in AMPS.items()) for i in range(4)]
    assert radii == [F(5,6), F(2,3), F(2,3), F(2,3)]
    rsort = sorted(radii)
    S = sum(x*x for x in radii)
    L = rsort[0]+rsort[1]+3*rsort[2]+3*rsort[3]
    flip_overlap = sum(F(a * AMPS.get(x ^ 15,0) * (-1)**x.bit_count(),12) for x,a in AMPS.items())
    C = flip_overlap * flip_overlap
    A = [F(0)]*5
    Qweights = [F(0)]*5
    for labels in itertools.product(range(4), repeat=4):
        weight = sum(a != 0 for a in labels)
        ar, aq = pauli_rho(labels), pauli_q(labels)
        A[weight] += ar*ar
        Qweights[weight] += aq*aq
    assert A == [F(1),F(73,36),F(145,36),F(215,36),F(107,36)]
    assert Qweights == [F(9),F(12),F(6),F(12),F(9)]
    assert S == F(73,36) and L == F(35,6) and C == 0
    assert sum(Qweights) == 48 and sum(A) == 16
    cuts = [(0,),(1,),(2,),(3,),(0,1),(0,2),(0,3)]
    minors = {','.join(map(str,cut)): nonzero_minor(cut) for cut in cuts}
    t = F(1,3)
    H = A[2]+t*t*A[3]+t**4*A[4]
    assert H == F(13787,2916)
    cap = L*L/S
    x0 = 39*S/(S+t*t*H)
    assert 0 <= cap <= 20 and x0 > cap
    assert H*(39-cap) < 121
    ref = F(32,81)
    assert ref - F(37,96) == F(25,2592)
    assert 4*S+8*C > F(64,9)
    delta = 8-L
    d_failure = 39*(15-S)-(5+delta/t)**2
    assert d_failure == F(1121,3) and d_failure > 0
    purity_failure = 39*(S+t*t*H)-(8+6*t-t**3)**2
    assert purity_failure == F(680,2187) and purity_failure > 0
    assert S*Qweights[1] < 25 and H*(39-Qweights[1]) < 144
    rows = []
    for p in (F(2,3),F(4,3)):
        tr = channel_trace(1-p)
        expected = F(5,18) if p == F(2,3) else F(41,324)
        assert tr == expected and ref-tr > F(13,648)
        rows.append({'p': str(p), 'same_rho_same_Q_trace': str(tr),
                     'reference_top3': str(ref), 'exact_same_Q_gap': str(ref-tr)})
    print(json.dumps({
        'scope':'One explicit pure input and one diagonal physical rank-three Q; all-variable theorem requires the separate written proof',
        'state_amplitudes_unnormalized': {str(k):v for k,v in AMPS.items()},
        'Q_basis_decimal_indices':sorted(QSET),
        'radii':list(map(str,radii)), 'S':str(S), 'C':str(C), 'L':str(L),
        'pure_state_A_weights':list(map(str,A)), 'Q_weight_norms_squared':list(map(str,Qweights)),
        'all_7_cut_minors':minors, 'H_t':str(H), 'x_cap':str(cap), 'x0':str(x0),
        'global_bound_sqrt_121_slack':str(F(121)-H*(39-cap)),
        'D_class_failure_square_slack':str(d_failure), 'old_purity_certificate_failure':str(purity_failure),
        'actual_channels':rows
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
