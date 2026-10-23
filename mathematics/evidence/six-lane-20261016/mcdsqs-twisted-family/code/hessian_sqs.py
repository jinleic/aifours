#!/usr/bin/env python3
"""F3.1 evaluation (README §3, frozen 04:07): Hessian-completion SQS(2p) on F_p x Z2 under the
twisted AGL(1,p).  Standard library only; writes only OUT.json (refuses to overwrite).

Points (x, i), x in F_p, i in {0,1}.  Copy-0 triple T completed by H_omega (canonical cyclic
orientation with (x-y)(y-z)(z-x) a square; fixed point of multiplier omega of the order-3
Mobius map x->y->z->x).  Variant P1: pole Netto orbit completed by its centroid in copy 1.
Variant P2: (4,0)-blocks = A-orbit of {0, 1, -omega^2, 1/(1-omega)}; H_omega elsewhere.
Copy-1 blocks are the images under (x,i) -> (-x, 1-i).  (2,2)-blocks: for every Phi-invariant
pairing of L0({0,1}), transported by A; the resulting block set is checked directly.
Usage: hessian_sqs.py P OUT.json
"""
import json
import os
import sys
from itertools import combinations


def deletion_disabled(*a, **k):
    raise RuntimeError("deletion disabled in this lane")


os.remove = os.unlink = os.rmdir = os.removedirs = deletion_disabled


