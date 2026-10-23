"""O-side sign-digit duality ILP (exploratory relaxation; CP-SAT).

For a hypothetical balanced 9-variable target of residue type (rank 2t, weight d) with t<=3
(so kappa=0: W_{Jq} in 8Z), aggregate the 256 input points y of Y=F_2^8 by type
(v(y), delta(y)=W_{Dq}(y), J(y)=W_{Jq}(y)) and impose the exact identities listed in
README/evidence.  Infeasibility (OPTIMAL/FEASIBLE vs INFEASIBLE) is a *solver* verdict and is
not promoted to a theorem without an independent certificate.
"""
import sys, json, time, itertools
from ortools.sat.python import cp_model

def build(rank2t, d, zmin, extra=None, jmax=256, mod16=True, fix=None):
    t = rank2t // 2
    D0 = 2 ** (8 - t)
    m = cp_model.CpModel()
    Jvals = list(range(-jmax, jmax + 1, 8))
    N = {}
    for v in (-1, 0, 1):
        for dl in (-D0, 0, D0):
            for J in Jvals:
                N[(v, dl, J)] = m.NewIntVar(0, 256, f"N_{v}_{dl}_{J}")
    n1, n3, n5, n7 = (m.NewIntVar(0, 256, f"n{k}") for k in (1, 3, 5, 7))
    z = m.NewIntVar(zmin, 256, "z"); c = m.NewIntVar(0, 256, "c")
    mp = m.NewIntVar(1, 256, "mp")
    allN = list(N.items())
    m.Add(sum(x for _, x in allN) == 256)
    m.Add(sum(x for (v, dl, J), x in allN if v != 0) == mp)
    m.Add(sum(x for (v, dl, J), x in allN if dl != 0) == 4 ** t)
    m.Add(sum(J * J * x for (v, dl, J), x in allN) == 65536)
    m.Add(sum(v * J * x for (v, dl, J), x in allN) == 2 * (n1 + 3 * n3 - 5 * n5 - 7 * n7))
    m.Add(sum(v * dl * x for (v, dl, J), x in allN) == 2 * (n1 - 3 * n3 + 5 * n5 - 7 * n7))
    m.Add(sum(J * dl * x for (v, dl, J), x in allN) == 256 * (n1 + n7 - n3 - n5))
    # sums of W_{Jq}, W_{Dq} are +-256
    sJ = m.NewBoolVar("sJ"); sD = m.NewBoolVar("sD")
    m.Add(sum(J * x for (v, dl, J), x in allN) == 256 - 512 * sJ)
    m.Add(sum(dl * x for (v, dl, J), x in allN) == 256 - 512 * sD)
    # sum v = 2 q(0), q(0) odd in [-7,7]
    q0 = m.NewIntVar(-7, 7, "q0"); q0h = m.NewIntVar(-4, 3, "q0h")
    m.Add(q0 == 2 * q0h + 1)
    m.Add(sum(v * x for (v, dl, J), x in allN) == 2 * q0)
    # O-side histogram
    m.Add(n1 + n3 + n5 + n7 == 256)
    m.Add(n1 + 9 * n3 + 25 * n5 + 49 * n7 == 64 * mp)
    # E-side: 16 m' = 16*192 - 5d + 4z + 8c ; z even
    m.Add(16 * mp == 16 * 192 - 5 * d + 4 * z + 8 * c)
    zh = m.NewIntVar(0, 128, "zh"); m.Add(z == 2 * zh)
    # E-side ranges: c <= d, z <= 256-d
    m.Add(c <= d); m.Add(z <= 256 - d)
    if mod16:
        # J/8 mod 2 affine: number of points with J = 8 mod 16 is 0, 128 or 256
        odd = m.NewIntVar(0, 256, "oddJ")
        m.Add(odd == sum(x for (v, dl, J), x in allN if (J // 8) % 2 != 0))
        cls = m.NewIntVar(0, 2, "cls"); m.Add(odd == 128 * cls)
    if extra:
        extra(m, locals())
    if fix:
        for k, val in fix.items():
            m.Add(locals()[k] == val)
    return m, dict(N=N, n=(n1, n3, n5, n7), z=z, c=c, mp=mp)

def solve(rank2t, d, zmin, timeout=120.0, workers=4, **kw):
    m, h = build(rank2t, d, zmin, **kw)
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = timeout
    s.parameters.num_search_workers = workers
    t0 = time.time()
    st = s.Solve(m)
    out = dict(type=(rank2t, d), status=s.StatusName(st), wall=round(time.time() - t0, 2))
    if st in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        out["z"] = s.Value(h["z"]); out["c"] = s.Value(h["c"]); out["mp"] = s.Value(h["mp"])
        out["n"] = [s.Value(x) for x in h["n"]]
        out["N"] = {str(k): s.Value(x) for k, x in h["N"].items() if s.Value(x)}
    return out

if __name__ == "__main__":
    for (r, d, zmin) in [(2, 192, 8), (4, 160, 8), (6, 112, 4), (6, 128, 8), (6, 144, 4)]:
        print(json.dumps(solve(r, d, zmin, timeout=float(sys.argv[1]) if len(sys.argv) > 1 else 60.0)))
        sys.stdout.flush()
