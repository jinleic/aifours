#!/usr/bin/env python3
"""Reviewer-written independent finite controls for review wave f107
(candidate: global AME(4,6) support >= 45, N=44 residual exclusion).

Independent of the author's control scripts: nothing is imported or executed
from the evidence directory.  Usage:

    python3 -B proof-independent-controls-v1.py <new-output.json> [--no-pcompletion]

The output path must not already exist.  All results are exact finite
computations; they are controls on the written argument, not a proof of it.
"""
import itertools
import json
import os
import sys
import time
from collections import Counter, defaultdict

PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
CUTS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]


def popcount(x):
    return bin(x).count("1")


# ---------------------------------------------------------------- Part A
# n x n 0/1 support patterns with all row/column degrees >= 2 and no two rows
# and no two columns meeting in exactly one position (necessary for unitarity).
def enumerate_support_patterns(n, ones):
    masks = sorted([m for m in range(1 << n) if popcount(m) >= 2], reverse=True)
    out = []
    rows = []

    def rec(i, start, remaining):
        if i == n:
            if remaining != 0:
                return
            colmasks = [sum(1 << ri for ri, r in enumerate(rows) if (r >> c) & 1) for c in range(n)]
            if min(popcount(c) for c in colmasks) < 2:
                return
            for a in range(n):
                for b in range(a + 1, n):
                    if popcount(colmasks[a] & colmasks[b]) == 1:
                        return
            out.append(tuple(rows))
            return
        for idx in range(start, len(masks)):
            m = masks[idx]
            pc = popcount(m)
            if pc > remaining - 2 * (n - i - 1):
                continue
            if any(popcount(r & m) == 1 for r in rows):
                continue
            rows.append(m)
            rec(i + 1, idx, remaining - pc)
            rows.pop()

    rec(0, 0, ones)
    return out


def is_two_by_two_block_union(rows):
    cnt = Counter(rows)
    if any(v != 2 for v in cnt.values()):
        return False
    ms = list(cnt)
    if any(popcount(m) != 2 for m in ms):
        return False
    return all(not (ms[a] & ms[b]) for a in range(len(ms)) for b in range(a + 1, len(ms)))


def pattern_shape(rows):
    """Connected components of the bipartite support graph as (rows, cols, ones)."""
    n = len(rows)
    seen_r = set()
    comps = []
    for r0 in range(n):
        if r0 in seen_r:
            continue
        stack = [("r", r0)]
        rs, cs = set(), set()
        while stack:
            kind, v = stack.pop()
            if kind == "r":
                if v in rs:
                    continue
                rs.add(v)
                for c in range(n):
                    if (rows[v] >> c) & 1:
                        stack.append(("c", c))
            else:
                if v in cs:
                    continue
                cs.add(v)
                for r in range(n):
                    if (rows[r] >> v) & 1:
                        stack.append(("r", r))
        seen_r |= rs
        ones = sum(popcount(rows[r]) for r in rs)
        comps.append((len(rs), len(cs), ones))
    return tuple(sorted(comps))


