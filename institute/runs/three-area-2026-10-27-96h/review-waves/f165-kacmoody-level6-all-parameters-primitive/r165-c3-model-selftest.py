#!/usr/bin/env python3
# r165 reviewer-authored control C3: validation of the independent model r165-c2-omega-model.py
# against the written definitions (descent file Section 3) and Kac-Moody relations.
import sys
sys.dont_write_bytecode = True
import json, hashlib, random, importlib.util, os
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r165model', os.path.join(HERE, 'r165-c2-omega-model.py'))
K = importlib.util.module_from_spec(spec); spec.loader.exec_module(K)

out = {'start_clock': K.clock(),
       'script_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
       'model_sha256': hashlib.sha256(open(os.path.join(HERE, 'r165-c2-omega-model.py'), 'rb').read()).hexdigest()}
checks = []
def check(name, cond, detail=None):
    checks.append({'name': name, 'pass': bool(cond), 'detail': detail})

def matF(M):
    return [[Fr(x) for x in row] for row in M]
I8 = [[Fr(int(i == j)) for j in range(8)] for i in range(8)]
def mlin(*pairs):
    R = [[Fr(0)] * 8 for _ in range(8)]
    for c, M in pairs:
        for i in range(8):
            for j in range(8):
                R[i][j] += Fr(c) * M[i][j]
    return R
def mmul8(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(8)) for j in range(8)] for i in range(8)]
def diag(v):
    return [[Fr(v[i]) if i == j else Fr(0) for j in range(8)] for i in range(8)]

# ---- T1 finite data ----
rH1, rH2 = K.rho(K.H1), K.rho(K.H2)
deg_ok = True
for k, (a, b) in enumerate(K.LET):
    for l in range(8):
        if l != k and (rH1[l][k] != 0 or rH2[l][k] != 0):
            deg_ok = False
    if rH1[k][k] != 2 * a - b - 1 or rH2[k][k] != -a + 2 * b - 1:
        deg_ok = False
check('T1_letter_degrees_from_h1_h2_weights', deg_ok)
rE1, rE2, rF1, rF2 = K.rho(K.E1), K.rho(K.E2), K.rho(K.F1), K.rho(K.F2)
rZ = K.rho(K.comm(K.E1, K.E2))
def col(M, k):
    return [M[l][k] for l in range(8)]
def unit(k):
    return [Fr(int(l == k)) for l in range(8)]
chain = [(rE1, 0, 1), (rE2, 0, 2), (rZ, 0, 3), (rE1, 2, 4), (rZ, 1, 5), (rZ, 2, 6), (rZ, 3, 7)]
check('T1_basis_chain_v_Xv_Yv_Zv_XYv_ZXv_ZYv_Z2v', all(col(M, s) == unit(t) for M, s, t in chain))
check('T1_Z_is_E13', K.comm(K.E1, K.E2) == K.Em(1, 3))
claimed = [[Fr(int(i == j)) for j in range(8)] for i in range(8)]
claimed[3][3] = claimed[4][4] = Fr(2); claimed[3][4] = claimed[4][3] = Fr(1); claimed[7][7] = Fr(4)
check('T1_gram_matches_written_G', K.GRAM == claimed, [[str(x) for x in r] for r in K.GRAM])
check('T1_ginv_times_gram_identity', mmul8(K.GINV, K.GRAM) == I8)
out['SIGMA'] = K.SIGMA; out['LAMBDA'] = K.LAMBDA; out['KW'] = {f'{i},{j}': v for (i, j), v in K.KW.items()}
# invariance of the pairing beta(u,w)=tr(B_u B_w^T) under l
inv_ok = True
for Z in (K.E1, K.E2, K.F1, K.F2, K.H1, K.H2):
    for i in range(8):
        for j in range(8):
            d = K.coords(K.comm(Z, K.BM[i]))                      # z.u_i
            c = K.coords(K.tp(K.comm(Z, K.tp(K.BM[j]))))          # z.w_j in w-coordinates
            val = sum(d[l] * K.GRAM[l][j] for l in range(8)) + sum(c[l] * K.GRAM[i][l] for l in range(8))
            if val != 0:
                inv_ok = False
