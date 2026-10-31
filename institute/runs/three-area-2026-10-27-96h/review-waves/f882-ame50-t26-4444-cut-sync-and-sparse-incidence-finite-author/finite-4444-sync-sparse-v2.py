#!/usr/bin/env python3
"""UNRUN v2 exact necessary-support scrutiny; supersedes the UNRUN v1 file.

Scope: AME(4,6), N=50, t=26, q=4444 local models only.  This is NOT a global
P/E enumeration, NOT a phase solver and NOT an AME feasibility test.
Requires a full parent source read and a separate one-shot GO before any run.
No input files, output files, subprocesses, randomness, network or external
packages.  All mathematics is integer/set arithmetic; only the monotonic clock
uses floating point.  Parent outer supervision must be at most 55 seconds; the
program interrupts itself by 39 seconds and then prints INCOMPLETE, never PASS.
Every status line is one flushed JSON object on stdout.
"""

from collections import Counter, defaultdict
from itertools import combinations, product
import json
import signal
import sys
import time

START = time.monotonic()
INTERNAL_SECONDS = 39.0
CUTS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
PAIRS = tuple(combinations(range(4), 2))
WORDS = tuple(product(range(2), repeat=4))
AB_FULL = frozenset(((0, 0), (1, 1)))
AB_OTHER = tuple(p for p in product(range(4), repeat=2) if p not in AB_FULL)
LOW_CD = tuple(product((2, 3), repeat=2))
PARTITIONS = (
    ("axis_C", ((0, 1), (2, 3))),
    ("axis_D", ((0, 2), (1, 3))),
    ("diagonal", ((0, 3), (1, 2))),
)
DEGREE_MULTISETS = ([2, 2, 2, 4], [2, 2, 3, 3])
RULE_SETS = (
    ("multiplicity_only", False, False),
    ("multiplicity_CD_degree", False, True),
    ("multiplicity_one_overlap", True, False),
    ("all_core_rules", True, True),
)
CONTEXTS = ((2, 0), (2, 1), (3, 0), (3, 1))
PROGRESS = {"phase": "starting"}
CHECKS = []


class Deadline(Exception):
    pass


def alarm_handler(_signum, _frame):
    raise Deadline("internal deadline")


def guard():
    if time.monotonic() - START >= INTERNAL_SECONDS:
        raise Deadline("internal deadline")


def emit(status, **fields):
    print(json.dumps({"status": status, **fields}, sort_keys=True), flush=True)


def record(name, expected, observed):
    CHECKS.append({"name": name, "expected_by_written_source": expected,
                   "observed": observed, "agrees": expected == observed})


def popcount(x):
    return bin(x).count("1")


def pair_of(word, pair):
    return (word[pair[0]], word[pair[1]])


def complement(pair):
    return tuple(i for i in range(4) if i not in pair)


# ---------------------------------------------------------------- high Omega

def mask_cut_type(mask, left, right):
    """X: two complementary full 2x2 rectangles; Y: 16 minus a permutation."""
    n = popcount(mask)
    if n not in (8, 12):
        return "other"
    rows = [0, 0, 0, 0]
    for k, w in enumerate(WORDS):
        if mask >> k & 1:
            rows[2 * w[left[0]] + w[left[1]]] |= 1 << (2 * w[right[0]] + w[right[1]])
    row_sizes = [popcount(r) for r in rows]
    col_sizes = [sum(r >> c & 1 for r in rows) for c in range(4)]
    if n == 12:
        return "Y" if row_sizes == [3] * 4 and col_sizes == [3] * 4 else "other"
    if row_sizes != [2] * 4:
        return "other"
    distinct = sorted(set(rows))
    if len(distinct) != 2 or rows.count(distinct[0]) != 2:
        return "other"
    a, b = distinct
    return "X" if a & b == 0 and a | b == 15 else "other"


def parity_masks():
    masks = set()
    for coords in combinations(range(4), 3):
        for parity in (0, 1):
            masks.add(sum(1 << k for k, w in enumerate(WORDS)
                          if sum(w[i] for i in coords) % 2 == parity))
    for parity in (0, 1):
        masks.add(sum(1 << k for k, w in enumerate(WORDS) if sum(w) % 2 == parity))
    return masks


