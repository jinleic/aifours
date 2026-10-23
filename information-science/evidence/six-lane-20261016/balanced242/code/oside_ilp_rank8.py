"""Rank-8 (kappa=4) O-side ILP with the affine canonical sign of W_{Jq} (exploratory; CP-SAT).

For types (8,120),(8,136): W_{Jq}(y) = eps(y) * w(y) with eps=(-1)^{l(y)} for an affine l and
w(y) in c0+16Z (c0 in {4,12}); W_{Dq}=16*(-1)^{Dtilde} (bent dual), |W_{Dq}|=16 everywhere.
Aggregate per-point types (vp=v*eps, dp=W_{Dq}*eps in {+-16}, w, eps).
A solver verdict here is exploratory evidence only.
"""
import sys, json, time
from ortools.sat.python import cp_model

def build(d, zmin, c0, wmax=124):
    m = cp_model.CpModel()
    wv = [w for w in range(-wmax, wmax + 1) if (w - c0) % 16 == 0]
    N = {}
    for vp in (-1, 0, 1):
        for dp in (-16, 16):
            for w in wv:
                for e in (-1, 1):
                    N[(vp, dp, w, e)] = m.NewIntVar(0, 256, f"N_{vp}_{dp}_{w}_{e}")
    it = list(N.items())
    n1, n3, n5, n7 = (m.NewIntVar(0, 256, f"n{k}") for k in (1, 3, 5, 7))
    z = m.NewIntVar(zmin, 256, "z"); c = m.NewIntVar(0, 256, "c"); mp = m.NewIntVar(1, 256, "mp")
    m.Add(sum(x for _, x in it) == 256)
    m.Add(sum(x for (vp, dp, w, e), x in it if vp != 0) == mp)
    m.Add(sum(w * w * x for (vp, dp, w, e), x in it) == 65536)
    m.Add(sum(vp * w * x for (vp, dp, w, e), x in it) == 2 * (n1 + 3 * n3 - 5 * n5 - 7 * n7))
    m.Add(sum(vp * dp * x for (vp, dp, w, e), x in it) == 2 * (n1 - 3 * n3 + 5 * n5 - 7 * n7))
    m.Add(sum(w * dp * x for (vp, dp, w, e), x in it) == 256 * (n1 + n7 - n3 - n5))
    # sum v' = +-2 q(lambda), q odd in [-7,7]
    ql = m.NewIntVar(-4, 3, "qlh")
    m.Add(sum(vp * x for (vp, dp, w, e), x in it) == 2 * (2 * ql + 1))
    # sum v = 2 q(0)
    q0 = m.NewIntVar(-4, 3, "q0h")
    m.Add(sum(e * vp * x for (vp, dp, w, e), x in it) == 2 * (2 * q0 + 1))
    sJ = m.NewBoolVar("sJ"); sD = m.NewBoolVar("sD")
    m.Add(sum(e * w * x for (vp, dp, w, e), x in it) == 256 - 512 * sJ)
    m.Add(sum(e * dp * x for (vp, dp, w, e), x in it) == 256 - 512 * sD)
    # eps distribution: affine l constant or balanced
    ce = m.NewIntVar(0, 2, "ce")
    m.Add(sum(x for (vp, dp, w, e), x in it if e == 1) == 128 * ce)
    # bent dual weight 120 or 136: #{W_Dq=-16}
    bw = m.NewBoolVar("bw")
    m.Add(sum(x for (vp, dp, w, e), x in it if e * dp < 0) == 120 + 16 * bw)
    m.Add(n1 + n3 + n5 + n7 == 256)
    m.Add(n1 + 9 * n3 + 25 * n5 + 49 * n7 == 64 * mp)
    m.Add(16 * mp == 16 * 192 - 5 * d + 4 * z + 8 * c)
    zh = m.NewIntVar(0, 128, "zh"); m.Add(z == 2 * zh)
    m.Add(c <= d); m.Add(z <= 256 - d)
    return m, dict(N=N, n=(n1, n3, n5, n7), z=z, c=c, mp=mp)

def solve(d, zmin, c0, timeout=60.0):
    m, h = build(d, zmin, c0)
    s = cp_model.CpSolver(); s.parameters.max_time_in_seconds = timeout; s.parameters.num_search_workers = 4
    t0 = time.time(); st = s.Solve(m)
    out = dict(type=(8, d), c0=c0, status=s.StatusName(st), wall=round(time.time() - t0, 2))
    if st in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        out.update(z=s.Value(h["z"]), c=s.Value(h["c"]), mp=s.Value(h["mp"]), n=[s.Value(x) for x in h["n"]])
        out["N"] = {str(k): s.Value(x) for k, x in h["N"].items() if s.Value(x)}
    return out

if __name__ == "__main__":
    T = float(sys.argv[1]) if len(sys.argv) > 1 else 60.0
    for d, zmin in [(120, 10), (136, 12)]:
        for c0 in (4, 12):
            print(json.dumps(solve(d, zmin, c0, T))); sys.stdout.flush()
