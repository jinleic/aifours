#!/usr/bin/env python3
"""Finite control (an aid, not a proof) for Lemma ZS of proof-ROT-half-v1.md / proof-ROT-half-v2.md.
Plan: zs-check-v1/PLAN-v1.md (frozen before any run).

For every item (p, k, kappa) of ITEMS, every multiset Y of 2p + 2kappa - k odd residues mod 2p with
(ZP) "no zero-sum sub-multiset of size in [2kappa+2, 2p]" is enumerated up to multiplication by units, by the method
of code/check_rotfew_v2.py part_b2: residue 1 carries a largest multiplicity (pass "1-max", ties allowed), or (1,0)
carries the strictly largest multiplicity (pass "(1,0)-max").  For each Y it checks:
  ZP2  (ZP) again, by an independent (size, sum) state-set computation;
  CONC the conclusion of Lemma ZS: min over odd generators h of cost_h(Y) <= k - 1;
and, for items inside the lemma's hypothesis (G) of v2 (3k <= 2p + 1, kappa <= min(k-1, p-k)), every claim of the
proof for the generator g of Step 3, with Z one maximum-size zero-sum sub-multiset:
  S1 every zero-sum sub-multiset has size <= 2kappa;      S2 Y - Z is zero-sum-free, e = k-1-2kappa+|Z|, 0 <= e <= k-1;
  S3 g = the unique most frequent value of Y - Z, a generator; its weights are 1 or odd >= 3, each <= m,
     sum (w - 1) = e' <= e, W' <= 2p - 1, sorted weights complete (each <= running total + 1), m >= k - 1;
  S5 every sub-multiset U of Z has tau(U) in {0} u [1, k-1] u [2p-k+1, 2p-1];
  S6 every term of Z has |b| <= k - 1, sigma+ <= k-1, sigma- <= k-1, sigma+ = sigma-;
  S7 W' <= 2p - 1 - sigma;   S8 |Z-| + sigma <= 2kappa;   S9 cost_g(Y) <= k - 1.
Controls: mutation M1 (cost_g <= k - 2) and M2 (S5 with k - 1 in place of k) must fail somewhere in every item that
contains the tight type II multiset; type I and type II multisets must be found; the k = p obstruction is evaluated
directly; the found counts at (11,6) and (13,7) are compared with out/check_rotfew_v3.jsonl.
Usage: zs_check_v1.py OUT.jsonl
"""
import json, sys, time, itertools

V1, V2, BEYOND = "v1", "v2", "beyond"
ITEMS = []
for (p, k) in ((5, 1), (5, 2), (5, 3), (7, 2), (7, 3), (7, 4)):
    for kap in range(0, k):
        ITEMS.append((p, k, kap, V1))
for kap in range(0, 3):
    ITEMS.append((7, 5, kap, V2))
for kap in range(0, 6):
    ITEMS.append((11, 6, kap, V1))
for kap in range(0, 7):
    ITEMS.append((13, 7, kap, V1))
for kap in range(0, 5):
    ITEMS.append((11, 7, kap, V2))
for kap in range(0, 6):
    ITEMS.append((13, 8, kap, V2))
for kap in range(0, 5):
    ITEMS.append((13, 9, kap, V2))
for kap in range(0, 9):
    ITEMS.append((17, 9, kap, V1))
for kap in range(3, 5):
    ITEMS.append((7, 5, kap, BEYOND))
for kap in range(5, 7):
    ITEMS.append((11, 7, kap, BEYOND))
for kap in range(6, 8):
    ITEMS.append((13, 8, kap, BEYOND))
for kap in range(5, 9):
    ITEMS.append((13, 9, kap, BEYOND))
EXPECTED_FOUND = {(11, 6): [4, 6, 7, 7, 3, 1], (13, 7): [7, 8, 10, 10, 8, 3, 1]}   # out/check_rotfew_v3.jsonl, "1-max"


def rotl(mask, y, n, full):
    y %= n
    return ((mask << y) | (mask >> (n - y))) & full if y else mask


