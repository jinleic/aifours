#!/usr/bin/env python3
"""UNRUN candidate: exact factorized local checks, not a full physical Y search.

No input files, network, subprocesses, dependencies, or output files.  A parent
must whole-read these bytes and give a separate one-shot GO before execution.
The cooperative internal deadline is 38 seconds; a deadline is PARTIAL, never
PASS.  See author-candidate-v1.md for the mathematical imports and coverage.
"""

from collections import Counter, defaultdict
from itertools import permutations, product
import json
import sys
import time

LIMIT = 38.0
ROWS = range(4)
PHASES = tuple(permutations(range(4)))
F_TABLES = tuple(f for f in range(16) if f.bit_count() % 2 == 1)


class Rejection(Exception):
    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


class Deadline(Exception):
    pass


def need(condition, reason):
    if not condition:
        raise Rejection(reason)


def dot(a, b):
    return (a & b).bit_count() & 1


def swap(x):
    return ((x & 1) << 1) | ((x >> 1) & 1)


def q(x):
    return (x & 1) & ((x >> 1) & 1)


def sign(bit):
    return -1 if bit & 1 else 1


def xor_values(values):
    value = 0
    for x in values:
        value ^= x
    return value


def row_zero(srow, drow):
    need(len(srow) == 4 and all(x in (-1, 1) for x in srow), "GRAPH_SIGNS")
    need(len(drow) == 4 and all(x in (-1, 0, 1) for x in drow), "D0_SIGNS")
    need(sum(srow) + 2 * sum(drow) == 0, "ROW_ZERO")


def negative_xor(srow, claimed):
    actual = xor_values(b for b in ROWS if srow[b] == -1)
    need(actual == claimed, "NEGATIVE_XOR")


def graph_phase(srow, lam, row_sign, graph):
    expected = tuple(row_sign * srow[b] * sign(q(b) ^ dot(lam, b)) for b in ROWS)
    need(tuple(graph) == expected, "PHASE_ACTION")


def mate_product(d3, alpha, row_sign, claimed_xor):
    positions = [b for b in ROWS if d3[b] != 0]
    neg = sum(d3[b] == -1 for b in positions) & 1
    actual = 1
    for b in positions:
        actual *= row_sign * d3[b] * sign(dot(alpha, b))
    exponent = neg ^ dot(alpha, claimed_xor) ^ ((len(positions) & 1) * (row_sign == -1))
    need(actual == sign(exponent), "MATE_XOR")


def slope_identity(m, v):
    need(len(m) == 4 and all(x in (0, 1) for x in m), "SLOPE_INPUT")
    values = [m[a] ^ dot(a, v) for a in ROWS]
    need(all(x == values[0] for x in values), "SLOPE_IDENTITY")


def f_odd(f):
    need(f.bit_count() % 2 == 1, "F_PARITY")


def slices(parity):
    need(len(parity) == 2 and all(len(row) == 16 for row in parity), "SLICE_SHAPE")
    need(all(all(v == row[0] for v in row) for row in parity), "SLICE_NONUNIFORM")
    need(parity[0][0] != parity[1][0], "SLICE_SWITCH")


def census(n, m, h, z):
    need(n == 2 * m, "ENERGY72")
    need(0 <= m <= 16 and 0 <= n <= 16 and 0 <= h <= m and 0 <= z <= 16 - n,
         "CENSUS_BOUNDS")
    need(3 * m + h + 2 * z == 8, "SMALL_COUNT")


def z_pair(b, z_value, mate):
    need(b in (1, 2, 3), "Z_LOCATION")
    need(abs(z_value) == 4, "Z4_MAGNITUDE")
    need(abs(mate) <= 2, "Z_MATE_BOUND")
    need(abs(z_value + mate) >= 2, "Z_PAIR_GAP")


def inverse_gap(nonzero_count):
    # A fixed 16-point inverse has numerator at most 8 * nonzero_count.
    need(8 * nonzero_count < 16 * 2, "INVERSE_GAP")


