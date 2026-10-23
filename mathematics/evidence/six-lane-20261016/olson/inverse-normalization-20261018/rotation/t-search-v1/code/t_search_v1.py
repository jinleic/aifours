#!/usr/bin/env python3
"""Finite aid (not a proof) for the residual of the ZX route: search for the structure (R1) of notes-ZX-residual-v1.md
(fdb5ad4a...ee98).  Plan: t-search-v1/PLAN-v1.md; expected outcomes: t-search-v1/EXPECTED-v1.json (frozen first).

(R1): if (ZP) holds at kappa (no zero-sum of length in [2kappa+2, 2p]), 3kappa <= 2p - 2, and (S1) fails, then a
shortest zero-sum T with |T| >= 2kappa + 2 is a zero-sum of even length N in [2p + 2, 4kappa] all of whose nonempty
proper zero-sub-sums have length in [N - 2kappa, 2kappa].  This script enumerates, up to multiplication by units of
Z_(2p), every multiset T of N odd residues mod 2p with
  (T0) sum(T) = 0, and
  (T1) no zero-sum sub-multiset of even length l with 2 <= l <= N - 2 and l not in [N - 2kappa, 2kappa],
for every even N in [2p + 2, 4kappa].  If none exists for (p, kappa), then (ZP) implies (S1) at (p, kappa) for every
sequence (by (R1)).  For each T found, it records the multiset, its zero-sub-sum lengths, and whether T extends to a
(ZP) sequence Y = T W of length R = 2p + 2kappa - k for some k with kappa + 1 <= k and 3k <= 2p + 1 (exhaustive over
W), and, for any such Y, min over odd generators of cost (the Lemma ZS conclusion is cost <= k - 1).
Enumeration: the multiplicity-vector DFS of zs-check-v1/code/zs_check_v1.py (d9d0e073...6818) with the forbidden
length set replaced by (T1) and the target size N; passes "1-max" (residue 1 has a largest multiplicity, ties
allowed) and "(1,0)-max" ((1,0) strictly largest).  Self-imposed budget BUDGET_S (wall clock); heartbeat every
HEARTBEAT_S; no other bound.
Usage: t_search_v1.py OUT.jsonl
"""
import json, sys, time, itertools

BUDGET_S = 5400.0
EXT_CAP = 200000
HEARTBEAT_S = 300.0
T_START = time.monotonic()
_last = [T_START]
_emit = [None]


class Stop(Exception):
    pass


def tick(tag, nodes):
    now = time.monotonic()
    if now - T_START > BUDGET_S:
        raise Stop()
    if now - _last[0] >= HEARTBEAT_S:
        _last[0] = now
        _emit[0](dict(kind="HEARTBEAT", item=tag, nodes=nodes, elapsed=round(now - T_START, 1),
                      clock=time.strftime("%H:%M:%S")))


# (p, kappa, role): CONTROL_POS = must find T (parent's g^13 (5g)^3 at p = 7); CONTROL_NEG = S1(c) range, must find none
ITEMS = [(7, 5, "CONTROL_POS"), (13, 7, "CONTROL_NEG"), (17, 9, "CONTROL_NEG"),
         (13, 8, "RESIDUAL"), (17, 10, "RESIDUAL"), (19, 11, "RESIDUAL"), (19, 12, "RESIDUAL"),
         (23, 13, "RESIDUAL"), (23, 14, "RESIDUAL")]


def rotl(mask, y, n, full):
    y %= n
    return ((mask << y) | (mask >> (n - y))) & full if y else mask


def enumerate_T(p, kappa, N, special, tag):
    n = 2 * p; full = (1 << n) - 1
    forbid = [l for l in range(2, N - 1, 2) if l < N - 2 * kappa or l > 2 * kappa]
    odd = [2 * t + 1 for t in range(p)]
    zt = (p - 1) // 2
    first = zt if special else 0
    order = [first] + [t for t in range(p) if t != first]
    mult = [0] * p
    out = []
    nodes = [0]

    def add(reach, y):
        nxt = reach[:]
        for l in range(N, 0, -1):
            nxt[l] |= rotl(reach[l - 1], y, n, full)
        for l in forbid:
            if nxt[l] & 1:
                return None
        return nxt

    def dfs(pos, reach, size, cap):
        nodes[0] += 1
        if nodes[0] & 4095 == 0:
            tick(tag, nodes[0])
        if size == N:
            if reach[N] & 1:
                out.append(tuple(mult))
            return
        if pos == p or size + (p - pos) * cap < N:
            return
        t = order[pos]
        dfs(pos + 1, reach, size, cap)
        cur = reach; j = 0
        lim = cap if not special else cap - 1
        while j < lim and size + j < N:
            cur = add(cur, odd[t])
            if cur is None:
                break
            j += 1; mult[t] = j
            dfs(pos + 1, cur, size + j, cap)
        mult[t] = 0

    reach0 = [0] * (N + 1); reach0[0] = 1
    cur = reach0; j = 0; t0 = order[0]; seq = []
    while j < N:
        cur = add(cur, odd[t0])
        if cur is None:
            break
        j += 1; seq.append((j, cur))
    for j, reach in seq:
        mult[t0] = j
        dfs(1, reach, j, j)
    mult[t0] = 0
    return out, nodes[0]


