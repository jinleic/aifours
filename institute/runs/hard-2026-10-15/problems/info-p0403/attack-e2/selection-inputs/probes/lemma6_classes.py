# Probe (<=5 min): same Lemma 6 (wt 5) test as lxw_lemma6_probe.py, plus an EA-invariant
# for each sampled bent f1, so we can see how many EA classes of 6-variable bent functions
# the random Maiorana-McFarland samples cover.
# Invariant: sorted multiset over a != 0 of rad(a) = #{b : D_a D_b f is constant}.
import random, time
import numpy as np
n = 6; N = 64
X = np.arange(N)
pc = np.array([bin(i).count('1') & 1 for i in range(N)])
H = 1 - 2 * pc[np.bitwise_and.outer(X, X)]
def mm_bent(pi, g):
    return np.array([pc[(z >> 3) & pi[z & 7]] ^ g[z & 7] for z in range(N)])
def invariant(f):
    A = X[:, None, None]; B = X[None, :, None]; x = X[None, None, :]
    D2 = f[x] ^ f[x ^ A] ^ f[x ^ B] ^ f[x ^ A ^ B]
    const = (D2.min(axis=2) == D2.max(axis=2))
    rad = const.sum(axis=1)[1:]
    return tuple(sorted(rad.tolist()))
def lemma6_wt5_counterexample(f1):
    W = H @ (1 - 2 * f1)
    assert set(np.abs(W).tolist()) == {8}
    f0 = (W < 0).astype(int)
    rows = []
    for xx in range(N):
        m = 0
        for w in range(N):
            if f0[w] ^ f1[xx] ^ pc[w & xx]: m |= (1 << w)
        rows.append(m)
    found = []
    def dfs(start, depth, o1, o2, o3, ch):
        if found: return
        if depth == 5: found.append(tuple(ch)); return
        for xx in range(start, N):
            r = rows[xx]
            if o3 & r: continue
            ch.append(xx); dfs(xx + 1, depth + 1, o1 | r, o2 | (o1 & r), o3 | (o2 & r), ch); ch.pop()
    dfs(0, 0, 0, 0, 0, [])
    return found[0] if found else None
random.seed(20261015)
t0 = time.time(); stats = {}
quad = np.array([pc[(z >> 3) & (z & 7)] for z in range(N)])
cands = [quad]
while time.time() - t0 < 200:
    if not cands:
        pi = list(range(8)); random.shuffle(pi); g = [random.randint(0, 1) for _ in range(8)]
        cands.append(mm_bent(pi, g))
    f1 = cands.pop()
    inv = invariant(f1)
    S = lemma6_wt5_counterexample(f1)
    st = stats.setdefault(inv, [0, 0]); st[0] += 1
    if S is not None:
        st[1] += 1
        f2 = f1.copy(); f2[list(S)] ^= 1
        print("COUNTEREXAMPLE", inv, S, "nl(f2) =", 32 - int(np.abs(H @ (1 - 2 * f2)).max()) // 2, flush=True)
        break
print(f"elapsed {time.time()-t0:.0f}s; distinct invariant classes seen: {len(stats)}")
for inv, (cnt, bad) in sorted(stats.items(), key=lambda kv: -kv[1][0]):
    from collections import Counter
    print(f"  samples={cnt:5d} counterexamples={bad}  rad-histogram={dict(sorted(Counter(inv).items()))}")
