#!/usr/bin/env python3
"""Prospective f658 local assay. NOT RUN by its author; see accompanying narrative.

No input files, network, subprocesses, or writes. All output is JSON on stdout.
The model deliberately does NOT certify an eleven-row array. A time limit produces
INCOMPLETE, never a pass. Parent must inspect and separately authorize execution.
"""
import itertools
import json
import sys
import time
from functools import lru_cache

A, B, C, D = range(4)  # I, L, J, K respectively; A/B and C/D are opposite.
CELLS = tuple(tuple(range(3 * c, 3 * c + 3)) for c in range(4))
VERTICES = frozenset(range(12))
OPP = {A: B, B: A, C: D, D: C}
ALL_INTERNAL = {
    (u, v) for cell in CELLS for u in cell for v in cell if u != v
}
START = time.monotonic()
DEADLINE = START + 50.0


class Reject(Exception):
    def __init__(self, code, detail=None):
        super().__init__(code)
        self.code = code
        self.detail = detail


class Incomplete(Exception):
    pass


def guard():
    if time.monotonic() >= DEADLINE:
        raise Incomplete()


def require(condition, code, detail=None):
    if not condition:
        raise Reject(code, detail)


def cell(v):
    return v // 3


def third(c, x, y):
    require(x != y and x in CELLS[c] and y in CELLS[c], "BAD_SEGMENT")
    return next(v for v in CELLS[c] if v != x and v != y)


def premises(m_eq_c, two_tripled, cells):
    # These are declarations, not a test that an actual array has the premises.
    require(m_eq_c is True and two_tripled is True, "ASSUMPTION_NOT_DECLARED")
    require(tuple(cells) == CELLS and len(set().union(*map(set, cells))) == 12,
            "CELL_LABELS")


def check_successor(succ):
    require(set(succ) == VERTICES and set(succ.values()) == VERTICES,
            "SUCCESSOR_NOT_PERMUTATION")
    seen = set()
    v = 0
    while v not in seen:
        seen.add(v)
        v = succ[v]
    require(v == 0 and seen == VERTICES, "DISCONNECTED_COVER")


def physical(row):
    require(len(row) == 12 and set(row) == VERTICES, "VERTEX_MULTISET")
    succ = {row[i]: row[(i + 1) % 12] for i in range(12)}
    check_successor(succ)
    arcs = frozenset((v, succ[v]) for v in row)
    squares = frozenset((v, succ[succ[v]]) for v in row)
    require(len(arcs) == 12 and len(squares) == 12, "ARC_CARDINALITY")
    return succ, arcs, squares


def square_certificate(row, declared):
    require(physical(row)[2] == frozenset(declared), "SQUARE_ARCS")


def h_cycle(order):
    require(tuple(sorted(order)) == (0, 1, 2), "H_ORDER")
    return tuple(v for i in order for v in (CELLS[A][i], CELLS[C][i],
                                              CELLS[B][i], CELLS[D][i]))


def matching_check(f, g):
    require(set(f) == set(CELLS[A]) and set(f.values()) == set(CELLS[B]), "H_F")
    require(set(g) == set(CELLS[B]) and set(g.values()) == set(CELLS[A]), "H_G")
    v = CELLS[A][0]
    orbit = (v, g[f[v]], g[f[g[f[v]]]])
    require(len(set(orbit)) == 3 and g[f[orbit[2]]] == v,
            "H_COMPOSITION_NOT_3CYCLE")


def h_matchings(row):
    succ, _, squares = physical(row)
    require(all(cell(succ[v]) != cell(v) for v in row), "H_INTERNAL")
    f = {a: succ[succ[a]] for a in CELLS[A]}
    g = {b: succ[succ[b]] for b in CELLS[B]}
    matching_check(f, g)
    require(all(f[a] == CELLS[B][a - CELLS[A][0]] for a in CELLS[A]), "H_F_NORMALIZATION")
    require(set(f.items()) <= squares and set(g.items()) <= squares, "H_SQUARES")
    return f, g


