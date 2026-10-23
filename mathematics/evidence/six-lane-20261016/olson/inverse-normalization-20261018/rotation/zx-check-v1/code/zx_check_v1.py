#!/usr/bin/env python3
"""Finite control (an aid, not a proof) for Lemma ZX and Lemma S1 of proof-ROT-ZX-v1.md (ad2460b2...815b).
Plan: zx-check-v1/PLAN-v1.md; expected outcomes: zx-check-v1/EXPECTED-v1.json (both frozen before any run).

Sequences only (multisets of odd residues mod 2p); no words are enumerated.  For each item (p, k, kappa), every
multiset Y of R = 2p + 2kappa - k odd residues with (ZP) "no zero-sum of size in [2kappa + 2, 2p]" is enumerated up to
units by the enumerator of zs-check-v1/code/zs_check_v1.py (d9d0e073...6818), copied below with two additions only: a
heartbeat line every HEARTBEAT_S seconds and a self-imposed global deadline (BUDGET_S), after which the current and all
later items are reported UNKNOWN.  Per multiset:
  ZP2  (ZP) re-checked from the (size, sum) state set;
  CONC min over odd generators of cost <= k - 1;
  S1   the longest zero-sum has length <= 2 kappa (else: record it, check 2 kappa >= p + 1, search for the P, P' pair
       of Lemma S1 (b) when the sub-multiset count is <= PP_CAP);
  ZX   if S1 holds, Steps A-G of Lemma ZX for Z = a longest zero-sum and g = the most frequent value of Y - Z.
Usage: zx_check_v1.py OUT.jsonl
"""
import json, sys, time, itertools

BUDGET_S = 9000.0
HEARTBEAT_S = 300.0
PP_CAP = 2000000
T_START = time.monotonic()
_last_beat = [T_START]
_emit = [None]


class Stop(Exception):
    pass


def tick(tag, nodes):
    now = time.monotonic()
    if now - T_START > BUDGET_S:
        raise Stop()
    if now - _last_beat[0] >= HEARTBEAT_S:
        _last_beat[0] = now
        _emit[0](dict(kind="HEARTBEAT", item=tag, nodes=nodes, elapsed=round(now - T_START, 1),
                      clock=time.strftime("%H:%M:%S")))


ITEMS = []
for (p, k) in ((5, 1), (5, 2), (5, 3), (7, 2), (7, 3), (7, 4), (7, 5), (11, 6), (11, 7), (13, 7), (13, 8), (13, 9)):
    for kap in range(0, k):
        ITEMS.append((p, k, kap))
P17 = [(17, k, kap) for k in (10, 11) for kap in range(0, k)]
P17.sort(key=lambda t: (2 * t[0] + 2 * t[2] - t[1], t[1]))
ITEMS += P17
RUN1_FOUND = {(7, 5, 0): 4, (7, 5, 1): 4, (7, 5, 2): 5, (7, 5, 3): 3, (7, 5, 4): 1,
              (11, 7, 0): 7, (11, 7, 1): 8, (11, 7, 2): 10, (11, 7, 3): 10, (11, 7, 4): 8, (11, 7, 5): 3,
              (11, 7, 6): 1,
              (13, 8, 0): 7, (13, 8, 1): 11, (13, 8, 2): 14, (13, 8, 3): 15, (13, 8, 4): 14, (13, 8, 5): 8,
              (13, 8, 6): 3, (13, 8, 7): 1,
              (13, 9, 0): 12, (13, 9, 1): 14, (13, 9, 2): 19, (13, 9, 3): 20, (13, 9, 4): 21, (13, 9, 5): 16,
              (13, 9, 6): 8, (13, 9, 7): 3, (13, 9, 8): 1,
              (11, 6, 0): 4, (11, 6, 1): 6, (11, 6, 2): 7, (11, 6, 3): 7, (11, 6, 4): 3, (11, 6, 5): 1,
              (13, 7, 0): 7, (13, 7, 1): 8, (13, 7, 2): 10, (13, 7, 3): 10, (13, 7, 4): 8, (13, 7, 5): 3,
              (13, 7, 6): 1,
              (5, 1, 0): 1, (5, 2, 0): 1, (5, 2, 1): 1, (5, 3, 0): 2, (5, 3, 1): 2, (5, 3, 2): 1,
              (7, 2, 0): 1, (7, 2, 1): 1, (7, 3, 0): 2, (7, 3, 1): 2, (7, 3, 2): 1,
              (7, 4, 0): 2, (7, 4, 1): 3, (7, 4, 2): 3, (7, 4, 3): 1}   # run1 "1-max" found; "(1,0)-max" found 0


