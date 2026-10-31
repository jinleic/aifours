#!/usr/bin/env python3
"""Independent exact check of one f347 six-node moment-only counterexample.

Checks only the supplied finite instance plus an analytic all-delta interlacing
certificate.  It does not establish a strict-negative certificate, an all-box
no-go, a universal cone reduction, or priority.  No file/network writes.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import sys


class Rejected(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise Rejected(reason)


def even(t):
    return (F(1, 2) - t) * (F(2) - t) * (F(4) - t)


def odd(t, delta):
    return (F(1) - t) * (F(3) - t) * (F(5) - t) + delta


def derivative(nodes, index):
    answer = F(1)
    for j, value in enumerate(nodes):
        if j != index:
            answer *= nodes[index] - value
    return answer


def signs(values):
    return [1 if x > 0 else -1 if x < 0 else 0 for x in values]


def finite_instance(nodes, deltas, weights):
    require(len(nodes) == len(deltas) == len(weights) == 6, 'wrong_count')
    require(all(nodes[i] < nodes[i + 1] for i in range(5)), 'node_order')
    require(all(F(-1) <= x <= F(1) for x in deltas), 'member_outside_box')
    odd_values = [odd(t, d) for t, d in zip(nodes, deltas)]
    require(odd_values == [F((-1) ** (i + 1), 10) for i in range(6)],
            'odd_value_mismatch')
    require(all(w > 0 for w in weights), 'nonpositive_weight')
    odd_moments = [sum((w * (-1) ** k * t ** (k + 1) * o
                        for t, o, w in zip(nodes, odd_values, weights)), F(0))
                   for k in range(4)]
    require(odd_moments == [F(0)] * 4, 'odd_moment_nonzero')
    rows = [[even(t), t * o, -t * even(t), -(t ** 2) * o,
             t ** 2 * even(t), t ** 3 * o, -(t ** 3) * even(t),
             -(t ** 4) * o] for t, o in zip(nodes, odd_values)]
    aggregate = [sum((w * row[j] for w, row in zip(weights, rows)), F(0))
                 for j in range(8)]
    require(signs(aggregate) == [-1, 0, 1, 0, -1, 0, 1, 0],
            'aggregate_sign_pattern')
    return odd_values, odd_moments, aggregate


def orientation(values, expected):
    require(signs(values) == expected, 'wrong_five_node_orientation')


def intended_failure(name, operation, expected_reason):
    try:
        operation()
    except Rejected as exc:
        require(str(exc) == expected_reason, 'unexpected_control_reason:' + name)
        return {'name': name, 'reason': str(exc)}
    raise Rejected('mutant_was_accepted:' + name)


def main():
    nodes = [F(26 + i, 30) for i in range(1, 7)]
    deltas = [F(-961, 1000), F(-3107, 6750), F(-10081, 27000),
              F(1, 10), F(4321, 27000), F(4097, 6750)]
    expected_odd = [F((-1) ** (i + 1), 10) for i in range(6)]
    weights = [1 / (t * o * derivative(nodes, i))
               for i, (t, o) in enumerate(zip(nodes, expected_odd))]

    # These exact endpoint inequalities hold for EVERY delta in [-1,1].
    # The fixed E roots are 1/2, 2, 4; the odd cubic has a sign change
    # in each successive interval and leading coefficient -1.  The named
    # strict Hermite-Biehler interlacing theorem then gives Hurwitz stability.
    extrema = [[odd(t, F(-1)), odd(t, F(1))]
               for t in (F(1, 2), F(2), F(4))]
    require(extrema[0][0] > 0 and extrema[1][1] < 0 and extrema[2][0] > 0,
            'hurwitz_interlacing_signs')
    require(all(F(1, 2) < t < F(2) for t in nodes), 'node_even_interval')
    odd_values, moments, aggregate = finite_instance(nodes, deltas, weights)

    left_nodes, right_nodes = nodes[:5], nodes[1:]
    left_odd, right_odd = odd_values[:5], odd_values[1:]
    orientation(left_odd, [-1, 1, -1, 1, -1])
    orientation(right_odd, [1, -1, 1, -1, 1])
    left = [-1 / (t * o * derivative(left_nodes, i))
            for i, (t, o) in enumerate(zip(left_nodes, left_odd))] + [F(0)]
    right = [F(0)] + [1 / (t * o * derivative(right_nodes, i))
                      for i, (t, o) in enumerate(zip(right_nodes, right_odd))]
    require(all(x > 0 for x in left[:5] + right[1:]), 'nonpositive_five_node_ray')
    scale = 1 / (nodes[-1] - nodes[0])
    require(all(weights[i] == scale * (left[i] + right[i]) for i in range(6)),
            'six_node_decomposition')
    positive_first = [list(indices) for indices in combinations(range(6), 5)
                      if signs([odd_values[i] for i in indices]) == [1, -1, 1, -1, 1]]
    require(positive_first == [[1, 2, 3, 4, 5]], 'positive_first_support_census')
    require(weights[0] > 0 and all(0 not in x for x in positive_first),
            'positive_first_cannot_cover_first_coordinate')

    bad_delta = deltas.copy()
    bad_delta[0] = F(2)
    changed_delta = deltas.copy()
    changed_delta[0] += F(1, 1000)
    bad_weights = weights.copy()
    bad_weights[0] += 1
    controls = [
        intended_failure('member_outside_box',
                         lambda: finite_instance(nodes, bad_delta, weights),
                         'member_outside_box'),
        intended_failure('changed_odd_value',
                         lambda: finite_instance(nodes, changed_delta, weights),
                         'odd_value_mismatch'),
        intended_failure('changed_weight',
                         lambda: finite_instance(nodes, deltas, bad_weights),
                         'odd_moment_nonzero'),
        intended_failure('wrong_orientation',
                         lambda: orientation(left_odd, [1, -1, 1, -1, 1]),
                         'wrong_five_node_orientation'),
    ]
    output = {
        'status': 'PASS_EXACT_FINITE_EXAMPLE',
        'nodes': [str(x) for x in nodes],
        'deltas': [str(x) for x in deltas],
        'odd_values': [str(x) for x in odd_values],
        'weights': [str(x) for x in weights],
        'odd_moments': [str(x) for x in moments],
        'aggregate': [str(x) for x in aggregate],
        'aggregate_signs': signs(aggregate),
        'endpoint_odd_ranges_at_even_roots': [[str(v) for v in pair] for pair in extrema],
        'five_node_decomposition_scale': str(scale),
        'positive_first_supports_zero_based': positive_first,
        'expected_mutation_rejections': controls,
        'all_box_hurwitz_boundary': 'analytic strict interlacing plus named Hermite-Biehler theorem',
        'strict_negative_certificate': False,
        'global_no_go_or_original_problem_closure': False,
        'universal_cone_reduction_proved_by_this_run': False,
    }
    print(json.dumps(output, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    try:
        main()
    except Rejected as exc:
        print(json.dumps({'status': 'FAIL', 'reason': str(exc)}, sort_keys=True))
        sys.exit(1)
