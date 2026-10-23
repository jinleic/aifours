#!/usr/bin/env python3
"""sun-coset7 (96h lane) EXPLORATORY probe v16 = v14 plus the TRIPLE-GRANULARITY constraints (TG) inside RPLP:
for every triple T = {a,b,c} of neighbours of v, U_v (U_a cap U_b cap U_c) lies in X_a cap X_b cap X_c and has measure
>= 1/gcd(n_v, [G : U_a cap U_b cap U_c]); with [G : ...] = L tau, tau in the T-rule range and a multiple of
lcm(I_ab, I_ac, I_bc)/L, the bound uses the WORST case gcd over admissible tau (any prime of tau outside {2,3,5}
is assumed to divide n_v).  Constraint: sum of atoms with A meeting T <= 1 - lb_T.
Original v14 docstring follows.
EXACT re-evaluation (Fractions) of given joint patterns.
argv: OUT INPUT INPUT_SHA ITEMS_JSON.  For each canonical joint solution listed in the pinned v6b result file (items
given by index), re-check exactly: LFC row values (alpha and alpha*) at all 7 vertices, T and Ppair(K2) on all 35
triangles (both sides), alpha + alpha* <= g, and RPLP-k7 at every vertex in both orientations with an EXACT two-phase
simplex over Fractions (minimise total measure; kill iff infeasible or min >= 1).  Reports per-rule outcomes.
EXPLORATORY ONLY; never a premise.  Standard library only; self budget 270 s.
"""
import itertools, json, math, os, sys, time, hashlib
from fractions import Fraction as F
T0 = time.monotonic()
BUDGET = 270.0


def v(p, n):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def num(t):
    return (2 ** t[0]) * (3 ** t[1]) * (5 ** t[2])


def vp(n):
    return (v(2, n), v(3, n), v(5, n))


def gval(P, Q):
    return tuple(min(a, b) for a, b in zip(P, Q))


def lab(P, a, g):
    vg = vp(g); va = vp(a)
    return num(tuple(P[i] + va[i] - vg[i] for i in range(3)))


def allowed_sets(labels, idx):
    res = set()
    for r in range(0, len(idx) + 1):
        for S in itertools.combinations(idx, r):
            ok = True
            for rr in range(2, len(S) + 1):
                for T in itertools.combinations(S, rr):
                    if max(math.gcd(labels[a], labels[b]) for a, b in itertools.combinations(T, 2)) < rr:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                res.add(S)
    return res


def simplex_exact(c, A_eq, b_eq):
    """min c.x, A x = b, x >= 0 (Fractions, two-phase, Bland). returns ('optimal', val) or ('infeasible', None)."""
    m = len(A_eq); n = len(c)
    A = [row[:] for row in A_eq]; b = b_eq[:]
    for i in range(m):
        if b[i] < 0:
            A[i] = [-x for x in A[i]]; b[i] = -b[i]
    T = [A[i] + [F(1) if k == i else F(0) for k in range(m)] + [b[i]] for i in range(m)]
    basis = [n + i for i in range(m)]

    def pivot(r, col):
        pv = T[r][col]
        T[r] = [x / pv for x in T[r]]
        for k in range(m):
            if k != r and T[k][col] != 0:
                f = T[k][col]
                T[k] = [a - f * bb for a, bb in zip(T[k], T[r])]
        basis[r] = col

    def run(cost, cols):
        while True:
            if time.monotonic() - T0 > BUDGET:
                raise TimeoutError()
            ent = None
            for col in cols:
                if col in basis:
                    continue
                rc = cost[col] - sum(cost[basis[i]] * T[i][col] for i in range(m))
                if rc < 0:
                    ent = col
                    break
            if ent is None:
                return
            r = None
            for i in range(m):
                if T[i][ent] > 0:
                    ratio = T[i][-1] / T[i][ent]
                    if r is None or ratio < r[0] or (ratio == r[0] and basis[i] < basis[r[1]]):
                        r = (ratio, i)
            pivot(r[1], ent)
    cost1 = [F(0)] * n + [F(1)] * m
    run(cost1, list(range(n + m)))
    if sum(cost1[basis[i]] * T[i][-1] for i in range(m)) > 0:
        return 'infeasible', None
    for i in range(m):
        if basis[i] >= n:
            for col in range(n):
                if T[i][col] != 0:
                    pivot(i, col)
                    break
    cost2 = list(c) + [F(0)] * m
    run(cost2, list(range(n)))
    return 'optimal', sum(cost2[basis[i]] * T[i][-1] for i in range(m))