def enumerate_zp(p, k, kappa, special):
    """Yield multiplicity vectors (over residues 1, 3, ..., 2p-1) of all (ZP) multisets of size R, normalised."""
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
    """Independent: the set of (size, sum mod n) of all sub-multisets."""
    st = {(0, 0)}
    for c, v in zip(counts, vals):
        if c == 0:
            continue
        st = {(l + j, (s + j * v) % n) for (l, s) in st for j in range(c + 1)}
    return st


def zp_holds(counts, vals, n, kappa):
    st = states(counts, vals, n)
    return not any(s == 0 and 2 * kappa + 2 <= l <= n for (l, s) in st), st


def max_zero_sum(counts, vals, n):
    """A maximum-size zero-sum sub-multiset (as counts), deterministic."""
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


def cost_of(counts, vals, n, hinv, p):
    tot = 0
    for c, v in zip(counts, vals):
        if c:
            b = sym(v * hinv, p)
            tot += c * ((b - 1) if b > 0 else -b)
    return tot


def min_cost(counts, vals, n, p):
    best = None
    for h in vals:
        if h == p:
            continue
        hinv = pow(h, -1, n)
        c = cost_of(counts, vals, n, hinv, p)
        if best is None or c < best[0]:
            best = (c, h)
    return best


def in_G(p, k, kappa):
    return k >= 1 and 3 * k <= 2 * p + 1 and 0 <= kappa <= min(k - 1, p - k)


def check_proof(counts, vals, n, p, k, kappa, st):
    """Return (list of failed proof claims, cost_g, data) for one multiset inside (G)."""
    bad = []
    R = sum(counts)
    zlens = [l for (l, s) in st if s == 0 and l >= 1]
    if zlens and max(zlens) > 2 * kappa:
        bad.append("S1")
    zlen, zc = max_zero_sum(counts, vals, n)
    yc = [c - z for c, z in zip(counts, zc)]
    L = sum(yc)
    if any(s == 0 and l >= 1 for (l, s) in states(yc, vals, n)):
        bad.append("S2_zsf")
    e = k - 1 - 2 * kappa + zlen
    if not (L == R - zlen and e == 2 * p - 1 - L and 0 <= e <= k - 1):
        bad.append("S2_e")
    m = max(yc) if L else 0
    tops = [i for i, c in enumerate(yc) if c == m] if L else []
    if len(tops) != 1:
        bad.append("S3_tie"); return bad, None, None
    g = vals[tops[0]]
    if g == p:
        bad.append("S3_g10"); return bad, None, None
    ginv = pow(g, -1, n)
    ws = []
    for c, v in zip(yc, vals):
        ws += [(v * ginv) % n] * c
    ws.sort()
    e1 = sum(w - 1 for w in ws)
    W1 = sum(ws)
    run = 0; complete = True
    for w in ws:
        if w > run + 1:
            complete = False
        run += w
    if not (all(w == 1 or (w % 2 == 1 and 3 <= w <= m) for w in ws) and e1 <= e and W1 <= n - 1 and complete
            and m >= k - 1):
        bad.append("S3_mult")
    zb = []
    for c, v in zip(zc, vals):
        zb += [sym(v * ginv, p)] * c
    allowed = lambda tau, kk: tau == 0 or 1 <= tau <= kk - 1 or n - kk + 1 <= tau <= n - 1
    m2 = False
    for sel in itertools.product(*[range(c + 1) for c in zc]):
        s = 0
        for j, c, v in zip(sel, zc, vals):
            if j:
                s += j * sym(v * ginv, p)
        tau = (-s) % n
        if not allowed(tau, k):
            bad.append("S5"); break
        if not allowed(tau, k - 1):
            m2 = True
    sp = sum(b for b in zb if b > 0); sm = sum(-b for b in zb if b < 0)
    if not (all(abs(b) <= k - 1 for b in zb) and sp <= k - 1 and sm <= k - 1 and sp == sm):
        bad.append("S6")
    sigma = sp
    if not W1 <= n - 1 - sigma:
        bad.append("S7")
    if not sum(1 for b in zb if b < 0) + sigma <= 2 * kappa:
        bad.append("S8")
    cg = cost_of(counts, vals, n, ginv, p)
    if not cg <= k - 1:
        bad.append("S9")
    return bad, cg, dict(g=g, zlen=zlen, sigma=sigma, m2=m2)


