#!/usr/bin/env python3
"""rv171-controls.py

Independent exact finite controls for review wave f171-moqls8-axis-surplus-six
(candidate frontier-20261028-axis-surplus6-self-contained-v1.md, SHA-256
4534db97ff45e79ea1d909ad77e6b42d7753d5f9dc93e7ea86ba9765a0bb1a1c).

Authored by the same-harness reviewer ReviewF171AxisSurplus.  Imports and executes
no author code.  All arithmetic is exact: int, fractions.Fraction, Gaussian integers
as (re, im) int pairs.  Writes rv171-controls-results.json next to this file.
Run with: python3 -B rv171-controls.py   (no bytecode cache is written).

Controls
  P  surplus partitions of the off-row 7x7 a-channel (sigma <= 7) and graph types
  G  every connected min-degree-2 3x3 and 4x4 support graph: adjacency counts
  T  Turan numbers, K4/K5 brute force, all 30-edge K5-free graphs on 9 vertices
  M  the channel-rank / frame-moment inequality tables (3x3 and 4x4)
  R  every N=9 "pentad" (rows, columns, three mate partitions) and its incidence rank
  X  two-plane cross-Gram zero patterns (exact Gaussian-rational examples, identities)
  F  an actual exact three-MOQLS(8) whose nonclassical member has a C8 a-component
  K  intercalate-modified Z2^3 members: exhaustive classical-mate searches
"""
import itertools
import json
import math
import os
import sys
import time
from fractions import Fraction as Fr
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "rv171-controls-results.json")
RES = {"script": "rv171-controls.py", "python": sys.version.split()[0], "controls": {}}
FAILS = []
T0 = time.perf_counter()


def put(ctrl, key, val):
    RES["controls"].setdefault(ctrl, {})[key] = val


def chk(ctrl, label, cond, kind="positive"):
    RES["controls"].setdefault(ctrl, {}).setdefault("checks", []).append(
        {"label": label, "kind": kind, "ok": bool(cond)})
    if not cond:
        FAILS.append(ctrl + ": " + label)


def stamp(ctrl):
    put(ctrl, "elapsed_s_cumulative", round(time.perf_counter() - T0, 2))
    print(ctrl, "done", round(time.perf_counter() - T0, 1), "s", flush=True)


# ------------------------------------------------------------------ utilities
def conn_mindeg2(k, cells):
    """True iff all 2k row/column vertices have degree >= 2 and the graph is connected."""
    rd = [0] * k
    cd = [0] * k
    for i, j in cells:
        rd[i] += 1
        cd[j] += 1
    if min(rd) < 2 or min(cd) < 2:
        return False
    par = list(range(2 * k))

    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for i, j in cells:
        a, b = f(i), f(k + j)
        if a != b:
            par[a] = b
    return len({f(v) for v in range(2 * k)}) == 1


def line_profile(cells, k):
    rd = [0] * k
    cd = [0] * k
    for i, j in cells:
        rd[i] += 1
        cd[j] += 1
    return tuple(sorted(rd, reverse=True)), tuple(sorted(cd, reverse=True))


def adjacency_count(cells):
    rows, cols = {}, {}
    for i, j in cells:
        rows[i] = rows.get(i, 0) + 1
        cols[j] = cols.get(j, 0) + 1
    return sum(comb(d, 2) for d in rows.values()) + sum(comb(d, 2) for d in cols.values())


