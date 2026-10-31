#!/usr/bin/env python3
"""Reviewer control C3 for wave f184-sun8-lie-type-away-from-seven.

Independently authored by the reviewer; no author code is opened or run.
Concrete-group test of Lemma 1 (overgroups of a Sylow p-subgroup U lie in a
proper standard parabolic P_J with J = W_H n {simple reflections}), Lemma 2
(D(S) divides every proper p'-index), and the key step of Theorem B (no two
p'-index subgroups have index gcd exactly 7), in small simple groups of Lie
type built from matrices over finite fields and acting on points.
Every overgroup of U is a union of U-double cosets; all of them are enumerated
exactly as product-closed sets of U-double cosets. B = N_S(U), Bruhat classes
are B-double cosets, and simple reflections are the classes s with B u BsB a
subgroup. No classification, maximal-subgroup list or author output is used.
Negative controls: PSL3(2) (the D=7 exception), p=7 description PSL2(7)
(p-divisible step fails), and a cross-characteristic Sylow 3-subgroup.
"""
import json, sys, time, itertools, math

T0 = time.time()
OUT = {"control": "reviewer-c3-small-group-overgroups", "checks": {}, "groups": {}, "negative": {}}
FAIL = []
def check(name, ok, detail=None):
    OUT["checks"][name] = {"ok": bool(ok), "detail": detail}
    if not ok:
        FAIL.append(name)

class GF:
    def __init__(self, p, k, mod):
        self.p, self.k, self.q = p, k, p ** k
        q = self.q
        def to_vec(a):
            return [(a // p ** i) % p for i in range(k)]
        def to_int(v):
            return sum(c * p ** i for i, c in enumerate(v))
        self.add = [[to_int([(x + y) % p for x, y in zip(to_vec(a), to_vec(b))]) for b in range(q)] for a in range(q)]
        def mulv(u, v):
            r = [0] * (2 * k - 1)
            for i, x in enumerate(u):
                for j, y in enumerate(v):
                    r[i + j] = (r[i + j] + x * y) % p
            for d in range(2 * k - 2, k - 1, -1):
                c = r[d]
                if c:
                    for i in range(k + 1):
                        r[d - k + i] = (r[d - k + i] - c * mod[i]) % p
            return r[:k]
        self.mul = [[to_int(mulv(to_vec(a), to_vec(b))) for b in range(q)] for a in range(q)]
        self.neg = [next(b for b in range(q) if self.add[a][b] == 0) for a in range(q)]
        inv = [None]
        for a in range(1, q):
            c = [b for b in range(1, q) if self.mul[a][b] == 1]
            assert len(c) == 1, "not a field"
            inv.append(c[0])
        self.inv = inv
        self.basis = [p ** i for i in range(k)]
    def pw(self, a, e):
        r = 1
        for _ in range(e):
            r = self.mul[r][a]
        return r
    def gen(self):
        for g in range(1, self.q):
            x, o = g, 1
            while x != 1:
                x = self.mul[x][g]; o += 1
            if o == self.q - 1:
                return g

def mmul(F, A, B):
    n = len(A)
    return tuple(tuple(_dot(F, A[i], [B[k][j] for k in range(n)]) for j in range(n)) for i in range(n))

def _dot(F, u, v):
    s = 0
    for x, y in zip(u, v):
        if x and y:
            s = F.add[s][F.mul[x][y]]
    return s

def mvec(F, M, v):
    return tuple(_dot(F, row, v) for row in M)

def transpose(M):
    return tuple(zip(*M))

def ident(n):
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))

def normalize(F, v):
    for c in v:
        if c:
            ic = F.inv[c]
            return tuple(F.mul[ic][x] for x in v)
    return None

def all_points(F, n):
    return [v for v in itertools.product(range(F.q), repeat=n) if any(v) and normalize(F, v) == v]

