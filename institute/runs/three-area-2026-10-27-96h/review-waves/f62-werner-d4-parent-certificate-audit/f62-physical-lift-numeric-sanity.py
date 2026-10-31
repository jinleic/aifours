#!/usr/bin/env python3
"""f62 reviewer: numeric end-to-end sanity check (float64, NOT a proof) of the physical rank<=2 lift used by
the d=4 certificate bridge: for random complex C on (C^4)^{x3} of rank 1 and 2 (non-normal, non-Hermitian),
scaled to ||C||_HS^2 = 1/2, build A (isometry with ran C inside ran A, via QR with completion), B = 2 C^dag A,
a = vec(A)/sqrt2, b = vec(B)/sqrt2, and verify: ||a||=||b||=1, Tr_H |a><a| = I_2/2, C_xy = sum_r a_xr conj(b_yr),
||Tr_S C||_HS^2 = <a x b| F_Q F_S |a x b> for all eight S (unnormalized partial traces), and
q3(C) = sum_S (-1/2)^|S| ||Tr_S C||^2 = <a x b| F_Q prod_i (I - F_i/2) |a x b|>. Writes only here."""
import itertools, json, time
from pathlib import Path
import numpy as np
OUT = Path(__file__).resolve().parent / 'f62-physical-lift-numeric-sanity-results.json'
rng = np.random.default_rng(20261028)
D = 64


def partial_trace_norm2(C, S):
    T = C.reshape(4, 4, 4, 4, 4, 4)   # (x1,x2,x3,y1,y2,y3)
    for i in sorted(S, reverse=True):
        T = np.trace(T, axis1=i, axis2=i + T.ndim // 2)
    return float(np.sum(np.abs(T) ** 2))


def q3(C):
    return sum((-0.5) ** len(S) * partial_trace_norm2(C, S) for k in range(4) for S in itertools.combinations(range(3), k))


def swap_form(a, b, S, with_Q=True):
    """<a x b| F_Q F_S |a x b> with a,b in H x Q as tensors (4,4,4,2)."""
    ab = np.multiply.outer(a, b)           # axes (x1,x2,x3,r, y1,y2,y3,s)
    perm = list(range(8))
    for i in S: perm[i], perm[4 + i] = perm[4 + i], perm[i]
    if with_Q: perm[3], perm[7] = perm[7], perm[3]
    return complex(np.vdot(ab, ab.transpose(perm)))


def lift(C):
    U, s, Vh = np.linalg.svd(C)
    rank = int(np.sum(s > 1e-10 * s.max()))
    A = U[:, :2]                            # isometric completion for rank 1 comes from the SVD's second left vector
    B = 2 * C.conj().T @ A
    a = (A / np.sqrt(2)).reshape(4, 4, 4, 2)
    b = (B / np.sqrt(2)).reshape(4, 4, 4, 2)
    return rank, A, B, a, b


def main():
    t0 = time.monotonic(); trials = []
    for trial in range(8):
        r = 1 if trial % 3 == 2 else 2
        X = rng.normal(size=(D, r)) + 1j * rng.normal(size=(D, r)); Y = rng.normal(size=(D, r)) + 1j * rng.normal(size=(D, r))
        C = X @ Y.conj().T
        C *= np.sqrt(0.5 / np.sum(np.abs(C) ** 2))
        rank, A, B, a, b = lift(C)
        av, bv = a.reshape(D, 2), b.reshape(D, 2)
        errs = {
            'rank': rank,
            'isometry': float(np.abs(A.conj().T @ A - np.eye(2)).max()),
            'reconstruction_C=AB^dag/2': float(np.abs(A @ B.conj().T / 2 - C).max()),
            'reconstruction_C_xy=sum_r a conj(b)': float(np.abs(av @ bv.conj().T - C).max()),
            'norm_a_minus_1': float(abs(np.vdot(av, av).real - 1)), 'norm_b_minus_1': float(abs(np.vdot(bv, bv).real - 1)),
            'Tr_H|a><a|-I/2': float(np.abs(av.T @ av.conj() - np.eye(2) / 2).max()),
            'nonnormal_commutator_norm': float(np.abs(C @ C.conj().T - C.conj().T @ C).max()),
        }
        worst = 0.0
        for k in range(4):
            for S in itertools.combinations(range(3), k):
                lhs = partial_trace_norm2(C, S); rhs = swap_form(a, b, S)
                worst = max(worst, abs(lhs - rhs.real), abs(rhs.imag))
        errs['max_|Tr_S|^2_vs_swap_form_over_8_subsets'] = worst
        q = q3(C)
        # prod_i (I - F_i/2) expanded: sum_S (-1/2)^|S| F_S
        z = sum((-0.5) ** len(S) * swap_form(a, b, S) for k in range(4) for S in itertools.combinations(range(3), k))
        errs['q3_definition'] = q; errs['q3_swap_operator_form'] = z.real; errs['q3_abs_difference'] = abs(q - z)
        errs['q3_nonnegative_in_sample'] = bool(q >= -1e-12)
        trials.append(errs)
    tol = 1e-9
    ok = all(max(v for k, v in t.items() if isinstance(v, float) and k not in ('q3_definition', 'q3_swap_operator_form', 'nonnormal_commutator_norm')) < tol for t in trials)
    res = {'kind': 'f62_physical_lift_numeric_sanity', 'tolerance': tol, 'trials': trials, 'elapsed_seconds': round(time.monotonic() - t0, 3),
           'scope': 'float64 sampled sanity of the lift/swap-trace bridge on random complex rank-1/rank-2 non-normal C; not a proof and not evidence for q3>=0 beyond the sampled points.',
           'verdict': 'PASS' if ok else 'FAIL'}
    OUT.write_text(json.dumps(res, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: v for k, v in res.items() if k != 'trials'}, indent=2))
    for t in trials: print({k: (round(v, 14) if isinstance(v, float) else v) for k, v in t.items()})
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
