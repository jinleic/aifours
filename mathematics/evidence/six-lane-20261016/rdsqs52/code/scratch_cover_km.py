import sys, json
sys.path.insert(0,'.')
from rdsqs_lib import SQSKM, kissat, closure
import pg125_cover as C
for name, gens in [("PSL", C.SL), ("PSL+swap", C.SL+[C.NSQ]), ("PSL+Frob", C.SL+[C.FROB]), ("PSL+swap+Frob", C.SL+[C.NSQ, C.FROB]),
                   ("GL-image", C.SL+[C.DIAG_NS]), ("GL-image+Frob", C.SL+[C.DIAG_NS, C.FROB])]:
    G = closure(gens, 52)
    stab = sum(1 for x in G if x[0] == 0)
    M = SQSKM(52, gens)
    cnf, rv = M.cnf(); p = f"runs/e4_km26/km52cover_{name.replace('+','_')}.cnf"; cnf.write(p)
    st, model, dt = kissat(p, 120, seed=0)
    s = M.summary()
    print(name, "order", len(G), "stab", stab, json.dumps({k: s[k] for k in ("triple_orbits", "triple_orbit_sizes", "valid_rows", "valid_rows_by_orbit_size")}), st, round(dt, 3), flush=True)
