#!/usr/bin/env python3
"""UNRUN F896 candidate. Parent full source read and a separate one-shot GO
are prerequisites; the author did not run, compile, test or hash this file.

Standard library only. No imports of prior research code, subprocesses,
network, files, randomization or floating point. Exact integer/bitmask work.
Cooperative monotonic internal limit 38 s (<= 40 s); the supervising parent
must impose an outer wall limit <= 55 s and keep stdout, stderr and exit code.
INCOMPLETE (deadline, signal or enumeration cap) is never PASS.

Object (original weighted fibres, F850/F868/F869/F870 reduction): modulo
m=2g, nonnegative integer multiplicities c_i, q_j with
    sum_i c_i q_(s-i) = L * 1_V(s),  L > 0,
V an antipodal selector, c_0 > 0, q_s > 0 for s in TAIL, and for each head
anchor a in {3,8,11} a positive c at residue a or a+g.  Every reported
contradiction uses only these necessary conditions; optional terms stay
nonnegative.  Finite projections are not anchored witnesses or a theorem.
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

TAIL = (0, 1, 7, 13, 14)
HEAD = (3, 8, 11)
TARGET_G = (18, 20, 21, 22, 24, 25, 26, 27, 28, 30)
REGRESSION_G = tuple(range(1, 17))
# Packet statements (S2 table/S6 section 3/S7/S8) used as regression
# expectations only: tail/anchor antipodes leave no selector, and the
# weighted rows close g = 8, 10, 11, 15, 16.
EXPECT_NO_SELECTOR = frozenset((1, 2, 3, 4, 5, 6, 7, 9, 12, 13, 14))
EXPECT_CLOSED = frozenset((8, 10, 11, 15, 16))
BRUTE_G = (15, 16, 18, 20)
ENUM_CAP_PER_G = 1 << 16
LIST_CAP = 64
FULL_ROWS_CAP = 8


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


def bits(mask):
    out = []
    x = mask
    while x:
        low = x & -x
        out.append(low.bit_length() - 1)
        x ^= low
    return out


def to_mask(elems, m):
    mask = 0
    for e in elems:
        mask |= 1 << (e % m)
    return mask


def rot(mask, k, m):
    """Image of the residue set under x -> x+k (mod m)."""
    k %= m
    if k == 0:
        return mask
    full = (1 << m) - 1
    return ((mask << k) & full) | (mask >> (m - k))


def tail_mask(m):
    return to_mask(TAIL, m)


def head_choices(g):
    m = 2 * g
    return [tuple(sorted({a % m, (a + g) % m})) for a in HEAD]


def selector_validate(g, vmask):
    m = 2 * g
    for r in range(g):
        forbid(((vmask >> r) & 1) + ((vmask >> (r + g)) & 1) != 1,
               "SELECTOR_ANTIPODAL")
    forbid(any(not (vmask >> (s % m)) & 1 for s in TAIL),
           "TAIL_ANCHOR_MISSING")


def superset(vmask, forced, m):
    """Exact intersection of V - f over f in forced (as a bitmask)."""
    out = (1 << m) - 1
    for f in bits(forced):
        out &= rot(vmask, -f, m)
    return out


def forced_validate(g, cf, cs):
    m = 2 * g
    forbid(not cf & 1, "C_ZERO_MISSING")
    for a in HEAD:
        forbid(not ((cf >> (a % m)) & 1) and not ((cf >> ((a + g) % m)) & 1),
               "HEAD_ANCHOR_%d_MISSING" % a)
    forbid(cf & ~cs, "FORCED_TRANSLATE_OUTSIDE_SELECTOR")


def incidence_rows(m, cs, qs):
    rows = [[] for _ in range(m)]
    for i in bits(cs):
        for j in bits(qs):
            rows[(i + j) % m].append((i, j))
    for s in range(m):
        rows[s].sort()
    return rows


def independent_rows(m, cs, qs):
    """Per-row filter over every residue i (O(m^2)); a different code path
    from incidence_rows, which distributes the product of the supersets."""
    return [[(i, (s - i) % m) for i in range(m)
             if (cs >> i) & 1 and (qs >> ((s - i) % m)) & 1]
            for s in range(m)]


def enumerate_cases(g, stats):
    """All (forced C mask, selector) with S and the anchor translates inside V.

    Every selector containing S and admitting anchor residues p with p+S in V
    contains F = union of the translates; V is F plus one element of each
    pair untouched by F. Keys are deduplicated.
    """
    m = 2 * g
    smask = tail_mask(m)
    seen = set()
    out = []
    if smask & rot(smask, g, m):
        stats["tail_antipodal"] = True
        return out
    stats["tail_antipodal"] = False
    for picked in itertools.product(*head_choices(g)):
        guard()
        cf = to_mask((0,) + picked, m)
        fmask = 0
        for a in bits(cf):
            fmask |= rot(smask, a, m)
        stats["anchor_picks"] += 1
        if fmask & rot(fmask, g, m):
            stats["picks_with_forced_antipodes"] += 1
            continue
        free = [r for r in range(g)
                if not (fmask >> r) & 1 and not (fmask >> (r + g)) & 1]
        count = 1 << len(free)
        if stats["selectors_enumerated"] + count > ENUM_CAP_PER_G:
            raise Incomplete("enumeration_cap_g%d" % g)
        stats["free_pairs_by_pick"].append(len(free))
        for b in range(count):
            if b % 256 == 0:
                guard()
            vmask = fmask
            for idx, r in enumerate(free):
                vmask |= 1 << (r + g * ((b >> idx) & 1))
            stats["selectors_enumerated"] += 1
            key = (cf, vmask)
            if key in seen:
                stats["duplicate_keys"] += 1
                continue
            seen.add(key)
            out.append(key)
    return out


def brute_keys(g):
    """Independent 2^g scan of every antipodal selector (cross-check)."""
    m = 2 * g
    found = set()
    low = (1 << g) - 1
    tm = tail_mask(m)
    all_choices = head_choices(g)
    for b in range(1 << g):
        if b % 1024 == 0:
            guard()
        vmask = (low ^ b) | (b << g)
        if (vmask & tm) != tm:
            continue
        cs0 = superset(vmask, tm, m)
        choices = [tuple(p for p in ch if (cs0 >> p) & 1)
                   for ch in all_choices]
        if any(not ch for ch in choices):
            continue
        for picked in itertools.product(*choices):
            found.add((to_mask((0,) + picked, m), vmask))
    return found


def analyse(g, vmask, cf, qf):
    """Propagate forced positives, build every row, search a strict cycle.

    Returns a dict with outcome CLOSED (reason) or RESIDUAL.  Edge u->v
    encodes v <= u for x_i = log c_i, z_j = log L - log q_j; an occupied row
    with exactly one admissible pair (i,j) gives c_i q_j = L (both ways);
    a forced-positive pair (i,j) in an occupied row gives c_i q_j <= L,
    strict when that row contains a second forced-positive pair.
    """
    m = 2 * g
    steps = []
    while True:
        guard()
        cs = superset(vmask, qf, m)
        qs = superset(vmask, cf, m)
        if cf & ~cs:
            return {"outcome": "CLOSED", "reason": "FORCED_C_OUTSIDE_SUPERSET",
                    "detail": bits(cf & ~cs), "cf": cf, "qf": qf,
                    "cs": cs, "qs": qs, "steps": steps}
        if qf & ~qs:
            return {"outcome": "CLOSED", "reason": "FORCED_Q_OUTSIDE_SUPERSET",
                    "detail": bits(qf & ~qs), "cf": cf, "qf": qf,
                    "cs": cs, "qs": qs, "steps": steps}
        rows = incidence_rows(m, cs, qs)
        ncf, nqf = cf, qf
        for s in bits(vmask):
            if not rows[s]:
                return {"outcome": "CLOSED", "reason": "EMPTY_OCCUPIED_ROW",
                        "detail": [s], "cf": cf, "qf": qf, "cs": cs,
                        "qs": qs, "steps": steps}
            if len(rows[s]) == 1:
                i, j = rows[s][0]
                ncf |= 1 << i
                nqf |= 1 << j
        if (ncf, nqf) == (cf, qf):
            break
        steps.append({"new_forced_C": bits(ncf & ~cf),
                      "new_forced_Q": bits(nqf & ~qf)})
        cf, qf = ncf, nqf
    result = cycle_search(g, vmask, cf, qf, rows)
    result["steps"] = steps
    if result["cycle"] is not None:
        result.update({"outcome": "CLOSED",
                       "reason": "STRICT_POSITIVE_CYCLE_AFTER_PROPAGATION"})
    else:
        result.update({"outcome": "RESIDUAL"})
    return result


def cycle_search(g, vmask, cf, qf, rows=None):
    """Rows, edges and a strict cycle for the given forced-positive masks.

    Edge u->v encodes v <= u.  A singleton occupied row (i,j) is an exact
    equality c_i q_j = L (so both factors are positive even if not yet in
    the masks); a forced-positive pair in a longer occupied row gives
    c_i q_j <= L, strict when a second forced-positive pair is present.
    """
    m = 2 * g
    cs = superset(vmask, qf, m)
    qs = superset(vmask, cf, m)
    if rows is None:
        rows = incidence_rows(m, cs, qs)
    edges = []
    for s in bits(vmask):
        row = rows[s]
        fp = [(i, j) for (i, j) in row if (cf >> i) & 1 and (qf >> j) & 1]
        if len(row) == 1:
            i, j = row[0]
            edges.append((("q", j), ("c", i), False, s))
            edges.append((("c", i), ("q", j), False, s))
        else:
            for (i, j) in fp:
                edges.append((("q", j), ("c", i), len(fp) >= 2, s))
    return {"cf": cf, "qf": qf, "cs": cs, "qs": qs, "rows": rows,
            "edges": edges, "cycle": find_strict_cycle(edges)}


def find_strict_cycle(edges):
    adj = {}
    for e in edges:
        adj.setdefault(e[0], []).append(e)
    for start in sorted(adj):
        adj[start].sort()
    for e in sorted(edges):
        if not e[2]:
            continue
        u, v = e[0], e[1]
        parent = {v: None}
        queue = [v]
        head = 0
        while head < len(queue):
            node = queue[head]
            head += 1
            if node == u:
                break
            for nxt in adj.get(node, []):
                if nxt[1] not in parent:
                    parent[nxt[1]] = nxt
                    queue.append(nxt[1])
        if u in parent:
            path = []
            node = u
            while parent[node] is not None:
                path.append(parent[node])
                node = parent[node][0]
            path.reverse()
            return [e] + path
    return None


def validate_cycle(g, vmask, cf, qf, cs, qs, cycle):
    """Independent re-derivation of every edge from the full square filter."""
    m = 2 * g
    need(cs == superset(vmask, qf, m) and qs == superset(vmask, cf, m),
         "certificate supersets differ from recomputation")
    cs2 = to_mask([i for i in range(m)
                   if all((vmask >> ((i + s) % m)) & 1 for s in bits(qf))], m)
    qs2 = to_mask([j for j in range(m)
                   if all((vmask >> ((j + i) % m)) & 1 for i in bits(cf))], m)
    need(cs2 == cs and qs2 == qs, "independent superset filter mismatch")
    rows = independent_rows(m, cs, qs)
    forbid(not cycle, "CYCLE_EMPTY")
    forbid(not any(e[2] for e in cycle), "NO_STRICT_EDGE")
    for k, (u, v, strict, s) in enumerate(cycle):
        nxt = cycle[(k + 1) % len(cycle)]
        forbid(v != nxt[0], "CYCLE_NOT_CLOSED")
        forbid(not (vmask >> s) & 1, "ROW_UNOCCUPIED")
        if u[0] == "c":
            forbid(v[0] != "q", "EDGE_TYPE")
            pair = (u[1], v[1])
            forbid(rows[s] != [pair], "SINGLETON_INCIDENCE")
            forbid(strict, "EQUALITY_MARKED_STRICT")
        else:
            forbid(v[0] != "c", "EDGE_TYPE")
            pair = (v[1], u[1])
            forbid(pair not in rows[s], "INCIDENCE")
            if rows[s] != [pair]:
                # Non-singleton row: the <= edge needs both factors forced.
                forbid(not ((cf >> pair[0]) & 1 and (qf >> pair[1]) & 1),
                       "PAIR_NOT_FORCED")
            if strict:
                forbid(rows[s] == [pair], "SINGLETON_MARKED_STRICT")
                others = [p for p in rows[s] if p != pair
                          and (cf >> p[0]) & 1 and (qf >> p[1]) & 1]
                forbid(not others, "STRICT_REMAINDER_NOT_FORCED")
    return True


def validate_forced_derivation(g, vmask, picked_cf, result):
    """Replay: every forced element is initial or from a singleton row."""
    m = 2 * g
    cf, qf = picked_cf, tail_mask(m)
    for step in result["steps"]:
        cs = superset(vmask, qf, m)
        qs = superset(vmask, cf, m)
        rows = independent_rows(m, cs, qs)
        singles = [rows[s][0] for s in bits(vmask) if len(rows[s]) == 1]
        for i in step["new_forced_C"]:
            need(any(p[0] == i for p in singles), "forced C not from singleton")
            cf |= 1 << i
        for j in step["new_forced_Q"]:
            need(any(p[1] == j for p in singles), "forced Q not from singleton")
            qf |= 1 << j
    need((cf, qf) == (result["cf"], result["qf"]), "forced replay mismatch")


def row_equations(g, vmask, res):
    m = 2 * g
    cf, qf, rows = res["cf"], res["qf"], res["rows"]
    out = []
    for s in range(m):
        out.append({"residue": s, "rhs": "L" if (vmask >> s) & 1 else "0",
                    "terms": [[i, j, "F" if ((cf >> i) & 1 and (qf >> j) & 1)
                               else "O"] for (i, j) in rows[s]]})
    return out


def validate_row_equations(g, vmask, res, eqs):
    m = 2 * g
    rows = independent_rows(m, res["cs"], res["qs"])
    forbid(len(eqs) != m, "ROW_COUNT")
    for s in range(m):
        forbid([tuple(t[:2]) for t in eqs[s]["terms"]] != rows[s],
               "ROW_TERMS_INCOMPLETE")
        forbid(eqs[s]["rhs"] != ("L" if (vmask >> s) & 1 else "0"), "ROW_RHS")


def expect_violation(label, reason, call):
    try:
        call()
    except Violation as exc:
        need(str(exc) == reason, "%s: wrong reason %s" % (label, exc))
        return {"mutant": label, "rejected_as": reason}
    raise CheckFailure("%s: mutant unexpectedly accepted" % label)


def run_mutants(g, cf0, vmask, res):
    """Intended-reason mutants on one closed STRICT_POSITIVE_CYCLE case."""
    m = 2 * g
    out = []
    out.append(expect_violation("add_antipode_of_zero", "SELECTOR_ANTIPODAL",
                                lambda: selector_validate(g, vmask | (1 << g))))
    out.append(expect_violation(
        "swap_away_tail_zero", "TAIL_ANCHOR_MISSING",
        lambda: selector_validate(g, (vmask & ~1) | (1 << g))))
    # Remove every residue that could represent anchor 3 (both a and a+g;
    # they may coincide with another anchor's choices), never residue 0.
    three_mask = to_mask(head_choices(g)[0], m) & ~1
    need(cf0 & three_mask, "mutant: anchor-3 residue absent")
    out.append(expect_violation(
        "remove_anchor_three_residues", "HEAD_ANCHOR_3_MISSING",
        lambda: forced_validate(g, cf0 & ~three_mask,
                                superset(vmask, tail_mask(m), m))))
    cf, qf, cs, qs, cyc = res["cf"], res["qf"], res["cs"], res["qs"], res["cycle"]
    out.append(expect_violation(
        "drop_closing_edge", "CYCLE_NOT_CLOSED",
        lambda: validate_cycle(g, vmask, cf, qf, cs, qs, cyc[:-1])))
    out.append(expect_violation(
        "mark_every_edge_nonstrict", "NO_STRICT_EDGE",
        lambda: validate_cycle(g, vmask, cf, qf, cs, qs,
                               [(u, v, False, s) for (u, v, _x, s) in cyc])))
    strict_edge = cyc[0]
    s0 = strict_edge[3]
    i0 = strict_edge[1][1]
    rows = independent_rows(m, cs, qs)
    others = [p[0] for p in rows[s0] if p[0] != i0]
    out.append(expect_violation(
        "unforce_strict_remainder", "STRICT_REMAINDER_NOT_FORCED",
        lambda: validate_cycle_relaxed(g, vmask, cf, qf, cs, qs, cyc, others)))
    eq_edges = [e for e in cyc if e[0][0] == "c"]
    applied = False
    for (u, v, _x, s) in eq_edges:
        for j in bits(qs):
            i_new = (s - j) % m
            if j != v[1] and not (cs >> i_new) & 1:
                out.append(expect_violation(
                    "extra_singleton_incident_pair", "SINGLETON_INCIDENCE",
                    lambda: validate_cycle_rows(g, vmask, cf, qf,
                                                cs | (1 << i_new), qs, cyc)))
                applied = True
                break
        if applied:
            break
    if not applied:
        out.append({"mutant": "extra_singleton_incident_pair",
                    "rejected_as": "NOT_APPLICABLE_NO_FREE_RESIDUE"})
    eqs = row_equations(g, vmask, res)
    victim = next(s for s in range(m) if len(eqs[s]["terms"]) >= 2)
    dropped = [dict(e) for e in eqs]
    dropped[victim] = {"residue": victim, "rhs": eqs[victim]["rhs"],
                       "terms": eqs[victim]["terms"][1:]}
    out.append(expect_violation(
        "drop_optional_or_forced_term", "ROW_TERMS_INCOMPLETE",
        lambda: validate_row_equations(g, vmask, res, dropped)))
    return out


def validate_cycle_relaxed(g, vmask, cf, qf, cs, qs, cyc, unforce):
    mask = cf
    for i in unforce:
        mask &= ~(1 << i)
    return validate_cycle_rows(g, vmask, mask, qf, cs, qs, cyc)


def validate_cycle_rows(g, vmask, cf, qf, cs, qs, cycle):
    """validate_cycle without the superset recomputation (mutant harness)."""
    m = 2 * g
    rows = independent_rows(m, cs, qs)
    forbid(not any(e[2] for e in cycle), "NO_STRICT_EDGE")
    for k, (u, v, strict, s) in enumerate(cycle):
        forbid(v != cycle[(k + 1) % len(cycle)][0], "CYCLE_NOT_CLOSED")
        if u[0] == "c":
            forbid(rows[s] != [(u[1], v[1])], "SINGLETON_INCIDENCE")
        else:
            pair = (v[1], u[1])
            forbid(pair not in rows[s], "INCIDENCE")
            if strict:
                others = [p for p in rows[s] if p != pair
                          and (cf >> p[0]) & 1 and (qf >> p[1]) & 1]
                forbid(not others, "STRICT_REMAINDER_NOT_FORCED")
    return True


def describe_case(g, cf0, vmask, res, full_rows):
    m = 2 * g
    entry = {"selector": bits(vmask), "anchor_forced_C": bits(cf0),
             "outcome": res["outcome"], "reason": res.get("reason"),
             "final_forced_C": bits(res["cf"]), "final_forced_Q": bits(res["qf"]),
             "C_superset": bits(res["cs"]), "Q_superset": bits(res["qs"]),
             "propagation_steps": res["steps"]}
    if "detail" in res:
        entry["detail"] = res["detail"]
    if res.get("cycle"):
        rows = res.get("rows")
        entry["strict_cycle"] = [
            {"from": list(u), "to": list(v), "strict": strict, "row": s,
             "pair": [u[1], v[1]] if u[0] == "c" else [v[1], u[1]],
             "kind": "EQUALITY_SINGLETON_GE" if u[0] == "c" else
             ("STRICT_LT_L" if strict else
              ("EQUALITY_SINGLETON_LE" if rows is not None and len(rows[s]) == 1
               else "LE_L"))}
            for (u, v, strict, s) in res["cycle"]]
    if full_rows and "rows" in res:
        entry["row_equations"] = row_equations(g, vmask, res)
    return entry


def do_g(g, section):
    stats = {"anchor_picks": 0, "picks_with_forced_antipodes": 0,
             "selectors_enumerated": 0, "duplicate_keys": 0,
             "free_pairs_by_pick": []}
    out = {"g": g, "modulus": 2 * g, "status": "RUNNING", "stats": stats}
    section["by_g"][str(g)] = out
    keys = enumerate_cases(g, stats)
    stats["cases"] = len(keys)
    reasons = {}
    listed_closed, listed_residual, mutants = [], [], None
    residual_count = 0
    m = 2 * g
    tmask = tail_mask(m)
    for (cf0, vmask) in keys:
        guard()
        selector_validate(g, vmask)
        forced_validate(g, cf0, superset(vmask, tmask, m))
        # f870-style first: only the anchor-forced C set and the tail.
        res = cycle_search(g, vmask, cf0, tmask)
        if res["cycle"] is not None:
            res.update({"outcome": "CLOSED", "steps": [],
                        "reason": "STRICT_POSITIVE_CYCLE_INITIAL_FORCED"})
        else:
            res = analyse(g, vmask, cf0, tmask)
            validate_forced_derivation(g, vmask, cf0, res)
        if res["outcome"] == "CLOSED":
            reasons[res["reason"]] = reasons.get(res["reason"], 0) + 1
            if res.get("cycle") is not None:
                validate_cycle(g, vmask, res["cf"], res["qf"], res["cs"],
                               res["qs"], res["cycle"])
                if mutants is None:
                    mutants = run_mutants(g, cf0, vmask, res)
            if len(listed_closed) < LIST_CAP:
                listed_closed.append(describe_case(
                    g, cf0, vmask, res, len(listed_closed) < FULL_ROWS_CAP))
        else:
            residual_count += 1
            eqs = row_equations(g, vmask, res)
            validate_row_equations(g, vmask, res, eqs)
            if len(listed_residual) < LIST_CAP:
                listed_residual.append(describe_case(g, cf0, vmask, res, True))
    out["closure_reasons"] = reasons
    out["residual_cases"] = residual_count
    out["closed_cases_listed"] = listed_closed
    out["residual_cases_listed"] = listed_residual
    out["listing_truncated"] = (len(keys) - residual_count > LIST_CAP or
                                residual_count > LIST_CAP)
    out["mutants"] = mutants
    if not keys:
        out["classification"] = "NO_SELECTOR_SURVIVES"
    elif residual_count:
        out["classification"] = "RESIDUAL_EQUATIONS_REMAIN"
    elif all(r.startswith("STRICT_POSITIVE_CYCLE") for r in reasons):
        out["classification"] = "ALL_CASES_STRICT_POSITIVE_CYCLE"
    else:
        out["classification"] = "ALL_CASES_CLOSED_MIXED_EXACT_REASONS"
    out["status"] = "COMPLETE"
    return out


def do_brute(section):
    section["status"] = "RUNNING"
    for g in BRUTE_G:
        stats = {"anchor_picks": 0, "picks_with_forced_antipodes": 0,
                 "selectors_enumerated": 0, "duplicate_keys": 0,
                 "free_pairs_by_pick": []}
        fast = set(enumerate_cases(g, stats))
        slow = brute_keys(g)
        need(fast == slow, "forced-first enumeration differs from 2^g scan g%d" % g)
        section["by_g"][str(g)] = {"scanned_selectors": 1 << g,
                                   "cases": len(slow)}
    section["status"] = "COMPLETE"


def check_fixture(n, d, c, q):
    guard()
    need(n > 14 and 0 in c and 0 in q and d % n, "fixture parameters")
    p_terms = [(x + e * d) % n for x in c for e in (0, 1)]
    need(len(set(p_terms)) == len(p_terms), "fixture C factor not direct")
    counts = [0] * n
    for x in p_terms:
        for y in q:
            counts[(x + y) % n] += 1
    need(counts == [1] * n, "fixture not an actual direct tiling")
    t = [0] * n
    for x in c:
        for y in q:
            t[(x + y) % n] += 1
    g = math.gcd(d, n)
    need(n % (2 * g) == 0, "fixture cycle not even")
    m, length = 2 * g, n // (2 * g)
    vmask = to_mask([x for x in range(n) if t[x] == 1], m)
    for x in range(n):
        need(t[x] == (vmask >> (x % m)) & 1, "fixture fibre not full")
        need(t[x] + t[(x - d) % n] == 1, "fixture alternation")
    selector_validate_plain(g, vmask)
    cc = [sum(1 for x in c if x % m == i) for i in range(m)]
    qq = [sum(1 for y in q if y % m == j) for j in range(m)]
    for s in range(m):
        need(sum(cc[i] * qq[(s - i) % m] for i in range(m)) ==
             length * ((vmask >> s) & 1), "fixture weighted coefficient")
    cf = to_mask([i for i in range(m) if cc[i]], m)
    qf = to_mask([j for j in range(m) if qq[j]], m)
    res = analyse(g, vmask, cf, qf)
    need(res["outcome"] == "RESIDUAL",
         "SOUNDNESS: engine closed an actual tiling's own supports")
    p = set(p_terms)
    missing_head = sorted({0, 3, 8, 11} - p)
    missing_tail = sorted(set(TAIL) - set(q))
    need(missing_head or missing_tail, "fixture accidentally anchored target")
    eqs = row_equations(g, vmask, res)
    validate_row_equations(g, vmask, res, eqs)
    return {"n": n, "d": d, "g": g, "L": length, "C": sorted(c),
            "Q_size": len(q), "selector": bits(vmask),
            "engine_outcome_on_actual_supports": res["outcome"],
            "missing_original_head_anchors": missing_head,
            "missing_original_tail_anchors": missing_tail,
            "classification": "ACTUAL_DIRECT_TILING_NON_TARGET"}


def selector_validate_plain(g, vmask):
    for r in range(g):
        need(((vmask >> r) & 1) + ((vmask >> (r + g)) & 1) == 1,
             "fixture selector property")


def do_fixtures(section):
    section["status"] = "RUNNING"
    for g in REGRESSION_G[-2:] + TARGET_G:
        section["fixtures"].append(
            check_fixture(4 * g, g, [0, 2 * g], list(range(g))))
    section["fixtures"].append(
        check_fixture(32, 3, [0, 8], [0, 2, 4, 6, 16, 18, 20, 22]))
    section["status"] = "COMPLETE"


def do_regression(section):
    section["status"] = "RUNNING"
    for g in REGRESSION_G:
        out = do_g(g, section)
        cls = out["classification"]
        if g in EXPECT_NO_SELECTOR:
            need(cls == "NO_SELECTOR_SURVIVES", "regression g%d: %s" % (g, cls))
        elif g in EXPECT_CLOSED:
            need(cls.startswith("ALL_CASES"), "regression g%d: %s" % (g, cls))
    section["status"] = "COMPLETE"


# Literal F870 (S8 table / S9 EXPECTED_CASES) selectors, forced C residues
# and initial supersets; the g15 h=5 cycle is S8's displayed two-cycle.
S8_CASES = (
    (15, (0, 1, 2, 5, 6, 7, 11, 12, 13, 14, 18, 19, 23, 24, 25),
     (0, 11, 18, 23), (0, 5, 11, 18, 23), (0, 1, 7, 12, 13, 14, 19, 25)),
    (15, (0, 1, 2, 6, 7, 11, 12, 13, 14, 18, 19, 20, 23, 24, 25),
     (0, 11, 18, 23), (0, 6, 11, 18, 23), (0, 1, 2, 7, 13, 14, 19, 25)),
    (16, (0, 1, 2, 7, 8, 9, 13, 14, 15, 19, 20, 21, 22, 26, 27, 28),
     (0, 8, 19, 27), (0, 1, 7, 8, 13, 14, 19, 20, 26, 27),
     (0, 1, 7, 13, 14, 20, 26)),
    (16, (0, 1, 5, 6, 7, 11, 12, 13, 14, 18, 19, 20, 24, 25, 26, 31),
     (0, 11, 19, 24), (0, 5, 6, 11, 12, 18, 19, 24, 25, 31),
     (0, 1, 7, 13, 14, 20, 26)),
)
S8_G15_H5_CYCLE = [
    (("q", 0), ("c", 0), True, 0),      # c0 q0 < L (row 0 also has c23 q7)
    (("c", 0), ("q", 14), False, 14),   # L = c0 q14 (singleton row 14)
    (("q", 14), ("c", 11), True, 25),   # c11 q14 < L (row 25 also c18 q7)
    (("c", 11), ("q", 0), False, 11),   # L = c11 q0 (singleton row 11)
]


def do_literal_s8(section):
    section["status"] = "RUNNING"
    for g in (15, 16):
        m = 2 * g
        stats = {"anchor_picks": 0, "picks_with_forced_antipodes": 0,
                 "selectors_enumerated": 0, "duplicate_keys": 0,
                 "free_pairs_by_pick": []}
        got = set(enumerate_cases(g, stats))
        want = {(to_mask(f, m), to_mask(v, m))
                for (gg, v, f, _c, _q) in S8_CASES if gg == g}
        need(got == want, "literal S8 selector/anchor universe g%d" % g)
    for (g, v, f, c_sup, q_sup) in S8_CASES:
        m = 2 * g
        vmask, cf = to_mask(v, m), to_mask(f, m)
        need(superset(vmask, tail_mask(m), m) == to_mask(c_sup, m),
             "literal S8 C superset g%d" % g)
        need(superset(vmask, cf, m) == to_mask(q_sup, m),
             "literal S8 Q superset g%d" % g)
    g, v, f = S8_CASES[0][0], S8_CASES[0][1], S8_CASES[0][2]
    m = 2 * g
    vmask, cf = to_mask(v, m), to_mask(f, m)
    res = cycle_search(g, vmask, cf, tail_mask(m))
    need(res["cycle"] is not None, "engine found no cycle on literal S8 case")
    validate_cycle(g, vmask, cf, tail_mask(m), res["cs"], res["qs"],
                   S8_G15_H5_CYCLE)
    literal = dict(res)
    literal["cycle"] = S8_G15_H5_CYCLE
    section["literal_g15_h5_cycle_valid"] = True
    section["mutants_on_literal_certificate"] = run_mutants(g, cf, vmask, literal)
    section["status"] = "COMPLETE"


def do_targets(section):
    section["status"] = "RUNNING"
    for g in TARGET_G:
        do_g(g, section)
    section["status"] = "COMPLETE"


def main():
    result = {
        "status": "INCOMPLETE",
        "scope": "exact local selector/weighted-incidence projections for an "
                 "assumed actual two-point head factor; no anchored witness, "
                 "no tiling solver, no global theorem",
        "internal_limit_seconds": 38,
        "required_parent_outer_limit_seconds_at_most": 55,
        "sections": {
            "literal_f870_s8_cases": {"status": "NOT_STARTED"},
            "regression_g1_to_16": {"status": "NOT_STARTED", "by_g": {}},
            "brute_force_enumeration_cross_check": {"status": "NOT_STARTED",
                                                    "by_g": {}},
            "actual_non_target_fixtures": {"status": "NOT_STARTED",
                                           "fixtures": []},
            "targets_composite_g": {"status": "NOT_STARTED", "by_g": {}},
        },
    }
    exit_code = 2
    try:
        signal.signal(signal.SIGINT, signal_latch)
        signal.signal(signal.SIGTERM, signal_latch)
        guard()
        sec = result["sections"]
        do_literal_s8(sec["literal_f870_s8_cases"])
        do_regression(sec["regression_g1_to_16"])
        do_brute(sec["brute_force_enumeration_cross_check"])
        do_fixtures(sec["actual_non_target_fixtures"])
        do_targets(sec["targets_composite_g"])
        guard()
        result["status"] = "COMPLETE"
        result["per_target_classification"] = {
            str(g): sec["targets_composite_g"]["by_g"][str(g)]["classification"]
            for g in TARGET_G}
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
            for entry in section.get("by_g", {}).values():
                if entry.get("status") == "RUNNING":
                    entry["status"] = "INCOMPLETE"
        result["elapsed_monotonic_seconds"] = round(time.monotonic() - START, 6)
        json.dump(result, sys.stdout, sort_keys=True, separators=(",", ":"))
        sys.stdout.write("\n")
        sys.stdout.flush()
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
