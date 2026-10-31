#!/usr/bin/env python3
"""ReviewF175TuscanOrbit-control-v1.py

Reviewer-authored bounded exact diagnostic control for review wave
f175-tuscan-odd-prime-orbit-asymmetry (manifest SHA-256
a8dec6fcd51e1580cfb7cc69eabf0cab9700762c0955eaa698a0f14ecf500ce0).

Authored independently by ReviewF175TuscanOrbit from its own reading of the
definitions. Python standard library only. It does not import, execute, read or
copy any author code or data, and it runs no order-11, T2(11), SAT or DRAT step.
Finite checks are diagnostics only; the all-odd-prime statements are proved in
writing in review-v1.md.

Definitions implemented (linear rows, directed events):
  order-n array : sequence of n rows; each row is a permutation of range(n),
                  read left to right.
  D1 events     : (x[j], x[j+1]) for 0 <= j <= n-2, over every row x.
  T1            : the n(n-1) D1 events are pairwise distinct.
  D2 events     : (x[j], x[j+2]) for 0 <= j <= n-3, over every row x.
  T2            : T1 and the n(n-2) D2 events are pairwise distinct.
  G(A)          : {g in Sym(n) : {g(x) : x row of A} == {x : x row of A}},
                  with g applied entrywise (positions kept).
  action        : ((g, pi) . A)[i] = g(A[pi^{-1}(i)]) for (g, pi) in S_n x S_n.
  normalized    : A[0] == (0, 1, ..., n-1) and A[r][0] == r for every r.

Usage : python3 ReviewF175TuscanOrbit-control-v1.py RESULTS_JSON_PATH
Exit  : 0 every section ran and every recorded expectation held;
        2 some recorded expectation failed; 3 some section raised an exception;
        4 some section was skipped for the time budget (that slice is UNKNOWN).
"""
import itertools
import json
import math
import platform
import random
import sys
import time
import traceback

T0 = time.monotonic()
SECTION_START_LIMIT_S = 40.0  # a section that would start later is skipped (UNKNOWN)
SAMPLE_STOP_S = 30.0          # p=7 sampling starts no new attempt after this elapsed time
SAMPLE_TARGET = 24
SAMPLE_NODE_CAP = 20000
SEED = 20261029

EXPECTATIONS = []
SECTIONS = {}


def elapsed():
    return round(time.monotonic() - T0, 3)


def expect(section, name, expected, actual):
    ok = expected == actual
    EXPECTATIONS.append({"section": section, "name": name, "expected": expected,
                         "actual": actual, "ok": ok})
    return ok


# ---------------------------------------------------------------- definitions

def perms_of(n):
    return list(itertools.permutations(range(n)))


def inverse(g):
    inv = [0] * len(g)
    for i, v in enumerate(g):
        inv[v] = i
    return tuple(inv)


def is_perm_row(x, n):
    return len(x) == n and sorted(x) == list(range(n))


def d1_events(rows):
    return [(x[j], x[j + 1]) for x in rows for j in range(len(x) - 1)]


def d2_events(rows):
    return [(x[j], x[j + 2]) for x in rows for j in range(len(x) - 2)]


def is_T1(rows, n):
    if len(rows) != n or not all(is_perm_row(x, n) for x in rows):
        return False
    ev = d1_events(rows)
    return len(ev) == n * (n - 1) and len(set(ev)) == len(ev)


def d2_distinct(rows):
    return len(set(d2_events(rows)))


def is_T2(rows, n):
    return is_T1(rows, n) and d2_distinct(rows) == n * (n - 2)


def apply_sym(g, x):
    return tuple(g[s] for s in x)


def act(g, pi, A):
    pinv = inverse(pi)
    return tuple(apply_sym(g, A[pinv[i]]) for i in range(len(A)))


