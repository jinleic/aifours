"""Calibration: is the C3-symmetric resolution model solved quickly when it is SATISFIABLE?
Use R3 q=19, C9 certificates (known: derived designs at finite points have C9-invariant
resolutions, hence C3-invariant ones).  Build the C3-symmetric model (anchor ∞0) and run kissat."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mult_pipeline import sym_model
from r3_pipeline import Field
from rdsqs_lib import closure, derived, kissat
q = 19; v = 40; I0 = 38
F = Field(q)
def blocks_of_cert(path):
    bl = []
    for line in open(path):
        line = line.split('#')[0].strip()
        if not line: continue
        t = line.split()
        if t[0] in ('RDSQS', 'BLOCKS'): continue
        if t[0] == 'POINT': break
        bl.append(tuple(map(int, t)))
    return bl
lift = lambda f: tuple([f(x) for x in range(q)] + [f(x) + q for x in range(q)] + [38, 39])
out = []
for cert in sys.argv[1:]:
    bl = blocks_of_cert(cert)
    for order in (3, 9):
        c = F.subgroup_gen(order)
        R = closure([lift(lambda x: F.mul(c, x))], v)
        der = derived(bl, 0); pts = [p for p in range(v) if p != 0]
        cnf, orbits, choice, cosets, stb, osz = sym_model(der, pts, R, I0)
        p = f"runs/engine_calib/c3cal_{os.path.basename(cert)}_R{order}.cnf"; cnf.write(p)
        st, model, dt = kissat(p, 600, seed=1)
        out.append({"cert": cert, "R_order": order, "vars": cnf.nv, "status": st, "seconds": round(dt, 2), "class_orbits": sorted(osz)})
        print(out[-1], flush=True)
json.dump(out, open("runs/engine_calib/c3_calibration.json", "w"), indent=1)
