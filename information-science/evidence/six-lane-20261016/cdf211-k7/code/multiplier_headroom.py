"""Exact multiplier-restricted searches for a cyclic (211,7,1) difference family.

A multiplier ansatz is NOT part of the target. An empty result here is a restricted-model miss, not
nonexistence of a cyclic (211,7,1) DF.  Every solution found is re-checked by cdf_tools (independent
direct verifier).

Normalisations used (each is an exact symmetry of the condition):
  - Base blocks may be translated; multiplying the whole family by a unit maps DFs to DFs.
  - A block fixed by a multiplier mu up to translation can be translated so that it is fixed exactly
    ((mu - 1) is invertible mod p).

Order 7 (H7 = 7th roots of unity): with 5 blocks every block is fixed, hence a coset c*H7.
  Block g^c*H7 covers the H7-cosets c + D (mod 30), D = {log(eps^j - 1) mod 30 : j = 1..6}.
  So the family is an exact cover of Z_30 by 5 translates of D, enumerated completely for p = 211.
Order 5 (H5): no 7-set is fixed (the orbits are {0} and 5-cycles), so the 5 blocks form one orbit
  {m^i B}.  ΔB must be a transversal of the 42 H5-cosets; equivalently the 21 unordered differences
  have distinct classes log(d) mod 21.  WLOG {0,1} ⊆ B (translate, then scale).  Exhaustive DFS over
  the other five elements in increasing order, split over 4 worker processes by the third element.
Order 3 (H3), all five blocks fixed: each block is {0} ∪ aH3 ∪ bH3, which uses the 7 H6-cosets
  aH6, bH6, a(w-1)H6, b(w-1)H6, (a - b w^s)H6 for s = 0,1,2.  The family is an exact cover of
  Z_35 by 5 such sets, enumerated completely for p = 211.
  The order-3 orbit-type 3+1+1 is NOT searched here.
Controls (first solution only, node-capped; a capped miss is UNKNOWN):
  - order 7 on other primes p ≡ 1 mod 42; radical DFs must verify;
  - the same single-orbit DFS on (31,3), (61,4), (101,5), (151,6) with an order-5 multiplier
    (exhaustive);
  - the order-3 all-fixed cover on p = 337.
"""
import sys, os, json, time, itertools
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdf_tools import all_checks, diff_check

def factor(n):
    f, d = set(), 2
    while d * d <= n:
        while n % d == 0: f.add(d); n //= d
        d += 1
    if n > 1: f.add(n)
    return f

