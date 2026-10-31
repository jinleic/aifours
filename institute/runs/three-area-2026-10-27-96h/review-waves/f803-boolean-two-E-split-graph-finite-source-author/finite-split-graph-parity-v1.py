#!/usr/bin/env python3
"""UNRUN proposal: exact, finite, factorized split-graph interface checks.

No files, network, child processes, or third-party packages are used. This is
not a full-X or full-Y search. Parent whole-read and a separate GO are required.
A cooperative deadline produces INCOMPLETE, never PASS. All counts and controls
are checked explicitly, not with assert (so -O cannot disable them).
"""
from itertools import combinations, permutations, product
import json
import sys
import time

SECONDS = 300
V = tuple(range(4))
SIGNS = (-1, 1)


class CheckFailure(Exception):
    def __init__(self, reason, detail=""):
        super().__init__(reason)
        self.reason = reason
        self.detail = detail


class DeadlineReached(Exception):
    pass


def need(condition, reason, detail=""):
    if not condition:
        raise CheckFailure(reason, detail)


def tick(deadline):
    if time.monotonic() >= deadline:
        raise DeadlineReached()


def sgn(bit):
    return -1 if bit & 1 else 1


def dot(x, y):
    return (x & y).bit_count() & 1


def quad(x):
    return (x & 1) * ((x >> 1) & 1)


def swap(x):
    return ((x & 1) << 1) | ((x >> 1) & 1)


def sign_product(values):
    out = 1
    for value in values:
        out *= value
    return out


def graph_values(sig, nu):
    return tuple(sig * sgn(quad(b) ^ dot(nu, b)) for b in V)


def check_graph_spec(F, rows, occupied, other):
    need(len(F) == 4 and all(v in (0, 1) for v in F), "F_BITS")
    need(sum(F) % 2 == 1, "F_PARITY")
    need(len(rows) == 2 and all(r in V for r in rows) and
         len(set(rows)) == 2, "GRAPH_ROW_DISTINCT")
    need(len(occupied) == 2 and len(other) == 2, "ROW_ARITY")
    for g, z, eps in occupied:
        need(len(g) == 4 and all(v in SIGNS for v in g) and
             abs(sum(g)) == 2, "SIGNED_3_TO_1")
        need(z in V, "MATE_POSITION")
        need(eps in SIGNS and sum(g) + 2 * eps == 0, "ZERO_FLAT")
    for theta, sig in other:
        need(theta in (1, 2, 3), "THETA_NONZERO")
        need(sig in SIGNS, "OTHER_SIGN")
    # Same b is allowed: rows differ, so these are distinct physical mates.
    need(len({(rows[j], occupied[j][1]) for j in range(2)}) == 2,
         "PHYSICAL_MATES_DISTINCT")


def check_e_sites(sites):
    allowed = {(i, h) for i in (1, 2, 3) for h in (0, 1)}
    need(len(sites) == 2 and len(set(sites)) == 2 and
         all(site in allowed for site in sites), "E_SITE_PLACEMENT")


def check_profile(values):
    need(len(values) == 8 and all(x in (-2, -1, 0, 1, 2) for x in values),
         "PROFILE_VALUES")
    support = [j for j, x in enumerate(values) if x]
    if len(support) == 1 and abs(values[support[0]]) == 2:
        return "singleton"
    need(len(support) == 4 and all(abs(values[j]) == 1 for j in support),
         "PROFILE_SUPPORT")
    x = 0
    for j in support:
        x ^= j
    need(x == 0, "PROFILE_PLANE_GEOMETRY")
    need(sign_product(values[j] for j in support) == -1,
         "PROFILE_SIGN_PRODUCT")
    return "plane"


def check_link(nu0, nu1, theta0, theta1, z0, z1):
    need((z0 ^ z1 ^ swap(nu0 ^ nu1) ^ swap(theta0 ^ theta1)) == 0,
         "PROFILE_PARITY_LINK")


