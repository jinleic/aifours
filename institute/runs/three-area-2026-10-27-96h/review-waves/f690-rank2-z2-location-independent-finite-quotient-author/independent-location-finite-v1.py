#!/usr/bin/env python3
"""Unexecuted author source: exact rank-two location quotient, not a caller.

Python >= 3.10, standard library only. No input, network, subprocess or file
writes. The cooperative deadline is 45 seconds from process start. A COMPLETE
record is emitted only after all checks and all individual map records.
"""

import itertools
import json
import signal
import sys
import time

START = time.monotonic()
DEADLINE = START + 45.0
STOP = None
DIRECTIONS = (1, 2, 3)
ALPHAS = (1, 2, 3)


class Failure(Exception):
    pass


class Interrupted(Exception):
    pass


def need(condition, reason):
    if not condition:
        raise Failure(reason)


def on_signal(signum, _frame):
    global STOP
    STOP = "signal_" + str(signum)


def tick():
    if STOP is not None:
        raise Interrupted(STOP)
    if time.monotonic() >= DEADLINE:
        raise Interrupted("cooperative_45s_deadline")


def parity(value):
    return value.bit_count() & 1


def sign(bit):
    return 1 - 2 * bit


def character(a, b):
    return sign(parity(a & b))


def xor_all(values):
    result = 0
    for value in values:
        result ^= value
    return result


# Each ell=0 H-cell has b=0 occupied by an E point, leaving b=1,2,3.
# A pair with difference d is uniquely {p[d], p[d] XOR d}.
P = {d: min(set(DIRECTIONS) - {d}) for d in DIRECTIONS}
ACTIVE = {a: tuple(d for d in DIRECTIONS if parity(a & d)) for a in ALPHAS}


def valid_locations(loc):
    return (len(loc) == 3 and all(len(c) == 2 and 0 <= c[0] < 4 and
                                  c[1] in (0, 1) for c in loc) and
            len(set(loc)) == 3)


def check_locations(loc):
    need(valid_locations(loc), "PAIRED_HCELL_LOCATION_CAPACITY")


def level_data(delta):
    result = [None] * 4
    for alpha in ALPHAS:
        groups = []
        for s in (0, 1):
            indices = tuple(i for i in range(4)
                            if parity(alpha & delta[i]) == s)
            groups.append((indices, xor_all(indices)))
        result[alpha] = tuple(groups)
    return tuple(result)


def geometry(loc, levels, check_flat=True, alphas=ALPHAS):
    """Exactly the omega bits passing norm and, optionally, support XOR.

    Bit d-1 of omega selects the sign at p[d]. Opposite signs at the
    paired point are mandatory. Graph signs are not independently selected.
    """
    check_locations(loc)
    constraints = []
    for alpha in alphas:
        d, e = ACTIVE[alpha]
        a, _ = loc[d - 1]
        b, _ = loc[e - 1]
        (g0, x0), (g1, x1) = levels[alpha]
        if a != b:
            if len(g0) != 2 or len(g1) != 2:
                return ()
            if check_flat and (x0 != (a ^ b) or x1 != (a ^ b)):
                return ()
        else:
            # Distinct H-cells in the same L-coset have opposite e bits.
            if len(g0) == 0 and len(g1) == 4:
                singleton_s = 0
            elif len(g0) == 4 and len(g1) == 0:
                singleton_s = 1
            else:
                return ()
            required = singleton_s ^ parity(alpha & P[d]) ^ parity(alpha & P[e])
            constraints.append((d - 1, e - 1, required))
    return tuple(w for w in range(8)
                 if all(((w >> i) & 1) ^ ((w >> j) & 1) == rhs
                        for i, j, rhs in constraints))


def cell_column(loc, omega, alpha, s):
    column = [0] * 4
    for d in ACTIVE[alpha]:
        a, tau = loc[d - 1]
        bit = ((omega >> (d - 1)) & 1) ^ parity(alpha & P[d]) ^ (s & tau)
        column[a] += sign(bit)
    return column