def singleton_check(row):
    succ, _, _ = physical(row)
    pred = {v: u for u, v in succ.items()}
    singles = []
    for v in row:
        if cell(pred[v]) != cell(v) and cell(succ[v]) != cell(v):
            x, y = cell(pred[v]), cell(succ[v])
            require(x != cell(v) and y != cell(v) and OPP.get(x) == y,
                    "SINGLETON_TRANSPORT", [v, pred[v], succ[v]])
            singles.append(v)
    return singles


def segment(s, p, x, t, y, q):
    require(OPP[s] == t and p != x and y != q, "BAD_SEGMENT")
    require(p in CELLS[s] and x in CELLS[s] and y in CELLS[t] and q in CELLS[t],
            "BAD_SEGMENT")
    return (s, p, x, t, y, q)


def segments(s, t):
    return [segment(s, p, x, t, y, q)
            for p, x in itertools.permutations(CELLS[s], 2)
            for y, q in itertools.permutations(CELLS[t], 2)]


def seg_squares(seg):
    _, p, x, _, y, q = seg
    return frozenset(((p, y), (x, q)))


def seg_join(seg):
    return (seg[2], seg[4])


def seg_edge(seg, c):
    s, p, x, t, y, q = seg
    if c == s:
        return (p, x)
    require(c == t, "CELL_NOT_IN_SEGMENT")
    return (y, q)


def extra_edge(seg, c):
    s, p, x, t, y, q = seg
    if c == s:
        return (third(c, p, x), p)
    require(c == t, "CELL_NOT_IN_SEGMENT")
    return (q, third(c, y, q))


def candidate_full_sets(segs, c, full_count):
    base = [seg_edge(s, c) for s in segs]
    if len(set(base)) != len(base):
        return ()
    universe = {(u, v) for u in CELLS[c] for v in CELLS[c] if u != v}
    missing = universe - set(base)
    if len(missing) != full_count:
        return ()
    return tuple(frozenset(indices)
                 for indices in itertools.combinations(range(len(segs)), full_count)
                 if {extra_edge(segs[i], c) for i in indices} == missing)


def other_full_masks(n, a_full, b_full, target):
    for c_indices in itertools.combinations(range(n), target):
        cs = frozenset(c_indices)
        for d_indices in itertools.combinations(range(n), target):
            ds = frozenset(d_indices)
            good = True
            for i in range(n):
                aa, bb, cc, dd = i in a_full, i in b_full, i in cs, i in ds
                # 0, 2 on adjacent cells, or 4 full cells, on this SAME row.
                good &= ((not aa and not bb and not cc and not dd)
                         or (aa and bb and cc and dd)
                         or (aa != bb and cc != dd))
            if good:
                yield cs, ds


@lru_cache(maxsize=None)
def first_paths(c, n, full_indices):
    """First actual labeled path assignment with every internal arc once.

    Paths have length two or three; the unused vertex of a length-two path is
    the singleton. The return is one deterministic lift, NOT all labeled lifts.
    """
    full = frozenset(full_indices)
    choices = tuple(itertools.permutations(CELLS[c]))
    all_edges = frozenset((u, v) for u in CELLS[c] for v in CELLS[c] if u != v)

    def search(i, used, out):
        if i == n:
            return tuple(out) if used == all_edges else None
        for perm in choices:
            path = perm if i in full else perm[:2]
            edges = frozenset(zip(path, path[1:]))
            if used.isdisjoint(edges):
                found = search(i + 1, used | edges, out + [tuple(path)])
                if found is not None:
                    return found
        return None

    return search(0, frozenset(), [])


