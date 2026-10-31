#!/usr/bin/env python3
"""UNRUN author source: necessary local relaxation for T14, not an array solver.

No files or network are accessed. A prospective parent may audit, pin and admit
one run. Cycles are identified only up to permutation of the three high-join
rows. A completed zero count would exclude this local interface, not certify
an 11-row array. The parent must review the completeness argument and source.
"""
from itertools import combinations, permutations
import json
import time

A = (0, 1, 2)
B = (3, 4, 5)
U = (6, 7, 8)
V = (9, 10, 11)
TIME_LIMIT_SECONDS = 40.0


def square_arcs(cycle):
    return {(cycle[i], cycle[(i + 2) % len(cycle)]) for i in range(len(cycle))}


def h_cycle(order):
    return tuple(vertex for i in order for vertex in (A[i], U[i], B[i], V[i]))


def paths(high):
    if high:
        return tuple((p, x, y, q) for p, x in permutations(A, 2)
                     for y, q in permutations(B, 2))
    return tuple((p, y, x, q) for p, y in permutations(B, 2)
                 for x, q in permutations(A, 2))


def square_pair(path):
    p, x, y, q = path
    return ((p, y), (x, q))


def selected_arc(path, high, side):
    if (high and side == 'A') or (not high and side == 'B'):
        return (path[0], path[1])
    return (path[2], path[3])


def extension_arc(path, high, side):
    universe = A if side == 'A' else B
    u, v = selected_arc(path, high, side)
    third = next(z for z in universe if z != u and z != v)
    # A->B joins leave the A run and enter the B run; B->A is reversed.
    if (high and side == 'A') or (not high and side == 'B'):
        return (third, u)
    return (v, third)


def all_internal(universe):
    return {(u, v) for u in universe for v in universe if u != v}


def full_slots(rows, side):
    selected = [selected_arc(path, high, side) for high, path in rows]
    required = all_internal(A if side == 'A' else B)
    if len(set(selected)) != 4:
        return ()
    answers = []
    for slots in combinations(range(4), 2):
        all_arcs = selected + [extension_arc(rows[i][1], rows[i][0], side)
                               for i in slots]
        if len(set(all_arcs)) == 6 and set(all_arcs) == required:
            answers.append(slots)
    return tuple(answers)


def high_is_admissible(highs, target_ab):
    squares = [arc for path in highs for arc in square_pair(path)]
    if len(set(squares)) != 6 or set(squares) != target_ab:
        return False
    if len({(path[1], path[2]) for path in highs}) != 3:
        return False
    for side in ('A', 'B'):
        if len({selected_arc(path, True, side) for path in highs}) != 3:
            return False
    return True


def fixture_control(f_ab, g_choices):
    # A deliberately local, NOT an actual 11-row array: it survives when
    # the h-square B->A exclusion is dropped, and must fail for both choices.
    highs = ((A[1], A[0], B[0], B[1]),
             (A[2], A[0], B[1], B[2]),
             (A[2], A[1], B[0], B[2]))
    low = (B[1], B[0], A[0], A[1])
    target = {(a, b) for a in A for b in B} - f_ab
    rows = tuple((True, p) for p in highs) + ((False, low),)
    local = (high_is_admissible(highs, target)
             and (1, 2) in full_slots(rows, 'A')
             and (1, 2) in full_slots(rows, 'B'))
    low_squares = set(square_pair(low))
    collisions = tuple(bool(low_squares & g) for g in g_choices)
    return local and all(collisions), collisions


def main():
    started = time.monotonic()
    h_plus = h_cycle((0, 1, 2))
    h_minus = h_cycle((0, 2, 1))
    if any(len(h) != 12 or len(set(h)) != 12 for h in (h_plus, h_minus)):
        raise RuntimeError('h_E control is not a connected 12-cycle')
    sq_plus, sq_minus = square_arcs(h_plus), square_arcs(h_minus)
    f_ab = {(A[i], B[i]) for i in range(3)}
    if any({arc for arc in sq if arc[0] in A and arc[1] in B} != f_ab
           for sq in (sq_plus, sq_minus)):
        raise RuntimeError('h_E A-to-B square matching control failed')
    g_choices = tuple({arc for arc in sq if arc[0] in B and arc[1] in A}
                      for sq in (sq_plus, sq_minus))
    if len(g_choices[0]) != 3 or len(g_choices[1]) != 3 or g_choices[0] == g_choices[1]:
        raise RuntimeError('h_E reverse-square control failed')
    fixture_ok, fixture_collisions = fixture_control(f_ab, g_choices)
    if not fixture_ok:
        raise RuntimeError('local positive/missing-G control failed')

    target_ab = {(a, b) for a in A for b in B} - f_ab
    high_paths, low_paths = paths(True), paths(False)
    high_combinations = 0
    low_candidates = 0
    drop_g_configurations = 0
    baseline_configurations = 0
    for highs in combinations(high_paths, 3):
        if time.monotonic() - started > TIME_LIMIT_SECONDS:
            print(json.dumps({'status': 'INCOMPLETE', 'reason': 'cooperative time limit',
                              'high_combinations': high_combinations,
                              'low_candidates': low_candidates}, sort_keys=True))
            return
        if not high_is_admissible(highs, target_ab):
            continue
        high_combinations += 1
        for low in low_paths:
            low_candidates += 1
            rows = tuple((True, p) for p in highs) + ((False, low),)
            a_slots = full_slots(rows, 'A')
            if not a_slots:
                continue
            b_slots = full_slots(rows, 'B')
            if not b_slots:
                continue
            multiplicity = len(a_slots) * len(b_slots)
            drop_g_configurations += 2 * multiplicity
            low_squares = set(square_pair(low))
            baseline_configurations += multiplicity * sum(
                not bool(low_squares & g) for g in g_choices)
    print(json.dumps({
        'status': 'COMPLETE',
        'high_combinations': high_combinations,
        'low_candidates': low_candidates,
        'baseline_configurations': baseline_configurations,
        'drop_g_configurations': drop_g_configurations,
        'fixture_local_positive': fixture_ok,
        'fixture_g_collisions': fixture_collisions,
        'interpretation': 'local necessary relaxation only; not eleven-row existence',
    }, sort_keys=True))


if __name__ == '__main__':
    main()
