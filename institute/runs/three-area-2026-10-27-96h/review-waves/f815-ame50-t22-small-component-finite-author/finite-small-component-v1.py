#!/usr/bin/env python3
"""Bounded local exact checks for a 12-word 2333 interface.

UNRUN source.  Intended invocation after a separate, source-bound GO:
    python3 -I -B -S finite-small-component-v1.py
No input files, third-party modules, output files, or network are used.  JSON
on stdout is the only output.  A COMPLETE_LOCAL result is only a result of
these explicitly finite checks; it is never a physical P completion.
"""

import itertools
import json
import math
import signal
import sys
import time
from collections import Counter


START = time.monotonic()
DEADLINE = START + 40.0
STOP = {"signal": None}
PROGRESS = {"completed_sections": []}


class StopWork(Exception):
    pass


class ReasonFailure(Exception):
    pass


def signal_stop(number, _frame):
    STOP["signal"] = int(number)


def guard():
    if STOP["signal"] is not None:
        raise StopWork("signal_" + str(STOP["signal"]))
    if time.monotonic() >= DEADLINE:
        raise StopWork("internal_40_second_deadline")


def need(condition, reason):
    if not condition:
        raise ReasonFailure(reason)


def pairs():
    return tuple(itertools.combinations(range(4), 2))


def pair_counts(words):
    return [Counter((word[i], word[j]) for word in words) for i, j in pairs()]


def pair_conditions(words):
    if len(words) != 12 or len(set(words)) != 12:
        return False, "word_count_or_duplicates"
    for counts in pair_counts(words):
        if len(counts) != 6 or any(n != 2 for n in counts.values()):
            return False, "pair_multiplicity"
    return True, "ok"


def triple_graph(triples):
    graph = [set() for _ in triples]
    for i, j in itertools.combinations(range(len(triples)), 2):
        shared = sum(triples[i][k] == triples[j][k] for k in range(3))
        if shared > 1:
            return None
        if shared == 1:
            graph[i].add(j)
            graph[j].add(i)
    return graph


def bipartite(graph):
    colors = {}
    for start in range(len(graph)):
        if start in colors:
            continue
        colors[start] = 0
        stack = [start]
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if v in colors:
                    if colors[v] == colors[u]:
                        return False
                else:
                    colors[v] = 1 - colors[u]
                    stack.append(v)
    return True


def graph_edges(graph):
    return tuple((u, v) for u in range(len(graph)) for v in graph[u] if u < v)


def signings(graph):
    edges = graph_edges(graph)
    return [signs for signs in itertools.product((-1, 1), repeat=len(graph))
            if all(signs[u] == -signs[v] for u, v in edges)]


def words_from_triples(triples):
    return {tuple(t) + (d,) for t in triples for d in range(2)}


def local_component(triples):
    """Check all six physical pair counts and all three actual cut blocks."""
    words = words_from_triples(triples)
    ok, why = pair_conditions(words)
    if not ok:
        return False, why
    all_squares = set()
    for row_axes in ((0, 1), (0, 2), (0, 3)):
        col_axes = tuple(k for k in range(4) if k not in row_axes)
        rows = {}
        cols = {}
        for w in words:
            r = tuple(w[k] for k in row_axes)
            c = tuple(w[k] for k in col_axes)
            rows.setdefault(r, set()).add(c)
            cols.setdefault(c, set()).add(r)
        if len(rows) != 6 or len(cols) != 6:
            return False, "active_shape"
        if any(len(x) != 2 for x in rows.values()) or any(len(x) != 2 for x in cols.values()):
            return False, "line_degree"
        cut_squares = set()
        for r, cs in rows.items():
            c0, c1 = sorted(cs)
            if cols[c0] != cols[c1] or r not in cols[c0]:
                return False, "not_k22"
            rs = cols[c0]
            square = frozenset(w for w in words
                               if tuple(w[k] for k in row_axes) in rs
                               and tuple(w[k] for k in col_axes) in cs)
            if len(square) != 4:
                return False, "not_four_corners"
            cut_squares.add(square)
        if len(cut_squares) != 3:
            return False, "not_three_blocks"
        all_squares.update(cut_squares)
    triples = tuple(sorted(triples))
    graph = triple_graph(triples)
    if graph is None or any(len(nbrs) != 3 for nbrs in graph):
        return False, "triple_graph_not_simple_cubic"
    edge_squares = set()
    for i, j in graph_edges(graph):
        edge_squares.add(frozenset((triples[i] + (0,), triples[i] + (1,),
                                    triples[j] + (0,), triples[j] + (1,))))
    if len(edge_squares) != 9 or all_squares != edge_squares:
        return False, "edge_square_correspondence"
    return True, "ok"


