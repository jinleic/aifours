from collections import Counter
from fractions import Fraction
from math import gcd
from time import perf_counter

HEAD = (0, 3, 8, 11)
TAIL = (0, 1, 7, 13, 14)
LIMIT_SECONDS = 55.0


class CheckError(Exception):
    pass


def need(condition, reason):
    if not condition:
        raise CheckError(reason)


def guard(start):
    need(perf_counter() - start < LIMIT_SECONDS, "LIMIT_55_SECONDS")


def sums_mod(A, B, modulus):
    return {(a + b) % modulus for a in A for b in B}


def support_shadow(g, V, C, Q):
    m = 2 * g
    V, C, Q = set(V), set(C), set(Q)
    universe = set(range(m))
    need(V <= universe and C <= universe and Q <= universe,
         "SUPPORT_RANGE")
    need(len(V) == g, "SELECTOR_SIZE")
    need(not (V & {(v + g) % m for v in V}), "ANTIPODAL_PAIR")
    need(V | {(v + g) % m for v in V} == universe,
         "SELECTOR_COVERAGE")
    need(0 in C, "C_ORIENTATION")
    need({q % m for q in TAIL} <= Q, "TAIL_SUPPORT")
    need({a % m for a in HEAD} <= sums_mod(C, (0, g), m),
         "HEAD_SUPPORT")
    occupied = sums_mod(C, Q, m)
    need(occupied <= V, "SUPPORT_OUTSIDE_V")
    need(occupied == V, "SUPPORT_MISSING_V")
    return Counter((c + q) % m for c in C for q in Q)


def enumerate_supports(start):
    statistics = []
    survivors = {}
    for g in range(1, 15):
        guard(start)
        m = 2 * g
        q_lower = Counter(q % m for q in TAIL)
        h_lower = Counter(a % m for a in HEAD)
        S = set(q_lower)
        seen = 0
        tail_count = 0
        candidates = []
        for mask in range(1 << g):
            if mask % 256 == 0:
                guard(start)
            seen += 1
            V = {r + g * ((mask >> r) & 1) for r in range(g)}
            if not S <= V:
                continue
            tail_count += 1
            D = {c for c in range(m)
                 if all((s + c) % m in V for s in S)}
            need(0 in D, "NORMALIZED_C_ZERO_LOST")
            options = {
                a: D & {a % m, (a - g) % m}
                for a in HEAD
            }
            if any(not choice for choice in options.values()):
                continue
            forced = {0}
            for choice in options.values():
                if len(choice) == 1:
                    forced.update(choice)
            Qmax = {
                q for q in range(m)
                if all((c + q) % m in V for c in forced)
            }
            need(S <= Qmax, "FORCED_Q_BOUND_LOST_TAIL")
            support_shadow(g, V, forced, S)
            minimal_head = Counter(
                (c + b) % m for c in forced for b in (0, g)
            )
            need(all(minimal_head[r] >= k for r, k in h_lower.items()),
                 "ORIGINAL_HEAD_LOWER_MULTIPLICITY")
            candidates.append({
                "g": g,
                "modulus": m,
                "V": tuple(sorted(V)),
                "Cmax": tuple(sorted(D)),
                "forced_C": tuple(sorted(forced)),
                "Qmax": tuple(sorted(Qmax)),
                "head_lower": tuple(sorted(h_lower.items())),
                "tail_lower": tuple(sorted(q_lower.items())),
                "head_options": tuple(
                    (a, tuple(sorted(options[a]))) for a in HEAD
                ),
            })
        need(seen == 1 << g, "SELECTOR_ENUMERATION_COUNT")
        statistics.append((g, seen, tail_count, len(candidates)))
        if candidates:
            survivors[g] = candidates
    return statistics, survivors


