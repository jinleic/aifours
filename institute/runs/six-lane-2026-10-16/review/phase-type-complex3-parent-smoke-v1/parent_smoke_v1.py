# Parent smoke v1 for the untrusted all-n PH cycle construction (Commault-Mocanu 2003 Conjecture 1 family).
# Finite high-precision smoke only: NOT a proof. Pure Python + mpmath; executed in-process by the parent.
import json, random, hashlib, time
import mpmath as mp
mp.mp.dps = 60
PI = mp.pi

def nstar(beta):
    n = 3
    while beta > mp.cot(PI / n):
        n += 1
    return n

def build(a, b, c, n=None, mutate=None):
    a, b, c = mp.mpf(a), mp.mpf(b), mp.mpf(c)
    d = a - c; A = a / d; C = c / d; beta = b / d
    ns = nstar(beta)
    if n is None: n = ns
    phi = mp.atan(beta); psi = PI - 2 * phi; S = 2 * PI - (n - 3) * psi
    G = lambda t: mp.sin(t + phi) * mp.sin((S - t) / 2 + phi) ** 2 - mp.sin(phi) ** 3
    lo, hi = mp.mpf(0), S / 3
    rec = {'n': n, 'nstar': ns, 'G0': float(G(lo)), 'GS3': float(G(hi)), 'S_over_psi': float(S / psi)}
    if not (G(lo) < 0 and G(hi) >= 0 and S / 2 <= PI - phi):
        rec['applicable'] = False
        return rec, None
    rec['applicable'] = True
    if G(hi) == 0:
        t = hi
    else:
        for _ in range(400):
            mid = (lo + hi) / 2
            if G(mid) < 0: lo = mid
            else: hi = mid
        t = hi
    th = [t, (S - t) / 2, (S - t) / 2] + [psi] * (n - 3)
    m = [-beta * mp.cot(x) for x in th]
    if mutate == 'wrong_mstar':
        m = m[:3] + [(1 + beta * beta) / 2 - mp.mpf(1) / 3] * (n - 3)
    W = mp.mpf(1)
    for mi in m: W *= (1 - mi)
    K = C * (A * A + beta * beta)
    rho = (1 + beta * beta) / 2
    coef = [(mp.cos(psi / 2) - mp.cos((k + mp.mpf(3) / 2) * psi)) / (2 * mp.sin(psi / 2) * mp.sin(psi)) * rho ** (-3 - k) for k in range(max(n - 3, 0))]
    tv = [mp.mpf(0), mp.mpf(0), K] + [K * W * coef[n - j] for j in range(4, n + 1)]
    if mutate == 'exit':
        tv[-1] = tv[-1] * (1 + mp.mpf('1e-3'))
    M = mp.zeros(n, n)
    for i in range(n):
        M[i, i] = m[i]
        if i < n - 1: M[i, i + 1] = 1
    M[n - 1, 0] = W
    T0 = (M - A * mp.eye(n)) * d
    tt = mp.matrix(tv) * d
    v = -mp.lu_solve(T0, tt)
    T = mp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            T[i, j] = T0[i, j] * v[j] / v[i]
    ex = [-sum(T[i, j] for j in range(n)) for i in range(n)]
    rec.update({
        'theta_min': float(min(th)), 'theta_max_minus_pi_minus_phi': float(max(th) - (PI - phi)),
        'sum_theta_minus_2pi': float(abs(sum(th) - 2 * PI)),
        'prod_identity_residual': float(abs(mp.fprod([mp.sin(x + phi) for x in th]) - mp.sin(phi) ** n)),
        'min_offdiag': float(min(T[i, j] for i in range(n) for j in range(n) if i != j)),
        'min_exit': float(min(ex)), 'min_v': float(min(v)), 'v1_minus_1': float(abs(v[0] - 1)),
        'min_tvec': float(min(tv)),
    })
    errs = []
    for s in [mp.mpf(0), mp.mpf('0.3'), mp.mpf('1.7'), mp.mpc(2, 1), mp.mpc('0.5', -3), mp.mpf(10)]:
        Fs = c * (a * a + b * b) / ((s + c) * ((s + a) ** 2 + b * b))
        x = mp.lu_solve(s * mp.eye(n) - T, mp.matrix(ex))
        errs.append(abs(Fs - x[0]) / max(1, abs(Fs)))
    rec['max_rel_transfer_err'] = float(max(errs))
    if n <= 22:
        ev = mp.eig(T, left=False, right=False)
        mx = max(ev, key=lambda z: mp.re(z))
        rec['max_re_eig'] = float(mp.re(mx)); rec['dominant_plus_c'] = float(abs(mx + c))
    return rec, T