def lfc_value(vv, P, G, row):
    N = [j for j in range(7) if j != vv]
    labels = {j: lab(P[j], row[j], G[vv][j]) for j in N}
    al = allowed_sets(labels, N)
    maxi = [S for S in al if S and not any(set(S) < set(S2) for S2 in al)]
    # LP: max sum c_j y_j s.t. sum_{S} y <= 1, y >= 0  -> min -c.y with slacks
    nn = len(N)
    A = []; b = []
    for k, S in enumerate(maxi):
        row_ = [F(1) if N[t] in S else F(0) for t in range(nn)] + [F(1) if kk == k else F(0) for kk in range(len(maxi))]
        A.append(row_); b.append(F(1))
    cst = [-F(row[N[t]], G[vv][N[t]]) for t in range(nn)] + [F(0)] * len(maxi)
    st, val = simplex_exact(cst, A, b)
    return -val


def tri_check(Px, Py, Pz, axy, axz, ayz, gxy, gxz, gyz):
    Pd = {'x': Px, 'y': Py, 'z': Pz}
    Al = {frozenset('xy'): axy, frozenset('xz'): axz, frozenset('yz'): ayz}
    Gg = {frozenset('xy'): gxy, frozenset('xz'): gxz, frozenset('yz'): gyz}

    def gamma(y):
        o = [t for t in 'xyz' if t != y]
        return Gg[frozenset(y + o[0])] * Gg[frozenset(y + o[1])] // math.gcd(Gg[frozenset(y + o[0])], Gg[frozenset(y + o[1])])

    def ell_v(z):
        gz = vp(gamma(z))
        return tuple(Pd[z][i] - gz[i] for i in range(3))
    tmin = 1
    for e in ('xy', 'xz', 'yz'):
        z = [t for t in 'xyz' if t not in e][0]
        a = Al[frozenset(e)]
        le = ell_v(z); va = vp(a)
        gg = num(tuple(min(va[i], le[i]) for i in range(3)))
        term = a // gg
        tmin = tmin * term // math.gcd(tmin, term)
    tmax = None
    for y in 'xyz':
        x, z = [t for t in 'xyz' if t != y]
        bd = gamma(y) * Al[frozenset(x + z)] * min(F(Al[frozenset(x + y)], Gg[frozenset(x + y)]), F(Al[frozenset(y + z)], Gg[frozenset(y + z)]))
        bb = math.floor(bd)
        tmax = bb if tmax is None else min(tmax, bb)
    if tmin > tmax:
        return 'T'
    for vv in 'xyz':
        j, k = [t for t in 'xyz' if t != vv]
        mj = F(Al[frozenset(vv + j)], Gg[frozenset(vv + j)]); mk = F(Al[frozenset(vv + k)], Gg[frozenset(vv + k)])
        ajk = Al[frozenset(j + k)]
        vajk = vp(ajk)
        gexp = tuple(min(Pd[vv][i], max(Pd[j][i], Pd[k][i]) + vajk[i]) for i in range(3))
        u = F(1, num(gexp))
        Lb = max(F(tmin, gamma(vv) * ajk), mj + mk - 1, F(0))
        lo = u * math.ceil(Lb / u)
        mm = min(mj, mk)
        hi = u * math.floor(mm / u)
        if hi == mm:
            barj = mj + F(ajk, Gg[frozenset(j + k)]) >= 1
            bark = mk + F(ajk, Gg[frozenset(j + k)]) >= 1
            barred = barj if mj < mk else (bark if mk < mj else (barj or bark))
            if barred:
                hi -= u
        if lo > hi:
            return 'Ppair'
    return None