def check_slice(bits):
    need(len(bits) == 2 and all(len(row) == 16 for row in bits),
         "SLICE_SHAPE")
    need(all(x == bits[s][0] for s in (0, 1) for x in bits[s]),
         "Y_SLICE_NONUNIFORM")
    need(bits[0][0] != bits[1][0], "Y_SLICE_SWITCH")


def check_census(n, m, h, z4):
    need(all(isinstance(x, int) for x in (n, m, h, z4)) and
         0 <= n <= 16 and 0 <= m <= 16 and 0 <= h <= m and
         0 <= z4 <= 16 - n, "COUNT_BOUNDS")
    need(4 * n + m + 9 * (16 - m) == 144, "ENERGY72")
    need(8 == n + m + h + 2 * z4, "SMALL_CENSUS")


def expect_rejection(expected, operation):
    try:
        operation()
    except CheckFailure as exc:
        need(exc.reason == expected, "CONTROL_WRONG_REASON",
             "expected " + expected + ", got " + exc.reason)
        return expected
    raise CheckFailure("CONTROL_UNDETECTED", expected)


def controls():
    F = (0, 0, 0, 1)
    g = graph_values(1, 0)
    # Two distinct physical mates deliberately share b=0.
    occ = ((g, 0, -1), (g, 0, -1))
    other = ((1, 1), (2, -1))
    check_graph_spec(F, (0, 1), occ, other)
    check_e_sites(((1, 0), (1, 1)))
    check_e_sites(((1, 0), (2, 0)))
    check_profile((2, 0, 0, 0, 0, 0, 0, 0))
    check_profile((1, -1, 0, 0, 1, 1, 0, 0))
    check_link(0, 0, 1, 1, 0, 0)
    check_slice([[0] * 16, [1] * 16])
    check_census(2, 1, 1, 2)
    out = {}
    out["even_F"] = expect_rejection("F_PARITY", lambda:
        check_graph_spec((0, 0, 0, 0), (0, 1), occ, other))
    out["same_graph_row"] = expect_rejection("GRAPH_ROW_DISTINCT", lambda:
        check_graph_spec(F, (0, 0), occ, other))
    out["constant_occupied_row"] = expect_rejection("SIGNED_3_TO_1", lambda:
        check_graph_spec(F, (0, 1), (((1, 1, 1, 1), 0, -1), occ[1]), other))
    out["wrong_mate_sign"] = expect_rejection("ZERO_FLAT", lambda:
        check_graph_spec(F, (0, 1), ((g, 0, 1), occ[1]), other))
    out["outside_b"] = expect_rejection("MATE_POSITION", lambda:
        check_graph_spec(F, (0, 1), ((g, 4, -1), occ[1]), other))
    out["constant_other_graph"] = expect_rejection("THETA_NONZERO", lambda:
        check_graph_spec(F, (0, 1), occ, ((0, 1), other[1])))
    out["full_site_as_E"] = expect_rejection("E_SITE_PLACEMENT", lambda:
        check_e_sites(((0, 0), (1, 0))))
    out["odd_graph_projection"] = expect_rejection("PROFILE_SUPPORT", lambda:
        check_profile((0, 0, 0, 0, 1, 0, 0, 0)))
    out["wrong_pair_difference"] = expect_rejection("PROFILE_PLANE_GEOMETRY", lambda:
        check_profile((1, 1, 0, 0, 1, 0, -1, 0)))
    out["even_plane_sign"] = expect_rejection("PROFILE_SIGN_PRODUCT", lambda:
        check_profile((1, 1, 1, 1, 0, 0, 0, 0)))
    out["missing_mate_position_in_link"] = expect_rejection("PROFILE_PARITY_LINK", lambda:
        check_link(0, 0, 1, 1, 0, 1))
    bad = [[0] * 16, [1] * 16]
    bad[0][1] = 1
    out["nonuniform_Y"] = expect_rejection("Y_SLICE_NONUNIFORM", lambda: check_slice(bad))
    out["no_Y_slice_switch"] = expect_rejection("Y_SLICE_SWITCH", lambda:
        check_slice([[0] * 16, [0] * 16]))
    out["wrong_ell1_energy"] = expect_rejection("ENERGY72", lambda:
        check_census(0, 1, 1, 2))
    out["wrong_small_count"] = expect_rejection("SMALL_CENSUS", lambda:
        check_census(0, 0, 0, 3))
    return out


