# Probe (<=5 min): Lou-Xu-Wang arXiv:2610.17897 Lemma 6, case wt(h)=5.
# Lemma 6: f1 bent on 6 vars, d(f1,f2) in {4,5,6} => nl(f2) <= 26.
# For wt(h)=5 with S=supp(h): nl(f1+1_S) >= 27  <=>  for all w: N(w) <= 3, where
# N(w) = #{x in S : phi_x(w)=1}, phi_x(w) = f0(w) + f1(x) + w.x, f0 = dual of f1.
# Search: DFS over 5-subsets with column-count pruning. Also direct FWHT check of any hit.
import random, sys, time, itertools
import numpy as np
n = 6; N = 1 << n
pc = [bin(i).count('1') & 1 for i in range(N)]
def walsh(tt):
    return np.array([sum((-1) ** (tt[x] ^ pc[a & x]) for x in range(N)) for a in range(N)])
def mm_bent(pi, g):  # f(x,y) = x.pi(y) + g(y), x,y in F_2^3 ; input z = x*8 + y
    return [ (pc[(z >> 3) & pi[z & 7]] ^ g[z & 7]) for z in range(N)]
def check(f1):
    W = walsh(f1)
    assert set(np.abs(W)) == {8}, "not bent"
    f0 = [0 if W[w] > 0 else 1 for w in range(N)]
    rows = []
    for x in range(N):
        m = 0
        for w in range(N):
            if f0[w] ^ f1[x] ^ pc[w & x]: m |= (1 << w)
        rows.append(m)
    hits = []
    def dfs(start, depth, o1, o2, o3, chosen):
        if depth == 5:
            hits.append(tuple(chosen)); return
        for x in range(start, N):
            r = rows[x]
            if o3 & r: continue
            chosen.append(x)
            dfs(x + 1, depth + 1, o1 | r, o2 | (o1 & r), o3 | (o2 & r), chosen)
            chosen.pop()
            if hits: return
    dfs(0, 0, 0, 0, 0, [])
    if hits:
        S = hits[0]; f2 = list(f1)
        for x in S: f2[x] ^= 1
        nl2 = (N // 2) - int(np.abs(walsh(f2)).max()) // 2
        return S, nl2
    return None, None
random.seed(20261015)
t0 = time.time(); tested = 0; degs = {}
# quadratic representative first
cands = [[pc[(z >> 3) & (z & 7)] for z in range(N)]]
while time.time() - t0 < 240:
    if not cands:
        pi = list(range(8)); random.shuffle(pi); g = [random.randint(0, 1) for _ in range(8)]
        cands.append(mm_bent(pi, g))
    f1 = cands.pop()
    S, nl2 = check(f1)
    tested += 1
    if S is not None:
        print("COUNTEREXAMPLE to Lemma 6 (wt 5):", "f1 truth table", ''.join(map(str, f1)), "S", S, "nl(f2) by FWHT =", nl2, flush=True)
        break
print(f"tested {tested} Maiorana-McFarland bent f1 (incl. quadratic); counterexample found: {S is not None}; {time.time()-t0:.0f}s", flush=True)
