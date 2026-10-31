#!/usr/bin/env python3
"""reviewer-f173-controls-v1.py -- reviewer-authored exact controls.

Wave: f173-kacmoody-whole-seed-lowest-projection (reviewer ReviewF173IdealProjection).
Independent toy implementation of the reviewed lemma's MECHANISM only.  It reads no
author code, author data, held/ZERO payload or sibling review; it uses only the Python
standard library with exact rationals (fractions.Fraction).

Toy models
  (A) l = sl2 acting on M = sl2 (adjoint; letters f, h, e), seeds = lowest vectors of
      the V4 and V2 components of L_3(M); levels 4..6.
  (B) l = sl3 acting on M = sl3 (adjoint) in the candidate's displayed basis
      B = (E31,-E32,E21,E11-E33,E11-E22,-E12,-E23,-2E13) with the Frobenius form;
      toy seed = lowest vector of the adjoint copy V(1,1) inside L_2(M) (root degree
      (1,1,2); NOT a node-3 Serre seed); levels 3..4.
L_n(M) is realised as the span of right-nested commutators inside M^(tensor n).
The ideal is recomputed by brute force (brackets with arbitrary Lie elements, both
orders, all seed modules) independently of the nested-letter description.
No actual Serre-quotient rank, Gram/cross matrix of the actual problem, determinant,
grade-7, B7 or all-level quantity is computed.
"""
import sys
import time
from fractions import Fraction as Fr
from itertools import product

ZERO, ONE = Fr(0), Fr(1)
POS, NEG = [], []


def pos(name, ok, detail=""):
    POS.append((name, bool(ok)))
    print(f"POS {'PASS' if ok else 'FAIL'} | {name} | {detail}", flush=True)


def neg(name, detected, reason_ok, detail=""):
    NEG.append((name, bool(detected), bool(reason_ok)))
    print(f"NEG {'DETECTED' if detected else 'NOT-DETECTED'} "
          f"reason={'CONFIRMED' if reason_ok else 'UNCONFIRMED'} | {name} | {detail}", flush=True)


def info(msg):
    print(f"INFO | {msg}", flush=True)


# ---------------------------------------------------------------- linear algebra
def vadd(a, b, s=ONE):
    r = dict(a)
    for k, v in b.items():
        nv = r.get(k, ZERO) + s * v
        if nv:
            r[k] = nv
        else:
            r.pop(k, None)
    return r


def vscale(a, s):
    return {k: s * v for k, v in a.items()} if s else {}


def lincomb(coeffs, vecs):
    out = {}
    for j, c in coeffs.items():
        if c:
            out = vadd(out, vecs[j], c)
    return out


class Ech:
    """Fully reduced echelon basis; each row's pivot is its minimal key."""

    def __init__(self, vecs=()):
        self.rows = {}
        for v in vecs:
            self.add(v)

    def reduce(self, v):
        r = dict(v)
        for p in [k for k in v if k in self.rows]:
            c = r.get(p)
            if c:
                r = vadd(r, self.rows[p], -c)
        return r

    def add(self, v):
        r = self.reduce(v)
        if not r:
            return False
        p = min(r)
        r = vscale(r, ONE / r[p])
        for q in list(self.rows):
            cq = self.rows[q].get(p)
            if cq:
                self.rows[q] = vadd(self.rows[q], r, -cq)
        self.rows[p] = r
        return True

    def contains(self, v):
        return not self.reduce(v)

    def dim(self):
        return len(self.rows)

    def basis(self):
        return [self.rows[p] for p in sorted(self.rows)]


def same_space(A, B):
    return A.dim() == B.dim() and all(A.contains(v) for v in B.basis())


def contained(A, B):
    return all(B.contains(v) for v in A.basis())


def intersect(Ub, Vb):
    """Zassenhaus: basis of span(Ub) cap span(Vb)."""
    E = Ech()
    for u in Ub:
        w = {(0, k): c for k, c in u.items()}
        w.update({(1, k): c for k, c in u.items()})
        E.add(w)
    for v in Vb:
        E.add({(0, k): c for k, c in v.items()})
    return Ech([{k[1]: c for k, c in row.items()} for p, row in E.rows.items() if p[0] == 1])


def kernel(images):
    """images[j] = image of j-th basis vector; returns kernel coefficient dicts."""
    E = Ech()
    for j, im in enumerate(images):
        w = {(0, k): c for k, c in im.items()}
        w[(1, j)] = ONE
        E.add(w)
    return [{k[1]: c for k, c in row.items()} for p, row in E.rows.items() if p[0] == 1]


def solve(H, b):
    n = len(H)
    A = [list(H[i]) + [b[i]] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        A[col] = [x / pv for x in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[col])]
    return [A[i][n] for i in range(n)]


# ---------------------------------------------------------------- matrices
def munit(N, i, j):
    return tuple(tuple(ONE if (r, c) == (i - 1, j - 1) else ZERO for c in range(N)) for r in range(N))


def madd(A, B, s=ONE):
    return tuple(tuple(a + s * b for a, b in zip(ra, rb)) for ra, rb in zip(A, B))


def msc(A, s):
    return tuple(tuple(Fr(s) * a for a in r) for r in A)


def mmul(A, B):
    N = len(A)
    return tuple(tuple(sum((A[i][k] * B[k][j] for k in range(N)), ZERO) for j in range(N)) for i in range(N))


