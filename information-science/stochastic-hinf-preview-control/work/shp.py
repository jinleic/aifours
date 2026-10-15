"""Stochastic H-infinity preview control (book problem: 随机系统 H∞ 预演控制).

Continuous-time model (book eq. (1)), with v(t) := w(t-h) the disturbance acting at time t:
    dx = (A x + B u + C v) dt + (A0 x + B0 u) dW,   z = D0 x + D1 u,
w adapted, w = 0 on [a-h, a), x(a) = 0, performance  E∫_a^b |z|^2  vs  gamma^2 E∫_a^{b-h} |w|^2.

Two independent computations live here:

1. `solve_grde`: the n x n "advanced" generalized Riccati differential equation of work/theory.md,
       -dP/dt = A'P + PA + A0'PA0 + D0'D0 - L' Rh^{-1} L + gamma^{-2} k k',   P(b) = PT,
       k(t)   = [P(t), -I] Phi0(t, t+h) [C; 0]   (k = 0 when t + h > b),
   where Phi0 is the transition matrix of the predicted Hamiltonian H0(P(s)) on the preview window.
2. `disc_game` / `disc_closed_loop_gain`: an Euler discretisation with the previewed disturbances
   stored in a shift register (augmented state of dimension n + N m), solved by the textbook
   discrete-time min-max dynamic programme with its stage-wise concavity test.  It shares only the
   plant data with (1).
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import expm


class Plant:
    def __init__(self, A, B, C, A0, B0, D0, D1):
        self.A = np.atleast_2d(np.asarray(A, float))
        self.B = np.atleast_2d(np.asarray(B, float))
        self.C = np.atleast_2d(np.asarray(C, float))
        self.A0 = np.atleast_2d(np.asarray(A0, float))
        self.B0 = np.atleast_2d(np.asarray(B0, float))
        self.D0 = np.atleast_2d(np.asarray(D0, float))
        self.D1 = np.atleast_2d(np.asarray(D1, float))
        self.n = self.A.shape[0]
        self.nu = self.B.shape[1]
        self.m = self.C.shape[1]
        assert self.B.shape == (self.n, self.nu) and self.B0.shape == (self.n, self.nu)
        assert self.A0.shape == (self.n, self.n) and self.C.shape[0] == self.n
        assert self.D0.shape[1] == self.n and self.D1.shape == (self.D0.shape[0], self.nu)
        assert np.linalg.eigvalsh(self.D1.T @ self.D1).min() > 0, "need D1'D1 > 0"

    # ----- blocks that depend on P ---------------------------------------------------------
    def blocks(self, P):
        A, B, A0, B0, D0, D1 = self.A, self.B, self.A0, self.B0, self.D0, self.D1
        Rh = D1.T @ D1 + B0.T @ P @ B0
        S = B0.T @ P @ A0 + D1.T @ D0
        Ri = np.linalg.inv(Rh)
        L = B.T @ P + S
        At = A - B @ Ri @ S
        Qt = A0.T @ P @ A0 + D0.T @ D0 - S.T @ Ri @ S
        H0 = np.block([[At, -B @ Ri @ B.T], [-Qt, -At.T]])
        return Rh, S, L, Ri, H0

    def rhs(self, P, k, gam):
        """Right-hand side F with -dP/dt = F(P, k)."""
        A, A0, D0 = self.A, self.A0, self.D0
        Rh, S, L, Ri, _ = self.blocks(P)
        F = A.T @ P + P @ A + A0.T @ P @ A0 + D0.T @ D0 - L.T @ Ri @ L + (k @ k.T) / gam**2
        return 0.5 * (F + F.T)


def _grid(T, dt, h):
    N = int(round(T / dt))
    Nw = int(round(h / dt))
    assert abs(N * dt - T) < 1e-9 * max(1, T) and abs(Nw * dt - h) < 1e-9 * max(1, h), "grid mismatch"
    return N, Nw


def solve_grde(plant: Plant, gam, h, T, dt, PT=None, store=False, blowup=1e9):
    """Backward Heun integration of the advanced GRDE on [0, T].

    Returns dict(ok, t_escape, P (N+1,n,n), G (if store): window columns Gamma(t_i, t_i + j dt)
    = Phi0(t_i, t_i + j dt)[C;0] for j = 0..Nw, shape (N+1, Nw+1, 2n, m)).
    """
    n, m = plant.n, plant.m
    N, Nw = _grid(T, dt, h)
    e0 = np.vstack([plant.C, np.zeros((n, m))])
    P = np.zeros((N + 1, n, n))
    P[N] = np.zeros((n, n)) if PT is None else np.asarray(PT, float)
    G = np.zeros((Nw + 1, 2 * n, m))
    G[0] = e0  # columns j >= 1 refer to s > T and stay 0
    Gs = np.zeros((N + 1, Nw + 1, 2 * n, m)) if store else None
    if store:
        Gs[N] = G
    I = np.eye(n)

    def kvec(Pm, Gm):
        return np.hstack([Pm, -I]) @ Gm[Nw]

    for i in range(N - 1, -1, -1):
        P1 = P[i + 1]
        f1 = plant.rhs(P1, kvec(P1, G), gam)
        Pp = P1 + dt * f1
        Gn = np.empty_like(G)
        Gn[0] = e0
        E = expm(-plant.blocks(0.5 * (P1 + Pp))[4] * dt)
        Gn[1:] = np.einsum("ab,jbc->jac", E, G[:-1])
        f2 = plant.rhs(Pp, kvec(Pp, Gn), gam)
        Pi = P1 + 0.5 * dt * (f1 + f2)
        # one more corrector sweep with the improved endpoint
        E = expm(-plant.blocks(0.5 * (P1 + Pi))[4] * dt)
        Gn[1:] = np.einsum("ab,jbc->jac", E, G[:-1])
        f2 = plant.rhs(Pi, kvec(Pi, Gn), gam)
        Pi = P1 + 0.5 * dt * (f1 + f2)
        Pi = 0.5 * (Pi + Pi.T)
        if not np.all(np.isfinite(Pi)) or np.abs(Pi).max() > blowup:
            return dict(ok=False, t_escape=i * dt, P=P, G=Gs, N=N, Nw=Nw)
        P[i] = Pi
        G = Gn
        if store:
            Gs[i] = G
    return dict(ok=True, t_escape=None, P=P, G=Gs, N=N, Nw=Nw)


def standard_grde(plant: Plant, gam, T, dt, PT=None, blowup=1e9):
    """h = 0 reference: the classical stochastic H-infinity full-information GRDE
    -dP/dt = A'P+PA+A0'PA0+D0'D0-L'Rh^{-1}L+gamma^{-2} P C C' P (RK4, independent code path)."""
    n = plant.n
    N = int(round(T / dt))
    P = np.zeros((n, n)) if PT is None else np.asarray(PT, float)

    def F(P):
        return plant.rhs(P, P @ plant.C, gam)

    for i in range(N):
        k1 = F(P)
        k2 = F(P + 0.5 * dt * k1)
        k3 = F(P + 0.5 * dt * k2)
        k4 = F(P + dt * k3)
        P = P + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if not np.all(np.isfinite(P)) or np.abs(P).max() > blowup:
            return False, P
    return True, P