def prim_root(p):
    fs = factor(p - 1)
    return next(g for g in range(2, p) if all(pow(g, (p - 1) // q, p) != 1 for q in fs))

def dlog(p, g):
    L = [None] * p; x = 1
    for e in range(p - 1): L[x] = e; x = x * g % p
    return L

def exact_cover(universe_size, sets, want, cap=None, node_cap=None):
    """All (or first `cap`) selections of `want` sets partitioning range(universe_size).
    Returns (solutions, nodes, complete) where complete=False means the node cap was hit."""
    sols = []; by_elem = [[i for i, S in enumerate(sets) if e in S] for e in range(universe_size)]
    full = frozenset(range(universe_size)); nodes = [0]; stopped = [False]
    def bt(cov, chosen):
        if (cap is not None and len(sols) >= cap) or stopped[0]: return
        nodes[0] += 1
        if node_cap is not None and nodes[0] > node_cap: stopped[0] = True; return
        if len(chosen) == want:
            if cov == full: sols.append(list(chosen))
            return
        x = min(full - cov)
        for i in by_elem[x]:
            if not (sets[i] & cov): bt(cov | sets[i], chosen + [i])
    bt(frozenset(), [])
    return sols, nodes[0], not stopped[0]

def order7(p, k=7, cap=None, node_cap=None):
    g = prim_root(p); L = dlog(p, g); n = (p - 1) // k; eps = pow(g, n, p)
    D = [L[(pow(eps, j, p) - 1) % p] % n for j in range(1, k)]
    t = (p - 1) // (k * (k - 1))
    rec = dict(p=p, g=g, D=D, D_distinct=len(set(D)) == k - 1, radical_sufficient=len({d % (k - 1) for d in D}) == k - 1)
    if not rec["D_distinct"]: rec.update(n_solutions=0, complete=True); return rec
    tr = [frozenset((c + d) % n for d in D) for c in range(n)]
    sols, nodes, complete = exact_cover(n, tr, t, cap=cap, node_cap=node_cap)
    H = [pow(eps, j, p) for j in range(k)]
    rec.update(n_solutions=len(sols), nodes=nodes, complete=complete, cap=cap)
    if sols:
        blocks = [sorted(pow(g, c, p) * h % p for h in H) for c in sols[0]]
        rec.update(example=blocks, example_verified=all_checks(p, k, blocks)["ok"])
    return rec

def _orbit_task(args):
    p, k, cl, x3 = args
    used = 1 << cl[1]
    a, b = cl[x3], cl[x3 - 1]
    if a == b or (used >> a) & 1 or (used >> b) & 1: return x3, 0, []
    sols = []; nodes = 0
    def dfs(B, used, start):
        nonlocal nodes
        if len(B) == k: sols.append(list(B)); return
        for x in range(start, p):
            nodes += 1; m = 0; ok = True
            for y in B:
                bit = 1 << cl[x - y]
                if (used | m) & bit: ok = False; break
                m |= bit
            if ok: dfs(B + [x], used | m, x + 1)
    dfs([0, 1, x3], used | (1 << a) | (1 << b), x3 + 1)
    return x3, nodes, sols

def single_orbit(p, k, m, workers=4):
    assert m * k * (k - 1) == p - 1 and m % 2 == 1
    g = prim_root(p); L = dlog(p, g); half = k * (k - 1) // 2
    cl = [None] + [L[d] % half for d in range(1, p)]
    t0 = time.time(); total_nodes = 0; sols = []
    with ProcessPoolExecutor(max_workers=workers) as ex:
        for x3, nodes, s in ex.map(_orbit_task, [(p, k, cl, x3) for x3 in range(2, p)], chunksize=4):
            total_nodes += nodes; sols.extend(s)
    mu = pow(g, (p - 1) // m, p)
    fam_of = lambda s: [sorted(pow(mu, i, p) * x % p for x in s) for i in range(m)]
    rec = dict(p=p, k=k, m=m, g=g, n_normalised_solutions=len(sols), nodes=total_nodes, wall=round(time.time() - t0, 1), complete=True)
    if sols:
        rec.update(example_base=sols[0], example_family=fam_of(sols[0]), example_all_checks=all_checks(p, k, fam_of(sols[0]))["ok"],
                   all_verified_diff=all(diff_check(p, k, fam_of(s))["ok"] for s in sols), solutions=sols[:200])
    return rec

def order3_all_fixed(p, k=7, cap=None, node_cap=None):
    g = prim_root(p); L = dlog(p, g); n6 = (p - 1) // 6; w = pow(g, (p - 1) // 3, p); H3 = [1, w, w * w % p]
    reps = [pow(g, e, p) for e in range((p - 1) // 3)]
    cands, pairs = [], []
    for i, j in itertools.combinations(range(len(reps)), 2):
        a, b = reps[i], reps[j]
        cos = [L[a] % n6, L[b] % n6, L[a * (w - 1) % p] % n6, L[b * (w - 1) % p] % n6] + [L[(a * h - b) % p] % n6 for h in H3]
        if len(set(cos)) == 7: cands.append(frozenset(cos)); pairs.append((a, b))
    t = (p - 1) // 42
    sols, nodes, complete = exact_cover(n6, cands, t, cap=cap, node_cap=node_cap)
    rec = dict(p=p, n_candidate_blocks=len(cands), n_solutions=len(sols), cap=cap, nodes=nodes, complete=complete)
    if sols:
        fams = [[sorted({0} | {pairs[i][0] * h % p for h in H3} | {pairs[i][1] * h % p for h in H3}) for i in s] for s in sols]
        rec.update(example=fams[0], example_all_checks=all_checks(p, k, fams[0])["ok"], all_verified_diff=all(diff_check(p, k, f)["ok"] for f in fams))
    return rec

if __name__ == "__main__":
    out = {"started": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    out["order7_211"] = order7(211)
    out["order3_all_fixed_211"] = order3_all_fixed(211)
    print(json.dumps(out, default=str)[:2500], flush=True)
    out["order7_controls"] = [order7(p, cap=1, node_cap=2_000_000) for p in (43, 127, 337, 379, 421, 463)]
    out["order3_all_fixed_control_337"] = order3_all_fixed(337, cap=1, node_cap=2_000_000)
    print(json.dumps({a: out[a] for a in ("order7_controls", "order3_all_fixed_control_337")}, default=str)[:2500], flush=True)
    out["single_orbit_controls"] = [single_orbit(p, k, 5) for p, k in ((31, 3), (61, 4), (101, 5), (151, 6))]
    print(json.dumps([{a: b for a, b in r.items() if a != "solutions"} for r in out["single_orbit_controls"]], default=str)[:2500], flush=True)
    out["order5_211"] = single_orbit(211, 7, 5)
    print(json.dumps({a: b for a, b in out["order5_211"].items() if a != "solutions"}, default=str), flush=True)
    out["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "headroom-211.json"), "w"), indent=1, default=str)