def mcomm(A, B):
    return madd(mmul(A, B), mmul(B, A), -ONE)


def mT(A):
    return tuple(tuple(r) for r in zip(*A))


def mtr(A):
    return sum((A[i][i] for i in range(len(A))), ZERO)


def mflat(A):
    return {(i, j): A[i][j] for i in range(len(A)) for j in range(len(A)) if A[i][j]}


def coord_fn(basis):
    E = Ech()
    for j, b in enumerate(basis):
        w = {(0, k): c for k, c in mflat(b).items()}
        w[(1, j)] = ONE
        E.add(w)
    assert all(p[0] == 0 for p in E.rows), "dependent basis"

    def coords(X):
        r = E.reduce({(0, k): c for k, c in mflat(X).items()})
        assert all(k[0] == 1 for k in r), "matrix not in span of basis"
        return {k[1]: -c for k, c in r.items()}
    return coords


# ---------------------------------------------------------------- tensor algebra
def letter(i):
    return {(i,): ONE}


def concat(X, Y):
    out = {}
    for w1, c1 in X.items():
        for w2, c2 in Y.items():
            w = w1 + w2
            nv = out.get(w, ZERO) + c1 * c2
            if nv:
                out[w] = nv
            else:
                out.pop(w, None)
    return out


def br(X, Y):
    return vadd(concat(X, Y), concat(Y, X), -ONE)


def nested(us, z):
    """beta(u1,...,uk; z) = ad(u1)...ad(uk) z for letter indices u."""
    v = z
    for u in reversed(us):
        v = br(letter(u), v)
    return v


def deriv(act, X):
    """Letter action extended to tensors as a derivation."""
    out = {}
    for w, c in X.items():
        for t, a in enumerate(w):
            for b, cb in act[a].items():
                w2 = w[:t] + (b,) + w[t + 1:]
                nv = out.get(w2, ZERO) + c * cb
                if nv:
                    out[w2] = nv
                else:
                    out.pop(w2, None)
    return out


def ip(X, Y, nbr):
    """Product form with letter Gram given by neighbour lists (real data)."""
    s = ZERO
    for w, c in X.items():
        partial = [((), ONE)]
        for a in w:
            partial = [(pw + (b,), pc * g) for pw, pc in partial for b, g in nbr[a]]
        for w2, g in partial:
            y = Y.get(w2)
            if y:
                s += c * y * g
    return s


def nbr_of(G):
    N = len(G)
    return [[(j, G[i][j]) for j in range(N) if G[i][j]] for i in range(N)]


class Model:
    def __init__(self, name, basis, Es, Fs, Hs, degfun, weightfun):
        self.name = name
        self.basis = basis
        self.N = len(basis)
        coords = coord_fn(basis)

        def act(X):
            return [dict(coords(mcomm(X, b))) for b in basis]
        self.Emats, self.Fmats, self.Hmats = Es, Fs, Hs
        self.E = [act(X) for X in Es]
        self.F = [act(X) for X in Fs]
        self.H = [act(X) for X in Hs]
        self.r = len(Es)
        self.G = [[mtr(mmul(mT(bi), bj)) for bj in basis] for bi in basis]
        self.nbr = nbr_of(self.G)
        lam = []
        for j in range(self.N):
            lj = []
            for Ha in self.H:
                img = Ha[j]
                assert set(img) <= {j}, "basis letter is not a weight vector"
                lj.append(img.get(j, ZERO))
            lam.append(tuple(lj))
        self.lam = lam
        self.deg = [degfun(l) for l in lam]
        self.weightfun = weightfun
        self._seqs = {}
        self._L = {}

    def wdeg(self, w):
        D = [0] * self.r
        for a in w:
            for i in range(self.r):
                D[i] += self.deg[a][i]
        return tuple(D)

    def vdeg(self, v):
        ds = {self.wdeg(w) for w in v}
        assert len(ds) == 1, "inhomogeneous vector"
        return ds.pop()

    def seqs(self, k):
        if k not in self._seqs:
            d = {}
            for s in product(range(self.N), repeat=k):
                d.setdefault(self.wdeg(s), []).append(s)
            self._seqs[k] = d
        return self._seqs[k]

    def L(self, n, D):
        key = (n, D)
        if key not in self._L:
            E = Ech()
            for s in self.seqs(n).get(D, []):
                E.add(nested(s[:-1], letter(s[-1])))
            self._L[key] = E
        return self._L[key]

    def antidominant(self, D, n):
        return all(x <= 0 for x in self.weightfun(D, n))

    def lower(self, D, i):
        return tuple(D[t] - (1 if t == i else 0) for t in range(self.r))

    def raise_(self, D, i):
        return tuple(D[t] + (1 if t == i else 0) for t in range(self.r))


def as_int(x):
    x = Fr(x)
    assert x.denominator == 1, x
    return int(x)


def build_sl2():
    e, f = munit(2, 1, 2), munit(2, 2, 1)
    h = madd(munit(2, 1, 1), munit(2, 2, 2), -ONE)
    return Model("sl2", [f, h, e], [e], [f], [h],
                 degfun=lambda l: (as_int((l[0] + 2) / 2),),
                 weightfun=lambda D, n: (2 * D[0] - 2 * n,))


