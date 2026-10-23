#!/usr/bin/env python3
"""DM-form CNF encoder for (Z_n, k; 1) difference matrices with a prescribed automorphism group (lane cfr33).

Usage: dm_orbit_cnf.py SPEC.json OUT_PREFIX     (writes OUT_PREFIX.cnf and OUT_PREFIX.map.json, mode 'x')
Group elements are pairs (mu, pi): mu a unit of Z_n, pi a permutation of rows 0..k-1 given as a list with pi[i] = image
of row i. Action on a column c (taken modulo adding constant vectors): (s c)_i = mu * c_{pi^-1(i)}.
Composition (mu1,pi1)(mu2,pi2) = (mu1*mu2, pi1 o pi2).  SPEC:
  n, k
  gens   : generators of G (list of [mu, pi])
  orbits : list of {"stab": [[mu, pi], ...] (generators of the stabiliser, a subgroup of G),
                    "count": number of orbits of this type, "zero": true -> base column is the all-zero column}
Every base column b is normalised b_0 = 0 (columns are defined modulo constants). For each stabiliser generator
h = (mu, pi): h(b) = b modulo constants, i.e. b_i = mu * (b_{pi^-1(i)} - b_{pi^-1(0)}) for every row i.
Orbit of b = {g(b) : g in a set of left coset representatives of Stab in G}. Requirement: sum of orbit sizes = n.
DM condition: for every pair of rows i < j and every z in Z_n exactly one column has c_i - c_j = z, where for column
g(b): c_i - c_j = mu_g * (b_{pi_g^-1(i)} - b_{pi_g^-1(j)}).
Variables: one-hot entries E(o,i,v) (i >= 1) and one-hot differences Dif(o,a,b,d) (a < b, defined by table clauses
both directions); everything else is exactly-one / equivalence clauses over these.
"""
import hashlib, json, sys
from math import gcd
from itertools import product


def compose(g, h, n):
    (m1, p1), (m2, p2) = g, h
    return ((m1 * m2) % n, tuple(p1[p2[i]] for i in range(len(p1))))


def closure(gens, n, k):
    ident = (1, tuple(range(k)))
    elems = {ident}
    frontier = [ident]
    gens = [(g[0] % n, tuple(g[1])) for g in gens]
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = compose(g, x, n)
                if y not in elems:
                    elems.add(y)
                    new.append(y)
        frontier = new
    return sorted(elems)


def inv_perm(p):
    q = [0] * len(p)
    for i, x in enumerate(p):
        q[x] = i
    return tuple(q)


def main():
    spec_bytes = open(sys.argv[1], "rb").read()
    spec = json.loads(spec_bytes)
    out = sys.argv[2]
    n, k = int(spec["n"]), int(spec["k"])
    for g in spec["gens"]:
        assert gcd(g[0] % n, n) == 1 and sorted(g[1]) == list(range(k))
    G = closure(spec["gens"], n, k)
    orbit_list = []
    for ot in spec["orbits"]:
        S = closure(ot["stab"], n, k) if ot["stab"] else [(1, tuple(range(k)))]
        assert set(S) <= set(G), "stabiliser not inside G"
        reps, seen = [], set()
        for g in G:
            if g in seen:
                continue
            reps.append(g)
            for s in S:
                seen.add(compose(g, s, n))
        for _ in range(int(ot["count"])):
            orbit_list.append({"stab_gens": [(h[0] % n, tuple(h[1])) for h in ot["stab"]], "reps": reps, "zero": bool(ot.get("zero"))})
    total = sum(len(o["reps"]) for o in orbit_list)
    assert total == n, "orbit sizes sum to %d, need %d" % (total, n)
    nv = 0
    E, Dif = {}, {}
    for o in range(len(orbit_list)):
        for i in range(1, k):
            for v in range(n):
                nv += 1
                E[o, i, v] = nv
        for a in range(k):
            for b in range(a + 1, k):
                for d in range(n):
                    nv += 1
                    Dif[o, a, b, d] = nv
    clauses = set()

    def add(lits):
        s = set(lits)
        if any(-x in s for x in s):
            return
        clauses.add(tuple(sorted(s, key=lambda z: (abs(z), z))))

    def exactly_one(lits):
        add(lits)
        for x in range(len(lits)):
            for y in range(x + 1, len(lits)):
                add([-lits[x], -lits[y]])

    def Dlit(o, a, b, d):
        d %= n
        if a < b:
            return Dif[o, a, b, d]
        return Dif[o, b, a, (-d) % n]

    for o in range(len(orbit_list)):
        for i in range(1, k):
            exactly_one([E[o, i, v] for v in range(n)])
        for b in range(1, k):            # row 0 is 0: Dif(o,0,b,d) <-> E(o,b,-d)
            for d in range(n):
                x, y = Dif[o, 0, b, d], E[o, b, (-d) % n]
                add([-x, y]); add([x, -y])
            exactly_one([Dif[o, 0, b, d] for d in range(n)])
        for a in range(1, k):
            for b in range(a + 1, k):
                for u in range(n):
                    for w in range(n):
                        add([-E[o, a, u], -E[o, b, w], Dif[o, a, b, (u - w) % n]])
                for d in range(n):
                    for u in range(n):
                        add([-Dif[o, a, b, d], -E[o, a, u], E[o, b, (u - d) % n]])
                        add([-Dif[o, a, b, d], -E[o, b, u], E[o, a, (u + d) % n]])
                exactly_one([Dif[o, a, b, d] for d in range(n)])
        if orbit_list[o]["zero"]:
            for i in range(1, k):
                add([E[o, i, 0]])
        for (mu, pi) in orbit_list[o]["stab_gens"]:
            pinv = inv_perm(pi)
            muinv = pow(mu, -1, n)
            q = pinv[0]
            for i in range(1, k):
                p = pinv[i]
                for v in range(n):
                    x, y = E[o, i, v], Dlit(o, p, q, muinv * v)
                    add([-x, y]); add([x, -y])
    # DM conditions
    for i in range(k):
        for j in range(i + 1, k):
            for z in range(n):
                lits = []
                for o in range(len(orbit_list)):
                    for (mu, pi) in orbit_list[o]["reps"]:
                        pinv = inv_perm(pi)
                        lits.append(Dlit(o, pinv[i], pinv[j], pow(mu, -1, n) * z))
                exactly_one(lits)
    cl = sorted(clauses)
    text = "p cnf %d %d\n" % (nv, len(cl)) + "".join(" ".join(map(str, c)) + " 0\n" for c in cl)
    with open(out + ".cnf", "x") as fh:
        fh.write(text)
    info = {"spec_sha256": hashlib.sha256(spec_bytes).hexdigest(), "spec": spec, "group_order": len(G),
            "orbit_sizes": [len(o["reps"]) for o in orbit_list], "cnf_sha256": hashlib.sha256(text.encode()).hexdigest(),
            "vars": nv, "clauses": len(cl), "encoder": "dm_orbit_cnf.py v1",
            "E": [[o, i, v, E[o, i, v]] for (o, i, v) in E],
            "reps": [[[g[0], list(g[1])] for g in o["reps"]] for o in orbit_list]}
    with open(out + ".map.json", "x") as fh:
        json.dump(info, fh)
    print(json.dumps({x: info[x] for x in ("spec_sha256", "cnf_sha256", "vars", "clauses", "group_order", "orbit_sizes")}))


if __name__ == "__main__":
    main()
