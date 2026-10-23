#!/usr/bin/env python3
"""classical_tangent_count_z9_v1: exact first-order deformation counts (theory: evidence/classical-tangent-theory-v1.md)
at the classical Z_9 + 1 pairs of evidence/z9p1_classical_search_v1.result.json (both roles).
Unsymmetric excess = 2 * sum_{a<s} (c_{a,s} - 1). Z_9 + 1 ansatz (U = shift (+) (omega^m*), every symbol pair is moved
by g because only one symbol is fixed): symmetric excess = 2 * N9 - 10, N9 = number of (free) Z_9-orbits of pair-graph
components; gauge orbit dimension = dim commutant (U(2) x U(1)^8 = 12) minus the symbol-diagonal part (2) = 10.
Standard library; budget 280 s; output JSON (exclusive) argv[2].
"""
import itertools, json, sys, time
T0 = time.monotonic()
N = 9
data = json.load(open(sys.argv[1]))


def build(d_inf, beta, gamma, delta):
    X = [[None] * 10 for _ in range(10)]
    for i in range(N):
        for d in range(N):
            X[i][(i + d) % N] = 9 if d == d_inf else (i + beta[d]) % N
    for j in range(N):
        X[9][j] = (j + gamma) % N
    for i in range(N):
        X[i][9] = (i + delta) % N
    X[9][9] = 9
    return X


def g_cell(p):
    return tuple((x + 1) % N if x < N else x for x in p)


def g_sym(s):
    return (s + 1) % N if s < N else s


def counts(X, R):
    cells = [(i, j) for i in range(10) for j in range(10)]
    lines = [[(i, j) for j in range(10)] for i in range(10)] + [[(i, j) for i in range(10)] for j in range(10)] + \
            [[c for c in cells if R[c[0]][c[1]] == s] for s in range(10)]
    line_of = {}
    for li, L in enumerate(lines):
        for p in L:
            line_of.setdefault(p, []).append(li)
    symc = {s: [p for p in cells if X[p[0]][p[1]] == s] for s in range(10)}
    comps = {}
    unsym = 0
    for a, s in itertools.combinations(range(10), 2):
        nodes = symc[a] + symc[s]
        par = {p: p for p in nodes}

        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x
        for p in symc[a]:
            for li in line_of[p]:
                q = [r for r in lines[li] if X[r[0]][r[1]] == s]
                ra, rb = find(p), find(q[0])
                if ra != rb:
                    par[ra] = rb
        groups = {}
        for p in nodes:
            groups.setdefault(find(p), []).append(p)
        comps[(a, s)] = [frozenset(gp) for gp in groups.values()]
        unsym += 2 * (len(groups) - 1)
    allc = {(a, s, c) for (a, s), cl in comps.items() for c in cl}
    seen, N9, Nfix = set(), 0, 0
    for item in allc:
        if item in seen:
            continue
        orb, cur = set(), item
        for _ in range(N):
            orb.add(cur)
            a2, s2 = sorted((g_sym(cur[0]), g_sym(cur[1])))
            cur = (a2, s2, frozenset(g_cell(p) for p in cur[2]))
            assert cur in allc
        seen |= orb
        if len(orb) == N:
            N9 += 1
        else:
            Nfix += 1
    multi = {f"{a},{s}": len(c) for (a, s), c in comps.items() if len(c) > 1}
    return {"unsym_excess": unsym, "N9": N9, "non_free_orbits": Nfix, "sym_excess": 2 * N9 - 10, "multi_component_pairs": multi}


out = {"probe": "classical_tangent_count_z9_v1", "results": []}
for hi, h in enumerate(data["first_hits"]):
    if time.monotonic() - T0 > 280:
        out["stop"] = "BUDGET"
        break
    bA = {int(k): v for k, v in h["betaA"].items()}
    bB = {int(k): v for k, v in h["betaB"].items()}
    A = build(0, bA, h["gammaA"], h["deltaA"])
    B = build(h["e"], bB, h["gammaB"], h["deltaB"])
    for role, X, R in (("QLS=A,res=B", A, B), ("QLS=B,res=A", B, A)):
        r = counts(X, R)
        r.update({"hit": hi, "role": role})
        out["results"].append(r)
out["elapsed_s"] = round(time.monotonic() - T0, 3)
with open(sys.argv[2], "x") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps([{k: r[k] for k in ("hit", "role", "unsym_excess", "N9", "non_free_orbits", "sym_excess")} for r in out["results"]]))
