#!/usr/bin/env python3
"""H^1 twist classes for an untwisted symmetry group G of (Z_n, k; 1) difference matrices, n SQUAREFREE
(sub-lane cfr21, worker InfoCFR27Lift; notes/facts-c21-v1.md T-section).

Usage: twist_h1_c21v1.py SPEC.json OUT.json        (OUT written with mode 'x')
SPEC: {"n", "k", "gens": [[mu, pi], ...]}  (pi[i] = image of row i; action (s c)_x = mu c_{pi^-1(x)}).
A twisted group replaces each generator s_j by (mu_j, pi_j, t_j) acting by (s c)_x = mu c_{pi^-1(x)} + t_x, t modulo the
diagonal. The assignment s_j -> t_j extends to a group action of the same group iff it is a 1-cocycle
c: G -> M = Z_n^k / diag (c(gh) = c(g) + L_g c(h), L_g t_x = mu_g t_{pi_g^-1(x)}); conjugating the DM by a row
translation u changes c by the coboundary g -> (L_g - 1) u. Twisted models up to such conjugation = H^1(G, M).
Method: Z_n = prod GF(p) (CRT, n squarefree). BFS over G by left multiplication with generators expresses every c(g)
as a linear function of the generator twists (normalised t_j[0] = 0); every second path to an element gives linear
equations (taken modulo the diagonal). Z^1 = kernel over GF(p); B^1 = image of u -> ((L_{s_j} - 1) u)_j; H^1 = Z^1/B^1.
Output: dimensions per prime and one representative generator-twist list per class (all p-combinations of a basis of
a complement of B^1 in Z^1, combined by CRT); class 0 is the untwisted group.
"""
import itertools, json, sys


def factor_squarefree(n):
    ps, m, d = [], n, 2
    while d * d <= m:
        if m % d == 0:
            ps.append(d)
            m //= d
            if m % d == 0:
                raise SystemExit("n is not squarefree")
        d += 1
    if m > 1:
        ps.append(m)
    return ps


def rref_mod(rows, ncols, p):
    """Row-reduce a list of rows (lists mod p); return (reduced rows, pivot columns)."""
    A = [r[:] for r in rows]
    piv, r = [], 0
    for c in range(ncols):
        pr = next((i for i in range(r, len(A)) if A[i][c] % p), None)
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        inv = pow(A[r][c], -1, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] % p:
                f = A[i][c]
                A[i] = [(a - f * b) % p for a, b in zip(A[i], A[r])]
        piv.append(c)
        r += 1
        if r == len(A):
            break
    return A[:r], piv


def nullspace_mod(rows, ncols, p):
    R, piv = rref_mod(rows, ncols, p) if rows else ([], [])
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for f in free:
        v = [0] * ncols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-R[i][f]) % p
        basis.append(v)
    return basis


