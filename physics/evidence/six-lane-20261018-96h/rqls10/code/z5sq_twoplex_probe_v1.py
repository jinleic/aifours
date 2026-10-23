#!/usr/bin/env python3
"""z5sq_twoplex_probe_v1: exact search in the Z_5^2-orbit ansatz for B = Cay(Z_5 x Z_2) (= Cay(Z_10)).

Ansatz (lane note to follow): coordinates k run over a set K of 10 distinct points (mu_k, nu_k) in Z_5^2; four flat
representatives x_ab (a, b in Z_2) with x_ab(k) = (-1)^{n_ab(k)} / sqrt(10); cell ((i1,i2),(j1,j2)) carries
q(k) = zeta5^(i1 mu_k + j1 nu_k) x_(i2 j2)(k). Rows/columns/classes are orthonormal iff every line {mu = c},
{nu = c}, {mu - nu = c} contains exactly two points of K (K is a 2-plex of the cyclic Latin square of order 5) and,
for every pair {k,k'} of such a line and every edge of the representative graph K4 attached to that direction
(nu: 00-01, 10-11; mu: 00-10, 01-11; mu-nu: 00-11, 01-10), n_r(k)+n_r'(k)+n_r(k')+n_r'(k') = 1 (mod 2).
This probe enumerates all 2-plexes K, records the union-graph bipartiteness (divisibility into two transversals)
and solves the GF(2) system exactly; for every solvable K it writes the explicit exact witness data.
Standard library; budget 280 s; output JSON (exclusive) argv[1].
"""
import itertools, json, sys, time
T0 = time.monotonic()
P = 5


def gf2_solve(rows, nvar):
    """rows: list of (bitmask, rhs). Returns a solution bitmask or None."""
    piv = {}
    for mask, rhs in rows:
        m, r = mask, rhs
        for col in sorted(piv, reverse=True):
            if (m >> col) & 1:
                pm, pr = piv[col]
                m ^= pm
                r ^= pr
        if m == 0:
            if r:
                return None
            continue
        col = m.bit_length() - 1
        for c2 in list(piv):
            pm, pr = piv[c2]
            if (pm >> col) & 1:
                piv[c2] = (pm ^ m, pr ^ r)
        piv[col] = (m, r)
    sol = 0
    for col, (m, r) in piv.items():
        if r:
            sol |= (1 << col)
    return sol


plexes = []
rows_choices = list(itertools.combinations(range(P), 2))
for choice in itertools.product(rows_choices, repeat=P):
    pts = [(mu, nu) for mu in range(P) for nu in choice[mu]]
    cnt_nu = [0] * P
    cnt_w = [0] * P
    for mu, nu in pts:
        cnt_nu[nu] += 1
        cnt_w[(mu - nu) % P] += 1
    if all(c == 2 for c in cnt_nu) and all(c == 2 for c in cnt_w):
        plexes.append(pts)

reps = [(0, 0), (0, 1), (1, 0), (1, 1)]
edges = {"nu": [((0, 0), (0, 1)), ((1, 0), (1, 1))], "mu": [((0, 0), (1, 0)), ((0, 1), (1, 1))],
         "w": [((0, 0), (1, 1)), ((0, 1), (1, 0))]}
key = {"mu": lambda p: p[0], "nu": lambda p: p[1], "w": lambda p: (p[0] - p[1]) % P}
results = []
n_solvable = 0
for K in plexes:
    idx = {p: i for i, p in enumerate(K)}
    match = {}
    for dname in ("mu", "nu", "w"):
        groups = {}
        for p in K:
            groups.setdefault(key[dname](p), []).append(idx[p])
        match[dname] = [tuple(g) for g in groups.values()]
    # union graph bipartiteness
    adj = {i: [] for i in range(10)}
    for dname in match:
        for a, b in match[dname]:
            adj[a].append(b)
            adj[b].append(a)
    color, bip_comps, comps = {}, [], []
    for s in range(10):
        if s in color:
            continue
        color[s] = 0
        stack, comp, bip = [s], [s], True
        while stack:
            u = stack.pop()
            for w_ in adj[u]:
                if w_ not in color:
                    color[w_] = 1 - color[u]
                    stack.append(w_)
                    comp.append(w_)
                elif color[w_] == color[u]:
                    bip = False
        comps.append(len(comp))
        bip_comps.append(bip)
    var = lambda r, k: reps.index(r) * 10 + k
    eqs = []
    for dname, elist in edges.items():
        for (r1, r2) in elist:
            for (k1, k2) in match[dname]:
                m = (1 << var(r1, k1)) ^ (1 << var(r2, k1)) ^ (1 << var(r1, k2)) ^ (1 << var(r2, k2))
                eqs.append((m, 1))
    sol = gf2_solve(eqs, 40)
    rec = {"K": K, "component_sizes": comps, "component_bipartite": bip_comps}
    if sol is not None:
        n_solvable += 1
        rec["n"] = {f"{a}{b}": [(sol >> var((a, b), k)) & 1 for k in range(10)] for (a, b) in reps}
        # independent re-check of every equation
        ok = True
        for dname, elist in edges.items():
            for (r1, r2) in elist:
                for (k1, k2) in match[dname]:
                    s_ = sum((sol >> var(r, k)) & 1 for r in (r1, r2) for k in (k1, k2)) % 2
                    ok &= (s_ == 1)
        rec["recheck"] = ok
    results.append(rec)
    if time.monotonic() - T0 > 280:
        break
out = {"probe": "z5sq_twoplex_probe_v1", "n_twoplexes": len(plexes), "n_examined": len(results), "n_gf2_solvable": n_solvable,
       "n_with_nonbipartite_component": sum(1 for r in results if not all(r["component_bipartite"])),
       "results": results, "elapsed_s": round(time.monotonic() - T0, 3)}
with open(sys.argv[1], "x") as fh:
    json.dump(out, fh)
print(json.dumps({k: out[k] for k in ("n_twoplexes", "n_examined", "n_gf2_solvable", "n_with_nonbipartite_component", "elapsed_s")}))