def build_row(seg, a_full, b_full, c_path, d_path, second_reverse=False,
              zero_mode="split"):
    """Construct one genuine Hamilton cycle from two joined physical blocks."""
    s, p, x, t, y, q = seg
    is_full = {A: a_full, B: b_full, C: len(c_path) == 3, D: len(d_path) == 3}
    source = ([third(s, p, x), p, x] if is_full[s] else [p, x])
    target = ([y, q, third(t, y, q)] if is_full[t] else [y, q])
    paths = {C: list(c_path), D: list(d_path)}
    c, d = (D, C) if second_reverse else (C, D)
    block1, block2 = source + target, paths[c] + paths[d]
    single = {}
    for z, path in ((s, source), (t, target), (c, paths[c]), (d, paths[d])):
        if not is_full[z]:
            single[z] = next(v for v in CELLS[z] if v not in path)
    if len(single) == 0:
        gap1, gap2 = [], []
    elif len(single) == 2:
        if set(single) == {d, s}:
            gap1, gap2 = [single[d], single[s]], []
        elif set(single) == {t, c}:
            gap1, gap2 = [], [single[t], single[c]]
        else:
            raise Reject("NONADJACENT_FULL_MASK")
    elif len(single) == 4:
        if zero_mode == "split":
            gap1, gap2 = [single[d], single[s]], [single[t], single[c]]
        elif zero_mode == "group1":
            gap1, gap2 = [single[c], single[s], single[d], single[t]], []
        elif zero_mode == "group2":
            gap1, gap2 = [], [single[s], single[c], single[t], single[d]]
        else:
            raise Reject("GAP_MODE")
    else:
        raise Reject("FULL_COUNT")
    row = tuple(block1 + gap1 + block2 + gap2)
    physical(row)
    return row


def lift_with_compatible_other_join(seg, a_full, b_full, c_path, d_path):
    # A two-full mask determines which C/D orientation permits its physical
    # singleton gap. Trying only C->D would silently drop the opposite masks.
    try:
        return build_row(seg, a_full, b_full, c_path, d_path)
    except Reject as exc:
        if exc.code != "NONADJACENT_FULL_MASK":
            raise
        return build_row(seg, a_full, b_full, c_path, d_path, second_reverse=True)


def joins(row, pair):
    _, arcs, _ = physical(row)
    return sorted((u, v) for u, v in arcs if {cell(u), cell(v)} == set(pair))


def join_uniqueness(rows, pair):
    entries = []
    for row in rows:
        js = joins(row, pair)
        require(len(js) == 1, "JOIN_COUNT")
        entries.append(js[0])
    require(len(set(entries)) == len(entries), "DUPLICATED_JOIN")


def row_info(row):
    succ, arcs, squares = physical(row)
    pred = {v: u for u, v in succ.items()}
    singles = singleton_check(row)
    ab, cd = joins(row, (A, B)), joins(row, (C, D))
    require(len(ab) == len(cd) == 1, "JOIN_COUNT")
    x, y = ab[0]
    u, v = cd[0]
    require(cell(pred[x]) == cell(x) and cell(succ[y]) == cell(y)
            and cell(pred[u]) == cell(u) and cell(succ[v]) == cell(v), "JOIN_ENDPOINT")
    internal = {c: sorted((p, q) for p, q in arcs if cell(p) == cell(q) == c)
                for c in range(4)}
    require(all(len(internal[c]) in (1, 2) for c in range(4)), "REGULAR_CELL_RUN")
    full = frozenset(c for c in range(4) if len(internal[c]) == 2)
    require(len(full) in (0, 2, 4), "FULL_COUNT")
    require(len(full) != 2 or next(iter(full)) != OPP[next(iter(full))]
            and not any(OPP[c] in full for c in full), "NONADJACENT_FULL_MASK")

    # Read the actual two gaps, not a separately chosen sign/mask schedule.
    def start_of_run(z):
        while cell(pred[z]) == cell(z):
            z = pred[z]
        return z

    def end_of_run(z):
        while cell(succ[z]) == cell(z):
            z = succ[z]
        return z

    def between(last, first):
        result = []
        z = succ[last]
        while z != first:
            require(len(result) < 12, "GAP_NOT_CONNECTED")
            result.append(z)
            z = succ[z]
        return result

    a, b, c, d = cell(x), cell(y), cell(u), cell(v)
    gap1 = between(end_of_run(y), start_of_run(u))
    gap2 = between(end_of_run(v), start_of_run(x))
    g1, g2 = [cell(z) for z in gap1], [cell(z) for z in gap2]
    if len(full) == 4:
        grammar = not g1 and not g2
    elif len(full) == 2:
        grammar = (g1 == [d, a] and not g2) or (not g1 and g2 == [b, c])
    else:
        grammar = ((g1 == [d, a] and g2 == [b, c])
                   or (g1 == [c, a, d, b] and not g2)
                   or (not g1 and g2 == [a, c, b, d]))
    require(grammar, "GAP_GRAMMAR", [g1, g2])
    return {"row": list(row), "adjacency_arcs": sorted(arcs),
            "square_arcs": sorted(squares), "ab_join": list(ab[0]),
            "cd_join": list(cd[0]), "full_cells": sorted(full),
            "internal_arcs": internal, "singletons": singles,
            "gaps": [gap1, gap2]}