def gadget():
    left = {(i, i, i) for i in range(3)}
    right = {(i, (i - 1) % 3, (i + 1) % 3) for i in range(3)}
    return left | right


def gadget_orbit():
    permutations = tuple(itertools.permutations(range(3)))
    original = gadget()
    orbit = set()
    for axes in permutations:
        for relabel in itertools.product(permutations, repeat=3):
            orbit.add(frozenset(tuple(relabel[k][t[axes[k]]] for k in range(3))
                                for t in original))
    return orbit


def graph_section():
    edges = tuple(itertools.combinations(range(6), 2))
    total = bip = signed = 0
    for index, picked in enumerate(itertools.combinations(edges, 9)):
        if index % 128 == 0:
            guard()
        graph = [set() for _ in range(6)]
        for u, v in picked:
            graph[u].add(v)
            graph[v].add(u)
        if any(len(a) != 3 for a in graph):
            continue
        total += 1
        good = signings(graph)
        is_bip = bipartite(graph)
        need(bool(good) == is_bip, "graph_sign_bipartite_disagreement")
        if is_bip:
            bip += 1
            need(len(good) == 2, "connected_cubic_bipartite_sign_count")
            signed += len(good)
    need((total, bip, signed) == (70, 10, 20), "labelled_graph_known_counts")
    k33 = [set(range(3, 6)) for _ in range(3)] + [set(range(3)) for _ in range(3)]
    prism_edges = ((0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5),
                   (0, 3), (1, 4), (2, 5))
    prism = [set() for _ in range(6)]
    for u, v in prism_edges:
        prism[u].add(v)
        prism[v].add(u)
    need(len(signings(k33)) == 2 and bipartite(k33), "k33_positive_control")
    need(not signings(prism) and not bipartite(prism), "prism_odd_cycle_control")
    return {"edge_subsets_examined": math.comb(15, 9),
            "labelled_simple_cubic_graphs": total, "bipartite_graphs": bip,
            "signed_labelled_graph_pairs": signed,
            "reason_controls": ["k33_two_signings", "triangular_prism_no_signing"]}


def fiber_section():
    # Four distinct B,C,D words in one fixed A fiber.  In a 3333
    # component every coordinate appears as two values, twice each.
    # Every selected 2x2 pair rectangle has at least one missing cell.
    universe = tuple(itertools.product(range(3), repeat=3))
    balanced = all_missing = single_pair_mutant = 0
    for index, fiber in enumerate(itertools.combinations(universe, 4)):
        if index % 256 == 0:
            guard()
        if any(sorted(Counter(t[k] for t in fiber).values()) != [2, 2] for k in range(3)):
            continue
        balanced += 1
        sizes = [len({(t[i], t[j]) for t in fiber})
                 for i, j in ((0, 1), (0, 2), (1, 2))]
        if all(size <= 3 for size in sizes):
            all_missing += 1
        if sizes[0] <= 3:
            single_pair_mutant += 1
    need(all_missing == 0, "3333_fiber_obstruction")
    witness = ((0, 0, 0), (0, 0, 1), (1, 1, 0), (1, 1, 1))
    need(all(sorted(Counter(t[k] for t in witness).values()) == [2, 2] for k in range(3)),
         "fiber_mutant_balanced")
    need(len({(t[0], t[1]) for t in witness}) <= 3 and
         len({(t[0], t[2]) for t in witness}) == 4 and single_pair_mutant > 0,
         "fiber_omitted_pair_requirements_mutant")
    return {"four_triple_subsets_examined": math.comb(27, 4),
            "balanced_fibers": balanced, "all_three_pair_deficits": all_missing,
            "one_pair_only_mutant_survivors": single_pair_mutant,
            "reason_controls": ["one_pair_deficit_only_has_balanced_witness"]}