def build_sl3():
    U = lambda i, j: munit(3, i, j)
    B = [U(3, 1), msc(U(3, 2), -1), U(2, 1), madd(U(1, 1), U(3, 3), -ONE),
         madd(U(1, 1), U(2, 2), -ONE), msc(U(1, 2), -1), msc(U(2, 3), -1), msc(U(1, 3), -2)]
    e1, e2, f1, f2 = U(1, 2), U(2, 3), U(2, 1), U(3, 2)
    h1, h2 = madd(U(1, 1), U(2, 2), -ONE), madd(U(2, 2), U(3, 3), -ONE)
    return Model("sl3", B, [e1, e2], [f1, f2], [h1, h2],
                 degfun=lambda l: (as_int((2 * l[0] + l[1] + 3) / 3), as_int((l[0] + 2 * l[1] + 3) / 3)),
                 weightfun=lambda D, n: (2 * D[0] - D[1] - n, -D[0] + 2 * D[1] - n))


# ---------------------------------------------------------------- lemma objects
def lowest(m, n, D):
    """P = ker F_1 cap ... cap ker F_r on L_n(M) at root degree D."""
    Lb = m.L(n, D).basis()
    imgs = []
    for y in Lb:
        im = {}
        for i, Fa in enumerate(m.F):
            for w, c in deriv(Fa, y).items():
                im[(i, w)] = c
        imgs.append(im)
    return [lincomb(c, Lb) for c in kernel(imgs)]


class Proj:
    """Orthogonal projection onto span(Pb) for the product form given by nbr."""

    def __init__(self, Pb, nbr):
        self.Pb, self.nbr = Pb, nbr
        self.H = [[ip(x, y, nbr) for y in Pb] for x in Pb]
        self.checked = 0

    def __call__(self, y):
        if not self.Pb:
            return {}
        b = [ip(x, y, self.nbr) for x in self.Pb]
        p = lincomb(dict(enumerate(solve(self.H, b))), self.Pb)
        resid = vadd(y, p, -ONE)
        assert all(ip(x, resid, self.nbr) == 0 for x in self.Pb), "projection residual not orthogonal"
        self.checked += 1
        return p


def raise_closure(m, q):
    """U(n_+) q as degree -> Ech (span of E-words applied to q)."""
    spaces, frontier = {}, [q]
    while frontier:
        new = []
        for v in frontier:
            E = spaces.setdefault(m.vdeg(v), Ech())
            if E.add(v):
                for Ea in m.E:
                    w = deriv(Ea, v)
                    if w:
                        new.append(w)
        frontier = new
    return spaces


def mod_dim(mod):
    return sum(E.dim() for E in mod.values())


def full_L(m, j):
    return [(D, v) for D in sorted(m.seqs(j)) for v in m.L(j, D).basis()]


def brute_ideal(m, mods, n_max, top_degrees=None):
    """Ideal of L(M) generated by the given seed modules, by brute recursion
    I_lev = (seeds at lev) + sum_j [L_j, I_{lev-j}] + [I_{lev-j}, L_j]."""
    d_min = min(d for d, _ in mods)
    I = {}
    for lev in range(d_min, n_max + 1):
        sp = {}
        restrict = (lev == n_max and top_degrees is not None)
        for d, mod in mods:
            if d == lev:
                for D, E in mod.items():
                    if restrict and D not in top_degrees:
                        continue
                    for v in E.basis():
                        sp.setdefault(D, Ech()).add(v)
        for j in range(1, lev - d_min + 1):
            prev = I.get(lev - j, {})
            if not prev:
                continue
            for Dl, x in full_L(m, j):
                for Dp, Ep in prev.items():
                    D = tuple(a + b for a, b in zip(Dl, Dp))
                    if restrict and D not in top_degrees:
                        continue
                    E = sp.setdefault(D, Ech())
                    for z in Ep.basis():
                        E.add(br(x, z))
                        E.add(br(z, x))
        I[lev] = sp
    return I


def getter(I):
    empty = Ech()
    return lambda n, D: I.get(n, {}).get(D, empty)


def nested_span(m, n, D, mods):
    """Candidate's description: span{ beta(u;z) : u in B^(n-d), z in seed module }."""
    E = Ech()
    for d, mod in mods:
        k = n - d
        if k < 0:
            continue
        for Dz, Ez in mod.items():
            Du = tuple(a - b for a, b in zip(D, Dz))
            for u in m.seqs(k).get(Du, []):
                for z in Ez.basis():
                    E.add(nested(u, z))
    return E


def proj_family(m, n, D, seeds, proj, filt=None):
    """span{ Pi_P beta(u; q) : degree-matching ordered tuples u } over the given seeds."""
    E = Ech()
    for d, q in seeds:
        k = n - d
        if k < 0:
            continue
        Du = tuple(a - b for a, b in zip(D, m.vdeg(q)))
        for u in m.seqs(k).get(Du, []):
            if filt is not None and not filt(u):
                continue
            E.add(proj(nested(u, q)))
    return E


def quotient_lowest_dim(m, n, D, Iget):
    """Direct count of lowest vectors of degree D in L_n/I_n (no projection used)."""
    Lb = m.L(n, D).basis()
    imgs = []
    for y in Lb:
        im = {}
        for i, Fa in enumerate(m.F):
            rem = Iget(n, m.lower(D, i)).reduce(deriv(Fa, y))
            for w, c in rem.items():
                im[(i, w)] = c
        imgs.append(im)
    Z = Ech([lincomb(c, Lb) for c in kernel(imgs)])
    assert contained(Iget(n, D), Z), "ideal not F-stable?"
    return Z.dim() - Iget(n, D).dim()


