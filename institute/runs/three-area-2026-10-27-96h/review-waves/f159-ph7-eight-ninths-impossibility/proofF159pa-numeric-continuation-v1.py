#!/usr/bin/env python3
"""proofF159pa spectral continuation (reviewer ReviewF159ProofAttack). FLOATING DIAGNOSTICS ONLY.

Follow-up to proofF159pa-numeric-attack-v1.py, whose random starts converged only at z=0.5.
Here converged z=0.5 spectral solutions (7x7 Metzler, zero row sums WLOG, all 42 off-diagonal
entries theta^2, det(yI-G) divisible by y((y+1)^2+z)^2) are continued upward in z with adaptive
steps. Along every path the Lemma 1 / Lemma 3 / z-crude-system chain is evaluated ("just below the
bound" controls). Then z=8/9 is attacked from the highest solutions reached. Residual ~0 at 8/9
would be a counterexample candidate to the (purely spectral) theorem; failure is NOT proof.
"""
import itertools, json, math, time
import numpy as np

OUT = ('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/'
       'f159-ph7-eight-ninths-impossibility/proofF159pa-numeric-continuation-v1-result.json')
n = 7
OFF = np.array([[i != j for j in range(n)] for i in range(n)])
rng = np.random.default_rng(15902)


def build(theta):
    G = np.zeros((n, n))
    G[OFF] = theta ** 2
    G[np.diag_indices(n)] = -G.sum(axis=1)
    return G


def target(z):
    quad = np.array([1.0, 2.0, 1.0 + z])
    return np.polymul([1.0, 0.0], np.polymul(quad, quad))


def resid(theta, z):
    chi = np.real(np.poly(build(theta)))
    _, r = np.polydiv(chi, target(z))
    r = np.atleast_1d(r)
    out = np.zeros(5)
    out[5 - len(r):] = r
    return out, np.linalg.norm(chi)


def solve(theta, z, iters=800):
    mu = 1e-3
    r, sc = resid(theta, z)
    nr = np.linalg.norm(r)
    for _ in range(iters):
        if nr < 1e-12 * max(1.0, sc):
            break
        h = 1e-7
        J = np.empty((5, theta.size))
        for k in range(theta.size):
            tp = theta.copy()
            tp[k] += h
            J[:, k] = (resid(tp, z)[0] - r) / h
        step = -J.T @ np.linalg.solve(J @ J.T + mu * np.eye(5), r)
        t2 = theta + step
        r2, sc2 = resid(t2, z)
        n2 = np.linalg.norm(r2)
        if n2 < nr:
            theta, r, nr, sc = t2, r2, n2, sc2
            mu = max(mu / 3, 1e-15)
        else:
            mu *= 4
            if mu > 1e8:
                break
    return theta, nr, nr / max(1.0, sc)


def ok(rel):
    return rel < 1e-11


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
    W = T3 = C4 = 0.0
    u = -np.diag(G)
    for k in (3, 4):
        for verts in itertools.combinations(range(n), k):
            groups = {}
            for rest in itertools.permutations(verts[1:]):
                seq = (verts[0],) + rest
                edges = [(seq[i], seq[(i + 1) % k]) for i in range(k)]
                w = float(np.prod([G[i, j] for i, j in edges]))
                if w <= 0:
                    continue
                if all(G[j, i] > 0 for i, j in edges):
                    groups.setdefault(frozenset(frozenset(e) for e in edges), []).append(w)
                else:
                    if k == 3:
                        W += w
                        T3 += w * sum(u[i] for i in range(n) if i not in verts)
                    else:
                        C4 += w
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
    quo, _ = np.polydiv(np.real(np.poly(G)), target(z))
    return {'z': z, 'lambda_max_S': float(-ut[0]), 'sG': float(max(ev.real)),
            'hidden_p_q_from_division': [float(quo[1]), float(quo[2])], 'p': p, 'q': q, 'E4': E4, 'W': W,
            'E4-W': E4 - W, 'E3-(T3+C4)': E3 - (T3 + C4), 'K': K, 'S4': S4,
            'ut': [float(x) for x in ut], 'max_offdiag': float(G[OFF].max()),
            'n_positive_offdiag(>1e-8)': int((G[OFF] > 1e-8).sum()),
            'two_cycles(>1e-8)': int(sum(1 for i in range(n) for j in range(i + 1, n) if G[i, j] > 1e-8 and G[j, i] > 1e-8)),
            'G': [[float(x) for x in row] for row in G]}


def main():
    t0 = time.time()
    res = {'kind': 'FLOATING DIAGNOSTICS ONLY', 'paths': []}
    seeds = []
    tries = 0
    while len(seeds) < 5 and tries < 80:
        tries += 1
        th, nr, rel = solve(np.sqrt(rng.uniform(0.0, 0.35, size=42)), 0.5)
        if ok(rel):
            seeds.append(th)
    res['z0.5_seed_tries'] = tries
    finals = []
    for si, th in enumerate(seeds):
        z, step = 0.5, 0.02
        checks = [chain_check(th, z)]
        lastcheck = z
        while step > 2e-4 and z < 0.8888:
            zt = min(z + step, 0.8888)
            got = None
            for attempt in range(5):
                start = th if attempt == 0 else th * (1 + 0.01 * attempt * rng.standard_normal(42))
                t2, nr, rel = solve(start, zt)
                if ok(rel):
                    got = t2
                    break
            if got is not None:
                th, z = got, zt
                step = min(step * 1.5, 0.02)
                if z - lastcheck >= 0.05:
                    checks.append(chain_check(th, z))
                    lastcheck = z
            else:
                step /= 2
        checks.append(chain_check(th, z))
        finals.append((z, th))
        res['paths'].append({'seed': si, 'max_z_reached': z, 'checks': checks})
        print('path', si, 'max z', z, 'elapsed', round(time.time() - t0, 1), flush=True)
    # attack 8/9 from the highest solutions
    best = None
    for z, th in finals:
        for a in range(40):
            start = th * (1 + 0.03 * rng.standard_normal(42)) if a else th.copy()
            _, nr, rel = solve(start, 8 / 9, iters=600)
            best = rel if best is None else min(best, rel)
    res['attack_8_9_min_relative_residual'] = best
    viol = []
    for pth in res['paths']:
        for c in pth['checks']:
            if not (c['lambda_max_S'] < 0 and c['p'] > 0 and c['q'] > 0 and c['E4'] > -1e-8 and c['K'] > -1e-8
                    and abs(c['E4-W']) < 1e-6 and abs(c['E3-(T3+C4)']) < 1e-6):
                viol.append((pth['seed'], c['z']))
    res['chain_violations'] = viol
    res['max_z_overall'] = max(z for z, _ in finals) if finals else None
    res['seconds'] = round(time.time() - t0, 1)
    with open(OUT, 'w') as fh:
        fh.write(json.dumps(res, indent=1, sort_keys=True) + '\n')
    print('max z', res['max_z_overall'], 'violations', viol, 'attack 8/9 min rel residual', best)
    print('wrote', OUT)


if __name__ == '__main__':
    main()
