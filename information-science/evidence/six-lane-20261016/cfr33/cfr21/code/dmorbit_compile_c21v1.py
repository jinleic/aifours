#!/usr/bin/env python3
"""Compile a DM-orbit spec with possibly TWISTED generators into the model read by dmorbit_xc_v2
(lane cfr33/cfr27, worker InfoCFR27Lift; README section 5.7).

Usage: dmorbit_compile_v2.py SPEC.json OUT.model      (OUT written with mode 'x')
SPEC: n, k, gens = list of [mu, pi] or [mu, pi, t] (t a k-vector; translation part, taken modulo the diagonal).
Element (mu, pi, t) acts by (s c)_i = mu c_{pi^-1(i)} + t_i (columns modulo constants). Composition
(s1 s2)(c) = s1(s2(c)): (mu1 mu2, pi1 o pi2, t) with t_i = mu1 t2_{pi1^-1(i)} + t1_i, normalised t_0 = 0.
Output: "DMORBIT-MODEL v2", "n k", "G |G|" + lines "mu pi^-1[0..k-1] t[0..k-1]", "REPPAIRS r" + pairs, "TYPES 0",
SPEC_SHA256. The closure must not contain a nontrivial pure translation (1, id, t != 0); that is reported as an error.
"""
import hashlib, json, sys


def main():
    spec_bytes = open(sys.argv[1], "rb").read()
    spec = json.loads(spec_bytes)
    n, k = spec["n"], spec["k"]

    def norm(t):
        return tuple((x - t[0]) % n for x in t)

    def inv(p):
        q = [0] * k
        for i, x in enumerate(p):
            q[x] = i
        return tuple(q)

    def compose(g, h):
        (m1, p1, t1), (m2, p2, t2) = g, h
        p1i = inv(p1)
        t = tuple((m1 * t2[p1i[i]] + t1[i]) % n for i in range(k))
        return ((m1 * m2) % n, tuple(p1[p2[i]] for i in range(k)), norm(t))

    gens = []
    for g in spec["gens"]:
        t = g[2] if len(g) > 2 else [0] * k
        gens.append((g[0] % n, tuple(g[1]), norm(tuple(t))))
    ident = (1, tuple(range(k)), tuple([0] * k))
    G = {ident}
    frontier = [ident]
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = compose(g, x)
                if y not in G:
                    G.add(y)
                    new.append(y)
        frontier = new
        if len(G) > 4096:
            raise SystemExit("group too large")
    G = sorted(G)
    for (mu, p, t) in G:
        if mu == 1 and p == tuple(range(k)) and any(t):
            raise SystemExit("closure contains a nontrivial pure translation: not a valid twisted group of this order")
    seen, reps = set(), []
    for i in range(k):
        for j in range(i + 1, k):
            if (i, j) in seen:
                continue
            reps.append((i, j))
            for (mu, p, t) in G:
                a, b = p[i], p[j]
                seen.add((min(a, b), max(a, b)))
    lines = ["DMORBIT-MODEL v2", "%d %d" % (n, k), "G %d" % len(G)]
    for (mu, p, t) in G:
        lines.append("%d %s %s" % (mu, " ".join(map(str, inv(p))), " ".join(map(str, t))))
    lines.append("REPPAIRS %d" % len(reps))
    for (i, j) in reps:
        lines.append("%d %d" % (i, j))
    lines.append("TYPES 0")
    lines.append("SPEC_SHA256 %s" % hashlib.sha256(spec_bytes).hexdigest())
    text = "\n".join(lines) + "\n"
    with open(sys.argv[2], "x") as fh:
        fh.write(text)
    print(json.dumps({"spec_sha256": hashlib.sha256(spec_bytes).hexdigest(),
                      "model_sha256": hashlib.sha256(text.encode()).hexdigest(), "group_order": len(G),
                      "rep_pairs": reps, "twisted_elements": sum(1 for (m, p, t) in G if any(t))}))


if __name__ == "__main__":
    main()
