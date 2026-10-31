#!/usr/bin/env python3
"""reviewer-adversarial-search-v2.py  (v2: frame-correct minimiser diagnostics, more starts; v1 kept as run)

Floating-point adversarial search (numpy) written independently by the reviewer
for review f130-depolarizing-global-k10-k5-k6.  No author code is imported or
executed.  Floating-point results are evidence about the searched instances,
not proof.

Targets
  (i)   dual lemma  lam_min(H1(Q) + spinflip(Q)) - (2r-5) >= 0 for rank-r
        projectors Q, r in {5,6,10,11} (claimed) and r in {7,8,9} (informational,
        NOT claimed by the packets); Haar-random and structured starts followed by
        projected-gradient descent on the Stiefel manifold (gradient of lam_min
        w.r.t. Q is H1(W)+spinflip(W) for the minimising eigenprojector W, using
        self-adjointness of both maps in the trace pairing).
  (ii)  output comparison  bottom_r(Phi_p^{(x)4}(psi)) - ref_bottom_r(p) >= 0 for
        pure psi (the bottom-r sum is concave in rho, so pure states suffice),
        r in {5,6,10,11} <-> k in {11,10,6,5}, p on a grid in [0, 4/3]; random
        starts + projected-gradient descent on psi.
  (iii) random-pair checks of Tr[Q H2(rho)] >= r-5 and Tr[Q H1(rho)] >= 2r-6.
  (NEG) the same rank-6 projector search against the false threshold 7.05 must
        report a violation (negative control for the search method).

Run:    python3 -B reviewer-adversarial-search-v2.py
Writes: reviewer-adversarial-search-v2.result.json
"""
import hashlib
import json
import os
import sys
import time
from functools import reduce
from itertools import combinations

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261028
rng = np.random.default_rng(SEED)

I2 = np.eye(2, dtype=complex)
X2 = np.array([[0, 1], [1, 0]], dtype=complex)
Y2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z2 = np.array([[1, 0], [0, -1]], dtype=complex)
NQ, D = 4, 16


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        h.update(fh.read())
    return h.hexdigest()


def site(P, i):
    ops = [I2] * NQ
    ops[i] = P
    return reduce(np.kron, ops)


Y4 = reduce(np.kron, [Y2] * NQ)
PAULIS = {(i, a): site(P, i) for i in range(NQ) for a, P in enumerate((I2, X2, Y2, Z2))}


def erase_pt(X, i):
    """I_i (x) Tr_i X via reshape/partial trace."""
    Xr = X.reshape([2] * (2 * NQ))
    T = np.trace(Xr, axis1=i, axis2=NQ + i)  # 3 row axes + 3 col axes
    R = np.multiply.outer(T, I2)  # ... + (s,t)
    R = np.moveaxis(R, [2 * NQ - 2, 2 * NQ - 1], [i, NQ + i])
    return R.reshape(D, D)


def erase_tw(X, i):
    """I_i (x) Tr_i X via half Pauli twirl (cross-check)."""
    return 0.5 * sum(PAULIS[(i, a)] @ X @ PAULIS[(i, a)] for a in range(4))


def erase_set(X, S):
    for i in S:
        X = erase_pt(X, i)
    return X


def H1(X):
    return sum(erase_set(X, [j for j in range(NQ) if j != i]) for i in range(NQ))


def H2(X):
    return sum(erase_set(X, [k for k in range(NQ) if k not in (i, j)]) for i, j in combinations(range(NQ), 2))


def sf(X):
    return Y4 @ X.T @ Y4


def channel(X, p):
    t, b = 1.0 - p, p / 2.0
    for i in range(NQ):
        X = t * X + b * erase_pt(X, i)
    return X


def ref_bottom(r, p):
    e = np.sort(np.real(np.diag(channel(np.diag([1.0] + [0.0] * 15).astype(complex), p))))
    return float(e[:r].sum())


def random_iso(r):
    Z = rng.standard_normal((D, r)) + 1j * rng.standard_normal((D, r))
    V, _ = np.linalg.qr(Z)
    return V


def ket(x):
    v = np.zeros(D, dtype=complex)
    v[x] = 1.0
    return v


def wt(x):
    return bin(x).count('1')


