#!/usr/bin/env python3
"""f166 independent reviewer controls (ReviewF166RankTwo). Independently authored; imports no author code.

Parts
  A  explicit 9-variable Boolean functions: exact integer Walsh (FWHT + direct), caller facts, u/w inverses,
     q/Q polar, collective Parseval, block Poisson identity, generalized mod-3 split, L1 parity,
     Z8 coset constancy mod 32 and residue formula; negative controls (T=0, perturbed formal spectrum).
  B  quadratic forms: zero counts per polar rank, odd-half Q weights, rank-4 dual-phase facts.
  C  low-rank profile enumeration under the packet's stated constraints vs. with the disclaimed m≡1-D filter.
  D  local coset lemmas: 81-vector class table, L4 integer family, exhaustive e=2 / e=4 tau geometry, flat fact.
  E  exhaustive class/region integer model for every rank-two case of the coset packet (relaxation: infeasible
     here => infeasible there), counting-only positive controls, exploratory m=116/114 probes.
  F  withdrawal / erratum polynomial counterexamples.
  G  lattice test: does dual-code (binomial-moment) integrality force E2 parity?
  H  Z>=8 derivation controls: degree of 1_{Z8} on K versus polar rank on actual functions.
"""
import itertools, json, sys, time
from collections import Counter, defaultdict
from math import comb
import numpy as np

T_START = time.time()
OUT = {}

def pc(x):
    return bin(x).count('1')

# ---------------------------------------------------------------- generic GF(2) / transform helpers
def fwht(v):
    a = np.array(v, dtype=np.int64).copy(); n = a.shape[0]; h = 1
    while h < n:
        a = a.reshape(-1, 2, h); x = a[:, 0, :].copy(); y = a[:, 1, :].copy()
        a[:, 0, :] = x + y; a[:, 1, :] = x - y; a = a.reshape(n); h *= 2
    return a

H9 = np.array([[(-1) ** pc(a & x) for x in range(512)] for a in range(512)], dtype=np.int64)

def anf_degree(tt, n):
    a = np.array(tt, dtype=np.int64) % 2; h = 1
    while h < (1 << n):
        a = a.reshape(-1, 2, h); a[:, 1, :] ^= a[:, 0, :]; a = a.reshape(1 << n); h *= 2
    return max((pc(i) for i in range(1 << n) if a[i]), default=-1)

def gf2_rank(vecs, nbits):
    rows = list(vecs); r = 0
    for bit in range(nbits):
        piv = next((k for k in range(r, len(rows)) if (rows[k] >> bit) & 1), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for k in range(len(rows)):
            if k != r and (rows[k] >> bit) & 1:
                rows[k] ^= rows[r]
        r += 1
    return r

def indep(vecs, nbits=9):
    return gf2_rank(vecs, nbits) == len(vecs)

def polar_rank(qtt, n):
    rows = []
    for i in range(n):
        r = 0
        for j in range(n):
            if i != j:
                r |= (qtt[(1 << i) ^ (1 << j)] ^ qtt[1 << i] ^ qtt[1 << j] ^ qtt[0]) << j
        rows.append(r)
    return gf2_rank(rows, n)

def apply(cols, x):
    y = 0; j = 0
    while x:
        if x & 1:
            y ^= cols[j]
        x >>= 1; j += 1
    return y

def gf2_inv_cols(cols, n):
    M = [[(cols[j] >> i) & 1 for j in range(n)] for i in range(n)]
    I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c])
        M[c], M[p] = M[p], M[c]; I[c], I[p] = I[p], I[c]
        for r in range(n):
            if r != c and M[r][c]:
                M[r] = [a ^ b for a, b in zip(M[r], M[c])]; I[r] = [a ^ b for a, b in zip(I[r], I[c])]
    return [sum(I[i][j] << i for i in range(n)) for j in range(n)]

def inv_transpose_cols(cols, n):
    inv = gf2_inv_cols(cols, n)
    return [sum(((inv[i] >> j) & 1) << i for i in range(n)) for j in range(n)]

def is_affine_set(S):
    S = list(S)
    if not S or (len(S) & (len(S) - 1)):
        return False
    a0 = S[0]; L = {x ^ a0 for x in S}
    return all((x ^ y) in L for x in L for y in L)

def subspaces(n, d):
    seen = set(); out = []
    for basis in itertools.combinations(range(1, 2 ** n), d):
        span = [0]
        for b in basis:
            span = span + [x ^ b for x in span]
        fs = frozenset(span)
        if len(fs) == 2 ** d and fs not in seen:
            seen.add(fs); out.append(fs)
    return out

# ---------------------------------------------------------------- Part A: explicit Boolean functions
def t_last(f, T):
    basis = []
    for e in range(9):
        if len(basis) == 8:
            break
        if indep(basis + [1 << e, T]):
            basis.append(1 << e)
    M = basis + [T]
    return np.array([f[apply(M, x)] for x in range(512)], dtype=np.int64)

