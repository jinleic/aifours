#!/usr/bin/env python3
"""proofF159pa numeric attack (reviewer ReviewF159ProofAttack). FLOATING DIAGNOSTICS ONLY, not proof.

N1  Spectral attack. WLOG (diagonal similarity preserves the graph, cycle weights, S and spectrum) a
    7x7 Metzler G with spectral bound 0 has zero row sums. Parametrise all 42 off-diagonal entries
    as theta^2 and drive the remainder of det(yI-G) modulo y((y+1)^2+z)^2 to zero by a minimum-norm
    damped Gauss-Newton iteration, random restarts plus continuation in z. A residual ~0 at z=8/9
    would be a counterexample candidate to the theorem (purely spectral statement).
N2  For every converged spectral solution at z<8/9 ("just below the bound" controls): Lemma 1
    (lambda_max(S)<0), Lemma 3 (E4_z(ut)=W, E3_z(ut)=sum omega tr + C4) and the z-dependent crude
    system (p>0, q>0, E4>=0, K>=0) are evaluated; any violation would refute Lemmas 1-4.
N3  Crude-system attack: maximise m(v)=min(p,q,E4,K) over seven positive reals by Nelder-Mead
    (many starts) at several z including 8/9. A feasible point found at some z<8/9 is rationalised
    and re-verified EXACTLY with Fractions (exact witness of non-vacuity at that z).
"""
import itertools, json, math, random, time
from fractions import Fraction as Fr
import numpy as np

OUT = ('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/'
       'f159-ph7-eight-ninths-impossibility/proofF159pa-numeric-attack-v1-result.json')
n = 7
OFF = np.array([[i != j for j in range(n)] for i in range(n)])
rng = np.random.default_rng(159)
R = {'script': 'proofF159pa-numeric-attack-v1.py', 'kind': 'FLOATING DIAGNOSTICS ONLY'}


def build(theta):
    G = np.zeros((n, n))
    G[OFF] = theta ** 2
    G[np.diag_indices(n)] = -G.sum(axis=1)
    return G


def target(z):
    quad = np.array([1.0, 2.0, 1.0 + z])
    return np.polymul([1.0, 0.0], np.polymul(quad, quad))


def resid(theta, z):
    G = build(theta)
    chi = np.real(np.poly(G))
    _, r = np.polydiv(chi, target(z))
    r = np.atleast_1d(r)
    out = np.zeros(5)
    out[5 - len(r):] = r
    return out


def solve(theta, z, iters=400, tol=1e-14):
    mu = 1e-3
    r = resid(theta, z)
    nr = np.linalg.norm(r)
    for _ in range(iters):
        if nr < tol:
            break
        h = 1e-7
        J = np.empty((5, theta.size))
        for k in range(theta.size):
            tp = theta.copy()
            tp[k] += h
            J[:, k] = (resid(tp, z) - r) / h
        M = J @ J.T + mu * np.eye(5)
        step = -J.T @ np.linalg.solve(M, r)
        t2 = theta + step
        r2 = resid(t2, z)
        n2 = np.linalg.norm(r2)
        if n2 < nr:
            theta, r, nr = t2, r2, n2
            mu = max(mu / 3, 1e-15)
        else:
            mu *= 4
            if mu > 1e8:
                break
    return theta, nr


def esym(v, k):
    E = [1.0] + [0.0] * k
    for x in v:
        for j in range(k, 0, -1):
            E[j] += E[j - 1] * x
    return E[k]


def crude_float(v, z):
    k = 1 + z
    e1, e2, e3, e4 = (esym(v, j) for j in (1, 2, 3, 4))
    p = e1 - 4
    q = e2 - 4 * e1 + 12 - 2 * k
    E4 = e3 - 4 * e2 + (12 - 2 * k) * e1 + 12 * k - 32
    E3 = e4 - (4 + 2 * k) * e2 + (16 + 4 * k) * e1 + 3 * k * k - 48
    S4 = sum(sorted(v)[:4])
    return p, q, E4, E3, E3 - E4 * S4, S4