def perm_of(F, M, pts, idx):
    return tuple(idx[normalize(F, mvec(F, M, P))] for P in pts)

def comp(s, t):
    return tuple(map(s.__getitem__, t))

def closure(gens, n, cap=None):
    e = tuple(range(n))
    elems = {e: 0}; lst = [e]
    i = 0
    while i < len(lst):
        g = lst[i]; i += 1
        for s in gens:
            h = comp(s, g)
            if h not in elems:
                elems[h] = len(lst); lst.append(h)
                if cap and len(lst) > cap:
                    return None, None
    return elems, lst

def ppart(n, p):
    r = 1
    while n % p == 0:
        n //= p; r *= p
    return r

def overgroup_lattice(elems, lst, Ul):
    """U-double cosets, product table and all product-closed unions (= all overgroups of U)."""
    N = len(lst)
    dc = [-1] * N; reps = []; sizes = []
    for gi in range(N):
        if dc[gi] >= 0:
            continue
        k = len(reps); reps.append(gi)
        gU = [comp(lst[gi], v) for v in Ul]
        cnt = 0
        for u in Ul:
            for x in gU:
                yi = elems[comp(u, x)]
                if dc[yi] < 0:
                    dc[yi] = k; cnt += 1
        sizes.append(cnt)
    nd = len(reps)
    prod = [[None] * nd for _ in range(nd)]
    for a in range(nd):
        raU = [comp(lst[reps[a]], u) for u in Ul]
        for b in range(nd):
            rb = lst[reps[b]]
            prod[a][b] = frozenset(dc[elems[comp(x, rb)]] for x in raU)
    def close(C):
        C = set(C)
        changed = True
        while changed:
            changed = False
            for a in list(C):
                for b in list(C):
                    new = prod[a][b] - C
                    if new:
                        C |= new; changed = True
        return frozenset(C)
    e_dc = dc[0]
    start = close({e_dc})
    found = {start}; queue = [start]
    while queue:
        C = queue.pop()
        for d in range(nd):
            if d not in C:
                C2 = close(C | {d})
                if C2 not in found:
                    found.add(C2); queue.append(C2)
    return dc, reps, sizes, prod, close, found, e_dc

