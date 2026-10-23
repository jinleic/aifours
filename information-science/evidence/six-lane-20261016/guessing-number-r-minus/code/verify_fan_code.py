"""Exact verification of the Codex fan-gadget code (review/codex-diamond-out.md).
Gadget words (T,A,B,C,D): 00000 00110 10010 11110 10001; fans (T,A,B,C,D) = (1,2,3,4,5) (1,2,7,6,5)
(8,10,4,3,9) (8,10,7,6,9).  Symbol of v = tuple of its gadget bits in fan order.  Checks: (1) global FDs on
R^-; (2) for the 8 diamonds, I(P;Q|Z)=I(U;V|ZP)=I(U;V|ZQ)=0 exactly (integer cross-products) and
U,V dependent given Z; (3) the exact rate comparison 5^7 > 16*3^6, i.e. rate < 20/3 ; (4) mutation control."""
import sys, os, json, itertools
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import R_MINUS_EDGES
W = ["00000", "00110", "10010", "11110", "10001"]
FANS = [(1,2,3,4,5), (1,2,7,6,5), (8,10,4,3,9), (8,10,7,6,9)]
DIAMONDS = [(2,4,1,3),(2,6,1,7),(3,5,1,4),(5,7,1,6),(3,10,4,8),(4,9,3,8),(6,10,7,8),(7,9,6,8)]
NB = {v: set() for v in range(1, 11)}
for a, b in R_MINUS_EDGES: NB[a].add(b); NB[b].add(a)
def build(words):
    code = set()
    for choice in itertools.product(range(len(words)), repeat=4):
        sym = {v: [] for v in range(1, 11)}
        for f, c in zip(FANS, choice):
            for pos, v in enumerate(f): sym[v].append(words[c][pos])
        code.add(tuple("".join(sym[v]) for v in range(1, 11)))
    return sorted(code)
def fd_ok(code):
    for v in range(1, 11):
        seen = {}
        for x in code:
            k = tuple(x[u - 1] for u in sorted(NB[v]))
            if seen.setdefault(k, x[v - 1]) != x[v - 1]: return False, v
    return True, None
def ci_zero(code, A, B, C):   # exact: p(abc)p(c) == p(ac)p(bc) for all values, counts over uniform code
    pr = lambda S: Counter(tuple(x[i - 1] for i in S) for x in code)
    nABC, nC, nAC, nBC = pr(A + B + C), pr(C), pr(A + C), pr(B + C)
    la, lb = len(A), len(B)
    for key, n in nABC.items():
        a, b, c = key[:la], key[la:la + lb], key[la + lb:]
        if n * nC[c] != nAC[a + c] * nBC[b + c]: return False
    # also zero-count cells: product of marginals must be 0 where joint is 0
    for (ac, nac) in nAC.items():
        a, c = ac[:la], ac[la:]
        for bc, nbc in nBC.items():
            if bc[lb:] != c: continue
            if (a + bc[:lb] + c) not in nABC and nac * nbc != 0: return False
    return True
code = build(W)
ok, bad = fd_ok(code)
res = dict(size=len(code), alphabet_sizes=[len({x[v] for x in code}) for v in range(10)], global_fd=ok)
dres = {}
for (u, v, p, q) in DIAMONDS:
    Z = [i for i in range(1, 11) if i not in (u, v, p, q)]
    dres[f"({u},{v};{p},{q})"] = dict(I_PQ_Z_zero=ci_zero(code, [p], [q], Z), I_UV_ZP_zero=ci_zero(code, [u], [v], Z + [p]),
                                    I_UV_ZQ_zero=ci_zero(code, [u], [v], Z + [q]), I_UV_Z_zero=ci_zero(code, [u], [v], Z))
res["diamonds"] = dres
res["all_eight_violate_pattern"] = all(d["I_PQ_Z_zero"] and d["I_UV_ZP_zero"] and d["I_UV_ZQ_zero"] and not d["I_UV_Z_zero"] for d in dres.values())
res["rate_below_20_3_exact"] = 5**7 > 16 * 3**6     # 2log2 5 / h2(2/5) < 20/3  <=>  5^7 > 16*3^6 (Codex claim; see note)
mut = list(W); mut[4] = "10011"                    # mutation: breaks the D decoder
res["mutation_fd"] = fd_ok(build(mut))[0]
print(json.dumps(res, indent=1))
json.dump(res, open(os.path.join(os.path.dirname(__file__), "..", "evidence", "fan-code-check.json"), "w"), indent=1)
sys.exit(0 if (ok and res["all_eight_violate_pattern"] and not res["mutation_fd"]) else 1)
