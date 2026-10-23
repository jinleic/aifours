"""Probe: SQS(52) on F25 x {0,1} ∪ {∞0,∞1} invariant under groups acting INDEPENDENTLY on the two copies."""
import sys, json
sys.path.insert(0,'.')
from rdsqs_lib import SQSKM, kissat, closure
import pg125 as F
I0, I1 = 50, 51
def on_copy(j, f):
    return tuple([f(x) if j == 0 else x for x in range(25)] + [f(x) + 25 if j == 1 else x + 25 for x in range(25)] + [I0, I1])
def both(f): return tuple([f(x) for x in range(25)] + [f(x) + 25 for x in range(25)] + [I0, I1])
tr = lambda b: (lambda x: F.add(x, b))
mu = lambda c: (lambda x: F.mul(c, x))
w3 = next(x for x in range(1, 25) if F.order(x) == 3)
SW = tuple([x + 25 for x in range(25)] + [x for x in range(25)] + [I1, I0])
cases = {
  "T0xT1": [on_copy(0, tr(1)), on_copy(0, tr(5)), on_copy(1, tr(1)), on_copy(1, tr(5))],
  "T0xT1+C3diag": [on_copy(0, tr(1)), on_copy(0, tr(5)), on_copy(1, tr(1)), on_copy(1, tr(5)), both(mu(w3))],
  "T0xT1+C3xC3": [on_copy(0, tr(1)), on_copy(0, tr(5)), on_copy(1, tr(1)), on_copy(1, tr(5)), on_copy(0, mu(w3)), on_copy(1, mu(w3))],
  "Tdiag+C3on1": [both(tr(1)), both(tr(5)), both(mu(w3)), on_copy(1, mu(w3))],
  "Tdiag+C3xC3+swap": [both(tr(1)), both(tr(5)), on_copy(0, mu(w3)), on_copy(1, mu(w3)), SW],
  "T0xT1+swap": [on_copy(0, tr(1)), on_copy(0, tr(5)), on_copy(1, tr(1)), on_copy(1, tr(5)), SW],
}
for name, gens in cases.items():
    G = closure(gens, 52)
    M = SQSKM(52, gens)
    cnf, rv = M.cnf(); p = f"runs/e4_km26/km52_indep_{name.replace('+','_')}.cnf"; cnf.write(p)
    st, model, dt = kissat(p, 120, seed=0)
    s = M.summary()
    print(name, "order", len(G), json.dumps({k: s[k] for k in ("triple_orbits", "valid_rows")}), st, round(dt, 3), flush=True)