def high_support_scrutiny():
    table = Counter()
    x_all, y_all = [], []
    x_cut0 = y_cut1 = 0
    for mask in range(1 << 16):
        if mask % 1024 == 0:
            guard()
        types = tuple(mask_cut_type(mask, left, right) for left, right in CUTS)
        table[(popcount(mask),) + types] += 1
        x_cut0 += types[0] == "X"
        y_cut1 += types[1] == "Y"
        if types == ("X", "X", "X"):
            x_all.append(mask)
        if types == ("Y", "Y", "Y"):
            y_all.append(mask)
    mixed = sum(n for key, n in table.items() if "X" in key[1:] and "Y" in key[1:])
    parity = parity_masks()
    zero_sets = [chosen for chosen in combinations(range(16), 4)
                 if all(len({pair_of(WORDS[k], p) for k in chosen}) == 4 for p in PAIRS)]
    record("three_cut_X_masks_are_exactly_ten_parity_masks", True,
           set(x_all) == parity and len(parity) == 10)
    record("three_cut_Y_masks", 0, len(y_all))
    record("six_pair_bijective_four_word_zero_sets", 0, len(zero_sets))
    record("one_mask_with_both_X_and_Y_cuts", 0, mixed)
    record("drop_common_tensor_mutant_has_independent_X_and_Y_masks", True,
           x_cut0 > 0 and y_cut1 > 0)
    return {
        "masks_visited": 1 << 16,
        "four_word_sets_visited": 1820,
        "size_and_cut_type_table": [
            {"size": key[0], "cuts": list(key[1:]), "count": n}
            for key, n in sorted(table.items())],
        "three_cut_X_masks": x_all,
        "parity_masks": sorted(parity),
        "three_cut_Y_masks": y_all,
        "six_pair_bijective_zero_sets": zero_sets,
        "independent_cut_mutant_counts": {"X_in_AB_CD": x_cut0, "Y_in_AC_BD": y_cut1},
    }


# ---------------------------------------------------------- single-F sparse

def cap(pair, value):
    if pair == (0, 1):
        return 4 if value in AB_FULL else 2
    return 3 if value[0] < 2 and value[1] < 2 else 2


def projections(words, pair):
    other = complement(pair)
    out = defaultdict(set)
    for word in words:
        out[pair_of(word, pair)].add(pair_of(word, other))
    return out


def saturated_one_overlap(words):
    """Two exact-capacity rows of one pair system meeting in one column."""
    for pair in PAIRS:
        rows = projections(words, pair)
        full = [(p, v) for p, v in sorted(rows.items()) if len(v) == cap(pair, p)]
        for (p, v), (q, z) in combinations(full, 2):
            common = v & z
            if len(common) == 1:
                return {"pair": list(pair), "rows": [p, q], "common": sorted(common)}
    return None


def partial_status(words, one_overlap=True, cd_degree=True):
    if len(set(words)) != len(words):
        return False, "duplicate_word"
    for pair in PAIRS:
        rows = projections(words, pair)
        for p, support in rows.items():
            if len(support) > cap(pair, p):
                return False, "pair_multiplicity"
        if not cd_degree:
            continue
        for side, party in enumerate(pair):
            if party not in (2, 3):
                continue
            for symbol in range(4):
                neighbors = {p[1 - side] for p in rows if p[side] == symbol}
                if len(neighbors) > (3 if symbol < 2 else 2):
                    return False, "CD_degree"
    if one_overlap and saturated_one_overlap(words) is not None:
        return False, "saturated_one_overlap"
    return True, "ok"