# ---------------------------------------------------------------- Part B
# All 16-point residual supports E in [maxsym]^4 whose six pair projections
# have exactly 8 values, each of multiplicity exactly 2.  Cells are generated in
# lexicographic order with the restricted-growth (first-occurrence) labelling
# in every coordinate; every support has at least one representative.
def enumerate_residual_supports(maxsym):
    mult = [dict() for _ in PAIRS]
    cells = []
    maxlab = [-1, -1, -1, -1]
    sols = []
    nodes = [0]

    def pairs_ok(c):
        for pi, (i, j) in enumerate(PAIRS):
            key = (c[i], c[j])
            m = mult[pi].get(key, 0)
            if m >= 2:
                return False
            if m == 0 and len(mult[pi]) >= 8:
                return False
        return True

    def push(c):
        for pi, (i, j) in enumerate(PAIRS):
            key = (c[i], c[j])
            mult[pi][key] = mult[pi].get(key, 0) + 1
        old = list(maxlab)
        for i in range(4):
            if c[i] > maxlab[i]:
                maxlab[i] = c[i]
        cells.append(c)
        return old

    def pop(c, old):
        cells.pop()
        for pi, (i, j) in enumerate(PAIRS):
            key = (c[i], c[j])
            mult[pi][key] -= 1
            if mult[pi][key] == 0:
                del mult[pi][key]
        maxlab[:] = old

    def lim(i):
        return min(maxlab[i] + 1, maxsym - 1)

    def rec_row():
        nodes[0] += 1
        if len(cells) == 16:
            for pi in range(6):
                if len(mult[pi]) != 8 or any(v != 2 for v in mult[pi].values()):
                    return
            sols.append(tuple(cells))
            return
        la, lb = (cells[-1][0], cells[-1][1]) if cells else (-1, -1)
        for a in range(max(la, 0), lim(0) + 1):
            if a > la and la >= 0:
                # every pending multiplicity-1 pair value with first coordinate la is dead
                dead = False
                for pi in (0, 1, 2):
                    for (u, v), m in mult[pi].items():
                        if m == 1 and u == la:
                            dead = True
                            break
                    if dead:
                        break
                if dead:
                    break
            bmin = lb + 1 if a == la else 0
            for b in range(bmin, lim(1) + 1):
                for c in range(0, lim(2) + 1):
                    for d in range(0, lim(3) + 1):
                        cell = (a, b, c, d)
                        if not pairs_ok(cell):
                            continue
                        old = push(cell)
                        for c2 in range(c, lim(2) + 1):
                            for d2 in range(d + 1 if c2 == c else 0, lim(3) + 1):
                                cell2 = (a, b, c2, d2)
                                if not pairs_ok(cell2):
                                    continue
                                old2 = push(cell2)
                                rec_row()
                                pop(cell2, old2)
                        pop(cell, old)

    rec_row()
    return sols, nodes[0]


def alphabet_sizes(E):
    return tuple(len(set(x[i] for x in E)) for i in range(4))


def cut_unique_overlap(E, cut):
    """Return a unique-overlap witness (rows or cols) in the given 2|2 cut, or None."""
    (i, j), (k, l) = cut
    rows = defaultdict(set)
    cols = defaultdict(set)
    for x in E:
        rows[(x[i], x[j])].add((x[k], x[l]))
        cols[(x[k], x[l])].add((x[i], x[j]))
    for name, S in (("rows", rows), ("cols", cols)):
        keys = sorted(S)
        for p in range(len(keys)):
            for q in range(p + 1, len(keys)):
                inter = S[keys[p]] & S[keys[q]]
                if len(inter) == 1:
                    return {"side": name, "a": keys[p], "b": keys[q], "common": sorted(inter)[0]}
    return None


def block_filter(E):
    """Witnesses (or None) for unique overlaps in the three cuts."""
    return [cut_unique_overlap(E, c) for c in CUTS]


def fiber_analysis(E, A):
    others = [i for i in range(4) if i != A]
    fib = defaultdict(list)
    for x in E:
        fib[x[A]].append(x)
    res = {"A": A, "fibers": {}, "balanced": True, "at_most_one_corr": True, "types_ok": True}
    for g in sorted(fib):
        pts = fib[g]
        d = {"size": len(pts), "values": {}, "pairs": {}}
        if len(pts) != 4:
            res["balanced"] = False
        for j in others:
            cnt = Counter(x[j] for x in pts)
            d["values"][j] = dict(cnt)
            if not (len(cnt) == 2 and all(v == 2 for v in cnt.values())):
                res["balanced"] = False
        ncorr = 0
        for j, k in itertools.combinations(others, 2):
            cnt = Counter((x[j], x[k]) for x in pts)
            if len(cnt) == 4 and all(v == 1 for v in cnt.values()):
                t = "full"
            elif len(cnt) == 2 and all(v == 2 for v in cnt.values()):
                t = "corr"
                ncorr += 1
            else:
                t = "other"
                res["types_ok"] = False
            d["pairs"][(j, k)] = t
        if ncorr > 1:
            res["at_most_one_corr"] = False
        res["fibers"][g] = d
    res["F"] = {}
    for j, k in itertools.combinations(others, 2):
        res["F"][(j, k)] = tuple(sorted(g for g in fib if res["fibers"][g]["pairs"][(j, k)] == "full"))
    res["rowsets"] = {}
    for j in others:
        res["rowsets"][j] = {g: frozenset(res["fibers"][g]["values"][j]) for g in fib}
    return res


