import sys, json
sys.path.insert(0,'.')
from rdsqs_lib import SQSKM, kissat, closure
import pg125
for name, gens in [("PSL", pg125.PSL), ("PSigmaL", pg125.PSL+[pg125.FROB]), ("PGL", pg125.PGL), ("PGammaL", pg125.PGL+[pg125.FROB])]:
    G = closure(gens, 26)
    M = SQSKM(26, gens)
    cnf, rv = M.cnf(); p = f"runs/e4_km26/km_{name}.cnf"; sha = cnf.write(p)
    st, model, dt = kissat(p, 60, seed=0)
    print(name, "order", len(G), json.dumps({k: M.summary()[k] for k in ("triple_orbits", "triple_orbit_sizes", "valid_rows", "valid_rows_by_orbit_size")}), st, round(dt,3))