def validate_regular(rows, target_full):
    infos = [row_info(row) for row in rows]
    all_edges = [tuple(e) for info in infos for edges in info["internal_arcs"].values()
                 for e in edges]
    require(len(all_edges) == len(set(all_edges)) and set(all_edges) == ALL_INTERNAL,
            "INTERNAL_ARC_COVER")
    require(all(sum(c in info["full_cells"] for info in infos) == target_full
                for c in range(4)), "FULL_RUN_TOTAL")
    return infos


def collision_inventory(rows, square=False):
    occurrences = {}
    for i, row in enumerate(rows):
        arcs = physical(row)[2 if square else 1]
        for arc in arcs:
            occurrences.setdefault(arc, []).append(i)
    return [[list(arc), indices] for arc, indices in sorted(occurrences.items())
            if len(indices) > 1]


def certificate(kind, h, rows):
    infos = validate_regular(rows, 2 if len(rows) == 4 else 1)
    f, g = h_matchings(h) if h is not None else ({}, {})
    all_rows = ([h] if h is not None else []) + list(rows)
    return {"kind": kind, "h": (list(h) if h is not None else None),
            "h_adjacency": (sorted(physical(h)[1]) if h is not None else None),
            "h_square": (sorted(physical(h)[2]) if h is not None else None),
            "F": sorted(f.items()), "G": sorted(g.items()), "rows": infos,
            "all_adjacency_collisions": collision_inventory(all_rows),
            "all_square_collisions": collision_inventory(all_rows, square=True),
            "warning": "Partial local cycles only; collision inventory is not a full-array certificate."}


def fixture_three_one():
    a, b, c, d = CELLS
    return (
        (a[1], a[0], b[0], b[1], d[1], a[2], c[2], c[0], d[2], d[0], b[2], c[1]),
        (a[2], a[0], b[1], b[2], b[0], d[0], a[1], c[0], c[1], c[2], d[2], d[1]),
        (a[0], a[2], a[1], b[0], b[2], c[2], c[1], d[0], d[1], d[2], b[1], c[0]),
        (b[2], b[1], b[0], a[0], a[1], a[2], c[1], c[0], c[2], d[1], d[0], d[2]),
    )


def fixture_two_two():
    a, b, c, d = CELLS
    return (
        (a[0], a[2], b[0], b[1], b[2], d[1], a[1], c[0], c[1], c[2], d[0], d[2]),
        (b[0], b[2], a[0], a[1], a[2], c[1], b[1], d[0], d[1], d[2], c[0], c[2]),
        (a[2], a[1], a[0], b[2], b[0], d[2], d[0], c[2], c[1], c[0], b[1], d[1]),
        (b[2], b[1], b[0], a[2], a[0], c[2], c[0], d[2], d[1], d[0], a[1], c[1]),
    )


