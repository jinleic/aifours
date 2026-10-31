#!/usr/bin/env python3
"""Independent exact f369 finite audit. Stdlib only; no writes/network/subprocess.
Run: python3 -I -B f369_independent_finite_verifier_v1.py
Execution status in the author's return: NOTRUN. A successful future run prints
its actual receipt; none of those future output fields is claimed observed now.
"""
from collections import defaultdict
from itertools import combinations, combinations_with_replacement, product
from pathlib import Path
import hashlib
import json
import sys
import time

START = time.perf_counter()
DEADLINE = START + 55.0


class VerificationError(Exception):
    def __init__(self, code, detail):
        self.code = code
        self.detail = detail
        super().__init__(code + ": " + repr(detail))


def require(condition, code, detail):
    if not condition:
        raise VerificationError(code, detail)


def tick():
    require(time.perf_counter() < DEADLINE, "TIME_LIMIT", "55-second cooperative limit")


PROFILES = tuple(combinations_with_replacement((3, 4, 5), 4))
CLAIMED = {q: set() for q in PROFILES}
CLAIMED.update({
    (3, 5, 5, 5): {(0, 0, 12, 12, 0)},
    (4, 4, 4, 4): {(0, 0, 24, 0, 0)},
    (4, 4, 4, 5): {(0, 0, 18, 6, 0)},
    (4, 4, 5, 5): {(0, 1, 10, 13, 0), (0, 0, 13, 10, 1)},
    (4, 5, 5, 5): {
        (0, 0, 9, 12, 3), (0, 1, 6, 15, 2),
        (0, 2, 3, 18, 1), (1, 0, 3, 20, 0)},
    (5, 5, 5, 5): {
        (0, 0, 6, 12, 6), (0, 1, 3, 15, 5), (1, 0, 0, 20, 3)},
})
RAW_EXPECTED = {q: set(hs) for q, hs in CLAIMED.items()}
RAW_EXPECTED[(4, 5, 5, 5)].add((0, 3, 0, 21, 0))
RAW_EXPECTED[(5, 5, 5, 5)].add((0, 2, 0, 18, 4))

# Source-supplied concrete claim, not a generated AME witness.
WORDS = (
    (0, 0, 0, 0), (0, 0, 1, 1), (0, 1, 0, 1), (0, 1, 1, 0),
    (1, 0, 0, 1), (1, 0, 1, 0), (1, 1, 0, 0), (1, 1, 1, 1),
)
CUTS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
PAIR_VALUES = tuple(product((0, 1), repeat=2))
READABLE_RELATION = (1, 0, -1, 0, 0, 1)
EXPECTED_PHASE_ROWS = (
    (1, -1, 0, 0, 0, 0, -1, 1),
    (0, 0, 1, -1, -1, 1, 0, 0),
    (1, 0, -1, 0, 0, -1, 0, 1),
    (0, 1, 0, -1, -1, 0, 1, 0),
    (1, 0, 0, -1, -1, 0, 0, 1),
    (0, 1, -1, 0, 0, -1, 1, 0),
)


def target(q):
    return (6 * sum(q) - 48,
            sum(q[i] * q[j] for i, j in combinations(range(4), 2)) - 72)


def compositions(n):
    for n0 in range(n + 1):
        tick()
        for n1 in range(n - n0 + 1):
            for n2 in range(n - n0 - n1 + 1):
                for n3 in range(n - n0 - n1 - n2 + 1):
                    yield (n0, n1, n2, n3, n - n0 - n1 - n2 - n3)