EXPECTED_SHAPES = {
    8: {
        "V": (0, 1, 3, 4, 7, 10, 13, 14),
        "Cmax": (0, 3),
        "forced_C": (0, 3),
        "Qmax": (0, 1, 4, 7, 10, 13, 14),
    },
    10: {
        "V": (0, 1, 2, 6, 7, 8, 9, 13, 14, 15),
        "Cmax": (0, 1, 7, 8, 13, 14),
        "forced_C": (0, 1, 8, 13),
        "Qmax": (0, 1, 7, 13, 14),
    },
    11: {
        "V": (0, 1, 5, 6, 7, 8, 9, 13, 14, 15, 21),
        "Cmax": (0, 8, 14),
        "forced_C": (0, 8, 14),
        "Qmax": (0, 1, 7, 13, 14, 15, 21),
    },
}


def incidence(record):
    m = record["modulus"]
    rows = {s: {} for s in range(m)}
    for c in record["Cmax"]:
        for q in record["Qmax"]:
            row = rows[(c + q) % m]
            pair = (c, q)
            row[pair] = row.get(pair, Fraction(0)) + Fraction(1)
    V = set(record["V"])
    need({s for s in range(m) if rows[s]} == V,
         "INCIDENCE_OCCUPIED_ROWS")
    return rows


def strict_edge(record, rows, singleton_s, comparison_s,
                smaller_c, positive_witness):
    V = set(record["V"])
    need(singleton_s in V and comparison_s in V,
         "CERTIFICATE_NOT_TWO_OCCUPIED_ROWS")
    single = rows[singleton_s]
    need(len(single) == 1, "CERTIFICATE_NOT_SINGLETON")
    (larger_c, shared_q), coefficient = next(iter(single.items()))
    need(coefficient == Fraction(1), "CERTIFICATE_SINGLETON_COEFFICIENT")
    forced = set(record["forced_C"])
    q_lower = dict(record["tail_lower"])
    need(larger_c in forced and smaller_c in forced,
         "CERTIFICATE_UNFORCED_C_POSITIVITY")
    need(q_lower.get(shared_q, 0) > 0,
         "CERTIFICATE_UNPROVIDED_SHARED_Q_POSITIVITY")
    remainder = dict(rows[comparison_s])
    target = (smaller_c, shared_q)
    remainder[target] = remainder.get(target, Fraction(0)) - Fraction(1)
    need(all(value >= 0 for value in remainder.values()),
         "CERTIFICATE_NEGATIVE_REMAINDER")
    need(remainder.get(positive_witness, Fraction(0)) > 0,
         "CERTIFICATE_MISSING_STRICT_WITNESS")
    witness_c, witness_q = positive_witness
    need(witness_c in forced,
         "CERTIFICATE_UNFORCED_WITNESS_C_POSITIVITY")
    need(q_lower.get(witness_q, 0) > 0,
         "CERTIFICATE_UNPROVIDED_WITNESS_Q_POSITIVITY")
    return {
        "strict_edge": (larger_c, smaller_c),
        "shared_positive_q": shared_q,
        "singleton_row": singleton_s,
        "comparison_row": comparison_s,
        "positive_witness": positive_witness,
        "nonnegative_remainder": tuple(
            (c, q, str(value))
            for (c, q), value in sorted(remainder.items())
            if value
        ),
    }


CERTIFICATES = {
    8: ((3, 0, 0, (3, 13)), (14, 1, 3, (0, 1))),
    10: ((6, 1, 8, (0, 1)), (9, 14, 13, (0, 14))),
    11: ((6, 0, 8, (0, 0)), (8, 14, 14, (0, 14))),
}


def verify_symbolic_cycle(record, rows):
    evidence = [
        strict_edge(record, rows, *spec)
        for spec in CERTIFICATES[record["g"]]
    ]
    first, second = (item["strict_edge"] for item in evidence)
    need(first[0] != first[1], "CERTIFICATE_TRIVIAL_EDGE")
    need(first == (second[1], second[0]),
         "CERTIFICATE_NO_STRICT_TWO_CYCLE")
    return {
        "status": "INFEASIBLE_BY_EXACT_POSITIVE_WEIGHT_CERTIFICATE",
        "evidence": tuple(evidence),
    }


