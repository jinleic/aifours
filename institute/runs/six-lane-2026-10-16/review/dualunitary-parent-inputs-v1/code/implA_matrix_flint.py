"""Implementation A: exact linearization of dual / T-dual unitarity in the MATRIX picture (source conventions).

Real coordinates of X in M_n(C), n = d^2: x = (Re X row-major, Im X row-major) in R^{2 n^2}.
Linear map for a list of reshapings f (identity, R, Gamma, or mutations):
    X -> [ f(P)^dagger f(X) + f(X)^dagger f(P) ]_f      (Re and Im parts of every entry)
All entries are integers for integer P; ranks, nullspaces, products and determinants are exact (python-flint
fmpz_mat). Orbit tangent: (A1 (x) I + I (x) A2) P + P (A3 (x) I + I (x) A4), A_k in a Z-basis of u(d).

python -B implA_matrix_flint.py --out ../evidence/implA.json --kernel-dir ../evidence/implA_kernels
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import random
import sys
import time

import flint
from flint import fmpz_mat

from perms import PERMS

PRIME = 2305843009213693951  # 2^61 - 1


# ---------------------------------------------------------------- complex integer matrices as (Re, Im) fmpz_mat
def zeros(n):
    return fmpz_mat(n, n)


def perm_mat(n, ones):
    M = fmpz_mat(n, n)
    for r, c in ones:
        M[r, c] = 1
    return M


def eye(n):
    M = fmpz_mat(n, n)
    for i in range(n):
        M[i, i] = 1
    return M


def cmul(A, B):
    return (A[0] * B[0] - A[1] * B[1], A[0] * B[1] + A[1] * B[0])


def cadd(A, B):
    return (A[0] + B[0], A[1] + B[1])


def dag(A):
    return (A[0].transpose(), -A[1].transpose())


def kron(A, B):
    """real Kronecker product of fmpz_mat A (a x a) and B (b x b)."""
    a, b = A.nrows(), B.nrows()
    K = fmpz_mat(a * b, a * b)
    for i in range(a):
        for j in range(a):
            x = A[i, j]
            if x != 0:
                for k in range(b):
                    for l in range(b):
                        y = B[k, l]
                        if y != 0:
                            K[i * b + k, j * b + l] = x * y
    return K


def ckron(A, B):  # complex (A0 + i A1) (x) (B0 + i B1)
    return (kron(A[0], B[0]) - kron(A[1], B[1]), kron(A[0], B[1]) + kron(A[1], B[0]))


# ---------------------------------------------------------------- reshapings (source definitions, eqs. (i), (ii))
def realign(M, d):          # <ij|U^R|ab> = <ia|U|jb>
    n = d * d
    R = fmpz_mat(n, n)
    for i, j, a, b in itertools.product(range(d), repeat=4):
        R[d * i + j, d * a + b] = M[d * i + a, d * j + b]
    return R


def ptrans(M, d):           # <ib|U^G|ja> = <ia|U|jb>
    n = d * d
    G = fmpz_mat(n, n)
    for i, j, a, b in itertools.product(range(d), repeat=4):
        G[d * i + b, d * j + a] = M[d * i + a, d * j + b]
    return G


def ident(M, d):
    return M


def wrong_trivial(M, d):    # MUTATION: <ij|W|ab> = <ij|U|ba>  (column relabelling only = cut 12|34 again)
    n = d * d
    W = fmpz_mat(n, n)
    for i, j, a, b in itertools.product(range(d), repeat=4):
        W[d * i + j, d * a + b] = M[d * i + j, d * b + a]
    return W


def realign_variant(M, d):  # equivalent reshaping of the same cut: <ij|V|ab> = <ai|U|bj> = (U^R)^T
    n = d * d
    V = fmpz_mat(n, n)
    for i, j, a, b in itertools.product(range(d), repeat=4):
        V[d * i + j, d * a + b] = M[d * a + i, d * b + j]
    return V


RESHAPES = {"id": ident, "R": realign, "G": ptrans, "W_trivial": wrong_trivial, "R_variant": realign_variant}


def creshape(f, A, d):
    return (f(A[0], d), f(A[1], d))


def is_unitary(A):
    n = A[0].nrows()
    H = cmul(dag(A), A)
    return H[0] == eye(n) and H[1] == zeros(n)


# ---------------------------------------------------------------- the linear maps
def vec(A):
    return [int(x) for x in A[0].entries()] + [int(x) for x in A[1].entries()]


def basis_matrix(n, k):
    """k-th real basis element of M_n(C) in our coordinates."""
    E = fmpz_mat(n, n)
    if k < n * n:
        E[k // n, k % n] = 1
        return (E, zeros(n))
    k -= n * n
    E[k // n, k % n] = 1
    return (zeros(n), E)


def linearization(P, d, shapes):
    """integer matrix (rows = constraints, cols = 2n^2 coordinates) of X -> [f(P)^+ f(X) + f(X)^+ f(P)]_f."""
    n = d * d
    fP = [creshape(RESHAPES[s], P, d) for s in shapes]
    cols = []
    for k in range(2 * n * n):
        X = basis_matrix(n, k)
        col = []
        for s, Pf in zip(shapes, fP):
            Xf = creshape(RESHAPES[s], X, d)
            H = cadd(cmul(dag(Pf), Xf), cmul(dag(Xf), Pf))
            col += vec(H)
        cols.append(col)
    return fmpz_mat(cols).transpose()


def u_basis(d):
    """Z-basis of u(d): i E_kk, E_kl - E_lk, i(E_kl + E_lk)."""
    out = []
    for k in range(d):
        Ai = fmpz_mat(d, d)
        Ai[k, k] = 1
        out.append(("iE%d%d" % (k, k), (fmpz_mat(d, d), Ai)))
    for k in range(d):
        for l in range(k + 1, d):
            Ar = fmpz_mat(d, d)
            Ar[k, l], Ar[l, k] = 1, -1
            out.append(("A%d%d" % (k, l), (Ar, fmpz_mat(d, d))))
            Ai = fmpz_mat(d, d)
            Ai[k, l], Ai[l, k] = 1, 1
            out.append(("S%d%d" % (k, l), (fmpz_mat(d, d), Ai)))
    return out


def orbit_tangent(P, d):
    I = (eye(d), fmpz_mat(d, d))
    cols, labels = [], []
    for name, A in u_basis(d):
        for slot in range(4):
            if slot == 0:
                T = cmul(ckron(A, I), P)
            elif slot == 1:
                T = cmul(ckron(I, A), P)
            elif slot == 2:
                T = cmul(P, ckron(A, I))
            else:
                T = cmul(P, ckron(I, A))
            cols.append(vec(T))
            labels.append("%s@%d" % (name, slot))
    return fmpz_mat(cols).transpose(), labels


def enphasing_tangent(P, d):
    """tangent vectors i*E_rr*P (left enphasing by diagonal phases)."""
    n = d * d
    cols = []
    for r in range(n):
        E = fmpz_mat(n, n)
        E[r, r] = 1
        cols.append(vec(cmul((fmpz_mat(n, n), E), P)))
    return fmpz_mat(cols).transpose()


# ---------------------------------------------------------------- certificates
def modp_pivots(rows, ncols, p):
    """row-echelon over GF(p); returns pivot columns (in order) and the rank."""
    piv = {}
    order = []
    for r in rows:
        row = {c: v % p for c, v in enumerate(r) if v % p}
        while row:
            c = min(row)
            if c in piv:
                f = row[c]
                for cc, vv in piv[c].items():
                    row[cc] = (row.get(cc, 0) - f * vv) % p
                    if row[cc] == 0:
                        del row[cc]
            else:
                inv = pow(row[c], p - 2, p)
                piv[c] = {cc: vv * inv % p for cc, vv in row.items()}
                order.append(c)
                break
    return order, len(piv)


def minor_certificate(M, p=PRIME):
    """rows/cols of a nonsingular maximal minor and its exact integer determinant (nonzero => rank >= r)."""
    rows = [[int(x) for x in M.row(i)] if hasattr(M, "row") else None for i in range(M.nrows())]
    if rows[0] is None:
        rows = [[int(M[i, j]) for j in range(M.ncols())] for i in range(M.nrows())]
    pcols, r = modp_pivots(rows, M.ncols(), p)
    pcols = sorted(pcols)
    sub_t = [[rows[i][c] for i in range(M.nrows())] for c in pcols]   # transpose of M[:, pcols]
    prows, r2 = modp_pivots(sub_t, M.nrows(), p)
    prows = sorted(prows)
    assert r2 == r
    S = fmpz_mat([[rows[i][c] for c in pcols] for i in prows])
    det = S.det()
    return {"r": r, "rows": prows, "cols": pcols, "det": str(det), "det_nonzero": det != 0,
            "det_bits": int(abs(int(det))).bit_length()}


def sha(M):
    return hashlib.sha256(json.dumps([int(x) for x in M.entries()]).encode()).hexdigest()


def analyse(name, d, ones, shapes, want_minor=True, kernel_dir=None):
    n = d * d
    P = (perm_mat(n, ones), zeros(n))
    rec = {"perm": name, "d": d, "ones": ones, "shapes": shapes}
    rec["unitary"] = {s: is_unitary(creshape(RESHAPES[s], P, d)) for s in ("id", "R", "G")}
    t0 = time.time()
    M = linearization(P, d, shapes)
    rank_M = M.rank()
    T, labels = orbit_tangent(P, d)
    rank_T = T.rank()
    MT = M * T
    incl = all(x == 0 for x in MT.entries())
    rec.update({"rows": M.nrows(), "cols": M.ncols(), "rank": int(rank_M), "kernel_dim": int(M.ncols() - rank_M),
                "orbit_tangent_rank": int(rank_T), "orbit_tangent_in_kernel": incl, "M_sha256": sha(M)})
    E = enphasing_tangent(P, d)
    ME = M * E
    rec["enphasing_in_kernel"] = all(x == 0 for x in ME.entries())
    TE = fmpz_mat([[T[i, j] for j in range(T.ncols())] + [E[i, j] for j in range(E.ncols())] for i in range(T.nrows())])
    rec["rank_tangent_plus_enphasing"] = int(TE.rank())
    if want_minor:
        rec["minor_certificate"] = minor_certificate(M)
        rec["tangent_minor_certificate"] = minor_certificate(T)
    rec["certified_kernel_equals_orbit_tangent"] = bool(incl and (M.ncols() - rank_M) == rank_T)
    if kernel_dir:
        try:
            N, nullity = M.nullspace()
            basis = [[int(N[i, j]) for i in range(N.nrows())] for j in range(int(nullity))]
        except Exception as e:  # pragma: no cover
            basis, nullity = [], -1
            rec["nullspace_error"] = repr(e)
        os.makedirs(kernel_dir, exist_ok=True)
        path = os.path.join(kernel_dir, "%s_%s.json" % (name, "-".join(shapes)))
        json.dump({"perm": name, "d": d, "shapes": shapes, "coords": "x = (Re X row-major, Im X row-major); X[(k,l),(i,j)]",
                   "basis": basis}, open(path, "w"))
        rec["kernel_basis_file"] = path
        rec["nullity_flint"] = int(nullity)
    rec["secs"] = round(time.time() - t0, 2)
    return rec


def local_perm_search(d, ones_src, ones_dst):
    """find local permutations (pi1,pi2,pi3,pi4) with dst = (Pi1 x Pi2) src (Pi3 x Pi4) as maps (exhaustive)."""
    src = {c: r for r, c in ones_src}
    dst = {c: r for r, c in ones_dst}
    for p1, p2, p3, p4 in itertools.product(itertools.permutations(range(d)), repeat=4):
        ok = True
        for i in range(d):
            for j in range(d):
                # column (i,j) of (Pi1xPi2) src (Pi3xPi4): input |ij> -> (Pi3xPi4)|ij> = |p3[i] p4[j]> -> src -> out
                c = d * p3[i] + p4[j]
                r = src[c]
                k, l = divmod(r, d)
                rr = d * p1[k] + p2[l]
                if dst[d * i + j] != rr:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return [list(p1), list(p2), list(p3), list(p4)]
    return None


def swap_identity_check(d, trials=3, seed=0):
    """exact check of (U S)^R = U^G S on random integer complex matrices."""
    rnd = random.Random(seed)
    n = d * d
    S = perm_mat(n, [(d * j + i, d * i + j) for i in range(d) for j in range(d)])
    Sc = (S, zeros(n))
    for _ in range(trials):
        U = (fmpz_mat([[rnd.randint(-5, 5) for _ in range(n)] for _ in range(n)]),
             fmpz_mat([[rnd.randint(-5, 5) for _ in range(n)] for _ in range(n)]))
        lhs = creshape(realign, cmul(U, Sc), d)
        rhs = cmul(creshape(ptrans, U, d), Sc)
        if lhs != rhs:
            return False
    return True


def lu_covariance_check(d, trials=2, seed=1):
    """exact check: ((v1 x v2) U (v3 x v4))^R = (v1 x v3^T) U^R (v2^T x v4) and
       ((v1 x v2) U (v3 x v4))^G = (v1 x v4^T) U^G (v3 x v2^T), random integer complex v_k, U."""
    rnd = random.Random(seed)
    n = d * d

    def rm(m):
        return (fmpz_mat([[rnd.randint(-3, 3) for _ in range(m)] for _ in range(m)]),
                fmpz_mat([[rnd.randint(-3, 3) for _ in range(m)] for _ in range(m)]))

    def T(A):
        return (A[0].transpose(), A[1].transpose())
    for _ in range(trials):
        v1, v2, v3, v4, U = rm(d), rm(d), rm(d), rm(d), rm(n)
        Up = cmul(cmul(ckron(v1, v2), U), ckron(v3, v4))
        if creshape(realign, Up, d) != cmul(cmul(ckron(v1, T(v3)), creshape(realign, U, d)), ckron(T(v2), v4)):
            return False
        if creshape(ptrans, Up, d) != cmul(cmul(ckron(v1, T(v4)), creshape(ptrans, U, d)), ckron(v3, T(v2))):
            return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--kernel-dir", default=None)
    ap.add_argument("--skip-d4", action="store_true")
    a = ap.parse_args()
    t0 = time.time()
    out = {"implementation": "A (matrix picture, python-flint %s)" % flint.__version__,
           "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "perms_sha256": hashlib.sha256(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "perms.py"), "rb").read()).hexdigest(),
           "python": sys.version.split()[0], "runs": []}
    d3, c7 = PERMS["C7"]
    out["C7_equals_closed_form"] = sorted(c7) == sorted(PERMS["closed_form_C7"][1])
    out["lu_covariance_identities_exact"] = lu_covariance_check(3)
    out["swap_identity_(US)^R=U^G S_exact"] = swap_identity_check(3)
    out["local_relabelings_to_C7"] = {}
    for name in ("eq14", "verbal_secIIIA", "ref44_A14"):
        out["local_relabelings_to_C7"][name] = local_perm_search(3, c7, PERMS[name][1])
    S9 = [(3 * j + i, 3 * i + j) for i in range(3) for j in range(3)]
    c7S = sorted((r, s_c) for (r, c) in c7 for (s_r, s_c) in S9 if s_r == c)   # P9 * S
    out["P9_times_S"] = c7S
    out["P9_times_S_local_relabeling_of_C7"] = local_perm_search(3, c7, c7S)
    jobs = [("C7", ["id", "R"]), ("C7", ["id", "G"]),
            ("eq14", ["id", "R"]), ("eq14", ["id", "G"]),
            ("verbal_secIIIA", ["id", "R"]), ("verbal_secIIIA", ["id", "G"]),
            ("ref44_A14", ["id", "R"]), ("ref44_A14", ["id", "G"]),
            ("C7", ["id", "R", "G"]),
            ("C7", ["id"]),
            ("C7", ["id", "W_trivial"]),          # mutation: must change the rank
            ("C7", ["id", "R_variant"]),          # equivalent reshaping: must not
            ("dual_not_tdual", ["id", "R"])]
    if not a.skip_d4:
        jobs += [("P16_gf4", ["id", "R"]), ("P16_gf4", ["id", "G"])]
    for name, shapes in jobs:
        d, ones = PERMS[name]
        rec = analyse(name, d, ones, shapes, want_minor=(d == 3), kernel_dir=a.kernel_dir if name in ("C7", "P16_gf4") else None)
        out["runs"].append(rec)
        print(json.dumps({k: rec[k] for k in ("perm", "shapes", "unitary", "rank", "kernel_dim", "orbit_tangent_rank",
                                                "orbit_tangent_in_kernel", "enphasing_in_kernel",
                                                "rank_tangent_plus_enphasing", "certified_kernel_equals_orbit_tangent", "secs")}),
              flush=True)
    out["secs"] = round(time.time() - t0, 1)
    json.dump(out, open(a.out, "w"), indent=1)


if __name__ == "__main__":
    main()