def triple_section():
    universe = tuple(itertools.product(range(3), repeat=3))
    base = gadget()
    ok, why = local_component(base)
    need(ok, "canonical_gadget_" + why)
    invalid = set(base)
    invalid.remove((0, 2, 1))
    invalid.add((0, 0, 1))
    ok, why = pair_conditions(words_from_triples(invalid))
    need(not ok and why == "pair_multiplicity", "duplicate_ab_pair_mutant")
    missing = words_from_triples(base)
    missing.remove((0, 0, 0, 0))
    ok, why = pair_conditions(missing)
    need(not ok and why == "word_count_or_duplicates", "missing_word_mutant")
    triples = tuple(sorted(base))
    graph = triple_graph(triples)
    signs = tuple(1 if t[0] == t[1] == t[2] else -1 for t in triples)
    need(all(signs[u] == -signs[v] for u, v in graph_edges(graph)), "gadget_phase_control")
    flipped = (-signs[0],) + signs[1:]
    need(any(flipped[u] == flipped[v] for u, v in graph_edges(graph)), "phase_flip_mutant")
    orbit = gadget_orbit()
    need(len(orbit) == 36, "canonical_relabeling_orbit_size")
    physical_triples = set()
    phase_triples = set()
    examined = 0
    for index, choice in enumerate(itertools.combinations(universe, 6)):
        if index % 256 == 0:
            guard()
        examined += 1
        if any(sorted(Counter(t[k] for t in choice).values()) != [2, 2, 2]
               for k in range(3)):
            continue
        if any(len({(t[i], t[j]) for t in choice}) != 6
               for i, j in ((0, 1), (0, 2), (1, 2))):
            continue
        support = frozenset(choice)
        physical_triples.add(support)
        ok, why = local_component(support)
        need(ok, "valid_six_triples_local_" + why)
        graph = triple_graph(choice)
        phase_ok = bipartite(graph)
        signs_for_graph = signings(graph)
        need(bool(signs_for_graph) == phase_ok, "triple_graph_phase_equivalence")
        if phase_ok:
            need(len(signs_for_graph) == 2, "triple_graph_two_signings")
            phase_triples.add(support)
    need(examined == math.comb(27, 6), "triple_enumeration_incomplete")
    need(len(physical_triples) == 144, "six_triple_incidence_count")
    need(phase_triples == orbit, "canonical_orbit_equivalence")
    need(len(phase_triples) == 36, "phase_triple_count")
    return {"six_triple_subsets_examined": examined,
            "pair_compatible_triple_sets": len(physical_triples),
            "bipartite_triple_sets": len(phase_triples),
            "phase_signings_on_labeled_triple_sets": 2 * len(phase_triples),
            "canonical_symbol_and_party_relabel_orbit": len(orbit),
            "reason_controls": ["canonical_all_cuts_and_six_pairs", "duplicate_ab_pair",
                                "missing_word", "single_triple_phase_flip"]}


def degree_multisets(q, cap):
    return [x for x in itertools.combinations_with_replacement(range(2, cap + 1), q)
            if sum(x) == 14]


