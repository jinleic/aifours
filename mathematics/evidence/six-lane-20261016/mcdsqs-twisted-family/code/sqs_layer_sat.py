#!/usr/bin/env python3
"""F3.2 / F3.2b (README §3, frozen 04:20): SQS layer with k = 0 on F_p x Z2 under the twisted
AGL(1,p).  Copy-0 triple orbits (normalized {0,1,z}): equilateral -> centroid; progression
{0,1/2,1} -> midpoint; every other orbit -> one of its two Hessian points (free bit); in mode
F3.2b the orbits through w = omega, omega^2 (w = z/(z-1)) are fully free.  SAT (kissat):
z -> f({0,1,z}) injective and missing exactly a consecutive pair {w0-1, w0}.  A SAT model is
expanded to the full block set and checked directly as an SQS(2p).
Writes only into a fresh OUTDIR (cnf, kissat log, result.json, blocks file).
Usage: sqs_layer_sat.py P MODE OUTDIR [TIMEOUT]
"""
import json
import os
import subprocess
import sys
from itertools import combinations


def deletion_disabled(*a, **k):
    raise RuntimeError("deletion disabled in this lane")


os.remove = os.unlink = os.rmdir = os.removedirs = deletion_disabled


def main():
    p, mode, out = int(sys.argv[1]), sys.argv[2], sys.argv[3]
    to = int(sys.argv[4]) if len(sys.argv) > 4 else 120
    if os.path.exists(out) and os.listdir(out):
        sys.exit(f"refusing to write into non-empty {out}")
    os.makedirs(out, exist_ok=True)
    inv = lambda a: pow(a % p, p - 2, p)
    S = {x * x % p for x in range(1, p)}
    chi = lambda a: 0 if a % p == 0 else (1 if a % p in S else -1)
    omegas = sorted(w for w in range(2, p) if (w * w + w + 1) % p == 0)

    def normalizations(T):
        """[(t, x, y)] for the three pairs of T: oriented (x,y) with y-x a square, t = (c-x)/(y-x)."""
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

    # orbits of copy-0 triples via the z-values of {0,1,z}
    seen, orbits = set(), []
    for z in range(2, p):
        if z in seen:
            continue
        T = (0, 1, z)
        zs = sorted({t for t, _, _ in normalizations(T)})
        assert z in zs
        seen |= set(zs)
        orbits.append({"rep": T, "zs": zs})
    wcoord = lambda z: z * inv(z - 1) % p
    special_w = {om for om in omegas}  # omega and omega^2
    half = inv(2)
    var = 0
    cands = []  # (var, orbit index, q, [(t, value)])
    clauses = []
    stats = {"orbits": len(orbits)}
    for oi, O in enumerate(orbits):
        T = O["rep"]
        hp = hessian_points(T)
        kinds = []
        if hp is None:
            O["kind"], qs = "equilateral", [sum(T) * inv(3) % p]
        elif mode in ("F3.2c", "F3.5"):
            O["kind"], qs = "free", list(range(p))
        elif half in O["zs"]:
            O["kind"], qs = "progression", [None]  # midpoint, resolved below
        elif mode == "F3.2b" and any(wcoord(z) in special_w for z in O["zs"]):
            O["kind"], qs = "free", list(range(p))
        else:
            O["kind"], qs = "hessian", hp
        if O["kind"] == "progression":
            # midpoint: the middle element of the progression T
            x, y, z = T
            mids = [c for c in T if (2 * c - sum(u for u in T if u != c)) % p == 0]
            assert len(mids) == 1
            qs = [mids[0]]
        O["candidates"] = qs
        lits = []
        for q in qs:
            vals = [(t, (q - x) * inv(y - x) % p) for t, x, y in normalizations(T)]
            vals = sorted(set(vals))
            if len({v for _, v in vals}) != len(vals):
                continue  # internal collision
            var += 1
            cands.append((var, oi, q, vals))
            lits.append(var)
        if not lits:
            clauses.append([])
        clauses.append(lits)
        for i in range(len(lits)):
            for j in range(i + 1, len(lits)):
                clauses.append([-lits[i], -lits[j]])
    m = {}
    for w0 in range(p):
        var += 1
        m[w0] = var
    ml = list(m.values())
    clauses.append(ml)
    if mode == "F3.5":
        clauses.append([m[1]])  # W = {0,1}: doubling-type SQS
    for i in range(len(ml)):
        for j in range(i + 1, len(ml)):
            clauses.append([-ml[i], -ml[j]])
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
    cnf = os.path.join(out, "layer.cnf")
    with open(cnf, "w") as fh:
        fh.write(f"p cnf {var} {len(clauses)}\n")
        for c in clauses:
            fh.write(" ".join(map(str, c)) + " 0\n")
    r = subprocess.run(["kissat", "-q", f"--time={to}", "--seed=0", cnf], capture_output=True, text=True)
    open(os.path.join(out, "kissat.log"), "w").write(r.stdout[-3000:] + "\n--stderr--\n" + r.stderr)
    status = "UNKNOWN"
    model = set()
    for line in r.stdout.splitlines():
        if line.startswith("s "):
            status = {"s SATISFIABLE": "SAT", "s UNSATISFIABLE": "UNSAT"}.get(line.strip(), "UNKNOWN")
        elif line.startswith("v "):
            model |= {int(x) for x in line[2:].split() if int(x) > 0}
    res = {"p": p, "mode": mode, "status": status, "vars": var, "clauses": len(clauses),
           "orbit_kinds": {k: sum(1 for O in orbits if O["kind"] == k) for k in
                           ("equilateral", "progression", "hessian", "free")}}
    if status == "SAT":
        f = {}
        choice = []
        for v, oi, q, vals in cands:
            if v in model:
                O = orbits[oi]
                choice.append({"orbit": oi, "kind": O["kind"], "zs": O["zs"], "q": q,
                               "hessian_index": O["candidates"].index(q) if O["kind"] == "hessian" else None})
                for T in [(0, 1, z) for z in O["zs"]]:
                    pass
        w0 = [w for w, v in m.items() if v in model]
        res["missing_pair"] = [(w0[0] - 1) % p, w0[0]]
        res["choices"] = choice
        # expand: completion of every copy-0 triple by A-equivariance from {0,1,z}
        phi = {}
        for v, oi, q, vals in cands:
            if v in model:
                for t, val in vals:
                    phi[t] = val
        assert sorted(phi) == list(range(2, p))
        blocks = set()
        for T in combinations(range(p), 3):
            t, x, y = normalizations(T)[0]
            h = (x + (y - x) * phi[t]) % p
            blocks.add(tuple(sorted([(u, 0) for u in T] + [(h, 1)])))
            blocks.add(tuple(sorted([((-u) % p, 1) for u in T] + [((-h) % p, 0)])))
        W = res["missing_pair"]
        for a in sorted(S):
            for b in range(p):
                P = sorted((b, (a + b) % p))
                Q = sorted(((a * W[0] + b) % p, (a * W[1] + b) % p))
                blocks.add(tuple(sorted([(P[0], 0), (P[1], 0), (Q[0], 1), (Q[1], 1)])))
        cnt = {}
        for B in blocks:
            for t3 in combinations(B, 3):
                cnt[t3] = cnt.get(t3, 0) + 1
        n = 2 * p
        res["blocks"] = len(blocks)
        res["is_sqs"] = (len(blocks) == n * (n - 1) * (n - 2) // 24 and len(cnt) == n * (n - 1) * (n - 2) // 6
                         and all(c == 1 for c in cnt.values()))
        with open(os.path.join(out, "blocks.txt"), "w") as fh:
            for B in sorted(blocks):
                fh.write(" ".join(f"{x},{i}" for x, i in B) + "\n")
    json.dump(res, open(os.path.join(out, "result.json"), "w"), indent=1)
    print(json.dumps({k: res[k] for k in res if k != "choices"}))


if __name__ == "__main__":
    main()