def run_item(p, k, kappa, scope):
    n = 2 * p; vals = [2 * t + 1 for t in range(p)]
    rec = dict(p=p, k=k, kappa=kappa, scope=scope, R=2 * p + 2 * kappa - k, inG=in_G(p, k, kappa), passes={},
               zp2_fail=0, conc_fail=0, proof_fail={}, m1_fired=0, m2_fired=0, typeI=False, typeII=False,
               typeII_expected=(kappa == k - 1), examples=[])
    t0 = time.time()
    for special in (False, True):
        found, nodes = enumerate_zp(p, k, kappa, special)
        rec["passes"]["(1,0)-max" if special else "1-max"] = dict(found=len(found), nodes=nodes)
        for mv in found:
            ok, st = zp_holds(list(mv), vals, n, kappa)
            if not ok:
                rec["zp2_fail"] += 1
            mc = min_cost(list(mv), vals, n, p)
            if mc[0] > k - 1:
                rec["conc_fail"] += 1
                if len(rec["examples"]) < 5:
                    rec["examples"].append(dict(kind="CONC", mult={vals[i]: c for i, c in enumerate(mv) if c},
                                                min_cost=mc[0]))
            if mv == tuple([2 * p - k if i == 0 else 0 for i in range(p)]) and kappa == 0:
                rec["typeI"] = True
            if kappa == k - 1 and mv == tuple([2 * p - 1 if i == 0 else (k - 1 if i == p - 1 else 0)
                                               for i in range(p)]):
                rec["typeII"] = True
            if rec["inG"]:
                bad, cg, data = check_proof(list(mv), vals, n, p, k, kappa, st)
                for b in bad:
                    rec["proof_fail"][b] = rec["proof_fail"].get(b, 0) + 1
                if bad and len(rec["examples"]) < 5:
                    rec["examples"].append(dict(kind="PROOF", why=bad, mult={vals[i]: c for i, c in enumerate(mv) if c}))
                if cg is not None and cg > k - 2:
                    rec["m1_fired"] += 1
                if data and data["m2"]:
                    rec["m2_fired"] += 1
    rec["sec"] = round(time.time() - t0, 1)
    return rec


def obstruction(p):
    n = 2 * p; vals = [2 * t + 1 for t in range(p)]
    counts = [0] * p; counts[0] = 2 * p - 1; counts[1] = p - 1          # g^(2p-1) (3g)^(p-1), kappa = p - 1
    ok, _ = zp_holds(counts, vals, n, p - 1)
    mc = min_cost(counts, vals, n, p)
    return dict(kind="OBSTRUCTION_k=p", p=p, k=p, kappa=p - 1, R=sum(counts), zp=ok, min_cost=mc[0], argmin=mc[1],
                exceeds_k_minus_1=mc[0] > p - 1)


def main():
    with open(sys.argv[1], "x") as out:
        def emit(r):
            out.write(json.dumps(r, sort_keys=True) + "\n"); out.flush(); print(json.dumps(r, sort_keys=True), flush=True)
        for p in (5, 7, 11, 13):
            emit(obstruction(p))
        for (p, k, kap, scope) in ITEMS:
            rec = run_item(p, k, kap, scope)
            if (p, k) in EXPECTED_FOUND and kap < len(EXPECTED_FOUND[(p, k)]):
                rec["expected_found_1max"] = EXPECTED_FOUND[(p, k)][kap]
                rec["found_matches_earlier"] = rec["passes"]["1-max"]["found"] == EXPECTED_FOUND[(p, k)][kap]
            emit(rec)
        emit(dict(kind="DONE"))


if __name__ == "__main__":
    main()
