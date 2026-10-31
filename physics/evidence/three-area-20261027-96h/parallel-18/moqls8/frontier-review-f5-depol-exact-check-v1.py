#!/usr/bin/env python3
"""Independent exact Gaussian-rational checks, not a universal proof.

Uses only the standard library; imports no author code. Two 1-uniform pure
four-qubit states, their mixture, and a complex rank-three projector are
constructed explicitly. Checks every computational matrix unit for two
physical mirror parameters and checks all erasure identities on the samples.
"""
import argparse
import hashlib
import itertools
import json
import pathlib
from fractions import Fraction as Q

D = 16
ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))
I = (Q(0), Q(1))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def mul(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])


def scale(a, value):
    return (a[0] * value, a[1] * value)


def conj(a):
    return (a[0], -a[1])


def empty():
    return [[ZERO for _ in range(D)] for _ in range(D)]


def matrix_add(A, B):
    return [[add(A[i][j], B[i][j]) for j in range(D)] for i in range(D)]


def matrix_scale(A, value):
    return [[scale(A[i][j], value) for j in range(D)] for i in range(D)]


def matrix_mul(A, B):
    C = empty()
    for i in range(D):
        for k in range(D):
            if A[i][k] == ZERO:
                continue
            for j in range(D):
                if B[k][j] != ZERO:
                    C[i][j] = add(C[i][j], mul(A[i][k], B[k][j]))
    return C


def hermitian(A):
    return all(A[i][j] == conj(A[j][i]) for i in range(D) for j in range(D))


def trace(A):
    value = ZERO
    for i in range(D):
        value = add(value, A[i][i])
    return value


def trace_product(A, B):
    value = ZERO
    for i in range(D):
        for j in range(D):
            value = add(value, mul(A[i][j], B[j][i]))
    if value[1] != 0:
        raise ValueError('trace of physical product unexpectedly nonreal')
    return value[0]


def erase_site(A, site):
    bit = 1 << site
    C = empty()
    for i in range(D):
        for j in range(D):
            if (i & bit) == (j & bit):
                C[i][j] = scale(add(A[i & ~bit][j & ~bit], A[i | bit][j | bit]), Q(1, 2))
    return C


def apply_channel(A, p):
    out = A
    for site in range(4):
        out = matrix_add(matrix_scale(out, 1-p), matrix_scale(erase_site(out, site), p))
    return out


def layers(A):
    result = []
    for m in range(5):
        layer = empty()
        for sites in itertools.combinations(range(4), m):
            term = A
            for site in sites:
                term = erase_site(term, site)
            layer = matrix_add(layer, term)
        result.append(layer)
    return result


def spinflip(A):
    return [[scale(A[j ^ 15][i ^ 15], -1 if ((i.bit_count()+j.bit_count()) & 1) else 1)
             for j in range(D)] for i in range(D)]


def phase(k):
    return (ONE, I, (-ONE[0], ZERO[1]), (ZERO[0], -ONE[0]))[k % 4]


def graph_state():
    amplitudes = []
    for x in range(D):
        bits = [(x >> i) & 1 for i in range(4)]
        edge_sign = sum(bits[i] * bits[(i+1) % 4] for i in range(4)) & 1
        amplitudes.append(scale(phase(sum(bits)), -1 if edge_sign else 1))
    return [[scale(mul(amplitudes[i], conj(amplitudes[j])), Q(1, 16))
             for j in range(D)] for i in range(D)]


def ghz_state():
    A = empty()
    A[0][0] = A[15][15] = (Q(1, 2), Q(0))
    A[0][15] = (Q(0), Q(-1, 2))
    A[15][0] = (Q(0), Q(1, 2))
    return A


def rank_three_complex_projector():
    # Columns of a phase-twisted 16-point Walsh ONB, indexed by 0, 5, 9.
    C = empty()
    for x in range(D):
        for y in range(D):
            coefficient = sum(-1 if ((j & (x ^ y)).bit_count() & 1) else 1
                              for j in (0, 5, 9))
            C[x][y] = scale(mul(phase(x.bit_count()), conj(phase(y.bit_count()))), Q(coefficient, 16))
    return C