def direct_support(loc, delta, omega, check_flat=True, alphas=ALPHAS):
    """Independently form F3's six integer columns, ignoring their signs.

    Setting the graph prefactors to +1 changes neither their magnitudes nor
    support. The pair signs and the e character remain coupled across alpha.
    """
    check_locations(loc)
    for alpha in alphas:
        for s in (0, 1):
            col = cell_column(loc, omega, alpha, s) + [
                (character(alpha, delta[i]) + sign(s)) // 2
                for i in range(4)
            ]
            if sum(v * v for v in col) != 4:
                return False
            supp = [i for i, v in enumerate(col) if v]
            if len(supp) == 1 and abs(col[supp[0]]) == 2:
                continue
            if len(supp) != 4 or any(abs(col[i]) != 1 for i in supp):
                return False
            if check_flat and xor_all(supp) != 0:
                return False
    return True


def theorem_relation(loc, delta):
    """The claimed affine relation, independent of the profile computation."""
    check_locations(loc)
    if delta[3] != (delta[0] ^ delta[1] ^ delta[2]):
        return False
    by_a = [loc[d - 1][0] for d in DIRECTIONS]
    if len(set(by_a)) == 3:
        if len(set(delta)) != 4:
            return False
        for d, e in itertools.combinations(DIRECTIONS, 2):
            v = by_a[d - 1] ^ by_a[e - 1]
            if (delta[v] ^ delta[0]) != (d ^ e):
                return False
        return True
    pair = next((d, e) for d, e in itertools.combinations(DIRECTIONS, 2)
                if by_a[d - 1] == by_a[e - 1])
    other = next(d for d in DIRECTIONS if d not in pair)
    if (pair[0] ^ pair[1]) != other:
        return False
    k = by_a[pair[0] - 1] ^ by_a[other - 1]
    image = set(delta)
    return (len(image) == 2 and xor_all(image) == other and
            delta[k] == delta[0])


def signed_equations(loc, delta, levels, omega):
    """GF(2) equations for the actual shared graph characters.

    Packed variables: bits 0..3 epsilon signs; 4+2*i,5+2*i beta_i;
    12+i theta_i. beta_i is the b-coordinate of G_i=D_i+e. theta_i is
    lambda(G_i). Their products/characters are reused in every column.
    """
    equations = [(sum(1 << i for i in range(4)), 0),
                 (sum(1 << (12 + i) for i in range(4)), 1)]
    for alpha in ALPHAS:
        for s in (0, 1):
            graph = levels[alpha][s][0]
            cells = cell_column(loc, omega, alpha, s)
            support = [a for a in range(4) if cells[a]]
            n = len(graph) + len(support)
            if n == 1:
                need(not graph and abs(cells[support[0]]) == 2,
                     "SINGLETON_SHAPE")
                continue
            need(n == 4 and all(abs(cells[a]) == 1 for a in support),
                 "FOUR_PROFILE_SHAPE")
            need(xor_all(support + [4 + i for i in graph]) == 0,
                 "FOUR_PROFILE_XOR")
            mask = 0
            constant = (s * len(graph)) & 1
            for a in support:
                constant ^= int(cells[a] < 0)
            for i in graph:
                mask ^= 1 << i
                if alpha & 1:
                    mask ^= 1 << (4 + 2 * i)
                if alpha & 2:
                    mask ^= 1 << (5 + 2 * i)
                if s:
                    mask ^= 1 << (12 + i)
            equations.append((mask, 1 ^ constant))
    return equations


def solve_equations(equations):
    """Exact row elimination; return count, one solution, or a contradiction."""
    pivots = {}
    for number, (original_mask, original_rhs) in enumerate(equations):
        mask, rhs, combination = original_mask, original_rhs, 1 << number
        while mask:
            low = (mask & -mask).bit_length() - 1
            if low not in pivots:
                pivots[low] = (mask, rhs, combination)
                break
            pm, pr, pc = pivots[low]
            mask ^= pm
            rhs ^= pr
            combination ^= pc
        if not mask and rhs:
            cm = cr = 0
            for i, (m, r) in enumerate(equations):
                if (combination >> i) & 1:
                    cm ^= m
                    cr ^= r
            need(cm == 0 and cr == 1, "BAD_CONTRADICTION_CERTIFICATE")
            return 0, None, combination, len(pivots)
    solution = 0
    for low in sorted(pivots, reverse=True):
        mask, rhs, _ = pivots[low]
        if rhs ^ parity(mask & solution):
            solution |= 1 << low
    need(all(parity(mask & solution) == rhs for mask, rhs in equations),
         "BAD_LINEAR_SOLUTION")
    return 1 << (16 - len(pivots)), solution, None, len(pivots)


