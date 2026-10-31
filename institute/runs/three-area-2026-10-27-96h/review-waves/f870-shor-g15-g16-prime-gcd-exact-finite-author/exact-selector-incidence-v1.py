#!/usr/bin/env python3
"""UNRUN F870 candidate. Parent source audit and one-shot GO are prerequisites.

Only Python standard library. No imports of prior research code, subprocesses,
network, external data, randomization, floating-point mathematical judgments,
or filesystem writes. JSON on stdout contains exact incidences and statuses.
The monotonic cooperative computation limit is 38 s; the supervising parent must
set an outer wall limit no greater than 55 s and retain stdout, stderr and exit
status. An interrupted/expired run is INCOMPLETE, never a negative theorem.
"""

import itertools
import json
import math
import signal
import sys
import time


START = time.monotonic()
DEADLINE = START + 38.0
STOP_REQUESTED = False
TAIL = frozenset((0, 1, 7, 13, 14))
HEAD = (3, 8, 11)
HEAD_WITH_ZERO = frozenset((0, 3, 8, 11))
SMALL_N_MAX = 12


def signal_latch(_signum, _frame):
    global STOP_REQUESTED
    STOP_REQUESTED = True


class Incomplete(Exception):
    pass


class CheckFailure(Exception):
    pass


class Violation(Exception):
    pass


def guard():
    if STOP_REQUESTED:
        raise Incomplete("signal_latched")
    if time.monotonic() >= DEADLINE:
        raise Incomplete("internal_38_second_limit")


def need(condition, message):
    if not condition:
        raise CheckFailure(message)


def forbid(condition, reason):
    if condition:
        raise Violation(reason)


def selector_validate(g, v):
    for r in range(g):
        forbid(int(r in v) + int(r + g in v) != 1, "SELECTOR_ANTIPODAL")
    forbid(not TAIL.issubset(v), "TAIL_ANCHOR_MISSING")


def c_superset(g, v):
    m = 2 * g
    return {i for i in range(m) if all((i + s) % m in v for s in TAIL)}


def forced_validate(g, forced, c_sup):
    forbid(0 not in forced, "C_ZERO_MISSING")
    for a in HEAD:
        forbid(a not in forced and a + g not in forced,
               "HEAD_ANCHOR_%d_MISSING" % a)
    forbid(not forced.issubset(c_sup), "FORCED_TRANSLATE_OUTSIDE_SELECTOR")


def q_superset(g, v, forced):
    m = 2 * g
    return {j for j in range(m) if all((j + i) % m in v for i in forced)}


def incidence(g, c_sup, q_sup):
    m = 2 * g
    rows = [[] for _ in range(m)]
    for i in sorted(c_sup):
        for j in sorted(q_sup):
            rows[(i + j) % m].append((i, j))
    return rows


def certificate_validate(case, rows, forced_c, forced_q):
    v = set(case["v"])
    eq1, eq2 = case["eq"]
    inequalities = case["inequalities"]
    for s, i, j in (eq1, eq2):
        forbid(s not in v, "EQUALITY_ROW_UNOCCUPIED")
        forbid(rows[s] != [(i, j)], "SINGLETON_INCIDENCE")
    _, a, u = eq1
    _, b, w = eq2
    forbid(a not in forced_c or b not in forced_c or
           u not in forced_q or w not in forced_q, "BASE_NOT_FORCED")
    expected_bases = ((b, u), (a, w))
    for index, (s, base, extra) in enumerate(inequalities):
        forbid(s not in v, "INEQUALITY_ROW_UNOCCUPIED")
        forbid(tuple(base) != expected_bases[index], "TWO_CYCLE_ORIENTATION")
        forbid(tuple(base) not in rows[s] or tuple(extra) not in rows[s],
               "INEQUALITY_INCIDENCE")
        forbid(tuple(base) == tuple(extra), "REMAINDER_NOT_DISTINCT")
        forbid(extra[0] not in forced_c or extra[1] not in forced_q,
               "REMAINDER_NOT_FORCED")


