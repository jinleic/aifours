# E15b (plan-E15b.md): interval + 2-pattern census of uncovered p = 7, B = 0 cells; survivors get the full 2^k check.
# Finite aid, not a premise.  Usage: python3 e15b_census.py OUTDIR kappa:k [kappa:k ...]
import json, sys, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from e15_two_avoiders import windows, search, full_avoid

def run_data(k, R, emax):
    out = []
    seq = [0] * k
    def rec(i, rem, ev):
        if ev > emax:
            return
        if i == k - 1:
            x = rem
            e2 = ev + (x % 2 == 0)
            if e2 > emax:
                return
            seq[i] = x
            t = tuple(seq)
            if all(t <= t[j:] + t[:j] for j in range(1, k)):
                out.append(list(t))
            return
        for x in range(rem + 1):
            seq[i] = x
            rec(i + 1, rem - x, ev + (x % 2 == 0))
    rec(0, R, 0)
    return out

def main():
    outdir = sys.argv[1]
    p = 7
    for spec in sys.argv[2:]:
        kap, k = map(int, spec.split(":"))
        R = 2 * p - k + 2 * kap
        t0 = time.time()
        data = run_data(k, R, 2 * kap)
        W = windows(p, kap, R, k)
        stats = {"nodes": 0}
        res = {"plan": "plan-E15b.md", "code": "e15b_census.py + e15_two_avoiders.py", "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
               "p": p, "kappa": kap, "k": k, "R": R, "data": len(data), "two_avoiders": 0, "full_avoiders": [],
               "minimal_m_hist": {}}
        for di, r in enumerate(data):
            found = search(p, kap, r, W, stats)
            res["two_avoiders"] += len(found)
            for u in found:
                mm = full_avoid(p, kap, r, u, W)
                if mm is None:
                    res["full_avoiders"].append({"r": r, "u": u})
                    print("FULL AVOIDER", kap, k, r, u, flush=True)
                else:
                    res["minimal_m_hist"][str(mm)] = res["minimal_m_hist"].get(str(mm), 0) + 1
            if di % 5000 == 0:
                print(spec, di, len(data), stats["nodes"], res["two_avoiders"], round(time.time() - t0), flush=True)
        res["nodes"] = stats["nodes"]; res["seconds"] = round(time.time() - t0, 1)
        res["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        print(json.dumps({kk: res[kk] for kk in res if kk != "full_avoiders"}), "full_avoiders:", len(res["full_avoiders"]), flush=True)
        with open(os.path.join(outdir, "e15b_%d_%d.json" % (kap, k)), "x") as f:
            json.dump(res, f, indent=1)

if __name__ == "__main__":
    main()
