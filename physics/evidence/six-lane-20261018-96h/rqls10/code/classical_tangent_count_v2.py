#!/usr/bin/env python3
"""classical_tangent_count_v2 (= v1 plus a 300 s self wall-budget check; v1 never ran): exact combinatorial first-order deformation counts at classical Z_7+3 points.

Theory (lane note evidence/classical-tangent-theory-v1.md): at a classical 1-RQLS (QLS = symbol square X orthogonal to
the resolution R) the first-order deformations modulo cell phases solve x_p'(a) = -conj(x_p(s)) along the edges of the
pair graphs G_{a,s} (a-cells and s-cells of X, joined when they share a row, column or R-class); each G_{a,s} is a
union of three perfect matchings, hence bipartite, and each connected component carries one free complex parameter.
Unsymmetric excess over the gauge orbit (u(10) mod cell phases, dimension 90) = 2 * sum_{a<s} (c_{a,s} - 1).
Z_7-symmetric (forced U, distinct eigen-labels on the three inf rays): one complex parameter per Z_7-orbit of size 7 of
components; g-fixed components (only possible in inf-inf pairs) carry twist omega^(m_l - m_k) != 1, hence 0; gauge
orbit (commutant of U modulo symbol-diagonal) has dimension 12 -> excess_forced = 2*N7 - 12.
Classical U (= shift (+) I_3): fixed components also free -> excess_classical = 2*(N7 + N1) - 18.
Input: the classical pairs JSON (argv[1]); output JSON (exclusive) argv[2]. Standard library only, <= 300 s.
"""
import json, sys, time, itertools
T0 = time.monotonic()
data = json.load(open(sys.argv[1]))

def g_cell(p):
    i, j = p
    return ((i + 1) % 7 if i < 7 else i, (j + 1) % 7 if j < 7 else j)

def counts(X, R):
    v = 10
    cells = [(i, j) for i in range(v) for j in range(v)]
    lines = [[(i, j) for j in range(v)] for i in range(v)] + [[(i, j) for i in range(v)] for j in range(v)] + \
            [[(i, j) for (i, j) in cells if R[i][j] == s] for s in range(v)]
    line_of = {}
    for li, L in enumerate(lines):
        for p in L:
            line_of.setdefault(p, []).append(li)
    sym_cells = {s: [p for p in cells if X[p[0]][p[1]] == s] for s in range(v)}
    res = {"pairs": {}}
    unsym_excess = 0
    comp_id = {}
    for a, s in itertools.combinations(range(v), 2):
        nodes = sym_cells[a] + sym_cells[s]
        parent = {p: p for p in nodes}
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for p in sym_cells[a]:
            for li in line_of[p]:
                q = [r for r in lines[li] if X[r[0]][r[1]] == s]
                assert len(q) == 1
                ra, rb = find(p), find(q[0])
                if ra != rb:
                    parent[ra] = rb
        roots = {}
        for p in nodes:
            roots.setdefault(find(p), []).append(p)
        comps = [frozenset(c) for c in roots.values()]
        res["pairs"][f"{a},{s}"] = len(comps)
        unsym_excess += 2 * (len(comps) - 1)
        for c in comps:
            comp_id[(a, s, c)] = True
    # Z_7 orbits of (pair, component)
    def g_sym(t):
        return (t + 1) % 7 if t < 7 else t
    allc = list(comp_id.keys())
    key = {(a, s, c) for (a, s, c) in allc}
    seen = set()
    N7 = N1 = 0
    N1_detail = []
    for (a, s, c) in allc:
        if (a, s, c) in seen:
            continue
        orb = []
        cur = (a, s, c)
        for _ in range(7):
            orb.append(cur)
            a2, s2 = g_sym(cur[0]), g_sym(cur[1])
            c2 = frozenset(g_cell(p) for p in cur[2])
            if a2 > s2:
                a2, s2 = s2, a2
            cur = (a2, s2, c2)
            assert cur in key, "image component not found"
        orbset = set(orb)
        for o in orbset:
            seen.add(o)
        if len(orbset) == 7:
            N7 += 1
        elif len(orbset) == 1:
            N1 += 1
            N1_detail.append([a, s, len(c)])
        else:
            raise AssertionError("orbit size not 1 or 7")
    res.update({"unsym_excess": unsym_excess, "N7": N7, "N1": N1, "N1_detail": N1_detail,
                "sym_forced_excess": 2 * N7 - 12, "sym_classicalU_excess": 2 * (N7 + N1) - 18,
                "total_components": len(allc)})
    return res

out = {"probe": "classical_tangent_count_v2", "results": []}
BUDGET = 290.0
for hi, hit in enumerate(data["pairs"]):
    A, B = hit["A_array"], hit["B_array"]
    if time.monotonic() - T0 > BUDGET:
        out["stop"] = "BUDGET"
        break
    for role, X, R in (("QLS=A,res=B", A, B), ("QLS=B,res=A", B, A)):
        r = counts(X, R)
        r.update({"hit": hi, "role": role})
        out["results"].append(r)
out["elapsed_s"] = round(time.monotonic() - T0, 3)
with open(sys.argv[2], "x") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps([{k: r[k] for k in ("hit", "role", "unsym_excess", "N7", "N1", "sym_forced_excess", "sym_classicalU_excess", "total_components")} for r in out["results"]]))