def bisect_gamma(test, lo, hi, tol=1e-6, maxit=80):
    """Smallest gamma with test(gamma) True, assuming monotonicity; test(lo) False, test(hi) True."""
    assert not test(lo) and test(hi), "bad bracket"
    it = 0
    while hi - lo > tol * hi and it < maxit:
        mid = 0.5 * (lo + hi)
        if test(mid):
            hi = mid
        else:
            lo = mid
        it += 1
    return lo, hi


# ----------------------------------------------------------------------------------------------
# Independent discrete-time check: Euler discretisation + shift-register augmentation.
# ----------------------------------------------------------------------------------------------
def _disc_mats(plant: Plant, dt, Nw):
    n, m, nu = plant.n, plant.m, plant.nu
    Dy = n + (Nw + 1) * m  # Y_k = [x_k; v_k; ...; v_{k+Nw}]  (v_{k+Nw} = w_k)
    D = n + Nw * m  # X_{k+1} = [x_{k+1}; v_{k+1}; ...; v_{k+Nw}]
    Ad = np.eye(n) + plant.A * dt
    F = np.zeros((D, Dy))
    F[:n, :n] = Ad
    F[:n, n:n + m] = plant.C * dt  # v_k acts on the plant now
    if Nw > 0:
        F[n:, n + m:] = np.eye(Nw * m)  # register shift; w_k becomes v_{k+Nw}
    G = np.zeros((D, nu))
    G[:n] = plant.B * dt
    Ex = np.zeros((n, Dy))
    Ex[:, :n] = np.eye(n)
    return Dy, D, F, G, Ex


