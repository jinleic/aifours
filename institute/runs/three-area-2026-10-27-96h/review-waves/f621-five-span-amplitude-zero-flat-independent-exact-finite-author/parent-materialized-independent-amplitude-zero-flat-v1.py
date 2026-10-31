#!/usr/bin/env python3
import json
import sys
from itertools import combinations, product


class CheckFailure(Exception):
    pass


def need(condition, reason):
    if not condition:
        raise CheckFailure(reason)


def must_reject(action, reason):
    try:
        action()
    except CheckFailure as exc:
        if str(exc) != reason:
            raise
        return reason
    raise CheckFailure("MUTANT_ACCEPTED:" + reason)


def chi(a, b):
    return 1 - 2 * ((a & b).bit_count() & 1)


def walsh(values):
    out = list(values)
    n = len(out)
    step = 1
    while step < n:
        for base in range(0, n, 2 * step):
            for j in range(step):
                a, b = out[base + j], out[base + j + step]
                out[base + j] = a + b
                out[base + j + step] = a - b
        step *= 2
    return out


def anf(truth_mask, n):
    out = truth_mask
    for i in range(n):
        step = 1 << i
        upper = sum(1 << x for x in range(1 << n) if x & step)
        out ^= (out << step) & upper
    return out


def high_terms(n, degree):
    return sum(1 << m for m in range(1 << n) if m.bit_count() > degree)


def values(mask):
    return [v for v in range(64) if (mask >> v) & 1]


def coset_mask(direction, t):
    return sum(1 << (t ^ v) for v in direction)


def perpendicular(direction):
    return sum(1 << v for v in range(64)
               if all(((v & k).bit_count() & 1) == 0 for k in direction))


def rank_binary(rows):
    basis = [0] * 4
    for original in rows:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if basis[pivot]:
                row ^= basis[pivot]
            else:
                basis[pivot] = row
                break
    return sum(bool(row) for row in basis)


def polar_rows(f):
    rows = [0] * 4
    bit0 = f & 1
    for i in range(4):
        for j in range(i + 1, 4):
            bij = (bit0 ^ ((f >> (1 << i)) & 1)
                   ^ ((f >> (1 << j)) & 1)
                   ^ ((f >> ((1 << i) | (1 << j))) & 1))
            rows[i] |= bij << j
            rows[j] |= bij << i
    return rows


def physical(c):
    ell = c & 1
    h0 = (c >> 1) & 1
    j = (c >> 2) & 3
    b = (c >> 4) & 3
    b0, b1 = b & 1, (b >> 1) & 1
    d = (ell ^ b0 ^ b1) | (b0 << 1) | (b1 << 2)
    h = h0 | (j << 1)
    return h | (d << 3)


def graph_support(f):
    support = 0
    physical_expected = set()
    db = (1, 2, 4, 7)
    for j in range(4):
        for b in range(4):
            h0 = (f >> (j | (b << 2))) & 1
            c = 1 | (h0 << 1) | (j << 2) | (b << 4)
            support |= 1 << c
            physical_expected.add((2 * j + h0) | (db[b] << 3))
    need(support.bit_count() == 16, "GRAPH_WEIGHT")
    need({physical(c) for c in values(support)} == physical_expected,
         "ACTUAL_PHYSICAL_GRAPH")
    for c in range(64):
        ell, h0 = c & 1, (c >> 1) & 1
        fc = (f >> ((c >> 2) & 15)) & 1
        need(((support >> c) & 1) == (ell & (1 ^ h0 ^ fc)),
             "GRAPH_INDICATOR_COORDINATES")
    return support


def quad(c):
    answer = 0
    for i in range(3):
        answer ^= ((c >> i) & 1) & ((c >> (i + 3)) & 1)
    return answer


def minimum_weight_models():
    result = []
    for n in range(5):
        for d in range(min(n, 2) + 1):
            mons = [m for m in range(1 << n) if m.bit_count() <= d]
            terms = [sum(1 << c for c in range(1 << n) if (c & m) == m)
                     for m in mons]
            checked = 0
            equalities = 0
            for selector in range(1 << len(mons)):
                truth = 0
                for i, term in enumerate(terms):
                    if (selector >> i) & 1:
                        truth ^= term
                need((anf(truth, n) & high_terms(n, d)) == 0,
                     "SMALL_MODEL_DEGREE")
                if not truth:
                    continue
                checked += 1
                points = [c for c in range(1 << n) if (truth >> c) & 1]
                minimum = 1 << (n - d)
                need(len(points) >= minimum, "SMALL_MODEL_MINIMUM_WEIGHT")
                if len(points) == minimum:
                    equalities += 1
                    base = points[0]
                    direction = {p ^ base for p in points}
                    need(all((a ^ b) in direction
                             for a in direction for b in direction),
                         "SMALL_MODEL_EQUALITY_NOT_AFFINE")
            result.append({"n": n, "d": d, "nonzero": checked,
                           "minimum_weight_equalities": equalities})
    return result


