from fractions import Fraction as F
from itertools import combinations
from time import monotonic

START = monotonic()

class Failure(Exception):
    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason

def tick():
    if monotonic() - START > 55:
        raise Failure("deadline")

def need(condition, reason):
    tick()
    if not condition:
        raise Failure(reason)

def expect(reason, operation):
    try:
        operation()
    except Failure as error:
        need(error.reason == reason, "wrong_mutation_reason")
    else:
        raise Failure("mutation_not_rejected")

def crt(a, u):
    a %= 5
    u %= 2
    return a + 5 * ((u - a) % 2)

def linear(terms, n=15):
    answer = [F(0) for _ in range(n)]
    for coefficient, vector in terms:
        answer = [x + F(coefficient) * y
                  for x, y in zip(answer, vector)]
    return tuple(answer)

def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))

def rref(rows):
    tick()
    a = [list(map(F, row)) for row in rows]
    if not a:
        return a, []
    n = len(a[0])
    need(all(len(row) == n for row in a), "matrix_shape")
    pivot_row = 0
    pivots = []
    for column in range(n):
        tick()
        chosen = next((k for k in range(pivot_row, len(a))
                       if a[k][column]), None)
        if chosen is None:
            continue
        a[pivot_row], a[chosen] = a[chosen], a[pivot_row]
        divisor = a[pivot_row][column]
        a[pivot_row] = [x / divisor for x in a[pivot_row]]
        for k in range(len(a)):
            if k != pivot_row and a[k][column]:
                factor = a[k][column]
                a[k] = [x - factor * y
                        for x, y in zip(a[k], a[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(a):
            break
    return a, pivots

def kernel(rows):
    a, pivots = rref(rows)
    n = len(rows[0])
    answer = []
    for free in range(n):
        if free in pivots:
            continue
        vector = [F(0) for _ in range(n)]
        vector[free] = F(1)
        for k, pivot in enumerate(pivots):
            vector[pivot] = -a[k][free]
        answer.append(tuple(vector))
    return answer

def reduce_word(word, orthogonality):
    word = list(word)
    i = 0
    while i + 1 < len(word):
        left, right = word[i], word[i + 1]
        if left[0] == right[0] and left[0] in ("e", "t", "p"):
            if left == right:
                word[i:i + 2] = [left]
                i = max(0, i - 1)
                continue
            if left[0] != "p":
                return None
            if frozenset((left[1], right[1])) in orthogonality:
                return None
        elif {left[0], right[0]} == {"e", "t"}:
            if left[1] == right[1]:
                return None
        i += 1
    return tuple(word)

def normal(terms, orthogonality=frozenset()):
    answer = {}
    for coefficient, word in terms:
        reduced = reduce_word(word, orthogonality)
        if reduced is not None:
            answer[reduced] = answer.get(reduced, F(0)) + F(coefficient)
    return {word: value for word, value in answer.items() if value}

def product_residual(u, v, orthogonality):
    terms = [(F(1), (("p", 2 * u + x), ("p", 2 * y + v)))
             for x in range(2) for y in range(2)]
    terms.append((F(-1), (("p", 2 * u + v),)))
    return normal(terms, orthogonality)

def matrix_product(a, b):
    answer = {}
    for (i, j), x in a.items():
        for (k, ell), y in b.items():
            if j == k:
                key = (i, ell)
                answer[key] = answer.get(key, F(0)) + x * y
    return {key: value for key, value in answer.items() if value}

def matrix_difference(a, b):
    return {key: a.get(key, F(0)) - b.get(key, F(0))
            for key in set(a) | set(b)
            if a.get(key, F(0)) != b.get(key, F(0))}

def commutator(a, b):
    return matrix_difference(matrix_product(a, b), matrix_product(b, a))

def consume_repetition(nonparallel):
    need(nonparallel, "nonparallel_required")

def run():
    delta = {2, 3, 4, 7, 8, 9}
    cells = frozenset((r, c) for r in range(10) for c in range(10)
                      if (c - r) % 10 in delta)
    need(len(cells) == 60, "cell_count")
    contexts = {}
    for label in range(10):
        contexts[("R", label)] = frozenset(x for x in cells if x[0] == label)
        contexts[("C", label)] = frozenset(x for x in cells if x[1] == label)
        contexts[("L", label)] = frozenset(x for x in cells
                                         if sum(x) % 10 == label)
    need(len(contexts) == 30, "context_count")
    need(all(len(x) == 6 for x in contexts.values()), "context_size")
    need(sum(map(len, contexts.values())) == 180, "membership_count")
    need(all(sum(x in group for group in contexts.values()) == 3
             for x in cells), "cell_degree")
    keys = tuple((a, d) for a in range(5) for d in (2, 3, 4))
    index = {key: k for k, key in enumerate(keys)}
    blocks = {key: frozenset(x for x in cells
                            if x[0] % 5 == key[0]
                            and (x[1] - x[0]) % 5 == key[1])
              for key in keys}
    need(all(len(block) == 4 for block in blocks.values()), "block_size")
    need(frozenset().union(*blocks.values()) == cells, "block_cover")
    need(sum(map(len, blocks.values())) == 60, "block_partition")

    def check_routes(inverse):
        emitted = []
        for a, d in keys:
            for u in range(2):
                for v in range(2):
                    r, c = inverse(a, u), inverse((a + d) % 5, v)
                    need((r % 5, r % 2) == (a, u), "crt_parity")
                    need((c % 5, c % 2) == ((a + d) % 5, v),
                         "crt_parity")
                    emitted.append((r, c))
        need(len(emitted) == len(set(emitted)) == 60, "crt_bijection")
        need(frozenset(emitted) == cells, "support")

    check_routes(crt)

    def check_symbols(inverse_two):
        for s in range(5):
            for w in range(2):
                emitted = []
                for d in (2, 3, 4):
                    a = inverse_two * (s - d) % 5
                    for u in range(2):
                        r = crt(a, u)
                        c = crt(a + d, w - u)
                        need((r + c) % 10 == crt(s, w), "symbol_routing")
                        emitted.append((r, c))
                need(frozenset(emitted) == contexts[("L", crt(s, w))],
                     "symbol_routing")

    check_symbols(3)
    routes = {}
    block_pairs = {}
    pair_counts = {"R": 0, "C": 0, "L": 0}
    for key, block in blocks.items():
        pairs = tuple(frozenset(pair) for pair in combinations(sorted(block), 2))
        block_pairs[key] = pairs
        for pair in pairs:
            shared = frozenset(label for label, group in contexts.items()
                               if pair <= group)
            need(len(shared) == 1, "block_pair")
            need(pair not in routes, "duplicate_block_pair")
            routes[pair] = shared
            pair_counts[next(iter(shared))[0]] += 1
    need(len(routes) == 90, "block_pair_count")
    need(pair_counts == {"R": 30, "C": 30, "L": 30}, "pair_family_counts")

    rows, rowmap, families = [], {}, []
    for family in ("R", "C", "L"):
        for residue in range(5):
            first = contexts[(family, crt(residue, 0))]
            second = contexts[(family, crt(residue, 1))]
            need(not first & second, "paired_context_disjointness")
            joined = first | second
            counts = [len(blocks[key] & joined) for key in keys]
            need(len(joined) == 12, "paired_context_size")
            need(all(count in (0, 4) for count in counts), "whole_block_union")
            coefficient = tuple(F(int(count == 4)) for count in counts)
            need(sum(coefficient) == 3, "three_blocks")
            need(sum(coefficient) - 2 == 1, "derived_rhs")
            rows.append(coefficient)
            families.append(family)
            rowmap[(family, residue)] = coefficient
    need(len(rows) == 15, "equation_count")

    def unit(a, d):
        wanted = index[(a % 5, d)]
        return tuple(F(int(k == wanted)) for k in range(15))

    def row(family, residue):
        return rowmap[(family, residue % 5)]

    rank = len(rref(rows)[1])
    nullspace = kernel(rows)
    augmented_rank = len(rref([tuple(r) + (F(1),) for r in rows])[1])
    need(rank == augmented_rank == 13, "full_rank")
    need(len(nullspace) == 2, "full_nullity")
    origin = tuple(F(int(d == 4)) for a, d in keys)
    basis_a = tuple(F(int(d == 2) - int(d == 4)) for a, d in keys)
    basis_b = tuple(F(int(d == 3) - int(d == 4)) for a, d in keys)
    need(all(dot(r, origin) == 1 for r in rows), "affine_origin")
    need(all(dot(r, v) == 0 for r in rows for v in (basis_a, basis_b)),
         "constant_difference_basis")
    for vector in nullspace:
        need(all(vector[index[(a, d)]] == vector[index[(0, d)]]
                 for a, d in keys), "nonconstant_mode")
        need(sum(vector[index[(0, d)]] for d in (2, 3, 4)) == 0,
             "constant_sum_constraint")

    q = {}
    for a in range(5):
        h_difference = linear([(1, unit(a, 4)), (-1, unit(a + 1, 2)),
                               (-1, unit(a - 1, 4)), (1, unit(a, 2))])
        need(h_difference == linear([(1, row("R", a)),
                                     (-1, row("C", a + 3))]), "h_certificate")
        q[a] = linear([(1, row("L", 2 * a + 3)),
                       (1, row("C", a + 4)), (1, row("C", a)),
                       (-1, row("R", a)), (-1, row("R", a + 1)),
                       (-1, row("R", a + 2))])
        need(q[a] == linear([(2, unit(a + 3, 2)), (-1, unit(a, 2)),
                             (-1, unit(a + 1, 2))]), "q_certificate")
    for a in range(5):
        certificate = linear([(F(1, 5), q[(a + 1) % 5]),
                              (F(-3, 5), q[(a + 2) % 5]),
                              (F(3, 5), q[(a + 3) % 5]),
                              (F(-1, 5), q[(a + 4) % 5])])
        need(certificate == linear([(1, unit(a + 1, 2)),
                                    (-1, unit(a, 2))]), "constancy_certificate")

    family_mutants = {}
    for omitted in ("R", "C", "L"):
        retained = [r for r, family in zip(rows, families) if family != omitted]
        mutant_rank = len(rref(retained)[1])
        mutant_kernel = kernel(retained)
        need(mutant_rank == 9 and len(mutant_kernel) == 6, "family_mutant_rank")
        witnesses = [v for v in mutant_kernel
                     if any(v[index[(a, d)]] != v[index[(0, d)]]
                            for a, d in keys)]
        need(bool(witnesses), "family_mutant_nonconstant_witness")
        witness = witnesses[0]
        need(all(dot(r, witness) == 0 for r in retained), "mutant_kernel")
        need(any(dot(r, witness) != 0 for r in rows), "mutant_detected_by_full")
        family_mutants[omitted] = (mutant_rank, len(mutant_kernel), witness)

    def check_support(candidate):
        need(candidate == cells, "support")

    reversed_cells = frozenset((r, c) for r in range(10) for c in range(10)
                               if (r - c) % 10 in delta)
    need(len(reversed_cells) == 60, "reversed_count_control")
    expect("support", lambda: check_support(reversed_cells))
    expect("crt_parity", lambda: check_routes(lambda a, u: a + 5 * u))
    expect("symbol_routing", lambda: check_symbols(1))

    def check_block_pairs(pairs, allowed):
        for pair in pairs:
            need(len(routes[pair] & allowed) == 1, "block_pair")

    omission_cases = 0
    allowed = frozenset(contexts)
    for key, pairs in block_pairs.items():
        required = frozenset().union(*(routes[pair] for pair in pairs))
        need(len(required) == 6, "block_required_context_count")
        for omitted in required:
            reduced_allowed = allowed - {omitted}
            need(sum(not (routes[pair] & reduced_allowed) for pair in pairs) == 1,
                 "one_pair_lost")
            expect("block_pair",
                   lambda: check_block_pairs(pairs, reduced_allowed))
            omission_cases += 1
    need(omission_cases == 90, "omission_case_count")

    off_diagonal_certificates = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if j == k:
                    continue
                ej, ek = ("e", j), ("e", k)
                if i == j or i == k:
                    terms = [(1, (ej, ("t", i), ek))]
                else:
                    terms = [(1, (ej, ek)),
                             (-1, (ej, ("t", j), ek)),
                             (-1, (ej, ("t", k), ek))]
                need(not normal(terms), "partition_commutation_certificate")
                off_diagonal_certificates += 1
    need(off_diagonal_certificates == 18, "partition_certificate_count")

    orthogonality = frozenset(frozenset(pair)
                              for pair in combinations(range(4), 2))
    for u in range(2):
        for v in range(2):
            need(not product_residual(u, v, orthogonality), "ray_intersection")
    weakened_orthogonality_cases = 0
    for omitted in orthogonality:
        weakened = orthogonality - {omitted}
        need(any(product_residual(u, v, weakened)
                 for u in range(2) for v in range(2)),
             "missing_orthogonality_not_detected")
        weakened_orthogonality_cases += 1
    need(weakened_orthogonality_cases == 6, "orthogonality_mutant_count")

    plane = {(0, 0): F(1), (1, 1): F(1)}
    sector = {(0, 0): F(1)}
    ray = {(i, j): F(1, 2) for i in range(2) for j in range(2)}
    need(matrix_product(plane, plane) == plane, "plane_projection")
    need(matrix_product(sector, sector) == sector, "sector_projection")
    need(matrix_product(ray, ray) == ray, "ray_projection")
    need(ray[(0, 0)] + ray[(1, 1)] == 1, "ray_rank_one_trace")
    need(ray[(0, 1)] == ray[(1, 0)], "ray_hermitian")
    need(not commutator(plane, sector), "plane_commutes")
    need(commutator(ray, sector) == {(1, 0): F(1, 2), (0, 1): F(-1, 2)},
         "plane_only_mutant")

    separated_pairs = 0
    for qcell in cells:
        row_others = contexts[("R", qcell[0])] - {qcell}
        column_others = contexts[("C", qcell[1])] - {qcell}
        for x in row_others:
            for y in column_others:
                need(x != y, "row_column_partner_cells")
                separated_pairs += 1
    need(separated_pairs == 1500, "partner_separation_count")
    consume_repetition(True)
    expect("nonparallel_required", lambda: consume_repetition(False))
    tick()
    return {
        "cells": len(cells),
        "contexts": len(contexts),
        "memberships": 180,
        "blocks": len(blocks),
        "block_pairs": len(routes),
        "pair_family_counts": pair_counts,
        "scalar_rank": rank,
        "augmented_rank": augmented_rank,
        "scalar_nullity": len(nullspace),
        "affine_origin": origin,
        "difference_basis": (basis_a, basis_b),
        "family_mutants": family_mutants,
        "row_span_certificates": 15,
        "physical_context_omissions": omission_cases,
        "partition_certificates": off_diagonal_certificates,
        "ray_product_certificates": 4,
        "orthogonality_omissions": weakened_orthogonality_cases,
        "partner_cell_separations": separated_pairs,
        "scope": "FINITE_AND_FORMAL_INTERFACES_ONLY"
    }

RESULTS = run()