def expect_violation(label, reason, call):
    try:
        call()
    except Violation as exc:
        need(str(exc) == reason, "%s: wrong reason %s" % (label, exc))
        return {"mutant": label, "rejected_as": reason}
    raise CheckFailure("%s: mutant unexpectedly accepted" % label)


EXPECTED_CASES = [
    {
        "name": "g15_h5", "g": 15,
        "v": [0, 1, 2, 5, 6, 7, 11, 12, 13, 14, 18, 19, 23, 24, 25],
        "forced": [0, 11, 18, 23],
        "c_sup": [0, 5, 11, 18, 23],
        "q_sup": [0, 1, 7, 12, 13, 14, 19, 25],
        "eq": [(11, 11, 0), (14, 0, 14)],
        "inequalities": [(0, (0, 0), (23, 7)),
                         (25, (11, 14), (18, 7))],
    },
    {
        "name": "g15_h20", "g": 15,
        "v": [0, 1, 2, 6, 7, 11, 12, 13, 14, 18, 19, 20, 23, 24, 25],
        "forced": [0, 11, 18, 23],
        "c_sup": [0, 6, 11, 18, 23],
        "q_sup": [0, 1, 2, 7, 13, 14, 19, 25],
        "eq": [(11, 11, 0), (14, 0, 14)],
        "inequalities": [(0, (0, 0), (23, 7)),
                         (25, (11, 14), (18, 7))],
    },
    {
        "name": "g16_A", "g": 16,
        "v": [0, 1, 2, 7, 8, 9, 13, 14, 15, 19, 20, 21, 22, 26, 27, 28],
        "forced": [0, 8, 19, 27],
        "c_sup": [0, 1, 7, 8, 13, 14, 19, 20, 26, 27],
        "q_sup": [0, 1, 7, 13, 14, 20, 26],
        "eq": [(19, 19, 0), (22, 8, 14)],
        "inequalities": [(8, (8, 0), (27, 13)),
                         (1, (19, 14), (0, 1))],
    },
    {
        "name": "g16_B", "g": 16,
        "v": [0, 1, 5, 6, 7, 11, 12, 13, 14, 18, 19, 20, 24, 25, 26, 31],
        "forced": [0, 11, 19, 24],
        "c_sup": [0, 5, 6, 11, 12, 18, 19, 24, 25, 31],
        "q_sup": [0, 1, 7, 13, 14, 20, 26],
        "eq": [(11, 11, 0), (14, 0, 14)],
        "inequalities": [(0, (0, 0), (19, 13)),
                         (25, (11, 14), (24, 1))],
    },
]


def run_mutants(case, c_sup, q_sup, rows):
    g = case["g"]
    v = set(case["v"])
    forced = set(case["forced"])
    controls = []
    controls.append(expect_violation(
        "add_antipode_of_zero", "SELECTOR_ANTIPODAL",
        lambda: selector_validate(g, v | {g})))
    controls.append(expect_violation(
        "swap_away_original_tail_zero", "TAIL_ANCHOR_MISSING",
        lambda: selector_validate(g, (v - {0}) | {g})))
    choice3 = ({3, 3 + g} & forced)
    need(len(choice3) == 1, "mutation: expected unique forced anchor 3")
    controls.append(expect_violation(
        "remove_anchor_three_representative", "HEAD_ANCHOR_3_MISSING",
        lambda: forced_validate(g, forced - choice3, c_sup)))
    singleton_row = case["eq"][0][0]
    added_c = (singleton_row - 1) % (2 * g)
    need(1 in q_sup and added_c not in c_sup,
         "mutation: extra singleton pair is not new")
    enlarged_rows = incidence(g, c_sup | {added_c}, q_sup)
    controls.append(expect_violation(
        "add_extra_singleton_incident_pair", "SINGLETON_INCIDENCE",
        lambda: certificate_validate(case, enlarged_rows, forced, TAIL)))
    controls.append(expect_violation(
        "remove_base_q_zero_positivity", "BASE_NOT_FORCED",
        lambda: certificate_validate(case, rows, forced, TAIL - {0})))
    extra_c = case["inequalities"][0][2][0]
    need(extra_c in forced, "mutation: remainder C factor not forced")
    controls.append(expect_violation(
        "remove_strict_remainder_positivity", "REMAINDER_NOT_FORCED",
        lambda: certificate_validate(case, rows, forced - {extra_c}, TAIL)))
    changed = dict(case)
    inequalities = list(case["inequalities"])
    s, base, _extra = inequalities[0]
    inequalities[0] = (s, base, base)
    changed["inequalities"] = inequalities
    controls.append(expect_violation(
        "duplicate_base_as_fake_remainder", "REMAINDER_NOT_DISTINCT",
        lambda: certificate_validate(changed, rows, forced, TAIL)))
    return controls