check('T1_pairing_beta_is_l_invariant', inv_ok)
# M^- structure sanity: w0=f3 killed by e1,e2; [f1,w0]=-w1, [f2,w0]=-w2
cw = lambda Z, j: K.coords(K.tp(K.comm(Z, K.tp(K.BM[j]))))
check('T1_e1_e2_kill_w0_f3', cw(K.E1, 0) == [0] * 8 and cw(K.E2, 0) == [0] * 8)
check('T1_f1w0_eq_minus_w1_f2w0_eq_minus_w2', cw(K.F1, 0) == [-x for x in unit(1)] and cw(K.F2, 0) == [-x for x in unit(2)])
# explicit brackets from Chevalley relations
P = K.PENCIL
A_ = [Fr(a) for a, b in K.LET]; B_ = [Fr(b) for a, b in K.LET]
check('T1_[w0,u0]=[f3,e3]=-h3', P[(0, 0)] == (diag([-2] * 8), diag(A_), diag(B_)))
Z8 = diag([0] * 8)
check('T1_[w0,u1]=-r e1', P[(0, 1)] == (Z8, mlin((-1, rE1)), Z8))
check('T1_[w0,u2]=-s e2', P[(0, 2)] == (Z8, Z8, mlin((-1, rE2))))
check('T1_[w1,u0]=-r f1', P[(1, 0)] == (Z8, mlin((-1, rF1)), Z8))
check('T1_[w2,u0]=-s f2', P[(2, 0)] == (Z8, Z8, mlin((-1, rF2))))
check('T1_[w1,u1]=-h3-r h1', P[(1, 1)] == (diag([-2] * 8), mlin((1, diag(A_)), (-1, rH1)), diag(B_)))
# local Jacobi / l-equivariance of the bracket M^- x M -> g0, componentwise
eq_ok = True
for Z in (K.E1, K.E2, K.F1, K.F2, K.H1, K.H2):
    rz = K.rho(Z)
    for j in range(8):
        c = cw(Z, j)
        for k in range(8):
            d = K.coords(K.comm(Z, K.BM[k]))
            for q in range(3):
                G = P[(j, k)][q]
                lhs = mlin((1, mmul8(rz, G)), (-1, mmul8(G, rz)))
                rhs = mlin(*([(c[l], P[(l, k)][q]) for l in range(8)] + [(d[l], P[(j, l)][q]) for l in range(8)]))
                if lhs != rhs:
                    eq_ok = False
check('T1_bracket_l_equivariant_all_j_k_components', eq_ok)

# ---- T2 recursion F on the free Lie algebra ----
def adv_power(letter, k):
    x, n = {letter: 1}, 1
    for _ in range(k):
        x = K.bracket_dict({0: 1}, 1, x, n); n += 1
    return x, n
serre_ok, serre_neg_ok = True, True
for r0 in range(1, 8):
    s1, n1 = adv_power(1, r0)
    s2, n2 = adv_power(2, r0)
    for r in range(1, 10):
        z1 = K.F_numeric(0, s1, n1, r, 4)
        z2 = K.F_numeric(0, s2, n2, 4, r)
        if (len(z1) == 0) != (r == r0) or (len(z2) == 0) != (r == r0):
            serre_ok = False
    if K.der_dict(K.RHO_F1, s1, n1) or K.der_dict(K.RHO_F2, s1, n1) or K.der_dict(K.RHO_F1, s2, n2) or K.der_dict(K.RHO_F2, s2, n2):
        serre_ok = False
check('T2_f3_kills_(ad e3)^(1+r)e1_exactly_when_r_matches_and_f1f2_kill', serre_ok)

random.seed(165)
def rand_lie(n):
    x, m = {random.randrange(8): 1}, 1
    while m < n:
        x = K.bracket_dict({random.randrange(8): 1}, 1, x, m); m += 1
    return x