def G_bruteforce(rows, allperms):
    """Every g in Sym(n) is tested exactly for g(rowset) == rowset."""
    rs = frozenset(rows)
    first = rows[0]
    out = []
    for g in allperms:
        if apply_sym(g, first) not in rs:  # g in G implies g(first) in rowset
            continue
        if frozenset(apply_sym(g, x) for x in rows) == rs:
            out.append(g)
    return out


def G_structural(rows, n):
    """Complete alternative: any g in G sends rows[0] to some row R, and R fixes g."""
    rs = frozenset(rows)
    first = rows[0]
    out = []
    for R in rows:
        g = [0] * n
        for j in range(n):
            g[first[j]] = R[j]
        g = tuple(g)
        if frozenset(apply_sym(g, x) for x in rows) == rs:
            out.append(g)
    return sorted(out)


def stabilizer_full(A, allperms):
    return [(g, pi) for g in allperms for pi in allperms if act(g, pi, A) == A]


def stabilizer_via_G(A, allperms):
    """(g,pi).A == A forces g(rowset) == rowset (row permutation keeps the row
    set), so g ranges over brute-forced G(A); pi is brute-forced over all S_n."""
    out = []
    for g in G_bruteforce(list(A), allperms):
        for pi in allperms:
            if act(g, pi, A) == A:
                out.append((g, pi))
    return out


def is_normalized(A, n):
    return tuple(A[0]) == tuple(range(n)) and all(A[r][0] == r for r in range(n))


def normalized_reps_bruteforce(rows, n, allperms, invs):
    """Normalized arrays in the S_n x S_n orbit of any ordering of rows.
    For each g in Sym(n): the identity row lies in g(rowset) iff
    g^{-1}(identity) == inverse(g) lies in rowset; then g(rowset) is listed in
    start-symbol order (rejected and counted if starts are not distinct)."""
    ident = tuple(range(n))
    rs = frozenset(rows)
    reps = set()
    hits = 0
    nonnormalizable = 0
    for g, ginv in zip(allperms, invs):
        if ginv in rs:
            hits += 1
            img = [apply_sym(g, x) for x in rows]
            if sorted(x[0] for x in img) != list(range(n)):
                nonnormalizable += 1
                continue
            img.sort(key=lambda x: x[0])
            if img[0] != ident:
                nonnormalizable += 1
                continue
            reps.add(tuple(img))
    return reps, hits, nonnormalizable


def start_end_indegree(rows, n):
    indeg = [0] * n
    for _, b in d1_events(rows):
        indeg[b] += 1
    later = [0] * n
    first_col = [0] * n
    for x in rows:
        first_col[x[0]] += 1
        for j in range(1, n):
            later[x[j]] += 1
    return {
        "starts_distinct": sorted(x[0] for x in rows) == list(range(n)),
        "ends_distinct": sorted(x[-1] for x in rows) == list(range(n)),
        "each_symbol_indegree_n_minus_1": all(d == n - 1 for d in indeg),
        "later_column_occurrences_equal_indegree": later == indeg,
        "each_symbol_once_in_first_column": all(c == 1 for c in first_col),
    }


# ---------------------------------------------------------------- enumerators