def residues(values, n, name):
    values = tuple(values)
    need(bool(values), name + "_EMPTY")
    need(all(type(x) is int and 0 <= x < n for x in values),
         name + "_RANGE")
    need(len(set(values)) == len(values), name + "_DUPLICATE")
    return values


def actual_tiling(n, d, C, Q):
    need(type(n) is int and n > 14, "N_GT_14")
    need(type(d) is int and 0 < d < n, "DISTINCT_TWO_POINT_FACTOR")
    C = residues(C, n, "C")
    Q = residues(Q, n, "Q")
    P_ordered = tuple((c + b) % n for c in C for b in (0, d))
    need(len(set(P_ordered)) == 2 * len(C), "ORIGINAL_P_FACTOR_NOT_DIRECT")
    P = set(P_ordered)
    total = Counter(
        (c + b + q) % n for c in C for b in (0, d) for q in Q
    )
    need(all(total[x] == 1 for x in range(n)),
         "ORIGINAL_ORDERED_SUM_NOT_EXACTLY_ONE")
    t_counts = Counter((c + q) % n for c in C for q in Q)
    need(all(value == 1 for value in t_counts.values()),
         "C_PLUS_Q_NOT_DIRECT")
    g = gcd(d, n)
    m = 2 * g
    need(n % m == 0, "TWO_POINT_ORDER_NOT_EVEN")
    L = n // m
    T = set(t_counts)
    V = {x % m for x in T}
    need(T == {x for x in range(n) if x % m in V},
         "ACTUAL_T_NOT_COMPLETE_RESIDUE_CLASSES")
    need(len(V) == g and not (V & {(v + g) % m for v in V}),
         "ACTUAL_T_NOT_ANTIPODAL_SELECTOR")
    c_counts = Counter(c % m for c in C)
    q_counts = Counter(q % m for q in Q)
    coefficients = tuple(
        sum(c_counts[i] * q_counts[(s - i) % m] for i in range(m))
        for s in range(m)
    )
    need(coefficients == tuple(L * int(s in V) for s in range(m)),
         "ORIGINAL_WEIGHTED_PROJECTION_EQUATION")
    return {
        "n": n, "d": d, "g": g, "L": L,
        "C": tuple(sorted(C)), "Q": tuple(sorted(Q)),
        "P": tuple(sorted(P)), "V": tuple(sorted(V)),
        "projected_C_counts": tuple(sorted(c_counts.items())),
        "projected_Q_counts": tuple(sorted(q_counts.items())),
        "weighted_coefficients": coefficients,
        "missing_head": tuple(a for a in HEAD if a not in P),
        "missing_tail": tuple(q for q in TAIL if q not in set(Q)),
    }


def anchor_check(record, require_head=True, require_tail=True):
    if require_head:
        need(not record["missing_head"],
             "HEAD_ANCHOR:" + repr(record["missing_head"]))
    if require_tail:
        need(not record["missing_tail"],
             "TAIL_ANCHOR:" + repr(record["missing_tail"]))


def expect_reason(operation, prefix):
    try:
        operation()
    except CheckError as error:
        reason = str(error)
        need(reason.startswith(prefix), "WRONG_CONTROL_REASON:" + reason)
        return reason
    raise CheckError("CONTROL_NOT_REJECTED:" + prefix)


