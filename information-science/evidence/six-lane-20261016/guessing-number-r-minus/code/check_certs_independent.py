"""Independent re-check of evidence/certs/*.json (no import of producer modules).

For each certificate: (1) every '>=' row must be literally an elemental Shannon inequality on 10 variables
(h(V)-h(V-i) or h(K+i)+h(K+j)-h(K+i+j)-h(K)), or one of the explicitly declared extra rows;
(2) every '=' row must be h(N[v]) - h(N(v)) for a vertex v of the graph, recomputed here from the edge
list typed below (transcribed from code/graphs.py and cross-checked against evidence/verify-graph.json);
(3) the identity e_V + sum y*row + sum z*eq - sum u_v e_{v} = 0 holds over Fractions with y,u >= 0.
"""
import json, sys, os
from fractions import Fraction as Fr

EDGES = {"Rminus": "12 13 14 15 16 17 23 27 29 2-10 34 38 39 45 48 4-10 56 59 5-10 67 68 69 78 7-10 89 8-10"}
EDGES["R"] = EDGES["Rminus"] + " 9-10"
def parse(s):
    out = []
    for tok in s.split():
        a, b = tok.split("-") if "-" in tok else (tok[0], tok[1:])
        out.append((int(a), int(b)))
    return out
def nbm(edges):
    nb = [0] * 10
    for a, b in edges:
        nb[a - 1] |= 1 << (b - 1); nb[b - 1] |= 1 << (a - 1)
    return nb

def is_elemental(row):
    full = 1023
    r = {int(k): Fr(v) for k, v in row.items()}
    if len(r) == 2:
        (m1, c1), (m2, c2) = sorted(r.items(), key=lambda t: -t[1])
        if c1 == 1 and c2 == -1 and m1 == full and bin(m1 ^ m2).count("1") == 1 and (m2 & m1) == m2:
            return True
    pos = [m for m, c in r.items() if c == 1]; neg = [m for m, c in r.items() if c == -1]
    if any(c not in (1, -1) for c in r.values()):
        return False
    if len(pos) == 2 and len(neg) in (1, 2):
        a, b = pos
        K = a & b
        top = a | b
        if bin(a ^ K).count("1") != 1 or bin(b ^ K).count("1") != 1: return False
        exp_neg = {top} | ({K} if K else set())
        return set(neg) == exp_neg
    return False

def check(path, graph, extra_rows=()):
    d = json.load(open(path))
    nb = nbm(parse(EDGES[graph]))
    fd = []
    for v in range(10):
        r = {nb[v] | (1 << v): Fr(1)}
        if nb[v]: r[nb[v]] = Fr(-1)
        fd.append(r)
    acc = {1023: Fr(1)}
    def add(m, c):
        acc[m] = acc.get(m, Fr(0)) + c
    extra_set = [{int(k): Fr(v) for k, v in er.items()} for er in extra_rows]
    for item in d["ge"]:
        y = Fr(item["y"]); assert y > 0
        row = {int(k): Fr(v) for k, v in item["row"].items()}
        assert is_elemental(item["row"]) or row in extra_set, ("non-elemental row", item["row"])
        for m, c in row.items(): add(m, y * c)
    for item in d["eq"]:
        z = Fr(item["z"]); row = {int(k): Fr(v) for k, v in item["row"].items()}
        assert row in fd, ("not a game equality", item["row"])
        for m, c in row.items(): add(m, z * c)
    u = [Fr(t) for t in d["u"]]
    for v in range(10):
        assert u[v] >= 0; add(1 << v, -u[v])
    bad = {m: c for m, c in acc.items() if c != 0}
    return len(bad) == 0, str(sum(u))

if __name__ == "__main__":
    base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "certs")
    Z = sum(1 << (i - 1) for i in [1, 2, 5, 6, 7, 9]); A, B, C, D = Z | 4, Z | 512, Z | 8, Z | 128
    ing = {}
    for m, c in ((A, -1), (B, -1), (A | B, 1), (A | C, 1), (A | D, 1), (B | C, 1), (B | D, 1), (C | D, -1), (A | B | C, -1), (A | B | D, -1)):
        ing[m] = ing.get(m, 0) + c
    ing = {str(k): v for k, v in ing.items() if v}
    res = {}
    for name, graph, extra in (("shannon_Rminus", "Rminus", ()), ("shannon_R", "R", ()), ("ingl1_Rminus", "Rminus", (ing,))):
        ok, B = check(os.path.join(base, name + ".json"), graph, extra)
        res[name] = dict(identity_ok=ok, bound=B)
    print(json.dumps(res))
    if not all(v["identity_ok"] for v in res.values()): sys.exit(1)
