#!/usr/bin/env python3
"""Exact canonical five-span TWO-FIBRE shadow assay, never a Boolean U/V witness.

The derivation, selected normalization, bounds, and unpaid conditions are frozen
in prospective-author-plan-v1.json. The finite result is not parent adoption.
No filesystem, network, subprocess, randomness, installation, or deletion.
"""
from collections import Counter
from time import monotonic

START = monotonic()
DEADLINE = START + 50
D = (1, 2, 4, 7)
RHO = (-1, -1, -1, 1)
SMALL = {0, 1, 2, 4}


class Incomplete(Exception):
    pass


class InvariantFailure(Exception):
    pass


def tick():
    if monotonic() >= DEADLINE:
        raise Incomplete('cooperative deadline; no completed classification')


def need(value, reason):
    if not value:
        raise InvariantFailure(reason)


def fwht(values):
    a = list(values)
    width = 1
    while width < len(a):
        for start in range(0, len(a), 2 * width):
            for i in range(start, start + width):
                u, v = a[i], a[i + width]
                a[i], a[i + width] = u + v, u - v
        width *= 2
    return a


def truth(mask):
    return [1 - 2 * ((mask >> i) & 1) for i in range(16)]


def is_bent(mask):
    return all(abs(x) == 4 for x in fwht(truth(mask)))


def g_values(graph):
    # c=(h<<3)|d, F={(0,0),(1,0)}, each B slice a transversal.
    result = [0] * 64
    for h in range(8):
        result[h << 3] = 4 if h in (0, 1) else -2
    for b, d in enumerate(D):
        for h in range(8):
            result[(h << 3) | d] = -2 * RHO[b]
        for j in range(4):
            low_bit = (graph >> (j + 4 * b)) & 1
            result[((2 * j + low_bit) << 3) | d] = RHO[b]
    return result


def g_spectrum_ok(values):
    spectrum = fwht(values)
    return all(abs(x) == (4 if r in SMALL else 12)
               for r, x in enumerate(spectrum))


def graph_support(graph):
    return [((2 * j + ((graph >> (j + 4 * b)) & 1)) << 3) | d
            for b, d in enumerate(D) for j in range(4)]


def a_values(graph, phase):
    out = [0] * 64
    for i, c in enumerate(graph_support(graph)):
        out[c] = 1 - 2 * ((phase >> i) & 1)
    return out


def flat_a(values):
    return all(abs(x) == 4 for x in fwht(values))


def algebraic_normal_form(mask):
    coefficients = [(mask >> i) & 1 for i in range(16)]
    for bit in range(4):
        for i in range(16):
            if i & (1 << bit):
                coefficients[i] ^= coefficients[i ^ (1 << bit)]
    return coefficients


def gf2_rank(rows):
    pivots = {}
    for row in rows:
        while row:
            bit = row.bit_length() - 1
            if bit in pivots:
                row ^= pivots[bit]
            else:
                pivots[bit] = row
                break
    return len(pivots)


def polar_rank(coefficients):
    rows = [0] * 4
    for i in range(4):
        for j in range(i + 1, 4):
            if coefficients[(1 << i) | (1 << j)]:
                rows[i] |= 1 << j
                rows[j] |= 1 << i
    return gf2_rank(rows)