class Cover:
    """Exact cover of the n(n-1) ordered distinct pairs by permutation rows
    (each row covers its n-1 D1 events). Branches on an uncovered pair with the
    fewest compatible rows; every solution row set is produced exactly once."""

    def __init__(self, n):
        self.n = n
        self.P = perms_of(n)
        self.arcs = [[x[j] * n + x[j + 1] for j in range(n - 1)] for x in self.P]
        self.masks = [sum(1 << a for a in ar) for ar in self.arcs]
        full = 0
        for a in range(n):
            for b in range(n):
                if a != b:
                    full |= 1 << (a * n + b)
        self.full = full
        self.index = {x: i for i, x in enumerate(self.P)}

    def search(self, fixed=(), rng=None, max_solutions=None, node_cap=None, deadline=None):
        n, P, arcs, masks, full = self.n, self.P, self.arcs, self.masks, self.full
        cov = 0
        chosen = []
        for x in fixed:
            i = self.index[x]
            if masks[i] & cov:
                return [], 0, "fixed-rows-conflict"
            cov |= masks[i]
            chosen.append(i)
        compat = [i for i in range(len(P)) if not (masks[i] & cov)]
        sols = []
        nodes = [0]

        class Stop(Exception):
            pass

        def rec(cov, compat, chosen):
            nodes[0] += 1
            if node_cap is not None and nodes[0] > node_cap:
                raise Stop("node-cap")
            if deadline is not None and time.monotonic() > deadline:
                raise Stop("deadline")
            if cov == full:
                if len(chosen) != n:
                    raise AssertionError("exact cover with wrong row count")
                sols.append(tuple(P[i] for i in chosen))
                if max_solutions is not None and len(sols) >= max_solutions:
                    raise Stop("max-solutions")
                return
            cnt = [0] * (n * n)
            for i in compat:
                for a in arcs[i]:
                    cnt[a] += 1
            best = -1
            bc = None
            rem = full & ~cov
            while rem:
                low = rem & -rem
                a = low.bit_length() - 1
                rem ^= low
                if bc is None or cnt[a] < bc:
                    bc = cnt[a]
                    best = a
                    if bc == 0:
                        return
            bit = 1 << best
            branch = [i for i in compat if masks[i] & bit]
            if rng is not None:
                rng.shuffle(branch)
            for i in branch:
                m = masks[i]
                rec(cov | m, [j for j in compat if not (masks[j] & m)], chosen + [i])

        status = "complete"
        try:
            rec(cov, compat, chosen)
        except Stop as e:
            status = "stopped:" + str(e)
        return sols, nodes[0], status


def combo_disjoint(n):
    """Independent second enumeration: n-subsets of permutation rows with
    pairwise disjoint D1-event sets, chosen in increasing permutation index."""
    P = perms_of(n)
    masks = [sum(1 << (x[j] * n + x[j + 1]) for j in range(n - 1)) for x in P]
    found = []

    def rec(chosen, cand):
        if len(chosen) == n:
            found.append(frozenset(P[i] for i in chosen))
            return
        for k, i in enumerate(cand):
            m = masks[i]
            rec(chosen + [i], [j for j in cand[k + 1:] if not (masks[j] & m)])

    rec([], list(range(len(P))))
    return found


def normalized_dfs(n):
    """Direct normalized enumeration (row 0 = identity, row r starts with r);
    used only as a cross-check algorithm for orders <= 6."""
    used = [[False] * n for _ in range(n)]
    for j in range(n - 1):
        used[j][j + 1] = True
    rows = [tuple(range(n))]
    results = []

    def build_row(r):
        if r == n:
            results.append(tuple(rows))
            return
        path = [r]
        inrow = [False] * n
        inrow[r] = True

        def ext(v):
            if len(path) == n:
                rows.append(tuple(path))
                build_row(r + 1)
                rows.pop()
                return
            uv = used[v]
            for w in range(n):
                if not inrow[w] and not uv[w]:
                    uv[w] = True
                    inrow[w] = True
                    path.append(w)
                    ext(w)
                    path.pop()
                    inrow[w] = False
                    uv[w] = False

        ext(r)

    build_row(1)
    return results


def orbits_full(X, allp):
    remaining = set(X)
    orbits = []
    while remaining:
        A = min(remaining)
        orb = {act(g, pi, A) for g in allp for pi in allp}
        orbits.append(orb)
        remaining -= orb
    return orbits


def rowsets_json(rowsets):
    return [[list(x) for x in sorted(s)] for s in sorted(rowsets, key=lambda s: sorted(s))]


# ---------------------------------------------------------------- sections