def cycle_data(G):
    """Extra-cycle bookkeeping of Lemma 2 in floating point: W, sum omega tr(A_{V\\C}) (|C|=3), C4."""
    W = T3 = C4 = 0.0
    u = -np.diag(G)
    for k in (3, 4):
        for verts in itertools.combinations(range(n), k):
            groups = {}
            for rest in itertools.permutations(verts[1:]):
                seq = (verts[0],) + rest
                edges = [(seq[i], seq[(i + 1) % k]) for i in range(k)]
                w = np.prod([G[i, j] for i, j in edges])
                if w <= 0:
                    continue
                if all(G[j, i] > 0 for i, j in edges):
                    groups.setdefault(frozenset(frozenset(e) for e in edges), []).append(w)
                else:
                    om = w
                    if k == 3:
                        W += om
                        T3 += om * sum(u[i] for i in range(n) if i not in verts)
                    else:
                        C4 += om
            for ws in groups.values():
                om = (math.sqrt(ws[0]) - math.sqrt(ws[1])) ** 2
                if k == 3:
                    W += om
                    T3 += om * sum(u[i] for i in range(n) if i not in verts)
                else:
                    C4 += om
    return W, T3, C4


def chain_check(theta, z):
    G = build(theta)
    S = np.where(OFF, np.sqrt(G * G.T), G)
    ut = np.sort(np.linalg.eigvalsh(-S))
    p, q, E4, E3, K, S4 = crude_float(list(ut), z)
    W, T3, C4 = cycle_data(G)
    ev = np.linalg.eigvals(G)
    chi = np.real(np.poly(G))
    quo, _ = np.polydiv(chi, target(z))
    return {'z': z, 'lambda_max_S': float(-ut[0]), 'sG': float(max(ev.real)),
            'hidden_quadratic_p_q': [float(quo[1]), float(quo[2])], 'p': p, 'q': q, 'E4': E4, 'W': W,
            'E4-W': E4 - W, 'E3-(T3+C4)': E3 - (T3 + C4), 'K': K, 'S4': S4,
            'min_offdiag': float(G[OFF].min()), 'max_offdiag': float(G[OFF].max()),
            'n_positive_offdiag(>1e-9)': int((G[OFF] > 1e-9).sum()),
            'two_cycles(>1e-9)': int(sum(1 for i in range(n) for j in range(i + 1, n) if G[i, j] > 1e-9 and G[j, i] > 1e-9))}


def N1_N2():
    out = {'random_start_success': {}, 'continuation': [], 'attack_8_9': {}, 'chain_checks': []}
    sols = {}
    for z in (0.5, 0.7, 0.78):
        best = None
        succ = 0
        for s in range(40):
            th0 = np.sqrt(rng.uniform(0.0, 0.35, size=42))
            th, nr = solve(th0, z)
            if nr < 1e-11:
                succ += 1
                if best is None or nr < best[1]:
                    best = (th, nr)
        out['random_start_success'][str(z)] = succ
        if best:
            sols[z] = best[0]
    # continuation upward from the z=0.78 solution(s)
    zs = [round(0.78 + 0.0025 * i, 4) for i in range(1, 45)]
    cur = sols.get(0.78)
    last_ok = 0.78 if cur is not None else None
    for z in zs:
        if cur is None:
            break
        best = None
        for s in range(12):
            th0 = cur * (1 + 0.02 * rng.standard_normal(42)) if s else cur.copy()
            th, nr = solve(th0, z, iters=600)
            if best is None or nr < best[1]:
                best = (th, nr)
        out['continuation'].append([z, float(best[1])])
        if best[1] < 1e-11:
            cur = best[0]
            last_ok = z
            sols[z] = cur
        else:
            break
    out['continuation_last_z_with_residual_below_1e-11'] = last_ok
    # attack z = 8/9
    z = 8 / 9
    bestn = None
    for s in range(150):
        if s < 30 and cur is not None:
            th0 = cur * (1 + 0.05 * rng.standard_normal(42))
        else:
            th0 = np.sqrt(rng.uniform(0.0, 0.35, size=42))
        th, nr = solve(th0, z, iters=500)
        if bestn is None or nr < bestn:
            bestn = nr
    out['attack_8_9'] = {'starts': 150, 'min_residual_norm': float(bestn)}
    # N2 chain checks on solutions
    for zz in sorted(sols):
        rec = chain_check(sols[zz], zz)
        out['chain_checks'].append(rec)
    return out