def main():
    need(len(sys.argv) == 1, "NO_PROGRAM_ARGUMENTS")
    high4 = high_terms(4, 2)
    bent = []
    for truth in range(1 << 16):
        signs = [1 - 2 * ((truth >> c) & 1) for c in range(16)]
        if all(abs(w) == 4 for w in walsh(signs)):
            need((anf(truth, 4) & high4) == 0, "BENT_NOT_QUADRATIC")
            bent.append(truth)
    bent_set = set(bent)
    need(len(bent) == 896, "BENT_CENSUS")
    q = sum(1 << c for c in range(16)
            if not (((c >> 2) & 1) and ((c >> 3) & 1)))
    graph_tables = sorted(r ^ q for r in bent)
    need(len(set(graph_tables)) == 896, "GRAPH_CENSUS")

    spaces = set()
    for a, b, c in combinations(range(1, 64), 3):
        if (a ^ b) == c:
            continue
        points = (0, a, b, c, a ^ b, a ^ c, b ^ c, a ^ b ^ c)
        spaces.add(sum(1 << p for p in points))
    need(len(spaces) == 1395, "LINEAR_THREE_SPACE_CENSUS")
    spaces = sorted(spaces)
    spaces_set = set(spaces)
    high6 = high_terms(6, 2)
    signatures = [(space, anf(space, 6) & high6) for space in spaces]
    need(all(sig for _, sig in signatures), "THREE_SPACE_SIGNATURE_ZERO")
    need(len({sig for _, sig in signatures}) == 1395,
         "THREE_SPACE_SIGNATURE_NOT_UNIQUE")

    graphs = []
    comparison_count = 0
    phase_total = 0
    for f in graph_tables:
        rows = polar_rows(f)
        rank = rank_binary(rows)
        need(rank in (2, 4), "GRAPH_POLAR_RANK")
        support = graph_support(f)
        ws = walsh([(support >> c) & 1 for c in range(64)])
        gamma = int(rank == 4)
        for xi in range(64):
            need(ws[xi] % 8 == 4 * gamma * ((xi >> 1) & 1),
                 "GRAPH_WALSH_CONGRUENCE")
        phases = sum((r ^ f) in bent_set for r in bent)
        need(phases == 384, "COMMON_PHASE_COUNT")
        phase_total += phases
        signature = anf(support, 6) & high6
        matching = [space for space, sig in signatures if sig == signature]
        comparison_count += len(signatures)
        if rank == 4:
            need(not matching, "RANK_FOUR_HAS_MATCH")
            direction = None
        else:
            need(len(matching) == 1, "RANK_TWO_NOT_UNIQUE")
            direction = matching[0]
            formula = sum(1 << c for c in range(64)
                          if (c & 1) == 0 and
                          all(((row & (c >> 2)).bit_count() & 1) == 0
                              for row in rows))
            need(direction == formula, "RANK_TWO_FORMULA")
            need((anf(support ^ direction, 6) & high6) == 0,
                 "DIRECT_ANF_CANCELLATION")
            need((direction >> 2) & 1, "PRIMAL_FULL_BLOCK_E_NOT_IN_L")
        graphs.append({"f": f, "rank": rank, "S": support,
                       "L": direction, "phases": phases})
    rank2 = [g for g in graphs if g["rank"] == 2]
    rank4 = [g for g in graphs if g["rank"] == 4]
    need((len(rank2), len(rank4)) == (512, 384), "RANK_CENSUS")
    need(phase_total == 344064, "PHASE_PAIR_CENSUS")
    need(comparison_count == 896 * 1395, "SIGNATURE_COMPARISON_CENSUS")

    all_flats = set()
    for k_mask in spaces:
        kvals = values(k_mask)
        l_mask = perpendicular(kvals)
        need(l_mask in spaces_set, "DUAL_PERP_NOT_THREE_SPACE")
        this_cosets = set()
        for t in range(64):
            if t != min(t ^ k for k in kvals):
                continue
            flat = coset_mask(kvals, t)
            need(flat not in all_flats, "DUPLICATE_AFFINE_FLAT")
            all_flats.add(flat)
            this_cosets.add(flat)
            for v in range(64):
                observed = sum(chi(t ^ k, v) for k in kvals)
                expected = 8 * chi(t, v) if (l_mask >> v) & 1 else 0
                need(observed == expected, "AFFINE_FLAT_CHARACTER_TRANSFORM")
        need(len(this_cosets) == 8, "AFFINE_COSETS_PER_DIRECTION")
    need(len(all_flats) == 11160, "AFFINE_FLAT_CENSUS")

    balance_trials = 0
    for g in rank2:
        l_mask = g["L"]
        lvals = values(l_mask)
        k_mask = perpendicular(lvals)
        kvals = values(k_mask)
        need(k_mask in spaces_set and len(kvals) == 8, "GRAPH_DUAL_DIRECTION")
        cosets = {}
        for t in range(64):
            flat = coset_mask(kvals, t)
            need((flat >> t) & 1, "SPECIFIC_BALANCE_NOT_IN_ZERO_FLAT")
            cosets[flat] = cosets.get(flat, 0) + 1
            corr = [64 * int(v == 0)
                    - (8 * chi(t, v) if (l_mask >> v) & 1 else 0)
                    for v in range(64)]
            spectrum_square = walsh(corr)
            need(all(spectrum_square[xi] == 64 * (1 - ((flat >> xi) & 1))
                     for xi in range(64)), "CORRELATION_SPECTRAL_IDENTITY")
            balance_trials += 1
        need(len(cosets) == 8 and all(count == 8 for count in cosets.values()),
             "GRAPH_CARRIED_FREQUENCY_COSETS")
    need(balance_trials == 512 * 64, "BALANCE_TRIAL_CENSUS")

    # An independently specified positive integer roundtrip, NOT a caller.
    k_positive = list(range(8))
    t_positive = 8
    flat_positive = coset_mask(k_positive, t_positive)
    l_positive = perpendicular(k_positive)
    x = [(0 if (c & 7) == 1 else 1 - 2 * quad(c)) for c in range(64)]
    z = [(0 if (flat_positive >> xi) & 1 else 1 - 2 * quad(xi))
         for xi in range(64)]
    wx = walsh(x)
    need(wx == [8 * a for a in z], "POSITIVE_WALSH_ROUNDTRIP_X")
    need(walsh(z) == [8 * a for a in x], "POSITIVE_WALSH_ROUNDTRIP_Z")
    need(sum(a * a for a in x) == 56, "POSITIVE_ENERGY")
    need(sum(a & 1 for a in x) == 56, "POSITIVE_NOT_ACTUAL_ODD_SUPPORT")
    need(z[t_positive] == 0 and z[0] != 0, "POSITIVE_BALANCE_CONTROL")
    actual_corr = [sum(x[c] * x[c ^ v] for c in range(64)) for v in range(64)]
    predicted_corr = [64 * int(v == 0)
                      - (8 * chi(t_positive, v) if (l_positive >> v) & 1 else 0)
                      for v in range(64)]
    need(actual_corr == predicted_corr, "POSITIVE_DIRECT_AUTOCORRELATION")
    negative = [int(a == -1) for a in z]
    wnegative = walsh(negative)
    need(all(a % 4 == 0 for a in wnegative), "NEGATIVE_SPECTRUM_DIVISIBLE_FOUR")

    def parity_division(divisor):
        need(all(((wnegative[c] // divisor) & 1)
                 == ((x[c] & 1) ^ ((l_positive >> c) & 1))
                 for c in range(64)), "PARITY_DIVISION_FOUR")

    parity_division(4)
    mutants = [must_reject(lambda: parity_division(2), "PARITY_DIVISION_FOUR")]

    def carried_balance(t):
        need(z[t] == 0, "CARRIED_BALANCE_ZERO")

    carried_balance(t_positive)
    # 8 is a real zero; replacing the carried value 0 by that zero is invalid.
    mutants.append(must_reject(lambda: carried_balance(0), "CARRIED_BALANCE_ZERO"))

    first_l = rank2[0]["L"]
    first_k = perpendicular(values(first_l))

    def direction_check(flat):
        need(flat == coset_mask(values(first_k), 0), "PRIMAL_DUAL_DIRECTION")

    direction_check(coset_mask(values(first_k), 0))
    mutants.append(must_reject(lambda: direction_check(first_l),
                               "PRIMAL_DUAL_DIRECTION"))

    def scope_guard(label):
        need(label == "normalized_graph_necessary_interface_only",
             "SCOPE_NOT_ACTUAL_CALLERS")

    scope_guard("normalized_graph_necessary_interface_only")
    mutants.append(must_reject(lambda: scope_guard("all_384_are_actual_callers"),
                               "SCOPE_NOT_ACTUAL_CALLERS"))

    v4 = [int((c & 3) == 3) for c in range(16)]
    v4truth = sum(a << c for c, a in enumerate(v4))
    v4anf = anf(v4truth, 4)
    degree = max(m.bit_count() for m in range(16) if (v4anf >> m) & 1)
    need(degree == 2 and all(w % 4 == 0 for w in walsh(v4)),
         "SHARP_N_MINUS_K_POSITIVE")
    mutants.append(must_reject(lambda: need(degree <= 1, "N_MINUS_K_TOO_STRONG"),
                               "N_MINUS_K_TOO_STRONG"))
    # A looser bound is not false; it cannot provide the claimed sharp step.
    mutants.append(must_reject(lambda: need(3 == 4 - 2, "N_MINUS_K_STRENGTH_GUARD"),
                               "N_MINUS_K_STRENGTH_GUARD"))
    v3 = [int((c & 7) == 7) for c in range(16)]
    need(any(w % 4 for w in walsh(v3)), "CUBIC_NOT_DIVISIBLE_CONTROL")

    wrong_character = [64 * int(v == 0)
                       - (8 * chi(0, v) if (l_positive >> v) & 1 else 0)
                       for v in range(64)]
    mutants.append(must_reject(
        lambda: need(wrong_character == actual_corr, "WRONG_CORRELATION_CHARACTER"),
        "WRONG_CORRELATION_CHARACTER"))
    wrong_constant = [63 * int(v == 0)
                      - (8 * chi(t_positive, v) if (l_positive >> v) & 1 else 0)
                      for v in range(64)]
    mutants.append(must_reject(
        lambda: need(wrong_constant == actual_corr, "WRONG_CORRELATION_64"),
        "WRONG_CORRELATION_64"))

    eligible = []
    for block in product((-1, 0, 1), repeat=4):
        uhat = walsh(block)
        for w in range(4):
            need(sum(uhat[k] * chi(k, w) for k in range(4)) == 4 * block[w],
                 "FOUR_FIBRE_INVERSE")
        if abs(uhat[1]) == 3:
            a = uhat[1] // 3
            need(abs(uhat[0]) == 1 and abs(uhat[2]) == 1,
                 "FOUR_FIBRE_S_SUPPORT")
            need(uhat[3] == -a * uhat[2] * uhat[0], "FOUR_FIBRE_S_SIGN")
            eligible.append(uhat)
    need(len(eligible) == 8, "FOUR_FIBRE_S_CENSUS")
    first = eligible[0]
    mutants.append(must_reject(
        lambda: need(first[3] == (first[1] // 3) * first[2] * first[0],
                     "FOUR_FIBRE_WRONG_SIGN"), "FOUR_FIBRE_WRONG_SIGN"))

    small = minimum_weight_models()
    output = {
        "status": "FINITE_CHECKS_COMPLETED_NOT_A_CALLER_OR_UNIVERSAL_PROOF",
        "truth_tables": 65536,
        "bent_tables": len(bent),
        "graph_rank_counts": {"2": len(rank2), "4": len(rank4)},
        "graph_phase_pairs": phase_total,
        "linear_three_spaces": len(spaces),
        "graph_subspace_signature_comparisons": comparison_count,
        "affine_three_flats": len(all_flats),
        "flat_character_values_checked": len(all_flats) * 64,
        "rank2_graph_balance_trials": balance_trials,
        "rank2_balance_spectral_values_checked": balance_trials * 64,
        "graphs": [{"f_truth_hex": hex(g["f"]), "rank": g["rank"],
                    "physical_coordinate_S_mask_hex": hex(g["S"]),
                    "matched_primal_L_mask_hex": None if g["L"] is None
                    else hex(g["L"]), "common_phases": g["phases"]}
                   for g in graphs],
        "positive_not_caller": {"t": t_positive,
                                "dual_K": k_positive,
                                "primal_L": values(l_positive),
                                "x": x, "z": z, "walsh_x": wx,
                                "autocorrelation": actual_corr,
                                "odd_support": sum(a & 1 for a in x),
                                "required_actual_odd_support": 16},
        "small_degree_models": small,
        "ternary_four_fibre_blocks": 81,
        "four_fibre_S_cases": len(eligible),
        "intended_reason_mutations": mutants,
        "unpaid": ["original physical caller", "all U3 constraints",
                   "complementary odd half", "universal minimum-weight lemma",
                   "independent-family review", "human/kernel/novelty/global NL242"]
    }
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