def orth_complement(m, n, D, Wb, nbr):
    Lb = m.L(n, D).basis()
    imgs = []
    for y in Lb:
        im = {}
        for i, w in enumerate(Wb):
            g = ip(w, y, nbr)
            if g:
                im[i] = g
        imgs.append(im)
    return [lincomb(c, Lb) for c in kernel(imgs)]


def analyze(m, label, n, D, seeds, mods, Iget, nbr, orth=True):
    Pb = lowest(m, n, D)
    if not Pb:
        return None
    proj = Proj(Pb, nbr)
    Ibr = Iget(n, D)
    Nsp = nested_span(m, n, D, mods)
    ok_nested = same_space(Nsp, Ibr)
    S2 = intersect(Pb, Ibr.basis())                 # P cap I by Zassenhaus
    S1 = proj_family(m, n, D, seeds, proj)           # lowest-seed projected family
    S3 = Ech([proj(v) for v in Ibr.basis()])         # Pi_P of the whole ideal component
    ok_proj = same_space(S1, S2) and same_space(S3, S2)
    qd = quotient_lowest_dim(m, n, D, Iget)
    ok_lift = (qd == len(Pb) - S2.dim())
    ok_dec, ok_perp = True, True
    if orth:
        Iperp = orth_complement(m, n, D, Ibr.basis(), nbr)
        PIp = intersect(Pb, Iperp)
        ok_dec = (PIp.dim() + S2.dim() == len(Pb))
        for x in Iperp:   # W-perp stability: E_i x and F_i x orthogonal to I at shifted degree
            for i in range(m.r):
                for act, D2 in ((m.E[i], m.raise_(D, i)), (m.F[i], m.lower(D, i))):
                    y = deriv(act, x)
                    if y and any(ip(w, y, nbr) != 0 for w in Iget(n, D2).basis()):
                        ok_perp = False
    ok = ok_nested and ok_proj and ok_lift and ok_dec and ok_perp
    pos(f"{label} n={n} D={D} wt={m.weightfun(D, n)}", ok,
        f"dimL={m.L(n, D).dim()} dimI={Ibr.dim()} dimP={len(Pb)} dim(PnI)={S2.dim()} "
        f"rkS1={S1.dim()} rkPi(I)={S3.dim()} quotient_direct={qd} formula={len(Pb) - S2.dim()} "
        f"nested==brute:{ok_nested} S1==PnI==Pi(I):{ok_proj} lift:{ok_lift} "
        f"P=(PnI)+(PnIperp):{ok_dec} Iperp-stable:{ok_perp}")
    return dict(P=Pb, S1=S1, S2=S2, qd=qd, proj=proj)


def check_transfer(m, label, k, z):
    ok, cnt = True, 0
    for u in product(range(m.N), repeat=k):
        base = nested(u, z)
        for Ea in m.E:
            lhs = nested(u, deriv(Ea, z))
            rhs = deriv(Ea, base)
            for j in range(k):
                for b, cb in Ea[u[j]].items():
                    rhs = vadd(rhs, nested(u[:j] + (b,) + u[j + 1:], z), -cb)
            ok = ok and not vadd(lhs, rhs, -ONE)
            cnt += 1
    pos(f"{label} derivation transfer beta(u;Ez)=E beta(u;z)-sum_j beta(..Eu_j..;z), k={k}", ok,
        f"checked {cnt} (tuple, raising) pairs exactly in T(M)")


def check_PiE(m, label, n, degrees, nbr):
    ok, cnt = True, 0
    for D in degrees:
        Pb = lowest(m, n, D)
        if not Pb:
            continue
        proj = Proj(Pb, nbr)
        for i, Ea in enumerate(m.E):
            Dm = m.lower(D, i)
            if min(Dm) < 0:
                continue
            for y in m.L(n, Dm).basis():
                ok = ok and not proj(deriv(Ea, y))
                cnt += 1
        for D2 in [m.raise_(D, 0), m.lower(D, 0)]:   # other-weight vectors project to zero
            if min(D2) >= 0:
                for y in m.L(n, D2).basis():
                    ok = ok and not proj(y)
                    cnt += 1
    pos(f"{label} Pi_P E_i y = 0 and Pi_P(other weight) = 0 at level {n}", ok, f"checked {cnt} vectors")