def turan(n, r):
    sizes = [n // r + (1 if i < n % r else 0) for i in range(r)]
    return comb(n, 2) - sum(comb(s, 2) for s in sizes)


def balanced_line_pairs(N, lines):
    q, rem = divmod(N, lines)
    return rem * comb(q + 1, 2) + (lines - rem) * comb(q, 2)


def rank_exact(rows):
    """Rank over Q of a list of integer/Fraction rows (Gaussian elimination)."""
    M = [[Fr(x) for x in r] for r in rows]
    rank, ncol = 0, (len(M[0]) if M else 0)
    for col in range(ncol):
        piv = next((i for i in range(rank, len(M)) if M[i][col] != 0), None)
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        pv = M[rank][col]
        for i in range(len(M)):
            if i != rank and M[i][col] != 0:
                fac = M[i][col] / pv
                M[i] = [a - fac * b for a, b in zip(M[i], M[rank])]
        rank += 1
    return rank


def det_exact(A):
    M = [[Fr(x) for x in r] for r in A]
    n, d = len(M), Fr(1)
    for c in range(n):
        piv = next((i for i in range(c, n) if M[i][c] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            d = -d
        d *= M[c][c]
        for i in range(c + 1, n):
            if M[i][c] != 0:
                fac = M[i][c] / M[c][c]
                M[i] = [a - fac * b for a, b in zip(M[i], M[c])]
    return d


def solve_exact(A, b):
    """Solve A w = b over Q (A: m x n).  Returns (status, w) with status in
    {'inconsistent', 'unique', 'underdetermined'}."""
    m, n = len(A), len(A[0])
    M = [[Fr(x) for x in A[i]] + [Fr(b[i])] for i in range(m)]
    r, pivcols = 0, []
    for col in range(n):
        piv = next((i for i in range(r, m) if M[i][col] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][col]
        M[r] = [x / pv for x in M[r]]
        for i in range(m):
            if i != r and M[i][col] != 0:
                fac = M[i][col]
                M[i] = [a - fac * c for a, c in zip(M[i], M[r])]
        pivcols.append(col)
        r += 1
    for i in range(r, m):
        if M[i][n] != 0:
            return "inconsistent", None
    if r < n:
        return "underdetermined", None
    w = [Fr(0)] * n
    for i, col in enumerate(pivcols):
        w[col] = M[i][n]
    return "unique", w


# ------------------------------------------------------------------ control P
def control_P():
    C = "P_surplus_partitions"
    types = [(k, N) for k in range(2, 8) for N in range(2 * k, k * k + 1)]
    real = {}
    for k, N in types:                       # constructive: Hamiltonian cycle + chords
        cyc = list(dict.fromkeys([(i, i) for i in range(k)] + [(i, (i + 1) % k) for i in range(k)]))
        rest = [(i, j) for i in range(k) for j in range(k) if (i, j) not in set(cyc)]
        cells = cyc + rest[:N - len(cyc)]
        real[(k, N)] = len(set(cells)) == N and conn_mindeg2(k, cells)
    chk(C, "every (k,N), k>=2, 2k<=N<=k^2 is realised by a connected min-degree-2 kxk graph",
        all(real.values()))

    def multisets(sigma, tlist, maxrows=7):
        out = []

        def go(start, rows_left, s_left, cur):
            if s_left == 0:
                out.append(tuple(cur))
                return
            for t in range(start, len(tlist)):
                k, N = tlist[t]
                if k <= rows_left and 0 < N - k <= s_left:
                    cur.append(tlist[t])
                    go(t, rows_left - k, s_left - (N - k), cur)
                    cur.pop()
        go(0, maxrows, sigma, [])
        return out
    table = {s: multisets(s, types) for s in range(0, 8)}
    put(C, "configurations_by_sigma (multisets of (k,N) nontrivial components, sum k <= 7)",
        {str(s): [[list(t) for t in m] for m in v] for s, v in table.items()})
    chk(C, "sigma=0 only the all-singleton channel", table[0] == [()])
    chk(C, "sigma=1 has no configuration", table[1] == [])
    chk(C, "sigma=2 only a sole (2,4)", set(table[2]) == {((2, 4),)})
    chk(C, "sigma=3 only a sole (3,6)", set(table[3]) == {((3, 6),)})
    chk(C, "sigma=4 exactly sole (4,8), sole (3,7), (2,4)+(2,4) [candidate cases i, ii, iii]",
        set(table[4]) == {((4, 8),), ((3, 7),), ((2, 4), (2, 4))})
    chk(C, "sigma=5 exactly sole (3,8), sole (4,9), sole (5,10), (2,4)+(3,6)",
        set(table[5]) == {((3, 8),), ((4, 9),), ((5, 10),), ((2, 4), (3, 6))})
    put(C, "sigma=6 configuration count", len(table[6]))
    # negative: drop the minimum-degree-two lemma (allow tree components N = 2k-1)
    loose = [(k, N) for k in range(2, 8) for N in range(2 * k - 1, k * k + 1)]
    lt = {s: multisets(s, loose) for s in range(1, 3)}
    put(C, "negative: configurations if tree components were allowed",
        {str(s): [[list(t) for t in m] for m in v] for s, v in lt.items()})
    chk(C, "negative: without the degree-one lemma sigma=1 would be possible (sole (2,3) path)",
        ((2, 3),) in set(lt[1]), kind="negative")
    # graph-level identification of each sigma<=5 type with 2-regular edge count
    # (5,10): all 5x5 row-sum-2 / column-sum-2 graphs
    pairs5 = list(itertools.combinations(range(5), 2))
    tot = conn = 0
    for choice in itertools.product(pairs5, repeat=5):
        cs = [0] * 5
        for pr in choice:
            cs[pr[0]] += 1
            cs[pr[1]] += 1
        if cs != [2] * 5:
            continue
        tot += 1
        cells = [(i, j) for i, pr in enumerate(choice) for j in pr]
        if conn_mindeg2(5, cells):
            conn += 1
    put(C, "5x5 2-regular bipartite graphs: total / connected (= single 10-cycles)", [tot, conn])
    chk(C, "(5,10): N=2k forces 2-regular; connected ones are exactly the 5!*4!/2=1440 Hamiltonian 10-cycles",
        tot == 2040 and conn == 1440)
    stamp(C)


# ------------------------------------------------------------------ control G
G4_N9 = []


def control_G():
    C = "G_support_graphs"
    summary = {}
    for k in (3, 4):
        allc = [(i, j) for i in range(k) for j in range(k)]
        byN = {}
        for mask in range(1 << (k * k)):
            cells = [allc[t] for t in range(k * k) if (mask >> t) & 1]
            if len(cells) < 2 * k or not conn_mindeg2(k, cells):
                continue
            N = len(cells)
            rp, cp = line_profile(cells, k)
            A = adjacency_count(cells)
            e = byN.setdefault(N, {"count": 0, "A": set(), "rp": set(), "cp": set(), "two_reg": 0})
            e["count"] += 1
            e["A"].add(A)
            e["rp"].add(rp)
            e["cp"].add(cp)
            if rp == (2,) * k and cp == (2,) * k:
                e["two_reg"] += 1
            if k == 4 and N == 9:
                G4_N9.append(cells)
        summary[k] = byN
        put(C, f"{k}x{k}", {str(N): {"count": v["count"], "A_min": min(v["A"]), "A_max": max(v["A"]),
                                      "A_values": sorted(v["A"]), "two_regular": v["two_reg"]}
                             for N, v in sorted(byN.items())})
    s3, s4 = summary[3], summary[4]
    chk(C, "3x3: N ranges exactly 6..9", sorted(s3) == [6, 7, 8, 9])
    chk(C, "3x3: adjacency A is forced: N=6,7,8,9 -> 6,10,14,18 (candidate table)",
        [sorted(s3[N]["A"]) for N in (6, 7, 8, 9)] == [[6], [10], [14], [18]])
    chk(C, "3x3: N=6 graphs are the 6 six-cycles", s3[6]["count"] == 6 and s3[6]["two_reg"] == 6)
    chk(C, "4x4: N ranges exactly 8..16", sorted(s4) == list(range(8, 17)))
    chk(C, "4x4: N=8 graphs are exactly the 72 Hamiltonian 8-cycles (sole C8)",
        s4[8]["count"] == 72 and s4[8]["two_reg"] == 72)
    chk(C, "4x4: N=9 row and column profiles are both (3,2,2,2) and A=12",
        s4[9]["rp"] == {(3, 2, 2, 2)} and s4[9]["cp"] == {(3, 2, 2, 2)} and s4[9]["A"] == {12})
    claimedA = {10: 16, 11: 20, 12: 24, 13: 30, 14: 36, 15: 42, 16: 48}
    chk(C, "4x4: balanced-degree formula equals the true minimum A over all graphs, N=10..16, and the candidate table",
        all(min(s4[N]["A"]) == 2 * balanced_line_pairs(N, 4) == claimedA[N] for N in claimedA))
    put(C, "4x4 N=9 labelled graph count", len(G4_N9))
    stamp(C)
    return s3, s4


# ------------------------------------------------------------------ control T
def every_graph_with_m_edges_has_clique(n, s, m):
    """True iff every graph on n vertices with m edges contains K_s
    (checked through all complements with C(n,2)-m edges having an independent s-set)."""
    pairs = list(itertools.combinations(range(n), 2))
    pidx = {p: i for i, p in enumerate(pairs)}
    masks = []
    for S in itertools.combinations(range(n), s):
        mk = 0
        for a, b in itertools.combinations(S, 2):
            mk |= 1 << pidx[(a, b)]
        masks.append(mk)
    ecomp = comb(n, 2) - m
    if ecomp < 0:
        return True
    for cmb in itertools.combinations(range(len(pairs)), ecomp):
        mk = 0
        for e in cmb:
            mk |= 1 << e
        for S in masks:
            if not (mk & S):
                break
        else:
            return False
    return True


def control_T():
    C = "T_turan_and_K5_equality"
    chk(C, "t_3(N) = floor(N^2/3) for N=0..60 (Turan graph T(N,3))",
        all(turan(N, 3) == N * N // 3 for N in range(61)))
    chk(C, "t_4(N) = floor(3N^2/8) for N=0..60 (Turan graph T(N,4))",
        all(turan(N, 4) == 3 * N * N // 8 for N in range(61)))
    chk(C, "K4 induction identity 3+2(N-3)+floor((N-3)^2/3) = floor(N^2/3), N=3..60",
        all(3 + 2 * (N - 3) + (N - 3) ** 2 // 3 == N * N // 3 for N in range(3, 61)))
    chk(C, "K5 induction identity 6+3(N-4)+floor(3(N-4)^2/8) = floor(3N^2/8), N=4..60",
        all(6 + 3 * (N - 4) + 3 * (N - 4) ** 2 // 8 == 3 * N * N // 8 for N in range(4, 61)))
    chk(C, "Mantel/K4-free bounds nest: floor(N^2/4) <= floor(N^2/3) <= floor(3N^2/8), N=0..60",
        all(N * N // 4 <= N * N // 3 <= 3 * N * N // 8 for N in range(61)))
    chk(C, "K4 base cases N<=3 and K5 base cases N<=4: complete graph fits the bound",
        all(comb(N, 2) <= N * N // 3 for N in range(4)) and all(comb(N, 2) <= 3 * N * N // 8 for N in range(5)))
    bf = {}
    for N in range(4, 9):
        bf[f"K4,N={N}"] = every_graph_with_m_edges_has_clique(N, 4, N * N // 3 + 1)
    for N in range(5, 10):
        bf[f"K5,N={N}"] = every_graph_with_m_edges_has_clique(N, 5, 3 * N * N // 8 + 1)
    put(C, "brute force: every graph with bound+1 edges contains the clique", bf)
    chk(C, "brute force ex(N,K4)<=floor(N^2/3) for N=4..8 and ex(N,K5)<=floor(3N^2/8) for N=5..9", all(bf.values()))
    # Caro-Wei cross-check (alpha >= n^2/(n+2m) for the complement) for N beyond brute force
    cw = {}
    for s, lo, hi, bound in ((4, 6, 10, lambda N: N * N // 3), (5, 9, 17, lambda N: 3 * N * N // 8)):
        for N in range(lo, hi):
            mc = comb(N, 2) - (bound(N) + 1)
            cw[f"K{s},N={N}"] = str(Fr(N * N, N + 2 * mc))
            chk(C, f"Caro-Wei: every graph on {N} vertices with {bound(N) + 1} edges contains K{s}",
                Fr(N * N, N + 2 * mc) > s - 1)
    put(C, "Caro-Wei lower bound on complement independence number", cw)
    # all 30-edge K5-free graphs on 9 vertices (complement: 6 edges, independence <= 4)
    n = 9
    pairs = list(itertools.combinations(range(n), 2))
    pidx = {p: i for i, p in enumerate(pairs)}
    masks5 = []
    for S in itertools.combinations(range(n), 5):
        mk = 0
        for a, b in itertools.combinations(S, 2):
            mk |= 1 << pidx[(a, b)]
        masks5.append(mk)
    bits = [1 << i for i in range(36)]
    surv = []
    for cmb in itertools.combinations(range(36), 6):
        mk = bits[cmb[0]] | bits[cmb[1]] | bits[cmb[2]] | bits[cmb[3]] | bits[cmb[4]] | bits[cmb[5]]
        for S in masks5:
            if not (mk & S):
                break
        else:
            surv.append(cmb)
    good = 0
    for cmb in surv:
        es = [pairs[e] for e in cmb]
        deg = [0] * n
        for a, b in es:
            deg[a] += 1
            deg[b] += 1
        two = [v for v in range(n) if deg[v] == 2]
        one = [v for v in range(n) if deg[v] == 1]
        tri = len(two) == 3 and all(tuple(sorted(p)) in es for p in itertools.combinations(two, 2))
        mat = len(one) == 6 and all((a in one) == (b in one) for a, b in es)
        if tri and mat:
            good += 1
    put(C, "9 vertices, 30 edges, K5-free: labelled count / complement = K3+3K2", [len(surv), good])
    chk(C, "every 30-edge K5-free graph on 9 vertices is complete 4-partite (3,2,2,2); 1260 labelled copies",
        len(surv) == 1260 and good == 1260)
    # negatives
    chk(C, "negative: no K5-free graph on 9 vertices with 31 edges (equality case is extremal)",
        every_graph_with_m_edges_has_clique(9, 5, 31), kind="negative")
    # K_{3,2,2,2} minus one edge: 29 edges, K5-free, not complete multipartite
    parts = [0, 0, 0, 1, 1, 2, 2, 3, 3]
    E = {p for p in pairs if parts[p[0]] != parts[p[1]]}
    E.discard((0, 3))
    comp = 0
    for p in pairs:
        if p not in E:
            comp |= 1 << pidx[p]
    k5free = all(comp & S for S in masks5)
    # complete multipartite <=> non-adjacency is transitive
    nonadj = {p for p in pairs if p not in E}
    transitive = all(((min(a, c), max(a, c)) in nonadj) for (a, b) in nonadj for (b2, c) in nonadj
                     if b == b2 and a != c) and all(
        ((min(x, z), max(x, z)) in nonadj) for x in range(n) for y in range(n) for z in range(n)
        if len({x, y, z}) == 3 and (min(x, y), max(x, y)) in nonadj and (min(y, z), max(y, z)) in nonadj)
    chk(C, "negative: K_{3,2,2,2} minus an edge (29 edges) is K5-free yet not complete multipartite",
        len(E) == 29 and k5free and not transitive, kind="negative")
    # 6-vertex K4-free 12-edge graphs are K6 minus a perfect matching (inner-appendix remark)
    pairs6 = list(itertools.combinations(range(6), 2))
    pid6 = {p: i for i, p in enumerate(pairs6)}
    m4 = []
    for S in itertools.combinations(range(6), 4):
        mk = 0
        for a, b in itertools.combinations(S, 2):
            mk |= 1 << pid6[(a, b)]
        m4.append(mk)
    s6 = []
    for cmb in itertools.combinations(range(15), 3):
        mk = sum(1 << e for e in cmb)
        if all(mk & S for S in m4):
            s6.append([pairs6[e] for e in cmb])
    pm = all(sorted(v for e in es for v in e) == list(range(6)) for es in s6)
    chk(C, "6 vertices, 12 edges, K4-free: exactly the 15 K6-minus-perfect-matching graphs", len(s6) == 15 and pm)
    stamp(C)


# ------------------------------------------------------------------ control M
def control_M(s3, s4):
    C = "M_rank_moment_tables"
    claimed4 = {10: (16, 6, 37, 112, 111), 11: (20, 6, 45, 136, 135), 12: (24, 7, 54, 163, 162),
                13: (30, 8, 63, 194, 189), 14: (36, 9, 73, 227, 219), 15: (42, 10, 84, 262, 252),
                16: (48, 11, 96, 299, 288)}
    rows = {}
    for N in range(8, 17):
        bound = Fr(16) + Fr((N - 4) ** 2, 7) - N
        Hmin = math.ceil(bound / 2)
        Amin = min(s4[N]["A"])
        t4 = 3 * N * N // 8
        lhs, rhs = 2 * comb(N, 2) + Amin + Hmin, 3 * t4
        rows[N] = (Amin, Hmin, t4, lhs, rhs)
    put(C, "4x4 rows N: (A_min over all graphs, H_min from (2), t4, LHS, RHS)", {str(k): v for k, v in rows.items()})
    chk(C, "4x4 table N=10..16 reproduced exactly and LHS > RHS in every row",
        all(rows[N] == claimed4[N] and rows[N][3] > rows[N][4] for N in claimed4))
    chk(C, "N=9: A=12, H>=6, LHS = RHS = 90 (equality case)", rows[9] == (12, 6, 30, 90, 90))
    chk(C, "negative: N=8 (sole C8) is NOT excluded by inequality (1): LHS 70 <= RHS 72, so section 1 is needed",
        rows[8][3] <= rows[8][4] and rows[8][3:] == (70, 72), kind="negative")
    # H lower bound without the ceiling at N=11 is exactly an integer (6)
    chk(C, "(2) at N=11 is exactly integral: (16+49/7-11)/2 = 6", (Fr(16) + Fr(49, 7) - 11) / 2 == 6)
    claimed3 = {6: (6, 36, 36), 7: (10, 52, 48), 8: (14, 70, 63), 9: (18, 90, 81)}
    r3 = {}
    for N in (6, 7, 8, 9):
        A = min(s3[N]["A"])
        r3[N] = (A, 2 * comb(N, 2) + A, 3 * (N * N // 3))
    put(C, "3x3 rows N: (A, LHS, RHS)", {str(k): v for k, v in r3.items()})
    chk(C, "3x3 table reproduced; N=7,8,9 strictly violated, N=6 equality",
        r3 == claimed3 and all(r3[N][1] > r3[N][2] for N in (7, 8, 9)) and r3[6][1] == r3[6][2])
    # sanity of (2) on the actual C8 channel of control F (S = 4|p><p| + 4|q><q|)
    chk(C, "(2) on an actual C8 channel: tr S^2 = 32 >= 16+16/7 and H=12 >= 6",
        Fr(32) >= 16 + Fr(16, 7) and 12 >= math.ceil((16 + Fr(16, 7) - 8) / 2))
    stamp(C)


# ------------------------------------------------------------------ control R
def perfect_matchings(lst):
    if not lst:
        yield []
        return
    a = lst[0]
    for i in range(1, len(lst)):
        rest = lst[1:i] + lst[i + 1:]
        for m in perfect_matchings(rest):
            yield [(a, lst[i])] + m


def partitions_3222():
    out = []
    for T in itertools.combinations(range(9), 3):
        rest = [x for x in range(9) if x not in T]
        for m in perfect_matchings(rest):
            out.append([T] + m)
    return out


def canon_graph(cells):
    """Canonical form of a 4x4 support graph under row/column permutations and transposition."""
    best = None
    for rp in itertools.permutations(range(4)):
        for cp in itertools.permutations(range(4)):
            t1 = tuple(sorted((rp[i], cp[j]) for i, j in cells))
            t2 = tuple(sorted((cp[j], rp[i]) for i, j in cells))
            m = t1 if t1 < t2 else t2
            if best is None or m < best:
                best = m
    return best


def det_mod_p(A, p=2147483647):
    M = [[x % p for x in r] for r in A]
    n, d = len(M), 1
    for c in range(n):
        piv = next((i for i in range(c, n) if M[i][c]), None)
        if piv is None:
            return 0
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            d = -d
        d = d * M[c][c] % p
        inv = pow(M[c][c], p - 2, p)
        for i in range(c + 1, n):
            if M[i][c]:
                f = M[i][c] * inv % p
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[c])]
    return d % p


def control_R():
    C = "R_N9_pentads_incidence_rank"
    parts = partitions_3222()
    chk(C, "number of (3,2,2,2) partitions of 9 points is 1260", len(parts) == 1260)
    pairs = list(itertools.combinations(range(9), 2))
    pidx = {p: i for i, p in enumerate(pairs)}

    def pmask(blocks):
        mk = 0
        for bl in blocks:
            for a, b in itertools.combinations(sorted(bl), 2):
                mk |= 1 << pidx[(a, b)]
        return mk
    pms = [pmask(p) for p in parts]

    def setup(cells):
        rowsb = [tuple(x for x in range(9) if cells[x][0] == r) for r in range(4)]
        colsb = [tuple(x for x in range(9) if cells[x][1] == c) for c in range(4)]
        line = pmask(rowsb) | pmask(colsb)
        L = [i for i, m in enumerate(pms) if not (m & line)]
        compat = {i: set() for i in L}
        for ii, i in enumerate(L):
            for j in L[ii + 1:]:
                if not (pms[i] & pms[j]):
                    compat[i].add(j)
        tri = [(i, j, l) for i in L for j in sorted(compat[i]) for l in sorted(compat[i] & compat[j])]
        return rowsb, colsb, line, L, tri

    # (a) all 816 labelled graphs: count pentads, H0 degree <= 3, det(BB^T) != 0 mod p
    groups = {}
    total, deg_all, detp_all, h0_edges = 0, True, True, set()
    per_graph = []
    for cells in G4_N9:
        groups.setdefault(canon_graph(cells), []).append(cells)
        rowsb, colsb, line, L, tri = setup(cells)
        per_graph.append(len(tri))
        total += len(tri)
        for i, j, l in tri:
            cov = line | pms[i] | pms[j] | pms[l]
            deg = [0] * 9
            BBt = [[5 if x == y else 0 for y in range(9)] for x in range(9)]
            ne = 0
            for (x, y), t in pidx.items():
                if (cov >> t) & 1:
                    BBt[x][y] = BBt[y][x] = 1
                else:
                    deg[x] += 1
                    deg[y] += 1
                    ne += 1
            h0_edges.add(ne)
            deg_all &= max(deg) <= 3
            detp_all &= det_mod_p(BBt) != 0
    put(C, "labelled N=9 support graphs / isomorphism classes (row, column perms and transpose)",
        [len(G4_N9), len(groups)])
    put(C, "labelled pentads (unordered mate-partition triples) total; per-graph counts present",
        [total, sorted(set(per_graph))])
    put(C, "H0 edge counts seen over all labelled pentads", sorted(h0_edges))
    chk(C, "combinatorial pentads exist (the incidence-rank argument is not vacuous)", total > 0)
    chk(C, "all labelled pentads: H0 has exactly 6 edges and max degree <= 3", deg_all and h0_edges == {6})
    chk(C, "all labelled pentads: det(BB^T) nonzero mod 2^31-1, hence rank B = 9 over Q", detp_all)
    # (b) one representative per isomorphism class: complete exact rational checks
    rank_ok = gram_ok = det_ok = True
    weight_status, min_det, examples, cls_info = {}, None, [], []
    naive_ok = None
    for key, members in sorted(groups.items()):
        cells = members[0]
        rowsb, colsb, line, L, tri = setup(cells)
        same = all(len(setup(m)[4]) == len(tri) for m in members)
        cls_info.append({"orbit_size": len(members), "pentads_per_graph": len(tri), "uniform_count": same})
        if naive_ok is None:                       # cross-check the triangle enumeration naively once
            naive = sum(1 for a_, b_, c_ in itertools.combinations(L, 3)
                        if not (pms[a_] & pms[b_] or pms[a_] & pms[c_] or pms[b_] & pms[c_]))
            naive_ok = naive == len(tri)
        for i, j, l in tri:
            blocks = rowsb + colsb + [tuple(b) for b in parts[i]] + [tuple(b) for b in parts[j]] + \
                [tuple(b) for b in parts[l]]
            B = [[1 if x in bl else 0 for bl in blocks] for x in range(9)]
            cov = line | pms[i] | pms[j] | pms[l]
            h0 = [[0] * 9 for _ in range(9)]
            for (x, y), t in pidx.items():
                if not (cov >> t) & 1:
                    h0[x][y] = h0[y][x] = 1
            BBt = [[sum(B[x][s] * B[y][s] for s in range(20)) for y in range(9)] for x in range(9)]
            gram_ok &= BBt == [[(4 if x == y else 0) + 1 - h0[x][y] for y in range(9)] for x in range(9)]
            rk = rank_exact(B)
            rank_ok &= rk == 9
            d = det_exact(BBt)
            det_ok &= d > 0
            min_det = d if min_det is None else min(min_det, d)
            st, w = solve_exact([[B[x][s] for x in range(9)] for s in range(20)], [1] * 20)
            k = st if st != "unique" else ("unique_positive" if all(v > 0 for v in w) else "unique_not_positive")
            weight_status[k] = weight_status.get(k, 0) + 1
            if len(examples) < 2:
                examples.append({"cells": cells, "R": parts[i], "S": parts[j], "T": parts[l], "rank_B": rk,
                                 "det_BBt": str(d), "weights": st, "w": [str(v) for v in w] if w else None})
    put(C, "isomorphism classes: orbit size, pentads per graph", cls_info)
    put(C, "representatives: weight system B^T w = 1 status counts", weight_status)
    put(C, "representatives: minimum det(BB^T)", str(min_det))
    put(C, "examples", examples)
    chk(C, "orbit sizes sum to 816 and pentad counts are constant on each class; labelled total reproduced",
        sum(c["orbit_size"] for c in cls_info) == len(G4_N9) and all(c["uniform_count"] for c in cls_info) and
        sum(c["orbit_size"] * c["pentads_per_graph"] for c in cls_info) == total)
    chk(C, "triangle enumeration agrees with naive triple enumeration on a representative", naive_ok)
    chk(C, "representatives (all pentads): BB^T = 4I + J - Adj(H0) exactly", gram_ok)
    chk(C, "representatives (all pentads): rank B = 9 exactly and det(BB^T) > 0", rank_ok and det_ok)
    # negative: two points sharing every block -> equal incidence rows -> rank <= 8
    neg_blocks = [(0, 1, 2), (3, 4), (5, 6), (7, 8)] * 5
    Bn = [[1 if x in bl else 0 for bl in neg_blocks] for x in range(9)]
    chk(C, "negative: if two points shared all five blocks, B would have rank < 9 (needs the no-repeated-pair rule)",
        rank_exact(Bn) < 9, kind="negative")
    # negative 2: replacing T by R violates the rule and breaks the BB^T identity
    ex = examples[0]
    cells = ex["cells"]
    rowsb = [tuple(x for x in range(9) if cells[x][0] == r) for r in range(4)]
    colsb = [tuple(x for x in range(9) if cells[x][1] == c) for c in range(4)]
    blocks = rowsb + colsb + [tuple(b) for b in ex["R"]] + [tuple(b) for b in ex["S"]] + [tuple(b) for b in ex["R"]]
    B2 = [[1 if x in bl else 0 for bl in blocks] for x in range(9)]
    BBt2 = [[sum(B2[x][s] * B2[y][s] for s in range(20)) for y in range(9)] for x in range(9)]
    chk(C, "negative: with T:=R some off-diagonal BB^T entry equals 2, so BB^T = 4I+J-Adj(H0) fails",
        any(BBt2[x][y] == 2 for x in range(9) for y in range(9) if x != y), kind="negative")
    stamp(C)


# ------------------------------------------------------------------ control X
class GQ:
    """Gaussian rational."""
    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re, self.im = Fr(re), Fr(im)

    def __add__(self, o):
        return GQ(self.re + o.re, self.im + o.im)

    def __mul__(self, o):
        return GQ(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def conj(self):
        return GQ(self.re, -self.im)

    def abs2(self):
        return self.re * self.re + self.im * self.im

    def zero(self):
        return self.re == 0 and self.im == 0


def gip(u, v):
    s = GQ(0)
    for a, b in zip(u, v):
        s = s + a.conj() * b
    return s


def gvec(*xs):
    return [x if isinstance(x, GQ) else GQ(*x) if isinstance(x, tuple) else GQ(x) for x in xs]


def cross_gram(u, v):
    """u, v: two-element lists of (unnormalised) vectors.  Returns zero pattern and
    det(G G* - I) of the normalised cross-Gram G (exact, rational)."""
    n_u = [gip(x, x).re for x in u]
    n_v = [gip(x, x).re for x in v]
    g = [[gip(u[i], v[j]) for j in range(2)] for i in range(2)]
    zeros = [[g[i][j].zero() for j in range(2)] for i in range(2)]
    a11 = sum(g[0][j].abs2() / (n_u[0] * n_v[j]) for j in range(2))
    a22 = sum(g[1][j].abs2() / (n_u[1] * n_v[j]) for j in range(2))
    s12 = GQ(0)
    for j in range(2):
        s12 = s12 + g[0][j] * g[1][j].conj() * GQ(Fr(1) / n_v[j])
    a12abs2 = s12.abs2() / (n_u[0] * n_u[1])
    return zeros, (a11 - 1) * (a22 - 1) - a12abs2, a11 + a22


def poly_mul(p, q):
    r = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            m = tuple(a + b for a, b in zip(m1, m2))
            r[m] = r.get(m, 0) + c1 * c2
    return {m: c for m, c in r.items() if c}


def poly_add(p, q, s=1):
    r = dict(p)
    for m, c in q.items():
        r[m] = r.get(m, 0) + s * c
    return {m: c for m, c in r.items() if c}


def control_X():
    C = "X_cross_gram"
    ea = [1, 0, 0]
    # X1: different planes span(e0,e1), span(e0,(3e1+4e2)/5), bases with exactly one zero
    p1, q1 = gvec(1, 1, 0), gvec(1, -1, 0)
    p2, q2 = gvec(-3, 3, 4), gvec(25, 9, 12)
    chk(C, "X1 bases orthogonal and all a-coefficients nonzero",
        gip(p1, q1).zero() and gip(p2, q2).zero() and all(not v[0].zero() for v in (p1, q1, p2, q2)))
    z1, d1, _ = cross_gram([p1, q1], [p2, q2])
    chk(C, "X1 (P2 != P3): exactly one zero; det(GG*-I)=0 so ||G||=1",
        sum(map(sum, z1)) == 1 and d1 == 0)
    # X2: same plane, same projective basis (swapped): exactly two zeros, anti-diagonal/diagonal
    z2, d2, _ = cross_gram([p1, q1], [gvec(2, -2, 0), gvec(-3, -3, 0)])
    chk(C, "X2 (same plane, same ray basis): two zeros on one diagonal, never a whole row",
        sum(map(sum, z2)) == 2 and not any(all(r) for r in z2) and not any(z2[0][j] and z2[1][j] for j in range(2))
        and d2 == 0)
    # X3: same plane, different basis e0 +- i e1: no zero at all
    z3, d3, _ = cross_gram([p1, q1], [gvec(1, (0, 1), 0), gvec(1, (0, -1), 0)])
    chk(C, "X3 (same plane, different ray basis): all four cross overlaps nonzero", sum(map(sum, z3)) == 0 and d3 == 0)
    # X4: different planes, generic bases: zero zeros
    z4, d4, _ = cross_gram([p1, q1], [gvec(1, 3, 4), gvec(-50, 6, 8)])
    chk(C, "X4 (different planes, generic) : 0 zeros, ||G||=1",
        gip(gvec(1, 3, 4), gvec(-50, 6, 8)).zero() and sum(map(sum, z4)) == 0 and d4 == 0)
    # real-parametrised identities: p1=x1 e0+y1 e1, q1=-y1 e0+x1 e1, v=c e1+s e2 (c^2+s^2=1),
    # p2=x2 e0+y2 v, q2=-y2 e0+x2 v.  Variables (x1,y1,x2,y2,c).
    def mono(**kw):
        order = ("x1", "y1", "x2", "y2", "c")
        return tuple(kw.get(v, 0) for v in order)
    P = lambda *terms: {mono(**t): c for c, t in terms}
    pp = P((1, {"x1": 1, "x2": 1}), (1, {"y1": 1, "y2": 1, "c": 1}))            # <p1,p2>
    qq = P((1, {"y1": 1, "y2": 1}), (1, {"x1": 1, "x2": 1, "c": 1}))            # <q1,q2>
    pq = P((-1, {"x1": 1, "y2": 1}), (1, {"y1": 1, "x2": 1, "c": 1}))           # <p1,q2>
    qp = P((-1, {"y1": 1, "x2": 1}), (1, {"x1": 1, "y2": 1, "c": 1}))           # <q1,p2>
    one_plus_c, one_minus_c = P((1, {}), (1, {"c": 1})), P((1, {}), (-1, {"c": 1}))
    c_minus_1 = P((-1, {}), (1, {"c": 1}))
    ok = (poly_add(pp, qq) == poly_mul(P((1, {"x1": 1, "x2": 1}), (1, {"y1": 1, "y2": 1})), one_plus_c) and
          poly_add(pp, qq, -1) == poly_mul(P((1, {"x1": 1, "x2": 1}), (-1, {"y1": 1, "y2": 1})), one_minus_c) and
          poly_add(pq, qp) == poly_mul(P((1, {"x1": 1, "y2": 1}), (1, {"y1": 1, "x2": 1})), c_minus_1) and
          poly_add(pq, qp, -1) == poly_mul(P((-1, {"x1": 1, "y2": 1}), (1, {"y1": 1, "x2": 1})), one_plus_c))
    chk(C, "real-case identities: diagonal or anti-diagonal double zero with c != +-1 forces x1x2=y1y2=0 or x1y2=y1x2=0",
        ok)
    # negative: if the planes were allowed to coincide (c = 1) a diagonal double zero is possible
    chk(C, "negative: with P2 = P3 (c=1) the double-zero pattern is realised (X2), so plane distinctness is the operative premise",
        sum(map(sum, z2)) == 2, kind="negative")
    stamp(C)


# ------------------------------------------------------------------ QLS helpers (Gaussian integer vectors)
def e(s, dim=8):
    return tuple((1, 0) if t == s else (0, 0) for t in range(dim))


def vadd(u, v, sgn=1):
    return tuple((a[0] + sgn * b[0], a[1] + sgn * b[1]) for a, b in zip(u, v))


def vmul_i(u):
    return tuple((-a[1], a[0]) for a in u)


def ipz(u, v):
    re = im = 0
    for (ar, ai), (br, bi) in zip(u, v):
        re += ar * br + ai * bi
        im += ar * bi - ai * br
    return re, im


def is_qls(Q):
    for r in range(8):
        for c1 in range(8):
            if ipz(Q[r][c1], Q[r][c1]) == (0, 0):
                return False
            for c2 in range(c1 + 1, 8):
                if ipz(Q[r][c1], Q[r][c2]) != (0, 0) or ipz(Q[c1][r], Q[c2][r]) != (0, 0):
                    return False
    return True


def weight(v, a):
    num = v[a][0] ** 2 + v[a][1] ** 2
    den = sum(x * x + y * y for x, y in v)
    return Fr(num, den)


def channel(Q, a, r0=0):
    """Off-row a-channel of a member standardised at row r0 (Q[r0][c] ~ e_c)."""
    W = [[weight(Q[r][c], a) for c in range(8)] for r in range(8)]
    ds = all(sum(W[r]) == 1 for r in range(8)) and all(sum(W[r][c] for r in range(8)) == 1 for c in range(8))
    sup = [(r, c) for r in range(8) for c in range(8) if W[r][c] != 0 and (r, c) != (r0, a)]
    inboard = all(r != r0 and c != a for r, c in sup)
    par = {}

    def f(x):
        par.setdefault(x, x)
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for r, c in sup:
        par[f(("r", r))] = f(("c", c))
    comps = {}
    for r, c in sup:
        comps.setdefault(f(("r", r)), []).append((r, c))
    types = sorted((len({x[0] for x in cl}), len(cl)) for cl in comps.values())
    nontriv = [t for t in types if t[1] > t[0]]
    return {"doubly_stochastic": ds, "support_in_7x7": inboard, "sigma": len(sup) - 7,
            "nontrivial_components": nontriv, "support": set(sup)}


def orth_table(Q):
    vec = [Q[x // 8][x % 8] for x in range(64)]
    return [[x != y and ipz(vec[x], vec[y]) == (0, 0) for y in range(64)] for x in range(64)]


def orth_classes(Q):
    orth = orth_table(Q)
    classes = []
    for perm in itertools.permutations(range(8)):
        idx = [r * 8 + perm[r] for r in range(8)]
        ok = True
        for s in range(8):
            ox = orth[idx[s]]
            for t in range(s + 1, 8):
                if not ox[idx[t]]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            classes.append(sum(1 << x for x in idx))
    return classes


def exact_covers(classes, cap=None, ncells=64):
    by_cell = [[] for _ in range(ncells)]
    for i, m in enumerate(classes):
        for x in range(ncells):
            if (m >> x) & 1:
                by_cell[x].append(i)
    full = (1 << ncells) - 1
    sols = []
    state = {"capped": False}

    def go(cov, chosen):
        if cov == full:
            sols.append(tuple(chosen))
            if cap is not None and len(sols) >= cap:
                state["capped"] = True
                return True
            return False
        best = None
        for x in range(ncells):
            if not (cov >> x) & 1:
                lst = [i for i in by_cell[x] if not (classes[i] & cov)]
                if best is None or len(lst) < len(best):
                    best = lst
                    if not lst:
                        return False
        for i in best:
            chosen.append(i)
            if go(cov | classes[i], chosen):
                return True
            chosen.pop()
        return False
    go(0, [])
    return [[classes[i] for i in s] for s in sols], state["capped"]


def compatible(classes, mates):
    return [m for m in classes if all((m & c).bit_count() == 1 for M in mates for c in M)]


def classical_member(mate):
    """Standardise a classical mate at row 0: the class meeting (0,c) gets symbol c."""
    R = [[None] * 8 for _ in range(8)]
    for cl in mate:
        cells = [x for x in range(64) if (cl >> x) & 1]
        sym = next(x % 8 for x in cells if x // 8 == 0)
        for x in cells:
            R[x // 8][x % 8] = e(sym)
    return R


def family_orthogonal(members):
    vecs = [[M[x // 8][x % 8] for x in range(64)] for M in members]
    for i, j in itertools.combinations(range(len(members)), 2):
        for x in range(64):
            for y in range(x + 1, 64):
                if ipz(vecs[i][x], vecs[i][y]) != (0, 0) and ipz(vecs[j][x], vecs[j][y]) != (0, 0):
                    return False
    return True


# ------------------------------------------------------------------ control F
def control_F():
    C = "F_three_family_C8_member"
    idx = lambda x, y: 2 * (x % 4) + (y % 2)
    add = lambda i, j: idx(i // 2 + j // 2, i % 2 + j % 2)
    L = [[add(r, c) for c in range(8)] for r in range(8)]
    a, b = idx(1, 0), idx(2, 0)
    Z = [(r, c) for r in range(8) for c in range(8) if L[r][c] in (a, b) and r % 2 == 1]
    p, q = vadd(e(a), e(b)), vadd(e(a), e(b), -1)
    Q = [[e(L[r][c]) for c in range(8)] for r in range(8)]
    for r, c in Z:
        Q[r][c] = p if L[r][c] == a else q
    chk(C, "Q is an ordinary QLS(8), row 0 standard, Z has 8 cells on 4 rows/4 columns not meeting row 0",
        is_qls(Q) and all(Q[0][c] == e(c) for c in range(8)) and len(Z) == 8 and all(r != 0 for r, _ in Z))
    ch = {s: channel(Q, s) for s in range(8)}
    chk(C, "Q channels: doubly stochastic, supports inside the 7x7 board",
        all(ch[s]["doubly_stochastic"] and ch[s]["support_in_7x7"] for s in range(8)))
    chk(C, "Q: sigma_a = sigma_b = 4 with one sole (4,8) component (a C8); every other coordinate inactive",
        ch[a]["sigma"] == 4 and ch[a]["nontrivial_components"] == [(4, 8)] and ch[b]["sigma"] == 4 and
        all(ch[s]["sigma"] == 0 for s in range(8) if s not in (a, b)))
    classes = orth_classes(Q)
    put(C, "Q-orthogonal transversal classes", len(classes))
    mates, capped = exact_covers(classes, cap=200000)
    put(C, "classical mates of Q (all, unless capped)", [len(mates), capped])
    chk(C, "Q has classical mates", len(mates) > 0)
    # orthogonal pair search
    pair = None
    for M in mates:
        sub = compatible(classes, [M])
        Ns, _ = exact_covers(sub, cap=1)
        if Ns:
            pair = (M, Ns[0])
            break
    chk(C, "an orthogonal pair of classical mates exists (three-family Q,R,S)", pair is not None)
    if pair is None:
        stamp(C)
        return
    Rm, Sm = pair
    R, S = classical_member(Rm), classical_member(Sm)
    chk(C, "Q,R,S: every member a QLS and every pair's 64 same-cell products orthonormal (exact)",
        is_qls(R) and is_qls(S) and family_orthogonal([Q, R, S]))
    chR = {s: channel(R, s) for s in range(8)}
    chS = {s: channel(S, s) for s in range(8)}
    chk(C, "three-family per-coordinate supports pairwise disjoint on the 7x7 board (budget premise)",
        all(not (ch[s]["support"] & chR[s]["support"]) and not (ch[s]["support"] & chS[s]["support"]) and
            not (chR[s]["support"] & chS[s]["support"]) for s in range(8)))
    # section 1 mechanism: transition supports
    pc = [r * 8 + c for r, c in Z if L[r][c] == a]
    qc = [r * 8 + c for r, c in Z if L[r][c] == b]

    def cls_of(Mm):
        arr = [None] * 64
        for i, cl in enumerate(Mm):
            for x in range(64):
                if (cl >> x) & 1:
                    arr[x] = i
        return arr
    aR, aS = cls_of(Rm), cls_of(Sm)
    mech = True
    detail = []
    for x in pc:
        adj = [y for y in qc if y // 8 == x // 8 or y % 8 == x % 8]
        free = [y for y in qc if y not in adj]
        yR = [y for y in qc if aR[y] == aR[x]]
        yS = [y for y in qc if aS[y] == aS[x]]
        mech &= len(adj) == 2 and len(yR) == 1 and len(yS) == 1 and yR[0] in free and yS[0] in free and yR != yS
        detail.append({"p_cell": divmod(x, 8), "adjacent_q": [divmod(y, 8) for y in adj],
                       "R_uses": divmod(yR[0], 8) if yR else None, "S_uses": divmod(yS[0], 8) if yS else None})
    put(C, "transition-support detail", detail)
    chk(C, "section-1 mechanism: each p cell has 2 adjacent q cells; R and S use the two free ones, disjointly",
        mech)
    sub3 = compatible(classes, [Rm, Sm])
    T3, _ = exact_covers(sub3, cap=None)
    put(C, "classes compatible with both R and S / third classical mates", [len(sub3), len(T3)])
    chk(C, "negative: no third classical mate orthogonal to R and S (both free transition slots used)",
        len(T3) == 0, kind="negative")
    # exhaustive over all orthogonal pairs of classical mates (when mates enumerated in full)
    if not capped:
        npairs, ntriples = 0, 0
        keyset = {tuple(sorted(M)) for M in mates}
        for M in mates:
            sub = compatible(classes, [M])
            Ns, _ = exact_covers(sub, cap=None)
            for N in Ns:
                if tuple(sorted(N)) not in keyset:
                    continue
                npairs += 1
                t, _ = exact_covers(compatible(sub, [N]), cap=None)
                ntriples += len(t)
        put(C, "ordered orthogonal classical mate pairs / third mates found over all pairs", [npairs, ntriples])
        chk(C, "negative: over every orthogonal pair of classical mates, no third mutually orthogonal classical mate",
            ntriples == 0, kind="negative")
    # light-cell pigeonhole at k=4: 7-k = 3 free singleton cells (no contradiction), R,S use distinct ones
    sing = [r * 8 + c for r in range(1, 8) for c in range(8) if Q[r][c] == e(a)]
    xb = b
    zR = [z for z in sing if aR[z] == aR[xb]]
    zS = [z for z in sing if aS[z] == aS[xb]]
    chk(C, "light-cell pigeonhole at k=4: 3 singleton e_a cells; R and S meet row-0 e_b at distinct ones",
        len(sing) == 3 and len(zR) == 1 and len(zS) == 1 and zR != zS)
    put(C, "R and S (row-0-standardised symbols)", {"R": [[R[r][c].index((1, 0)) for c in range(8)] for r in range(8)],
                                                   "S": [[S[r][c].index((1, 0)) for c in range(8)] for r in range(8)],
                                                   "Q_classical_symbols": L, "Z_cells": Z, "a": a, "b": b})
    stamp(C)


# ------------------------------------------------------------------ control K
def control_K():
    C = "K_intercalate_members_Z2cubed"
    L = [[r ^ c for c in range(8)] for r in range(8)]

    def inter(r, s1, s2):
        r2 = r ^ s1 ^ s2
        return [(r, r ^ s1), (r2, r ^ s2)], [(r, r ^ s2), (r2, r ^ s1)]

    def build(mods):
        Q = [[e(L[r][c]) for c in range(8)] for r in range(8)]
        for cells_p, cells_q, pv, qv in mods:
            for (r, c) in cells_p:
                Q[r][c] = pv
            for (r, c) in cells_q:
                Q[r][c] = qv
        return Q
    pab, qab = vadd(e(1), e(2)), vadd(e(1), e(2), -1)
    pabi, qabi = vadd(e(1), vmul_i(e(2))), vadd(e(1), vmul_i(e(2)), -1)
    pac, qac = vadd(e(1), e(4)), vadd(e(1), e(4), -1)
    I47 = inter(4, 1, 2)
    I56 = inter(5, 1, 2)
    I36 = inter(3, 1, 4)
    cases = {
        "K0_classical_Z2^3": ([], None),
        "K1_sole_2x2": ([(I47[0], I47[1], pab, qab)], [(2, 4)]),
        "K2_two_2x2_same_plane_same_basis": ([(I47[0], I47[1], pab, qab), (I56[0], I56[1], pab, qab)],
                                             [(2, 4), (2, 4)]),
        "K3_two_2x2_same_plane_other_basis": ([(I47[0], I47[1], pab, qab), (I56[0], I56[1], pabi, qabi)],
                                              [(2, 4), (2, 4)]),
        "K4_two_2x2_different_planes": ([(I47[0], I47[1], pab, qab), (I36[0], I36[1], pac, qac)],
                                        [(2, 4), (2, 4)]),
    }
    summary = {}
    for name, (mods, expect_comp) in cases.items():
        Q = build(mods)
        ok_q = is_qls(Q) and all(Q[0][c] == e(c) for c in range(8))
        cha = channel(Q, 1)
        comp_ok = (cha["nontrivial_components"] == (expect_comp or [])) and cha["doubly_stochastic"]
        classes = orth_classes(Q)
        cap = 1 if name.startswith("K0") else 200000
        mates, capped = exact_covers(classes, cap=cap)
        info = {"qls": ok_q, "a_channel_sigma": cha["sigma"], "a_components": cha["nontrivial_components"],
                "orth_classes": len(classes), "classical_mates": len(mates), "capped": capped}
        if name.startswith("K2") and mates and not capped:
            npairs = ntrip = 0
            keyset = {tuple(sorted(M)) for M in mates}
            for M in mates:
                sub = compatible(classes, [M])
                Ns, _ = exact_covers(sub, cap=None)
                for N in Ns:
                    if tuple(sorted(N)) in keyset:
                        npairs += 1
                        t, _ = exact_covers(compatible(sub, [N]), cap=None)
                        ntrip += len(t)
            info["ordered_orthogonal_pairs"] = npairs
            info["third_mates_over_all_pairs"] = ntrip
        summary[name] = info
        chk(C, f"{name}: QLS with row 0 standard and intended a-channel components {expect_comp}", ok_q and comp_ok)
    put(C, "cases", summary)
    chk(C, "K0 positive: the classical Z2^3 member has classical mates", summary["K0_classical_Z2^3"]["classical_mates"] >= 1)
    chk(C, "K1 negative: sole 2x2 member has no classical mate (inner appendix: impossible with one mate)",
        summary["K1_sole_2x2"]["classical_mates"] == 0 and not summary["K1_sole_2x2"]["capped"], kind="negative")
    chk(C, "K3 negative: two 2x2, same plane, different bases -> no classical mate (section 2: excluded with one mate)",
        summary["K3_two_2x2_same_plane_other_basis"]["classical_mates"] == 0, kind="negative")
    chk(C, "K4 negative: two 2x2, different planes -> no classical mate (section 2: excluded with one mate)",
        summary["K4_two_2x2_different_planes"]["classical_mates"] == 0, kind="negative")
    k2 = summary["K2_two_2x2_same_plane_same_basis"]
    if "third_mates_over_all_pairs" in k2:
        chk(C, "K2 (same basis): no three mutually orthogonal classical mates (section 2 transition pigeonhole)",
            k2["third_mates_over_all_pairs"] == 0, kind="negative")
    # GF(8) four-family: classical positive control of the final statement
    def gmul(x, y):
        r = 0
        for i in range(3):
            if (y >> i) & 1:
                r ^= x << i
        for i in (4, 3):
            if (r >> i) & 1:
                r ^= 0b1011 << (i - 3)
        return r
    chk(C, "GF(8) multiplication table is a field (x^3+x+1): every nonzero element invertible",
        all(any(gmul(x, y) == 1 for y in range(1, 8)) for x in range(1, 8)))
    fam = []
    for lam in (1, 2, 3, 4):
        Lm = [[r ^ gmul(lam, c) for c in range(8)] for r in range(8)]
        # standardise row 0 (symbol at (0,c) is lam*c): relabel symbol s -> column c with lam*c = s
        inv = {gmul(lam, c): c for c in range(8)}
        fam.append([[e(inv[Lm[r][c]]) for c in range(8)] for r in range(8)])
    ok4 = all(is_qls(M) for M in fam) and family_orthogonal(fam)
    inactive = all(channel(M, s)["sigma"] == 0 for M in fam for s in range(8))
    chk(C, "GF(8) classical four-MOQLS(8): exact family check, every coordinate inactive in every member "
           "(final statement holds, every local ray complete)", ok4 and inactive)
    stamp(C)


def control_0_selftest():
    C = "0_helper_selftest"
    chk(C, "solve_exact: consistent overdetermined system solved uniquely",
        solve_exact([[1, 0], [0, 1], [1, 1]], [1, 2, 3]) == ("unique", [Fr(1), Fr(2)]))
    chk(C, "solve_exact: inconsistent system detected", solve_exact([[1, 0], [0, 1], [1, 1]], [1, 2, 4])[0] ==
        "inconsistent", kind="negative")
    chk(C, "rank_exact / det_exact / det_mod_p on known matrices",
        rank_exact([[1, 2, 3], [2, 4, 6], [1, 0, 1]]) == 2 and det_exact([[2, 1], [1, 2]]) == 3 and
        det_mod_p([[2, 1], [1, 2]]) == 3 and det_exact([[1, 2], [2, 4]]) == 0)
    chk(C, "conn_mindeg2 accepts C4 and rejects a path and two disjoint C4s",
        conn_mindeg2(2, [(0, 0), (0, 1), (1, 0), (1, 1)]) and not conn_mindeg2(2, [(0, 0), (0, 1), (1, 1)]) and
        not conn_mindeg2(4, [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (2, 3), (3, 2), (3, 3)]), kind="negative")
    stamp(C)


def main():
    control_0_selftest()
    control_P()
    s3, s4 = control_G()
    control_T()
    control_M(s3, s4)
    control_R()
    control_X()
    control_F()
    control_K()
    RES["failures"] = FAILS
    RES["all_checks_ok"] = not FAILS
    RES["n_checks"] = sum(len(v.get("checks", [])) for v in RES["controls"].values())

    def default(o):
        if isinstance(o, (set, frozenset)):
            return sorted(o)
        if isinstance(o, Fr):
            return str(o)
        return str(o)
    for ctrl in RES["controls"].values():
        for k in list(ctrl):
            if isinstance(ctrl[k], dict) and "support" in ctrl[k]:
                ctrl[k].pop("support")
    with open(OUT, "x", encoding="utf-8", newline="\n") as fh:
        json.dump(RES, fh, indent=1, sort_keys=True, default=default)
        fh.write("\n")
    print("checks:", RES["n_checks"], "failures:", len(FAILS))
    for f in FAILS:
        print("FAIL", f)


if __name__ == "__main__":
    main()