def moments(h):
    return (sum(k * h[k] for k in range(5)),
            sum((k * (k - 1) // 2) * h[k] for k in range(5)))


def enumerate_shadows(nwords=24, second_shift=0):
    targets = {q: (target(q)[0], target(q)[1] + second_shift) for q in PROFILES}
    index = {cm: set() for cm in targets.values()}
    count = 0
    for h in compositions(nwords):
        count += 1
        cm = moments(h)
        if cm in index:
            index[cm].add(h)
    return {q: set(index[cm]) for q, cm in targets.items()}, count


def compare_sets(q, actual, expected, stage):
    require(actual == expected, "HISTOGRAM_SET_MISMATCH", {
        "q": q, "stage": stage,
        "missing": sorted(expected - actual), "extra": sorted(actual - expected)})


def compare_tables(actual, expected, stage):
    require(set(actual) == set(expected) == set(PROFILES),
            "HISTOGRAM_PROFILE_SET", stage)
    for q in PROFILES:
        compare_sets(q, actual[q], expected[q], stage)


def check_histogram(h, nwords, c, m):
    require(len(h) == 5 and all(type(x) is int and x >= 0 for x in h),
            "SHADOW_DOMAIN", h)
    require(sum(h) == nwords, "MAXIMAL_WORD_COUNT", (sum(h), nwords))
    hc, hm = moments(h)
    require(hc == c, "SHADOW_FIRST_MOMENT", (hc, c))
    require(hm == m, "SHADOW_SECOND_MOMENT", (hm, m))


def outside_footprint_bound(q):
    # A k=1 word has three outside coordinates. Every outside pair it uses
    # is a pair value of P, so two such footprints may not intersect.
    # Inside symbol labels are deliberately forgotten: this is a relaxation.
    footprints = []
    for inside in range(4):
        choices = [(None,) if i == inside else tuple(range(q[i], 6))
                   for i in range(4)]
        for values in product(*choices):
            fp = frozenset((i, j, values[i], values[j])
                           for i, j in combinations(range(4), 2)
                           if values[i] is not None and values[j] is not None)
            require(len(fp) == 3, "FOOTPRINT_SIZE", (q, values))
            footprints.append(fp)
    require(len(footprints) == len(set(footprints)), "DUPLICATE_FOOTPRINT", q)
    best, witness = 0, ()
    for size in range(len(footprints) + 1):
        tick()
        for subset in combinations(range(len(footprints)), size):
            used = set()
            for i in subset:
                if not used.isdisjoint(footprints[i]):
                    break
                used.update(footprints[i])
            else:
                if size > best:
                    best, witness = size, subset
    return {"patterns": len(footprints), "maximum": best,
            "witness": [sorted(footprints[i]) for i in witness]}


def apply_separate_bounds(raw, bounds):
    out = {}
    for q in PROFILES:
        pair_capacity = all(q[i] * q[j] >= 12 for i, j in combinations(range(4), 2))
        out[q] = {h for h in raw[q] if pair_capacity and
                  (q not in bounds or h[1] <= bounds[q])}
    return out


def forced_degrees():
    expected = {
        (3, 5, 5, 5): [{(4, 4, 4)}] + [{(2, 2, 2, 3, 3)} for _ in range(3)],
        (4, 4, 4, 4): [{(3, 3, 3, 3)} for _ in range(4)],
        (4, 4, 4, 5): [{(3, 3, 3, 3)} for _ in range(3)] + [{(2, 2, 2, 3, 3)}],
    }
    result = []
    for q, wanted in expected.items():
        parties = []
        for i in range(4):
            cap = min(q[j] for j in range(4) if j != i)
            possible = set()
            for rs in combinations_with_replacement(range(2, cap + 1), q[i]):
                if sum(rs) != 12:
                    continue
                # Equation (9), applicable because these three histograms
                # have only k=2,3 words. Counts n3(i,a) lie in [0,p_i(a)].
                if all(0 <= sum(q) - q[i] - 6 - 2*r <= 6-r for r in rs):
                    possible.add(rs)
            require(possible == wanted[i], "FORCED_DEGREES", (q, i, sorted(possible)))
            parties.append(sorted(possible))
        result.append({"q": q, "degree_multisets_by_party": parties})
    return result


def word_text(w):
    return "".join(map(str, w))


def flatten_and_derive(words):
    words = tuple(tuple(w) for w in words)
    require(all(len(w) == 4 and all(type(x) is int and x in (0, 1) for x in w)
                for w in words), "SUPPORT_DOMAIN", words)
    require(len(set(words)) == len(words), "SUPPORT_DUPLICATE", words)
    positions = {w: i for i, w in enumerate(words)}
    graphs, equations = [], []
    for left, right in CUTS:
        tick()
        label = "".join(str(i+1) for i in left) + "|" + "".join(str(i+1) for i in right)
        cells, row_adj, col_adj = {}, defaultdict(set), defaultdict(set)
        for w in words:
            r, c = tuple(w[i] for i in left), tuple(w[i] for i in right)
            require((r, c) not in cells, "FLATTEN_DUPLICATE", (label, r, c))
            cells[r, c] = positions[w]
            row_adj[r].add(c)
            col_adj[c].add(r)
        require(set(row_adj) == set(col_adj) == set(PAIR_VALUES),
                "PAIR_VALUE_COVERAGE", label)
        for kind, adjacency in (("row", row_adj), ("column", col_adj)):
            for value in PAIR_VALUES:
                require(len(adjacency[value]) == 2, "PAIR_DEGREE",
                        (label, kind, value, len(adjacency[value]), 2))
        unseen, blocks = set(PAIR_VALUES), []
        while unseen:
            rs, cs = {min(unseen)}, set()
            while True:
                new_cs = set().union(*(row_adj[r] for r in rs))
                new_rs = set().union(*(col_adj[c] for c in new_cs))
                if new_rs == rs and new_cs == cs:
                    break
                rs, cs = new_rs, new_cs
            require(len(rs) == len(cs) == 2, "BLOCK_NOT_2X2", (label, sorted(rs), sorted(cs)))
            require(all((r, c) in cells for r in rs for c in cs),
                    "BLOCK_NOT_FULL", label)
            rr, cc = sorted(rs), sorted(cs)
            corners = [cells[rr[0], cc[0]], cells[rr[0], cc[1]],
                       cells[rr[1], cc[0]], cells[rr[1], cc[1]]]
            coeff = [0] * len(words)
            for index, sign in zip(corners, (1, -1, -1, 1)):
                coeff[index] += sign
            equations.append(tuple(coeff))
            blocks.append({"rows": rr, "columns": cc,
                           "corners_row_major": [word_text(words[i]) for i in corners]})
            unseen.difference_update(rs)
        require(len(blocks) == 2, "BLOCK_COUNT", (label, len(blocks)))
        matrix = [[word_text(words[cells[r, c]]) if (r, c) in cells else None
                   for c in PAIR_VALUES] for r in PAIR_VALUES]
        graphs.append({"cut": label, "row_and_column_order": PAIR_VALUES,
                       "matrix": matrix, "row_degrees": [2]*4,
                       "column_degrees": [2]*4, "blocks": blocks})
    return graphs, tuple(equations)


def certify_integer_relation(equations, rhs, relation):
    require(len(equations) == len(rhs) == len(relation) and
            all(type(x) is int for x in relation + tuple(rhs)),
            "PHASE_CERTIFICATE_DOMAIN", (rhs, relation))
    lhs = tuple(sum(relation[j] * equations[j][i] for j in range(len(equations)))
                for i in range(len(equations[0])))
    require(all(x == 0 for x in lhs), "PHASE_INTEGER_LHS", lhs)
    rhs_units = sum(a*b for a, b in zip(relation, rhs))
    require(rhs_units % 2 == 1, "PHASE_RHS_EVEN", rhs_units)
    return {"coefficients": relation, "integer_lhs": lhs, "rhs_pi_units": rhs_units}


def discover_relation(equations, rhs):
    # Ordinary integer arithmetic, NOT a GF(2) nullspace calculation.
    for weight in range(1, len(equations) + 1):
        tick()
        for relation in product((-1, 0, 1), repeat=len(equations)):
            if sum(abs(x) for x in relation) != weight:
                continue
            if next((x for x in relation if x), 0) < 0:
                continue
            lhs = [sum(relation[j] * equations[j][i] for j in range(len(equations)))
                   for i in range(len(equations[0]))]
            if not any(lhs) and sum(a*b for a, b in zip(relation, rhs)) % 2 == 1:
                return certify_integer_relation(equations, rhs, relation)
    raise VerificationError("NO_SMALL_INTEGER_CERTIFICATE", "search {-1,0,1}^6")


def expect_rejection(name, expected_code, operation):
    try:
        operation()
    except VerificationError as error:
        require(error.code == expected_code, "CONTROL_WRONG_REASON",
                (name, expected_code, error.code, error.detail))
        return {"name": name, "rejected_by": error.code, "detail": error.detail}
    raise VerificationError("CONTROL_ACCEPTED_MUTATION", name)


def main():
    require(len(sys.argv) == 1, "USAGE", "verifier accepts no arguments")
    require(len(PROFILES) == 15, "PROFILE_UNIVERSE", len(PROFILES))
    raw, count = enumerate_shadows()
    require(count == 20475, "COMPOSITION_UNIVERSE", count)
    compare_tables(raw, RAW_EXPECTED, "raw shadow equations only")
    for q in PROFILES:
        for h in raw[q]:
            check_histogram(h, 24, *target(q))
    footprint_results = {q: outside_footprint_bound(q)
                         for q in ((4, 5, 5, 5), (5, 5, 5, 5))}
    require(footprint_results[(4, 5, 5, 5)]["patterns"] == 7 and
            footprint_results[(4, 5, 5, 5)]["maximum"] == 2,
            "PAIR_BOUND_4555", footprint_results[(4, 5, 5, 5)])
    require(footprint_results[(5, 5, 5, 5)]["patterns"] == 4 and
            footprint_results[(5, 5, 5, 5)]["maximum"] == 1,
            "PAIR_BOUND_5555", footprint_results[(5, 5, 5, 5)])
    bounds = {q: result["maximum"] for q, result in footprint_results.items()}
    restricted = apply_separate_bounds(raw, bounds)
    compare_tables(restricted, CLAIMED, "pair capacity plus separate k=1 injectivity bounds")
    degrees = forced_degrees()
    parity_universe = {w for w in product((0, 1), repeat=4) if sum(w) % 2 == 0}
    require(set(WORDS) == parity_universe and len(WORDS) == 8,
            "SUPPLIED_PARITY_SUPPORT", WORDS)
    graphs, equations = flatten_and_derive(WORDS)
    require(equations == EXPECTED_PHASE_ROWS, "PHASE_EQUATION_BINDING", equations)
    rhs = (1,) * len(equations)
    discovered = discover_relation(equations, rhs)
    readable = certify_integer_relation(equations, rhs, READABLE_RELATION)

    mutations = []
    mutations.append(expect_rejection("maximal count changed 24 to 23", "MAXIMAL_WORD_COUNT",
                     lambda: check_histogram((0, 0, 24, 0, 0), 23, 48, 24)))
    mutations.append(expect_rejection("second shadow moment changed 24 to 25", "SHADOW_SECOND_MOMENT",
                     lambda: check_histogram((0, 0, 24, 0, 0), 24, 48, 25)))
    shifted, _ = enumerate_shadows(second_shift=1)
    mutations.append(expect_rejection("enumeration with changed M offset", "HISTOGRAM_SET_MISMATCH",
                     lambda: compare_sets((4, 4, 4, 4), shifted[(4, 4, 4, 4)],
                                          RAW_EXPECTED[(4, 4, 4, 4)], "M+1 mutation")))
    omitted = set(CLAIMED[(4, 5, 5, 5)]) - {(1, 0, 3, 20, 0)}
    mutations.append(expect_rejection("omit one claimed histogram", "HISTOGRAM_SET_MISMATCH",
                     lambda: compare_sets((4, 5, 5, 5), restricted[(4, 5, 5, 5)],
                                          omitted, "incomplete claimed set")))
    for q in ((4, 5, 5, 5), (5, 5, 5, 5)):
        weakened = dict(bounds)
        weakened[q] += 1
        bad = apply_separate_bounds(raw, weakened)
        mutations.append(expect_rejection("weaken pair bound " + "".join(map(str, q)),
                         "HISTOGRAM_SET_MISMATCH",
                         lambda q=q, bad=bad: compare_sets(q, bad[q], CLAIMED[q], "weakened n1 bound")))
    mutations.append(expect_rejection("delete support word 0000", "PAIR_DEGREE",
                     lambda: flatten_and_derive(WORDS[1:])))
    bad_relation = (1, 0, 1, 0, 0, 1)
    mutations.append(expect_rejection("GF2-only false phase certificate", "PHASE_INTEGER_LHS",
                     lambda: certify_integer_relation(equations, rhs, bad_relation)))
    changed_rhs = list(rhs)
    changed_rhs[5] = 0
    mutations.append(expect_rejection("single selected phase RHS changed pi to zero", "PHASE_RHS_EVEN",
                     lambda: certify_integer_relation(equations, tuple(changed_rhs), READABLE_RELATION)))
    # Strong equation-only positive control: theta_0000=pi, all other phases=0.
    # Changing RHS rows 1,3,5 to zero (zero-based) makes all six congruences
    # consistent. This mutated system is NOT physical block orthogonality.
    theta_units = (1, 0, 0, 0, 0, 0, 0, 0)
    consistent_rhs = (1, 0, 1, 0, 1, 0)
    require(tuple(sum(a*b for a, b in zip(row, theta_units)) % 2 for row in equations)
            == consistent_rhs, "PHASE_POSITIVE_CONTROL", "explicit solution failed")
    mutations.append(expect_rejection("known-consistent mutated phase RHS", "PHASE_RHS_EVEN",
                     lambda: certify_integer_relation(equations, consistent_rhs, READABLE_RELATION)))
    tick()
    receipt = {
        "status": "PASS", "scope": "finite shadows and the supplied eight-word phase obstruction only",
        "input_metadata_attribution": "Assigned pins are parent-supplied; not rehashed source files",
        "manifest_sha256": "34bf20954abd0fa0726e4aaf23da6cfed378312c3190760760616a95f3cd105d",
        "freeze_receipt_sha256": "997bea41ab082f3196e1e68d36fff60d4fd2ffc4e83d48ae9716db7240d44387",
        "packet_sha256": "fa0807349a97a80a89f24256dd1631d6c7c5ebd3fbd288ef5c4eec2205778027",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "profile_count": len(PROFILES), "weak_compositions_examined_per_baseline_pass": count,
        "profiles": [{"q": q, "C": target(q)[0], "M": target(q)[1],
                      "pair_capacity": all(q[i]*q[j] >= 12 for i, j in combinations(range(4), 2)),
                      "raw_histograms": sorted(raw[q]),
                      "after_separate_bounds": sorted(restricted[q])} for q in PROFILES],
        "outside_footprint_bounds": [{"q": q, **footprint_results[q]} for q in footprint_results],
        "forced_degree_shadows": degrees, "support_word_order": [word_text(w) for w in WORDS],
        "flattenings": graphs, "phase_equations_in_cut_block_order": equations,
        "phase_rhs_pi_units": rhs, "discovered_integer_certificate": discovered,
        "readable_integer_certificate": readable, "intended_rejections": mutations,
        "phase_positive_control": {"theta_pi_units": theta_units, "rhs_pi_units": consistent_rhs,
                                   "meaning": "mutated equations only; not a physical tensor"},
        "elapsed_seconds": time.perf_counter() - START,
        "limitations": ["No full tensor/support enumeration", "No global t=24 exclusion",
                        "No no-OLS(6) waiver", "No novelty or independent-model-family acceptance"],
    }
    print(json.dumps(receipt, sort_keys=True, indent=2))


if __name__ == "__main__":
    try:
        main()
    except VerificationError as error:
        print("FAIL " + error.code + ": " + repr(error.detail), file=sys.stderr)
        sys.exit(1)