# ---------------------------------------------------------------- model A: sl2
def run_sl2():
    t0 = time.perf_counter()
    A = build_sl2()
    info(f"[A] sl2 letters deg={A.deg} Gram={[[str(x) for x in r] for r in A.G]}")
    ok_adj = all(ip(deriv(A.E[0], letter(x)), letter(y), A.nbr) == ip(letter(x), deriv(A.F[0], letter(y)), A.nbr)
                 for x in range(3) for y in range(3))
    pos("[A] adjointness <E x,y>=<x,F y> on M (Frobenius)", ok_adj)

    Pa, Pb_ = lowest(A, 3, (1,)), lowest(A, 3, (2,))
    assert len(Pa) == 1 and len(Pb_) == 1
    qa, qb = Pa[0], Pb_[0]
    Qa, Qb = raise_closure(A, qa), raise_closure(A, qb)
    L3 = sum(A.L(3, D).dim() for D in A.seqs(3))
    pos("[A] seeds: q_a (V4 lowest, wt -4), q_b (V2 lowest, wt -2) in L_3; dim Qa=5, Qb=3, Qa+Qb=L_3",
        mod_dim(Qa) == 5 and mod_dim(Qb) == 3 and L3 == 8, f"dimL3={L3}")

    Ia = brute_ideal(A, [(3, Qa)], 6)
    Ib = brute_ideal(A, [(3, Qb)], 6)
    Iab = brute_ideal(A, [(3, Qa), (3, Qb)], 6)
    ga, gb, gab = getter(Ia), getter(Ib), getter(Iab)
    ok_sum = all(same_space(gab(n, D), Ech(ga(n, D).basis() + gb(n, D).basis()))
                 for n in range(3, 7) for D in A.seqs(n))
    pos("[A] brute ideal(Qa+Qb) == ideal(Qa)+ideal(Qb) at every degree, levels 3..6", ok_sum)

    rec = {}
    for n in (4, 5, 6):
        for D in sorted(A.seqs(n)):
            if not A.antidominant(D, n):
                continue
            ra = analyze(A, "[A] seed a", n, D, [(3, qa)], [(3, Qa)], ga, A.nbr)
            rb = analyze(A, "[A] seed b", n, D, [(3, qb)], [(3, Qb)], gb, A.nbr)
            rab = analyze(A, "[A] seeds a+b", n, D, [(3, qa), (3, qb)], [(3, Qa), (3, Qb)], gab, A.nbr)
            if ra:
                rec[(n, D)] = (ra, rb, rab)

    # mixed-seed brackets at level 6 lie in each single-seed nested-letter span
    ok_mix, cnt = True, 0
    cache = {}
    for Da, Ea in Qa.items():
        for Db, Eb in Qb.items():
            D = (Da[0] + Db[0],)
            if (D, "a") not in cache:
                cache[(D, "a")] = nested_span(A, 6, D, [(3, Qa)])
                cache[(D, "b")] = nested_span(A, 6, D, [(3, Qb)])
            for za in Ea.basis():
                for zb in Eb.basis():
                    v = br(za, zb)
                    ok_mix = ok_mix and bool(v) and cache[(D, "a")].contains(v) and cache[(D, "b")].contains(v)
                    cnt += 1
    pos("[A] mixed brackets [z_a,z_b] (level 6) lie in nested-letter span of Qa AND of Qb", ok_mix,
        f"{cnt} nonzero mixed brackets")

    check_transfer(A, "[A] seed b", 3, qb)
    check_transfer(A, "[A] seed a", 2, qa)
    check_PiE(A, "[A]", 5, [D for D in sorted(A.seqs(5)) if A.antidominant(D, 5)], A.nbr)

    # NEG-overlap: naive direct-sum count vs union rank
    det, why, rows = False, False, []
    for (n, D), (ra, rb, rab) in sorted(rec.items()):
        r_a, r_b, r_u = ra["S1"].dim(), rb["S1"].dim(), rab["S1"].dim()
        naive = len(ra["P"]) - (r_a + r_b)
        if r_a + r_b != r_u:
            ov = intersect(ra["S2"].basis(), rb["S2"].basis()).dim()
            rows.append(f"n={n} D={D}: rk_a={r_a} rk_b={r_b} rk_union={r_u} naive_quot={naive} direct_quot={rab['qd']} dim(PnIanIb)={ov}")
            if naive != rab["qd"]:
                det = True
                why = why or ov > 0
    neg("[A] overlap neglect: summing the two projected ranks (direct-sum presumption)", det, why,
        "; ".join(rows[:6]) + (f" (+{len(rows) - 6} more)" if len(rows) > 6 else ""))

    # NEG-line: ideal generated by the LINE C q_b only (not the complete module)
    n, d = 4, 3
    rows, det, manuf = [], False, False
    for D in sorted(A.seqs(n)):
        if not A.antidominant(D, n):
            continue
        Pb = lowest(A, n, D)
        if not Pb:
            continue
        proj = Proj(Pb, A.nbr)
        J = nested_span(A, n, D, [(d, {A.vdeg(qb): Ech([qb])})])
        PJ = intersect(Pb, J.basis())
        S1 = proj_family(A, n, D, [(d, qb)], proj)
        rows.append(f"D={D}: dim(PnJ)={PJ.dim()} rk Pi_P(J)={S1.dim()} Pi_P(J)subJ={contained(S1, J)}")
        if PJ.dim() < S1.dim():
            det = True
            manuf = manuf or not contained(S1, J)
    Jlev = {D: nested_span(A, n, D, [(d, {A.vdeg(qb): Ech([qb])})]) for D in A.seqs(n)}
    notE = any(not Jlev.get(A.raise_(D, 0), Ech()).contains(deriv(A.E[0], v))
               for D, J in Jlev.items() for v in J.basis())
    isF = all(Jlev.get(A.lower(D, 0), Ech()).contains(deriv(A.F[0], v))
              for D, J in Jlev.items() for v in J.basis())
    neg("[A] non-stable span: J = ideal generated by the line C q_b (level 4)", det, manuf and notE,
        "; ".join(rows) + f"; J not E-stable={notE}; J F-stable={isF}")

    # NEG-nonlowest: use z0 = E q_b (not a lowest vector) as the 'seed'
    z0 = deriv(A.E[0], qb)
    rows, det = [], False
    for n in (4, 5):
        for D in sorted(A.seqs(n)):
            if not A.antidominant(D, n):
                continue
            Pb = lowest(A, n, D)
            if not Pb:
                continue
            proj = Proj(Pb, A.nbr)
            Sz = proj_family(A, n, D, [(3, z0)], proj)
            S2 = intersect(Pb, gb(n, D).basis())
            if Sz.dim() < S2.dim():
                det = True
                rows.append(f"n={n} D={D}: rk family(z0)={Sz.dim()} < dim(PnI)={S2.dim()}")
    Fz0 = deriv(A.F[0], z0)
    reason = bool(Fz0) and mod_dim(raise_closure(A, z0)) < mod_dim(Qb)
    neg("[A] seed-span loss: non-lowest seed z0=E q_b in the projected formula", det, reason,
        "; ".join(rows[:6]) + f"; F z0 != 0: {bool(Fz0)}; dim U(n+)z0={mod_dim(raise_closure(A, z0))} < dim Q={mod_dim(Qb)}")

    # NEG-W: weight-graded but non-F-stable one-dimensional W
    n, D = 4, (2,)
    Pb = lowest(A, n, D)
    proj = Proj(Pb, A.nbr)
    w = A.L(n, (1,)).basis()[0]
    Ew = deriv(A.E[0], w)
    y = vadd(Pb[0], Ew)
    Wsp = Ech([y])
    piW = Ech([proj(y)])
    PW = intersect(Pb, [y])
    det = (not contained(piW, Wsp)) and PW.dim() == 0 and piW.dim() == 1
    Fy = deriv(A.F[0], y)
    neg("[A] non-stable W=span{x+E w} (x in P): Pi_P(W) not inside W, PnW=0", det, bool(Fy) and not Wsp.contains(Fy),
        f"dim Pi_P(W)={piW.dim()} dim(PnW)={PW.dim()} F y in W: {Wsp.contains(Fy)}")

    # NEG-sorted: drop ordered tuples (keep only nondecreasing letter tuples)
    rows, det = [], False
    for n in (5, 6):
        for D in sorted(A.seqs(n)):
            if not A.antidominant(D, n):
                continue
            Pb = lowest(A, n, D)
            if not Pb:
                continue
            proj = Proj(Pb, A.nbr)
            Ss = proj_family(A, n, D, [(3, qb)], proj, filt=lambda u: list(u) == sorted(u))
            S2 = intersect(Pb, gb(n, D).basis())
            if Ss.dim() < S2.dim():
                det = True
                rows.append(f"n={n} D={D}: rk sorted-only={Ss.dim()} < dim(PnI)={S2.dim()}")
    info(f"[A] probe sampled-tuples (nondecreasing only, seed b): deficit found={det}; " + "; ".join(rows[:6]))

    # NEG-wrong-form: identity letter Gram (breaks <E x,y>=<x,F y> since |h|^2=2)
    I3 = [[ONE if i == j else ZERO for j in range(3)] for i in range(3)]
    nbr_id = nbr_of(I3)
    adj_fail = any(ip(deriv(A.E[0], letter(x)), letter(yy), nbr_id) != ip(letter(x), deriv(A.F[0], letter(yy)), nbr_id)
                   for x in range(3) for yy in range(3))
    rows, det, spans_differ = [], False, False
    for n in (4, 5):
        for D in sorted(A.seqs(n)):
            if not A.antidominant(D, n):
                continue
            Pb = lowest(A, n, D)
            if not Pb:
                continue
            pw = Proj(Pb, nbr_id)
            Dm = A.lower(D, 0)
            bad = sum(1 for v in A.L(n, Dm).basis() if pw(deriv(A.E[0], v))) if min(Dm) >= 0 else 0
            Sw = proj_family(A, n, D, [(3, qb)], pw)
            S2 = intersect(Pb, gb(n, D).basis())
            diff = not same_space(Sw, S2)
            spans_differ = spans_differ or diff
            if bad:
                det = True
            rows.append(f"n={n} D={D}: #y with Pi'_P(E y)!=0: {bad}; family==PnI: {not diff}")
    neg("[A] adjointness loss: identity letter Gram used for the projection", det, adj_fail,
        "; ".join(rows) + f"; final spans differ somewhere: {spans_differ}")
    info(f"[A] elapsed {time.perf_counter() - t0:.2f}s")


