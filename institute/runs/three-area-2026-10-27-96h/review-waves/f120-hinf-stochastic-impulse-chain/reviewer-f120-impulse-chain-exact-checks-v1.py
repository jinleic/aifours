#!/usr/bin/env python3
"""reviewer-f120-impulse-chain-exact-checks-v1.py

Independent reviewer diagnostic for review wave f120 (stochastic impulse-chain
necessary lower bound, candidate SHA256 c165f2df...). Written by the f120 reviewer.
It does NOT import, execute, or copy the author's
frontier-20261028-stochastic-impulse-lower-check.py. There is NO Monte Carlo here.

Scope of the computation (closed loops with Q = A0+B0K = 0, where the impulse state
between jumps is the deterministic flow e^{P(t-t_j)} and the impulse functional is
exactly a Gaussian quadratic form):

  L(a) = E sqrt( c^2 + xi^T M xi ),   c = ||B_n a||,   xi ~ N(0, I_{n+1}),
  M_{jk} = int_{max(t_j,t_k)}^T (O e^{P(t-t_j)} G_j)^T (O e^{P(t-t_k)} G_k) dt   (exact Fractions),

evaluated through the exact one-dimensional representation (sqrt(y) = (2 sqrt(pi))^{-1}
int_0^inf (1-e^{-sy}) s^{-3/2} ds and the chi-square mgf):

  L = (1/(2 sqrt(pi))) int_0^inf s^{-3/2} [ 1 - exp(-s c^2) det(I + 2 s M)^{-1/2} ] ds,

cross-checked in rank-1 cases against the Bessel closed form

  E sqrt(c^2 + lam xi^2) = sqrt(lam) k^2 e^{k^2/4} [K_0(k^2/4)+K_1(k^2/4)] / (2 sqrt(2 pi)),  k^2 = c^2/lam,

and against direct Gaussian quadrature. Fractions are exact; mpmath quadrature is
high-precision deterministic numerics (30 digits requested), not Monte Carlo.
The finite-epsilon identities for the author's scalar example (E||z_eps||^2 = 2 - eps/2
exactly, and a rigorous Jensen lower bound for E||z_eps||) are evaluated by
Gauss-Hermite quadrature (numpy hermegauss) and cross-checked by nested mpmath quadrature.
"""
import datetime
import hashlib
import json
import math
import os
import platform
import subprocess
import sys
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np

mp.mp.dps = 30

# ----------------------------------------------------------------------------- exact linear algebra


def fr(x):
    return x if isinstance(x, Fr) else Fr(x)


def mat(rows):
    return [[fr(v) for v in r] for r in rows]


def vec(vals):
    return [fr(v) for v in vals]


def matvec(A, x):
    return [sum(A[i][k] * x[k] for k in range(len(x))) for i in range(len(A))]


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def eye(n):
    return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]


def zeros(n, m):
    return [[Fr(0) for _ in range(m)] for _ in range(n)]