def signs_and_masks(rows):
    infos = validate_regular(rows, 2)
    pairs = []
    for info in infos:
        s = "+" if cell(info["ab_join"][0]) == A else "-"
        t = "+" if cell(info["cd_join"][0]) == C else "-"
        mask = frozenset(info["full_cells"])
        require(len(mask) == 2, "TWO_FULL_FIXTURE")
        permitted = ({frozenset((C, B)), frozenset((A, D))} if s == t else
                     {frozenset((A, C)), frozenset((B, D))})
        require(mask in permitted, "SAME_ROW_SIGN_MASK")
        pairs.append((s, t))
    require(sum(s == "+" for s, _ in pairs) == 2
            and sum(t == "+" for _, t in pairs) == 2, "NOT_TWO_TWO")
    counts = [pairs.count(p) for p in (("+", "+"), ("-", "-"), ("+", "-"), ("-", "+"))]
    require(counts[0] == counts[1] and counts[2] == counts[3]
            and counts[0] + counts[2] == 2, "SIGN_PAIR_COUNTS")
    masks = [frozenset(info["full_cells"]) for info in infos]
    mask_counts = [masks.count(m) for m in (
        frozenset((C, B)), frozenset((A, D)),
        frozenset((A, C)), frozenset((B, D)))]
    require(mask_counts == [counts[0], counts[0], counts[2], counts[2]],
            "SAME_ROW_MASK_MULTIPLICITIES")
    return {"sign_pairs": pairs, "sign_pair_counts_pp_mm_pm_mp": counts,
            "masks_on_same_rows": [info["full_cells"] for info in infos],
            "mask_counts_CB_AD_AC_BD": mask_counts}


def expect_reject(name, code, action):
    try:
        action()
    except Reject as exc:
        require(exc.code == code, "CONTROL_WRONG_REASON", [name, code, exc.code])
        return {"control": name, "reason": exc.code}
    raise Reject("CONTROL_ACCEPTED", name)


def controls():
    rows = fixture_three_one()
    row = rows[0]
    sq = set(physical(row)[2])
    sq.remove(next(iter(sq)))
    disjoint = {i: (i + 1) % 6 for i in range(6)}
    disjoint.update({i: 6 + ((i - 6 + 1) % 6) for i in range(6, 12)})
    bad_g = {CELLS[B][i]: CELLS[A][i] for i in range(3)}
    f, _ = h_matchings(h_cycle((0, 1, 2)))
    mutated = list(row)
    i, j = mutated.index(CELLS[A][2]), mutated.index(CELLS[B][2])
    mutated[i], mutated[j] = mutated[j], mutated[i]
    alias = list(row)
    alias[alias.index(CELLS[A][2])] = CELLS[A][0]
    return [
        expect_reject("omitted-square-arc", "SQUARE_ARCS", lambda: square_certificate(row, sq)),
        expect_reject("disconnected-two-six-covers", "DISCONNECTED_COVER", lambda: check_successor(disjoint)),
        expect_reject("wrong-h-three-cycle", "H_COMPOSITION_NOT_3CYCLE", lambda: matching_check(f, bad_g)),
        expect_reject("singleton-adjacency", "SINGLETON_TRANSPORT", lambda: singleton_check(tuple(mutated))),
        expect_reject("duplicated-join", "DUPLICATED_JOIN", lambda: join_uniqueness((row, row), (A, B))),
        expect_reject("independent-cell-label-alias", "VERTEX_MULTISET", lambda: physical(tuple(alias))),
        expect_reject("missing-M-equals-C-premise", "ASSUMPTION_NOT_DECLARED", lambda: premises(False, True, CELLS)),
        expect_reject("missing-tripled-support-premise", "ASSUMPTION_NOT_DECLARED", lambda: premises(True, False, CELLS)),
    ]


def emit(obj):
    print(json.dumps(obj, sort_keys=True, separators=(",", ":")), flush=True)