def run():
    start = perf_counter()
    statistics, survivors = enumerate_supports(start)
    expected_tail = (0, 0, 1, 0, 1, 0, 0, 8, 16, 32, 64, 0, 0, 0)
    expected_head = (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0)
    need(tuple(row[2] for row in statistics) == expected_tail,
         "TAIL_SELECTOR_COUNT_DISAGREEMENT")
    need(tuple(row[3] for row in statistics) == expected_head,
         "HEAD_SUPPORT_COUNT_DISAGREEMENT")
    need(sum(row[1] for row in statistics) == 32766,
         "TOTAL_SELECTOR_COUNT")
    need(set(survivors) == {8, 10, 11}, "UNEXPECTED_SUPPORT_SURVIVOR")
    tables = {}
    proofs = {}
    selected = {}
    for g in (8, 10, 11):
        guard(start)
        need(len(survivors[g]) == 1, "NONUNIQUE_SUPPORT_SHADOW")
        record = survivors[g][0]
        for key, expected in EXPECTED_SHAPES[g].items():
            need(record[key] == expected,
                 "SUPPORT_SHAPE_DISAGREEMENT:" + repr((g, key)))
        rows = incidence(record)
        tables[g] = tuple(
            (s, tuple(sorted(rows[s]))) for s in range(record["modulus"])
        )
        proofs[g] = verify_symbolic_cycle(record, rows)
        selected[g] = record
    genuine = {}
    for g in range(1, 15):
        guard(start)
        m = 2 * g
        L = (15 + m - 1) // m
        n = m * L
        Q = tuple(x for x in range(n) if x % m < g)
        record = actual_tiling(n, g, (0,), Q)
        need(record["g"] == g, "GENUINE_FIXTURE_WRONG_GCD")
        need(bool(record["missing_head"]), "GENUINE_FIXTURE_ACCIDENTAL_TARGET")
        genuine[g] = record
    head_control = genuine[3]
    anchor_check(head_control, require_head=False, require_tail=True)
    head_reason = expect_reason(
        lambda: anchor_check(head_control), "HEAD_ANCHOR:"
    )
    tail_control = actual_tiling(
        24, 1, tuple(range(0, 12, 2)), (0, 12)
    )
    anchor_check(tail_control, require_head=True, require_tail=False)
    tail_reason = expect_reason(
        lambda: anchor_check(tail_control), "TAIL_ANCHOR:"
    )
    shadow8 = selected[8]
    unit_counts = support_shadow(
        8, shadow8["V"], shadow8["forced_C"], TAIL
    )
    need(len({unit_counts[s] for s in shadow8["V"]}) > 1,
         "WEIGHTED_CONTROL_NOT_NONCONSTANT")
    need(proofs[8]["status"] ==
         "INFEASIBLE_BY_EXACT_POSITIVE_WEIGHT_CERTIFICATE",
         "WEIGHTED_CONTROL_MISSING_ALL_WEIGHT_CERTIFICATE")
    controls = {
        "drop_head": {
            "status": "GENUINE_NON_TARGET_COUNTEREXAMPLE",
            "fixture": head_control,
            "intended_full_check_rejection": head_reason,
        },
        "drop_tail": {
            "status": "GENUINE_NON_TARGET_COUNTEREXAMPLE",
            "fixture": tail_control,
            "intended_full_check_rejection": tail_reason,
        },
        "drop_weighted_multiplicities": {
            "status": "PROJECTION_ONLY_SUPPORT_FALSE_POSITIVE",
            "not_an_actual_anchored_tiling": True,
            "g": 8,
            "C_support": shadow8["forced_C"],
            "Q_support": TAIL,
            "V": shadow8["V"],
            "unit_convolution": tuple(sorted(unit_counts.items())),
            "all_positive_weights_rejected_by": proofs[8],
        },
        "drop_actual_original_P_factor": {
            "status": "NOT_TESTED",
            "reason": (
                "No actual tiling with all original anchors and without "
                "the factor was constructed; shadows are not substitutes."
            ),
        },
    }
    guard(start)
    return {
        "method": (
            "EXHAUSTIVE_NECESSARY_PROJECTED_SUPPORT_SCREEN_AND_"
            "EXACT_SYMBOLIC_POSITIVE_WEIGHT_CERTIFICATES"
        ),
        "not_an_original_tiling_solver": True,
        "head_anchors": HEAD,
        "tail_anchors": TAIL,
        "selector_statistics": tuple(statistics),
        "support_shadows": selected,
        "all_residue_incidence_tables": tables,
        "positive_weight_certificates": proofs,
        "genuine_non_target_tilings": genuine,
        "mutation_controls": controls,
        "scope": (
            "Necessary shadows excluded for g=1..14; no unrestricted "
            "anchored nonexistence, original factor existence, novelty, "
            "independent-family, human, or kernel assurance."
        ),
        "elapsed_seconds": perf_counter() - start,
    }


RESULT = run()