def moments(profile):
    first = 6 * sum(profile) - 56
    second = sum(profile[i] * profile[j] for i, j in itertools.combinations(range(4), 2)) - 84
    full = profile.count(6)
    solutions = []
    for n0 in range(23):
        for n1 in range(23 - n0):
            for n2 in range(23 - n0 - n1):
                for n3 in range(23 - n0 - n1 - n2):
                    n = (n0, n1, n2, n3, 22 - n0 - n1 - n2 - n3)
                    if any(n[k] for k in range(full)):
                        continue
                    if sum(k * n[k] for k in range(5)) != first:
                        continue
                    if sum((k * (k - 1) // 2) * n[k] for k in range(5)) == second:
                        solutions.append(n)
    return first, second, solutions


def cross_capacity(nx12, ny16, nz12, nz16, e12, e16, unused_z):
    demand = nx12 * ny16
    caps = (nz12 * nx12 - e12, nz16 * ny16 - e16, unused_z * ny16)
    need(min(caps) >= 0, "negative_cross_cell_capacity")
    return {"required_distinct_P_words": demand, "capacity_classes": caps,
            "total_capacity": sum(caps)}


def capacity_section():
    expected_moments = {
        (3, 5, 6, 6): (64, 63, [(0, 0, 3, 18, 1)]),
        (3, 6, 6, 6): (70, 78, [(0, 0, 0, 18, 4)]),
        (4, 4, 5, 6): (58, 50, [(0, 0, 8, 14, 0)]),
    }
    moment_results = {}
    for profile, expected in expected_moments.items():
        guard()
        got = moments(profile)
        need(got == expected, "profile_moments_" + str(profile))
        moment_results["".join(map(str, profile))] = {"S1": got[0], "S2": got[1], "n0_to_n4": got[2][0]}
    need(degree_multisets(3, 5) == [(4, 5, 5)], "3566_degree_three")
    need(degree_multisets(5, 3) == [(2, 3, 3, 3, 3)], "3566_degree_five")
    need(degree_multisets(6, 3) == [(2, 2, 2, 2, 3, 3)], "degree_six")
    need(degree_multisets(3, 6) == [(2, 6, 6), (3, 5, 6), (4, 4, 6), (4, 5, 5)],
         "3666_degree_three")
    need(degree_multisets(4, 4) == [(2, 4, 4, 4), (3, 3, 4, 4)], "4456_degree_four")
    need(degree_multisets(5, 4) == [(2, 2, 2, 4, 4), (2, 2, 3, 3, 4), (2, 3, 3, 3, 3)],
         "4456_degree_five")
    # At a fixed D, exactly five pairs with unused A/B/C symbols require P;
    # at most two such incidences can belong to one P word.  The control
    # below keeps the number of words and the incidence total separate.
    need((5 + 1) // 2 == 3 and 6 - ((5 + 1) // 2) == 3, "4456_D_degree_bound")
    for p_words, expected_double in ((3, 2), (4, 1)):
        double = 5 - p_words
        single = p_words - double
        need((double, single) == (expected_double, p_words - expected_double), "4456_D_mask_counts")
    # Exactly two P holes in a 4x4 pair graph.  Count both ordered profiles.
    cells = tuple(itertools.product(range(4), repeat=2))
    hole_types = Counter()
    for holes in itertools.combinations(cells, 2):
        row = tuple(sorted(4 - sum(a == i for a, _ in holes) for i in range(4)))
        col = tuple(sorted(4 - sum(b == j for _, b in holes) for j in range(4)))
        hole_types[(row, col)] += 1
    d2444, d3344 = (2, 4, 4, 4), (3, 3, 4, 4)
    need(hole_types == {(d2444, d3344): 24, (d3344, d2444): 24,
                        (d3344, d3344): 72}, "4456_two_hole_classification")
    need(hole_types.get((d2444, d2444), 0) == 0, "4456_two_concentrated_holes")
    # C12 ternary at a four-symbol party: enumerate labelled alphabets and
    # every nonnegative component-16 degree vector with sum eight.
    ternary_profiles = set()
    ternary_q16 = Counter()
    for s12 in itertools.combinations(range(4), 3):
        for q16 in (2, 3, 4):
            for s16 in itertools.combinations(range(4), q16):
                if len(set(s12) | set(s16)) != 4:
                    continue
                for ds in itertools.product(range(2, 5), repeat=q16):
                    if sum(ds) != 8:
                        continue
                    d = [2 if i in s12 else 0 for i in range(4)]
                    for i, value in zip(s16, ds):
                        d[i] += value
                    if max(d) <= 4:
                        ternary_profiles.add(tuple(sorted(d)))
                        ternary_q16[q16] += 1
    need(ternary_profiles == {d2444} and ternary_q16[2] == 0 and
         ternary_q16[3] > 0 and ternary_q16[4] > 0, "4456_ternary_degree_enumeration")
    # At the binary 12-component party, overlap with C16 has degree >=5,
    # so the two 16-symbols are disjoint and each has degree four.  Thus
    # C16 uses four D symbols.  Compare 3+4 in six with the seven-symbol mutant.
    def disjoint_counts(universe_size):
        return sum(not (set(a) & set(b))
                   for a in itertools.combinations(range(universe_size), 3)
                   for b in itertools.combinations(range(universe_size), 4))
    need(disjoint_counts(6) == 0 and disjoint_counts(7) > 0, "4456_full_party_pigeonhole")
    cross = {
        "3666_binary_at_three_symbol_party": cross_capacity(3, 3, 3, 3, 6, 8, 0),
        "3666_binary_at_full_party": cross_capacity(3, 3, 2, 4, 6, 8, 0),
        "3566_binary_at_five_symbol_party": cross_capacity(3, 3, 2, 3, 6, 8, 1),
    }
    need(all(x["required_distinct_P_words"] > x["total_capacity"] for x in cross.values()),
         "cross_cell_capacity_contradiction")
    # 3566 with the 12-binary party A (q_A=3): C16 must use all A,
    # with degrees (2,3,3), because its three-symbol full partner bounds
    # each degree by three.  Enumerate the two overlapping binary symbols.
    strict = relaxed = 0
    for s12 in itertools.combinations(range(3), 2):
        for ds in set(itertools.permutations((2, 3, 3))):
            total = [ds[i] + (3 if i in s12 else 0) for i in range(3)]
            strict += max(total) <= 5
            relaxed += max(total) <= 6
    need(strict == 0 and relaxed > 0, "3566_binary_A_degree_cap")
    # 3566 with 12-binary X (one full party): its ternary A/B pair
    # graph is K3,3 minus a matching.  A16 has all 3 A symbols and
    # 8 pair cells, all disjoint from the 6 C12 cells.  Enumerate the
    # 8-subsets of the 9 remaining A x B cells.  Every C16-used B
    # symbol must have at least 2 A neighbors.
    e12 = {(a, b) for a in range(3) for b in range(3) if a != b}
    available = tuple((a, b) for a in range(3) for b in range(5) if (a, b) not in e12)
    survivors = mutant = 0
    for chosen in itertools.combinations(available, 8):
        row = [sum(a == i for a, _ in chosen) for i in range(3)]
        col = [sum(b == i for _, b in chosen) for i in range(5)]
        global_a = sorted(2 + d for d in row)
        global_b = sorted((2 if i < 3 else 0) + col[i] for i in range(5))
        base = (global_a == [4, 5, 5] and global_b == [2, 3, 3, 3, 3]
                and sum(d > 0 for d in col) <= 4)
        if base and all(d == 0 or d >= 2 for d in col):
            survivors += 1
        if base and all(d == 0 or d >= 1 for d in col):
            mutant += 1
    need(len(available) == 9 and survivors == 0 and mutant > 0, "3566_binary_X_pair_cells")
    return {"profile_moments": moment_results,
            "4456_two_hole_counts": {"row2444_col3344": 24, "row3344_col2444": 24,
                                     "row3344_col3344": 72, "both2444": 0},
            "4456_ternary_q16_labelled_counts": dict(ternary_q16),
            "cross_cell_capacities": cross,
            "3566_binary_A_strict_survivors": strict,
            "3566_binary_A_relaxed_cap_mutant_survivors": relaxed,
            "3566_binary_X_pair_cell_survivors": survivors,
            "3566_binary_X_degree_one_mutant_survivors": mutant,
            "reason_controls": ["moment_vectors", "degree_multisets", "4456_outside_incidence",
                                "two_hole_types", "ternary_component_degree_vectors",
                                "seven_symbol_disjointness_mutant", "cross_cell_capacity",
                                "3566_relaxed_global_degree", "3566_degree_one_mutant"]}


def main():
    result = {"status": "INCOMPLETE", "completed_sections": PROGRESS["completed_sections"],
              "physical_P_completion": "NOT_ENUMERATED", "physical_P_candidates_examined": 0,
              "scope": "bounded local incidence, phase graph, and necessary capacity checks only"}
    try:
        signal.signal(signal.SIGINT, signal_stop)
        signal.signal(signal.SIGTERM, signal_stop)
        guard()
        if len(sys.argv) != 1:
            raise ReasonFailure("arguments_not_permitted")
        for name, function in (("labelled_graphs", graph_section), ("3333_fibers", fiber_section),
                               ("six_abc_triples", triple_section), ("profile_capacity", capacity_section)):
            guard()
            result[name] = function()
            PROGRESS["completed_sections"].append(name)
        guard()
        result["status"] = "COMPLETE_LOCAL"
    except StopWork as exc:
        result["status"] = "INCOMPLETE"
        result["reason"] = str(exc)
    except Exception as exc:
        result["status"] = "FAILED"
        result["reason"] = type(exc).__name__ + ": " + str(exc)
    finally:
        result["elapsed_seconds"] = round(time.monotonic() - START, 6)
        print(json.dumps(result, sort_keys=True, separators=(",", ":")), flush=True)
    return 0 if result["status"] == "COMPLETE_LOCAL" else 2


if __name__ == "__main__":
    sys.exit(main())