def main():
    tick()
    # rho(d(b))=(-1)^(1+b0*b1), b encoded in two bits.
    q = sum((1 ^ (((b >> 0) & 1) * ((b >> 1) & 1))) << (j + 4 * b)
            for b in range(4) for j in range(4))
    need(q.bit_count() == 12, 'rho-sign-normalization')
    all_bent = []
    graph_ok = []
    for f in range(1 << 16):
        if f % 256 == 0:
            tick()
        if is_bent(f):
            all_bent.append(f)
        predicted = is_bent(f ^ q)
        actual = g_spectrum_ok(g_values(f))
        need(actual == predicted, 'full-64-Walsh-vs-four-variable-bent')
        if actual:
            graph_ok.append(f)
    need(len(all_bent) == 896, 'four-variable-bent-count')
    need(len(graph_ok) == 896, 'actual-g-spectrum-graph-count')

    # Every ordered pair is an independently enumerated pair of flat a phases.
    pair_counts = Counter()
    for index, first in enumerate(all_bent):
        if index % 16 == 0:
            tick()
        for second in all_bent:
            pair_counts[first ^ second] += 1
    survivors = [f for f in graph_ok if pair_counts[f] > 0]
    ranks = Counter()
    multiplicities = Counter()
    for f in survivors:
        tick()
        coefficients = algebraic_normal_form(f)
        need(not any(coefficients[i] and i.bit_count() > 2 for i in range(16)),
             'pair-of-bent-phases-must-have-degree-at-most-two')
        ranks[polar_rank(coefficients)] += 1
        multiplicities[pair_counts[f]] += 1
    need(all(rank in (2, 4) for rank in ranks), 'no-affine-graph-survivor')

    # Exhaustively compare every phase for a representative gluable graph,
    # directly transforming actual 64-position ternary a, not a copied formula.
    f = next((candidate for candidate in survivors if not is_bent(candidate)), None)
    need(f is not None, 'non-bent-graph-positive-control-missing')
    direct_phases = []
    for r in range(1 << 16):
        if r % 256 == 0:
            tick()
        if flat_a(a_values(f, r)):
            direct_phases.append(r)
    expected_phases = [r for r in all_bent if is_bent(r ^ f)]
    need(direct_phases == expected_phases, 'actual-64-Walsh-common-phase-equivalence')
    need(len(direct_phases) == pair_counts[f], 'common-phase-multiplicity')

    controls = []
    bad_g = g_values(f)
    bad_g[0] += 1
    need(not g_spectrum_ok(bad_g), 'mutated-full-block-detected')
    controls.append('mutated-F-block')
    bad_g = g_values(f)
    first = graph_support(f)[0]
    bad_g[first] *= -1
    need(not g_spectrum_ok(bad_g), 'mutated-coset-sign-detected')
    controls.append('mutated-B-sign')
    bad_a = a_values(f, direct_phases[0])
    bad_a[graph_support(f)[0]] *= -1
    need(not flat_a(bad_a), 'mutated-shared-a-sign-detected')
    controls.append('mutated-shared-phase')
    need(not is_bent(f), 'graph-bent-is-not-the-g-spectrum-condition')
    controls.append('wrong-bent-offset')

    tick()
    print('STATUS: COMPLETE_CANONICAL_TWO_FIBRE_SHADOW_CLASSIFICATION')
    print('ALL_65536_GRAPH_SUPPORTS_CHECKED_FULL_64_G_WALSH')
    print('bent_four_variable_functions=' + str(len(all_bent)))
    print('g_spectral_graphs=' + str(len(graph_ok)))
    print('ordered_bent_pairs=' + str(len(all_bent) ** 2))
    print('g_and_common_flat_a_graphs=' + str(len(survivors)))
    print('survivors_by_graph_polar_rank=' + repr(sorted(ranks.items())))
    print('common_flat_a_phase_count_histogram=' + repr(sorted(multiplicities.items())))
    print('direct_64_a_phase_checks=65536; representative_solutions=' + str(len(direct_phases)))
    print('intended_controls=' + repr(controls))
    print('elapsed_seconds=' + format(monotonic() - START, '.6f'))
    print('LIMIT: NONPHYSICAL TWO-FIBRE SHADOW; NOT FULL U/V, BALANCE, OR NL242 WITNESS')


if __name__ == '__main__':
    try:
        main()
    except (Incomplete, InvariantFailure) as exc:
        print('STATUS: INCOMPLETE_OR_FAILED: ' + str(exc))
        raise SystemExit(1)