def disc_game(plant: Plant, gam, h, T, dt, PT=None, return_all=False):
    """Discrete min-max DP (adversary picks w_k first, controller sees it).

    Returns (ok, k_fail, info).  ok == all stage-wise concavity tests passed.
    """
    n, m, nu = plant.n, plant.m, plant.nu
    N, Nw = _grid(T, dt, h)
    Dy, D, F, G, Ex = _disc_mats(plant, dt, Nw)
    D0, D1, A0, B0 = plant.D0, plant.D1, plant.A0, plant.B0
    Pi = np.zeros((D, D))
    if PT is not None:
        Pi[:n, :n] = PT
    Zx = D0 @ Ex  # z = Zx Y + D1 u
    Nx = A0 @ Ex  # noise coefficient (A0 x + B0 u) sqrt(dt)
    margins = []
    for k in range(N - 1, -1, -1):
        Pxx = Pi[:n, :n]
        MYY = dt * Zx.T @ Zx + F.T @ Pi @ F + dt * Nx.T @ Pxx @ Nx
        MYu = dt * Zx.T @ D1 + F.T @ Pi @ G + dt * Nx.T @ Pxx @ B0
        Muu = dt * D1.T @ D1 + G.T @ Pi @ G + dt * B0.T @ Pxx @ B0
        counted = k <= N - Nw - 1
        if counted:
            MYY = MYY.copy()
            MYY[-m:, -m:] -= dt * gam**2 * np.eye(m)
        Nmat = MYY - MYu @ np.linalg.solve(Muu, MYu.T)
        Nmat = 0.5 * (Nmat + Nmat.T)
        NXX, NXw, Nww = Nmat[:-m, :-m], Nmat[:-m, -m:], Nmat[-m:, -m:]
        if counted:
            ev = np.linalg.eigvalsh(Nww).max()
            margins.append(-ev / dt)
            if ev >= 0:
                return False, k, dict(margin=min(margins))
            Pi = NXX - NXw @ np.linalg.solve(Nww, NXw.T)
        else:
            Pi = NXX
        Pi = 0.5 * (Pi + Pi.T)
    return True, None, dict(margin=min(margins) if margins else np.inf, Pi0=Pi)


def continuous_controller_gains(plant: Plant, sol, dt):
    """Discretised version of u*(t) = -Rh^{-1}(L x + B' ∫ K(t,s) v(s) ds), K(t,s) = [P,-I]Gamma(t,s).

    Returns U (N, nu, Dy): u_k = U[k] @ Y_k with Y_k = [x_k; v_k; ...; v_{k+Nw}] (trapezoid rule)."""
    n, m, nu = plant.n, plant.m, plant.nu
    N, Nw = sol["N"], sol["Nw"]
    Dy = n + (Nw + 1) * m
    w = np.full(Nw + 1, dt)
    if Nw > 0:
        w[0] = w[-1] = dt / 2
    U = np.zeros((N, nu, Dy))
    I = np.eye(n)
    for k in range(N):
        P = sol["P"][k]
        _, _, L, Ri, _ = plant.blocks(P)
        U[k, :, :n] = -Ri @ L
        if Nw == 0:
            continue  # with h = 0 the integral term vanishes (point mass of zero length)
        Kmat = np.einsum("ab,jbc->jac", np.hstack([P, -I]), sol["G"][k])  # (Nw+1, n, m)
        for j in range(Nw + 1):
            U[k, :, n + j * m:n + (j + 1) * m] = -Ri @ plant.B.T @ Kmat[j] * w[j]
    return U