def control_function(f, seed):
    rep = {}
    f = np.array(f, dtype=np.int64)
    S = [x for x in range(512) if f[x]]
    rep['support'] = len(S)
    T = 0
    for x in S:
        T ^= x
    rep['T'] = T
    F = (-1) ** f
    W = fwht(F)
    rep['fwht_equals_direct_character_sums'] = bool(np.array_equal(W, H9 @ F))
    rep['W0'] = int(W[0]); rep['peak'] = int(np.abs(W).max())
    rep['all_W_divisible_by_4'] = bool(np.all(W % 4 == 0))
    k = W // 4
    ind = np.zeros(512, dtype=np.int64); ind[S] = 1
    Na = (256 - H9 @ ind) // 2
    rep['k_eq_Na_minus_128_for_a_ne_0'] = bool(np.all(k[1:] == Na[1:] - 128))
    rep['k_parity_eq_a_dot_T'] = bool(all((int(k[a]) - pc(a & T)) % 2 == 0 for a in range(512)))
    rep['odd_k_count'] = int(np.sum(k % 2 != 0))
    if T == 0:
        return rep
    fp = t_last(f, T)
    Sp = [x for x in range(512) if fp[x]]; Tp = 0
    for x in Sp:
        Tp ^= x
    rep['T_moved_to_e8'] = (Tp == 256)
    Fp = (-1) ** fp; Wp = fwht(Fp); kp = Wp // 4
    rep['spectrum_multiset_preserved'] = bool(np.array_equal(np.sort(np.abs(W)), np.sort(np.abs(Wp))))
    u = (Fp[:256] + Fp[256:]) // 2; w = (Fp[:256] - Fp[256:]) // 2
    m = int(np.sum(u != 0)); rep['m'] = m; rep['sum_u'] = int(u.sum())
    rep['supports_u_w_complementary'] = bool(np.all(np.abs(u) + np.abs(w) == 1))
    What = fwht(u)
    rep['Walsh_u_eq_2k_even_half'] = bool(np.array_equal(What, 2 * kp[:256]))
    rep['Walsh_w_eq_2k_odd_half'] = bool(np.array_equal(fwht(w), 2 * kp[256:]))
    rep['Walsh_k_even_eq_128u'] = bool(np.array_equal(fwht(kp[:256]), 128 * u))
    rep['Walsh_k_odd_eq_128w'] = bool(np.array_equal(fwht(kp[256:]), 128 * w))
    rep['Parseval_even_eq_64m'] = bool(int(np.sum(kp[:256] ** 2)) == 64 * m)
    rep['Parseval_odd_eq_64(256-m)'] = bool(int(np.sum(kp[256:] ** 2)) == 64 * (256 - m))
    rep['m_even'] = (m % 2 == 0)
    q = [(int(v) // 2) % 2 for v in kp[:256]]
    Q = [1 if int(v) % 4 == 3 else 0 for v in kp[256:]]
    rep['anf_degree_q'] = anf_degree(q, 8); rep['anf_degree_Q'] = anf_degree(Q, 8)
    ind_p = np.zeros(512, dtype=np.int64); ind_p[Sp] = 1
    Nap = (256 - H9 @ ind_p) // 2
    rep['q_eq_binom(N_a,2)_mod2'] = bool(all(q[a] == (int(Nap[a]) * (int(Nap[a]) - 1) // 2) % 2 for a in range(256)))
    qa = np.array(q); Qa = np.array(Q); idx = np.arange(256)
    Bq = qa[idx[:, None] ^ idx[None, :]] ^ qa[:, None] ^ qa[None, :] ^ qa[0]
    BQ = Qa[idx[:, None] ^ idx[None, :]] ^ Qa[:, None] ^ Qa[None, :] ^ Qa[0]
    rep['Q_has_same_polar_as_q'] = bool(np.array_equal(Bq, BQ))
    pr = polar_rank(q, 8); rep['polar_rank'] = pr; rep['z'] = 256 - sum(q)
    rep['general_mod3_m_eq_#odd_3|k'] = bool((m - int(np.sum(kp[256:] % 3 == 0))) % 3 == 0)
    g = np.array([(-1) ** x for x in Q]); Wg = fwht(g)
    Y = np.nonzero(Wg)[0]; t = pr // 2; L = 2 ** (8 - t)
    rep['Y_size'] = int(len(Y)); rep['Y_size_eq_4^t_and_mag_eq_2^(8-t)'] = bool(len(Y) == 4 ** t and np.all(np.abs(Wg[Y]) == L))
    sig = np.sign(Wg[Y]); Wk = fwht(kp[256:])
    rep['collective_Parseval_sum_Y_sigma_Wk_eq_2^t_sum_kg'] = bool(int(np.sum(sig * Wk[Y])) == 2 ** t * int(np.sum(kp[256:] * g)))
    rep['v_on_Y_in_{-1,0,1}'] = bool(np.all(np.isin(Wk[Y] // 128, [-1, 0, 1])) and np.all(Wk[Y] % 128 == 0))
    y0 = int(Y[0]); Ly = [int(y) ^ y0 for y in Y]
    rep['Y_affine_subspace'] = is_affine_set([int(y) for y in Y])
    bas = []
    for y in Ly:
        if y and indep(bas + [y], 8):
            bas.append(y)
    sd = {int(y): int(s) for y, s in zip(Y, sig)}
    if bas:
        phi = [0 if sd[y0 ^ apply(bas, i)] == 1 else 1 for i in range(1 << len(bas))]
        rep['sigma_on_Y_quadratic'] = anf_degree(phi, len(bas)) <= 2
        rep['sigma_on_Y_polar_rank'] = polar_rank(phi, len(bas))
    # block Poisson identity, generalized mod-3 split, parity facts (coordinate split and one random split)
    pois = parity = mod3 = L1 = True
    rng = np.random.default_rng(seed + 7)
    for trial in range(2):
        if trial == 0:
            Acols = [1 << i for i in range(8)]
        else:
            while True:
                Acols = [int(x) for x in rng.integers(1, 256, size=8)]
                if indep(Acols, 8):
                    break
        P = inv_transpose_cols(Acols, 8)
        upts = np.array([u[apply(P, y)] for y in range(256)])
        Wnew = np.array([What[apply(Acols, a)] for a in range(256)])
        assert np.array_equal(fwht(upts), Wnew)
        Ub = np.zeros((4, 64), dtype=np.int64); n_c = np.zeros(64, dtype=np.int64)
        for c in range(64):
            for zz in range(4):
                val = int(upts[c + 64 * zz]); n_c[c] += abs(val)
                for s in range(4):
                    Ub[s, c] += val * (-1) ** pc(s & zz)
        nodd = int(np.sum(n_c % 2))
        for s in range(4):
            blk = Wnew[64 * s:64 * s + 64]
            if not np.array_equal(fwht(Ub[s]), blk):
                pois = False
            if not np.array_equal(64 * Ub[s], fwht(blk)):
                pois = False
            if not np.all((Ub[s] - n_c) % 2 == 0):
                parity = False
            if (int(np.sum(Ub[s] ** 2)) - nodd) % 4:
                L1 = False
            if np.any(blk % 4):
                mod3 = False; continue
            vs = blk // 4
            tau = ((vs + 1) % 3) - 1; sg = (vs + 2 * tau) // 3
            if not (np.array_equal(vs, 3 * sg - 2 * tau) and np.array_equal(16 * Ub[s], 3 * fwht(sg) - 2 * fwht(tau))
                    and np.all((fwht(tau) - Ub[s]) % 3 == 0)):
                mod3 = False
        if not np.array_equal((Ub ** 2).sum(0), 4 * n_c):
            parity = False
    rep['block_Poisson_W(r,s)=sum_c U_s(c)(-1)^{r.c}_and_inverse'] = pois
    rep['block_U_s≡n_c_mod2_and_sum_s_U_s^2=4n_c'] = parity
    rep['generalized_mod3_16U=3W(sigma)-2W(tau)_and_t≡U_mod3'] = mod3
    rep['L1_sum_c_U_s^2≡#odd_n_c_mod4_all_s'] = L1
    # Z8 coset constancy mod 32 + residue formula, random 5-dim L inside K
    kev = kp[:256]; Z8 = (kev % 8 == 0)
    const = resid = True
    rng2 = np.random.default_rng(seed + 99)
    for trial in range(60):
        while True:
            Lb = [int(x) for x in rng2.integers(1, 256, size=5)]
            if indep(Lb, 8):
                break
        Lset = [apply(Lb, i) for i in range(32)]
        seen = set(); cosets = []
        for b0 in range(256):
            if b0 in seen:
                continue
            cs = [b0 ^ l for l in Lset]; seen |= set(cs); cosets.append(cs)
        sums = [int(np.sum(kev[cs] ** 2)) for cs in cosets]
        if len({s_ % 32 for s_ in sums}) != 1:
            const = False
        for cs, s_ in zip(cosets, sums):
            wq = sum(q[a] for a in cs)
            if wq % 4 or (s_ - 16 * (wq // 4 + int(Z8[cs].sum()))) % 32:
                resid = False
    rep['Z8_sum_A_k^2_constant_mod32_over_cosets_of_L'] = const
    rep['Z8_residue_formula_mod32'] = resid
    rep['deg_1_Z8_on_K'] = anf_degree([1 if v else 0 for v in Z8], 8)
    rep['Z8_size'] = int(Z8.sum())
    return rep

def random_balanced(seed):
    rng = np.random.default_rng(seed)
    f = np.zeros(512, dtype=np.int64); f[rng.choice(512, 256, replace=False)] = 1
    return f

partA = {'random': [], 'low_polar_rank_swaps': [], 'negative': {}}
for seed in (20261029, 20261030, 20261031, 20261032):
    f = random_balanced(seed)
    partA['random'].append(dict(seed=seed, **control_function(f, seed)))
# actual high-peak low-polar-rank functions: affine hyperplane complement with r point swaps
S0 = [x for x in range(512) if (x >> 8) & 1]; notS0 = [x for x in range(512) if not (x >> 8) & 1]
rng = np.random.default_rng(11)
want = {}
for trial in range(400):
    r = int(rng.integers(1, 4))
    rem = [int(x) for x in rng.choice(S0, r, replace=False)]; add = [int(x) for x in rng.choice(notS0, r, replace=False)]
    S = (set(S0) - set(rem)) | set(add)
    T = 0
    for x in S:
        T ^= x
    if T == 0:
        continue
    f = np.zeros(512, dtype=np.int64); f[list(S)] = 1
    kk = fwht((-1) ** f) // 4
    fp = t_last(f, T); kp = fwht((-1) ** fp) // 4
    qq = [(int(v) // 2) % 2 for v in kp[:256]]
    key = (polar_rank(qq, 8), 256 - sum(qq))
    if key not in want:
        want[key] = (trial, sorted(rem), sorted(add), f)
for key in sorted(want):
    trial, rem, add, f = want[key]
    partA['low_polar_rank_swaps'].append(dict(removed=rem, added=add, **control_function(f, 500 + trial)))
# negative 1: balanced T=0 function (odd half disappears)
f = random_balanced(777); S = [x for x in range(512) if f[x]]; T = 0
for x in S:
    T ^= x
if T:
    x = next(x for x in S if not f[x ^ T]); f[x] = 0; f[x ^ T] = 1
partA['negative']['T_zero_function'] = control_function(f, 777)
# negative 2: perturbed formal even-half spectrum (k + 4 at one q-zero frequency): not a Boolean spectrum
f = random_balanced(20261029); S = [x for x in range(512) if f[x]]; T = 0
for x in S:
    T ^= x
fp = t_last(f, T); kp = fwht((-1) ** fp) // 4; kev = kp[:256].copy()
a0 = next(a for a in range(1, 256) if int(kev[a]) % 4 == 0)
kpert = kev.copy(); kpert[a0] += 4
inv = fwht(kpert)
neg2 = {'a0': a0, 'k_a0': int(kev[a0]), 'q_unchanged': (int(kev[a0]) // 2) % 2 == (int(kpert[a0]) // 2) % 2,
        'inverse_128u_integral_actual': bool(np.all(fwht(kev) % 128 == 0)),
        'inverse_128u_integral_perturbed': bool(np.all(inv % 128 == 0))}
qv = [(int(v) // 2) % 2 for v in kpert]; Z8p = (kpert % 8 == 0)
rng3 = np.random.default_rng(5); fails = 0; resid_ok = True; trials = 0
for trial in range(60):
    while True:
        Lb = [int(x) for x in rng3.integers(1, 256, size=5)]
        if indep(Lb, 8):
            break
    Lset = [apply(Lb, i) for i in range(32)]; seen = set(); cosets = []
    for b0 in range(256):
        if b0 in seen:
            continue
        cs = [b0 ^ l for l in Lset]; seen |= set(cs); cosets.append(cs)
    sums = [int(np.sum(kpert[cs] ** 2)) for cs in cosets]
    trials += 1
    if len({s_ % 32 for s_ in sums}) != 1:
        fails += 1
    for cs, s_ in zip(cosets, sums):
        wq = sum(qv[a] for a in cs)
        if (s_ - 16 * (wq // 4 + int(Z8p[cs].sum()))) % 32:
            resid_ok = False
neg2['coset_constancy_failures_out_of_trials'] = [fails, trials]
neg2['pointwise_residue_formula_still_holds'] = resid_ok
# block-level perturbation: Ŵ + 4 at one frequency breaks integrality of U_s
u = (((-1) ** fp)[:256] + ((-1) ** fp)[256:]) // 2; What = fwht(u); Wpert = What.copy(); Wpert[64 * 1 + 5] += 4
neg2['block_U_integral_actual'] = bool(np.all(fwht(What[64:128]) % 64 == 0))
neg2['block_U_integral_perturbed'] = bool(np.all(fwht(Wpert[64:128]) % 64 == 0))
partA['negative']['perturbed_formal_spectrum'] = neg2
OUT['A_boolean_function_controls'] = partA
print('Part A done', round(time.time() - T_START, 1), flush=True)

# ---------------------------------------------------------------- Part B: quadratic forms
def quad_tt(t, lam, const=0, n=8):
    return [(sum(((x >> (2 * i)) & 1) * ((x >> (2 * i + 1)) & 1) for i in range(t)) + pc(lam & x) + const) % 2 for x in range(1 << n)]
zero_counts = {}
for t in range(5):
    zs = set()
    for lam in range(256):
        tt = quad_tt(t, lam); assert polar_rank(tt, 8) == 2 * t
        zs.add(256 - sum(tt))
    zero_counts[str(2 * t)] = sorted(zs)
rngB = np.random.default_rng(5); consistent = True
for trial in range(300):
    Bm = np.triu(rngB.integers(0, 2, size=(8, 8)), 1); lam = int(rngB.integers(0, 256))
    vec = lambda x: np.array([(x >> i) & 1 for i in range(8)])
    tt = [(int(vec(x) @ Bm @ vec(x)) + pc(lam & x)) % 2 for x in range(256)]
    if str(polar_rank(tt, 8)) not in zero_counts or (256 - sum(tt)) not in zero_counts[str(polar_rank(tt, 8))]:
        consistent = False
qan = [(((x >> 6) & 1) * ((x >> 7) & 1) + ((x >> 6) & 1) + ((x >> 7) & 1)) % 2 for x in range(256)]
Qw = Counter(); rad0 = Counter(); radnz = Counter()
for lam in range(256):
    for c in (0, 1):
        wgt = sum((qan[x] + pc(lam & x) + c) % 2 for x in range(256))
        Qw[wgt] += 1; (rad0 if (lam & 63) == 0 else radnz)[wgt] += 1
phases = []
for lam in range(16):
    for c in (0, 1):
        phases.append([((x & 1) * ((x >> 1) & 1) + ((x >> 2) & 1) * ((x >> 3) & 1) + pc(lam & x) + c) % 2 for x in range(16)])
def aff_flats(n, d):
    out = set()
    for V in subspaces(n, d):
        for c in range(1 << n):
            out.add(frozenset(x ^ c for x in V))
    return list(out)
F3_4 = aff_flats(4, 3); F2_4 = aff_flats(4, 2)
def affine_on(ph, A):
    A = sorted(A); a0 = A[0]
    return all((ph[a0] ^ ph[a] ^ ph[b] ^ ph[a ^ b ^ a0]) == 0 for a in A for b in A)
H4 = np.array([[(-1) ** pc(a & x) for x in range(16)] for a in range(16)])
half_ok = True; iso2 = set(); iso3 = 0
for ph in phases:
    sg = np.array([(-1) ** v for v in ph])
    iso3 += sum(affine_on(ph, A) for A in F3_4)
    cnt = 0
    for A in F2_4:
        if not affine_on(ph, A):
            continue
        cnt += 1
        ind = np.array([1 if x in A else 0 for x in range(16)])
        tr = H4 @ (sg * (2 - 6 * ind)); supp = np.nonzero(H4 @ (sg * ind))[0]
        rest = [xi for xi in range(16) if xi not in supp]
        if len(supp) != 4 or not all(abs(int(tr[xi])) == 8 for xi in rest) or not np.all(np.abs(H4 @ sg) == 4):
            half_ok = False
    iso2.add(cnt)
OUT['B_quadratic_forms'] = dict(zero_counts_q0_eq0_by_polar_rank=zero_counts, random_quadratics_consistent=consistent,
    odd_Q_weights_fixed_rank2_anisotropic_polar=dict(sorted(Qw.items())),
    Q_weights_radical_linear_term_zero=dict(sorted(rad0.items())), Q_weights_radical_linear_term_nonzero=dict(sorted(radnz.items())),
    rank4_phases=len(phases), affine_3flats_F2_4=len(F3_4), phases_affine_on_some_3flat=iso3,
    affine_2flats_per_phase_where_affine=sorted(iso2), half_integer_obstruction_all=half_ok)
print('Part B done', round(time.time() - T_START, 1), flush=True)

# ---------------------------------------------------------------- Part C: profile enumeration
def enum_profiles(rank, spurious=False):
    out = set(); withS = set()
    if rank == 2:
        Ds = (12, 16, 20, 24, 28); Srange = range(-4, 5); coef = 2; z = 64; mmax = 122
    else:
        Ds = range(8, 25, 2); Srange = range(-16, 17); coef = 1; z = 96; mmax = 112
    for D in Ds:
        for S in Srange:
            m = 116 + D // 2 + coef * S
            if m > mmax or m % 2 or 64 * m > 9216 - 20 * z - 16 * 1:
                continue
            if spurious and (m - (1 - D)) % 3:
                continue
            for n1 in range(D + 1):
                n3 = D - n1
                if (m - n3) % 3:
                    continue
                num = 8 * (m - 60) - 6 * n1 - 5 * n3
                if num % 3:
                    continue
                n5 = num // 3; n7 = 256 - D - n5
                if n5 < 0 or n7 < 0:
                    continue
                # independent consistency: odd energy and collective identity (5)
                assert n1 + 9 * n3 + 25 * n5 + 49 * n7 == 64 * (256 - m)
                assert 3 * (n3 + n5) - 2 * (n3 - n1) == 448 + (16 if rank == 2 else 8) * S
                out.add((D, m, n1, n3, n5, n7)); withS.add((D, m, S))
    return out, withS
partC = {}
for rank, z in ((2, 64), (4, 96)):
    for sp in (False, True):
        P, PS = enum_profiles(rank, sp)
        pairs = sorted({(p[0], p[1]) for p in P}); mmin = min(p[1] for p in P)
        partC[f'rank{rank}_{"with_disclaimed_m≡1-D_filter" if sp else "stated_constraints"}'] = dict(
            profiles=len(P), DM_pairs=pairs, S_values_by_pair=sorted(PS), n7_min=min(p[5] for p in P), n7_max=max(p[5] for p in P),
            m_min=mmin, Z_max_from_even_bound=(9216 - 20 * z - 64 * mmin) // 16)
cp = dict(D=12, m=114, S=-4, n1=12, n3=0, n5=120, n7=124)
cp_checks = dict(D_allowed=cp['D'] in (12, 16, 20, 24, 28), S_in_range=-4 <= cp['S'] <= 4,
    m_formula=cp['m'] == 116 + cp['D'] // 2 + 2 * cp['S'], m_even=cp['m'] % 2 == 0, m_le_122=cp['m'] <= 122,
    even_half_bound_Z1=64 * cp['m'] <= 9216 - 20 * 64 - 16, mod3=(cp['m'] - cp['n3']) % 3 == 0,
    deficit_eq3=8 * (cp['m'] - 60) == 6 * cp['n1'] + 5 * cp['n3'] + 3 * cp['n5'],
    counts_sum_256=cp['n1'] + cp['n3'] + cp['n5'] + cp['n7'] == 256,
    odd_energy=cp['n1'] + 9 * cp['n3'] + 25 * cp['n5'] + 49 * cp['n7'] == 64 * (256 - cp['m']),
    collective_5=3 * (cp['n3'] + cp['n5']) - 2 * (cp['n3'] - cp['n1']) == 448 + 16 * cp['S'],
    outside_claimed_list=(cp['D'], cp['m']) not in {(12, 118), (16, 120), (20, 122)})
partC['explicit_counter_profile'] = dict(profile=cp, checks=cp_checks)
OUT['C_profile_enumeration'] = partC
print('Part C done', round(time.time() - T_START, 1), flush=True)

# ---------------------------------------------------------------- Part D: local lemmas
def U4(vec):
    return tuple(sum(vec[z] * (-1) ** pc(s & z) for z in range(4)) for s in range(4))
pats = Counter(); prod_n3 = set(); ok4n = True
for vec in itertools.product((-1, 0, 1), repeat=4):
    Uv = U4(vec); n = sum(1 for x in vec if x)
    ok4n &= sum(x * x for x in Uv) == 4 * n and all((x - n) % 2 == 0 for x in Uv)
    pats[tuple(abs(x) for x in Uv)] += 1
    if n == 3:
        prod_n3.add(Uv[0] * Uv[1] * Uv[2] * Uv[3])
def cname(p):
    n = sum(x * x for x in p) // 4
    if n == 0: return 'O'
    if n == 1: return 'F'
    if n == 3:
        j = [s for s in range(4) if p[s] == 3][0]; return 'B' if j == 0 else 'A%d' % j
    if n == 2:
        if p[0] == 2: return 'C%d' % [s for s in (1, 2, 3) if p[s] == 2][0]
        return 'D%d' % [s for s in (1, 2, 3) if p[s] == 0][0]
    if p == (2, 2, 2, 2): return 'E'
    if p[0] == 4: return 'H'
    return 'G%d' % [s for s in (1, 2, 3) if p[s] == 4][0]
CLS = sorted(((cname(p), p) for p in pats), key=lambda t: t[0])
def local_states(e):
    out = []
    for U in range(5):
        for t in range(-e, e + 1):
            if (t - e) % 2 or (t - U) % 3:
                continue
            if (16 * U + 2 * t) % 3 == 0:
                out.append((U, t, (16 * U + 2 * t) // 3))
    return out
st2 = {U: (t, W) for U, t, W in local_states(2)}
L4 = []
for N in itertools.product(range(65), repeat=4):
    N4 = 64 - sum(N)
    if N4 < 0:
        continue
    Nv = list(N) + [N4]
    tot = lambda fn: sum(Nv[U] * fn(U, *st2[U]) for U in range(5))
    if tot(lambda U, t, W: U * U) == 140 and tot(lambda U, t, W: t * t) == 128 and tot(lambda U, t, W: W * t) == 128 and tot(lambda U, t, W: W * W) == 4096:
        L4.append(Nv)
# negative: drop the mod-3 congruence (any t in {0,+-2}, W rational) -> integrality fails / other solutions
CH = np.array([[(-1) ** pc(p & c) for c in range(64)] for p in range(64)], dtype=np.int64)
e2ok = True; e2n = 0
for p1 in range(64):
    for p2 in range(p1 + 1, 64):
        for s1 in (1, -1):
            for s2 in (1, -1):
                t = s1 * CH[p1] + s2 * CH[p2]; e2n += 1
                Z0 = [c for c in range(64) if t[c] == 0]
                if not (len(Z0) == 32 and is_affine_set(Z0)):
                    e2ok = False
def pack(boolarr):
    return np.packbits(boolarr.astype(np.uint8), axis=1).view('>u8').ravel()
def flat_keys(n, d):
    keys = set()
    for V in subspaces(n, d):
        for c in range(2 ** n):
            Sm = np.zeros((1, 2 ** n), dtype=bool); Sm[0, list({x ^ c for x in V})] = True
            keys.add(int(pack(Sm)[0]))
    return keys
Hyp6 = flat_keys(6, 5); F3_6 = flat_keys(6, 3); F4_6 = flat_keys(6, 4)
combos = np.array(list(itertools.combinations(range(1, 64), 3)), dtype=np.int64)
hist = Counter(); geo_bad = 0; n4 = 0
for sg in itertools.product((1, -1), repeat=3):
    t = CH[0][None, :] + sg[0] * CH[combos[:, 0]] + sg[1] * CH[combos[:, 1]] + sg[2] * CH[combos[:, 2]]
    a = np.abs(t); h0 = (a == 0).sum(1); h2 = (a == 2).sum(1); h4 = (a == 4).sum(1)
    ind_ = (combos[:, 0] ^ combos[:, 1] ^ combos[:, 2]) != 0
    for key, cnt in Counter(zip(ind_.tolist(), h0.tolist(), h2.tolist(), h4.tolist())).items():
        hist[str(key)] += cnt
    n4 += len(combos)
    m24 = (h0 == 24) & (h2 == 32) & (h4 == 8)
    if m24.any():
        A_ = a[m24]
        okh = np.array([int(x) in Hyp6 for x in pack(A_ != 2)]) & np.array([int(x) in F3_6 for x in pack(A_ == 4)])
        geo_bad += int((~okh).sum())
    m48 = (h0 == 48) & (h4 == 16)
    if m48.any():
        geo_bad += int((~np.array([int(x) in F4_6 for x in pack(a[m48] == 4)])).sum())
    geo_bad += int((~(m24 | m48 | (h2 == 64))).sum())
fl5 = set()
for V in subspaces(5, 3):
    for c in range(32):
        fl5.add(frozenset(x ^ c for x in V))
fl5 = list(fl5)
inter5 = Counter(len(A & B) for A, B in itertools.combinations(fl5, 2))
A6 = frozenset(range(8)); B6 = frozenset(x << 3 for x in range(8))
OUT['D_local_lemmas'] = {
    'ternary_vectors': 81, 'distinct_abs_patterns': len(pats), 'class_table': {nm: list(p) for nm, p in CLS},
    'class_sizes': {cname(p): c for p, c in pats.items()}, 'sum_s_U^2_eq_4n_and_U_s≡n_mod2': ok4n,
    'n3_product_values': sorted(prod_n3),
    'e2_local_states(absU,t_rel,W)': local_states(2), 'e4_local_states(absU,t_rel,W)': local_states(4),
    'L4_all_integer_solutions': L4,
    'L4_equals_kappa_family': sorted(L4) == sorted([[24 + 2 * k, 20 - 2 * k, 12 + k, 8 - 2 * k, k] for k in range(5)]),
    'e2_taus_checked': e2n, 'e2_zero_set_always_affine_hyperplane': e2ok,
    'e4_taus_checked_p1=0_eps1=+1': n4, 'e4_(affinely_independent,#|t|=0,#|t|=2,#|t|=4)': dict(hist),
    'e4_geometry_failures': geo_bad,
    'F2^5_affine_3flats': len(fl5), 'F2^5_pairwise_intersections': dict(sorted(inter5.items())),
    'F2^6_negative_two_3flats_meeting_in_one_point': len(A6 & B6)}
print('Part D done', round(time.time() - T_START, 1), flush=True)

# ---------------------------------------------------------------- Part E: exhaustive class/region model
class IntSys:
    """Exact nonnegative-integer equality system; DFS with interval propagation (all-integer arithmetic)."""
    def __init__(self):
        self.nv = 0; self.lo = []; self.hi = []; self.eqs = []
    def var(self, lo, hi):
        self.lo.append(lo); self.hi.append(hi); self.nv += 1; return self.nv - 1
    def eq(self, terms, rhs):
        d = defaultdict(int)
        for v, c in terms:
            d[v] += c
        self.eqs.append(([(v, c) for v, c in d.items() if c], rhs))
    def solve(self, limit=1):
        var_eqs = defaultdict(list)
        for i, (terms, rhs) in enumerate(self.eqs):
            for v, c in terms:
                var_eqs[v].append(i)
        eqs = self.eqs; sols = []; nodes = [0]
        def propagate(lo, hi):
            queue = list(range(len(eqs))); inq = set(queue)
            while queue:
                i = queue.pop(); inq.discard(i); terms, rhs = eqs[i]
                mn = mx = 0
                for v, c in terms:
                    if c > 0: mn += c * lo[v]; mx += c * hi[v]
                    else: mn += c * hi[v]; mx += c * lo[v]
                if rhs < mn or rhs > mx:
                    return False
                changed = False
                for v, c in terms:
                    if c > 0: cmin = c * lo[v]; cmax = c * hi[v]
                    else: cmin = c * hi[v]; cmax = c * lo[v]
                    a = rhs - (mx - cmax); b = rhs - (mn - cmin)
                    if c > 0: nl = -((-a) // c); nh = b // c
                    else: nl = -((-b) // c); nh = a // c
                    if nl > lo[v] or nh < hi[v]:
                        lo[v] = max(lo[v], nl); hi[v] = min(hi[v], nh)
                        if lo[v] > hi[v]:
                            return False
                        changed = True
                        for j in var_eqs[v]:
                            if j not in inq: queue.append(j); inq.add(j)
                if changed and i not in inq:
                    queue.append(i); inq.add(i)
            return True
        def dfs(lo, hi):
            nodes[0] += 1
            if not propagate(lo, hi):
                return
            best = None; bw = None
            for v in range(self.nv):
                wdt = hi[v] - lo[v]
                if wdt > 0 and (bw is None or wdt < bw): best = v; bw = wdt
            if best is None:
                sols.append(lo[:]); return
            for val in range(lo[best], hi[best] + 1):
                l2 = lo[:]; h2 = hi[:]; l2[best] = val; h2[best] = val
                dfs(l2, h2)
                if len(sols) >= limit:
                    return
        dfs(self.lo[:], self.hi[:])
        return sols, nodes[0]

# solver self-test against brute force
rngE = np.random.default_rng(1); mism = 0
for trial in range(300):
    n = int(rngE.integers(2, 5)); Sx = IntSys(); vs = [Sx.var(0, int(rngE.integers(1, 6))) for _ in range(n)]; eqs = []
    for _ in range(int(rngE.integers(1, 4))):
        co = [int(x) for x in rngE.integers(-3, 4, size=n)]; rhs = int(rngE.integers(-6, 11)); Sx.eq(list(zip(vs, co)), rhs); eqs.append((co, rhs))
    sols, _ = Sx.solve(limit=10 ** 6)
    bf = [list(p) for p in itertools.product(*[range(Sx.lo[v], Sx.hi[v] + 1) for v in vs]) if all(sum(c * x for c, x in zip(co, p)) == r for co, r in eqs)]
    mism += sorted(sols) != sorted(bf)

def contrib(absU, ts):
    if ts == 0:
        if absU not in (0, 3): return None
        t = 0
    else:
        if absU not in (1, 2, 4): return None
        t = (-2 if absU in (1, 4) else 2) if ts == 2 else (4 if absU in (1, 4) else -4)
    W = (16 * absU + 2 * t) // 3
    return (absU * absU, t * t, W * W, W * t)

def build_model(Z, es, regions=None, unconstrained=()):
    Sx = IntSys(); X = {}
    if regions is None:
        opts = [(None,) if s in unconstrained else ((0,) if es[s - 1] == 0 else (0, 2) if es[s - 1] == 2 else (0, 2, 4)) for s in (1, 2, 3)]
        regs = {rv: 64 for rv in itertools.product(*opts)}
    else:
        regs = dict(regions)
    for nm, p in CLS:
        for rv, size in regs.items():
            ok = True; cons = []
            for s in (1, 2, 3):
                if s in unconstrained:
                    cons.append(None); continue
                c = contrib(p[s], rv[s - 1])
                if c is None:
                    ok = False; break
                cons.append(c)
            if ok and size > 0:
                X[(nm, rv)] = (Sx.var(0, size), cons, p)
    if regions is None:
        Sx.eq([(v, 1) for v, c, p in X.values()], 64)
    else:
        for rv, size in regs.items():
            Sx.eq([(v, 1) for (nm, r), (v, c, p) in X.items() if r == rv], size)
    for s in (1, 2, 3):
        if s in unconstrained:
            continue
        e = es[s - 1]
        for kk, rhs in ((0, 144 - 2 * e), (1, 64 * e), (2, 4096), (3, 64 * e)):
            Sx.eq([(v, c[s - 1][kk]) for v, c, p in X.values()], rhs)
    Sx.eq([(v, p[0] ** 2) for v, c, p in X.values()], 64 - Z)
    return Sx, X

FULL = (1 << 64) - 1
def mask_of(cond):
    return sum(1 << c for c in range(64) if cond(c))
ALLHYP = sorted({mask_of(lambda c, rho=rho, beta=beta: pc(rho & c) % 2 == beta) for rho in range(1, 64) for beta in (0, 1)})
def flats_masks(d):
    out = set()
    for V in subspaces(6, d):
        for c in range(64):
            out.add(sum(1 << (x ^ c) for x in V))
    return sorted(out)
FL3 = flats_masks(3); FL4 = flats_masks(4)
HYP_CAN = mask_of(lambda c: (c & 1) == 0); F_CAN = mask_of(lambda c: (c & 7) == 0); G_CAN = mask_of(lambda c: (c & 3) == 0)
H24_ALL = [(h, f_) for h in ALLHYP for f_ in FL3 if f_ & ~h & FULL == 0]
def ts_sets(obj):
    k = obj[0]
    if k == 'zero': return {0: FULL}
    if k == 'hyp': return {0: obj[1], 2: FULL ^ obj[1]}
    if k == 'H24': return {0: obj[1] ^ obj[2], 4: obj[2], 2: FULL ^ obj[1]}
    if k == 'H48': return {4: obj[1], 0: FULL ^ obj[1]}
    return {2: FULL}
def region_vector(objs):
    sets = [ts_sets(o) for o in objs]; rv = {}
    for t1, m1 in sets[0].items():
        for t2, m2 in sets[1].items():
            m12 = m1 & m2
            if not m12: continue
            for t3, m3 in sets[2].items():
                n = pc(m12 & m3)
                if n: rv[(t1, t2, t3)] = n
    return tuple(sorted(rv.items()))
geo_cases = {}
geo_cases[(2, 2, 2)] = {region_vector([('hyp', HYP_CAN), ('hyp', h2), ('hyp', h3)]) for h2 in ALLHYP for h3 in ALLHYP}
geo_cases[(2, 2, 4)] = {region_vector([('hyp', h1), ('hyp', h2), s3]) for s3 in [('H24', HYP_CAN, F_CAN), ('H48', G_CAN), ('H64',)] for h1 in ALLHYP for h2 in ALLHYP}
s3all = [('H24', h, f_) for h, f_ in H24_ALL] + [('H48', g) for g in FL4] + [('H64',)]
rv044 = {region_vector([('zero',), s2, s3]) for s2 in [('H24', HYP_CAN, F_CAN), ('H48', G_CAN)] for s3 in s3all}
rv044 |= {region_vector([('zero',), ('H64',), s3]) for s3 in [('H24', HYP_CAN, F_CAN), ('H48', G_CAN), ('H64',)]}
geo_cases[(0, 4, 4)] = rv044

def patterns(E2):
    return [(a, b, E2 - a - b) for a in range(0, E2 + 1, 2) for b in range(a, E2 + 1, 2) if E2 - a - b >= b]
def describe(sol, X):
    return {k[0] + ':' + ''.join(str(t) for t in k[1]): sol[v] for k, (v, c, p) in X.items() if sol[v]}
case_rows = []
for m, Zs in ((122, [8]), (120, [8, 12, 16]), (118, [8, 12, 16, 20, 24])):
    for Z in Zs:
        E2 = 248 - Z // 2 - 2 * m
        for pat in patterns(E2):
            unc = tuple(s for s in (1, 2, 3) if pat[s - 1] > 4)
            Sx, X = build_model(Z, pat, None, unc); sols, nodes = Sx.solve(1)
            row = dict(m=m, Z=Z, E2=E2, pattern=list(pat), relaxed_s=list(unc), counting_only_feasible=bool(sols))
            if sols:
                row['counting_only_example'] = describe(sols[0], X)
            if sols and pat in geo_cases:
                feas = 0
                for rv in geo_cases[pat]:
                    Sg, Xg = build_model(Z, pat, dict(rv)); sg_, _ = Sg.solve(1); feas += bool(sg_)
                row['geometric_region_vectors'] = len(geo_cases[pat]); row['geometric_feasible'] = feas
            case_rows.append(row)
excluded_all = all((not r['counting_only_feasible']) or r.get('geometric_feasible') == 0 for r in case_rows)
probes = []
for pat, Z, m in (((0, 4, 4), 16, 116), ((2, 2, 2), 20, 116), ((0, 4, 4), 24, 114), ((2, 2, 2), 28, 114)):
    feas = []
    for rv in sorted(geo_cases[pat]):
        Sg, Xg = build_model(Z, pat, dict(rv)); sg_, _ = Sg.solve(1)
        if sg_:
            feas.append(dict(region_vector={''.join(str(t) for t in k): n for k, n in rv}, solution=describe(sg_[0], Xg)))
    probes.append(dict(m=m, Z=Z, pattern=list(pat), feasible_region_vectors=len(feas), first=feas[0] if feas else None))
OUT['E_case_analysis_model'] = dict(solver_bruteforce_mismatches=mism, region_vector_counts={str(k): len(v) for k, v in geo_cases.items()},
    P1_list_cases=case_rows, all_P1_list_cases_excluded=excluded_all, exploratory_gap_probes=probes)
print('Part E done', round(time.time() - T_START, 1), flush=True)

# ---------------------------------------------------------------- Part F: polynomial counterexamples
bit = lambda x, i: (x >> i) & 1
Htt = [(bit(x, 0) * bit(x, 1) * bit(x, 2) + bit(x, 3) * bit(x, 4) * bit(x, 5) + bit(x, 0) * bit(x, 1) * bit(x, 3)) % 2 for x in range(64)]
p0 = next(x for x in range(64) if Htt[x]); Ht = [Htt[x ^ p0] for x in range(64)]
htt = [(bit(x, 0) * bit(x, 1) * bit(x, 2) + bit(x, 3) * bit(x, 4) * bit(x, 5) + bit(x, 0) * bit(x, 6) * bit(x, 7)) % 2 for x in range(256)]
quot = {}
for i, j in itertools.combinations(range(8), 2):
    quot[f'x{i},x{j}'] = [sum(htt[x] for x in range(256) if (bit(x, i), bit(x, j)) == (a, b)) for a in (0, 1) for b in (0, 1)]
OUT['F_counterexamples'] = dict(H_degree=anf_degree(Htt, 6), H_weight=sum(Htt), H_translated_value_at_0=Ht[0], H_translated_weight=sum(Ht),
    h_degree=anf_degree(htt, 8), h_weight=sum(htt),
    h_coset_weights_matching_8_20_8_32={k: v for k, v in quot.items() if sorted(v) == [8, 8, 20, 32]})
print('Part F done', round(time.time() - T_START, 1), flush=True)

# ---------------------------------------------------------------- Part G: lattice test for E2 parity
def hnf_cols(M, n):
    A = [row[:] for row in M]; r = len(A)
    U = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    def swap(i, j):
        for row in A: row[i], row[j] = row[j], row[i]
        for row in U: row[i], row[j] = row[j], row[i]
    def addmul(dst, src, qq):
        for row in A: row[dst] -= qq * row[src]
        for row in U: row[dst] -= qq * row[src]
    pivots = []; pcnt = 0
    for i in range(r):
        if pcnt >= n: break
        while True:
            nz = [j for j in range(pcnt, n) if A[i][j]]
            if not nz: break
            jm = min(nz, key=lambda j: abs(A[i][j]))
            if jm != pcnt: swap(jm, pcnt)
            for j in range(pcnt + 1, n):
                if A[i][j]: addmul(j, pcnt, A[i][j] // A[i][pcnt])
            if all(A[i][j] == 0 for j in range(pcnt + 1, n)): break
        if A[i][pcnt] if pcnt < n else 0:
            pivots.append((i, pcnt)); pcnt += 1
    return A, U, pivots, pcnt
ks = list(range(-7, 8)); nk = len(ks); kidx = {k: i for i, k in enumerate(ks)}
cong = [([comb(128 + k, j) for k in ks], 2 ** (9 - j)) for j in range(1, 9)]
cong += [([comb(128 + k, j) if k % 2 == 0 else 0 for k in ks], 2 ** (8 - j)) for j in range(1, 8)]
ns = len(cong); ncols = nk + ns + 1
rows = []; rhs = []
def row(coefs, slack=None, mcoef=0):
    rr = list(coefs) + [0] * ns + [mcoef]
    if slack is not None: rr[nk + slack[0]] = slack[1]
    return rr
rows.append(row([1 if k % 2 == 0 else 0 for k in ks])); rhs.append(255)
rows.append(row([1 if k % 2 else 0 for k in ks])); rhs.append(256)
rows.append(row([k * k for k in ks])); rhs.append(16384)
rows.append(row([k * k if k % 2 == 0 else 0 for k in ks], mcoef=-64)); rhs.append(0)
rr = [0] * ncols; rr[kidx[0]] = rr[kidx[4]] = rr[kidx[-4]] = 1; rows.append(rr); rhs.append(63)
rr = [0] * ncols
for k in (2, -2, 6, -6): rr[kidx[k]] = 1
rows.append(rr); rhs.append(192)
for i_, (coefs, mod) in enumerate(cong):
    rows.append(row(coefs, (i_, -mod))); rhs.append(0)
A_, U_, piv, rk = hnf_cols(rows, ncols)
ker = [[U_[i][j] for i in range(ncols)] for j in range(rk, ncols)]
ker_ok = all(sum(rw[i] * v[i] for i in range(ncols)) == 0 for rw in rows for v in ker)
# particular integer solution via the column echelon form
y = [0] * ncols; part_ok = True
for (i, j) in piv:
    val = rhs[i] - sum(A_[i][l] * y[l] for l in range(j))
    if val % A_[i][j]: part_ok = False; break
    y[j] = val // A_[i][j]
xpart = [sum(U_[i][j] * y[j] for j in range(ncols)) for i in range(ncols)]
part_ok = part_ok and all(sum(rw[i] * xpart[i] for i in range(ncols)) == b for rw, b in zip(rows, rhs))
phiE = [0] * ncols; phiE[kidx[2]] = phiE[kidx[-2]] = 1
phi = [0] * ncols; phi[kidx[2]] = phi[kidx[-2]] = 1; phi[kidx[3]] = phi[kidx[-3]] = 2
E2_par = sorted({sum(a * b for a, b in zip(phiE, v)) % 2 for v in ker})
phi_mod4 = sorted({sum(a * b for a, b in zip(phi, v)) % 4 for v in ker})
OUT['G_lattice_E2_parity'] = dict(constraints='dual-code binomial-moment integrality (full, mod 2^(9-j), j=1..8; even half, mod 2^(8-j), j=1..7), counts 255/256, Parseval, even-half 64m, rank-two z=64 counts',
    kernel_rank=len(ker), kernel_vectors_verified=ker_ok, particular_integer_solution_exists=part_ok,
    E2_parity_values_on_kernel_basis=E2_par, E2_plus_2n3_mod4_values_on_kernel_basis=phi_mod4,
    conclusion='E2 parity is not forced by these constraints' if E2_par == [0, 1] and part_ok and ker_ok else 'see data')
print('Part G done', round(time.time() - T_START, 1), flush=True)

# ---------------------------------------------------------------- Part H: Z8 degree vs polar rank
rowsH = []
for grp in ('random', 'low_polar_rank_swaps'):
    for rr_ in partA[grp]:
        rowsH.append(dict(group=grp, polar_rank=rr_.get('polar_rank'), z=rr_.get('z'), deg_1_Z8_on_K=rr_.get('deg_1_Z8_on_K'), Z8_size=rr_.get('Z8_size')))
OUT['H_Z8_degree_vs_polar_rank'] = dict(rows=rowsH,
    rank_le_2_all_deg_le_5=all(r['deg_1_Z8_on_K'] <= 5 for r in rowsH if r['polar_rank'] is not None and r['polar_rank'] <= 2),
    some_rank_ge_6_with_deg_6=any(r['deg_1_Z8_on_K'] == 6 for r in rowsH if r['polar_rank'] is not None and r['polar_rank'] >= 6))

OUT['runtime_seconds'] = round(time.time() - T_START, 1)
OUT['python'] = sys.version.split()[0]; OUT['numpy'] = np.__version__
outpath = sys.argv[1]
with open(outpath, 'w') as fh:
    json.dump(OUT, fh, indent=1, sort_keys=False, default=str)
    fh.write('\n')
print('wrote', outpath, OUT['runtime_seconds'])