def do_selectors(section):
    section["status"] = "RUNNING"
    expected = {(c["g"], tuple(c["v"]), tuple(c["forced"])): c
                for c in EXPECTED_CASES}
    seen = set()
    for g in (15, 16):
        guard()
        m = 2 * g
        total = 1 << g
        stats = {"scanned": 0, "tail_selectors": 0, "anchor_assignments": 0}
        section["by_g"][str(g)] = stats
        for bits in range(total):
            if bits % 128 == 0:
                guard()
            stats["scanned"] += 1
            vmask = ((1 << g) - 1) ^ bits | (bits << g)
            if not all((vmask >> s) & 1 for s in TAIL):
                continue
            stats["tail_selectors"] += 1
            v = {s for s in range(m) if (vmask >> s) & 1}
            selector_validate(g, v)
            c_sup = c_superset(g, v)
            choices = [tuple(x for x in (a, a + g) if x in c_sup)
                       for a in HEAD]
            if any(not x for x in choices):
                continue
            for picked in itertools.product(*choices):
                guard()
                forced = {0, *picked}
                forced_validate(g, forced, c_sup)
                stats["anchor_assignments"] += 1
                key = (g, tuple(sorted(v)), tuple(sorted(forced)))
                need(key in expected, "unexpected admissible selector/anchor " + str(key))
                need(key not in seen, "duplicate selector/anchor assignment")
                seen.add(key)
                case = expected[key]
                q_sup = q_superset(g, v, forced)
                need(sorted(c_sup) == case["c_sup"], case["name"] + ": C superset")
                need(sorted(q_sup) == case["q_sup"], case["name"] + ": Q superset")
                need(TAIL.issubset(q_sup), case["name"] + ": tail not in Q superset")
                rows = incidence(g, c_sup, q_sup)
                need(sum(map(len, rows)) == len(c_sup) * len(q_sup),
                     case["name"] + ": lost incidence")
                for s in range(m):
                    independently_selected = [(i, j) for i in sorted(c_sup)
                                              for j in sorted(q_sup)
                                              if (i + j) % m == s]
                    need(rows[s] == independently_selected,
                         case["name"] + ": incidence row " + str(s))
                certificate_validate(case, rows, forced, TAIL)
                mutants = run_mutants(case, c_sup, q_sup, rows)
                section["cases"].append({
                    "name": case["name"], "g": g, "selector": sorted(v),
                    "forced_C": sorted(forced), "forced_Q": sorted(TAIL),
                    "possible_C_superset": sorted(c_sup),
                    "possible_Q_superset": sorted(q_sup),
                    "rows": [{"residue": s, "occupied": s in v,
                              "incident_pairs": [list(x) for x in rows[s]]}
                             for s in range(m)],
                    "equalities": case["eq"],
                    "strict_inequality_witnesses": case["inequalities"],
                    "reason_specific_mutants": mutants,
                    "interpretation": "necessary support supersets only; no tiling constructed",
                })
        need(stats["scanned"] == total, "selector scan incomplete")
        need(stats["tail_selectors"] == (1 << (g - len(TAIL))),
             "tail selector count")
        need(stats["anchor_assignments"] == 2, "unexpected anchor assignment count")
    need(seen == set(expected), "one or more expected selector cases absent")
    section["status"] = "COMPLETE"


def coefficients(n, a, b):
    counts = [0] * n
    for x in a:
        for y in b:
            counts[(x + y) % n] += 1
    return counts


def direct(n, a, b):
    return coefficients(n, a, b) == [1] * n