def t14_enumerate(h):
    f, g = h_matchings(h)
    forbidden = frozenset(f.items())
    reverse_forbidden = frozenset(g.items())
    universe = frozenset(itertools.product(CELLS[A], CELLS[B]))
    high = [s for s in segments(A, B) if seg_squares(s).isdisjoint(forbidden)]
    high_triples = []
    for ss in itertools.combinations(high, 3):
        guard()
        square_entries = set().union(*(seg_squares(s) for s in ss))
        if (len(square_entries) == 6 and square_entries == universe - forbidden
                and len({seg_join(s) for s in ss}) == 3
                and all(len({seg_edge(s, c) for s in ss}) == 3 for c in (A, B))):
            high_triples.append(ss)
    summary = {"high_triples": len(high_triples), "segment_full_signatures": 0,
               "lift_signatures_relaxed": 0, "lift_signatures_baseline": 0,
               "reverse_matching": sorted(g.items()),
               "count_units": "canonical unordered high segments + low segment + four cell full masks; one actual labeled C/D lift per signature, NOT all lifts"}
    positive = None
    baseline_example = None
    for high_ss in high_triples:
        for low in segments(B, A):
            guard()
            ss = tuple(high_ss) + (low,)
            afs = candidate_full_sets(ss, A, 2)
            bfs = candidate_full_sets(ss, B, 2)
            if not afs or not bfs:
                continue
            for af in afs:
                for bf in bfs:
                    summary["segment_full_signatures"] += 1
                    for cf, df in other_full_masks(4, af, bf, 2):
                        cp = first_paths(C, 4, tuple(sorted(cf)))
                        dp = first_paths(D, 4, tuple(sorted(df)))
                        if cp is None or dp is None:
                            continue
                        rows = tuple(lift_with_compatible_other_join(
                            s, i in af, i in bf, cp[i], dp[i]) for i, s in enumerate(ss))
                        validate_regular(rows, 2)
                        join_uniqueness(rows, (A, B))
                        for i in range(4):
                            # The claimed join squares must be actual squares of this very row.
                            require(seg_squares(ss[i]) <= physical(rows[i])[2], "SEGMENT_SQUARES")
                        summary["lift_signatures_relaxed"] += 1
                        if positive is None:
                            positive = rows
                        if seg_squares(low).isdisjoint(reverse_forbidden):
                            summary["lift_signatures_baseline"] += 1
                            if baseline_example is None:
                                baseline_example = rows
    return summary, positive, baseline_example


def t13_segment_enumerate():
    """Exhaust segment/missing-square/full-extension signatures, not physical bridges."""
    universe = frozenset(itertools.product(CELLS[A], CELLS[B]))
    out = {"high_four_sets": 0, "extended_segment_signatures": 0,
           "unique_high_bridge_index": 0, "other_bridge_index_multiplicity": 0,
           "bridge_nonfull_and_low_one_full": 0, "bridge_nonfull_low_other": 0,
           "scope": "segment interface only; no actual five-cycle bridge or full T13 array is certified"}
    first_other = None
    for high in itertools.combinations(segments(A, B), 4):
        guard()
        sq = set().union(*(seg_squares(s) for s in high))
        if (len(sq) != 8 or len({seg_join(s) for s in high}) != 4
                or any(len({seg_edge(s, c) for s in high}) != 4 for c in (A, B))):
            continue
        out["high_four_sets"] += 1
        za, zb = next(iter(universe - sq))
        bridge = [i for i, s in enumerate(high)
                  if za not in seg_edge(s, A) and zb not in seg_edge(s, B)]
        for low in segments(B, A):
            guard()
            ss = tuple(high) + (low,)
            afs = candidate_full_sets(ss, A, 1)
            bfs = candidate_full_sets(ss, B, 1)
            if not afs or not bfs:
                continue
            for af in afs:
                for bf in bfs:
                    out["extended_segment_signatures"] += 1
                    if len(bridge) != 1:
                        out["other_bridge_index_multiplicity"] += 1
                        if first_other is None:
                            first_other = {"segments": ss, "missing": [za, zb],
                                           "bridge_indices": bridge,
                                           "A_full": sorted(af), "B_full": sorted(bf)}
                        continue
                    out["unique_high_bridge_index"] += 1
                    k = bridge[0]
                    if k not in af and k not in bf:
                        if int(4 in af) + int(4 in bf) == 1:
                            out["bridge_nonfull_and_low_one_full"] += 1
                        else:
                            out["bridge_nonfull_low_other"] += 1
                            if first_other is None:
                                first_other = {"segments": ss, "missing": [za, zb],
                                               "bridge_index": k,
                                               "A_full": sorted(af), "B_full": sorted(bf)}
    out["representative_other_segment_signature"] = first_other
    out["actual_five_cycle_bridge"] = "NOTTESTED: no actual bridge fixture or exhaustive physical lift supplied"
    return out