def rotl(mask, y, n, full):
    y %= n
    return ((mask << y) | (mask >> (n - y))) & full if y else mask


def enumerate_zp(p, k, kappa, special, tag):
    """Copy of zs_check_v1.enumerate_zp plus tick() every 4096 nodes."""
    n = 2 * p; full = (1 << n) - 1
    R = 2 * p + 2 * kappa - k
    lo = 2 * kappa + 2
    odd = [2 * t + 1 for t in range(p)]
    zt = (p - 1) // 2
    first = zt if special else 0
    order = [first] + [t for t in range(p) if t != first]
    mult = [0] * p
    out = []
    nodes = [0]

    def add(reach, y):
        nxt = reach[:]
        for l in range(n, 0, -1):
            nxt[l] |= rotl(reach[l - 1], y, n, full)
        for l in range(lo, n + 1):
            if nxt[l] & 1:
                return None
        return nxt

    def dfs(pos, reach, size, cap):
        nodes[0] += 1
        if nodes[0] & 4095 == 0:
            tick(tag, nodes[0])
        if size == R:
            out.append(tuple(mult)); return
        if pos == p or size + (p - pos) * cap < R:
            return
        t = order[pos]
        dfs(pos + 1, reach, size, cap)
        cur = reach; j = 0
        lim = cap if not special else cap - 1
        while j < lim and size + j < R:
            cur = add(cur, odd[t])
            if cur is None:
                break
            j += 1; mult[t] = j
            dfs(pos + 1, cur, size + j, cap)
        mult[t] = 0

    reach0 = [0] * (n + 1); reach0[0] = 1
    cur = reach0; j = 0; t0 = order[0]; seq = []
    while j < R:
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
        if c == 0:
            continue
        st = {(l + j, (s + j * v) % n) for (l, s) in st for j in range(c + 1)}
    return st


def max_zero_sum(counts, vals, n):
    """A longest zero-sum sub-multiset (as counts; possibly empty), deterministic (copy of zs_check_v1)."""
    best = {0: (0, ())}
    for c, v in zip(counts, vals):
        nb = {}
        for s, (ln, ch) in sorted(best.items()):
            for j in range(c + 1):
                s2 = (s + j * v) % n
                cand = (ln + j, ch + (j,))
                if s2 not in nb or cand[0] > nb[s2][0]:
                    nb[s2] = cand
        best = nb
    return best[0][0], list(best[0][1])


def sym(x, p):
    x %= 2 * p
    return x if x <= p else x - 2 * p


def cost_of(counts, vals, hinv, p):
    tot = 0
    for c, v in zip(counts, vals):
        if c:
            b = sym(v * hinv, p)
            tot += c * ((b - 1) if b > 0 else -b)
    return tot


def min_cost(counts, vals, n, p):
    return min(cost_of(counts, vals, pow(h, -1, n), p) for h in vals if h != p)