def core_words(row0, row1, support0, support1):
    words = [(a, b, c, d) for a, b in sorted(AB_FULL) for c, d in product(range(2), repeat=2)]
    for (a, b), support in ((row0, support0), (row1, support1)):
        words.extend((a, b, p // 2, p % 2) for p in support)
    return tuple(sorted(words))


def row_type(row):
    a, b = row
    return "X" if a < 2 and b < 2 else "Y" if a < 2 else "Z" if b < 2 else "W"


def closed_high_box(core):
    if any(any(x >= 2 for x in w) for w in core):
        return False
    for pair in PAIRS:
        rows = projections(core, pair)
        for value in product(range(2), repeat=2):
            if len(rows.get(value, ())) != cap(pair, value):
                return False
    return True


def context_options(core, varying_party, high_symbol):
    """AB values of the two low-partner words of one high C or high D symbol."""
    slice_words = [w for w in core if w[varying_party] == high_symbol]
    a_count = Counter(w[0] for w in slice_words)
    b_count = Counter(w[1] for w in slice_words)
    options = set()
    for low_a, low_b in product((2, 3), repeat=2):
        deficits = []
        for counts, low in ((a_count, low_a), (b_count, low_b)):
            target = {0: 3, 1: 3, low: 2, 5 - low: 0}
            delta = [target[x] - counts[x] for x in range(4)]
            if min(delta) < 0 or sum(delta) != 2:
                break
            deficits.append(tuple(x for x in range(4) for _ in range(delta[x])))
        if len(deficits) != 2:
            continue
        aa, bb = deficits
        for second in (bb, bb[::-1]):
            cells = tuple(sorted(((aa[0], second[0]), (aa[1], second[1]))))
            if cells[0] != cells[1]:
                options.add(cells)
    return tuple(sorted(options))


def context_words(party, symbol, low_partner, cells):
    if party == 2:
        return tuple((a, b, symbol, low_partner) for a, b in cells)
    return tuple((a, b, low_partner, symbol) for a, b in cells)


def ab_degree_candidates(words):
    counts = Counter((w[0], w[1]) for w in words)
    if any(counts[p] != 4 for p in AB_FULL):
        return
    used = {p for p in AB_OTHER if counts[p]}
    if any(counts[p] > 2 for p in used):
        return
    missing = 8 - len(used)
    if not 0 <= missing <= 2:
        return
    once = [p for p in used if counts[p] == 1]
    if len(once) + 2 * missing != 4:
        return
    for added in combinations([p for p in AB_OTHER if p not in used], missing):
        edges = set(AB_FULL) | used | set(added)
        da = sorted(sum(a == x for a, _ in edges) for x in range(4))
        db = sorted(sum(b == x for _, b in edges) for x in range(4))
        if da in DEGREE_MULTISETS and db in DEGREE_MULTISETS:
            yield tuple(sorted(once + [p for p in added for _ in range(2)]))


def low_cd_choices(words):
    rows = projections(words, (2, 3))
    count_c = Counter(w[2] for w in words)
    count_d = Counter(w[3] for w in words)
    for p, q in combinations(LOW_CD, 2):
        if any(count_c[c] + 2 * ((p[0] == c) + (q[0] == c)) != 4 for c in (2, 3)):
            continue
        if any(count_d[d] + 2 * ((p[1] == d) + (q[1] == d)) != 4 for d in (2, 3)):
            continue
        values = set(rows) | {p, q}
        if any(len({y for x, y in values if x == c}) != 2 for c in (2, 3)):
            continue
        if any(len({x for x, y in values if y == d}) != 2 for d in (2, 3)):
            continue
        yield p, q


def full_pair_degree_check(words):
    if len(words) != 24 or len(set(words)) != 24:
        return False
    for pair in PAIRS:
        rows = projections(words, pair)
        if len(rows) != 10:
            return False
        if any(len(support) != cap(pair, p) for p, support in rows.items()):
            return False
        needed = AB_FULL if pair == (0, 1) else set(product(range(2), repeat=2))
        if any(p not in rows for p in needed):
            return False
    for i in range(4):
        for x in range(4):
            degrees = [len({w[j] for w in words if w[i] == x}) for j in range(4) if j != i]
            if len(set(degrees)) != 1 or not 2 <= degrees[0] <= 4:
                return False
            if i in (2, 3) and degrees[0] != (3 if x < 2 else 2):
                return False
            if sum(w[i] == x for w in words) != 2 * degrees[0] + (2 if x < 2 else 0):
                return False
    return True


def cut_shape(words, left):
    graph = projections(words, left)
    if len(graph) != 10 or len({v for vs in graph.values() for v in vs}) != 10:
        return "other"
    unseen = set(graph)
    shapes = []
    while unseen:
        stack = [(0, next(iter(unseen)))]
        rows, cols = set(), set()
        while stack:
            side, value = stack.pop()
            if side == 0 and value not in rows:
                rows.add(value)
                unseen.discard(value)
                stack.extend((1, c) for c in graph[value])
            elif side == 1 and value not in cols:
                cols.add(value)
                stack.extend((0, r) for r, vs in graph.items() if value in vs)
        shapes.append((len(rows), len(cols), sum(len(graph[r] & cols) for r in rows)))
    shapes.sort()
    if shapes == [(2, 2, 4), (2, 2, 4), (3, 3, 8), (3, 3, 8)]:
        return "X"
    if shapes == [(2, 2, 4), (2, 2, 4), (2, 2, 4), (4, 4, 12)]:
        return "Y"
    return "other"


def complete_boundary(words):
    """Add the four low-C/low-D words at two distinct low-low CD values."""
    for deficits in ab_degree_candidates(words):
        for p, q in low_cd_choices(words):
            seen = set()
            for indices in combinations(range(4), 2):
                first = tuple(sorted(deficits[k] for k in indices))
                second = tuple(sorted(deficits[k] for k in range(4) if k not in indices))
                if first[0] == first[1] or second[0] == second[1] or (first, second) in seen:
                    continue
                seen.add((first, second))
                added = tuple((a, b) + p for a, b in first) + tuple((a, b) + q for a, b in second)
                result = tuple(sorted(words + added))
                if full_pair_degree_check(result):
                    yield result


def sparse_scrutiny():
    counts = Counter()
    samples = {}
    distinct = set()
    boxed_survivors = 0
    for row0, row1 in combinations(AB_OTHER, 2):
        label = "/".join(sorted((row_type(row0), row_type(row1))))
        for partition, (s0, s1) in PARTITIONS:
            for support0, support1 in ((s0, s1), (s1, s0)):
                guard()
                key = label + ":" + partition
                counts["core:" + key] += 1
                core = core_words(row0, row1, support0, support1)
                for rule, overlap_rule, degree_rule in RULE_SETS:
                    if partial_status(core, overlap_rule, degree_rule)[0]:
                        counts["core_accept_" + rule + ":" + key] += 1
                ok, reason = partial_status(core)
                if not ok:
                    counts["core_reject_" + reason + ":" + key] += 1
                    continue
                boxed = closed_high_box(core)
                if boxed:
                    counts["closed_box_core_not_used_to_reject:" + key] += 1
                options = [context_options(core, party, symbol) for party, symbol in CONTEXTS]
                if not all(options):
                    counts["context_marginal_reject:" + key] += 1
                    continue
                stack = [(0, core)]
                while stack:
                    guard()
                    depth, words = stack.pop()
                    if depth == len(CONTEXTS):
                        counts["high_boundary:" + key] += 1
                        for full in complete_boundary(words):
                            guard()
                            counts["pair_degree_completion:" + key] += 1
                            if saturated_one_overlap(full) is not None:
                                counts["final_one_overlap_reject:" + key] += 1
                                continue
                            types = tuple(cut_shape(full, left) for left, _ in CUTS)
                            if types[0] != "Y" or any(t not in ("X", "Y") for t in types[1:]):
                                counts["final_cut_shape_reject:" + key] += 1
                                continue
                            counts["strict_survivor:" + key] += 1
                            distinct.add(full)
                            boxed_survivors += boxed
                            samples.setdefault(key, {"cuts": types, "E": full,
                                                     "closed_box_core": boxed})
                        continue
                    party, symbol = CONTEXTS[depth]
                    for cells in options[depth]:
                        for low_partner in (2, 3):
                            grown = words + context_words(party, symbol, low_partner, cells)
                            ok, reason = partial_status(grown)
                            if ok:
                                stack.append((depth + 1, grown))
                            else:
                                counts["branch_reject_" + reason + ":" + key] += 1
    total = sum(n for k, n in counts.items() if k.startswith("strict_survivor:"))
    cores = sum(n for k, n in counts.items() if k.startswith("core:"))
    record("single_F_core_assignments", 546, cores)
    record("single_F_strict_survivor_completions", 0, total)
    record("single_F_closed_box_core_survivors", 0, boxed_survivors)
    return {"core_assignments": cores, "strict_survivor_completions": total,
            "distinct_strict_survivor_E_sets": len(distinct),
            "counts_by_stage_and_type_partition": dict(sorted(counts.items())),
            "strict_survivor_examples": samples}


# -------------------------------------------- I/II, star, reason mutants

def degree_vector(graph, side):
    return tuple(sum(edge[side] == x for edge in graph) for x in range(4))


def matching_cases():
    m0 = ((1, 0), (2, 2))
    m1 = ((1, 2), (2, 0))
    cases = (("I", ((0, 1), (2, 2))), ("II", ((0, 2), (2, 1))))
    written7 = ((2, 3, 3, 2), (3, 2, 3, 2))
    result = {}
    for name, sparse in cases:
        surviving, general, seven = [], [], []
        for choices in product((0, 1), repeat=4):
            counts = Counter({(0, 0): 4, (1, 1): 4, sparse[0]: 2, sparse[1]: 2})
            for choice in choices:
                counts.update(m1 if choice else m0)
            if any(n > (4 if p in AB_FULL else 2) for p, n in counts.items()):
                continue
            surviving.append(choices)
            used = {p for p, n in counts.items() if n}
            free = [p for p in product(range(4), repeat=2) if p not in used]
            for added in combinations(free, max(0, 10 - len(used))):
                graph = used | set(added)
                da, db = degree_vector(graph, 0), degree_vector(graph, 1)
                if sorted(da) in DEGREE_MULTISETS and sorted(db) in DEGREE_MULTISETS:
                    general.append([choices, added])
                if (da, db) == written7:
                    seven.append([choices, added])
        result[name] = {"capacity_surviving_assignments": surviving,
                        "general_degree_completions": general,
                        "written_7_degree_completions": seven}
    record("case_I_capacity_surviving_assignments", 0,
           len(result["I"]["capacity_surviving_assignments"]))
    record("case_II_capacity_surviving_assignments", 6,
           len(result["II"]["capacity_surviving_assignments"]))
    record("case_I_II_general_degree_completions", 0,
           sum(len(r["general_degree_completions"]) for r in result.values()))
    record("case_I_II_written_7_degree_completions", 0,
           sum(len(r["written_7_degree_completions"]) for r in result.values()))
    return result


def star_scrutiny():
    propagated, unconstrained = [], 0
    for bits in product((0, 1), repeat=6):
        unconstrained += 1
        endpoint = {edge: edge[bits[k]] for k, edge in enumerate(PAIRS)}
        if all(endpoint[e] == v for v in endpoint.values() for e in PAIRS if v in e):
            propagated.append(bits)
    record("four_bit_star_propagated_orientations", 0, len(propagated))
    record("drop_propagation_mutant_orientations", 64, unconstrained)
    return {"orientations": unconstrained, "propagated": propagated}


def one_overlap_mutant():
    fixture = core_words((0, 2), (1, 2), (0, 3), (1, 2))
    relaxed = partial_status(fixture, one_overlap=False)
    strict = partial_status(fixture)
    witness = saturated_one_overlap(fixture)
    record("drop_one_overlap_mutant_accepts_YY_fixture", [True, "ok"], list(relaxed))
    record("one_overlap_rejects_YY_fixture", [False, "saturated_one_overlap"], list(strict))
    return {"fixture_E": fixture, "relaxed": list(relaxed), "strict": list(strict),
            "witness": witness}


def main():
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, INTERNAL_SECONDS)
    emit("START", version=2, internal_seconds=INTERNAL_SECONDS, parent_outer_limit_at_most=55,
         model="conditional necessary local supports only; no P, phases or AME feasibility")
    try:
        for phase, function in (("high_support", high_support_scrutiny),
                                ("I_II_matching", matching_cases),
                                ("four_bit_star", star_scrutiny),
                                ("one_overlap_mutant", one_overlap_mutant),
                                ("single_F_sparse", sparse_scrutiny)):
            PROGRESS["phase"] = phase
            emit("PHASE_START", phase=phase)
            emit("PHASE_COMPLETE", phase=phase, result=function())
        signal.setitimer(signal.ITIMER_REAL, 0)
        disagreements = [c for c in CHECKS if not c["agrees"]]
        emit("COMPLETE_ALL_AGREE" if not disagreements else "COMPLETE_WITH_DISAGREEMENTS",
             elapsed_seconds=round(time.monotonic() - START, 3), checks=CHECKS,
             disagreements=disagreements,
             qualification="conditional finite necessary-support models only")
        sys.exit(0 if not disagreements else 3)
    except Deadline:
        signal.setitimer(signal.ITIMER_REAL, 0)
        emit("INCOMPLETE_TIMEOUT", phase=PROGRESS["phase"], checks_so_far=CHECKS,
             qualification="not exhaustive; not a PASS")
        sys.exit(124)
    except Exception as error:
        signal.setitimer(signal.ITIMER_REAL, 0)
        emit("ERROR", phase=PROGRESS["phase"], error=repr(error), checks_so_far=CHECKS,
             qualification="not exhaustive; not a PASS")
        sys.exit(1)


if __name__ == "__main__":
    main()
