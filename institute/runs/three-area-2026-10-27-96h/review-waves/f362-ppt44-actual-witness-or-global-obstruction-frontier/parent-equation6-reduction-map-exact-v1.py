#!/usr/bin/env python3
"""Exact finite check of a 2-positive/non-CP map against public Eq.(6).

All matrices are integer-scaled; the universal 2-positivity statement uses the
written rank-two trace inequality and the published SDP definition is a named
external source.  This is NOT a 4x4 PPT Schmidt-number-three witness and does
not itself prove any all-dimension SDP-collapse theorem. No file writes.
"""
from fractions import Fraction
import json
import sys


class Rejected(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise Rejected(reason)


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def outer_omega(n):
    v = [int(i // n == i % n) for i in range(n * n)]
    return [[x * y for y in v] for x in v]


def flip(n):
    return [[int(i // n == j % n and i % n == j // n)
             for j in range(n * n)] for i in range(n * n)]


def kron(a, b):
    return [[a[i][j] * b[k][l] for j in range(len(a[0]))
             for l in range(len(b[0]))] for i in range(len(a))
            for k in range(len(b))]


def add(*terms):
    n, m = len(terms[0][1]), len(terms[0][1][0])
    return [[sum(scale * matrix[i][j] for scale, matrix in terms)
             for j in range(m)] for i in range(n)]


def mul(a, b):
    n, m, k = len(a), len(b[0]), len(b)
    return [[sum(a[i][h] * b[h][j] for h in range(k))
             for j in range(m)] for i in range(n)]


def trace_product(a, b):
    return sum(a[i][j] * b[j][i]
               for i in range(len(a)) for j in range(len(a)))


def ix(a, b, aa, bb):
    return ((a * 4 + b) * 2 + aa) * 2 + bb


def partial_transpose(matrix, transpose_ancilla=True):
    out = [[0] * 64 for _ in range(64)]
    for a in range(4):
        for b in range(4):
            for aa in range(2):
                for bb in range(2):
                    for c in range(4):
                        for d in range(4):
                            for cc in range(2):
                                for dd in range(2):
                                    if transpose_ancilla:
                                        row, col = ix(c, b, cc, bb), ix(a, d, aa, dd)
                                    else:
                                        row, col = ix(c, b, aa, bb), ix(a, d, cc, dd)
                                    out[ix(a, b, aa, bb)][ix(c, d, cc, dd)] = matrix[row][col]
    return out


def symmetry(a):
    return all(a[i][j] == a[j][i] for i in range(len(a)) for j in range(len(a)))


def quad(a, vector):
    return sum(vector[i] * a[i][j] * vector[j]
               for i in range(len(a)) for j in range(len(a)))


def intended_failure(name, operation, wanted):
    try:
        operation()
    except Rejected as exc:
        require(str(exc) == wanted, 'unexpected_mutation_reason:' + name)
        return {'name': name, 'reason': str(exc)}
    raise Rejected('mutant_accepted:' + name)


def main():
    # AB and A'B' are grouped for construction; the SDP bipartition is AA'|BB'.
    i16, i4, i64 = eye(16), eye(4), eye(64)
    o4, o2, f4, f2 = outer_omega(4), outer_omega(2), flip(4), flip(2)
    require(mul(f4, f4) == i16 and mul(f2, f2) == i4, 'swap_not_involution')
    require(symmetry(f4) and symmetry(f2), 'swap_not_symmetric')

    # 8Q = O4 tensor O2 + 8I - 4 I tensor O2, where Q is the
    # UNNORMALIZED feasible operator; Tr(Q)=49.
    first = kron(o4, o2)
    filler = add((8, i64), (-4, kron(i16, o2)))
    q8 = add((1, first), (1, filler))
    require(symmetry(first) and symmetry(filler), 'not_hermitian')
    require(mul(first, first) == add((8, first)), 'first_not_scaled_projector')
    require(mul(filler, filler) == add((8, filler)), 'filler_not_scaled_projector')
    require(mul(first, filler) == [[0] * 64 for _ in range(64)],
            'summands_not_orthogonal')
    tr_q8 = sum(q8[i][i] for i in range(64))
    require(tr_q8 == 392, 'wrong_state_normalization')

    # Partial transpose acts on A and A' in AA'|BB', not on only one factor.
    qpt = partial_transpose(q8)
    expected_qpt = add((8, i64), (-4, kron(i16, f2)), (1, kron(f4, f2)))
    require(qpt == expected_qpt, 'wrong_partial_transpose')
    # Commuting real symmetric involutions have simultaneous eigenvalues ±1.
    eigs = [8 - 4 * eta + eps * eta for eps in (-1, 1) for eta in (-1, 1)]
    require(min(eigs) == 3, 'ppt_spectral_lower_bound')

    # Phi(X)=Tr(X) I4 - X/2. 2 C(Phi tensor id_2) = (2I-O4) tensor O2.
    choi2 = kron(add((2, i16), (-1, o4)), o2)
    pairing = trace_product(q8, choi2)
    require(pairing == -32, 'wrong_choi_pairing')
    objective = Fraction(pairing, 2 * tr_q8)
    require(objective == Fraction(-2, 49), 'wrong_normalized_objective')

    # For every rank<=2 M, |Tr M|^2 <= 2 ||M||_F^2. Thus the Choi
    # quadratic form ||M||_F^2 - |Tr M|^2/2 is nonnegative: Phi is
    # 2-positive by the standard Choi/Schmidt-rank criterion. Its normalized
    # maximally entangled eigenvector has Choi eigenvalue -1, so it is not CP.

    v = [0] * 64
    v[ix(0, 1, 0, 0)] = 1
    v[ix(1, 0, 0, 0)] = -1
    require(quad(qpt, v) >= 0, 'ppt_test_vector_negative')
    controls = [
        intended_failure('transpose_only_A',
                         lambda: require(partial_transpose(q8, False) == expected_qpt,
                                         'wrong_partial_transpose'),
                         'wrong_partial_transpose'),
        intended_failure('omit_ppt_filler',
                         lambda: require(quad(partial_transpose(first), v) >= 0,
                                         'ppt_test_vector_negative'),
                         'ppt_test_vector_negative'),
        intended_failure('wrong_map_scaling',
                         lambda: require(trace_product(q8, kron(add((2, i16), (-2, o4)), o2)) == -32,
                                         'wrong_choi_pairing'),
                         'wrong_choi_pairing'),
    ]
    print(json.dumps({
        'status': 'PASS_EXACT_SELECTED_EQ6_EXAMPLE',
        'd': 4, 'k': 2,
        'map': 'Phi(X)=Tr(X) I_4 - X/2',
        'unscaled_Q_trace': 49,
        'PPT_scaled_eigenvalues': sorted(set(eigs)),
        'PPT_minimum_eigenvalue': str(Fraction(3, 392)),
        'scaled_choi_pairing': pairing,
        'normalized_objective': str(objective),
        'intended_mutation_rejections': controls,
        'two_positivity_proof': 'rank-two trace inequality, a written named Choi criterion',
        'is_4x4_ppt_schmidt_number_three_witness': False,
        'universal_equation6_collapse_proved_by_finite_run': False,
        'priority_or_novelty_established': False,
    }, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    try:
        main()
    except Rejected as exc:
        print(json.dumps({'status': 'FAIL', 'reason': str(exc)}, sort_keys=True))
        sys.exit(1)