def section_S0():
    sec = "S0-checker-and-intended-reason-negatives"
    out = {}
    A2 = ((0, 1), (1, 0))
    expect(sec, "p2 array (01,10) is T1", True, is_T1(A2, 2))
    expect(sec, "duplicate rows (01,01) are not T1", False, is_T1(((0, 1), (0, 1)), 2))
    expect(sec, "non-permutation row (00,10) is not T1", False, is_T1(((0, 0), (1, 0)), 2))
    base = (0, 1, 2, 3, 4)
    fam = tuple(tuple((v + k) % 5 for v in base) for k in range(5))
    expect(sec, "p5 translates of 01234 (repeated difference 1) are not T1", False, is_T1(fam, 5))
    ev = d1_events(fam)
    out["p5_translates_of_01234_duplicated_events"] = sorted(
        [list(e) for e in set(ev) if ev.count(e) > 1])
    same_start = ((0, 1, 2, 3, 4), (0, 2, 1, 4, 3), (0, 3, 4, 1, 2), (0, 4, 3, 2, 1), (0, 1, 3, 2, 4))
    expect(sec, "five distinct p5 rows all starting with 0 are not T1", False, is_T1(same_start, 5))
    out["same_start_rows_start_symbols"] = sorted(x[0] for x in same_start)
    seq4 = (0, 1, 3, 2)
    fam4 = tuple(tuple((v + k) % 4 for v in seq4) for k in range(4))
    expect(sec, "n4 translates of sequencing 0132 are T1", True, is_T1(fam4, 4))
    G4 = G_bruteforce(list(fam4), perms_of(4))
    expect(sec, "n4 translate family has translation x->x+1 in G", True, (1, 2, 3, 0) in G4)
    out["n4_translate_family_rows"] = [list(x) for x in fam4]
    out["n4_translate_family_G"] = [list(g) for g in G4]
    return out