def ok(rec, tol=mp.mpf('1e-40')):
    return (rec.get('applicable') and rec['theta_min'] > 0 and rec['theta_max_minus_pi_minus_phi'] < 0
            and rec['sum_theta_minus_2pi'] < 1e-40 and rec['prod_identity_residual'] < 1e-40
            and rec['min_offdiag'] >= 0 and rec['min_exit'] >= -1e-45 and rec['min_v'] > 0 and rec['v1_minus_1'] < 1e-40
            and rec['min_tvec'] >= 0 and rec['max_rel_transfer_err'] < 1e-40
            and (('max_re_eig' not in rec) or (rec['max_re_eig'] < 0 and rec['dominant_plus_c'] < 1e-30)))

def main(out):
    rng = random.Random(20261018)
    cases = []
    for n in range(4, 13):
        cases.append(('upper_endpoint', n, 1 + n / 7, mp.cot(PI / n), 1))
        cases.append(('near_lower_endpoint', n + 1, 2.5, mp.cot(PI / n) * (1 + mp.mpf('1e-12')), 1.25))
    for k in range(120):
        c = mp.mpf(rng.uniform(0.05, 5)); d = mp.mpf(rng.uniform(0.05, 5)); target = rng.randint(4, 30)
        lo, hi = mp.cot(PI / (target - 1)), mp.cot(PI / target)
        beta = lo + (hi - lo) * mp.mpf(rng.uniform(0.001, 1.0))
        cases.append(('random', target, c + d, beta * d, c))
    res = []; npass = 0
    for kind, ntarget, a, b, c in cases:
        a, b, c = mp.mpf(a), mp.mpf(b), mp.mpf(c)
        if kind != 'random':
            b = b * (a - c)
        rec, _ = build(a, b, c)
        rec.update({'kind': kind, 'a': str(a), 'b': str(b), 'c': str(c), 'expected_nstar': ntarget, 'pass': bool(ok(rec)) and rec['nstar'] == ntarget})
        npass += rec['pass']; res.append(rec)
    controls = []
    a, b, c = mp.mpf(3), mp.mpf(4), mp.mpf(1)
    r0, _ = build(a, b, c); controls.append({'name': 'baseline_3_4_1', 'pass': bool(ok(r0)), 'rec': r0})
    r1, _ = build(a, b, c, n=r0['nstar'] - 1)
    controls.append({'name': 'n_minus_1_not_applicable', 'pass': r1.get('applicable') is False, 'rec': r1})
    r2, _ = build(a, b, c, mutate='exit')
    controls.append({'name': 'perturbed_exit_breaks_transfer', 'pass': r2['max_rel_transfer_err'] > 1e-8, 'rec': r2})
    r3, _ = build(a, b, c, mutate='wrong_mstar')
    controls.append({'name': 'wrong_mstar_breaks_transfer_or_positivity', 'pass': (r3['max_rel_transfer_err'] > 1e-8) or (r3['min_exit'] < 0), 'rec': r3})
    r4, _ = build(2, mp.cot(PI / 3) * 1 * mp.mpf('0.999'), 1)
    controls.append({'name': 'order3_regime_not_used', 'pass': r4['nstar'] == 3 and r4.get('applicable') is False, 'rec': r4})
    summary = {'cases': len(res), 'pass': npass, 'controls_pass': sum(1 for x in controls if x['pass']), 'controls': len(controls), 'dps': mp.mp.dps}
    with open(out, 'x') as f:
        json.dump({'summary': summary, 'cases': res, 'controls': controls}, f, indent=1, default=str)
    return summary
