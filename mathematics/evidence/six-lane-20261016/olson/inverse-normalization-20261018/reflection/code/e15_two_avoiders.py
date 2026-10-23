# E15 (plan-E15.md): exhaustive 2-avoider search + full avoidance check, B = 0, all blocks odd.  Finite aid, not a premise.
import json, sys, time
from itertools import combinations

def windows(p, kap, R, mmax):
    W = {}
    for m in range(1, mmax + 1):
        W[m] = []
        for E in range(R + 1):
            g = lambda mm, EE: min(p - mm, EE + mm - kap - 1, EE // 2)
            lo, hi = -g(m, R - E), g(m, E)
            mask = 0
            if hi >= lo:
                if hi - lo + 1 >= p:
                    mask = (1 << p) - 1
                else:
                    for y in range(lo, hi + 1):
                        mask |= 1 << (y % p)
            W[m].append(mask)
    return W

def full_avoid(p, kap, r, u, W):
    """Return minimal m of a killing pattern, or None if u avoids every proper pattern."""
    k = len(r); R = sum(r); best = None
    for mask in range(1, (1 << k) - 1):
        E = 0; x = 0; m = 0
        for t in range(k):
            if (mask >> t) & 1:
                E += r[t]; x += u[t]
                if not (mask >> ((t - 1) % k)) & 1:
                    m += 1
        if m not in W:
            continue
        if (W[m][E] >> (x % p)) & 1:
            if best is None or m < best:
                best = m
                if best == 1:
                    return 1
    return best

def search(p, kap, r, W, stats):
    k = len(r); R = sum(r)
    U = [0] * (k + 1); M = [0] * (k + 1)
    for t in range(k):
        M[t + 1] = M[t] + r[t]
    u = [0] * k
    Scum = [0] * k
    found = []
    W1, W2 = W[1], W[2]
    def dfs(j):
        for x in range(p):
            if r[j] == 0 and x == 0:
                continue
            stats["nodes"] += 1
            U[j + 1] = (U[j] + x) % p
            if j == k - 1 and U[k] != 0:
                continue
            ok = True
            bits_new = 0
            for i in range(j + 1):
                uu = (U[j + 1] - U[i]) % p; E = M[j + 1] - M[i]
                if not (i == 0 and j == k - 1):
                    if (W1[E] >> uu) & 1:
                        ok = False; break
                bits_new |= 1 << (E * p + uu)
            if not ok:
                continue
            if j < k - 1:
                for i2 in range(2, j + 1):
                    u2 = (U[j + 1] - U[i2]) % p; E2 = M[j + 1] - M[i2]
                    b = Scum[i2 - 2]
                    while b:
                        low = b & -b; idx = low.bit_length() - 1; b ^= low
                        E1, u1 = divmod(idx, p)
                        if (W2[E1 + E2] >> ((u1 + u2) % p)) & 1:
                            ok = False; break
                    if not ok:
                        break
            else:
                for i2 in range(2, k):
                    u2 = (U[k] - U[i2]) % p; E2 = M[k] - M[i2]
                    for j1 in range(1, i2 - 1):
                        for i1 in range(1, j1 + 1):
                            u1 = (U[j1 + 1] - U[i1]) % p; E1 = M[j1 + 1] - M[i1]
                            if (W2[E1 + E2] >> ((u1 + u2) % p)) & 1:
                                ok = False; break
                        if not ok:
                            break
                    if not ok:
                        break
            if not ok:
                continue
            u[j] = x
            Scum[j] = (Scum[j - 1] if j > 0 else 0) | bits_new
            if j == k - 1:
                found.append(list(u))
            else:
                dfs(j + 1)
    dfs(0)
    return found

def necklaces(k, ne):
    seen = set(); out = []
    for comb in combinations(range(k), ne):
        r = [0 if t in comb else 1 for t in range(k)]
        key = min(tuple(r[i:] + r[:i]) for i in range(k))
        if key not in seen:
            seen.add(key); out.append(list(key))
    return out

def main():
    p, kap, k, ne = 7, 3, 13, 6
    data = necklaces(k, ne)
    R = k - ne
    W = windows(p, kap, R, k)
    stats = {"nodes": 0}
    res = {"plan": "plan-E15.md", "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "p": p, "kappa": kap, "k": k, "R": R,
           "data": len(data), "two_avoiders": 0, "full_avoiders": [], "minimal_m_hist": {}}
    for di, r in enumerate(data):
        found = search(p, kap, r, W, stats)
        res["two_avoiders"] += len(found)
        for u in found:
            mm = full_avoid(p, kap, r, u, W)
            if mm is None:
                res["full_avoiders"].append({"r": r, "u": u})
                print("FULL AVOIDER", r, u, flush=True)
            else:
                res["minimal_m_hist"][str(mm)] = res["minimal_m_hist"].get(str(mm), 0) + 1
        if di % 20 == 0:
            print(di, stats["nodes"], res["two_avoiders"], flush=True)
    res["nodes"] = stats["nodes"]
    res["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    print(json.dumps({kk: res[kk] for kk in res if kk != "full_avoiders"}), "full_avoiders:", len(res["full_avoiders"]), flush=True)
    with open(sys.argv[1], "x") as f:
        json.dump(res, f, indent=1)

if __name__ == "__main__":
    main()