def tri_tmin(P, G, AL, a, b, c):
    def gamma(y, o1, o2):
        return G[y][o1] * G[y][o2] // math.gcd(G[y][o1], G[y][o2])
    t = 1
    for (x, y, z) in ((a, b, c), (a, c, b), (b, c, a)):
        al = AL[x][y]
        gz = vp(gamma(z, x, y))
        le = tuple(P[z][i] - gz[i] for i in range(3))
        va = vp(al)
        gg = num(tuple(min(va[i], le[i]) for i in range(3)))
        term = al // gg
        t = t * term // math.gcd(t, term)
    return t


def pair_bounds(P, G, AL, vv, j, k):
    mj = F(AL[vv][j], G[vv][j]); mk = F(AL[vv][k], G[vv][k])
    tmin = tri_tmin(P, G, AL, vv, j, k)
    gam = G[vv][j] * G[vv][k] // math.gcd(G[vv][j], G[vv][k])
    ajk = AL[j][k]
    vajk = vp(ajk)
    gexp = tuple(min(P[vv][i], max(P[j][i], P[k][i]) + vajk[i]) for i in range(3))
    u = F(1, num(gexp))
    Lb = max(F(tmin, gam * ajk), mj + mk - 1, F(0))
    lo = u * math.ceil(Lb / u)
    mm = min(mj, mk)
    hi = u * math.floor(mm / u)
    if hi == mm:
        barj = mj + F(ajk, G[j][k]) >= 1
        bark = mk + F(ajk, G[j][k]) >= 1
        barred = barj if mj < mk else (bark if mk < mj else (barj or bark))
        if barred:
            hi -= u
    return lo, hi, tmin, gam