def identity16():
    A = empty()
    for i in range(D):
        A[i][i] = ONE
    return A


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    ident = identity16()
    P = rank_three_complex_projector()
    require(hermitian(P) and matrix_mul(P, P) == P and trace(P) == (Q(3), Q(0)), 'rank-3 projector check')
    require(any(entry[1] != 0 for row in P for entry in row), 'projector must genuinely be complex')
    pure = [graph_state(), ghz_state()]
    for state in pure:
        require(hermitian(state) and matrix_mul(state, state) == state and trace(state) == ONE, 'pure density check')
        for keep in range(4):
            marginal_expanded = state
            for site in range(4):
                if site != keep:
                    marginal_expanded = erase_site(marginal_expanded, site)
            require(marginal_expanded == matrix_scale(ident, Q(1, 16)), 'one-qubit marginal not I/2')
    mix = matrix_add(matrix_scale(pure[0], Q(2, 5)), matrix_scale(pure[1], Q(3, 5)))
    states = [('complex_cycle_graph', pure[0]), ('complex_ghz', pure[1]), ('convex_mixture', mix)]
    results = []
    for name, state in states:
        Ts = layers(state)
        spin = spinflip(state)
        rebuilt = empty()
        for coefficient, T in zip((1, -2, 4, -8, 16), Ts):
            rebuilt = matrix_add(rebuilt, matrix_scale(T, coefficient))
        require(spin == rebuilt, 'spinflip erasure operator identity')
        vals = [trace_product(P, T) for T in Ts]
        require(vals[0] <= 1 and vals[1] <= 3 and vals[2] <= Q(5, 2)
                and vals[3] == Q(3, 4) and vals[4] == Q(3, 16), 'layer inequalities')
        samples = []
        for p in (Q(0), Q(1,3), Q(1,2), Q(1), Q(7,6), Q(4,3)):
            actual = trace_product(P, apply_channel(state, p))
            s = min(p, 2-p)
            a, b = 1-s/2, s/2
            reference = a**4 + 2*a**3*b
            gap = s*s*(1-s)/2
            require(actual <= reference-gap, 'one-uniform promised gap failed')
            samples.append({'p': str(p), 'actual': str(actual), 'reference': str(reference),
                            'guaranteed_gap': str(gap), 'slack_beyond_gap': str(reference-gap-actual)})
        results.append({'state': name, 'layer_traces': [str(v) for v in vals],
                        'spinflip_operator_identity': True, 'parameters': samples})
    reference_state = empty()
    reference_state[0][0] = ONE
    P_ref = empty()
    for q in (0,1,2):
        P_ref[q][q] = ONE
    reference_vals = [trace_product(P_ref, T) for T in layers(reference_state)]
    require(reference_vals == [Q(1), Q(3), Q(3), Q(5,4), Q(3,16)], 'reference layers')
    basis_checks = 0
    for p in (Q(7,6), Q(4,3)):
        for a in range(D):
            for b in range(D):
                E = empty()
                E[a][b] = ONE
                require(apply_channel(E, p) == spinflip(apply_channel(E, 2-p)), 'operator mirror basis failure')
                basis_checks += 1
    report = {
        'result': 'PASS_INDEPENDENT_EXACT_SAMPLES_NOT_UNIVERSAL_PROOF',
        'checker_sha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        'arithmetic': 'fractions.Fraction pairs for exact complex rational matrices',
        'complex_projector_hermitian_idempotent_trace3': True,
        'pure_sample_idempotence_and_all_one_qubit_marginals': True,
        'physical_samples': results,
        'reference_layer_coefficients': [str(v) for v in reference_vals],
        'mirror_parameters': ['7/6', '4/3'],
        'matrix_unit_mirror_checks': basis_checks,
        'limits': 'Two exact one-uniform pure states and one mixture, one complex rank-three projector; not exhaustive, not a proof or novelty clearance.'
    }
    with pathlib.Path(args.output).open('x', encoding='utf-8') as handle:
        json.dump(report, handle, indent=2)
        handle.write('\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