def main():
    spec_bytes = open(sys.argv[1], "rb").read()
    spec = json.loads(spec_bytes)
    n, k = spec["n"], spec["k"]
    gens = [(g[0] % n, tuple(g[1])) for g in spec["gens"]]
    r = len(gens)
    primes = factor_squarefree(n)

    def inv(p):
        q = [0] * k
        for i, x in enumerate(p):
            q[x] = i
        return tuple(q)

    def mul(a, b):  # a after b
        return ((a[0] * b[0]) % n, tuple(a[1][b[1][i]] for i in range(k)))

    def Lmat(g):
        """k x k matrix of L_g: (L t)_x = mu t_{pi^-1(x)}."""
        mu, p = g
        pi_inv = inv(p)
        M = [[0] * k for _ in range(k)]
        for x in range(k):
            M[x][pi_inv[x]] = mu % n
        return M

    nv = r * (k - 1)                     # unknowns: t_j[1..k-1]

    def sel(j):
        """k x nv matrix selecting t_j (row 0 = 0)."""
        M = [[0] * nv for _ in range(k)]
        for x in range(1, k):
            M[x][j * (k - 1) + (x - 1)] = 1
        return M

    def matmul(A, B):
        return [[sum(A[i][l] * B[l][j] for l in range(len(B))) % n for j in range(len(B[0]))] for i in range(len(A))]

    def matadd(A, B):
        return [[(a + b) % n for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]

    def normrows(A):  # N(v) = v - v_0 * 1 applied column-wise to a k x nv matrix
        return [[(A[x][j] - A[0][j]) % n for j in range(nv)] for x in range(k)]

    ident = (1, tuple(range(k)))
    C = {ident: [[0] * nv for _ in range(k)]}
    order = [ident]
    eqs = []
    q = 0
    while q < len(order):
        h = order[q]
        q += 1
        for j, s in enumerate(gens):
            g = mul(s, h)
            cand = normrows(matadd(sel(j), matmul(Lmat(s), C[h])))
            if g not in C:
                C[g] = cand
                order.append(g)
            else:
                diff = normrows([[(a - b) % n for a, b in zip(ra, rb)] for ra, rb in zip(C[g], cand)])
                for x in range(1, k):
                    if any(diff[x]):
                        eqs.append(diff[x])
        if len(order) > 5000:
            raise SystemExit("group too large")
    out = {"spec": sys.argv[1], "n": n, "k": k, "gens": [[g[0], list(g[1])] for g in gens], "group_order": len(order),
           "primes": {}, "classes": []}
    per_prime_reps = {}
    for p in primes:
        rows = [[x % p for x in e] for e in eqs]
        Z = nullspace_mod(rows, nv, p)
        # coboundaries: t_j = N((L_{s_j} - 1) u), u in GF(p)^k
        Bvecs = []
        for x0 in range(k):
            u = [0] * k
            u[x0] = 1
            v = []
            for s in gens:
                mu, pp = s
                pinv = inv(pp)
                Lu = [(mu * u[pinv[x]]) % n for x in range(k)]
                d = [(Lu[x] - u[x]) for x in range(k)]
                d = [(d[x] - d[0]) for x in range(k)]
                v.extend(d[1:])
            Bvecs.append([x % p for x in v])
        Bred, _ = rref_mod(Bvecs, nv, p)
        dimB = len(Bred)
        dimZ = len(Z)
        # check B in Z: every B vector satisfies the equations
        for b in Bred:
            for e in rows:
                if sum(a * c for a, c in zip(e, b)) % p:
                    raise SystemExit("INTERNAL: coboundary violates cocycle equations mod %d" % p)
        # complement of B in Z
        comp, cur = [], [b[:] for b in Bred]
        curdim = dimB
        for z in Z:
            test, _ = rref_mod(cur + [z], nv, p)
            if len(test) > curdim:
                comp.append(z)
                cur = cur + [z]
                curdim += 1
        if dimB + len(comp) != dimZ:
            raise SystemExit("INTERNAL: complement dimension")
        out["primes"][str(p)] = {"dim_Z1": dimZ, "dim_B1": dimB, "dim_H1": len(comp), "equations": len(rows)}
        reps = []
        for coefs in itertools.product(range(p), repeat=len(comp)):
            v = [0] * nv
            for a, w in zip(coefs, comp):
                v = [(x + a * y) % p for x, y in zip(v, w)]
            reps.append(v)
        per_prime_reps[p] = reps
    # CRT combine
    for combo in itertools.product(*[per_prime_reps[p] for p in primes]):
        v = [0] * nv
        for idx in range(nv):
            # x = combo[p] mod p for each p
            x = 0
            for p, vp in zip(primes, combo):
                m = n // p
                x = (x + vp[idx] * m * pow(m, -1, p)) % n
            v[idx] = x
        tw = []
        for j in range(r):
            tw.append([0] + v[j * (k - 1):(j + 1) * (k - 1)])
        out["classes"].append({"generator_twists": tw, "trivial": not any(v)})
    out["num_classes"] = len(out["classes"])
    with open(sys.argv[2], "x") as fh:
        json.dump(out, fh)
    print(json.dumps({"order": out["group_order"], "primes": out["primes"], "num_classes": out["num_classes"]}))


if __name__ == "__main__":
    main()