def lie_residual_zero(x, n):
    bydeg = {}
    for code, c in x.items():
        ls = K.letters(code, n)
        dg = (sum(K.LET[t][0] for t in ls), sum(K.LET[t][1] for t in ls))
        bydeg.setdefault(dg, {})[code] = c
    for (a, b), part in bydeg.items():
        _, lw = K.lyndon_basis(n, a, b)
        _, rem = K.lie_coordinates(part, n, lw)
        if rem:
            return False
    return True
lie_ok, rel_ok, def_ok, h3_ok = True, True, True, True
samples = 0
for trial in range(12):
    n = random.choice([3, 4, 5])
    x = K.add_dicts((1, rand_lie(n)), (random.choice([1, -2, 3]), rand_lie(n)))
    if not x:
        continue
    samples += 1
    r, s = random.randint(1, 9), random.randint(1, 9)
    for j in range(8):
        Fx = K.F_numeric(j, x, n, r, s)
        if Fx and not lie_residual_zero(Fx, n - 1):
            lie_ok = False
        for Z, cols, sz in ((K.E1, K.RHO_E1, 2), (K.E2, K.RHO_E2, 2), (K.F1, K.RHO_F1, 1), (K.F2, K.RHO_F2, 1)):
            lhs = K.add_dicts((1, K.der_dict(cols, Fx, n - 1)), (-1, K.F_numeric(j, K.der_dict(cols, x, n), n, r, s)))
            c = cw(Z, j)
            qs = [c[l] * sz for l in range(8)]
            D = 1
            for q in qs:
                D = D * q.denominator // __import__('math').gcd(D, q.denominator)
            rhs = {}
            for l in range(8):
                if qs[l]:
                    rhs = K.add_dicts((1, rhs), (int(qs[l] * D), K.F_numeric(l, x, n, r, s)))
            if K.add_dicts((D, lhs)) != rhs:
                rel_ok = False
        for kk in range(8):
            ux = K.bracket_dict({kk: 1}, 1, x, n)
            lhs = K.F_numeric(j, ux, n + 1, r, s)
            G0, Gr, Gs = P[(j, kk)]
            Gnum = [[(G0[l][m] + r * Gr[l][m] + s * Gs[l][m]) * K.SIGMA for m in range(8)] for l in range(8)]
            cols = K.int_sparse_cols(Gnum, 1)
            rhs = K.add_dicts((1, K.der_dict(cols, x, n)), (1, K.bracket_dict({kk: 1}, 1, Fx, n - 1)))
            if lhs != rhs:
                def_ok = False
check('T2_F_maps_Lie_elements_to_Lie_elements', lie_ok, samples)
check('T2_[z,w_j]_relations_z_in_e1e2f1f2', rel_ok)
check('T2_F_j([u_k,x])=[w_j,u_k].x+[u_k,F_j x]', def_ok)

# ---- T3 lowest vectors at level 4 (exact) ----
def exact_kernel(rows, ncols):
    A = [[Fr(x) for x in r] for r in rows]
    piv, rr = [], 0
    for c in range(ncols):
        pr = next((i for i in range(rr, len(A)) if A[i][c] != 0), None)
        if pr is None:
            continue
        A[rr], A[pr] = A[pr], A[rr]
        pv = A[rr][c]
        A[rr] = [v / pv for v in A[rr]]
        for i in range(len(A)):
            if i != rr and A[i][c] != 0:
                f = A[i][c]
                A[i] = [v - f * w for v, w in zip(A[i], A[rr])]
        piv.append(c); rr += 1
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fcol in free:
        v = [Fr(0)] * ncols
        v[fcol] = Fr(1)
        for i, pc in enumerate(piv):
            v[pc] = -A[i][fcol]
        basis.append(v)
    return basis
def lowest_space(n, a, b):
    ws, lw = K.lyndon_basis(n, a, b)
    exps = [K.expand(tuple(K.letters(w, n))) for w in lw]
    rows = {}
    for jcol, e in enumerate(exps):
        for cols in (K.RHO_F1, K.RHO_F2):
            img = K.der_dict(cols, e, n)
            for key, v in img.items():
                rows.setdefault((id(cols), key), [0] * len(lw))[jcol] += v
    basis = exact_kernel(list(rows.values()), len(lw))
    vecs = []
    for v in basis:
        den = 1
        for q in v:
            den = den * q.denominator // __import__('math').gcd(den, q.denominator)
        x = {}
        for coef, e in zip(v, exps):
            if coef:
                for key, val in e.items():
                    x[key] = x.get(key, 0) + int(coef * den) * val
        vecs.append({k: c for k, c in x.items() if c})
    return vecs, exps