def transpose(A):
    return [list(r) for r in zip(*A)]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def det(A):
    """Exact determinant by Gaussian elimination over Fractions."""
    n = len(A)
    M = [row[:] for row in A]
    d = Fr(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return Fr(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d *= M[c][c]
        inv = 1 / M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] * inv
            if f:
                for k in range(c, n):
                    M[r][k] -= f * M[c][k]
    return d


def charpoly_coeffs(S):
    """Coefficients e_0..e_m of det(I + 2 s S) as a polynomial in s, exact, via
    interpolation at s = 0..m (degree <= m)."""
    m = len(S)
    pts = list(range(m + 1))
    vals = []
    for s_ in pts:
        A = [[(Fr(int(i == j)) + 2 * Fr(s_) * S[i][j]) for j in range(m)] for i in range(m)]
        vals.append(det(A))
    coeffs = [Fr(0)] * (m + 1)
    for i, si in enumerate(pts):
        basis = [Fr(1)]
        denom = Fr(1)
        for j, sj in enumerate(pts):
            if j == i:
                continue
            basis = [Fr(0)] + basis
            for k in range(len(basis) - 1):
                basis[k] -= sj * basis[k + 1]
            denom *= (si - sj)
        for k in range(len(basis)):
            coeffs[k] += vals[i] * basis[k] / denom
    assert coeffs[0] == 1, coeffs
    return coeffs


# ----------------------------------------------------------------------------- chain algebra


def chain_Bn(E0, Eh, n):
    """B_n : R^{n p} -> R^{(n+1) q},  y_j = E0 a_j + Eh a_{j-1}, a_{-1}=a_n=0."""
    q, p = len(E0), len(E0[0])
    B = zeros((n + 1) * q, n * p)
    for j in range(n + 1):
        for k in range(n):
            blk = None
            if k == j:
                blk = E0
            elif k == j - 1:
                blk = Eh
            if blk is not None:
                for r in range(q):
                    for c in range(p):
                        B[j * q + r][k * p + c] = blk[r][c]
    return B


def split_blocks(a, p, n):
    return [a[j * p:(j + 1) * p] for j in range(n)]


def chain_G(G0, Gh, a_blocks, n):
    p = len(a_blocks[0])
    zero = vec([0] * p)
    out = []
    for j in range(n + 1):
        aj = a_blocks[j] if j < n else zero
        ajm = a_blocks[j - 1] if j >= 1 else zero
        out.append([x + y for x, y in zip(matvec(G0, aj), matvec(Gh, ajm))])
    return out


def nilpotent_index(P, maxidx=6):
    d = len(P)
    Pk = eye(d)
    for i in range(maxidx):
        Pk = matmul(Pk, P)
        if all(v == 0 for r in Pk for v in r):
            return i + 1
    return None


def output_poly(O, P, Gj, tj):
    """Coefficients (vectors) in powers of t of  O e^{P(t-tj)} Gj, P nilpotent."""
    idx = nilpotent_index(P)
    assert idx is not None, "P must be nilpotent for exact polynomial flow"
    d = len(P)
    coef = [vec([0] * len(O)) for _ in range(idx)]
    Pk = eye(d)
    for i in range(idx):
        term = matvec(O, matvec(Pk, Gj))
        fact = Fr(math.factorial(i))
        for l in range(i + 1):
            cl = Fr(math.comb(i, l)) * (-tj) ** (i - l) / fact
            coef[l] = [x + cl * y for x, y in zip(coef[l], term)]
        Pk = matmul(Pk, P)
    return coef


def gram_M(O, P, Gs, times, T):
    """M_{jk} = int_{max(tj,tk)}^T (O e^{P(t-tj)}Gj) . (O e^{P(t-tk)}Gk) dt, exact."""
    polys = [output_poly(O, P, Gs[j], times[j]) for j in range(len(Gs))]
    m = len(Gs)
    M = zeros(m, m)
    for j in range(m):
        for k in range(m):
            lo = max(times[j], times[k])
            prod = [Fr(0)] * (len(polys[j]) + len(polys[k]) - 1)
            for u, cu in enumerate(polys[j]):
                for v, cv in enumerate(polys[k]):
                    prod[u + v] += dot(cu, cv)
            M[j][k] = sum(cc * (T ** (i + 1) - lo ** (i + 1)) / (i + 1) for i, cc in enumerate(prod))
    return M


# ----------------------------------------------------------------------------- the functional


def mpf(x):
    x = fr(x)
    return mp.mpf(x.numerator) / mp.mpf(x.denominator)


def L_sintegral(c2, M):
    """L = (2 sqrt(pi))^{-1} int_0^inf s^{-3/2}[1 - e^{-s c2} det(I+2sM)^{-1/2}] ds, stable form."""
    e = charpoly_coeffs(M)  # det(I+2sM) = sum e_k s^k, e_0 = 1
    tail = [mpf(v) for v in e[1:]]
    c2m = mpf(c2)

    def q(s_):
        r = mp.mpf(0)
        for coeff in reversed(tail):
            r = r * s_ + coeff
        return r * s_

    def f(s_):
        if s_ == 0:
            return mp.mpf(0)
        inner = -s_ * c2m - mp.mpf('0.5') * mp.log1p(q(s_))
        return -mp.expm1(inner) * s_ ** mp.mpf('-1.5')

    val = mp.quad(f, [0, mp.mpf('0.01'), 1, 10, mp.inf])
    return val / (2 * mp.sqrt(mp.pi))


def L_bessel(c2, lam):
    """Rank-1 closed form E sqrt(c2 + lam xi^2)."""
    c2m, lamm = mpf(c2), mpf(lam)
    if lamm == 0:
        return mp.sqrt(c2m)
    if c2m == 0:
        return mp.sqrt(lamm) * mp.sqrt(2 / mp.pi)
    k2 = c2m / lamm
    z = k2 / 4
    return mp.sqrt(lamm) * k2 * mp.exp(z) * (mp.besselk(0, z) + mp.besselk(1, z)) / (2 * mp.sqrt(2 * mp.pi))


def L_direct(c2, lam):
    c2m, lamm = mpf(c2), mpf(lam)
    g = lambda x: mp.sqrt(c2m + lamm * x * x) * mp.exp(-x * x / 2) / mp.sqrt(2 * mp.pi)
    return mp.quad(g, [-mp.inf, -1, 0, 1, mp.inf])


def eig_sym(M):
    A = mp.matrix([[mpf(v) for v in r] for r in M])
    ev = mp.eigsy(A, eigvals_only=True)
    return sorted([ev[i] for i in range(len(M))], reverse=True)


def s(x):
    return mp.nstr(x, 25)


# ----------------------------------------------------------------------------- instances


def run_instance(name, *, E0, Eh, G0, Gh, O, P, h, T, a, notes=""):
    """h = 0 means single impulse at 0 with taps E0+Eh, G0+Gh (registered h=0 convention)."""
    E0, Eh, G0, Gh, O, P = mat(E0), mat(Eh), mat(G0), mat(Gh), mat(O), mat(P)
    h, T = fr(h), fr(T)
    a = vec(a)
    p = len(E0[0])
    if h == 0:
        n = 1
        E0s = [[x + y for x, y in zip(r0, rh)] for r0, rh in zip(E0, Eh)]
        G0s = [[x + y for x, y in zip(r0, rh)] for r0, rh in zip(G0, Gh)]
        Ehs = zeros(len(E0), p)
        Ghs = zeros(len(G0), p)
        B = chain_Bn(E0s, Ehs, 1)[:len(E0)]
        times = [Fr(0)]
        Gs = chain_G(G0s, Ghs, split_blocks(a, p, 1), 1)[:1]
    else:
        S = T - h
        n = math.ceil(S / h)
        B = chain_Bn(E0, Eh, n)
        times = [j * h for j in range(n + 1)]
        Gs = chain_G(G0, Gh, split_blocks(a, p, n), n)
    assert len(a) == n * p, (len(a), n, p)
    Ba = matvec(B, a)
    c2 = dot(Ba, Ba)
    BtB = matmul(transpose(B), B)
    M = gram_M(O, P, Gs, times, T)
    a2 = dot(a, a)
    trM = sum(M[i][i] for i in range(len(M)))
    Lval = L_sintegral(c2, M)
    ev = eig_sym(M)
    rank1 = sum(1 for v in ev if abs(v) > mp.mpf('1e-20')) <= 1
    out = {
        'name': name,
        'notes': notes,
        'n': n,
        'times_tj': [str(t) for t in times],
        'T': str(T), 'h': str(h),
        'a': [str(v) for v in a],
        'B_n_a': [str(v) for v in Ba],
        'c2_exact': str(c2), 'c_exact_sqrt': s(mp.sqrt(mpf(c2))),
        'BtB_exact': [[str(v) for v in r] for r in BtB],
        'OG_j_exact': [[str(v) for v in matvec(O, g)] for g in Gs],
        'author_condition_OGj_nonzero': [any(v != 0 for v in matvec(O, g)) for g in Gs],
        'M_exact': [[str(v) for v in r] for r in M],
        'M_diag_alpha_j': [str(M[i][i]) for i in range(len(M))],
        'general_condition_some_alpha_j_positive': any(M[i][i] > 0 for i in range(len(M))),
        'M_eigenvalues_30dps': [s(v) for v in ev],
        'L_a_sintegral': s(Lval),
        'ratio_L_over_norm_a': s(Lval / mp.sqrt(mpf(a2))),
        'jensen_rms_upper_sqrt_c2_plus_trM_over_norm_a': s(mp.sqrt(mpf(c2 + trM)) / mp.sqrt(mpf(a2))),
        'direct_atom_lower_c_over_norm_a': s(mp.sqrt(mpf(c2)) / mp.sqrt(mpf(a2))),
        'L_minus_c': s(Lval - mp.sqrt(mpf(c2))),
    }
    if rank1:
        lam_exact = trM
        out['rank1_lambda_exact'] = str(lam_exact)
        lb = L_bessel(c2, lam_exact)
        ld = L_direct(c2, lam_exact)
        out['L_a_bessel_closed_form'] = s(lb)
        out['L_a_direct_quadrature'] = s(ld)
        out['abs_diff_sintegral_vs_bessel'] = s(abs(Lval - lb))
        out['abs_diff_sintegral_vs_direct'] = s(abs(Lval - ld))
    return out


def scalar_example_finite_eps(eps_list, nodes=(200, 300)):
    """Author's scalar example dx = w dW, z = x + w, h=0, T=1, w_eps = eps^{-1/2} 1_[0,eps].
    Exact representation: ||z_eps||^2 = int_0^1 (1+sqrt(eps) B_s)^2 ds + (1-eps) B_1^2.
    Exact second moment: E||z_eps||^2 = 2 - eps/2.
    Rigorous lower bound (Cauchy-Schwarz in time): E||z_eps|| >= E sqrt((1+sqrt(eps) I)^2 + (1-eps) xi^2),
    with I = int_0^1 B_s ds = xi/2 + eta/sqrt(12), xi = B_1, eta independent N(0,1)."""
    res = []
    for eps in eps_list:
        vals = {}
        for N in nodes:
            x, w = np.polynomial.hermite_e.hermegauss(N)
            w = w / math.sqrt(2 * math.pi)
            X, Y = np.meshgrid(x, x, indexing='ij')
            WX, WY = np.meshgrid(w, w, indexing='ij')
            I = X / 2 + Y / math.sqrt(12)
            f = np.sqrt((1 + math.sqrt(eps) * I) ** 2 + (1 - eps) * X ** 2)
            vals[str(N)] = float(np.sum(f * WX * WY))
        # independent nested mpmath cross-check at 15 digits on [-8,8]^2
        with mp.workdps(15):
            e = mp.mpf(eps)
            phi = lambda u: mp.exp(-u * u / 2) / mp.sqrt(2 * mp.pi)
            inner = lambda x_: mp.quad(lambda y_: mp.sqrt((1 + mp.sqrt(e) * (x_ / 2 + y_ / mp.sqrt(12))) ** 2 + (1 - e) * x_ * x_) * phi(y_), [-8, 0, 8])
            cross = mp.quad(lambda x_: inner(x_) * phi(x_), [-8, 0, 8])
            vals['mpmath_nested_15dps'] = mp.nstr(cross, 15)
        res.append({'eps': eps,
                    'exact_E_norm_sq': 2 - eps / 2,
                    'rms_upper_sqrt_E_norm_sq': math.sqrt(2 - eps / 2),
                    'rigorous_lower_bound_E_norm': vals,
                    })
    return res


def main():
    t0 = datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        date_out = subprocess.run(['/bin/date', '-u', '+%Y-%m-%dT%H:%M:%SZ'], capture_output=True, text=True).stdout.strip()
    except Exception as exc:  # pragma: no cover
        date_out = f'unavailable: {exc}'
    src_path = os.path.abspath(__file__)
    with open(src_path, 'rb') as fh:
        src_bytes = fh.read()
    report = {
        'kind': 'REVIEWER_INDEPENDENT_EXACT_CHECKS_F120',
        'reviewer_note': 'Reviewer-written. No author code imported/executed. No Monte Carlo. Fractions exact; mpmath 30-digit deterministic quadrature; GH + nested mpmath quadrature for finite-eps bounds.',
        'clock_utc_python': t0,
        'clock_utc_bin_date': date_out,
        'python': sys.version.split()[0], 'mpmath': mp.__version__, 'numpy': np.__version__,
        'platform': platform.platform(),
        'script_path': src_path,
        'script_sha256': hashlib.sha256(src_bytes).hexdigest(),
        'script_bytes': len(src_bytes),
        'instances': [],
    }
    inst = report['instances']

    # S1 author's scalar example, h=0, T=1: E=1, G=1, O=1, P=0.
    inst.append(run_instance(
        'S1_author_scalar_h0_dx=wdW_z=x+w',
        E0=[[1]], Eh=[[0]], G0=[[1]], Gh=[[0]], O=[[1]], P=[[0]], h=0, T=1, a=[1],
        notes='Candidate section 5. Expect L(1)=E sqrt(1+xi^2)=e^{1/4}(K0+K1)(1/4)/(2 sqrt(2pi)) > 1 = delta.'))
    s1 = inst[-1]
    s1['author_simple_lower_1+(sqrt2-1)erfc(1/sqrt2)'] = s(1 + (mp.sqrt(2) - 1) * mp.erfc(1 / mp.sqrt(2)))
    s1['closed_form_e^{1/4}(K0+K1)(1/4)/(2sqrt(2pi))'] = s(mp.exp(mp.mpf(1) / 4) * (mp.besselk(0, mp.mpf(1) / 4) + mp.besselk(1, mp.mpf(1) / 4)) / (2 * mp.sqrt(2 * mp.pi)))
    s1['jensen_upper_sqrt2'] = s(mp.sqrt(2))
    s1['author_reported_quadrature_value_for_comparison_only'] = '1.3545308064813155'
    s1['finite_eps_exact_identities_and_rigorous_lower_bounds'] = scalar_example_finite_eps([0.1, 0.04, 0.01])
    s1['author_reported_MC_values_for_comparison_only'] = {'0.1': 1.334214397851863, '0.04': 1.3444025316870851, '0.01': 1.3492549984417297}

    # S2 Source-4 n=2 chain: h=1, T=5/2 (S=3/2, n=2), E0=1, Eh=-1, O=1, G0=1, Gh=0, P=Q=0.
    for a in ([1, -1], [1, 1], [1, 0], [0, 1]):
        inst.append(run_instance(
            f'S2_source4_chain_n2_E0=1_Eh=-1_a={a}',
            E0=[[1]], Eh=[[-1]], G0=[[1]], Gh=[[0]], O=[[1]], P=[[0]], h=1, T=Fr(5, 2), a=a,
            notes='B_2^T B_2 must be [[2,-1],[-1,2]] (eigs 3,1); a=(1,-1) is the top singular direction, delta=sqrt3.'))

    # S3 matrix-tap chain: p=2 inputs, q=2 outputs, state dim 2; E0=I, Eh=J; G0=diag(1,0), Gh=0; O=I; P=0.
    J = [[0, 1], [1, 0]]
    for a in ([1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 0, -1]):
        inst.append(run_instance(
            f'S3_matrix_tap_chain_n2_E0=I_Eh=J_a={a}',
            E0=[[1, 0], [0, 1]], Eh=J, G0=[[1, 0], [0, 0]], Gh=[[0, 0], [0, 0]], O=[[1, 0], [0, 1]], P=[[0, 0], [0, 0]],
            h=1, T=Fr(5, 2), a=a,
            notes='B_2^T B_2 = [[2I,J],[J,2I]], eigs {3,3,1,1}; (v,Jv) are top singular vectors.'))

    # NC1 negative control: O = 0 -> L(a) = ||B_n a|| exactly (formula must return c).
    inst.append(run_instance(
        'NC1_O_zero_no_state_output',
        E0=[[1]], Eh=[[-1]], G0=[[1]], Gh=[[0]], O=[[0]], P=[[0]], h=1, T=Fr(5, 2), a=[1, -1],
        notes='Expect L = c = sqrt6 exactly and L_minus_c = 0 to working precision.'))

    # NC2 negative control: p=2, h=0, T=1: E=[1,0], G=[0,1] (state dim 1), O=1, P=0.
    for a in ([1, 0], [3, 1], [1, 1], [1, 3], [0, 1]):
        inst.append(run_instance(
            f'NC2_jensen_capped_p2_h0_a={a}',
            E0=[[1, 0]], Eh=[[0, 0]], G0=[[0, 1]], Gh=[[0, 0]], O=[[1]], P=[[0]], h=0, T=1, a=a,
            notes='Expect ratio <= 1 with equality only at a=(1,0); a=(0,1) gives E|xi| = sqrt(2/pi).'))

    # NC3 dynamics-visible control: h=0, T=1, scalar input, state dim 2, P nilpotent [[0,1],[0,0]],
    # O=[1,0], G=(0,1): O G = 0 (author condition fails) but O e^{Pt} G = t, so alpha = 1/3 > 0 and L > delta = 1.
    inst.append(run_instance(
        'NC3_OG_zero_but_dynamics_visible_P_nilpotent',
        E0=[[1]], Eh=[[0]], G0=[[0], [1]], Gh=[[0], [0]], O=[[1, 0]], P=[[0, 1], [0, 0]], h=0, T=1, a=[1],
        notes='Expect M=[[1/3]], L = E sqrt(1 + xi^2/3) > 1 although OG=0: the strict-gap condition can be weakened.'))

    # D1 drift-channel control (exact, no stochastic part): dx = w dt, z = x + w, h=0, T=1 (G=0, E=1, O=1, P=0).
    # Impulse functional: L(a)=|a| (delta=1, no gap). Constant input w=1 on [0,1]: z=1+t, ||z||^2 = 7/3.
    report['D1_drift_channel_control'] = {
        'model': 'dx = w dt, z = x + w, h=0, T=1, deterministic',
        'impulse_functional_ratio': '1 (= delta; G=0 so no stochastic impulse)',
        'constant_input_w=1_norm_sq_exact': str(Fr(7, 3)),
        'constant_input_ratio': s(mp.sqrt(mpf(Fr(7, 3)))),
        'meaning': 'actual gain >= sqrt(7/3) > 1 = sup_a L(a)/||a||: the pulse family is blind to drift-channel energy; impulse bound is not the gain.',
    }

    report['clock_utc_end_python'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    out_path = sys.argv[1] if len(sys.argv) > 1 else None
    text = json.dumps(report, indent=1, sort_keys=False)
    if out_path:
        with open(out_path, 'x', encoding='utf-8') as fh:
            fh.write(text + '\n')
        print(f'wrote {out_path} sha256={hashlib.sha256((text + chr(10)).encode()).hexdigest()}')
    else:
        print(text)


if __name__ == '__main__':
    main()