# ---------------------------------------------------------------- model B: sl3
def run_sl3():
    t0 = time.perf_counter()
    Bm = build_sl3()
    G_claim = [[ONE if i == j else ZERO for j in range(8)] for i in range(8)]
    G_claim[3][3] = G_claim[4][4] = Fr(2)
    G_claim[3][4] = G_claim[4][3] = ONE
    G_claim[7][7] = Fr(4)
    pos("[B] Gram of displayed basis B = identity except block(3,4)=[[2,1],[1,2]], G77=4 (0-based)",
        Bm.G == G_claim, f"G={[[str(x) for x in r] for r in Bm.G]}")
    ok1 = all(ip(deriv(Bm.E[i], letter(x)), letter(y), Bm.nbr) == ip(letter(x), deriv(Bm.F[i], letter(y)), Bm.nbr)
              for i in range(2) for x in range(8) for y in range(8))
    okh = all(ip(deriv(Bm.H[i], letter(x)), letter(y), Bm.nbr) == ip(letter(x), deriv(Bm.H[i], letter(y)), Bm.nbr)
              for i in range(2) for x in range(8) for y in range(8))
    words2 = list(product(range(8), repeat=2))
    ok2 = all(ip(deriv(Bm.E[i], {x: ONE}), {y: ONE}, Bm.nbr) == ip({x: ONE}, deriv(Bm.F[i], {y: ONE}), Bm.nbr)
              for i in range(2) for x in words2 for y in words2)
    pos("[B] (ad e_i)^dagger = ad f_i on M and on M^(x)2; Cartan self-adjoint", ok1 and ok2 and okh,
        f"M:{ok1} M^2:{ok2} H:{okh}")
    pos("[B] letter root degrees of B", Bm.deg == [(0, 0), (1, 0), (0, 1), (1, 1), (1, 1), (2, 1), (1, 2), (2, 2)],
        f"{Bm.deg}")
    e1, e2 = Bm.Emats
    e12 = mcomm(e1, e2)
    B = Bm.basis
    pres = [mcomm(e1, B[0]) == B[1], mcomm(e2, B[0]) == B[2], mcomm(e12, B[0]) == B[3], mcomm(e1, B[2]) == B[4],
            mcomm(e1, B[3]) == B[5], mcomm(e2, B[3]) == B[6], mcomm(e12, B[3]) == B[7]]
    pos("[B] presentation (non-load-bearing): B_1..B_7 = raisings of B_0=E31 as listed in review", all(pres), f"{pres}")

    Pq = lowest(Bm, 2, (1, 1))
    assert len(Pq) == 1
    q = Pq[0]
    Q = raise_closure(Bm, q)
    pos("[B] toy seed q = lowest vector of V(1,1) in L_2(M) at degree (1,1); dim U(n+)q = 8", mod_dim(Q) == 8,
        f"dim L_2={sum(Bm.L(2, D).dim() for D in Bm.seqs(2))}")

    ad3 = [D for D in sorted(Bm.seqs(3)) if Bm.antidominant(D, 3)]
    ad4 = [D for D in sorted(Bm.seqs(4)) if Bm.antidominant(D, 4)]
    top4 = set(ad4) | {Bm.lower(D, i) for D in ad4 for i in range(2)} | {Bm.raise_(D, i) for D in ad4 for i in range(2)}
    I = brute_ideal(Bm, [(2, Q)], 4, top_degrees=top4)
    g = getter(I)
    rec = {}
    for n, degs in ((3, ad3), (4, ad4)):
        for D in degs:
            r = analyze(Bm, "[B] seed q", n, D, [(2, q)], [(2, Q)], g, Bm.nbr)
            if r:
                rec[(n, D)] = r
    check_transfer(Bm, "[B] seed q", 1, q)
    check_transfer(Bm, "[B] seed q", 2, q)
    check_PiE(Bm, "[B]", 3, ad3, Bm.nbr)

    # NEG-overlap (contrived full overlap): second seed q2 = [B0, q] lies inside ideal(Q)
    q2 = br(letter(0), q)
    low2 = all(not deriv(Fa, q2) for Fa in Bm.F)
    Q2 = raise_closure(Bm, q2)
    inside = all(g(3, D).contains(v) for D, E in Q2.items() for v in E.basis())
    rows, det = [], False
    for D in ad4:
        if (4, D) not in rec:
            continue
        r = rec[(4, D)]
        S2nd = proj_family(Bm, 4, D, [(3, q2)], r["proj"])
        Su = proj_family(Bm, 4, D, [(2, q), (3, q2)], r["proj"])
        naive = len(r["P"]) - (r["S1"].dim() + S2nd.dim())
        if r["S1"].dim() + S2nd.dim() != Su.dim():
            rows.append(f"D={D}: rk1={r['S1'].dim()} rk2={S2nd.dim()} rk_union={Su.dim()} naive_quot={naive} direct_quot={r['qd']}")
            det = det or naive != r["qd"]
    neg("[B] overlap neglect with q2=[B0,q] (lowest, inside ideal(Q))", det, low2 and inside,
        "; ".join(rows[:5]) + (f" (+{len(rows) - 5} more)" if len(rows) > 5 else "") + f"; q2 lowest={low2}; U(n+)q2 in I_3={inside}")

    # NEG-line at level 3
    rows, det, manuf = [], False, False
    J3 = {D: nested_span(Bm, 3, D, [(2, {(1, 1): Ech([q])})]) for D in Bm.seqs(3)}
    for D in ad3:
        if (3, D) not in rec:
            continue
        r = rec[(3, D)]
        J = J3.get(D, Ech())
        PJ = intersect(r["P"], J.basis())
        rows.append(f"D={D}: dim(PnJ)={PJ.dim()} rk Pi_P(J)={r['S1'].dim()}")
        if PJ.dim() < r["S1"].dim():
            det = True
            manuf = manuf or not contained(r["S1"], J)
    notE = any(not J3.get(Bm.raise_(D, i), Ech()).contains(deriv(Bm.E[i], v))
               for D, J in J3.items() for v in J.basis() for i in range(2))
    neg("[B] non-stable span: J = ideal generated by the line C q (level 3)", det, manuf and notE,
        "; ".join(rows) + f"; J not E-stable={notE}")

    # NEG-nonlowest seed z0 = E_1 q (or E_2 q)
    z0 = deriv(Bm.E[0], q) or deriv(Bm.E[1], q)
    rows, det = [], False
    for D in ad3:
        if (3, D) not in rec:
            continue
        r = rec[(3, D)]
        Sz = proj_family(Bm, 3, D, [(2, z0)], r["proj"])
        if Sz.dim() < r["S2"].dim():
            det = True
            rows.append(f"D={D}: rk family(z0)={Sz.dim()} < dim(PnI)={r['S2'].dim()}")
    reason = any(deriv(Fa, z0) for Fa in Bm.F) and mod_dim(raise_closure(Bm, z0)) < mod_dim(Q)
    neg("[B] seed-span loss: non-lowest seed z0=E q in the projected formula (level 3)", det, reason,
        "; ".join(rows[:6]) + f"; dim U(n+)z0={mod_dim(raise_closure(Bm, z0))} < 8")

    # probe: sampled tuples at level 4
    rows, det = [], False
    for D in ad4:
        if (4, D) not in rec:
            continue
        r = rec[(4, D)]
        Ss = proj_family(Bm, 4, D, [(2, q)], r["proj"], filt=lambda u: list(u) == sorted(u))
        if Ss.dim() < r["S2"].dim():
            det = True
            rows.append(f"D={D}: rk sorted-only={Ss.dim()} < dim(PnI)={r['S2'].dim()}")
    info(f"[B] probe sampled-tuples (nondecreasing only): deficit found={det}; " + "; ".join(rows[:6]))

    # NEG-wrong-form: identity Gram on B-coordinates
    I8 = [[ONE if i == j else ZERO for j in range(8)] for i in range(8)]
    nbr_id = nbr_of(I8)
    adj_fail = any(ip(deriv(Bm.E[i], letter(x)), letter(y), nbr_id) != ip(letter(x), deriv(Bm.F[i], letter(y)), nbr_id)
                   for i in range(2) for x in range(8) for y in range(8))
    rows, det, spans_differ = [], False, False
    for D in ad3:
        Pb = lowest(Bm, 3, D)
        if not Pb:
            continue
        pw = Proj(Pb, nbr_id)
        bad = 0
        for i in range(2):
            Dm = Bm.lower(D, i)
            if min(Dm) >= 0:
                bad += sum(1 for v in Bm.L(3, Dm).basis() if pw(deriv(Bm.E[i], v)))
        Sw = proj_family(Bm, 3, D, [(2, q)], pw)
        diff = not same_space(Sw, intersect(Pb, g(3, D).basis()))
        spans_differ = spans_differ or diff
        det = det or bad > 0
        rows.append(f"D={D}: #y with Pi'_P(E y)!=0: {bad}; family==PnI: {not diff}")
    neg("[B] adjointness loss: identity Gram on B-coordinates used for the projection", det, adj_fail,
        "; ".join(rows) + f"; final spans differ somewhere: {spans_differ}")
    info(f"[B] elapsed {time.perf_counter() - t0:.2f}s")