def section_S1():
    sec = "S1-complete-orders-2-3-4-5"
    out = {}
    for n in (2, 3, 4, 5):
        r = {}
        nf2 = math.factorial(n) ** 2
        allp = perms_of(n)
        cover = Cover(n)
        sols, nodes, status = cover.search()
        rowsets = {frozenset(s) for s in sols}
        combos = combo_disjoint(n)
        r["exact_cover_status"] = status
        r["exact_cover_nodes"] = nodes
        r["t1_rowsets_exact_cover"] = len(rowsets)
        r["t1_rowsets_combination_dfs"] = len(combos)
        expect(sec, f"n{n} exact cover ran to completion", "complete", status)
        expect(sec, f"n{n} exact cover finds each row set once", len(sols), len(rowsets))
        expect(sec, f"n{n} combination DFS finds each row set once", len(combos), len(set(combos)))
        expect(sec, f"n{n} the two enumerations agree", True, rowsets == set(combos))
        expect(sec, f"n{n} every row set passes the independent T1 checker", True,
               all(is_T1(sorted(s), n) for s in rowsets))
        X = {tuple(o) for s in rowsets for o in itertools.permutations(sorted(s))}
        r["X_ordered_arrays"] = len(X)
        r["X_mod_nfact_squared"] = len(X) % nf2
        expect(sec, f"n{n} |X| equals n! times the number of row sets",
               math.factorial(n) * len(rowsets), len(X))
        r["start_end_indegree_all_true"] = all(all(start_end_indegree(A, n).values()) for A in X)
        expect(sec, f"n{n} start/end/indegree identities hold on every ordered array", True,
               r["start_end_indegree_all_true"])
        Gs = {}
        for s in rowsets:
            rows = sorted(s)
            gb = G_bruteforce(rows, allp)
            expect(sec, f"n{n} structural G equals brute-force G for {rows}",
                   sorted(gb), G_structural(rows, n))
            Gs[s] = gb
        r["rowsets"] = rowsets_json(rowsets)
        r["G_orders"] = sorted(len(g) for g in Gs.values())
        orbs = orbits_full(X, allp)
        r["orbit_sizes"] = sorted(len(o) for o in orbs)
        expect(sec, f"n{n} every orbit stays inside X", True, all(o <= X for o in orbs))
        expect(sec, f"n{n} orbits partition X", len(X), sum(len(o) for o in orbs))
        stab = {A: stabilizer_full(A, allp) for A in X}
        r["stabilizer_orders"] = sorted({len(v) for v in stab.values()})
        expect(sec, f"n{n} orbit size times stabilizer order equals (n!)^2", True,
               all(len(o) * len(stab[A]) == nf2 for o in orbs for A in o))
        expect(sec, f"n{n} stabilizer order equals |G(rowset)|", True,
               all(len(stab[A]) == len(Gs[frozenset(A)]) for A in X))
        normalized = [A for A in X if is_normalized(A, n)]
        r["normalized_arrays"] = len(normalized)
        per_orbit = [sum(1 for A in o if is_normalized(A, n)) for o in orbs]
        r["normalized_per_orbit"] = per_orbit
        expect(sec, f"n{n} normalized per orbit times |G| equals n", True,
               all(k * len(Gs[frozenset(min(o))]) == n for k, o in zip(per_orbit, orbs)))
        nd = normalized_dfs(n)
        r["normalized_dfs_count"] = len(nd)
        expect(sec, f"n{n} direct normalized DFS equals normalized arrays of X", True,
               set(nd) == set(normalized) and len(nd) == len(set(nd)))
        if n in (3, 5):
            r["role"] = "odd prime: theorem expectations (vacuous if X is empty)"
            expect(sec, f"n{n} every G trivial", True, all(len(g) == 1 for g in Gs.values()))
            expect(sec, f"n{n} every stabilizer trivial (free action)", True,
                   all(len(v) == 1 for v in stab.values()))
            expect(sec, f"n{n} every orbit has (n!)^2 elements", True, all(len(o) == nf2 for o in orbs))
            expect(sec, f"n{n} every orbit has exactly n normalized arrays", True,
                   all(k == n for k in per_orbit))
            expect(sec, f"n{n} |X| divisible by (n!)^2", 0, len(X) % nf2)
            expect(sec, f"n{n} normalized count divisible by n", 0, len(normalized) % n)
            r["X_is_empty"] = (len(X) == 0)
        elif n == 2:
            r["role"] = "p=2 negative boundary (predicted from the swap symmetry)"
            expect(sec, "n2 exactly one T1 row set", 1, len(rowsets))
            expect(sec, "n2 G is all of Sym(2)", [(0, 1), (1, 0)], sorted(Gs[frozenset(A2_ROWS)]))
            expect(sec, "n2 every stabilizer has order 2 (action not free)", [2], r["stabilizer_orders"])
            expect(sec, "n2 (swap symbols, swap rows) fixes (01,10)", True,
                   ((1, 0), (1, 0)) in stab[A2_ROWS])
            expect(sec, "n2 orbit sizes", [2], r["orbit_sizes"])
            expect(sec, "n2 |X| mod (2!)^2", 2, len(X) % nf2)
            expect(sec, "n2 normalized arrays", 1, len(normalized))
            expect(sec, "n2 normalized per orbit (not p=2)", [1], per_orbit)
        else:
            r["role"] = "even order 4: outside theorem scope; observation plus general identities"
        out[f"n{n}"] = r
    return out


A2_ROWS = ((0, 1), (1, 0))