def main():
    p, out = int(sys.argv[1]), sys.argv[2]
    if os.path.exists(out):
        sys.exit(f"refusing to overwrite {out}")
    inv = lambda a: pow(a % p, p - 2, p)
    S = {x * x % p for x in range(1, p)}
    chi = lambda a: 0 if a % p == 0 else (1 if a % p in S else -1)
    omegas = sorted(w for w in range(2, p) if (w * w + w + 1) % p == 0)
    A = [(a, b) for a in sorted(S) for b in range(p)]
    res = {"p": p, "omegas": omegas, "variants": []}

    def mobius_cycle(x, y, z):
        # matrix [[a,b],[c,d]] with x->y, y->z, z->x : compose maps to (0,1,inf)
        def to01inf(u, v, w):  # u->0, v->1, w->inf : X -> (X-u)(v-w)/((X-w)(v-u))
            return [[(v - w) % p, (-u * (v - w)) % p], [(v - u) % p, (-w * (v - u)) % p]]
        def mul(M, N):
            return [[(M[0][0] * N[0][0] + M[0][1] * N[1][0]) % p, (M[0][0] * N[0][1] + M[0][1] * N[1][1]) % p],
                    [(M[1][0] * N[0][0] + M[1][1] * N[1][0]) % p, (M[1][0] * N[0][1] + M[1][1] * N[1][1]) % p]]
        def adjinv(M):
            return [[M[1][1], (-M[0][1]) % p], [(-M[1][0]) % p, M[0][0]]]
        T1 = to01inf(x, y, z)
        T2 = to01inf(y, z, x)
        return mul(adjinv(T2), T1)

    def fixed_points(M):
        a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
        # c h^2 + (d-a) h - b = 0
        if c == 0:
            return [None, b * inv(d - a) % p]  # infinity and one finite fixed point
        disc = ((d - a) ** 2 + 4 * b * c) % p
        r = pow(disc, (p + 1) // 4, p)
        assert r * r % p == disc, "Hessian points not rational"
        i2c = inv(2 * c)
        return sorted({((a - d + r) * i2c) % p, ((a - d - r) * i2c) % p})

    def multiplier(M, h):
        a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
        den = (c * h + d) % p
        return (a * d - b * c) * inv(den * den) % p

    for om in omegas:
        for variant in ("P1", "P2"):
            rec = {"omega": om, "variant": variant}
            c0 = inv(1 - om)
            K = tuple(sorted({0, 1, (-om * om) % p, c0}))
            forty = set()
            if variant == "P2":
                for a, b in A:
                    forty.add(tuple(sorted((a * t + b) % p for t in K)))
            in40 = {}
            for B in forty:
                for t in combinations(B, 3):
                    assert t not in in40
                    in40[t] = B
            f = {}
            poles = 0
            for T in combinations(range(p), 3):
                if T in in40:
                    continue
                x, y, z = T
                if chi((x - y) * (y - z) * (z - x)) != 1:
                    y, z = z, y
                M = mobius_cycle(x, y, z)
                hs = fixed_points(M)
                pick = [h for h in hs if h is not None and (M[1][0] * h + M[1][1]) % p != 0
                        and multiplier(M, h) == om]
                if len(pick) != 1:
                    poles += 1
                    f[T] = (x + y + z) * inv(3) % p  # centroid (variant P1 patch)
                    assert variant == "P1", "pole outside the (4,0) orbit"
                else:
                    f[T] = pick[0]
            rec["poles_patched"] = poles
            # injectivity for every copy-0 pair, leftover sets
            coll = 0
            left0 = None
            for P in combinations(range(p), 2):
                vals = [f[tuple(sorted(P + (z,)))] for z in range(p)
                        if z not in P and tuple(sorted(P + (z,))) in f]
                if len(vals) != len(set(vals)):
                    coll += 1
                if P == (0, 1):
                    left0 = sorted(set(range(p)) - set(vals))
                    rec["pair01_values"] = len(vals)
            rec["pairs_with_collisions"] = coll
            rec["L0_01"] = left0
            rec["sqs_found"] = []
            if coll == 0 and len(left0) % 2 == 0:
                def Phi(Q):
                    q1, q2 = Q
                    if chi(q1 - q2) != 1:
                        q1, q2 = q2, q1
                    d = inv(q1 - q2)
                    return tuple(sorted((q1 * d % p, (q1 - 1) * d % p)))
                def pairings(s):
                    if not s:
                        yield []
                        return
                    a = s[0]
                    for j in range(1, len(s)):
                        rest = s[1:j] + s[j + 1:]
                        for r in pairings(rest):
                            yield [(a, s[j])] + r
                inv_pairings = [pr for pr in pairings(left0)
                                if all(Phi(Q) in {tuple(sorted(q)) for q in pr} for Q in pr)]
                rec["phi_invariant_pairings"] = [[list(q) for q in pr] for pr in inv_pairings]
                for pr in inv_pairings:
                    blocks = set()
                    for T, h in f.items():
                        blocks.add(tuple(sorted([(t, 0) for t in T] + [(h, 1)])))
                        blocks.add(tuple(sorted([((-t) % p, 1) for t in T] + [((-h) % p, 0)])))
                    for B in forty:
                        blocks.add(tuple((t, 0) for t in B))
                        blocks.add(tuple(sorted(((-t) % p, 1) for t in B)))
                    for a, b in A:
                        P = tuple(sorted(((a * 0 + b) % p, (a * 1 + b) % p)))
                        for q1, q2 in pr:
                            Q = sorted(((a * q1 + b) % p, (a * q2 + b) % p))
                            blocks.add(tuple(sorted([(P[0], 0), (P[1], 0), (Q[0], 1), (Q[1], 1)])))
                    cnt = {}
                    for B in blocks:
                        for t in combinations(B, 3):
                            cnt[t] = cnt.get(t, 0) + 1
                    n = 2 * p
                    ok = (len(blocks) == n * (n - 1) * (n - 2) // 24 and len(cnt) == n * (n - 1) * (n - 2) // 6
                          and all(v == 1 for v in cnt.values()))
                    rec["sqs_found"].append({"pairing": [list(q) for q in pr], "blocks": len(blocks), "is_sqs": ok})
            res["variants"].append(rec)
            print(json.dumps({k: rec[k] for k in rec if k not in ("phi_invariant_pairings",)}), flush=True)
    json.dump(res, open(out, "w"), indent=1)


if __name__ == "__main__":
    main()
