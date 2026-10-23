"""LP: Shannon + FD + Aut symmetry + for all 8 diamonds  Ing(U,V;P,Q | Z) >= -c * H(P,Q | Z)  (floats).
Shows what a (hypothetical or proven) diamond Ingleton-score bound c would give.  c=0 -> 20/3.
AND/OR satisfies the diamond FDs with Ing = -c_AO * H(PQ), c_AO = (5/2 - (3/2)log2 3)/2 ~ 0.0613,
so no valid diamond-local score bound can have c < c_AO."""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from block_sep import NBM, SIG, TAU
from copy_lp import Model
DIAMONDS = [(2,4,1,3),(2,6,1,7),(3,5,1,4),(5,7,1,6),(3,10,4,8),(4,9,3,8),(6,10,7,8),(7,9,6,8)]
def m(*vs): return sum(1 << (v - 1) for v in vs)
def row(d, c):
    u, v, p, q = d
    Z = sum(1 << (i - 1) for i in range(1, 11) if i not in d)
    U, V, P, Q = m(u), m(v), m(p), m(q)
    t = {}
    def add(mask, x): t[mask] = t.get(mask, 0) + x
    def I(a, b, cc):  # I(a;b|Z cc) as mask coefficients
        add(Z | a | cc, 1); add(Z | b | cc, 1); add(Z | a | b | cc, -1); add(Z | cc, -1)
    def negI(a, b, cc):
        add(Z | a | cc, -1); add(Z | b | cc, -1); add(Z | a | b | cc, 1); add(Z | cc, 1)
    I(U, V, P); I(U, V, Q); I(P, Q, 0); negI(U, V, 0)
    add(Z | P | Q, c); add(Z, -c)          # + c*H(PQ|Z)
    return tuple((None, k, x) for k, x in t.items() if x)
cAO = (2.5 - 1.5 * math.log2(3)) / 2
res = {}
for blocks_name, blocks in (("shannon", [[]]), ("copyA", [[([9], [0, 1, 2, 4, 5, 6, 7, 8])]])):
    for c in (0.0, 0.03, cAO, 0.0894, 0.1, 0.14):
        mdl = Model(NBM)
        for b in blocks: mdl.add_block(b)
        st, val, nc, nr = mdl.solve(sym_perms=[SIG, TAU], extra_ge=[row(d, c) for d in DIAMONDS])
        res[f"{blocks_name}:c={c:.5f}"] = val
        print(blocks_name, f"c={c:.5f}", st, round(val, 6), flush=True)
json.dump(dict(c_AO=cAO, results=res), open(os.path.join(os.path.dirname(__file__), "..", "evidence", "ingleton-score-lp-float.json"), "w"), indent=1)