def lam_margin(V, r):
    Q = V @ V.conj().T
    w, U = np.linalg.eigh(H1(Q) + sf(Q))
    return float(w[0] - (2 * r - 5)), U[:, 0]


def descend_projector(V, r, iters=400, eta=0.05):
    best, wmin = lam_margin(V, r)
    for _ in range(iters):
        W = np.outer(wmin, wmin.conj())
        Gm = H1(W) + sf(W)
        Vn, _ = np.linalg.qr(V - eta * (Gm @ V))
        val, wn = lam_margin(Vn, r)
        if val < best - 1e-15:
            V, best, wmin = Vn, val, wn
            eta *= 1.15
        else:
            eta *= 0.5
            if eta < 1e-10:
                break
    return best, V


def structured_starts(r, n_each):
    """Starts near the tight configurations: |0000>, weight-1 and low-weight states,
    with |0000>-|1111> mixing (S>10 region), plus noise of several sizes."""
    starts = []
    low = sorted(range(D), key=lambda x: (wt(x), x))
    for _ in range(n_each):
        for eps in (0.0, 0.02, 0.1, 0.3):
            cols = []
            th = rng.uniform(0, np.pi / 2)
            ph = rng.uniform(0, 2 * np.pi)
            cols.append(np.cos(th) * ket(0) + np.exp(1j * ph) * np.sin(th) * ket(15))
            pool = [x for x in low if x not in (0, 15)]
            rng.shuffle(pool[4:])
            for x in pool[: r - 1]:
                cols.append(ket(x))
            M = np.array(cols).T
            M = M + eps * (rng.standard_normal(M.shape) + 1j * rng.standard_normal(M.shape))
            V, _ = np.linalg.qr(M)
            starts.append(V)
    return starts