def nelder_mead(f, x0, step=0.3, iters=3000, tol=1e-13):
    d = len(x0)
    pts = [x0] + [x0 + step * np.eye(d)[i] for i in range(d)]
    vals = [f(p) for p in pts]
    for _ in range(iters):
        order = np.argsort(vals)
        pts = [pts[i] for i in order]
        vals = [vals[i] for i in order]
        if abs(vals[-1] - vals[0]) < tol:
            break
        c = np.mean(pts[:-1], axis=0)
        xr = c + (c - pts[-1])
        fr = f(xr)
        if fr < vals[0]:
            xe = c + 2 * (c - pts[-1])
            fe = f(xe)
            if fe < fr:
                pts[-1], vals[-1] = xe, fe
            else:
                pts[-1], vals[-1] = xr, fr
        elif fr < vals[-2]:
            pts[-1], vals[-1] = xr, fr
        else:
            xc = c + 0.5 * (pts[-1] - c)
            fc = f(xc)
            if fc < vals[-1]:
                pts[-1], vals[-1] = xc, fc
            else:
                pts = [pts[0] + 0.5 * (p - pts[0]) for p in pts]
                vals = [f(p) for p in pts]
    i = int(np.argmin(vals))
    return pts[i], vals[i]


def crude_exact(v, z):
    k = 1 + z
    def es(j):
        E = [Fr(1)] + [Fr(0)] * j
        for x in v:
            for t in range(j, 0, -1):
                E[t] += E[t - 1] * x
        return E[j]
    e1, e2, e3, e4 = es(1), es(2), es(3), es(4)
    p = e1 - 4
    q = e2 - 4 * e1 + 12 - 2 * k
    E4 = e3 - 4 * e2 + (12 - 2 * k) * e1 + 12 * k - 32
    E3 = e4 - (4 + 2 * k) * e2 + (16 + 4 * k) * e1 + 3 * k * k - 48
    S4 = sum(sorted(v)[:4])
    return p, q, E4, E3 - E4 * S4


def N3():
    out = {}
    witness = None
    for zr in (Fr(80, 100), Fr(85, 100), Fr(87, 100), Fr(875, 1000), Fr(88, 100), Fr(8, 9)):
        z = float(zr)
        def negm(w):
            v = np.exp(w)
            p, q, E4, E3, K, S4 = crude_float(list(v), z)
            return -min(p, q, E4, K)
        best = None
        for s in range(60):
            w0 = np.log(rng.uniform(0.6, 1.3, size=7))
            w, fv = nelder_mead(negm, w0)
            w, fv = nelder_mead(negm, w, step=0.05)
            if best is None or fv < best[1]:
                best = (w, fv)
        v = np.sort(np.exp(best[0]))
        rec = {'max_min_slack_float': float(-best[1]), 'argmax_rates': [float(x) for x in v]}
        if -best[1] > 0:
            vr = [Fr(float(x)).limit_denominator(10 ** 6) for x in v]
            p, q, E4, K = crude_exact(vr, zr)
            rec['exact_rational_witness'] = [str(x) for x in vr]
            rec['exact_witness_feasible'] = p > 0 and q > 0 and E4 >= 0 and K >= 0
            rec['exact_values'] = [str(p), str(q), str(E4), str(K)]
            if rec['exact_witness_feasible'] and witness is None:
                witness = (str(zr), rec['exact_rational_witness'])
            # intended-reason negative: the SAME rational point under the 8/9 constants is infeasible
            p8, q8, E48, K8 = crude_exact(vr, Fr(8, 9))
            rec['same_point_at_8_9_feasible'] = p8 > 0 and q8 > 0 and E48 >= 0 and K8 >= 0
        out[str(zr)] = rec
        print('N3', zr, rec.get('max_min_slack_float'), rec.get('exact_witness_feasible'), flush=True)
    out['first_exact_feasible_witness'] = witness
    return out


def main():
    t = time.time()
    R['N1_N2'] = N1_N2()
    print('N1/N2 done', json.dumps({k: v for k, v in R['N1_N2'].items() if k != 'chain_checks'})[:1500], flush=True)
    viol = [c for c in R['N1_N2']['chain_checks']
            if not (c['lambda_max_S'] < 0 and c['p'] > 0 and c['q'] > 0 and c['E4'] > -1e-9 and c['K'] > -1e-9
                    and abs(c['E4-W']) < 1e-7 and abs(c['E3-(T3+C4)']) < 1e-7)]
    R['N2_violations'] = viol
    print('N2 chain checks:', len(R['N1_N2']['chain_checks']), 'violations:', len(viol), flush=True)
    R['N3'] = N3()
    R['seconds'] = round(time.time() - t, 1)
    with open(OUT, 'w') as fh:
        fh.write(json.dumps(R, indent=1, sort_keys=True, default=float) + '\n')
    print('wrote', OUT)


if __name__ == '__main__':
    main()