def split_partition(rowsets):
    """If the incidence graph splits into two K_{2,2} (two row sets, each twice), return the fiber partition."""
    groups = defaultdict(list)
    for g, s in rowsets.items():
        groups[s].append(g)
    parts = [tuple(sorted(v)) for v in groups.values()]
    if len(parts) == 2 and all(len(p) == 2 for p in parts):
        return tuple(sorted(parts))
    return None


def p_completion_exists(E, nsym=6, node_cap=2_000_000):
    """Does a set P of 28 words exist with pair projections exactly complementary to E's
    (pairwise pair-distinct, avoiding every E pair value)?  Exact backtracking with MRV.
    Returns (exists, nodes, capped)."""
    Epairs = [set((x[i], x[j]) for x in E) for (i, j) in PAIRS]
    used = [set() for _ in PAIRS]
    rows01 = [(a, b) for a in range(nsym) for b in range(nsym) if (a, b) not in Epairs[0]]
    assert len(rows01) == 28
    nodes = [0]
    capped = [False]

    def options(a, b):
        res = []
        for c in range(nsym):
            if (a, c) in Epairs[1] or (a, c) in used[1]:
                continue
            if (b, c) in Epairs[3] or (b, c) in used[3]:
                continue
            for d in range(nsym):
                if (a, d) in Epairs[2] or (a, d) in used[2]:
                    continue
                if (b, d) in Epairs[4] or (b, d) in used[4]:
                    continue
                if (c, d) in Epairs[5] or (c, d) in used[5]:
                    continue
                res.append((c, d))
        return res

    def rec(remaining):
        nodes[0] += 1
        if nodes[0] > node_cap:
            capped[0] = True
            return False
        if not remaining:
            return True
        best, bestopts = None, None
        for r in remaining:
            o = options(*r)
            if not o:
                return False
            if best is None or len(o) < len(bestopts):
                best, bestopts = r, o
        rem2 = [r for r in remaining if r != best]
        a, b = best
        for (c, d) in bestopts:
            keys = ((1, (a, c)), (2, (a, d)), (3, (b, c)), (4, (b, d)), (5, (c, d)))
            for pi, key in keys:
                used[pi].add(key)
            if rec(rem2):
                return True
            for pi, key in keys:
                used[pi].discard(key)
        return False

    ok = rec(rows01)
    return ok, nodes[0], capped[0]


def p_counting_three_ternary(E):
    """Section 8 counting data from E alone: for each size-3 coordinate, fiber sizes and the number
    of P words forced per residual symbol (6 minus the E pair degree, for each other coordinate)."""
    sizes = alphabet_sizes(E)
    out = {}
    for i in range(4):
        if sizes[i] != 3:
            continue
        cnt = Counter(x[i] for x in E)
        out[i] = {"fiber_sizes": sorted(cnt.values()), "P_words_per_symbol": {}}
        for s in sorted(cnt):
            degs = []
            for j in range(4):
                if j == i:
                    continue
                degs.append(len(set(x[j] for x in E if x[i] == s)))
            out[i]["P_words_per_symbol"][s] = [6 - d for d in degs]
    return out


# ---------------------------------------------------------------- Part C
# F2 rectangle-parity lemmas over all permitted incidence graphs.
def all_4x4_two_regular():
    out = []
    rows2 = [frozenset(c) for c in itertools.combinations(range(4), 2)]
    for choice in itertools.product(rows2, repeat=4):
        deg = Counter()
        for s in choice:
            for v in s:
                deg[v] += 1
        if all(deg[v] == 2 for v in range(4)):
            out.append(choice)
    return out