def states(counts, vals, n):
    st = {(0, 0)}
    for c, v in zip(counts, vals):
        if c:
            st = {(l + j, (s + j * v) % n) for (l, s) in st for j in range(c + 1)}
    return st


def sym(x, p):
    x %= 2 * p
    return x if x <= p else x - 2 * p


def min_cost(counts, vals, n, p):
    best = None
    for h in vals:
        if h == p:
            continue
        hinv = pow(h, -1, n); tot = 0
        for c, v in zip(counts, vals):
            if c:
                b = sym(v * hinv, p)
                tot += c * ((b - 1) if b > 0 else -b)
        best = tot if best is None or tot < best else best
    return best


def extensions(T, p, kappa, vals, n):
    """For each k (kappa+1 <= k, 3k <= 2p+1): is there W with |W| = R - N and T W satisfying (ZP)?"""
    res = []
    N = sum(T)
    for k in range(kappa + 1, (2 * p + 1) // 3 + 1):
        R = 2 * p + 2 * kappa - k
        w = R - N
        if w < 0:
            res.append(dict(k=k, R=R, w=w, extends=False, reason="R < N")); continue
        ncomb = 1
        for i in range(w):
            ncomb = ncomb * (p + i) // (i + 1)
        if ncomb > EXT_CAP:
            res.append(dict(k=k, R=R, w=w, extends=None, reason="EXT_UNCHECKED: %d completions > cap" % ncomb))
            continue
        found = []
        for comb in itertools.combinations_with_replacement(range(p), w):
            Y = list(T)
            for t in comb:
                Y[t] += 1
            st = states(Y, vals, n)
            if not any(s == 0 and 2 * kappa + 2 <= l <= n for (l, s) in st):
                found.append(Y)
                if len(found) >= 3:
                    break
        res.append(dict(k=k, R=R, w=w, extends=bool(found),
                        examples=[dict(mult={vals[i]: c for i, c in enumerate(Y) if c},
                                       min_cost=min_cost(Y, vals, n, p)) for Y in found]))
    return res


def run_item(p, kappa, role):
    n = 2 * p; vals = [2 * t + 1 for t in range(p)]
    rec = dict(kind="ITEM", p=p, kappa=kappa, role=role, Ns=[], found_total=0, examples=[])
    target = tuple(13 if i == 0 else (3 if i == 2 else 0) for i in range(p))   # g^13 (5g)^3 (p = 7 control)
    hit = False
    t0 = time.monotonic()
    for N in range(2 * p + 2, 4 * kappa + 1, 2):
        for special in (False, True):
            tag = "%d,%d,N=%d,%s" % (p, kappa, N, "(1,0)" if special else "1")
            found, nodes = enumerate_T(p, kappa, N, special, tag)
            rec["Ns"].append(dict(N=N, pass_="(1,0)-max" if special else "1-max", found=len(found), nodes=nodes))
            rec["found_total"] += len(found)
            if role == "CONTROL_POS" and target in found:
                hit = True
            for T in found:
                if len(rec["examples"]) >= 6:
                    break
                T = list(T)
                st = states(T, vals, n)
                zl = sorted({l for (l, s) in st if s == 0})
                ex = dict(N=N, mult={vals[i]: c for i, c in enumerate(T) if c}, zero_sum_lengths=zl)
                if role == "RESIDUAL":
                    ex["extensions"] = extensions(T, p, kappa, vals, n)
                rec["examples"].append(ex)
    rec["sec"] = round(time.monotonic() - t0, 1)
    if role == "CONTROL_POS":
        rec["control_target_found"] = hit
    return rec


def main():
    with open(sys.argv[1], "x") as out:
        def emit(r):
            out.write(json.dumps(r, sort_keys=True) + "\n"); out.flush()
            print(json.dumps(r, sort_keys=True), flush=True)
        _emit[0] = emit
        emit(dict(kind="START", clock=time.strftime("%Y-%m-%dT%H:%M:%S%z"), budget_s=BUDGET_S, items=ITEMS))
        stopped = False
        for (p, kappa, role) in ITEMS:
            if stopped:
                emit(dict(kind="ITEM_UNKNOWN", p=p, kappa=kappa, role=role, reason="budget")); continue
            try:
                emit(run_item(p, kappa, role))
            except Stop:
                stopped = True
                emit(dict(kind="ITEM_UNKNOWN", p=p, kappa=kappa, role=role, reason="budget reached during item"))
        emit(dict(kind="DONE" if not stopped else "DONE_PARTIAL", clock=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                  elapsed=round(time.monotonic() - T_START, 1)))


if __name__ == "__main__":
    main()
