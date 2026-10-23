# wkill.py -- c3 README Sec. 4: test of the kill rule KW-ALL for W(p, kB) (anti run at 0, aligned 1..k-1).
# Independent lambda (Lemma H, all-odd, beta = 0): lambda(Q) = min(p-m+1, D_Q + m - kB, floor((D_Q+B)/2)+1).
# Hard lift vectors: integer x with sum p, singleton bounds, and ALL pair constraints (lower and upper),
# found by randomized DFS; plus uniformly random singleton-feasible x with sum p.  Aid only.
# Usage: python3 wkill.py p kB nsol seed
import sys, random
p, kB, NS, seed = map(int, sys.argv[1:5]); rng = random.Random(seed)
k = p + 1 + kB; B = 1
d = [-1] + [1] * (k - 1)
def blocks(Q):
    s = set(Q); return sum(1 for t in s if (t - 1) % k not in s)
def lam(Q):
    Q = list(Q); m = blocks(Q); D = sum(d[t] for t in Q)
    return min(p - m + 1, D + m - kB, (D + B) // 2 + 1)
def comp(Q):
    s = set(Q); return [t for t in range(k) if t not in s]
lo = [lam([t]) for t in range(k)]; hi = [p - lam(comp([t])) for t in range(k)]
pairL = {}; pairU = {}
for a in range(k):
    for b in range(a + 1, k):
        pairL[(a, b)] = lam([a, b]); pairU[(a, b)] = p - lam(comp([a, b]))
def dfs_solutions(limit, tries=200000):
    sols = []; order = list(range(k)); x = [None] * k; count = [0]
    def rec(i, partial):
        if len(sols) >= limit or count[0] > tries: return
        count[0] += 1
        if i == k:
            if partial == p: sols.append(x[:])
            return
        t = order[i]
        rest = order[i + 1:]
        rmin = sum(lo[u] for u in rest); rmax = sum(hi[u] for u in rest)
        vals = list(range(lo[t], hi[t] + 1)); rng.shuffle(vals)
        for v in vals:
            if not (rmin <= p - partial - v <= rmax): continue
            ok = True
            for u in order[:i]:
                a, b = min(t, u), max(t, u); s2 = v + x[u]
                if s2 < pairL[(a, b)] or s2 > pairU[(a, b)]: ok = False; break
            if not ok: continue
            x[t] = v; rec(i + 1, partial + v); x[t] = None
            if len(sols) >= limit: return
    while len(sols) < limit:
        rng.shuffle(order); count[0] = 0; before = len(sols)
        rec(0, 0)
        if len(sols) == before and count[0] <= tries: break   # exhausted with no new solution
    return sols
def random_vectors(n):
    out = []
    while len(out) < n:
        x = [rng.randint(lo[t], hi[t]) for t in range(k)]
        diff = p - sum(x)
        for _ in range(10 * k):
            if diff == 0: break
            t = rng.randrange(k)
            if diff > 0 and x[t] < hi[t]: x[t] += 1; diff -= 1
            elif diff < 0 and x[t] > lo[t]: x[t] -= 1; diff += 1
        if diff == 0: out.append(x)
    return out
def kwall(x):
    c = [d[t] - x[t] for t in range(k)]
    assert sum(c) == kB - 1
    Zal = [t for t in range(1, k) if x[t] <= 0]
    Z = Zal + ([0] if x[0] <= -1 else [])
    if len(Zal) >= kB: return 'S1', Zal[:kB]
    cZ = sum(c[t] for t in Z)
    assert cZ >= kB - (1 if 0 in Z else 0)
    if Z and cZ + blocks(Z) >= kB + 1: return 'S2', Z
    # step 3 claims
    assert 0 in Z and blocks(Z) == 1 and cZ == kB - 1
    assert all(x[t] == 1 for t in range(1, k) if t not in Z)
    sZ = set(Z); cand = [t for t in range(1, k) if t not in sZ and (t - 1) % k not in sZ and (t + 1) % k not in sZ]
    return 'S3', Z + [cand[0]]
stats = {'S1': 0, 'S2': 0, 'S3': 0}; maxsize = 0; fails = 0; n = 0
sols = dfs_solutions(NS)
vecs = sols + random_vectors(NS)
for x in vecs:
    n += 1
    step, Q = kwall(x)
    stats[step] += 1; maxsize = max(maxsize, len(Q))
    XQ = sum(x[t] for t in Q)
    if not (XQ < lam(Q) and len(Q) <= kB + 1): fails += 1
print({'p': p, 'kB': kB, 'k': k, 'pair_feasible_vectors': len(sols), 'random_vectors': len(vecs) - len(sols),
       'steps': stats, 'max_kill_size': maxsize, 'failures': fails})