def disc_closed_loop_gain(plant: Plant, U, gam, h, T, dt, PT=None, return_policy=False):
    """Max-only DP for the discrete closed loop u_k = U[k] Y_k: concavity at every stage
    <=> the closed loop has discrete L2 gain (mean-square) < gam from zero state."""
    n, m = plant.n, plant.m
    N, Nw = _grid(T, dt, h)
    Dy, D, F, G, Ex = _disc_mats(plant, dt, Nw)
    D0, D1, A0, B0 = plant.D0, plant.D1, plant.A0, plant.B0
    Pi = np.zeros((D, D))
    if PT is not None:
        Pi[:n, :n] = PT
    policy = [None] * N
    for k in range(N - 1, -1, -1):
        Uk = U[k]
        Zc = D0 @ Ex + D1 @ Uk
        Fc = F + G @ Uk
        Nc = A0 @ Ex + B0 @ Uk
        Pxx = Pi[:n, :n]
        Nmat = dt * Zc.T @ Zc + Fc.T @ Pi @ Fc + dt * Nc.T @ Pxx @ Nc
        counted = k <= N - Nw - 1
        if counted:
            Nmat[-m:, -m:] -= dt * gam**2 * np.eye(m)
        Nmat = 0.5 * (Nmat + Nmat.T)
        NXX, NXw, Nww = Nmat[:-m, :-m], Nmat[:-m, -m:], Nmat[-m:, -m:]
        if counted:
            evs, vecs = np.linalg.eigh(Nww)
            if evs.max() >= 0:
                return (False, k, dict(direction=vecs[:, -1], policy=policy)) if return_policy else (False, k, None)
            Kw = -np.linalg.solve(Nww, NXw.T)  # w_k = Kw X_k maximises
            policy[k] = Kw
            Pi = NXX + NXw @ Kw
        else:
            policy[k] = np.zeros((m, D))
            Pi = NXX
        Pi = 0.5 * (Pi + Pi.T)
    return (True, None, dict(policy=policy, Pi0=Pi)) if return_policy else (True, None, None)


def simulate(plant: Plant, U, h, T, dt, w_fn, n_paths, rng, PT=None):
    """Euler-Maruyama Monte Carlo of the discrete closed loop. w_fn(k, X, rng_noise_state) -> (n_paths, m).
    Returns per-path z-energy, w-energy (both with the dt weights)."""
    n, m = plant.n, plant.m
    N, Nw = _grid(T, dt, h)
    Dy, D, F, G, Ex = _disc_mats(plant, dt, Nw)
    X = np.zeros((n_paths, D))
    Ez = np.zeros(n_paths)
    Ew = np.zeros(n_paths)
    for k in range(N):
        w = w_fn(k, X) if k <= N - Nw - 1 else np.zeros((n_paths, m))
        Y = np.hstack([X, w])
        u = Y @ U[k].T
        x = X[:, :n]
        z = x @ plant.D0.T + u @ plant.D1.T
        Ez += dt * np.sum(z * z, axis=1)
        Ew += dt * np.sum(w * w, axis=1)
        noise = (x @ plant.A0.T + u @ plant.B0.T) * (np.sqrt(dt) * rng.standard_normal((n_paths, 1)))
        X = Y @ F.T + u @ G.T
        X[:, :n] += noise
    if PT is not None:
        xN = X[:, :n]
        Ez += np.einsum("pi,ij,pj->p", xN, PT, xN)
    return Ez, Ew


# ----------------------------------------------------------------------------------------------
# Infinite horizon (time-invariant data)
# ----------------------------------------------------------------------------------------------
def stationary_k(plant: Plant, P, h):
    """k = [P, -I] expm(-H0(P) h) [C; 0]."""
    n = plant.n
    H0 = plant.blocks(P)[4]
    e0 = np.vstack([plant.C, np.zeros((n, plant.m))])
    return np.hstack([P, -np.eye(n)]) @ expm(-H0 * h) @ e0


def gare_residual(plant: Plant, P, gam, h):
    return plant.rhs(P, stationary_k(plant, P, h), gam)


def limit_solution(plant: Plant, gam, h, dt, T_max=200.0, chunk=10.0, tol=1e-10, blowup=1e9):
    """P_inf = lim_{T->oo} P_T(0): integrate the time-invariant advanced GRDE in time-to-go until
    stationary.  Returns (ok, P, info)."""
    n, m = plant.n, plant.m
    Nw = int(round(h / dt))
    e0 = np.vstack([plant.C, np.zeros((n, m))])
    P = np.zeros((n, n))
    G = np.zeros((Nw + 1, 2 * n, m))
    G[0] = e0
    I = np.eye(n)
    steps = int(round(T_max / dt))
    hist = []

    def kvec(Pm, Gm):
        return np.hstack([Pm, -I]) @ Gm[Nw]

    for i in range(steps):
        f1 = plant.rhs(P, kvec(P, G), gam)
        Pp = P + dt * f1
        Gn = np.empty_like(G)
        Gn[0] = e0
        E = expm(-plant.blocks(0.5 * (P + Pp))[4] * dt)
        Gn[1:] = np.einsum("ab,jbc->jac", E, G[:-1])
        f2 = plant.rhs(Pp, kvec(Pp, Gn), gam)
        Pn = P + 0.5 * dt * (f1 + f2)
        E = expm(-plant.blocks(0.5 * (P + Pn))[4] * dt)
        Gn[1:] = np.einsum("ab,jbc->jac", E, G[:-1])
        f2 = plant.rhs(Pn, kvec(Pn, Gn), gam)
        Pn = P + 0.5 * dt * (f1 + f2)
        Pn = 0.5 * (Pn + Pn.T)
        if not np.all(np.isfinite(Pn)) or np.abs(Pn).max() > blowup:
            return False, Pn, dict(T_escape=(i + 1) * dt)
        dP = np.abs(Pn - P).max() / dt
        P, G = Pn, Gn
        if (i + 1) * dt > max(5 * h, 5.0) and dP < tol:
            return True, P, dict(T_used=(i + 1) * dt, dPdt=dP)
    return False, P, dict(T_used=T_max, dPdt=dP, note="not converged")