def analyze(name, S_gens, U_gens, npts, p, D, expected_max, expected_order, cap=70000, check_thmB=True):
    t = time.time()
    rec = {"p": p, "D": D}
    elems, lst = closure(S_gens, npts, cap)
    if elems is None:
        rec["status"] = "CAP_EXCEEDED_UNKNOWN"
        OUT["groups"][name] = rec
        check(f"{name}: group built", False, rec)
        return None
    order = len(lst)
    Uel, Ul = closure(U_gens, npts)
    rec.update({"order": order, "expected_order": expected_order, "|U|": len(Ul), "U_is_Sylow_p": len(Ul) == ppart(order, p) and all(g in elems for g in Ul)})
    dc, reps, sizes, prod, close, found, e_dc = overgroup_lattice(elems, lst, Ul)
    nd = len(reps)
    full = frozenset(range(nd))
    Bset = frozenset(d for d in range(nd) if sizes[d] == len(Ul))
    rec["|N(U)|"] = sum(sizes[d] for d in Bset)
    B_closed = close(Bset) == Bset
    # Bruhat classes (B-double cosets) as sets of U-double cosets
    cls_of = {}; classes = []
    for i in range(nd):
        if i in cls_of:
            continue
        X = set()
        for a in Bset:
            X |= prod[a][i]
        Y = set()
        for x in X:
            for b in Bset:
                Y |= prod[x][b]
        assert i in Y and not (set(cls_of) & Y)
        cid = len(classes); classes.append(frozenset(Y))
        for y in Y:
            cls_of[y] = cid
    Bcls = cls_of[e_dc]
    simple = [c for c in range(len(classes)) if c != Bcls and close(Bset | classes[c]) == (Bset | classes[c])]
    rec.update({"num_U_double_cosets": nd, "|W|(=#B-double cosets)": len(classes), "rank(#simple reflections)": len(simple)})
    lemma1_ok = True; lemma2_ok = True
    proper = []
    for C in found:
        size = sum(sizes[d] for d in C)
        idx = order // size
        assert order % size == 0
        WH = frozenset(cls_of[d] for d in C)
        J = [s for s in simple if s in WH]
        PJ = close(set(Bset).union(*[classes[s] for s in J])) if J else Bset
        WJ = frozenset(cls_of[d] for d in PJ)
        if C != full:
            lemma1_ok &= (C <= PJ) and (WH == WJ) and (PJ != full)
            lemma2_ok &= (idx % D == 0)
            proper.append((idx, C))
    max_idx = sorted(i for i, C in proper if not any(C < C2 for _, C2 in proper))
    rec.update({"num_proper_overgroups_of_U": len(proper), "proper_overgroup_indices": sorted(i for i, _ in proper),
                "maximal_overgroup_indices": max_idx, "expected_maximal_parabolic_indices": sorted(expected_max)})
    idxs = sorted(set(i for i, _ in proper))
    gcds = sorted(set(math.gcd(a, b) for a in idxs for b in idxs))
    rec["pairwise_gcds_of_p'_indices"] = gcds
    rec["some_pair_gcd_7"] = 7 in gcds
    rec["elapsed_s"] = round(time.time() - t, 3)
    OUT["groups"][name] = rec
    ok = (order == expected_order) and rec["U_is_Sylow_p"] and B_closed and lemma1_ok and lemma2_ok and max_idx == sorted(expected_max)
    rec["lemma1_W_H=W_J_and_H<=P_J_proper"] = lemma1_ok
    rec["lemma2_D_divides_all_proper_p'_indices"] = lemma2_ok
    check(f"{name}: Lemma1/Lemma2/max-parabolic indices", ok, None)
    if check_thmB:
        check(f"{name}: Theorem B key step (no two p'-indices with gcd 7)", 7 not in gcds, gcds)
    return rec, elems, lst

# ---------------- constructions ----------------
FIELDS = {
    2: GF(2, 1, [0, 1]), 3: GF(3, 1, [0, 1]), 4: GF(2, 2, [1, 1, 1]), 5: GF(5, 1, [0, 1]), 7: GF(7, 1, [0, 1]),
    8: GF(2, 3, [1, 1, 0, 1]), 9: GF(3, 2, [1, 0, 1]), 11: GF(11, 1, [0, 1]), 13: GF(13, 1, [0, 1]),
    16: GF(2, 4, [1, 1, 0, 0, 1]), 25: GF(5, 2, [2, 1, 1]), 27: GF(3, 3, [1, 2, 0, 1]),
}

def elem_mat(n, i, j, a):
    return tuple(tuple((1 if r == c else 0) if not (r == i and c == j) else a for c in range(n)) for r in range(n))

def greedy_gens(F, mats, pts, idx):
    perms = [perm_of(F, M, pts, idx) for M in mats]
    target = len(set(perms))
    gens = []
    cur = {tuple(range(len(pts)))}
    for pm in perms:
        if pm not in cur:
            gens.append(pm)
            e, l = closure(gens, len(pts))
            cur = set(l)
    return gens

def PSL(n, q):
    F = FIELDS[q]
    pts = all_points(F, n); idx = {P: i for i, P in enumerate(pts)}
    Umats = [elem_mat(n, i, j, a) for i in range(n) for j in range(i + 1, n) for a in F.basis]
    Ug = [perm_of(F, M, pts, idx) for M in Umats]
    Lg = [perm_of(F, transpose(M), pts, idx) for M in Umats]
    return Ug + Lg, Ug, len(pts)