def all_4x3_two_three_three():
    out = []
    rows2 = [frozenset(c) for c in itertools.combinations(range(3), 2)]
    for choice in itertools.product(rows2, repeat=4):
        deg = Counter()
        for s in choice:
            for v in s:
                deg[v] += 1
        if sorted(deg[v] for v in range(3)) == [2, 3, 3]:
            out.append(choice)
    return out


def parity_zero(U, V, F):
    acc = Counter()
    for g in F:
        for a in U[g]:
            for b in V[g]:
                acc[(a, b)] ^= 1
    return all(v == 0 for v in acc.values())


def duplicate_pairs(rows):
    groups = defaultdict(list)
    for g, s in enumerate(rows):
        groups[s].append(g)
    return [tuple(v) for v in groups.values() if len(v) == 2]


def check_parity_lemmas():
    G4 = all_4x4_two_regular()
    G3 = all_4x3_two_three_three()
    rep = {"n_4x4_two_regular": len(G4), "n_4x3_degree_233": len(G3)}
    masks = [F for fs in range(1, 5) for F in itertools.combinations(range(4), fs)]
    # R44
    bad44 = 0
    sizes44 = Counter()
    for U in G4:
        pu = split_partition(dict(enumerate(U)))
        for V in G4:
            pv = split_partition(dict(enumerate(V)))
            for F in masks:
                if not parity_zero(U, V, F):
                    continue
                sizes44[len(F)] += 1
                ok = pu is not None and pv is not None and pu == pv
                if len(F) == 2:
                    ok = ok and (tuple(F) in pu)
                if not ok:
                    bad44 += 1
    rep["R44_zero_parity_masks_by_size"] = dict(sorted(sizes44.items()))
    rep["R44_violations"] = bad44
    # R34: U is 4x3 (2,3,3), V is 4x4 2-regular
    bad34 = 0
    sizes34 = Counter()
    for U in G3:
        dup = duplicate_pairs(U)
        for V in G4:
            pv = split_partition(dict(enumerate(V)))
            for F in masks:
                if not parity_zero(U, V, F):
                    continue
                sizes34[len(F)] += 1
                ok = len(F) == 2 and len(dup) == 1 and tuple(F) == dup[0] and pv is not None and tuple(F) in pv
                if not ok:
                    bad34 += 1
    rep["R34_zero_parity_masks_by_size"] = dict(sorted(sizes34.items()))
    rep["R34_violations"] = bad34
    # 3/3: both degree (2,3,3); zero-parity masks by whether the duplicate pairs coincide
    sizes33 = Counter()
    bad33 = 0
    for U in G3:
        du = duplicate_pairs(U)[0]
        for V in G3:
            dv = duplicate_pairs(V)[0]
            same = du == dv
            for F in masks:
                if not parity_zero(U, V, F):
                    continue
                sizes33[("same_dup" if same else "diff_dup", len(F))] += 1
                if same and not (len(F) == 2 and tuple(F) == du):
                    bad33 += 1
                if (not same) and len(F) != 4:
                    bad33 += 1
    rep["R33_zero_parity_masks"] = {f"{k[0]}_F{k[1]}": v for k, v in sorted(sizes33.items())}
    rep["R33_violations"] = bad33
    return rep