def stabilizing_tests(plant: Plant, P, gam, h, nquad=400):
    """(T1) A_P = A_c + gam^-2 phi22' C k' Hurwitz;  (T2) spectral radius of the renewal map
    T(Sig) = int_0^oo Gs Psi(t) Sig Psi(t)' Gs' dt  < 1, Psi(t) = e^{H0 t}[I;P] (t<=h),
    e^{H0 h}[I;P] e^{A_P (t-h)} (t>h), Gs = [A0 - B0 Rh^-1 S, -B0 Rh^-1 B'].
    Also internal stability (A+BF, A0+B0F) and the GARE residual."""
    n = plant.n
    Rh, S, L, Ri, H0 = plant.blocks(P)
    k = stationary_k(plant, P, h)
    Phi = expm(H0 * h)
    phi22 = Phi[n:, n:]
    F = -Ri @ L
    Ac = plant.A + plant.B @ F
    AP = Ac + phi22.T @ plant.C @ k.T / gam**2
    # check A_P is the restriction of H_eff = e^{-H0 h} H_gam e^{H0 h} to graph(P)
    Hg = H0.copy()
    Hg[:n, n:] += plant.C @ plant.C.T / gam**2
    Heff = np.linalg.solve(Phi, Hg @ Phi)
    IP = np.vstack([np.eye(n), P])
    inv_res = np.abs(Heff @ IP - IP @ (Heff[:n, :] @ IP)).max()
    AP_from_Heff = Heff[:n, :] @ IP
    Gs = np.hstack([plant.A0 - plant.B0 @ Ri @ S, -plant.B0 @ Ri @ plant.B.T])
    eigAP = np.linalg.eigvals(AP)
    # internal stability operator  X -> Acl'X + X Acl + A0cl' X A0cl  (vectorised)
    A0cl = plant.A0 + plant.B0 @ F
    In = np.eye(n)
    Lint = np.kron(In, Ac.T) + np.kron(Ac.T, In) + np.kron(A0cl.T, A0cl.T)
    int_stab = np.linalg.eigvals(Lint).real.max()
    rho = np.inf
    if eigAP.real.max() < 0:
        # vec(M Sig M') = (M kron M) vec(Sig)
        ts = np.linspace(0, h, nquad + 1) if h > 0 else np.array([0.0])
        Tm = np.zeros((n * n, n * n))
        if h > 0:
            wq = np.full(nquad + 1, h / nquad)
            wq[0] = wq[-1] = h / (2 * nquad)
            for t, wt in zip(ts, wq):
                Mt = Gs @ expm(H0 * t) @ IP
                Tm += wt * np.kron(Mt, Mt)
        Nm = Gs @ Phi @ IP
        Kint = -np.linalg.inv(np.kron(In, AP) + np.kron(AP, In))  # int_0^oo e^{AP t} kron e^{AP t}
        Tm += np.kron(Nm, Nm) @ Kint
        rho = np.abs(np.linalg.eigvals(Tm)).max()
    return dict(residual=float(np.abs(gare_residual(plant, P, gam, h)).max()),
                AP_eigs=eigAP.tolist(), AP_max_real=float(eigAP.real.max()),
                AP_vs_Heff=float(np.abs(AP - AP_from_Heff).max()), Heff_invariance_residual=float(inv_res),
                rho_T=float(rho), internal_stab_max_real=float(int_stab), P=P.tolist(), k=k.tolist())
