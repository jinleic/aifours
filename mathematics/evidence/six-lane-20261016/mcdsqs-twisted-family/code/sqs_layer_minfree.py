#!/usr/bin/env python3
"""F3.4 (README §3, frozen 04:33): k = 0 SQS layer where every non-equilateral orbit takes a
Hessian point unless declared free; at most K free orbits; W = missing pair consecutive and
W != {0,1}.  Standard library + kissat; writes only into a fresh OUTDIR.
Usage: sqs_layer_minfree.py P K OUTDIR [TIMEOUT]"""
import json
import os
import subprocess
import sys


def deletion_disabled(*a, **k):
    raise RuntimeError("deletion disabled in this lane")


os.remove = os.unlink = os.rmdir = os.removedirs = deletion_disabled


def main():
    p, K, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    to = int(sys.argv[4]) if len(sys.argv) > 4 else 60
    if os.path.exists(out) and os.listdir(out):
        sys.exit(f"refusing to write into non-empty {out}")
    os.makedirs(out, exist_ok=True)
    inv = lambda a: pow(a % p, p - 2, p)
    S = {x * x % p for x in range(1, p)}
    chi = lambda a: 0 if a % p == 0 else (1 if a % p in S else -1)

    def normalizations(T):
        res = []
        for c in T:
            x, y = [u for u in T if u != c]
            if chi(y - x) != 1:
                x, y = y, x
            res.append(((c - x) * inv(y - x) % p, x, y))
        return res

    def hessian_points(T):
        x, y, z = T
        s1, s2, s3 = (x + y + z) % p, (x * y + y * z + z * x) % p, x * y * z % p
        A2, A1, A0 = (s1 * s1 - 3 * s2) % p, (-(s1 * s2 - 9 * s3)) % p, (s2 * s2 - 3 * s1 * s3) % p
        if A2 == 0:
            return None
        disc = (A1 * A1 - 4 * A2 * A0) % p
        r = pow(disc, (p + 1) // 4, p)
        assert r * r % p == disc
        i2 = inv(2 * A2)
        return sorted({(-A1 + r) * i2 % p, (-A1 - r) * i2 % p})

    seen, orbits = set(), []
    for z in range(2, p):
        if z in seen:
            continue
        T = (0, 1, z)
        zs = sorted({t for t, _, _ in normalizations(T)})
        seen |= set(zs)
        orbits.append({"rep": T, "zs": zs, "hessian": hessian_points(T)})
    nv = 0
    clauses = []

    def new():
        nonlocal nv
        nv += 1
        return nv

    cands, free = [], {}
    for oi, O in enumerate(orbits):
        T = O["rep"]
        if O["hessian"] is None:
            qs = [sum(T) * inv(3) % p]
        else:
            qs = list(range(p))
            free[oi] = new()
        lits = []
        for q in qs:
            vals = sorted({(t, (q - x) * inv(y - x) % p) for t, x, y in normalizations(T)})
            if len({v for _, v in vals}) != len(vals):
                continue
            v = new()
            cands.append((v, oi, q, vals))
            lits.append(v)
            if O["hessian"] is not None and q not in O["hessian"]:
                clauses.append([-v, free[oi]])
        clauses.append(lits)
        for i in range(len(lits)):
            for j in range(i + 1, len(lits)):
                clauses.append([-lits[i], -lits[j]])
    m = {w0: new() for w0 in range(p)}
    clauses.append(list(m.values()))
    ml = list(m.values())
    for i in range(len(ml)):
        for j in range(i + 1, len(ml)):
            clauses.append([-ml[i], -ml[j]])
    clauses.append([-m[1]])  # W = {0,1} excluded (L6a)
    prod = {y: [] for y in range(p)}
    for v, oi, q, vals in cands:
        for _, val in vals:
            prod[val].append(v)
    for y in range(p):
        P = prod[y]
        for i in range(len(P)):
            for j in range(i + 1, len(P)):
                clauses.append([-P[i], -P[j]])
        clauses.append(P + [m[y], m[(y + 1) % p]])
        for c in P:
            clauses.append([-c, -m[y]])
            clauses.append([-c, -m[(y + 1) % p]])
    # sequential counter: sum free <= K
    F = list(free.values())
    n = len(F)
    if K < n:
        s = [[new() for _ in range(K)] for _ in range(n)]
        for i in range(n):
            clauses.append([-F[i], s[i][0]] if K > 0 else [-F[i]])
            if i > 0:
                for j in range(K):
                    clauses.append([-s[i - 1][j], s[i][j]])
                for j in range(1, K):
                    clauses.append([-F[i], -s[i - 1][j - 1], s[i][j]])
                if K > 0:
                    clauses.append([-F[i], -s[i - 1][K - 1]])
    cnf = os.path.join(out, "layer.cnf")
    with open(cnf, "w") as fh:
        fh.write(f"p cnf {nv} {len(clauses)}\n")
        for c in clauses:
            fh.write(" ".join(map(str, c)) + " 0\n")
    r = subprocess.run(["kissat", "-q", f"--time={to}", "--seed=0", cnf], capture_output=True, text=True)
    open(os.path.join(out, "kissat.log"), "w").write(r.stdout[-3000:] + "\n--stderr--\n" + r.stderr)
    status, model = "UNKNOWN", set()
    for line in r.stdout.splitlines():
        if line.startswith("s "):
            status = {"s SATISFIABLE": "SAT", "s UNSATISFIABLE": "UNSAT"}.get(line.strip(), "UNKNOWN")
        elif line.startswith("v "):
            model |= {int(x) for x in line[2:].split() if int(x) > 0}
    res = {"p": p, "K": K, "status": status, "vars": nv, "clauses": len(clauses), "orbits": len(orbits)}
    if status == "SAT":
        res["W"] = [[(w - 1) % p, w] for w, v in m.items() if v in model][0]
        res["free_orbits"] = []
        for v, oi, q, vals in cands:
            if v in model and oi in free and model.__contains__(free[oi]) and q not in orbits[oi]["hessian"]:
                res["free_orbits"].append({"zs": orbits[oi]["zs"], "q_for_rep": q, "rep": orbits[oi]["rep"],
                                           "normalized_values": vals})
    json.dump(res, open(os.path.join(out, "result.json"), "w"), indent=1)
    print(json.dumps(res))


if __name__ == "__main__":
    main()