# ---------------------------------------------------------------- Part D
# Shadow bound sharpness from the five-qubit code (independent construction).
def shadow_control():
    try:
        import numpy as np
    except Exception as e:  # pragma: no cover
        return {"skipped": str(e)}
    I = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    P = {"I": I, "X": X, "Y": Y, "Z": Z}

    def kron(*ops):
        out = np.array([[1.0 + 0j]])
        for o in ops:
            out = np.kron(out, o)
        return out

    def pstr(s):
        return kron(*[P[ch] for ch in s])

    gens = ["XZZXI", "IXZZX", "XIXZZ", "ZXIXZ"]
    proj = np.eye(32, dtype=complex)
    for g in gens:
        proj = proj @ (np.eye(32) + pstr(g)) / 2
    proj0 = proj @ (np.eye(32) + pstr("ZZZZZ")) / 2
    v = proj0 @ np.ones(32, dtype=complex)
    v = v / np.linalg.norm(v)
    psi = v.reshape([2] * 5)
    rho3 = np.tensordot(psi, psi.conj(), axes=([3, 4], [3, 4])).reshape(8, 8)
    ev = np.linalg.eigvalsh(rho3)

    def marg(rho, keep):
        t = rho.reshape([2] * 6)
        trace_out = [i for i in range(3) if i not in keep][0]
        t = np.trace(t, axis1=trace_out, axis2=trace_out + 3)
        return t.reshape(4, 4)

    margs_ok = all(np.allclose(marg(rho3, k), np.eye(4) / 4, atol=1e-10) for k in ([0, 1], [0, 2], [1, 2]))
    YYY = pstr("YYY")
    tilde = YYY @ rho3.conj() @ YYY
    identity_ok = np.allclose(tilde, np.eye(8) / 4 - rho3, atol=1e-10)
    rank = int(np.sum(ev > 1e-9))
    return {
        "five_qubit_code_three_qubit_marginal_eigenvalues": [round(float(x), 10) for x in ev],
        "rank": rank,
        "two_qubit_marginals_maximally_mixed": bool(margs_ok),
        "spin_flip_identity_rho_tilde_eq_I4_minus_rho": bool(identity_ok),
        "max_eigenvalue_le_quarter": bool(ev.max() <= 0.25 + 1e-9),
    }


