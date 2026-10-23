"""Probe: SQS(52) on PG(1,25) x {0,1} invariant under PSL(2,25) (diagonal) extended by an
outer element composed with the copy swap: phi∘swap, delta∘swap, delta∘phi∘swap (delta in PGL\\PSL)."""
import sys, json
sys.path.insert(0,'.')
from rdsqs_lib import SQSKM, kissat, closure, comp
import pg125
def diag(g): return tuple(g[p % 26] + 26 * (p // 26) for p in range(52))
SW = tuple((p % 26) + 26 * (1 - p // 26) for p in range(52))
PSL = [diag(g) for g in pg125.PSL]
PHI = diag(pg125.FROB); DEL = diag(pg125.NS)
for name, extra in [("phi.swap", comp(PHI, SW)), ("delta.swap", comp(DEL, SW)), ("delta.phi.swap", comp(DEL, comp(PHI, SW)))]:
    gens = PSL + [extra]
    G = closure(gens, 52)
    M = SQSKM(52, gens)
    cnf, rv = M.cnf(); p = f"runs/e4_km26/km52_twist_{name}.cnf"; cnf.write(p)
    st, model, dt = kissat(p, 120, seed=0)
    s = M.summary()
    print(name, "order", len(G), "transitive", len({g[0] for g in G}) == 52, json.dumps({k: s[k] for k in ("triple_orbits", "valid_rows")}), st, round(dt, 3), flush=True)