def bits_to_elements(mask, n):
    return [i for i in range(n) if (mask >> i) & 1]


def normalized_direct_tilings(n):
    """Each ordered pair of nonempty sets containing 0, with exact cover, once."""
    full = (1 << n) - 1
    for amask in range(1, 1 << n, 2):
        guard()
        a = bits_to_elements(amask, n)
        if n % len(a):
            continue
        translates = []
        for q in range(n):
            mask = 0
            for x in a:
                mask |= 1 << ((x + q) % n)
            translates.append(mask)

        def extend(covered, qmask):
            guard()
            if covered == full:
                yield bits_to_elements(qmask, n)
                return
            missing = full ^ covered
            first = (missing & -missing).bit_length() - 1
            for x in a:
                q = (first - x) % n
                tm = translates[q]
                if not (covered & tm):
                    yield from extend(covered | tm, qmask | (1 << q))

        for b in extend(amask, 1):
            yield a, b


def do_small_tilings(section):
    section["status"] = "RUNNING"
    for n in range(1, SMALL_N_MAX + 1):
        guard()
        stats = {"normalized_tilings": 0, "head_dilations": 0,
                 "tail_dilations": 0, "unit_head_dilations": 0,
                 "unit_tail_dilations": 0}
        section["by_n"][str(n)] = stats
        saw_trivial_left = False
        saw_trivial_right = False
        saw_four_control = False
        for a, b in normalized_direct_tilings(n):
            guard()
            need(0 in a and 0 in b and len(a) * len(b) == n,
                 "bad normalized enumerator output")
            need(direct(n, a, b), "enumerator produced non-tiling")
            stats["normalized_tilings"] += 1
            saw_trivial_left |= len(a) == 1 and len(b) == n
            saw_trivial_right |= len(b) == 1 and len(a) == n
            saw_four_control |= n == 4 and a == [0, 2] and b == [0, 1]
            for k in range(1, 2 * n + 1):
                guard()
                if math.gcd(k, len(a)) == 1:
                    dilated = [(k * x) % n for x in a]
                    need(len(set(dilated)) == len(a) and direct(n, dilated, b),
                         "head coprime-cardinality dilation failed")
                    stats["head_dilations"] += 1
                    if math.gcd(k, n) == 1:
                        stats["unit_head_dilations"] += 1
                if math.gcd(k, len(b)) == 1:
                    dilated = [(k * x) % n for x in b]
                    need(len(set(dilated)) == len(b) and direct(n, a, dilated),
                         "tail coprime-cardinality dilation failed")
                    stats["tail_dilations"] += 1
                    if math.gcd(k, n) == 1:
                        stats["unit_tail_dilations"] += 1
        need(saw_trivial_left and saw_trivial_right, "missing trivial tiling control")
        if n == 4:
            need(saw_four_control, "missing nontrivial n=4 control")
    section["status"] = "COMPLETE"


def do_equal_gcd_units(section):
    section["status"] = "RUNNING"
    for n in range(1, SMALL_N_MAX + 1):
        guard()
        units = [u for u in range(n) if math.gcd(u, n) == 1]
        checks = 0
        for t in range(n):
            for s in range(n):
                guard()
                same_gcd = math.gcd(t, n) == math.gcd(s, n)
                witness = any((u * t - s) % n == 0 for u in units)
                need(same_gcd == witness,
                     "equal-gcd unit orbit failure at %d,%d,%d" % (n, t, s))
                checks += 1
        section["by_n"][str(n)] = {"residue_pairs": checks, "units": units}
    section["status"] = "COMPLETE"


