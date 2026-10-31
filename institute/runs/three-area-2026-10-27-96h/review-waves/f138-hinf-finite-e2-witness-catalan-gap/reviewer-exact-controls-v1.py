#!/usr/bin/env python3
"""reviewer-exact-controls-v1.py  (review f138-hinf-finite-e2-witness-catalan-gap)

Independent reviewer controls.  Structurally independent of the author checker
frontier-20261028-brownian-exit-catalan-exact-check.py, which is NEVER executed
or imported here:
  * pi is enclosed with the Euler/Hutton identity pi/4 = arctan(1/2)+arctan(1/3)
    (the author used Machin), with strict alternating-series brackets;
  * Catalan G is enclosed with the PAIRED POSITIVE series
    G = sum_m [1/(4m+1)^2 - 1/(4m+3)^2] plus an explicit integral tail bound
    (the author used the alternating partial sum + next term);
  * all Part A/B statements are exact fractions.Fraction comparisons.
Part C (mpmath/numpy) is a NON-load-bearing numerical cross-check of the
closed form E sqrt(tau) = 4 sqrt(2 pi) G / pi^2 through two further classical
representations (Laplace transform sech sqrt(2 lambda); method-of-images
survival series) and a discretised Monte Carlo of the actual witness.
The script writes reviewer-exact-controls-v1.log next to itself.
"""
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, 'reviewer-exact-controls-v1.log')
_lines = []
RESULTS = {}


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def out(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    _lines.append(s)


def check(name, cond, expect=True):
    """expect=True: a positive control that must hold.
    expect=False: a NEGATIVE control, the condition must be False."""
    ok = (bool(cond) == expect)
    RESULTS[name] = ok
    tag = 'PASS' if ok else 'FAIL'
    kind = 'POS' if expect else 'NEG'
    out(f'{tag} [{kind}] {name}  (raw condition={bool(cond)})')
    return ok


def dec(fr, digits):
    """Exact decimal string of a positive Fraction truncated to `digits`."""
    n, d = fr.numerator, fr.denominator
    ip = n // d
    rem = n - ip * d
    s = str(ip) + '.'
    for _ in range(digits):
        rem *= 10
        s += str(rem // d)
        rem -= (rem // d) * d
    return s


def sqrt_lo(fr, digits):
    """Rational lower bound for sqrt(fr) with `digits` decimals (exact isqrt)."""
    scale = 10 ** digits
    n, d = fr.numerator, fr.denominator
    return Fr(math.isqrt(n * scale * scale // d), scale)


def sqrt_hi(fr, digits):
    scale = 10 ** digits
    n, d = fr.numerator, fr.denominator
    return Fr(math.isqrt(-(-(n * scale * scale) // d)) + 1, scale)


out('reviewer-exact-controls-v1.py start UTC', utc())
out('python', sys.version.split()[0])

# =====================================================================
# Part A: exact enclosure of  m := E sqrt(tau) = 4 sqrt(2 pi) G / pi^2,
#         tau = first exit time of standard Brownian motion from (-1,1).
#         Equivalent squared form used (no square roots in the proof):
#         m^2 = 32 G^2 / pi^3.
# =====================================================================
out('\n=== Part A: exact rational enclosure of E sqrt(tau) ===')


def arctan_inv_bracket(q, n):
    """Strict rational bracket (lo, hi) of arctan(1/q), integer q >= 2, from the
    Gregory series sum_k (-1)^k / ((2k+1) q^(2k+1)); |terms| strictly decrease
    because (2k+1)/((2k+3) q^2) < 1, so consecutive partial sums bracket."""
    terms = [Fr((-1) ** k, (2 * k + 1) * q ** (2 * k + 1)) for k in range(n + 2)]
    s_n = sum(terms[:n + 1], Fr(0))
    s_n1 = s_n + terms[n + 1]
    return (min(s_n, s_n1), max(s_n, s_n1))


a2lo, a2hi = arctan_inv_bracket(2, 40)
a3lo, a3hi = arctan_inv_bracket(3, 30)
pi_lo = 4 * (a2lo + a3lo)
pi_hi = 4 * (a2hi + a3hi)
out('pi_lo =', dec(pi_lo, 25))
out('pi_hi =', dec(pi_hi, 25))
check('A1 pi bracket consistent (0 < pi_lo < pi_hi, width < 1e-20)',
      0 < pi_lo < pi_hi and pi_hi - pi_lo < Fr(1, 10 ** 20))
check('A1b pi_lo > 3 and pi_hi < 22/7', pi_lo > 3 and pi_hi < Fr(22, 7))


def catalan_bracket(M):
    """G = sum_{m>=0} g_m, g_m = 1/(4m+1)^2 - 1/(4m+3)^2 > 0 (paired Catalan
    series, all terms positive).  Lower bound: partial sum over m < M.  Tail:
    g_m = int_{4m+1}^{4m+3} 2 x^-3 dx <= 2 * 2/(4m+1)^3 = 4/(4m+1)^3, and
    sum_{m>=M} 4/(4m+1)^3 <= 4/(4M+1)^3 + int_M^inf 4/(4x+1)^3 dx
                          = 4/(4M+1)^3 + 1/(2 (4M+1)^2)."""
    S = sum((Fr(1, (4 * m + 1) ** 2) - Fr(1, (4 * m + 3) ** 2) for m in range(M)), Fr(0))
    tail_hi = Fr(4, (4 * M + 1) ** 3) + Fr(1, 2 * (4 * M + 1) ** 2)
    return S, S + tail_hi


G_lo, G_hi = catalan_bracket(200)
out('G_lo  =', dec(G_lo, 12))
out('G_hi  =', dec(G_hi, 12))
check('A2 G bracket consistent (0 < G_lo < G_hi, width < 1e-6)',
      0 < G_lo < G_hi and G_hi - G_lo < Fr(1, 10 ** 6))
check('A2b 0.9159 < G_lo and G_hi < 0.9160', G_lo > Fr(9159, 10000) and G_hi < Fr(9160, 10000))

m2_lo = 32 * G_lo ** 2 / pi_hi ** 3   # lower bound of m^2 (G down, pi up)
m2_hi = 32 * G_hi ** 2 / pi_lo ** 3   # upper bound of m^2 (G up, pi down)
check('A3 m^2 bracket consistent', 0 < m2_lo < m2_hi)
check('A4 LOWER: 32 G_lo^2 / pi_hi^3 > (9305/10000)^2', m2_lo > Fr(9305, 10000) ** 2)
check('A5 UPPER: 32 G_hi^2 / pi_lo^3 < (9306/10000)^2', m2_hi < Fr(9306, 10000) ** 2)
m_lo = sqrt_lo(m2_lo, 12)
m_hi = sqrt_hi(m2_hi, 12)
out('derived E sqrt(tau) in [', dec(m_lo, 12), ',', dec(m_hi, 12), ']  (12-decimal outer bracket)')
check('A6 derived outer bracket inside (9305/10000, 9306/10000)',
      Fr(9305, 10000) < m_lo and m_hi < Fr(9306, 10000))
check('A7 consequence 1/E sqrt(tau) > 10000/9306  (equivalently m < 9306/10000)',
      m2_hi < Fr(9306, 10000) ** 2)

# Negative controls for Part A
check('NA1 enclosure must NOT certify E sqrt(tau) > 9306/10000', m2_lo > Fr(9306, 10000) ** 2, expect=False)
check('NA2 enclosure must NOT certify E sqrt(tau) < 9305/10000', m2_hi < Fr(9305, 10000) ** 2, expect=False)
wrong_a = 32 * G_hi ** 2 / pi_lo ** 2   # exponent slip pi^2 instead of pi^3
wrong_b = 16 * G_hi ** 2 / pi_lo ** 3   # coefficient slip 16 instead of 32
check('NA3 wrong formula 32 G^2/pi^2 falls outside (0.9305^2, 0.9306^2)',
      Fr(9305, 10000) ** 2 < wrong_a < Fr(9306, 10000) ** 2, expect=False)
check('NA4 wrong formula 16 G^2/pi^3 falls outside (0.9305^2, 0.9306^2)',
      Fr(9305, 10000) ** 2 < wrong_b < Fr(9306, 10000) ** 2, expect=False)
G_lo2, G_hi2 = catalan_bracket(2)
check('NA5 too-short Catalan sum (M=2) is too loose to certify the upper bound',
      32 * G_hi2 ** 2 / pi_lo ** 3 < Fr(9306, 10000) ** 2, expect=False)

# =====================================================================
# Part B: exact combination arithmetic and parameter checks
# =====================================================================
out('\n=== Part B: exact combination arithmetic ===')
f_delta = Fr(8191, 8192)       # sqrt(1-delta/T) >= 1-delta/T >= 8191/8192
f_N = Fr(4095, 4096)           # E|B_(tau^N)| >= 1 - 1/N, N = 4096
f_cat = Fr(10000, 9306)        # 1/E sqrt(tau) > 10000/9306  (Part A)
r_claim = f_delta * f_N * f_cat
out('(8191/8192)(4095/4096)(10000/9306) =', r_claim, '=', dec(r_claim, 12))
check('B1 product equals 2329315625/2168455168 exactly', r_claim == Fr(2329315625, 2168455168))
check('B2 2329315625/2168455168 > 107/100', r_claim > Fr(107, 100))
check('B2b 2329315625/2168455168 < 108/100 (claim is not overstated)', r_claim < Fr(108, 100))
check('B2c 1.0741 < ratio < 1.0742', Fr(10741, 10000) < r_claim < Fr(10742, 10000))
check('B1b gcd check: fraction is in lowest terms', math.gcd(2329315625, 2168455168) == 1)

r_pred = Fr(8191, 8192) * Fr(4095, 4096) * Fr(1944, 1943)
check('B3 predecessor product equals 8150741235/8149532672', r_pred == Fr(8150741235, 8149532672))
check('B4 predecessor product = 1 + 1208563/8149532672', r_pred - 1 == Fr(1208563, 8149532672))
check('B4b predecessor multiplier in (1.00014, 1.00015)', Fr(100014, 100000) < r_pred < Fr(100015, 100000))
check('B5 1-1/4096 = 4095/4096 and 1-1/8192 = 8191/8192',
      1 - Fr(1, 4096) == Fr(4095, 4096) and 1 - Fr(1, 8192) == Fr(8191, 8192))
# sqrt(1-y) >= 1-y on [0,1]  <=>  (1-y) >= (1-y)^2  <=> 0 <= 1-y <= 1.  Exact grid check.
check('B6 (1-y) >= (1-y)^2 on grid y=j/4096, j=0..4096',
      all((1 - Fr(j, 4096)) >= (1 - Fr(j, 4096)) ** 2 for j in range(4097)))

# delta = min((T-h)/2, T/8192): positive, support [0,delta] inside [0,T-h), delta <= T/8192
grid_ok = True
branch_counts = {'S/2': 0, 'T/8192': 0}
for T in (Fr(1), Fr(1, 3), Fr(7, 2), Fr(10 ** 6), Fr(1, 10 ** 6)):
    for hfrac in (Fr(0), Fr(1, 2), Fr(4094, 4096), Fr(4095, 4096), Fr(8191, 8192), Fr(1) - Fr(1, 10 ** 9)):
        h = T * hfrac
        S = T - h
        delta = min(S / 2, T / 8192)
        branch_counts['S/2' if S / 2 <= T / 8192 else 'T/8192'] += 1
        cond = (delta > 0) and (delta <= S / 2) and (delta < S) and (delta <= T / 8192) \
            and (1 - delta / T >= Fr(8191, 8192))
        grid_ok = grid_ok and cond
check('B7 delta=min((T-h)/2,T/8192): delta>0, [0,delta] in [0,T-h), 1-delta/T >= 8191/8192 (30 cases)', grid_ok)
out('   branch usage over grid:', branch_counts)
check('B7b branch switch at h/T = 4095/4096: T/8192 <= (T-h)/2  iff  h <= T*(4095/4096)',
      all((Fr(1, 8192) <= (1 - x) / 2) == (x <= Fr(4095, 4096)) for x in (Fr(0), Fr(1, 2), Fr(4094, 4096), Fr(4095, 4096), Fr(4096, 4097), Fr(8191, 8192))))

# minimal N such that (1-1/N)(8191/8192)(10000/9306) > 1
Nmin = next(N for N in range(1, 10 ** 6) if (1 - Fr(1, N)) * f_delta * f_cat > 1)
out('   smallest N with (1-1/N)(8191/8192)(10000/9306) > 1 :', Nmin)
check('B8 N=4096 is far above the minimal N (=%d) needed for a certified gap' % Nmin, 4096 > Nmin)

# Negative controls for Part B
# NB1: wrong delta = T/2 (ignores the preview support constraint)
T, h = Fr(1), Fr(3, 4)
bad_delta = T / 2
check('NB1a wrong delta=T/2 with h=3T/4 violates support [0,delta] in [0,T-h]', bad_delta <= T - h, expect=False)
# certified factor squared with this delta: (1-delta/T) * f_N^2 * f_cat^2  < 1  -> no gap certified
check('NB1b wrong delta=T/2: (1-delta/T) f_N^2 f_cat^2 < 1, i.e. NO gap certified',
      (1 - bad_delta / T) * f_N ** 2 * f_cat ** 2 >= 1, expect=False)
# NB2: wrong delta = T/4096 breaks the specific stated factor 8191/8192
bad_delta2 = Fr(1, 4096)
check('NB2a wrong delta=T/4096: 1-delta/T >= 8191/8192 FAILS', 1 - bad_delta2 >= Fr(8191, 8192), expect=False)
check('NB2b (honest note) with factor 4095/4096 instead the product still exceeds 1',
      Fr(4095, 4096) * f_N * f_cat > 1)
# NB3: wrong stopping rule = deterministic time sigma = 1 (Jensen slack vanishes):
#      E|B_1|/E sqrt(1) = sqrt(2/pi) < 1 ;  exact: 2/pi < 1  <=>  pi > 2
check('NB3 deterministic stopping (sigma=1): factor^2 = 2/pi < 1, hence NO gap over sqrt(T)', 2 / pi_lo < 1)
check('NB3b deterministic stopping: 2/pi < 0.64 so factor < 0.8', 2 / pi_lo < Fr(64, 100))
# NB4: Markov factor 1-1/N with N=1 is vacuous (certified bound 0)
check('NB4 N=1 gives vacuous factor 1-1/N = 0 -> certified ratio 0, NO gap', (1 - Fr(1, 1)) * f_delta * f_cat > 1, expect=False)

# E tau = 1 check through the eigen-series:  E tau = (32/pi^3) * beta(3),  beta(3) = sum (-1)^k/(2k+1)^3 = pi^3/32
# exact rational enclosure of (32/pi^3) * beta(3) must contain 1
def beta3_bracket(M):
    # paired positive series: sum_m [1/(4m+1)^3 - 1/(4m+3)^3], term <= int_{4m+1}^{4m+3} 3 x^-4 dx <= 6/(4m+1)^4
    S = sum((Fr(1, (4 * m + 1) ** 3) - Fr(1, (4 * m + 3) ** 3) for m in range(M)), Fr(0))
    tail_hi = Fr(6, (4 * M + 1) ** 4) + Fr(1, 2 * (4 * M + 1) ** 3)   # f(M) + int_M^inf 6/(4x+1)^4 dx
    return S, S + tail_hi


b3_lo, b3_hi = beta3_bracket(200)
Etau_lo = 32 * b3_lo / pi_hi ** 3
Etau_hi = 32 * b3_hi / pi_lo ** 3
out('   E tau via eigen-series enclosure: [', dec(Etau_lo, 10), ',', dec(Etau_hi, 10), ']')
check('B9 E tau = 32 beta(3)/pi^3 enclosure contains 1 (consistency of the exit law with Wald E tau = 1)',
      Etau_lo < 1 < Etau_hi)

# =====================================================================
# Part C: NON-load-bearing numerical cross-checks (mpmath / numpy)
# =====================================================================
out('\n=== Part C: numerical cross-checks (NOT proof arithmetic) ===')
try:
    import mpmath as mp
    mp.mp.dps = 30
    v1 = 4 * mp.sqrt(2 * mp.pi) * mp.catalan / mp.pi ** 2
    out('C1 closed form 4 sqrt(2pi) G/pi^2            =', mp.nstr(v1, 25))
    # Laplace route: E e^{-lam tau} = sech(sqrt(2 lam));
    # sqrt(s) = (1/(2 sqrt(pi))) int_0^inf (1-e^{-lam s}) lam^{-3/2} d lam
    # => E sqrt(tau) = sqrt(2/pi) int_0^inf (1 - sech u)/u^2 du   (lam = u^2/2)
    v2 = mp.sqrt(2 / mp.pi) * mp.quad(lambda u: (1 - mp.sech(u)) / u ** 2, [0, 1, 10, mp.inf])
    out('C2 Laplace-transform route sqrt(2/pi)Int(1-sech u)/u^2 =', mp.nstr(v2, 25))
    # survival function two ways
    def surv_eigen(t, K=60):
        return (4 / mp.pi) * mp.fsum(((-1) ** k) / (2 * k + 1) * mp.exp(-(2 * k + 1) ** 2 * mp.pi ** 2 * t / 8) for k in range(K))

    def surv_images(t, K=12):
        rt = mp.sqrt(t)
        return mp.fsum(((-1) ** n) * (mp.ncdf((2 * n + 1) / rt) - mp.ncdf((2 * n - 1) / rt)) for n in range(-K, K + 1))

    maxdiff = max(abs(surv_eigen(t) - surv_images(t)) for t in (mp.mpf('0.05'), mp.mpf('0.1'), mp.mpf('0.25'), mp.mpf('0.5'), mp.mpf(1), mp.mpf(2), mp.mpf(5)))
    out('C3 max |P(tau>t)_eigen - P(tau>t)_images| over 7 t-values =', mp.nstr(maxdiff, 5))
    check('C3 eigen-series and method-of-images survival agree to 1e-20', maxdiff < mp.mpf('1e-20'))
    out('   P(tau>1/4) =', mp.nstr(surv_images(mp.mpf('0.25')), 15), ' P(tau>1) =', mp.nstr(surv_eigen(mp.mpf(1)), 15),
        ' P(tau>4096) =', mp.nstr(surv_eigen(mp.mpf(4096)), 5))
    # E sqrt(tau) from the survival function (images for small t, eigen for large t)
    v3 = mp.quad(lambda t: surv_images(t) / (2 * mp.sqrt(t)), [0, mp.mpf('0.5')]) + \
        mp.quad(lambda t: surv_eigen(t) / (2 * mp.sqrt(t)), [mp.mpf('0.5'), 5, 50, mp.inf])
    out('C4 tail-integral route Int P(tau>t)/(2 sqrt t) dt       =', mp.nstr(v3, 25))
    check('C5 three numerical routes agree with the closed form to 1e-18',
          abs(v1 - v2) < mp.mpf('1e-18') and abs(v1 - v3) < mp.mpf('1e-18'))
    Etau_num = mp.quad(lambda t: surv_images(t), [0, mp.mpf('0.5')]) + mp.quad(lambda t: surv_eigen(t), [mp.mpf('0.5'), 5, 50, mp.inf])
    out('C6 E tau numerically =', mp.nstr(Etau_num, 20))
    check('C6 E tau numerically = 1 to 1e-18', abs(Etau_num - 1) < mp.mpf('1e-18'))
    out('   1/E sqrt(tau) =', mp.nstr(1 / v1, 20), '  certified rational factor 10000/9306 =', mp.nstr(mp.mpf(10000) / 9306, 20))
    out('   P(tau <= 1/4) =', mp.nstr(1 - surv_images(mp.mpf('0.25')), 10), ' vs predecessor crude bound 1/243 =', mp.nstr(mp.mpf(1) / 243, 10))
    out('   1 - E sqrt(tau) =', mp.nstr(1 - v1, 10), ' vs predecessor crude bound 1/1944 =', mp.nstr(mp.mpf(1) / 1944, 10))
except Exception as e:  # pragma: no cover
    out('Part C mpmath block raised:', repr(e))
    RESULTS['C-block'] = False

# Monte Carlo of the actual witness (discretised; plausibility only)
try:
    import numpy as np
    rng = np.random.default_rng(20261028)
    T_mc, h_mc = 1.0, 0.0
    N_mc = 4096
    delta_mc = min((T_mc - h_mc) / 2, T_mc / 8192)
    ds = 1e-4
    npaths = 20000
    B = np.zeros(npaths)
    alive = np.ones(npaths, dtype=bool)
    tau_d = np.full(npaths, np.nan)
    Bstop = np.zeros(npaths)
    intB2 = np.zeros(npaths)   # int_0^{tau_d} B_s^2 ds (fast time)
    s = 0.0
    sq = math.sqrt(ds)
    step = 0
    while alive.any() and s < N_mc:
        idx = np.flatnonzero(alive)
        B[idx] += sq * rng.standard_normal(idx.size)
        intB2[idx] += B[idx] ** 2 * ds
        s += ds
        step += 1
        hit = idx[np.abs(B[idx]) >= 1.0]
        if hit.size:
            tau_d[hit] = s
            Bstop[hit] = B[hit]
            alive[hit] = False
    if alive.any():
        tau_d[alive] = N_mc
        Bstop[alive] = B[alive]
    tauN = np.minimum(tau_d, N_mc)
    w_norm = np.sqrt(tauN)                                  # ||w||_{L2[0,T]} = sqrt(tau ^ N)
    z_norm2 = (delta_mc / N_mc) * intB2 + (T_mc - delta_mc * tauN / N_mc) * Bstop ** 2
    z_norm = np.sqrt(z_norm2)
    ratio = z_norm.mean() / w_norm.mean()
    se_w = w_norm.std(ddof=1) / math.sqrt(npaths)
    se_z = z_norm.std(ddof=1) / math.sqrt(npaths)
    out(f'C7 Monte Carlo witness T=1,h=0,N=4096,delta={delta_mc:.3e}, ds={ds}, paths={npaths}, steps={step}')
    out(f'   E||w|| ~ {w_norm.mean():.5f} (se {se_w:.5f}), E||z|| ~ {z_norm.mean():.5f} (se {se_z:.5f}), E|B_stop| ~ {np.abs(Bstop).mean():.5f}, max tau_d ~ {np.nanmax(tau_d):.3f}')
    out(f'   ratio E||z||/E||w|| ~ {ratio:.5f}   (certified lower bound 1.07418 sqrt(T); limit value 1/E sqrt(tau) = 1.07466)')
    check('C7 Monte Carlo ratio exceeds 1.05 sqrt(T) (plausibility only; discretisation biases are O(sqrt(ds)))', ratio > 1.05)
    # negative control: deterministic input on [0,delta] with the same energy scale (sigma = 1 fixed)
    Bdet = rng.standard_normal(npaths)   # B_1
    z_det = np.sqrt((T_mc - delta_mc) * Bdet ** 2 + 0.0)   # ignores the tiny [0,delta] part (lower bound part only)
    ratio_det_lb_part = z_det.mean() / 1.0
    out(f'   deterministic stopping control: E|B_1| ~ {np.abs(Bdet).mean():.5f} (sqrt(2/pi)=0.79788), ratio part ~ {ratio_det_lb_part:.5f} < 1')
    check('C8 deterministic-stopping control ratio part < 1 (no gap)', ratio_det_lb_part < 1.0)
except Exception as e:  # pragma: no cover
    out('Part C Monte Carlo block raised:', repr(e))
    RESULTS['C-mc'] = False

# =====================================================================
out('\n=== Summary ===')
npass = sum(1 for v in RESULTS.values() if v)
nfail = sum(1 for v in RESULTS.values() if not v)
out(f'checks passed: {npass}, failed: {nfail}')
for k, v in RESULTS.items():
    if not v:
        out('  FAILED:', k)
with open(os.path.abspath(__file__), 'rb') as fh:
    out('self sha256 =', hashlib.sha256(fh.read()).hexdigest())
out('reviewer-exact-controls-v1.py end UTC', utc())
with open(LOG, 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(_lines) + '\n')
sys.exit(0 if nfail == 0 else 1)