# ---------------------------------------------------------------- lifting boundary
def run_lift_boundary():
    # 2-dim module of the 1-dim Lie algebra spanned by a nilpotent F (not semisimple):
    # F v1 = v0, F v0 = 0; W = span{v0} is F-stable.
    F = {0: {}, 1: {0: ONE}}
    apply = lambda v: deriv(F, v)
    v0, v1 = {(0,): ONE}, {(1,): ONE}
    kerF = Ech([lincomb(c, [v0, v1]) for c in kernel([apply(v0), apply(v1)])])
    W = Ech([v0])
    lifts = [x for x in kerF.basis() if not W.contains(x)]            # images in V/W of ker F
    quot_lowest = 1 if W.contains(apply(v1)) else 0                  # class of v1 is killed in V/W
    # no F-stable complement span{v1 + c v0}: F(v1 + c v0) = v0 is never a multiple of v1 + c v0
    no_complement = W.contains(apply(vadd(v1, v0, Fr(7, 3)))) and apply(v1) == v0
    neg("[C] lifting needs complete reducibility: nilpotent non-semisimple 2-dim toy",
        quot_lowest == 1 and len(lifts) == 0, no_complement,
        f"dim ker F={kerF.dim()} (inside W), quotient lowest dim={quot_lowest}, liftable={len(lifts)}")


def main():
    info(f"python {sys.version.split()[0]}; exact Fraction arithmetic; reviewer-authored toy controls only")
    t0 = time.perf_counter()
    run_sl2()
    run_sl3()
    run_lift_boundary()
    npos = sum(ok for _, ok in POS)
    ndet = sum(d for _, d, _ in NEG)
    nrea = sum(r for _, _, r in NEG)
    print(f"SUMMARY | positive {npos}/{len(POS)} PASS | negative {ndet}/{len(NEG)} DETECTED | "
          f"reasons {nrea}/{len(NEG)} CONFIRMED | total {time.perf_counter() - t0:.2f}s", flush=True)
    return 0 if (npos == len(POS) and ndet == len(NEG) and nrea == len(NEG)) else 1


if __name__ == "__main__":
    sys.exit(main())