def expect_rejection(expected, function, *args):
    try:
        function(*args)
    except Rejection as exc:
        need(exc.reason == expected, "MUTANT_WRONG_REASON:" + expected + ":" + exc.reason)
        return
    raise Rejection("MUTANT_ACCEPTED:" + expected)


def main():
    start = time.monotonic()
    end = start + LIMIT
    state = {"stage": "initial", "completed": {}, "progress": {}}

    def check_time():
        if time.monotonic() >= end:
            raise Deadline()

    try:
        # Enumerate all one-row X graph signs and D0-mate signs, not all Y.
        state["stage"] = "one_row"
        hist = [Counter() for _ in range(5)]
        representatives = [dict() for _ in range(5)]
        row_counts = Counter()
        row_phase_cells = 0
        quotient_cells = 0
        for occupied in range(16):
            check_time()
            sites = [b for b in ROWS if (occupied >> b) & 1]
            k = len(sites)
            for dmask in range(1 << k):
                drow = [0] * 4
                for j, b in enumerate(sites):
                    drow[b] = sign((dmask >> j) & 1)
                for smask in range(16):
                    srow = tuple(sign((smask >> b) & 1) for b in ROWS)
                    if sum(srow) + 2 * sum(drow) != 0:
                        continue
                    row_zero(srow, drow)
                    p = xor_values(b for b in ROWS if srow[b] == -1)
                    b0 = xor_values(sites)
                    negative_xor(srow, p)
                    if k & 1:
                        nu = 3 ^ swap(p)
                        need(all(srow[b] == srow[0] * sign(q(b) ^ dot(nu, b))
                                 for b in ROWS), "ODD_ROW_FORM")
                    else:
                        xi = swap(p)
                        need(all(srow[b] == srow[0] * sign(dot(xi, b))
                                 for b in ROWS), "EVEN_ROW_FORM")
                    for s in range(2):
                        for alpha in (1, 2, 3):
                            numerator = sum(srow[b] * sign(dot(alpha, b)) for b in ROWS)
                            numerator += 2 * sign(s) * sum(drow[b] * sign(dot(alpha, b)) for b in ROWS)
                            need(numerator % 4 == 0, "QUOTIENT_DIVISIBILITY")
                            need((numerator // 4) % 2 == (1 ^ (s & (k & 1)) ^ dot(alpha, p ^ b0)),
                                 "ROW_QUOTIENT_PARITY")
                            quotient_cells += 1
                    for lam in ROWS:
                        graph = tuple(srow[b] * sign(q(b) ^ dot(lam, b)) for b in ROWS)
                        graph_phase(srow, lam, 1, graph)
                        for alpha in ROWS:
                            transform = sum(graph[b] * sign(dot(alpha, b)) for b in ROWS)
                            if k & 1:
                                need(abs(transform) == (4 if alpha == (lam ^ nu) else 0),
                                     "AFFINE_GRAPH_WALSH")
                            else:
                                need(abs(transform) == 2, "BENT_GRAPH_WALSH")
                                need(transform == 2 * srow[0] * sign(q(alpha ^ lam ^ xi)),
                                     "BENT_GRAPH_SIGN")
                            row_phase_cells += 1
                    delta = p ^ b0
                    hist[k][delta] += 1
                    representatives[k].setdefault(delta, (srow, tuple(drow), p, b0))
                    row_counts[k] += 1
        state["completed"]["one_row"] = {
            "row_sign_and_D0_sign_assignments_by_k": dict(row_counts),
            "quotient_cells": quotient_cells, "phase_walsh_cells": row_phase_cells,
        }

        # Compress all actual local row assignments by their four-valued P xor B.
        # The weighted DP applies only the even graph-support projection, not
        # singleton/plane signs or a common ell-zero X completion.
        state["stage"] = "weighted_graph_projection"
        shapes = [ks for ks in product(range(5), repeat=4) if sum(ks) in (0, 2, 4)]
        projection = {d: {"occupancy_shapes": 0, "all_rows_weighted": 0,
                          "even_support_weighted": 0, "nonempty_shapes": 0}
                      for d in (0, 2, 4)}
        shape_examples = []
        for ks in shapes:
            check_time()
            d = 4 - sum(ks)
            dp = [1, 0, 0, 0]
            for k in ks:
                nxt = [0, 0, 0, 0]
                for x in ROWS:
                    for delta, count in hist[k].items():
                        nxt[x ^ delta] += dp[x] * count
                dp = nxt
            record = projection[d]
            record["occupancy_shapes"] += 1
            record["all_rows_weighted"] += sum(dp)
            record["even_support_weighted"] += dp[0]
            if dp[0]:
                record["nonempty_shapes"] += 1
                witness = None
                for a, b, c in product(ROWS, repeat=3):
                    delta_tuple = (a, b, c, a ^ b ^ c)
                    if all(delta_tuple[i] in representatives[ks[i]] for i in ROWS):
                        witness = tuple(representatives[ks[i]][delta_tuple[i]] for i in ROWS)
                        break
                need(witness is not None, "PROJECTION_WITNESS")
                shape_examples.append((ks, witness))
        state["completed"]["weighted_graph_projection"] = projection

        # Exhaust the slope identity in an explicitly larger algebraic quotient:
        # every even/odd row mask, every P tuple and every distinct phase tuple.
        state["stage"] = "slope_quotient"
        slope_counts = Counter()
        slope_cases = 0
        for odd_mask in range(16):
            if odd_mask.bit_count() % 2:
                continue
            odd_count = odd_mask.bit_count()
            for ps in product(ROWS, repeat=4):
                check_time()
                B = xor_values(ps)
                for lam in PHASES:
                    theta_xor = 0
                    kappas = []
                    for i in ROWS:
                        if (odd_mask >> i) & 1:
                            kappas.append(lam[i] ^ 3 ^ swap(ps[i]))
                        else:
                            theta_xor ^= lam[i] ^ swap(ps[i])
                    v = B ^ swap(theta_xor)
                    need(xor_values(kappas) == swap(v), "PHASE_LINK")
                    counts = Counter(kappas)
                    m = [counts[a] & 1 for a in ROWS]
                    support = [a for a in ROWS if m[a]]
                    need(len(support) in (0, 2, 4), "EVEN_SUPPORT")
                    need(xor_values(support) == swap(v), "SUPPORT_XOR")
                    slope_identity(m, v)
                    for alpha in ROWS:
                        left = sum(q(alpha ^ (lam[i] ^ swap(ps[i])))
                                   for i in ROWS if not ((odd_mask >> i) & 1)) & 1
                        right = (sum(q(lam[i] ^ swap(ps[i]))
                                     for i in ROWS if not ((odd_mask >> i) & 1)) & 1)
                        right ^= dot(alpha, swap(theta_xor))
                        need(left == right, "BENT_QUADRATIC_FACTOR")
                    slope_counts[(odd_count, len(support))] += 1
                    slope_cases += 1
        state["completed"]["slope_quotient"] = {
            "cases": slope_cases,
            "odd_rows_support_size": {str(k): v for k, v in sorted(slope_counts.items())},
            "scope": "algebraic superset, not weighted physical graph objects",
        }

        # All four-position mate rows, including every D0 choice and every D3
        # sign, are checked separately. Product-class weighting is a theorem:
        # every global mate-sign parity represents 2**(nmate-1) assignments.
        state["stage"] = "mate_factor"
        mate_rows = 0
        mate_cells = 0
        for mask in range(16):
            check_time()
            d3_sites = [b for b in ROWS if not ((mask >> b) & 1)]
            b0 = xor_values(b for b in ROWS if (mask >> b) & 1)
            need(xor_values(d3_sites) == b0, "D3_COMPLEMENT_XOR")
            for bits in range(1 << len(d3_sites)):
                d3 = [0] * 4
                for j, b in enumerate(d3_sites):
                    d3[b] = sign((bits >> j) & 1)
                for alpha in ROWS:
                    for weight in (-1, 1):
                        mate_product(d3, alpha, weight, b0)
                        mate_cells += 1
                mate_rows += 1
        state["completed"]["mate_factor"] = {
            "actual_local_mate_rows": mate_rows, "product_cells": mate_cells,
            "global_negative_parity_class_weight": {str(n): 1 << (n - 1) for n in (12, 14, 16)},
            "weight_is_symbolic_not_enumerated_global_Y": True,
        }

        # Separate exhaustions for the beta and s exponents of the product.
        state["stage"] = "physical_row_geometry"
        geometry_cases = 0
        for ks in shapes:
            nmate = 16 - sum(ks)
            even_rows = sum((k & 1) == 0 for k in ks)
            need((nmate + even_rows) % 2 == 0, "EVEN_TERM_COUNT")
            for f in F_TABLES:
                f_odd(f)
                for beta in ROWS:
                    for s in range(2):
                        bexp = 0
                        sexp = 0
                        for i, k in enumerate(ks):
                            fi = (f >> i) & 1
                            if k % 2 == 0:
                                bexp ^= dot(beta, i)
                                sexp ^= fi
                            if (4 - k) & 1:
                                bexp ^= dot(beta, i)
                                sexp ^= 1 ^ fi
                        need(bexp == 0 and (s * sexp) == s, "ROW_GEOMETRY")
                        geometry_cases += 1
                check_time()
        for N in range(12, 21, 2):
            for negatives in range(N + 1):
                need(((N - 2 * negatives) // 2) % 2 == (N // 2 + negatives) % 2,
                     "SIGN_PRODUCT_PARITY")
        state["completed"]["physical_row_geometry"] = {"cases": geometry_cases}

        # Direct actual graph/mate checks on ONE constructed row witness per
        # nonempty occupancy, with ALL distinct phase permutations, odd F,
        # two graph-sign representatives and two mate-sign parities.  This is
        # intentionally not a full X- or Y-enumeration.
        state["stage"] = "direct_factorized_representatives"
        representative_cases = 0
        direct_cells = 0
        by_mates = Counter()
        for ks, witness in shape_examples:
            check_time()
            nmate = 16 - sum(ks)
            even_index = next((i for i in ROWS if ks[i] % 2 == 0), 0)
            d3base = [[1 if witness[i][1][b] == 0 else 0 for b in ROWS] for i in ROWS]
            first = next((i, b) for i in ROWS for b in ROWS if d3base[i][b])
            for lam in PHASES:
                transforms = []
                for i in ROWS:
                    sr = witness[i][0]
                    graph = tuple(sr[b] * sign(q(b) ^ dot(lam[i], b)) for b in ROWS)
                    graph_phase(sr, lam[i], 1, graph)
                    transforms.append([sum(graph[b] * sign(dot(alpha, b)) for b in ROWS)
                                       for alpha in ROWS])
                for graph_flip in (0, 1):
                    gw = [row[:] for row in transforms]
                    if graph_flip:
                        gw[even_index] = [-x for x in gw[even_index]]
                    for mate_flip in (0, 1):
                        d3 = [row[:] for row in d3base]
                        if mate_flip:
                            i, b = first
                            d3[i][b] = -1
                        mw = [[sum(d3[i][b] * sign(dot(alpha, b)) for b in ROWS)
                               for alpha in ROWS] for i in ROWS]
                        for f in F_TABLES:
                            check_time()
                            parity = [[], []]
                            for s in range(2):
                                for alpha in ROWS:
                                    for beta in ROWS:
                                        total = 0
                                        for i in ROWS:
                                            weight = sign((s * ((f >> i) & 1)) ^ dot(beta, i))
                                            total += weight * (gw[i][alpha] + 2 * sign(s) * mw[i][alpha])
                                        need(total % 4 == 0, "A1_DIVISIBILITY")
                                        parity[s].append((total // 4) & 1)
                                        direct_cells += 1
                            slices(parity)
                            representative_cases += 1
                            by_mates[nmate] += 1
                            state["progress"] = {"representatives_checked": representative_cases,
                                                 "direct_cells_checked": direct_cells}
        state["completed"]["direct_factorized_representatives"] = {
            "occupancy_witnesses": len(shape_examples),
            "cases": representative_cases, "frequency_cells": direct_cells,
            "cases_by_nmate": dict(by_mates),
            "not_enumerated": "other row realizations, other mate-sign assignments, ell-zero X, full Y",
        }

        state["stage"] = "integer_census_and_inverse"
        pair_types = Counter()
        for u, v in product((-12, -4, 4, 12), repeat=2):
            a0, a1 = (u + v) // 2, (u - v) // 2
            need(a0 % 4 == 0 and a1 % 4 == 0 and ((a0 // 4) ^ (a1 // 4)) & 1,
                 "PAIR_RESIDUE")
            pair_types[(abs(a0), abs(a1), (abs(u) == 4) + (abs(v) == 4))] += 1
        solutions = []
        for m in range(17):
            for n in range(17):
                if n != 2 * m:
                    continue
                for h in range(m + 1):
                    for z in range(17 - n):
                        if 3 * m + h + 2 * z == 8:
                            census(n, m, h, z)
                            solutions.append((n, m, h, z))
        expected = {(0, 0, 0, 4), (2, 1, 1, 2), (4, 2, 0, 1), (4, 2, 2, 0)}
        need(set(solutions) == expected, "CENSUS_COMPLETENESS")
        for n, m, h, z in solutions:
            need(m - h <= 2, "ODD_SLICE_NONZERO")
            inverse_gap(m - h)
        for b, z_value, mate in product((1, 2, 3), (-4, 4), range(-2, 3)):
            z_pair(b, z_value, mate)
            z_pair(b, z_value, -mate)
        state["completed"]["integer_census_and_inverse"] = {
            "ordered_full_coefficient_pairs": sum(pair_types.values()),
            "absolute_pair_signatures": {str(k): v for k, v in sorted(pair_types.items())},
            "solutions_n_m_h_z": sorted(solutions),
            "odd_A0_nonzero_max": max(m - h for n, m, h, z in solutions),
            "inverse_upper_numerator": 16, "inverse_denominator": 16,
            "physical_Z4_lower_bound": 2,
        }

        state["stage"] = "targeted_mutants"
        mutants = []
        def reject(label, fn, *args):
            expect_rejection(label, fn, *args)
            mutants.append(label)
        reject("ROW_ZERO", row_zero, (1, 1, 1, 1), (0, 0, 0, 0))
        reject("NEGATIVE_XOR", negative_xor, (-1, 1, 1, 1), 1)
        reject("PHASE_ACTION", graph_phase, (1, 1, -1, -1), 0, 1, (1, 1, -1, -1))
        reject("MATE_XOR", mate_product, (1, 1, 1, 0), 1, 1, 2)
        reject("SLOPE_IDENTITY", slope_identity, (1, 1, 0, 0), 0)
        reject("F_PARITY", f_odd, 0)
        reject("SLICE_NONUNIFORM", slices, [[0] * 15 + [1], [1] * 16])
        reject("SLICE_SWITCH", slices, [[0] * 16, [0] * 16])
        reject("ENERGY72", census, 3, 1, 1, 2)
        reject("SMALL_COUNT", census, 2, 1, 0, 2)
        reject("Z_LOCATION", z_pair, 0, 4, 2)
        reject("Z_MATE_BOUND", z_pair, 1, 4, 3)
        reject("INVERSE_GAP", inverse_gap, 4)
        state["completed"]["targeted_mutants"] = mutants
        state["stage"] = "complete"
        state["status"] = "COMPLETE_FINITE_LOCAL_NECESSARY_ONLY"
        state["elapsed_seconds"] = time.monotonic() - start
        print(json.dumps(state, sort_keys=True))
        return 0
    except Deadline:
        state["status"] = "PARTIAL_COOPERATIVE_DEADLINE"
        state["elapsed_seconds"] = time.monotonic() - start
        print(json.dumps(state, sort_keys=True))
        return 2
    except Rejection as exc:
        state["status"] = "FAIL_CHECK"
        state["reason"] = exc.reason
        state["elapsed_seconds"] = time.monotonic() - start
        print(json.dumps(state, sort_keys=True))
        return 1


if __name__ == "__main__":
    sys.exit(main())