def PSp4_3():
    F = FIELDS[3]; n = 4
    Om = ((0, 0, 0, 1), (0, 0, 1, 0), (0, 2, 0, 0), (2, 0, 0, 0))
    def is_symp(M):
        return mmul(F, mmul(F, transpose(M), Om), M) == Om
    Umats = []
    for v in itertools.product(range(3), repeat=6):
        M = ((1, v[0], v[1], v[2]), (0, 1, v[3], v[4]), (0, 0, 1, v[5]), (0, 0, 0, 1))
        if is_symp(M):
            Umats.append(M)
    pts = all_points(F, n); idx = {P: i for i, P in enumerate(pts)}
    Ug = greedy_gens(F, Umats, pts, idx)
    Lg = greedy_gens(F, [transpose(M) for M in Umats], pts, idx)
    return Ug + Lg, Ug, len(pts), len(Umats)

def SU(m, q):
    F = FIELDS[q * q]
    conj = [F.pw(a, q) for a in range(F.q)]
    J = tuple(tuple(1 if c == m - 1 - r else 0 for c in range(m)) for r in range(m))
    def is_unitary(M):
        Mb = tuple(tuple(conj[x] for x in row) for row in M)
        return mmul(F, mmul(F, transpose(M), J), Mb) == J
    Umats = []
    free = [(i, j) for i in range(m) for j in range(i + 1, m)]
    for vals in itertools.product(range(F.q), repeat=len(free)):
        M = [list(r) for r in ident(m)]
        for (i, j), v in zip(free, vals):
            M[i][j] = v
        M = tuple(tuple(r) for r in M)
        if is_unitary(M):
            Umats.append(M)
    def h(u, v):
        s = 0
        for i in range(m):
            s = F.add[s][F.mul[u[i]][conj[v[m - 1 - i]]]]
        return s
    pts = [P for P in all_points(F, m) if h(P, P) == 0]
    idx = {P: i for i, P in enumerate(pts)}
    # w0 = c*J with c*conj(c)=1 and det = 1
    c = F.neg[1] if (m % 2 == 1 and F.p != 2) else 1
    w0 = tuple(tuple(F.mul[c][x] for x in row) for row in J)
    assert is_unitary(w0)
    Ug = greedy_gens(F, Umats, pts, idx)
    return Ug + [perm_of(F, w0, pts, idx)], Ug, len(pts), len(Umats)

def Sz8():
    F = FIELDS[8]
    th = lambda a: F.pw(a, 4)        # theta: x -> x^(2^(n+1)) with q=2^(2n+1)=8, n=1
    def Smat(a, b):
        r3 = (F.add[F.add[F.pw(a, 6)][F.mul[a][b]]][th(b)], F.add[F.pw(a, 5)][b], a, 1)
        return ((1, 0, 0, 0), (a, 1, 0, 0), (b, th(a), 1, 0), r3)
    lam = F.gen()
    d = (F.pw(lam, 3), F.pw(lam, 2), F.inv[F.pw(lam, 2)], F.inv[F.pw(lam, 3)])
    Dm = tuple(tuple(d[i] if i == j else 0 for j in range(4)) for i in range(4))
    Tm = tuple(tuple(1 if c == 3 - r else 0 for c in range(4)) for r in range(4))
    Umats = [Smat(a, b) for a in range(8) for b in range(8)]
    # U must be closed under multiplication (exactly these 64 matrices)
    Uset = set(Umats)
    U_closed = all(mmul(F, A, B) in Uset for A in Umats[:16] for B in Umats)
    Jsym = Tm
    pres_form = all(mmul(F, mmul(F, transpose(M), Jsym), M) == Jsym for M in Umats + [Dm, Tm])
    # point set: orbit of <e4> under generators (column action)
    gens_m = Umats + [Dm, Tm]
    orbit = [(0, 0, 0, 1)]; seen = set(orbit); i = 0
    while i < len(orbit):
        P = orbit[i]; i += 1
        for M in gens_m:
            Q = normalize(F, mvec(F, M, P))
            if Q not in seen:
                seen.add(Q); orbit.append(Q)
    idx = {P: k for k, P in enumerate(orbit)}
    Ug = greedy_gens(F, Umats, orbit, idx)
    Sg = Ug + [perm_of(F, Dm, orbit, idx), perm_of(F, Tm, orbit, idx)]
    return Sg, Ug, len(orbit), {"U_closed_64": U_closed and len(Uset) == 64, "preserves_symplectic_antidiag": pres_form, "orbit_size": len(orbit)}