# ---------------------------------------------------------------- main
def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        sys.exit(2)
    out_path = args[0]
    if os.path.exists(out_path):
        print("refusing to overwrite", out_path)
        sys.exit(3)
    do_pc = "--no-pcompletion" not in flags
    t0 = time.time()
    report = {"script": os.path.basename(__file__), "python": sys.version.split()[0]}

    # Part A
    A = {}
    for n, ones in [(6, 13), (6, 14), (7, 15), (7, 16), (5, 12), (3, 8), (8, 16)]:
        pats = enumerate_support_patterns(n, ones)
        entry = {"count": len(pats)}
        if pats:
            shapes = sorted(Counter(pattern_shape(p) for p in pats).items())
            entry["component_shapes_(rows,cols,ones)"] = [[list(map(list, k)), v] for k, v in shapes]
        if (n, ones) == (8, 16):
            entry["all_two_by_two_block_unions"] = all(is_two_by_two_block_union(p) for p in pats)
        A[f"n{n}_ones{ones}"] = entry
    report["A_unitary_support_patterns"] = A
    print("Part A done", round(time.time() - t0, 1), flush=True)

    # Part C
    report["C_parity_lemmas"] = check_parity_lemmas()
    print("Part C done", round(time.time() - t0, 1), flush=True)

    # Part D
    report["D_shadow_control"] = shadow_control()
    print("Part D done", round(time.time() - t0, 1), flush=True)

    # Part B
    t1 = time.time()
    sols, nodes = enumerate_residual_supports(6)
    tB = time.time() - t1
    print("Part B enumeration done", len(sols), "supports", round(tB, 1), "s", flush=True)
    B = {"maxsym": 6, "search_nodes": nodes, "supports_with_restricted_growth_labels": len(sols), "seconds": round(tB, 1)}
    by_sizes = Counter(tuple(sorted(alphabet_sizes(E))) for E in sols)
    B["by_sorted_alphabet_sizes"] = {str(k): v for k, v in sorted(by_sizes.items())}
    B["max_alphabet_size"] = max(max(alphabet_sizes(E)) for E in sols) if sols else None

    survivors = []
    fail_cut = Counter()
    for E in sols:
        w = block_filter(E)
        if all(x is None for x in w):
            survivors.append(E)
        else:
            fail_cut[tuple(sorted(alphabet_sizes(E)))] += 1
    B["survivors_of_no_unique_overlap_filter"] = len(survivors)
    B["survivors_by_sorted_alphabet_sizes"] = {str(k): v for k, v in sorted(Counter(tuple(sorted(alphabet_sizes(E))) for E in survivors).items())}
    B["filtered_out_by_sorted_alphabet_sizes"] = {str(k): v for k, v in sorted(fail_cut.items())}

    # (3,3,4,4): Section 7 predicts a unique row overlap in the cut with rows (size-4,size-4), cols (size-3,size-3)
    mixed = [E for E in sols if tuple(sorted(alphabet_sizes(E))) == (3, 3, 4, 4)]
    mixed_ADBC = 0
    mixed_ADBC_rows = 0
    example_mixed = None
    for E in mixed:
        sizes = alphabet_sizes(E)
        four = tuple(i for i in range(4) if sizes[i] == 4)
        three = tuple(i for i in range(4) if sizes[i] == 3)
        w = cut_unique_overlap(E, (four, three))
        if w is not None:
            mixed_ADBC += 1
            if w["side"] == "rows":
                mixed_ADBC_rows += 1
            if example_mixed is None:
                example_mixed = {"E": [list(x) for x in E], "sizes": list(sizes), "witness": w}
    B["mixed_3344"] = {"count": len(mixed), "with_unique_overlap_in_44rows_33cols_cut": mixed_ADBC,
                       "first_witness_on_rows": mixed_ADBC_rows, "example": example_mixed}

    # structural claims on survivors with a size-4 coordinate
    S = {"checked": 0, "balanced_fail": 0, "types_fail": 0, "corr_fail": 0, "R44_fail": 0, "R34_fail": 0,
         "pairs_with_empty_F": Counter(), "pairs_with_nonempty_F": Counter(), "size3_degree_patterns": Counter(),
         "shadow_group_B_values": Counter(), "route": Counter()}
    for E in survivors:
        sizes = alphabet_sizes(E)
        if 4 not in sizes:
            continue
        A_ = sizes.index(4)
        fa = fiber_analysis(E, A_)
        S["checked"] += 1
        if not fa["balanced"]:
            S["balanced_fail"] += 1
        if not fa["types_ok"]:
            S["types_fail"] += 1
        if not fa["at_most_one_corr"]:
            S["corr_fail"] += 1
        others = [i for i in range(4) if i != A_]
        key = tuple(sorted(sizes))
        for j, k in itertools.combinations(others, 2):
            F = fa["F"][(j, k)]
            tag = (key, (sizes[j], sizes[k]))
            if not F:
                S["pairs_with_empty_F"][str(tag)] += 1
            else:
                S["pairs_with_nonempty_F"][str(tag)] += 1
                if sizes[j] == 4 and sizes[k] == 4:
                    pj, pk = split_partition(fa["rowsets"][j]), split_partition(fa["rowsets"][k])
                    if pj is None or pk is None or pj != pk:
                        S["R44_fail"] += 1
                if {sizes[j], sizes[k]} == {3, 4}:
                    j3, k4 = (j, k) if sizes[j] == 3 else (k, j)
                    gs = sorted(fa["rowsets"][j3])
                    dup = duplicate_pairs([fa["rowsets"][j3][g] for g in gs])
                    dup = [tuple(gs[i] for i in d) for d in dup]
                    pk = split_partition(fa["rowsets"][k4])
                    if not (len(dup) == 1 and tuple(sorted(F)) == tuple(sorted(dup[0])) and pk is not None and tuple(sorted(F)) in pk):
                        S["R34_fail"] += 1
        for j in others:
            if sizes[j] == 3:
                deg = tuple(sorted(Counter(v for g in fa["rowsets"][j] for v in fa["rowsets"][j][g]).values()))
                S["size3_degree_patterns"][str((key, deg))] += 1
        allF = all(fa["F"][(j, k)] for j, k in itertools.combinations(others, 2))
        if not allF:
            S["route"][str((key, "some pair all-correlated -> Section 3 OLS route"))] += 1
        else:
            S["route"][str((key, "all pairs have full fibers -> Section 5/6 shadow route"))] += 1
            four_others = [j for j in others if sizes[j] == 4]
            if len(four_others) >= 2:
                C_, D_ = four_others[:2]
                part = split_partition(fa["rowsets"][C_])
                if part is not None and part == split_partition(fa["rowsets"][D_]):
                    Bc = [j for j in others if j not in (C_, D_)][0]
                    for grp in part:
                        nb = len(set(x[Bc] for x in E if x[A_] in grp))
                        S["shadow_group_B_values"][str((key, nb))] += 1
    for k in list(S):
        if isinstance(S[k], Counter):
            S[k] = dict(sorted(S[k].items()))
    B["structure_on_survivors"] = S

    # Section 8 counting data on all (3,3,3,x) supports (before the unitarity filter)
    tern = [E for E in sols if sorted(alphabet_sizes(E)).count(3) >= 3]
    pat = Counter()
    for E in tern:
        d = p_counting_three_ternary(E)
        for i, v in d.items():
            pat[str((tuple(sorted(alphabet_sizes(E))), tuple(v["fiber_sizes"]),
                     tuple(sorted(tuple(sorted(set(w))) for w in v["P_words_per_symbol"].values()))))] += 1
    B["three_or_four_ternary_counting_patterns"] = dict(sorted(pat.items()))

    if do_pc:
        # P-completion search: pure combinatorics, no unitarity
        def pc_batch(Es, label):
            agg = defaultdict(lambda: {"n": 0, "exists": 0, "capped": 0, "max_nodes": 0})
            for E in Es:
                key = str(tuple(sorted(alphabet_sizes(E))))
                ok, nodes_, capped = p_completion_exists(E)
                agg[key]["n"] += 1
                agg[key]["exists"] += int(ok)
                agg[key]["capped"] += int(capped)
                agg[key]["max_nodes"] = max(agg[key]["max_nodes"], nodes_)
            print("P-completion", label, dict(agg), round(time.time() - t0, 1), flush=True)
            return dict(agg)

        B["P_completion_three_or_four_ternary_all"] = pc_batch(tern, "ternary")

    report["B_residual_supports"] = B
    report["seconds_total"] = round(time.time() - t0, 1)
    with open(out_path, "x") as f:
        json.dump(report, f, indent=1, default=str)
    print(json.dumps(report, indent=1, default=str))

    if "--survivor-pcompletion" in flags:
        # Bounded, optional: support-only P-completion on the unitarity-filter survivors.  The candidate
        # does not claim support-only exclusion there (Sections 3, 5, 6 use unitarity), so a capped or
        # positive outcome is informative, not a defect.
        cap = 20000
        out2 = out_path[:-5] + "-survivors.json" if out_path.endswith(".json") else out_path + "-survivors.json"
        if os.path.exists(out2):
            print("refusing to overwrite", out2)
            sys.exit(3)
        agg = defaultdict(lambda: {"n": 0, "exists": 0, "capped": 0, "max_nodes": 0})
        witnesses = {}
        for E in survivors:
            key = str(tuple(sorted(alphabet_sizes(E))))
            ok, nodes_, capped = p_completion_exists(E, node_cap=cap)
            agg[key]["n"] += 1
            agg[key]["exists"] += int(ok)
            agg[key]["capped"] += int(capped)
            agg[key]["max_nodes"] = max(agg[key]["max_nodes"], nodes_)
            if ok and key not in witnesses:
                witnesses[key] = [list(x) for x in E]
        rep2 = {"node_cap_per_support": cap, "by_sorted_sizes": dict(agg), "first_support_with_P_completion_by_sizes": witnesses,
                "seconds": round(time.time() - t0, 1)}
        with open(out2, "x") as f:
            json.dump(rep2, f, indent=1, default=str)
        print(json.dumps(rep2, indent=1, default=str))


if __name__ == "__main__":
    main()
