#!/usr/bin/env python3
"""Compile a DM-orbit spec JSON (semantics of code/dm_orbit_cnf.py) into the plain-text model read by
dmorbit_dfs_v1 (lane cfr33/cfr27, worker InfoCFR27Lift, README section 5.1(a)).

Usage: dmorbit_compile_v1.py SPEC.json OUT.model      (OUT written with mode 'x')
Group elements (mu, pi): pi[i] = image of row i; action on a column (s c)_i = mu * c_{pi^-1(i)}, columns modulo constants.
Output lists the whole group (mu, pi^-1), one representative per G-orbit of unordered row pairs, and per orbit type the
full stabiliser (as group elements) and a left-coset transversal of it. Checks: closure, stabiliser membership, sum of
orbit sizes = n, exactly one zero orbit with stabiliser G if requested.
"""
import hashlib, json, sys


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
    n, k = spec["n"], spec["k"]
    G = closure(spec["gens"], n, k)
    Gset = set(G)
    # representative unordered pairs
    seen, reps = set(), []
    for i in range(k):
        for j in range(i + 1, k):
            if (i, j) in seen:
                continue
            reps.append((i, j))
            for (mu, pi) in G:
                a, b = pi[i], pi[j]
                seen.add((min(a, b), max(a, b)))
    types = []
    total = 0
    nzero = 0
    for o in spec["orbits"]:
        S = closure(o.get("stab", []), n, k)
        for s in S:
            assert s in Gset, "stabiliser element not in G"
        Sset = set(S)
        cos, covered = [], set()
        for g in G:
            if g in covered:
                continue
            cos.append(g)
            for s in S:
                covered.add(compose(g, s, n))
        assert len(cos) * len(S) == len(G)
        zero = bool(o.get("zero", False))
        if zero:
            assert len(S) == len(G) and o["count"] == 1
            nzero += 1
        total += o["count"] * len(cos)
        types.append((o["count"], zero, S, cos))
    assert total == n, "orbit sizes sum to %d, not n = %d" % (total, n)
    assert nzero <= 1
    lines = ["DMORBIT-MODEL v1", "%d %d" % (n, k), "G %d" % len(G)]
    for (mu, pi) in G:
        lines.append("%d %s" % (mu, " ".join(map(str, inv_perm(pi)))))
    lines.append("REPPAIRS %d" % len(reps))
    for (i, j) in reps:
        lines.append("%d %d" % (i, j))
    lines.append("TYPES %d" % len(types))
    for (count, zero, S, cos) in types:
        lines.append("TYPE %d %d %d %d" % (count, 1 if zero else 0, len(S), len(cos)))
        for (mu, pi) in S:
            lines.append("S %d %s" % (mu, " ".join(map(str, inv_perm(pi)))))
        for (mu, pi) in cos:
            lines.append("C %d %s" % (mu, " ".join(map(str, inv_perm(pi)))))
    lines.append("SPEC_SHA256 %s" % hashlib.sha256(spec_bytes).hexdigest())
    text = "\n".join(lines) + "\n"
    with open(sys.argv[2], "x") as fh:
        fh.write(text)
    print(json.dumps({"spec_sha256": hashlib.sha256(spec_bytes).hexdigest(),
                      "model_sha256": hashlib.sha256(text.encode()).hexdigest(), "group_order": len(G),
                      "rep_pairs": reps, "orbit_sizes": [(c, len(cos)) for (c, z, S, cos) in types]}))


if __name__ == "__main__":
    main()
