"""Probe: SQS(52) on PG(1,25) x {0,1} invariant under PSL(2,25)-family acting diagonally,
with or without the copy swap. KM satisfiability only (no resolution yet)."""
import sys, json
sys.path.insert(0,'.')
from rdsqs_lib import SQSKM, kissat, closure
import pg125
def diag(g):  # (x,i) -> (g x, i), point id x + 26 i
    return tuple(g[p % 26] + 26 * (p // 26) for p in range(52))
SW = tuple((p % 26) + 26 * (1 - p // 26) for p in range(52))
for name, gens in [("PSL", pg125.PSL), ("PSigmaL", pg125.PSL+[pg125.FROB]), ("PGL", pg125.PGL), ("PGammaL", pg125.PGL+[pg125.FROB])]:
    for swap in (False, True):
        g52 = [diag(g) for g in gens] + ([SW] if swap else [])
        M = SQSKM(52, g52)
        cnf, rv = M.cnf(); p = f"runs/e4_km26/km52_{name}_{'sw' if swap else 'nosw'}.cnf"; sha = cnf.write(p)
        st, model, dt = kissat(p, 120, seed=0)
        s = M.summary()
        print(name, "swap" if swap else "noswap", json.dumps({k: s[k] for k in ("triple_orbits", "triple_orbit_sizes", "valid_rows", "valid_rows_by_orbit_size")}), st, round(dt, 3), flush=True)