def main():
    premises(True, True, CELLS)
    emit({"status": "START", "premises": "M=C and two distinct tripled supports are ASSUMED, NOT TESTED",
          "cells": CELLS, "interpretation": {"A": "I", "B": "L", "C": "J", "D": "K"},
          "limit_seconds": 50.0})
    emit({"controls": controls()})
    hs = (h_cycle((0, 1, 2)), h_cycle((0, 2, 1)))
    supplied = fixture_three_one()
    infos = validate_regular(supplied, 2)
    require(sum(cell(info["ab_join"][0]) == A for info in infos) == 3,
            "RELAXED_FIXTURE_NOT_THREE_ONE")
    join_uniqueness(supplied, (A, B))
    for h in hs:
        f, g = h_matchings(h)
        high = [info for info in infos if cell(info["ab_join"][0]) == A]
        low = next(info for info in infos if cell(info["ab_join"][0]) == B)
        high_squares = set()
        for info in high:
            x, y = info["ab_join"]
            row = tuple(info["row"])
            succ, _, _ = physical(row)
            pred = {v: u for u, v in succ.items()}
            high_squares.update(((pred[x], y), (x, succ[y])))
        x, y = low["ab_join"]
        succ, _, _ = physical(tuple(low["row"]))
        pred = {v: u for u, v in succ.items()}
        low_squares = {(pred[x], y), (x, succ[y])}
        require(high_squares == set(itertools.product(CELLS[A], CELLS[B])) - set(f.items()),
                "RELAXED_FIXTURE_HIGH_SQUARES")
        require(not low_squares.isdisjoint(set(g.items())), "RELAXED_FIXTURE_NO_G_COLLISION")
        emit(certificate("actual-local-three-one-relaxation-G-check-dropped", h, supplied))
        summary, positive, baseline = t14_enumerate(h)
        emit({"T14_interface_counts": summary,
              "interpretation": "Only the selected opposite-pair join-square constraints are counted; other intercycle adjacency and square collisions are not forbidden."})
        if positive is not None:
            emit(certificate("first-enumerated-relaxed-lift", h, positive))
        if baseline is not None:
            emit(certificate("UNEXPECTED-baseline-local-interface-lift", h, baseline))
    rows22 = fixture_two_two()
    emit({"actual_two_two_same_cycle_masks": signs_and_masks(rows22)})
    emit(certificate("two-two-physical-mask-fixture-not-an-array", hs[0], rows22))
    emit({"T13_interface_counts": t13_segment_enumerate(),
          "T13_physical_bridge_status": "NOTTESTED"})
    emit({"status": "COMPLETE_LOCAL_ONLY", "full_T2_11_array": "NOTTESTED",
          "M_not_equal_C": "NOTTESTED", "conclusion": "No original-target closure."})


if __name__ == "__main__":
    try:
        main()
    except Incomplete:
        emit({"status": "INCOMPLETE", "reason": "cooperative 50-second deadline; no zero or pass is inferred"})
        sys.exit(2)
    except Reject as exc:
        emit({"status": "REJECTED_OR_SOURCE_DEFECT", "reason": exc.code, "detail": exc.detail})
        sys.exit(1)