def zx_steps(counts, vals, n, p, k, kappa, zc=None):
    """Steps A-G of Lemma ZX.  zc: the Z to use (counts); default a longest zero-sum.  Returns (failed, data)."""
    bad = []
    if zc is None:
        zlen, zc = max_zero_sum(counts, vals, n)
    zlen = sum(zc)
    yc = [c - z for c, z in zip(counts, zc)]
    L = sum(yc)
    e = 2 * p - 1 - L
    if any(s == 0 and l >= 1 for (l, s) in states(yc, vals, n)):
        bad.append("A_zsf")
    if not (0 <= e <= k - 1 and e == k - 1 - 2 * kappa + zlen):
        bad.append("A_e")
    m = max(yc) if L else 0
    tops = [i for i, c in enumerate(yc) if c == m]
    if L == 0 or len(tops) != 1 or vals[tops[0]] == p:
        bad.append("A_g"); return bad, None
    g = vals[tops[0]]
    ginv = pow(g, -1, n)
    ws = []
    for c, v in zip(yc, vals):
        ws += [(v * ginv) % n] * c
    ws.sort()
    ds = [w for w in ws if w != 1]
    e1 = sum(w - 1 for w in ws)
    W1 = sum(ws)
    run = 0; complete = True
    for w in ws:
        if w > run + 1:
            complete = False
        run += w
    if not (ws.count(1) == m and all(w % 2 == 1 and 3 <= w <= min(m, k) for w in ds) and e1 <= e
            and m >= max(2, e + 1) and 2 * m - 2 * p + 1 >= 2 * L - e1 - 2 * p + 1 and complete and W1 <= n - 1):
        bad.append("A_mult")
    zb = []
    for c, v in zip(zc, vals):
        zb += [sym(v * ginv, p)] * c
    pos = [b for b in zb if b > 0]
    neg = [-b for b in zb if b < 0]
    r = len(pos)
    if any(b != 1 for b in pos):
        bad.append("C")
    if any(beta > e - e1 for beta in neg):
        bad.append("D")
    sigma = sum(neg)
    if sigma != r:
        bad.append("E")
    if not W1 <= 2 * p - 1 - r:
        bad.append("F")
    cg = cost_of(counts, vals, ginv, p)
    if not (cg <= e <= k - 1):
        bad.append("G")
    allb = []
    for c, v in zip(counts, vals):
        allb += [sym(v * ginv, p)] * c
    if any(abs(b) > k for b in allb):
        bad.append("G_b")
    return bad, dict(g=g, zlen=zlen, e=e, e1=e1, r=r, sigma=sigma, cost=cg)


def pp_search(counts, vals, n, p, kappa):
    """Lemma S1 (b): two disjoint minimal zero-sums with lengths in [2p-2kappa+2, 2kappa], total >= 2p+2."""
    tot = 1
    for c in counts:
        tot *= c + 1
    if tot > PP_CAP:
        return "PP_UNCHECKED"
    lo, hi = 2 * p - 2 * kappa + 2, 2 * kappa
    mins = []
    for sel in itertools.product(*[range(c + 1) for c in counts]):
        l = sum(sel)
        if l < lo or l > hi or sum(j * v for j, v in zip(sel, vals)) % n:
            continue
        if any(s == 0 and 0 < ll < l for (ll, s) in states(list(sel), vals, n)):
            continue
        mins.append(sel)
    for a in range(len(mins)):
        for b in range(a, len(mins)):
            A, B = mins[a], mins[b]
            if sum(A) + sum(B) >= 2 * p + 2 and all(x + y <= c for x, y, c in zip(A, B, counts)):
                return "PP_FOUND"
    return "PP_NOT_FOUND"