def cyc(e, q):
    # cyclotomic value Phi_e(q) by Moebius product
    def mu(n):
        r, m, pr = 1, n, 2
        while pr * pr <= m:
            if m % pr == 0:
                m //= pr
                if m % pr == 0:
                    return 0
                r = -r
            pr += 1
        if m > 1:
            r = -r
        return r
    num, den = 1, 1
    for d in range(1, e + 1):
        if e % d == 0:
            m = mu(e // d)
            if m == 1: num *= q ** d - 1
            elif m == -1: den *= q ** d - 1
    assert num % den == 0
    return num // den

# ---------------- run positive cases ----------------
for q in [4, 5, 8, 9, 11, 13, 16, 25, 27]:
    F = FIELDS[q]
    Sg, Ug, n = PSL(2, q)
    analyze(f"PSL2({q})", Sg, Ug, n, F.p, cyc(2, q), [q + 1], q * (q * q - 1) // math.gcd(2, q - 1))
for q in [3, 4]:
    F = FIELDS[q]
    Sg, Ug, n = PSL(3, q)
    analyze(f"PSL3({q})", Sg, Ug, n, F.p, cyc(3, q), [q * q + q + 1] * 2, q ** 3 * (q * q - 1) * (q ** 3 - 1) // math.gcd(3, q - 1))
Sg, Ug, n = PSL(4, 2)
analyze("PSL4(2)", Sg, Ug, n, 2, cyc(4, 2), [15, 35, 15], 20160)
Sg, Ug, n, nU = PSp4_3()
analyze("PSp4(3)", Sg, Ug, n, 3, cyc(4, 3), [40, 40], 25920)
for (m, q) in [(3, 3), (4, 2), (3, 4)]:
    Sg, Ug, n, nU = SU(m, q)
    e = 2 * m if m % 2 else 2 * (m - 1)
    exp = {(3, 3): [28], (4, 2): [45, 27], (3, 4): [65]}[(m, q)]
    analyze(f"PSU{m}({q})", Sg, Ug, n, FIELDS[q].p, cyc(e, q), exp, {(3, 3): 6048, (4, 2): 25920, (3, 4): 62400}[(m, q)])
Sg, Ug, n, info = Sz8()
OUT["sz8_construction"] = info
check("Sz(8) construction sanity", info["U_closed_64"] and info["orbit_size"] == 65, info)
analyze("Sz(8)=2B2(8)", Sg, Ug, n, 2, 8 * 8 + 1, [65], 29120)

# ---------------- negative controls ----------------
# NEG-1: PSL3(2), p=2, D=Phi_3(2)=7: two p'-index subgroups with gcd 7 must be FOUND (the stated exception)
Sg, Ug, n = PSL(3, 2)
res = analyze("PSL3(2)", Sg, Ug, n, 2, cyc(3, 2), [7, 7], 168, check_thmB=False)
rec, elems, lst = res
check("NEG-1 PSL3(2): gcd-7 pair among p'-indices found (expected)", rec["some_pair_gcd_7"], rec["pairwise_gcds_of_p'_indices"])
# count index-7 subgroups: point stabilizers and line stabilizers in PG(2,2)
F2 = FIELDS[2]
pts = all_points(F2, 3)
def stab(i):
    return frozenset(g for g in lst if g[i] == i)
pstabs = [stab(i) for i in range(7)]
# line stabilizers: lines = 2-dim subspaces; a line is a set of 3 points closed under addition
lines = set()
for a, b in itertools.combinations(range(7), 2):
    c = tuple(F2.add[x][y] for x, y in zip(pts[a], pts[b]))
    lines.add(frozenset([a, b, pts.index(c)]))
lines = sorted(lines, key=sorted)
lstabs = [frozenset(g for g in lst if frozenset(g[x] for x in L) == L) for L in lines]
idx7 = set(pstabs) | set(lstabs)
three = pstabs[:3]
OUT["negative"]["NEG-1_index7"] = {"num_lines": len(lines), "distinct_index7_subgroups_found": len(idx7),
    "all_index_7": all(len(H) * 7 == 168 for H in idx7),
    "three_point_stabilizers_pairwise_gcd": [math.gcd(168 // len(A), 168 // len(B)) for A, B in itertools.combinations(three, 2)]}
check("NEG-1 PSL3(2): >=14 distinct index-7 subgroups (point+line stabilizers)", len(idx7) == 14 and all(len(H) * 7 == 168 for H in idx7), OUT["negative"]["NEG-1_index7"])

# NEG-2: p=7 description PSL2(7): three p-divisible subgroups (index 7) with pairwise gcd 7 exist
Sg, Ug, n = PSL(2, 7)
rec7, elems7, lst7 = analyze("PSL2(7) [p=7]", Sg, Ug, n, 7, cyc(2, 7), [8], 168, check_thmB=False)
def order_of(g):
    e = tuple(range(len(g))); x = g; o = 1
    while x != e:
        x = comp(g, x); o += 1
    return o
o4 = [g for g in lst7 if order_of(g) == 4]
o2 = [g for g in lst7 if order_of(g) == 2]
s4s = set()
for a in o4:
    for b in o2:
        e_, l_ = closure([a, b], n, cap=30)
        if l_ is not None and len(l_) == 24:
            s4s.add(frozenset(l_))
s4l = sorted(s4s, key=lambda H: sorted(H))[:3]
g7 = [math.gcd(168 // len(A), 168 // len(B)) for A, B in itertools.combinations(s4l, 2)]
OUT["negative"]["NEG-2_p7"] = {"num_order24_subgroups_from_<ord4,ord2>": len(s4s), "pairwise_gcds_of_three": g7, "each_index_divisible_by_p=7": all((168 // len(H)) % 7 == 0 for H in s4l)}
check("NEG-2 PSL2(7) p=7: three p-divisible index-7 subgroups pairwise gcd 7 (expected)", len(s4s) >= 3 and g7 == [7, 7, 7], OUT["negative"]["NEG-2_p7"])

# NEG-3: cross-characteristic: PSL3(2) with a Sylow 3-subgroup V: overgroup indices have no common divisor > 1
g3 = next(g for g in lst if order_of(g) == 3)
Vel, Vl = closure([g3], 7)
dcV, repsV, sizesV, prodV, closeV, foundV, eV = overgroup_lattice(elems, lst, Vl)
fullV = frozenset(range(len(repsV)))
idxV = sorted(168 // sum(sizesV[d] for d in C) for C in foundV if C != fullV)
gV = 0
for i in idxV:
    gV = math.gcd(gV, i)
OUT["negative"]["NEG-3_cross_char"] = {"|V|": len(Vl), "proper_overgroup_indices": idxV, "gcd_all": gV}
check("NEG-3 cross-characteristic Sylow 3 in PSL3(2): common divisor fails (expected)", gV == 1, OUT["negative"]["NEG-3_cross_char"])

OUT["fail"] = FAIL
OUT["all_ok"] = not FAIL
OUT["elapsed_s"] = round(time.time() - T0, 3)
json.dump(OUT, sys.stdout, indent=1, sort_keys=True, default=str)
sys.stdout.write("\n")
sys.exit(0 if not FAIL else 1)