def unpack(solution):
    eps = [sign((solution >> i) & 1) for i in range(4)]
    beta = [((solution >> (4 + 2 * i)) & 1) |
            (((solution >> (5 + 2 * i)) & 1) << 1) for i in range(4)]
    theta = [(solution >> (12 + i)) & 1 for i in range(4)]
    return eps, beta, theta


def profile_ok(col):
    supp = [i for i, v in enumerate(col) if v]
    if len(supp) == 1:
        return abs(col[supp[0]]) == 2
    if len(supp) != 4 or any(abs(col[i]) != 1 for i in supp):
        return False
    product = 1
    for i in supp:
        product *= col[i]
    return xor_all(supp) == 0 and product == -1


def signed_columns(loc, delta, omega, solution):
    eps, beta, theta = unpack(solution)
    columns = {}
    columns[(0, 0)] = [0] * 8
    columns[(0, 1)] = [0] * 4 + [
        -eps[i] * sign(theta[i]) for i in range(4)
    ]
    for alpha in ALPHAS:
        for s in (0, 1):
            columns[(alpha, s)] = cell_column(loc, omega, alpha, s) + [
                eps[i] * character(alpha, beta[i]) * sign(s & theta[i]) *
                ((character(alpha, delta[i]) + sign(s)) // 2)
                for i in range(4)
            ]
    return columns


def validate_signed(loc, delta, omega, solution):
    cols = signed_columns(loc, delta, omega, solution)
    need(all(profile_ok(cols[key]) for key in cols if key != (0, 0)),
         "SHARED_SIGN_CHARACTER_PROFILE")


def walsh(values):
    n = len(values)
    return [sum(values[x] * character(a, x) for x in range(n))
            for a in range(n)]


def integer_column_census():
    total = passed = singleton = four = 0
    flats = set()
    for i in range(8):
        for value in (-2, 2):
            col = [0] * 8
            col[i] = value
            total += 1
            good = all(abs(x) == 2 for x in walsh(col))
            need(good == profile_ok(col), "SINGLETON_WALSH_CRITERION")
            passed += int(good)
            singleton += int(good)
    for supp in itertools.combinations(range(8), 4):
        for values in itertools.product((-1, 1), repeat=4):
            col = [0] * 8
            for i, value in zip(supp, values):
                col[i] = value
            total += 1
            good = all(abs(x) == 2 for x in walsh(col))
            need(good == profile_ok(col), "FOUR_WALSH_FLAT_SIGN_CRITERION")
            if good:
                passed += 1
                four += 1
                flats.add(supp)
    need((total, passed, singleton, four, len(flats)) == (1136, 128, 16, 112, 14),
         "INTEGER_PROFILE_CENSUS")
    # Omitting the ell character maps frequency 4 to frequency 0 incorrectly.
    col = [1, -1, 0, 0, 1, 1, 0, 0]
    spectrum = walsh(col)
    need(profile_ok(col) and spectrum[0] == 2 and spectrum[4] == -2,
         "ELL_CHARACTER_NEGATIVE_CONTROL")
    return {"total": total, "passed": passed, "singletons": singleton,
            "four_entries": four, "affine_flats": len(flats),
            "ell_control_w0_well": [spectrum[0], spectrum[4]]}


def pack(eps, beta, theta):
    result = 0
    for i in range(4):
        result |= int(eps[i] == -1) << i
        result |= (beta[i] & 1) << (4 + 2 * i)
        result |= ((beta[i] >> 1) & 1) << (5 + 2 * i)
        result |= theta[i] << (12 + i)
    return result


def physical_x(loc, delta, omega, solution):
    """Canonical K=b-plane, t=0: c=(m<<3)|(h<<2)|b, m=4*ell+j."""
    check_locations(loc)
    eps, beta, theta = unpack(solution)
    x = [0] * 64
    for i in range(4):
        m = 4 + i
        exception = beta[i] ^ delta[i]
        for b in range(4):
            x[(m << 3) | (theta[i] << 2) | b] = eps[i] * (
                2 * int(b == exception) - 1)
        x[(m << 3) | ((theta[i] ^ 1) << 2) | beta[i]] = 2 * eps[i]
    for d in DIRECTIONS:
        a, h = loc[d - 1]
        first = (a << 3) | (h << 2) | P[d]
        second = (a << 3) | (h << 2) | (P[d] ^ d)
        need(x[first] == 0 and x[second] == 0, "PHYSICAL_CELL_COLLISION")
        x[first] = 2 * sign((omega >> (d - 1)) & 1)
        x[second] = -x[first]
    return x


def physical_example():
    # Fresh explicit x, f and r; not an even-half or Boolean witness.
    loc = ((1, 0), (2, 0), (3, 0))
    delta = (0, 1, 2, 3)
    eps, beta, theta = [1, -1, 1, -1], [0, 0, 0, 3], [1, 1, 1, 0]
    omega = 0
    solution = pack(eps, beta, theta)
    levels = level_data(delta)
    need(omega in geometry(loc, levels), "EXAMPLE_SUPPORT")
    need(all(parity(mask & solution) == rhs for mask, rhs in
             signed_equations(loc, delta, levels, omega)), "EXAMPLE_SIGN_EQUATIONS")
    validate_signed(loc, delta, omega, solution)
    x = physical_x(loc, delta, omega, solution)
    f = [theta[z >> 2] for z in range(16)]
    r = [parity((z >> 2) & (z & 3)) for z in range(16)]
    q = [1 ^ ((z & 1) & ((z >> 1) & 1)) for z in range(16)]
    for z in range(16):
        for w in range(16):
            j, k = z >> 2, w >> 2
            polar = f[z ^ w] ^ f[z] ^ f[w] ^ f[0]
            expected = ((j & 1) & ((k >> 1) & 1)) ^ (((j >> 1) & 1) & (k & 1))
            need(polar == expected, "EXAMPLE_F_POLAR_RANK2")
    for truth in ([f[i] ^ q[i] for i in range(16)], r,
                  [r[i] ^ f[i] for i in range(16)]):
        need(all(abs(v) == 4 for v in walsh([sign(z) for z in truth])),
             "EXAMPLE_BENT")
    a = [0] * 64
    g = [0] * 64
    graph = []
    for c in range(64):
        m, v = c >> 3, c & 7
        ell, j, h, b = m >> 2, m & 3, v >> 2, v & 3
        if ell:
            on_graph = h == theta[j]
            if on_graph:
                graph.append(c)
                a[c] = sign(r[(j << 2) | b])
            rho = sign(q[(j << 2) | b])
            g[c] = rho * (1 if on_graph else -2)
        elif b == 0:
            g[c] = 4 if j == 0 else -2
    ahat, ghat, xhat = walsh(a), walsh(g), walsh(x)
    need(all(abs(v) == 4 for v in ahat), "EXAMPLE_A_64")
    need(sum(v == 4 for v in ghat) == 4 and
         sum(abs(v) == 12 for v in ghat) == 60, "EXAMPLE_G_64")
    need(sum(v * v for v in x) == 56 and len(graph) == 16,
         "EXAMPLE_U0_ENERGY_AND_GRAPH")
    need(xhat[0] == 0 and xhat.count(0) == 8 and
         all(v in (-8, 0, 8) for v in xhat), "EXAMPLE_U0_ALL64")
    columns = signed_columns(loc, delta, omega, solution)
    for alpha in range(4):
        for s in (0, 1):
            eta = alpha | (s << 2)
            numerators = [sum(x[(m << 3) | v] * character(eta, v)
                              for v in range(8)) for m in range(8)]
            need(all(n % 4 == 0 for n in numerators), "EXAMPLE_PROFILE_INTEGRAL")
            need([n // 4 for n in numerators] == columns[(alpha, s)],
                 "EXAMPLE_F3_DIRECT")
            for mu in range(8):
                quotient = sum(columns[(alpha, s)][m] * character(mu, m)
                               for m in range(8))
                need(xhat[(mu << 3) | eta] == 4 * quotient,
                     "EXAMPLE_NORMALIZATION_FOUR")
    need(any(xhat[(mu << 3) | eta] != 2 * sum(
        columns[(eta & 3, eta >> 2)][m] * character(mu, m) for m in range(8))
        for eta in range(8) for mu in range(8)), "WRONG_NORMALIZATION_CONTROL")
    Pneg = [c for c in graph if x[c] < 0]
    W = [c for c in range(64) if abs(x[c]) == 2]
    Nneg = [c for c in W if x[c] < 0]
    need(len(W) == 10 and len(Pneg) % 2 == 0 and
         (len(Pneg) // 2 + len(Nneg)) % 2 == 1 and
         xor_all(Pneg) == xor_all(W), "EXAMPLE_DIVISIBILITY_XOR")
    physical_exceptions = [beta[i] ^ delta[i] for i in range(4)]
    need(len(set(delta)) == 4 and len(set(physical_exceptions)) < 4,
         "DELTA_VERSUS_PHYSICAL_EXCEPTION_CONTROL")
    return {"kind": "actual_canonical_graph_u0_illustration", "t": 0,
            "f_formula": "1 XOR j0*j1", "r_formula": "j0*b0 XOR j1*b1",
            "coordinates": "c=((4*ell+j)<<3)|(h<<2)|b; z=(j<<2)|b",
            "locations_by_direction_1_2_3": loc, "delta": delta,
            "epsilon": eps, "beta_D_mates": beta, "theta": theta,
            "omega_bits": omega, "physical_exception_b": physical_exceptions,
            "f_truth_16": f, "r_truth_16": r, "x_64": x, "xhat_64": xhat,
            "a_hat_64": ahat, "g_hat_64": ghat,
            "P_count": len(Pneg), "N_count": len(Nneg),
            "status": "U0_ILLUSTRATION_ONLY_Y_U_V_CALLER_NOTTESTED"}


def guard_caller(state):
    required = ("same_physical_u", "actual_y_and_J", "all_u3_caps",
                "specified_original_t", "same_140_point_complement",
                "all_odd_caps_and_parity", "original_T_rank_atoms_inverse")
    need(all(state.get(key) is True for key in required), "FALSE_CALLER_CLAIM")


def negative_controls():
    distinct = ((1, 0), (2, 0), (3, 0))
    swapped = (0, 2, 1, 3)
    need(geometry(distinct, level_data(swapped), check_flat=False) and
         not geometry(distinct, level_data(swapped)), "MISSING_FLAT_XOR_CONTROL")
    one_alpha = (0, 1, 0, 1)
    need(geometry(distinct, level_data(one_alpha), alphas=(1,)) and
         not geometry(distinct, level_data(one_alpha)), "ALL_ALPHA_CONTROL")
    collision = ((0, 0), (0, 0), (1, 0))
    try:
        check_locations(collision)
    except Failure as error:
        need(str(error) == "PAIRED_HCELL_LOCATION_CAPACITY", "CAPACITY_WRONG_REASON")
    else:
        raise Failure("CAPACITY_MUTANT_ACCEPTED")
    need(bool({P[1], P[1] ^ 1} & {P[2], P[2] ^ 2}),
         "THREE_Z_POINTS_CAPACITY_CONTROL")
    paired = ((0, 0), (0, 1), (1, 0))
    wrong_kernel = (0, 3, 0, 3)
    need(wrong_kernel[0] == wrong_kernel[2] and
         wrong_kernel[0] != wrong_kernel[1] and
         geometry(paired, level_data(wrong_kernel), check_flat=False) and
         not geometry(paired, level_data(wrong_kernel)), "WRONG_KERNEL_CONTROL")
    try:
        guard_caller({"quotient_profiles": True})
    except Failure as error:
        need(str(error) == "FALSE_CALLER_CLAIM", "CALLER_GUARD_WRONG_REASON")
    else:
        raise Failure("FALSE_CALLER_MUTANT_ACCEPTED")
    return ["missing_flat_xor", "all_alpha", "paired_H_cell_location_capacity",
            "wrong_kernel", "delta_vs_physical_exception_in_example",
            "false_caller_claim", "normalization_four_in_example", "ell_character"]


def emit(record):
    print(json.dumps(record, sort_keys=True, separators=(",", ":")))


def main():
    signal.signal(signal.SIGINT, on_signal)
    signal.signal(signal.SIGTERM, on_signal)
    tick()
    census = integer_column_census()
    controls = negative_controls()
    example = physical_example()
    maps = tuple(itertools.product(range(4), repeat=4))
    levels_by_map = {delta: level_data(delta) for delta in maps}
    cells = tuple(itertools.product(range(4), range(2)))
    counts = {kind: {"locations": 0, "maps_examined": 0,
                     "support_maps": 0, "support_omega_tuples": 0,
                     "signed_maps": 0, "signed_omega_tuples": 0,
                     "signed_graph_assignments": 0}
              for kind in ("1+1+1", "2+1")}
    records = []
    direct_comparisons = 0
    for loc in itertools.permutations(cells, 3):
        tick()
        by_a = [loc[d - 1][0] for d in DIRECTIONS]
        kind = "1+1+1" if len(set(by_a)) == 3 else "2+1"
        counts[kind]["locations"] += 1
        # In the distinct case support ignores omega; in the paired case it
        # depends only on the XOR of the two colliding-cell sign bits.
        if kind == "1+1+1":
            representatives = (0,)
        else:
            first = next(d for d, e in itertools.combinations(DIRECTIONS, 2)
                         if by_a[d - 1] == by_a[e - 1])
            representatives = (0, 1 << (first - 1))
        for number, delta in enumerate(maps):
            if number % 32 == 0:
                tick()
            counts[kind]["maps_examined"] += 1
            levels = levels_by_map[delta]
            allowed = geometry(loc, levels)
            need(bool(allowed) == theorem_relation(loc, delta),
                 "LOCATION_RELATION_MISMATCH")
            for omega in representatives:
                need(direct_support(loc, delta, omega) == (omega in allowed),
                     "F3_DIRECT_SUPPORT_MISMATCH")
                direct_comparisons += 1
            if not allowed:
                continue
            counts[kind]["support_maps"] += 1
            counts[kind]["support_omega_tuples"] += len(allowed)
            outcomes = []
            map_signed = False
            for omega in allowed:
                equations = signed_equations(loc, delta, levels, omega)
                number_solutions, representative, contradiction, rank = solve_equations(equations)
                if number_solutions:
                    validate_signed(loc, delta, omega, representative)
                    counts[kind]["signed_omega_tuples"] += 1
                    counts[kind]["signed_graph_assignments"] += number_solutions
                    map_signed = True
                outcomes.append({"omega": omega, "solutions": number_solutions,
                                 "rank": rank, "representative_bits": representative,
                                 "contradiction_equation_mask": contradiction})
            counts[kind]["signed_maps"] += int(map_signed)
            records.append({"kind": "allowed_support_map", "multiplicity": kind,
                            "locations_d1_d2_d3": loc, "delta_on_m1_0_1_2_3": delta,
                            "signed_omega_outcomes": outcomes})
    need(counts["1+1+1"]["locations"] == 192 and
         counts["2+1"]["locations"] == 144, "LOCATION_CENSUS")
    need(counts["1+1+1"]["maps_examined"] == 192 * 256 and
         counts["2+1"]["maps_examined"] == 144 * 256, "ALL_256_MAPS")
    need(counts["1+1+1"]["support_maps"] == 768 and
         counts["2+1"]["support_maps"] == 576 and
         counts["1+1+1"]["support_omega_tuples"] == 6144 and
         counts["2+1"]["support_omega_tuples"] == 2304,
         "SUPPORT_CERTIFICATE_CENSUS")
    need(direct_comparisons == 192 * 256 + 144 * 256 * 2,
         "DIRECT_SUPPORT_COMPARISON_CENSUS")
    tick()
    emit({"kind": "header", "status": "IN_PROGRESS",
          "scope": "finite quotient, same weighted signs, not full caller",
          "child_execution": "parent_run_only_if_admitted",
          "maps_per_location": 256, "integer_column_census": census,
          "controls": controls, "direct_support_comparisons": direct_comparisons})
    emit(example)
    for i, record in enumerate(records):
        if i % 8 == 0:
            tick()
        emit(record)
    tick()
    emit({"kind": "summary", "status": "COMPLETE_QUOTIENT_ONLY", "counts": counts,
          "map_records": len(records), "elapsed_seconds": time.monotonic() - START,
          "actual_y_J_u3": "NOTTESTED", "complement_v_odd_caps": "NOTTESTED",
          "original_T_rank_atoms_boolean_caller": "NOTTESTED"})


if __name__ == "__main__":
    try:
        main()
    except Interrupted as error:
        emit({"kind": "termination", "status": "INCOMPLETE", "reason": str(error)})
        sys.exit(2)
    except Failure as error:
        emit({"kind": "termination", "status": "FAIL", "reason": str(error)})
        sys.exit(1)
