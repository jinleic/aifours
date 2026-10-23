# E14 (plan-E14.md): c-function structure for interval-feasible data in regime III.  Finite aid, not a premise.
import json, os, random, sys, time

def g(E, kap):
    return min(E - kap, E // 2)

def run_datum(p, kap, r, cap, rng):
    k = len(r); R = sum(r)
    forb = {}
    for m in range(R + 1):
        lo, hi = -g(R - m, kap), g(m, kap)
        forb[m] = set(x % p for x in range(lo, hi + 1)) if hi >= lo else set()
    M = [0] * (k + 1)
    for t in range(k):
        M[t + 1] = M[t] + r[t]
    P = [0] * (k + 1)
    u = [0] * k
    leaves = []
    def dfs(j):
        if len(leaves) >= cap:
            return
        vals = list(range(p)); rng.shuffle(vals)
        for x in vals:
            if r[j] == 0 and x == 0:
                continue
            P[j + 1] = (P[j] + x) % p
            if j == k - 1 and P[k] != 0:
                continue
            ok = True
            for i in range(j + 1):
                if i == 0 and j == k - 1:
                    continue
                if (P[j + 1] - P[i]) % p in forb[M[j + 1] - M[i]]:
                    ok = False; break
            if not ok:
                continue
            u[j] = x
            if j == k - 1:
                leaves.append(list(u))
                if len(leaves) >= cap:
                    return
            else:
                dfs(j + 1)
                if len(leaves) >= cap:
                    return
    dfs(0)
    return leaves

def cvals(p, kap, r, u):
    k = len(r); R = sum(r)
    def gap(m):
        return g(m, kap) + 1, p - 1 - g(R - m, kap)
    def rep(x, m):
        lo, hi = gap(m)
        y = lo + ((x - lo) % p)
        assert y <= hi, (x, m, lo, hi)
        return y
    w = [rep(u[t], r[t]) for t in range(k)]
    J = sum(w) // p - 1
    assert sum(w) % p == 0
    ww = w + w; rr = r + r
    pw = [0]; pm = [0]
    for t in range(2 * k):
        pw.append(pw[-1] + ww[t]); pm.append(pm[-1] + rr[t])
    cs = {}
    for s in range(k):
        for L in range(1, k):
            W = pw[s + L] - pw[s]; m = pm[s + L] - pm[s]
            cs[(s, L)] = (W - rep(W % p, m)) // p
    return J, cs, w

def necklaces(k, ne):
    from itertools import combinations
    seen = set(); out = []
    for comb in combinations(range(k), ne):
        r = [0 if t in comb else 1 for t in range(k)]
        key = min(tuple(r[i:] + r[:i]) for i in range(k))
        if key not in seen:
            seen.add(key); out.append(list(key))
    return out

def main():
    out = {"plan": "plan-E14.md", "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "sets": []}
    rng = random.Random(14)
    configs = [(7, 3, 13, 6, None, 1000), (11, 4, 19, 8, 20, 1000)]
    for (p, kap, k, ne, nsample, cap) in configs:
        data = necklaces(k, ne)
        if nsample is not None:
            rng2 = random.Random(1400 + p); data = rng2.sample(data, nsample)
        S = {"p": p, "kappa": kap, "k": k, "n_E": ne, "R": k - ne, "data": len(data), "cap": cap,
             "leaves": 0, "cmin": None, "cmax": None, "J_values": {}, "leaves_with_c_nonzero": 0, "examples": []}
        for r in data:
            leaves = run_datum(p, kap, r, cap, rng)
            for u in leaves:
                J, cs, w = cvals(p, kap, r, u)
                S["leaves"] += 1
                S["J_values"][str(J)] = S["J_values"].get(str(J), 0) + 1
                mn, mx = min(cs.values()), max(cs.values())
                S["cmin"] = mn if S["cmin"] is None else min(S["cmin"], mn)
                S["cmax"] = mx if S["cmax"] is None else max(S["cmax"], mx)
                if mn != 0 or mx != 0:
                    S["leaves_with_c_nonzero"] += 1
                    if len(S["examples"]) < 5:
                        bad = [[s, L, c] for (s, L), c in cs.items() if c != 0][:12]
                        S["examples"].append({"r": r, "u": u, "w": w, "J": J, "nonzero_c": bad})
        out["sets"].append(S)
        print(json.dumps({kk: S[kk] for kk in ("p", "kappa", "k", "data", "leaves", "cmin", "cmax", "J_values", "leaves_with_c_nonzero")}), flush=True)
    out["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    path = sys.argv[1]
    with open(path, "x") as f:
        json.dump(out, f, indent=1)

if __name__ == "__main__":
    main()