def unit_tests():
    """S1 checker and step checker on fixed sequences (controls)."""
    res = {}
    p = 7; n = 14; vals = [2 * t + 1 for t in range(p)]
    c = [0] * p; c[0] = 2 * p                                   # g^(2p): longest zero-sum 2p
    res["S1_g2p"] = max(l for (l, s) in states(c, vals, n) if s == 0) == 2 * p
    c = [0] * p; c[0] = p; c[p - 1] = p; c[(p - 1) // 2] = 2   # g^p (-g)^p (pg)^2: longest zero-sum 2p + 2
    res["S1_long"] = max(l for (l, s) in states(c, vals, n) if s == 0) == 2 * p + 2 == max_zero_sum(c, vals, n)[0]
    k, kap = 4, 3                                              # type II at (7, 4, 3)
    c = [0] * p; c[0] = 2 * p - 1; c[p - 1] = kap
    bad, d = zx_steps(c, vals, n, p, k, kap)
    res["typeII_pass"] = (bad == [] and d["cost"] == d["e"] == k - 1)
    res["M1_fires_typeII"] = not (d["cost"] <= d["e"] - 1)
    bad2, _ = zx_steps(c, vals, n, p, k, kap, zc=[0] * p)       # planted defect: Z empty is not longest
    res["planted_A_zsf"] = "A_zsf" in bad2
    return res


def run_item(p, k, kappa, emit):
    n = 2 * p; vals = [2 * t + 1 for t in range(p)]
    tag = "%d,%d,%d" % (p, k, kappa)
    rec = dict(kind="ITEM", p=p, k=k, kappa=kappa, R=2 * p + 2 * kappa - k,
               region=("ZX" if 2 * kappa <= p - 1 else "RESIDUAL"), passes={}, zp2_fail=0, conc_fail=0,
               s1_fail=0, s1_fail_examples=[], pp={}, zx_fail={}, zx_examples=[], typeII=False,
               typeII_expected=(kappa == k - 1), typeII_ok=None, m1_fired=0, cost_eq_e=0)
    t0 = time.monotonic()
    for special in (False, True):
        found, nodes = enumerate_zp(p, k, kappa, special, tag)
        rec["passes"]["(1,0)-max" if special else "1-max"] = dict(found=len(found), nodes=nodes)
        for mv in found:
            counts = list(mv)
            st = states(counts, vals, n)
            if any(s == 0 and 2 * kappa + 2 <= l <= n for (l, s) in st):
                rec["zp2_fail"] += 1
            if min_cost(counts, vals, n, p) > k - 1:
                rec["conc_fail"] += 1
            zmax = max(l for (l, s) in st if s == 0)
            isII = (kappa == k - 1 and counts == [2 * p - 1 if i == 0 else (k - 1 if i == p - 1 else 0)
                                                  for i in range(p)])
            if isII:
                rec["typeII"] = True
            if zmax > 2 * kappa:
                rec["s1_fail"] += 1
                pp = pp_search(counts, vals, n, p, kappa)
                rec["pp"][pp] = rec["pp"].get(pp, 0) + 1
                if len(rec["s1_fail_examples"]) < 5:
                    rec["s1_fail_examples"].append(dict(mult={vals[i]: c for i, c in enumerate(counts) if c},
                                                        zmax=zmax, two_kappa_ge_p_plus_1=(2 * kappa >= p + 1),
                                                        min_cost=min_cost(counts, vals, n, p), pp=pp))
                continue
            bad, d = zx_steps(counts, vals, n, p, k, kappa)
            for b in bad:
                rec["zx_fail"][b] = rec["zx_fail"].get(b, 0) + 1
            if bad and len(rec["zx_examples"]) < 5:
                rec["zx_examples"].append(dict(why=bad, mult={vals[i]: c for i, c in enumerate(counts) if c}))
            if d is not None:
                if d["cost"] == d["e"]:
                    rec["cost_eq_e"] += 1
                if d["cost"] > d["e"] - 1:
                    rec["m1_fired"] += 1
                if isII:
                    rec["typeII_ok"] = (bad == [] and d["cost"] == k - 1)
    rec["sec"] = round(time.monotonic() - t0, 1)
    if (p, k, kappa) in RUN1_FOUND:
        rec["run1_found"] = RUN1_FOUND[(p, k, kappa)]
        rec["found_matches_run1"] = (rec["passes"]["1-max"]["found"] == RUN1_FOUND[(p, k, kappa)]
                                     and rec["passes"]["(1,0)-max"]["found"] == 0)
    return rec


def main():
    with open(sys.argv[1], "x") as out:
        def emit(r):
            out.write(json.dumps(r, sort_keys=True) + "\n"); out.flush()
            print(json.dumps(r, sort_keys=True), flush=True)
        _emit[0] = emit
        emit(dict(kind="START", clock=time.strftime("%Y-%m-%dT%H:%M:%S%z"), items=len(ITEMS), budget_s=BUDGET_S))
        emit(dict(kind="UNIT_TESTS", **unit_tests()))
        stopped = False
        for (p, k, kap) in ITEMS:
            if stopped:
                emit(dict(kind="ITEM_UNKNOWN", p=p, k=k, kappa=kap, reason="budget")); continue
            try:
                emit(run_item(p, k, kap, emit))
            except Stop:
                stopped = True
                emit(dict(kind="ITEM_UNKNOWN", p=p, k=k, kappa=kap, reason="budget reached during item"))
        emit(dict(kind="DONE" if not stopped else "DONE_PARTIAL", clock=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                  elapsed=round(time.monotonic() - T_START, 1)))


if __name__ == "__main__":
    main()