def section_S1b():
    sec = "S1b-order-6-identity-row-sets"
    n = 6
    out = {"role": "even order 6: outside theorem scope; complete over row sets containing the identity row"}
    allp = perms_of(n)
    invs = [inverse(g) for g in allp]
    ident = tuple(range(n))
    cover = Cover(n)
    sols, nodes, status = cover.search(fixed=(ident,))
    rowsets = {frozenset(s) for s in sols}
    out["exact_cover_status"] = status
    out["exact_cover_nodes"] = nodes
    out["identity_rowsets"] = len(rowsets)
    expect(sec, "exact cover ran to completion", "complete", status)
    expect(sec, "each identity-containing row set found once", len(sols), len(rowsets))
    expect(sec, "every row set passes the T1 checker", True, all(is_T1(sorted(s), n) for s in rowsets))
    expect(sec, "start/end/indegree identities on every row set", True,
           all(all(start_end_indegree(sorted(s), n).values()) for s in rowsets))
    norm = normalized_dfs(n)
    norm_sets = {frozenset(A) for A in norm}
    out["normalized_dfs_count"] = len(norm)
    expect(sec, "normalized DFS gives each array once", len(norm), len(norm_sets))
    expect(sec, "normalized arrays correspond exactly to identity-containing row sets", True,
           norm_sets == rowsets)
    dist = {}
    ok_struct = ok_reps = ok_inside = ok_nonnorm = True
    orbit_units = 0
    example = None
    for s in rowsets:
        rows = sorted(s)
        gb = G_bruteforce(rows, allp)
        if sorted(gb) != G_structural(rows, n):
            ok_struct = False
        k = len(gb)
        dist[str(k)] = dist.get(str(k), 0) + 1
        reps, hits, nonnorm = normalized_reps_bruteforce(rows, n, allp, invs)
        if nonnorm:
            ok_nonnorm = False
        if len(reps) * k != n:
            ok_reps = False
        if not all(frozenset(B) in rowsets for B in reps):
            ok_inside = False
        orbit_units += k
        if k > 1 and (example is None or rows < example[0]):
            example = (rows, gb, len(reps))
    out["G_order_distribution"] = dist
    expect(sec, "structural G equals brute-force G on all row sets", True, ok_struct)
    expect(sec, "no non-normalizable relabelling", True, ok_nonnorm)
    expect(sec, "normalized reps per orbit times |G| equals n", True, ok_reps)
    expect(sec, "normalized reps are among the enumerated row sets", True, ok_inside)
    expect(sec, "sum of |G| over identity row sets divisible by n", 0, orbit_units % n)
    out["orbits"] = orbit_units // n
    if example is not None:
        out["least_example_with_nontrivial_G"] = {
            "rows": [list(x) for x in example[0]],
            "G": [list(g) for g in example[1]],
            "normalized_reps_in_orbit": example[2],
        }
    return out