def allowed_profiles():
    projections = set()
    counts = {"singleton": 0, "plane": 0}
    for pos in range(8):
        for sign in SIGNS:
            values = [0] * 8
            values[pos] = 2 * sign
            counts[check_profile(values)] += 1
            projections.add(tuple(values[4:]))
    for positions in combinations(range(8), 4):
        x = 0
        for pos in positions:
            x ^= pos
        if x:
            continue
        for signs in product(SIGNS, repeat=4):
            if sign_product(signs) != -1:
                continue
            values = [0] * 8
            for pos, sign in zip(positions, signs):
                values[pos] = sign
            counts[check_profile(values)] += 1
            projections.add(tuple(values[4:]))
    need(counts == {"singleton": 16, "plane": 112}, "PROFILE_CENSUS")
    # Independently characterize all graph projections with entries 0,+/-1.
    for g in product((-1, 0, 1), repeat=4):
        nonzero = [x for x in g if x]
        direct = (len(nonzero) in (0, 2) or
                  (len(nonzero) == 4 and sign_product(nonzero) == -1))
        need((g in projections) == direct, "GRAPH_PROJECTION_CENSUS", repr(g))
    return projections, counts


def make_occupied_options():
    options = []
    for sig, nu, z in product(SIGNS, V, V):
        g = graph_values(sig, nu)
        eps = -(sum(g) // 2)
        need(abs(sum(g)) == 2 and eps in SIGNS, "OCCUPIED_GENERATOR")
        table = []
        for s in (0, 1):
            row = []
            for alpha in V:
                w = sum(g[b] * sgn(dot(alpha, b)) for b in V)
                numerator = w + sgn(s) * 2 * eps * sgn(dot(alpha, z))
                need(numerator % 4 == 0, "OCCUPIED_INTEGRALITY")
                row.append(numerator // 4)
            table.append(tuple(row))
        need(table[0][0] == 0 and abs(table[1][0]) == 1,
             "OCCUPIED_LAMBDA")
        for alpha in V:
            need(sorted((abs(table[0][alpha]), abs(table[1][alpha])) == [0, 1],
                 "OCCUPIED_SLICE_UNIQUENESS")
        options.append((nu, z, sig, eps, g, tuple(table)))
    need(len(options) == 32 and len({o[4] for o in options}) == 8,
         "OCCUPIED_GENERATOR_COVERAGE")
    return options


def graph_census(deadline, projections):
    options = make_occupied_options()
    balanced = tuple(product((1, 2, 3), SIGNS))
    F_tables = [F for F in product((0, 1), repeat=4) if sum(F) % 2]
    row_pairs = list(combinations(V, 2))
    counts = {"cases": 0, "parity_survivors": 0,
              "projection_survivors": 0, "same_b": 0, "different_b": 0,
              "four_graph_positive_rejected": 0}
    placements = {}
    L_seen = [0, 0, 0]
    for F in F_tables:
        for a, ap in row_pairs:
            b, bp = [i for i in V if i not in (a, ap)]
            key = "".join(map(str, F)) + ":" + str(a) + str(ap)
            placements[key] = {"total": 0, "parity": 0, "projectable": 0}
            for oa in options:
                for ob in options:
                    for c in balanced:
                        for d in balanced:
                            counts["cases"] += 1
                            placements[key]["total"] += 1
                            if counts["cases"] % 2048 == 0:
                                tick(deadline)
                            parity_ok = True
                            projectable = True
                            sign_reject = False
                            for alpha in V:
                                slices = []
                                for s in (0, 1):
                                    if s == 0 and alpha == 0:
                                        continue
                                    g = [0, 0, 0, 0]
                                    g[a] = sgn(s * F[a]) * oa[5][s][alpha]
                                    g[ap] = sgn(s * F[ap]) * ob[5][s][alpha]
                                    g[b] = sgn(s * F[b]) * c[1] * (alpha == c[0])
                                    g[bp] = sgn(s * F[bp]) * d[1] * (alpha == d[0])
                                    n = sum(x != 0 for x in g)
                                    slices.append(n)
                                    if n % 2:
                                        parity_ok = False
                                    if tuple(g) not in projections:
                                        projectable = False
                                        if n == 4 and sign_product(g) == 1:
                                            sign_reject = True
                                if alpha == 0:
                                    need(slices == [2], "LAMBDA_GRAPH_COUNT")
                                elif parity_ok:
                                    L = (alpha == c[0]) + (alpha == d[0])
                                    expected = ((0, 2), (2, 2), (2, 4))[L]
                                    need(tuple(sorted(slices)) == expected,
                                         "GRAPH_SLICE_TYPE")
                            link = (oa[1] ^ ob[1] ^ swap(oa[0] ^ ob[0]) ^
                                    swap(c[0] ^ d[0])) == 0
                            need(parity_ok == link, "GRAPH_PARITY_EQUIVALENCE")
                            if parity_ok:
                                counts["parity_survivors"] += 1
                                placements[key]["parity"] += 1
                                for alpha in (1, 2, 3):
                                    L_seen[(alpha == c[0]) + (alpha == d[0])] += 1
                            if parity_ok and sign_reject:
                                counts["four_graph_positive_rejected"] += 1
                            if projectable:
                                need(parity_ok, "PROJECTABLE_WITH_ODD_GRAPH")
                                counts["projection_survivors"] += 1
                                placements[key]["projectable"] += 1
                                counts["same_b" if oa[1] == ob[1] else "different_b"] += 1
    need(counts["cases"] == 1769472 and len(placements) == 48,
         "GRAPH_COVERAGE")
    need(all(p["total"] == 36864 for p in placements.values()),
         "PLACEMENT_COVERAGE")
    need(counts["parity_survivors"] > 0 and counts["projection_survivors"] > 0 and
         counts["same_b"] > 0 and counts["different_b"] > 0 and
         counts["four_graph_positive_rejected"] > 0 and all(L_seen),
         "GRAPH_NONVACUITY")
    return {"counts": counts, "per_F_and_row_pair": placements,
            "parity_survivor_L_occurrences": L_seen}


def e_placements():
    sites = [(i, h) for i in (1, 2, 3) for h in (0, 1)]
    shapes = {"same_E_row": 0, "different_E_rows": 0}
    for pair in combinations(sites, 2):
        check_e_sites(pair)
        shapes["same_E_row" if pair[0][0] == pair[1][0]
               else "different_E_rows"] += 1
    need(shapes == {"same_E_row": 3, "different_E_rows": 12},
         "E_PLACEMENT_COVERAGE")
    return shapes


def local_fourier():
    affine = bent = occupied_mates = other_mates = 0
    for phi, sig, alpha in product(V, SIGNS, V):
        w = sum(sig * sgn(dot(phi, b) ^ dot(alpha, b)) for b in V)
        need(w == (4 * sig if alpha == phi else 0), "AFFINE_WALSH")
        affine += 1
    for mu, sig, alpha in product(V, SIGNS, V):
        w = sum(sig * sgn(quad(b) ^ dot(mu, b) ^ dot(alpha, b)) for b in V)
        need(w == 2 * sig * sgn(quad(alpha ^ mu)), "BENT_WALSH")
        bent += 1
    for z in V:
        positions = [b for b in V if b != z]
        for signs in product(SIGNS, repeat=3):
            dvals = [0] * 4
            for b, v in zip(positions, signs):
                dvals[b] = v
            sums = [sum(dvals[b] * sgn(dot(alpha, b)) for b in V) for alpha in V]
            d = 1 if sums[0] % 4 == 1 else -1
            need(sums[0] % 4 in (1, 3), "MATE_ODD_RESIDUE")
            for alpha in V:
                need(sums[alpha] % 4 == (d * sgn(dot(alpha, z))) % 4,
                     "MATE_MISSING_POSITION_RESIDUE")
            occupied_mates += 1
    for signs in product(SIGNS, repeat=4):
        sums = [sum(signs[b] * sgn(dot(alpha, b)) for b in V) for alpha in V]
        need(sums[0] % 2 == 0 and all(x % 4 == sums[0] % 4 for x in sums),
             "FULL_MATE_RESIDUE")
        need((-sums[0]) % 4 == sums[0] % 4, "FULL_MATE_WEIGHT")
        other_mates += 1
    return {"affine_alpha_checks": affine, "bent_alpha_checks": bent,
            "three_mate_sign_rows": occupied_mates,
            "four_mate_sign_rows": other_mates}


def physical_link_census(deadline):
    total = accepted = same_b = different_b = 0
    for a, ap in combinations(V, 2):
        b, bp = [i for i in V if i not in (a, ap)]
        need((a ^ ap) == (b ^ bp) != 0, "ROW_PAIR_DIFFERENCE")
        for rho in permutations(V):
            need((rho[0] ^ rho[1] ^ rho[2] ^ rho[3]) == 0, "RHO_XOR")
            for nu0, nu1, t0, t1, z0, z1 in product(V, V, (1, 2, 3), (1, 2, 3), V, V):
                total += 1
                if total % 2048 == 0:
                    tick(deadline)
                left = z0 ^ z1 ^ swap(nu0 ^ nu1) ^ swap(t0 ^ t1)
                phi0, phi1 = rho[a] ^ nu0, rho[ap] ^ nu1
                mu0, mu1 = rho[b] ^ t0, rho[bp] ^ t1
                coefficient = z0 ^ z1 ^ swap(phi0 ^ phi1 ^ mu0 ^ mu1)
                need(left == coefficient, "PHYSICAL_PHASE_LINK")
                if left == 0:
                    accepted += 1
                    if z0 == z1:
                        same_b += 1
                    else:
                        different_b += 1
    need(total == 331776 and accepted > 0 and same_b > 0 and different_b > 0,
         "PHASE_LINK_COVERAGE")
    return {"physical_phase_cases": total, "necessary_link": accepted,
            "same_b": same_b, "different_b": different_b}


def residue_census(deadline):
    # Factorization: local_fourier covers every actual local sign array;
    # physical_link_census covers every rho, nu, theta and pair z0,z1.
    # Only z0 XOR z1 appears in the two odd-row residue product, so choosing
    # z0=0 here loses no residue case. phi and mu are over-relaxed to V^4.
    cases = cells = 0
    for F in product((0, 1), repeat=4):
        if sum(F) % 2 == 0:
            continue
        for a, ap in combinations(V, 2):
            b, bp = [i for i in V if i not in (a, ap)]
            for phi0, phi1, mu0, mu1 in product(V, repeat=4):
                z0 = 0
                z1 = swap(phi0 ^ phi1 ^ mu0 ^ mu1)
                for r, t, k in product((0, 1), repeat=3):
                    cases += 1
                    if cases % 128 == 0:
                        tick(deadline)
                    base = None
                    for s in (0, 1):
                        for alpha in V:
                            for beta in V:
                                wa = sgn(s * F[a] ^ dot(beta, a))
                                wap = sgn(s * F[ap] ^ dot(beta, ap))
                                wb = sgn(s * F[b] ^ dot(beta, b))
                                wbp = sgn(s * F[bp] ^ dot(beta, bp))
                                r0 = wb * sgn(quad(alpha ^ mu0))
                                r1 = wbp * sgn(r ^ quad(alpha ^ mu1))
                                t0 = wa * sgn(s ^ dot(alpha, z0))
                                t1 = wap * sgn(s ^ t ^ dot(alpha, z1))
                                # Graph affine signs do not matter modulo 8.
                                A = (4 * ((alpha == phi0) * wa +
                                          (alpha == phi1) * wap) +
                                     2 * (r0 + r1 + t0 + t1) + 4 * k)
                                need(A % 4 == 0, "Y_PARTIAL_MULTIPLE_FOUR")
                                bit = (A // 4) % 2
                                formula = (k + (alpha == phi0) + (alpha == phi1) +
                                           (1 + r0 * r1) // 2 +
                                           (1 + t0 * t1) // 2) % 2
                                need(bit == formula, "Y_MIXED_RESIDUE_FORMULA")
                                if base is None:
                                    base = bit
                                need(bit == (base ^ s), "Y_SLICE_CANCELLATION")
                                cells += 1
    need(cases == 98304 and cells == 3145728, "Y_RESIDUE_COVERAGE")
    return {"factorized_cases": cases, "s_alpha_beta_cells": cells,
            "full_Y_enumerated": False}


def integer_census():
    # Generate ordered full-pair values, rather than assuming a type list.
    values = (-12, -4, 4, 12)
    types = set()
    for x, y in product(values, repeat=2):
        A0, A1 = (x + y) // 2, (x - y) // 2
        small = int(abs(x) == 4) + int(abs(y) == 4)
        types.add((abs(A1), abs(A0), small))
    expected_types = {(0, 4, 2), (0, 12, 0), (4, 0, 2),
                      (4, 8, 1), (8, 4, 1), (12, 0, 0)}
    need(types == expected_types, "FULL_PAIR_TYPES")
    solutions = []
    for n in range(17):
        for m in range(17):
            for h in range(m + 1):
                for z4 in range(17 - n):
                    try:
                        check_census(n, m, h, z4)
                    except CheckFailure:
                        continue
                    solutions.append((n, m, h, z4))
    expected = {(0, 0, 0, 4), (2, 1, 1, 2),
                (4, 2, 0, 1), (4, 2, 2, 0)}
    need(set(solutions) == expected, "CENSUS_SOLUTIONS")
    need(all(m - h <= 2 for n, m, h, z4 in solutions), "ODD_SLICE_SPARSITY")
    return {"ordered_pair_count": 16, "pair_types": sorted(types),
            "solutions_n_m_H_Z4": sorted(solutions),
            "max_odd_slice_nonzero_A0": max(m - h for n, m, h, z4 in solutions)}


def main():
    deadline = time.monotonic() + SECONDS
    report = {"status": "INCOMPLETE", "scope": "FINITE_LOCAL_NECESSARY_ONLY"}
    phase = "controls"
    try:
        report["controls"] = controls()
        phase = "profiles"
        projections, report["profile_counts"] = allowed_profiles()
        phase = "E_placements"
        report["E_placements"] = e_placements()
        phase = "graph_census"
        report["graph"] = graph_census(deadline, projections)
        phase = "local_fourier"
        report["local_fourier"] = local_fourier()
        phase = "physical_link"
        report["physical_link"] = physical_link_census(deadline)
        phase = "residue"
        report["Y_residue"] = residue_census(deadline)
        phase = "integer_census"
        report["integer_census"] = integer_census()
        tick(deadline)
        report["status"] = "PASS_FINITE_LOCAL_NECESSARY_ONLY"
        report["limitations"] = [
            "Each profile is projected separately; no common ell-zero X completion enumerated.",
            "Graph/mate Y residue checks are factorized, not an enumeration of full common Y.",
            "No physical inverse, actual phase import, U3 cap, J, Z4, original caller, or global theorem is certified.",
            "Mutation controls are synthetic and do not claim physical realizability.",
        ]
        print(json.dumps(report, sort_keys=True))
        return 0
    except DeadlineReached:
        report.update(status="INCOMPLETE_DEADLINE", phase=phase)
        print(json.dumps(report, sort_keys=True))
        return 3
    except CheckFailure as exc:
        report.update(status="FAILED_CHECK", phase=phase, reason=exc.reason,
                      detail=exc.detail)
        print(json.dumps(report, sort_keys=True))
        return 2
    except Exception as exc:
        report.update(status="INCOMPLETE_EXCEPTION", phase=phase,
                      exception=type(exc).__name__, detail=str(exc))
        print(json.dumps(report, sort_keys=True))
        return 4


if __name__ == "__main__":
    sys.exit(main())
