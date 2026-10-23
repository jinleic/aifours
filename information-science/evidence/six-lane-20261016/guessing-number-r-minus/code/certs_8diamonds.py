"""Exact certificates: Shannon + FD + h(v)<=1 + ONE diamond conditional Ingleton row => h(V) <= 20/3,
for each of the 8 diamonds (U,V;P,Q | rest) of R^-.  (LP facts; the Ingleton rows are not valid
entropic inequalities in isolation -- see diamond_and_or.py.)"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import R_MINUS_EDGES, nbmasks
from ingleton_cg import ing_row
from make_certs import cert, serialize
DIAMONDS = [(2,4,1,3),(2,6,1,7),(3,5,1,4),(5,7,1,6),(3,10,4,8),(4,9,3,8),(6,10,7,8),(7,9,6,8)]
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "certs")
res = {}
for (u, v, p, q) in DIAMONDS:
    Z = sum(1 << (i - 1) for i in range(1, 11) if i not in (u, v, p, q))
    key = (Z | 1 << (u - 1), Z | 1 << (v - 1), Z | 1 << (p - 1), Z | 1 << (q - 1))
    o, ge, eq, y, z, uu, ok, bad, B = cert(nbmasks(R_MINUS_EDGES), [ing_row(*key)])
    name = f"diamond_{u}_{v}_{p}_{q}"
    rec = dict(name=name, exact_bound=str(B), identity_exact=ok, ingleton_multiplier=str(y[len(ge) - 1]))
    json.dump(dict(rec, **serialize(ge, eq, y, z, uu)), open(os.path.join(outdir, name + ".json"), "w"))
    res[name] = rec; print(json.dumps(rec)); sys.stdout.flush()
if not all(r["identity_exact"] and r["exact_bound"] == "20/3" for r in res.values()): sys.exit(1)