def section_S2():
    sec = "S2-cyclic-translates-and-endpoint-sum"
    out = {}
    for n in range(2, 10):
        r = {}
        cnt0 = 0
        end_ok = True
        example = None
        residue_sum = (n * (n - 1) // 2) % n
        for tail in itertools.permutations(range(1, n)):
            x = (0,) + tail
            d = [(x[i + 1] - x[i]) % n for i in range(n - 1)]
            if len(set(d)) == n - 1:
                cnt0 += 1
                if example is None:
                    example = x
                if (x[-1] - x[0]) % n != residue_sum:
                    end_ok = False
        r["sequencings_with_x0_equal_0"] = cnt0
        r["nonzero_residue_sum_mod_n"] = residue_sum
        r["least_example"] = list(example) if example is not None else None
        expect(sec, f"n{n} endpoint difference equals residue sum for every distinct-difference base",
               True, end_ok)
        if n % 2 == 1:
            expect(sec, f"n{n} odd: no permutation of Z_n has pairwise distinct consecutive differences",
                   0, cnt0)
        if n <= 7:
            full = 0
            t1fam = 0
            equiv = True
            for x in itertools.permutations(range(n)):
                d = [(x[i + 1] - x[i]) % n for i in range(n - 1)]
                distinct = len(set(d)) == n - 1
                fam = [tuple((v + k) % n for v in x) for k in range(n)]
                t1 = is_T1(fam, n)
                full += distinct
                t1fam += t1
                if t1 != distinct:
                    equiv = False
            r["sequencings_all_bases"] = full
            r["translate_families_T1_all_bases"] = t1fam
            expect(sec, f"n{n} translation invariance of the count", n * cnt0, full)
            expect(sec, f"n{n} translate family is T1 iff differences distinct (all n! bases)", True, equiv)
            if example is not None:
                fam = [tuple((v + k) % n for v in example) for k in range(n)]
                G = G_bruteforce(fam, perms_of(n))
                tau = tuple((s + 1) % n for s in range(n))
                r["example_translate_family_G_order"] = len(G)
                expect(sec, f"n{n} example translate family has the translation automorphism", True, tau in G)
        out[f"n{n}"] = r
    return out


def section_S4():
    sec = "S4-residue-sums"
    primes = [q for q in range(2, 200) if all(q % d for d in range(2, int(q ** 0.5) + 1))]
    bad = [q for q in primes if q > 2 and (q * (q - 1) // 2) % q != 0]
    expect(sec, "odd primes below 200: sum of nonzero residues is 0 mod p", [], bad)
    expect(sec, "p=2: sum of nonzero residues mod 2", 1, (2 * 1 // 2) % 2)
    return {"primes_checked": len(primes), "largest": primes[-1]}


def section_S3():
    sec = "S3-p7-bounded-sample"
    n = 7
    out = {"label": "BOUNDED SAMPLE ONLY: not a census, not a count, not theorem evidence",
           "seed": SEED, "target": SAMPLE_TARGET, "node_cap_per_attempt": SAMPLE_NODE_CAP,
           "stop_new_attempts_after_elapsed_s": SAMPLE_STOP_S}
    allp = perms_of(n)
    invs = [inverse(g) for g in allp]
    ident = tuple(range(n))
    idpair = (ident, ident)
    cover = Cover(n)
    rng = random.Random(SEED)
    samples = []
    seen = set()
    attempts = 0
    attempt_status = {}
    duplicates = 0
    while len(samples) < SAMPLE_TARGET and time.monotonic() - T0 < SAMPLE_STOP_S:
        attempts += 1
        sols, nodes, status = cover.search(rng=rng, max_solutions=1, node_cap=SAMPLE_NODE_CAP,
                                           deadline=T0 + SAMPLE_STOP_S + 5.0)
        attempt_status[status] = attempt_status.get(status, 0) + 1
        if not sols:
            continue
        A = sols[0]  # rows in the order the unnormalized search chose them
        key = frozenset(A)
        if key in seen:
            duplicates += 1
            continue
        seen.add(key)
        rows = list(A)
        rec = {"rows_as_found": [list(x) for x in A], "search_nodes": nodes}
        rec["T1"] = is_T1(A, n)
        rec["start_end_indegree"] = start_end_indegree(A, n)
        gb = G_bruteforce(rows, allp)
        rec["G_order_bruteforce"] = len(gb)
        rec["G_structural_equals_bruteforce"] = sorted(gb) == G_structural(rows, n)
        reps, hits, nonnorm = normalized_reps_bruteforce(rows, n, allp, invs)
        rec["normalized_reps"] = len(reps)
        rec["normalized_hits"] = hits
        rec["nonnormalizable"] = nonnorm
        rec["reps_all_T1_and_normalized"] = all(is_T1(B, n) and is_normalized(B, n) for B in reps)
        if reps:
            m = min(reps)
            reps2, _, _ = normalized_reps_bruteforce(list(m), n, allp, invs)
            rec["renormalization_closure"] = reps2 == reps
            rec["least_normalized_rep"] = [list(x) for x in m]
        else:
            rec["renormalization_closure"] = False
        st = stabilizer_via_G(A, allp)
        rec["stabilizer"] = [[list(g), list(pi)] for g, pi in st]
        rec["stabilizer_is_identity_only"] = st == [idpair]
        rec["d2_distinct_of_35"] = d2_distinct(A)
        rec["T2"] = is_T2(A, n)
        samples.append(rec)
    out["attempts"] = attempts
    out["attempt_status"] = attempt_status
    out["duplicate_row_sets_skipped"] = duplicates
    out["distinct_samples"] = len(samples)
    out["samples"] = samples
    out["T2_among_samples"] = sum(1 for s in samples if s["T2"])
    expect(sec, "p7 sample nonempty", True, len(samples) > 0)
    expect(sec, "p7 all samples T1", True, all(s["T1"] for s in samples))
    expect(sec, "p7 start/end/indegree identities on all samples (search did not assume them)", True,
           all(all(s["start_end_indegree"].values()) for s in samples))
    expect(sec, "p7 all samples |G| = 1 by brute force over S_7", True,
           all(s["G_order_bruteforce"] == 1 for s in samples))
    expect(sec, "p7 structural G agrees with brute force", True,
           all(s["G_structural_equals_bruteforce"] for s in samples))
    expect(sec, "p7 exactly 7 distinct normalized reps per sampled orbit", True,
           all(s["normalized_reps"] == 7 and s["normalized_hits"] == 7 and s["nonnormalizable"] == 0
               for s in samples))
    expect(sec, "p7 reps are T1 and normalized", True, all(s["reps_all_T1_and_normalized"] for s in samples))
    expect(sec, "p7 renormalizing a rep returns the same 7 reps", True,
           all(s["renormalization_closure"] for s in samples))
    expect(sec, "p7 S_7 x S_7 stabilizer is {(id,id)} for each sampled ordered array", True,
           all(s["stabilizer_is_identity_only"] for s in samples))
    if samples:
        A = [tuple(x) for x in samples[0]["rows_as_found"]]
        mut = list(A)
        y = list(mut[1])
        y[2], y[3] = y[3], y[2]
        mut[1] = tuple(y)
        expect(sec, "p7 mutation: swapping two adjacent entries of one row breaks T1", False, is_T1(mut, n))
    return out


# ---------------------------------------------------------------- main

def main():
    if len(sys.argv) != 2:
        print("usage: ReviewF175TuscanOrbit-control-v1.py RESULTS_JSON_PATH", file=sys.stderr)
        return 64
    out_path = sys.argv[1]
    exceptions = []
    order = [("S0", section_S0), ("S1", section_S1), ("S1b", section_S1b),
             ("S2", section_S2), ("S4", section_S4), ("S3", section_S3)]
    for name, fn in order:
        t = elapsed()
        if t > SECTION_START_LIMIT_S:
            SECTIONS[name] = {"status": "SKIPPED_BUDGET_UNKNOWN", "start_elapsed_s": t}
            continue
        try:
            res = fn()
            SECTIONS[name] = {"status": "RAN", "start_elapsed_s": t, "end_elapsed_s": elapsed(),
                              "result": res}
        except Exception as e:  # recorded, never hidden
            exceptions.append(name)
            SECTIONS[name] = {"status": "EXCEPTION", "start_elapsed_s": t, "end_elapsed_s": elapsed(),
                              "error": repr(e), "traceback": traceback.format_exc()}
    failed = [e for e in EXPECTATIONS if not e["ok"]]
    skipped = [k for k, v in SECTIONS.items() if v["status"] == "SKIPPED_BUDGET_UNKNOWN"]
    code = 3 if exceptions else (2 if failed else (4 if skipped else 0))
    result = {
        "tool": "ReviewF175TuscanOrbit-control-v1.py",
        "python": sys.version,
        "platform": platform.platform(),
        "seed": SEED,
        "sections": SECTIONS,
        "expectations_total": len(EXPECTATIONS),
        "expectations_failed": len(failed),
        "failed_expectations": failed,
        "expectations": EXPECTATIONS,
        "exceptions": exceptions,
        "skipped_sections": skipped,
        "exit_code": code,
        "elapsed_s": elapsed(),
    }
    with open(out_path, "x", encoding="utf-8") as fh:
        json.dump(result, fh, indent=1, sort_keys=True)
        fh.write("\n")
    summary = {
        "exit_code": code,
        "elapsed_s": result["elapsed_s"],
        "expectations_total": len(EXPECTATIONS),
        "expectations_failed": len(failed),
        "sections": {k: v["status"] for k, v in SECTIONS.items()},
        "exceptions": exceptions,
        "skipped": skipped,
    }
    print(json.dumps(summary, sort_keys=True))
    return code


if __name__ == "__main__":
    sys.exit(main())
