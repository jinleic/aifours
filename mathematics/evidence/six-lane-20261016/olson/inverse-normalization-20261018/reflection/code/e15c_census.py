# E15c (plan-E15c.md): p = 7, B = 0 census with interval + 2-pattern + 3-pattern pruning; survivors: killed_by(m=3), full check.
# Finite aid, not a premise.  Usage: python3 e15c_census.py OUTDIR kappa:k [kappa:k ...]
import json, sys, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from e15_two_avoiders import windows, full_avoid
from e15b_census_v2 import run_data
from e14e_kills import killed_by

def bits_iter(b):
    while b:
        low = b & -b
        yield low.bit_length() - 1
        b ^= low

def search3(p, kap, r, W, stats):
    k = len(r); R = sum(r)
    U = [0] * (k + 1); M = [0] * (k + 1)
    for t in range(k):
        M[t + 1] = M[t] + r[t]
    u = [0] * k
    Scum = [0] * k; S2cum = [0] * k
    W1, W2, W3 = W[1], W[2], W[3]
    found = []
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
            bits2_new = 0
            if j < k - 1:
                for i2 in range(2, j + 1):
                    u2 = (U[j + 1] - U[i2]) % p; E2 = M[j + 1] - M[i2]
                    for idx in bits_iter(Scum[i2 - 2]):
                        E1, u1 = divmod(idx, p)
                        s = (u1 + u2) % p
                        if (W2[E1 + E2] >> s) & 1:
                            ok = False; break
                        bits2_new |= 1 << ((E1 + E2) * p + s)
                    if not ok:
                        break
                if ok:
                    for i3 in range(4, j + 1):
                        u3 = (U[j + 1] - U[i3]) % p; E3 = M[j + 1] - M[i3]
                        for idx in bits_iter(S2cum[i3 - 2]):
                            E12, u12 = divmod(idx, p)
                            if (W3[E12 + E3] >> ((u12 + u3) % p)) & 1:
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
            S2cum[j] = (S2cum[j - 1] if j > 0 else 0) | bits2_new
            if j == k - 1:
                found.append(list(u))
            else:
                dfs(j + 1)
    dfs(0)
    return found

def main():
    outdir = sys.argv[1]; p = 7
    for spec in sys.argv[2:]:
        kap, k = map(int, spec.split(":"))
        R = 2 * p - k + 2 * kap
        t0 = time.time()
        data = run_data(k, R, 2 * kap)
        W = windows(p, kap, R, k)
        stats = {"nodes": 0}
        res = {"plan": "plan-E15c.md", "code": "e15c_census.py", "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "p": p,
               "kappa": kap, "k": k, "R": R, "data": len(data), "leaves_after_m3_pruning": 0, "full_avoiders": [],
               "minimal_m_hist": {}}
        for di, r in enumerate(data):
            found = search3(p, kap, r, W, stats)
            res["leaves_after_m3_pruning"] += len(found)
            for uu in found:
                if killed_by(p, kap, r, uu, 2) is not None:
                    mm = 2
                elif killed_by(p, kap, r, uu, 3) is not None:
                    mm = 3
                else:
                    mm = full_avoid(p, kap, r, uu, W)
                if mm is None:
                    res["full_avoiders"].append({"r": r, "u": uu})
                    print("FULL AVOIDER", kap, k, r, uu, flush=True)
                else:
                    res["minimal_m_hist"][str(mm)] = res["minimal_m_hist"].get(str(mm), 0) + 1
            if di % 2000 == 0:
                print(spec, di, len(data), stats["nodes"], res["leaves_after_m3_pruning"], round(time.time() - t0), flush=True)
        res["nodes"] = stats["nodes"]; res["seconds"] = round(time.time() - t0, 1)
        res["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        print(json.dumps({kk: res[kk] for kk in res if kk != "full_avoiders"}), "full_avoiders:", len(res["full_avoiders"]), flush=True)
        with open(os.path.join(outdir, "e15c_%d_%d.json" % (kap, k)), "x") as f:
            json.dump(res, f, indent=1)

if __name__ == "__main__":
    main()