def F12(d, n):
    return K.add_dicts((1, K.der_dict(K.RHO_F2, K.der_dict(K.RHO_F1, d, n), n)),
                       (-1, K.der_dict(K.RHO_F1, K.der_dict(K.RHO_F2, d, n), n)))
def jacobi_list(d, n):
    f1 = lambda y, m: K.der_dict(K.RHO_F1, y, m)
    f2 = lambda y, m: K.der_dict(K.RHO_F2, y, m)
    neg = lambda y: {k: -v for k, v in y.items()}
    return [d, neg(f1(d, n)), neg(f2(d, n)), neg(F12(d, n)), f1(f2(d, n), n), f1(F12(d, n), n),
            f2(F12(d, n), n), F12(F12(d, n), n)]
def omega_numeric(x, n, r, s, weights):
    res = {}
    for (i, j), kw in weights.items():
        Fx = K.F_numeric(j, x, n, r, s)
        res = K.add_dicts((1, res), (kw, K.bracket_dict({i: 1}, 1, Fx, n - 1)))
    return res
alt = {(i, i): 12 for i in range(8)}   # deliberately NON-invariant contraction (Gram replaced by identity)
jac_ok, jac_neg_fails, inv_P_ok, alt_breaks, tested_types = True, False, True, False, []
for (a, b) in [(3, 3), (2, 3), (3, 2), (2, 2), (1, 2)]:
    n = 4
    vecs, exps = lowest_space(n, a, b)
    if not vecs:
        continue
    tested_types.append([a, b, n, len(vecs)])
    r, s = 7, 3
    for x in vecs:
        d = K.F_numeric(0, x, n, r, s)
        jl = jacobi_list(d, n - 1)
        for j in range(8):
            if K.F_numeric(j, x, n, r, s) != jl[j]:
                jac_ok = False
        Ox = omega_numeric(x, n, r, s, K.KW)
        if K.der_dict(K.RHO_F1, Ox, n) or K.der_dict(K.RHO_F2, Ox, n):
            inv_P_ok = False
        Oa = omega_numeric(x, n, r, s, alt)
        if K.der_dict(K.RHO_F1, Oa, n) or K.der_dict(K.RHO_F2, Oa, n):
            alt_breaks = True
    # negative: a non-lowest Lie element violates the j=1 identity
    for e in exps:
        if K.der_dict(K.RHO_F1, e, n):
            d = K.F_numeric(0, e, n, r, s)
            if K.F_numeric(1, e, n, r, s) != jacobi_list(d, n - 1)[1]:
                jac_neg_fails = True
            break
out['T3_tested_types'] = tested_types
check('T3_eight_inner_brackets_equal_written_negative_Levi_words_on_D3x', jac_ok)
check('T3_Omega_preserves_lowest_space', inv_P_ok)
check('T3_NEG_identity_fails_off_lowest_space', jac_neg_fails)
check('T3_NEG_noninvariant_contraction_leaves_lowest_space', alt_breaks)
# kerD3 subset kerOmega on a genuine kernel: Serre-type lowest vector (ad v)^r u1 at level r+1
kk_ok = True
for r0 in (2, 3, 4, 5):
    sv, nv = adv_power(1, r0)
    if K.F_numeric(0, sv, nv, r0, 6) or omega_numeric(sv, nv, r0, 6, K.KW):
        kk_ok = False
    if not omega_numeric(sv, nv, r0 + 1, 6, K.KW):
        kk_ok = False
check('T3_D3=0_forces_Omega=0_on_seed_vectors_and_Omega_nonzero_off_root', kk_ok)
out['checks'] = checks
out['all_pass'] = all(c['pass'] for c in checks)
out['end_clock'] = K.clock()
print(json.dumps(out, indent=1, default=str))