def tg_bound(P, G, AL, vv, a, b, c):
    """lower bound on mu(U_v (U_a cap U_b cap U_c)) valid for every admissible tau, or None if tau range empty."""
    tmin = tri_tmin(P, G, AL, a, b, c)
    # tau_max from the T rule (apex minimum, floor)
    def gam(y, o1, o2):
        return G[y][o1] * G[y][o2] // math.gcd(G[y][o1], G[y][o2])
    tmax = None
    for (y, x, z) in ((a, b, c), (b, a, c), (c, a, b)):
        bd = gam(y, x, z) * AL[x][z] * min(F(AL[x][y], G[x][y]), F(AL[y][z], G[y][z]))
        bb = math.floor(bd)
        tmax = bb if tmax is None else min(tmax, bb)
    L = num(tuple(max(P[a][i], P[b][i], P[c][i]) for i in range(3)))
    pidx = []
    for (x, y) in ((a, b), (a, c), (b, c)):
        lxy = num(tuple(max(P[x][i], P[y][i]) for i in range(3)))
        pidx.append(lxy * AL[x][y])
    need = 1
    for q in pidx:
        need = need * q // math.gcd(need, q)
    nv = num(P[vv])
    worst = None
    for tau in range(max(1, tmin), tmax + 1):
        if (L * tau) % need:
            continue
        t235 = tau
        rest = 1
        for p_ in (2, 3, 5):
            pass
        m = tau
        for p_ in (2, 3, 5):
            while m % p_ == 0:
                m //= p_
        gg = math.gcd(nv, L * (tau // m)) * m
        worst = gg if worst is None else max(worst, gg)
    if worst is None:
        return None
    return F(1, worst)


def rplp(P, G, AL, Q, vv):
    N = [j for j in range(7) if j != vv]
    labels = {j: lab(P[j], Q[vv][j], G[vv][j]) for j in N}
    allowed = allowed_sets(labels, N)
    forced = []
    for a in N:
        for b in N:
            if a != b:
                lo, hi, tmin, gam = pair_bounds(P, G, AL, vv, a, b)
                if tmin * G[vv][a] >= gam * AL[a][b] * AL[vv][a]:
                    forced.append((a, b))
    tight = {j for j in N if AL[vv][j] + Q[vv][j] == G[vv][j]}
    cols = []
    for r in range(1, 7):
        for Aset in itertools.combinations(N, r):
            As = set(Aset)
            if any((b in As) and (a not in As) for a, b in forced):
                continue
            for S in allowed:
                if set(S) <= As and not any((j in As) and (j not in S) for j in tight):
                    cols.append((As, set(S)))
    rows, rhs = [], []
    for j in N:
        rows.append([F(1) if j in S else F(0) for A_, S in cols]); rhs.append(F(Q[vv][j], G[vv][j]))
    for j in N:
        rows.append([F(1) if j in A_ else F(0) for A_, S in cols]); rhs.append(1 - F(AL[vv][j], G[vv][j]))
    ineq = []
    for j, k in itertools.combinations(N, 2):
        lo, hi, _, _ = pair_bounds(P, G, AL, vv, j, k)
        mj = F(AL[vv][j], G[vv][j]); mk = F(AL[vv][k], G[vv][k])
        ylo = 1 - mj - mk + lo; yhi = 1 - mj - mk + hi
        if yhi < 0:
            return 'kill(yhi<0)', None
        coef = [F(1) if (j in A_ and k in A_) else F(0) for A_, S in cols]
        ineq.append((coef, yhi, 1))
        if ylo > 0:
            ineq.append((coef, ylo, -1))
    # TG: triple granularity
    for T3 in itertools.combinations(N, 3):
        a, b, c = T3
        lb = tg_bound(P, G, AL, vv, a, b, c)
        if lb is None:
            continue
        coef = [F(1) if (A_ & set(T3)) else F(0) for A_, S in cols]
        ineq.append((coef, 1 - lb, 1))
    tot = len(ineq)
    Aeq = [row + [F(0)] * tot for row in rows]
    beq = list(rhs)
    for t, (coef, bound, sgn) in enumerate(ineq):
        sl = [F(0)] * tot
        sl[t] = F(1) if sgn > 0 else F(-1)
        Aeq.append(coef + sl); beq.append(bound)
    st, val = simplex_exact([F(1)] * len(cols) + [F(0)] * tot, Aeq, beq)
    if st == 'infeasible':
        return 'kill(infeasible)', None
    return ('kill(min>=1)' if val >= 1 else 'survive'), str(val)


def main():
    outp, inp, insha, items = sys.argv[1], sys.argv[2], sys.argv[3], json.loads(sys.argv[4])
    raw = open(inp, 'rb').read()
    if hashlib.sha256(raw).hexdigest() != insha:
        raise SystemExit('input sha mismatch')
    data = json.loads(raw)
    out = {'probe': 'exact_rplp_tg_probe_v16', 'input': inp, 'input_sha256': insha, 'results': []}
    status = 'COMPLETE'
    try:
        for ii in items:
            it = data['items'][ii]
            P = [tuple(p) for p in it['profiles']]
            G = [[num(gval(P[i], P[j])) if i != j else 0 for j in range(7)] for i in range(7)]
            for k in it.get('canonical_list', []):
                AL = [[k[i * 7 + j][0] for j in range(7)] for i in range(7)]
                AS = [[k[i * 7 + j][1] for j in range(7)] for i in range(7)]
                rec = {'item': ii, 'alpha': AL, 'alpha_star': AS}
                rec['sum_ok'] = all(AL[i][j] + AS[i][j] <= G[i][j] for i in range(7) for j in range(7) if i != j)
                rec['lfc'] = [[str(lfc_value(vv, P, G, AL[vv])), str(lfc_value(vv, P, G, AS[vv]))] for vv in range(7)]
                tri = []
                for a, b, c in itertools.combinations(range(7), 3):
                    r1 = tri_check(P[a], P[b], P[c], AL[a][b], AL[a][c], AL[b][c], G[a][b], G[a][c], G[b][c])
                    r2 = tri_check(P[a], P[b], P[c], AS[a][b], AS[a][c], AS[b][c], G[a][b], G[a][c], G[b][c])
                    if r1 or r2:
                        tri.append([a, b, c, r1, r2])
                rec['triangle_failures'] = tri
                rec['rplp'] = [[list(rplp(P, G, AL, AS, vv)), list(rplp(P, G, AS, AL, vv))] for vv in range(7)]
                out['results'].append(rec)
    except TimeoutError:
        status = 'INCOMPLETE'
    out['status'] = status
    out['seconds'] = round(time.monotonic() - T0, 3)
    fh = open(outp, 'x')
    json.dump(out, fh, indent=0)
    fh.write('\n'); fh.flush(); os.fsync(fh.fileno()); fh.close()
    print(json.dumps({'status': status, 'n': len(out['results']), 'seconds': out['seconds']}))


if __name__ == '__main__':
    main()