def projector_stats(V, r):
    """Frame-correct diagnostics of a projector: rotate every site so its marginal is
    (r/2) I + (m_i/2) Z with m_i >= 0, then read S = sum m_i, c = (S-10)/2 and
    q = <0000|Q'|0000> in that rotated frame (the quantity used by the lemma)."""
    Q = V @ V.conj().T
    Us, ms = [], []
    for i in range(NQ):
        R = Q.reshape([2] * (2 * NQ))
        for j in sorted([j for j in range(NQ) if j != i], reverse=True):
            R = np.trace(R, axis1=j, axis2=R.ndim // 2 + j)
        M = R.reshape(2, 2)
        vec = np.array([np.trace(M @ P).real for P in (X2, Y2, Z2)])
        Mv = vec[0] * X2 + vec[1] * Y2 + vec[2] * Z2
        w, E = np.linalg.eigh(Mv)  # ascending: E[:,1] has eigenvalue +|m|
        Ui = np.array([E[:, 1], E[:, 0]]).conj()  # rows: U M U^dag = diag(+|m|, -|m|)
        Us.append(Ui)
        ms.append(float(np.linalg.norm(vec)))
    U = reduce(np.kron, Us)
    Qr = U @ Q @ U.conj().T
    S = float(sum(ms))
    c = (S - 10) / 2
    q = float(Qr[0, 0].real)
    # verify rotated marginals are Z-diagonal with +m_i
    ok = True
    for i in range(NQ):
        R = Qr.reshape([2] * (2 * NQ))
        for j in sorted([j for j in range(NQ) if j != i], reverse=True):
            R = np.trace(R, axis1=j, axis2=R.ndim // 2 + j)
        M = R.reshape(2, 2)
        ok &= bool(np.allclose(M, (r / 2) * I2 + (ms[i] / 2) * Z2, atol=1e-9))
    d = np.real(np.diag(H1(Qr))) - (2 * r - 5)
    return {'m': ms, 'S': S, 'c': c, 'q_rotated_frame': q, 'rotated_marginals_are_(r/2)I+(m/2)Z': ok,
            'occupancy_q_minus_(S-8)/4': q - (S - 8) / 4,
            'H1Q_minus_(2r-5)_at_1111_rotated': float(d[15]), 'minus_c': -c,
            'min_other_diag_rotated': float(d[:15].min()),
            'two_by_two_det_c(2q-1-c)': c * (2 * q - 1 - c)}


def search_dual_lemma(ranks, n_haar, n_struct, iters):
    res = {}
    for r in ranks:
        t0 = time.time()
        best = (np.inf, None)
        worst_start = np.inf
        n = 0
        for V in [random_iso(r) for _ in range(n_haar)] + structured_starts(r, n_struct):
            n += 1
            v0, _ = lam_margin(V, r)
            worst_start = min(worst_start, v0)
            val, Vb = descend_projector(V, r, iters=iters)
            if val < best[0]:
                best = (val, Vb)
        st = projector_stats(best[1], r)
        res[str(r)] = {'rank': r, 'threshold': 2 * r - 5, 'starts': n, 'min_margin_before_descent': float(worst_start),
                       'min_margin_after_descent': float(best[0]), 'minimiser_stats': st,
                       'seconds': round(time.time() - t0, 1)}
        print(f'rank {r}: starts={n} min margin before={worst_start:.3e} after descent={best[0]:.3e} '
              f'(S={st["S"]:.6f}, c={st["c"]:.6f}, q_rot={st["q_rotated_frame"]:.6f}, q-(S-8)/4={st["occupancy_q_minus_(S-8)/4"]:.2e}) [{res[str(r)]["seconds"]}s]')
    return res


def bottom_margin(psi, r, p):
    rho = np.outer(psi, psi.conj())
    w = np.linalg.eigvalsh(channel(rho, p))
    return float(w[:r].sum() - ref_bottom(r, p))


def descend_state(psi, r, p, iters=300, eta=0.1):
    best = bottom_margin(psi, r, p)
    for _ in range(iters):
        rho = np.outer(psi, psi.conj())
        w, U = np.linalg.eigh(channel(rho, p))
        Qb = U[:, :r] @ U[:, :r].conj().T
        grad = channel(Qb, p) @ psi  # Phi is self-dual; d(bottom_r)/d rho = Phi(Q_bottom)
        pn = psi - eta * grad
        pn = pn / np.linalg.norm(pn)
        val = bottom_margin(pn, r, p)
        if val < best - 1e-15:
            psi, best = pn, val
            eta *= 1.15
        else:
            eta *= 0.5
            if eta < 1e-10:
                break
    return best, psi


def search_output_comparison(ranks, ps, n_starts, iters):
    res = {}
    for r in ranks:
        for p in ps:
            best = np.inf
            worst0 = np.inf
            for s in range(n_starts):
                if s % 3 == 0:
                    psi = rng.standard_normal(D) + 1j * rng.standard_normal(D)
                elif s % 3 == 1:  # near-product start
                    psi = ket(0) + 0.3 * (rng.standard_normal(D) + 1j * rng.standard_normal(D))
                else:  # GHZ-like / symmetric start
                    psi = ket(0) + np.exp(1j * rng.uniform(0, 2 * np.pi)) * ket(15) + 0.2 * (rng.standard_normal(D) + 1j * rng.standard_normal(D))
                psi = psi / np.linalg.norm(psi)
                worst0 = min(worst0, bottom_margin(psi, r, p))
                val, _ = descend_state(psi, r, p, iters=iters)
                best = min(best, val)
            res[f'r{r}_k{D - r}_p{p:.4f}'] = {'rank_r': r, 'index_k': D - r, 'p': p, 'starts': n_starts,
                                               'min_margin_before': float(worst0), 'min_margin_after_descent': float(best)}
            print(f'r={r} (k={D - r}) p={p:.4f}: min margin after descent {best:.3e}')
    return res


def random_pairs(ranks, n):
    res = {}
    for r in ranks:
        mh1, mh2 = np.inf, np.inf
        for _ in range(n):
            V = random_iso(r)
            Q = V @ V.conj().T
            psi = rng.standard_normal(D) + 1j * rng.standard_normal(D)
            psi /= np.linalg.norm(psi)
            rho = np.outer(psi, psi.conj())
            mh1 = min(mh1, float(np.trace(Q @ H1(rho)).real) - (2 * r - 6))
            mh2 = min(mh2, float(np.trace(Q @ H2(rho)).real) - (r - 5))
        res[str(r)] = {'samples': n, 'min_trQH1_minus_(2r-6)': mh1, 'min_trQH2_minus_(r-5)': mh2}
        print(f'rank {r}: random pairs min TrQH1-(2r-6)={mh1:.3e}  min TrQH2-(r-5)={mh2:.3e}')
    return res


def self_checks():
    X = rng.standard_normal((D, D)) + 1j * rng.standard_normal((D, D))
    X = X + X.conj().T
    ok = all(np.allclose(erase_pt(X, i), erase_tw(X, i)) for i in range(NQ))
    # identity H2 - H1 + Tr(X) I = X + sf(X) + F(X)/2
    F = sum(PAULIS[(i, a)] @ X @ PAULIS[(i, a)] for i in range(NQ) for a in (1, 2, 3))
    ok &= np.allclose(H2(X) - H1(X) + np.trace(X) * np.eye(D), X + sf(X) + 0.5 * F)
    # self-adjointness
    Y = rng.standard_normal((D, D)) + 1j * rng.standard_normal((D, D))
    Y = Y + Y.conj().T
    ok &= np.isclose(np.trace(X @ H1(Y)), np.trace(H1(X) @ Y)) and np.isclose(np.trace(X @ sf(Y)), np.trace(sf(X) @ Y))
    # mirror
    psi = rng.standard_normal(D) + 1j * rng.standard_normal(D)
    rho = np.outer(psi, psi.conj()) / np.vdot(psi, psi).real
    ok &= np.allclose(sf(channel(rho, 1.25)), channel(rho, 0.75))
    return bool(ok)


def main():
    t0 = utc()
    print('self-checks:', self_checks())
    ranks_claimed = [5, 6, 10, 11]
    ranks_info = [7, 8, 9]
    out = {'scope': 'floating-point adversarial search on sampled/descended instances; evidence, not proof',
           'receipts': {'clock_start_utc': t0, 'numpy': np.__version__, 'python': sys.version.split()[0], 'seed': SEED,
                        'script_sha256': sha256_file(os.path.abspath(__file__))}}
    print('--- dual lemma search, claimed ranks')
    out['dual_lemma_claimed_ranks'] = search_dual_lemma(ranks_claimed, n_haar=400, n_struct=30, iters=400)
    print('--- dual lemma search, ranks 7,8,9 (informational; not claimed by the packets)')
    out['dual_lemma_ranks_7_8_9_informational'] = search_dual_lemma(ranks_info, n_haar=200, n_struct=15, iters=400)
    # negative control: false threshold at rank 6
    m6 = out['dual_lemma_claimed_ranks']['6']['min_margin_after_descent']
    out['negative_control_false_threshold_7.05_rank6'] = {'min_lam_minus_7.05': m6 - 0.05, 'violation_found': bool(m6 - 0.05 < 0)}
    print('negative control (rank 6 vs 7.05): violation found =', out['negative_control_false_threshold_7.05_rank6']['violation_found'])
    print('--- output comparison search (pure states)')
    ps = [0.05, 0.2, 0.4, 0.6, 0.8, 0.95, 1.0, 1.1, 1.25, 4 / 3]
    out['output_comparison'] = search_output_comparison(ranks_claimed, ps, n_starts=24, iters=250)
    print('--- random pairs')
    out['random_pairs'] = random_pairs(ranks_claimed, 2000)
    out['summary'] = {
        'min_dual_margin_claimed_ranks': min(v['min_margin_after_descent'] for v in out['dual_lemma_claimed_ranks'].values()),
        'min_dual_margin_ranks_7_8_9': min(v['min_margin_after_descent'] for v in out['dual_lemma_ranks_7_8_9_informational'].values()),
        'min_output_margin_claimed': min(v['min_margin_after_descent'] for v in out['output_comparison'].values()),
        'min_random_pair_H2_margin': min(v['min_trQH2_minus_(r-5)'] for v in out['random_pairs'].values()),
        'min_random_pair_H1_margin': min(v['min_trQH1_minus_(2r-6)'] for v in out['random_pairs'].values()),
    }
    out['receipts']['clock_end_utc'] = utc()
    with open(os.path.join(HERE, 'reviewer-adversarial-search-v2.result.json'), 'w') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(json.dumps({'summary': out['summary'], 'receipts': out['receipts']}, indent=1, sort_keys=True))


if __name__ == '__main__':
    main()