def check_physical_fixture(n, d, c, q, require_head, require_tail):
    guard()
    need(n > 14 and 0 in c and 0 in q and d % n != 0,
         "invalid physical fixture parameters")
    need(len(c) == len(set(c)) and len(q) == len(set(q)), "fixture duplicates")
    p_terms = [(x + e * d) % n for x in c for e in (0, 1)]
    need(len(set(p_terms)) == len(p_terms), "fixture C factor not direct")
    p = set(p_terms)
    need(direct(n, p_terms, q), "fixture is not an actual direct tiling")
    t_counts = coefficients(n, c, q)
    need(all(x in (0, 1) for x in t_counts), "fixture C+Q not direct")
    g = math.gcd(d, n)
    need(n % (2 * g) == 0, "fixture cycle not even")
    m = 2 * g
    length = n // m
    v = {x % m for x in range(n) if t_counts[x] == 1}
    need(all(int(r in v) + int(r + g in v) == 1 for r in range(g)),
         "fixture selector property")
    for x in range(n):
        need(t_counts[x] == int(x % m in v), "fixture fibre not full")
        need(t_counts[x] + t_counts[(x - d) % n] == 1,
             "fixture alternating recurrence")
    cc = [sum(x % m == i for x in c) for i in range(m)]
    qq = [sum(x % m == j for x in q) for j in range(m)]
    for s in range(m):
        need(sum(cc[i] * qq[(s - i) % m] for i in range(m)) ==
             length * int(s in v), "fixture weighted coefficient")
    missing_head = sorted(HEAD_WITH_ZERO - p)
    missing_tail = sorted(TAIL - set(q))
    need((not missing_head) == require_head, "fixture head classification")
    need((not missing_tail) == require_tail, "fixture tail classification")
    need(missing_head or missing_tail, "fixture accidentally treated as target")
    return {"n": n, "d": d, "g": g, "L": length,
            "C": sorted(c), "Q": sorted(q), "P": sorted(p),
            "selector": sorted(v), "projected_C_multiplicities": cc,
            "projected_Q_multiplicities": qq,
            "missing_original_head_anchors": missing_head,
            "missing_original_tail_anchors": missing_tail,
            "classification": "ACTUAL_DIRECT_TILING_NON_TARGET"}


def do_physical_controls(section):
    section["status"] = "RUNNING"
    for g in (15, 16):
        section["fixtures"].append(check_physical_fixture(
            4 * g, g, [0, 2 * g], list(range(g)), False, True))
    section["fixtures"].append(check_physical_fixture(
        32, 3, [0, 8], [0, 2, 4, 6, 16, 18, 20, 22], True, False))
    section["status"] = "COMPLETE"


def main():
    result = {
        "status": "INCOMPLETE",
        "scope": "local projected support certificates and non-target controls; no target realization or global prime theorem",
        "internal_limit_seconds": 38,
        "required_parent_outer_limit_seconds_at_most": 55,
        "sections": {
            "selectors_and_incidence": {"status": "NOT_STARTED", "by_g": {}, "cases": []},
            "actual_non_target_fixtures": {"status": "NOT_STARTED", "fixtures": []},
            "normalized_small_direct_tilings": {"status": "NOT_STARTED", "by_n": {}},
            "equal_gcd_unit_orbits": {"status": "NOT_STARTED", "by_n": {}},
        },
    }
    exit_code = 2
    try:
        signal.signal(signal.SIGINT, signal_latch)
        signal.signal(signal.SIGTERM, signal_latch)
        guard()
        sections = result["sections"]
        do_selectors(sections["selectors_and_incidence"])
        do_physical_controls(sections["actual_non_target_fixtures"])
        do_small_tilings(sections["normalized_small_direct_tilings"])
        do_equal_gcd_units(sections["equal_gcd_unit_orbits"])
        guard()
        result["status"] = "COMPLETE"
        exit_code = 0
    except Incomplete as exc:
        result["status"] = "INCOMPLETE"
        result["reason"] = str(exc)
    except (CheckFailure, Violation) as exc:
        result["status"] = "FAIL"
        result["reason"] = str(exc)
        exit_code = 1
    except Exception as exc:
        result["status"] = "ERROR"
        result["reason"] = type(exc).__name__ + ": " + str(exc)
        exit_code = 1
    finally:
        for section in result["sections"].values():
            if section["status"] == "RUNNING":
                section["status"] = "INCOMPLETE"
        result["elapsed_monotonic_seconds"] = round(time.monotonic() - START, 6)
        json.dump(result, sys.stdout, sort_keys=True, separators=(",", ":"))
        sys.stdout.write("\n")
        sys.stdout.flush()
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
