#!/usr/bin/env python3
"""Exact second-order test of the two-copy d=4 dual inequality at a cross-sector equality point.

f(X) = sigma1(X)^2 + sigma2(X)^2 - ||X||^2/2 on W_odd = {S(x)I + I(x)R : S, R traceless 4x4}.
At X0 = |0><1|(x)I + I(x)|0><1| we have f(X0)=0; the top-2 eigenvalue 2 of X0^dag X0 is double and
isolated (next eigenvalue 1), so f is real-analytic near X0 and its second-order coefficient is
  c2(Y) = Tr(Pi Y^dag Y) + Tr(Pi H1 P1 H1) + (1/2) Tr(Pi H1 P0 H1) - ||Y||^2/2,
  H1 = X0^dag Y + Y^dag X0,
with Pi, P1, P0 the spectral projectors of X0^dag X0 for eigenvalues 2, 1, 0.  This is computed as
an exact rational quadratic form on the 60 real coordinates of (S, R), and its inertia is found by
exact symmetric elimination.  Arithmetic: Gaussian rationals from fractions.Fraction; no floats.
Authorized by Main as part of an exact counterexample search; no held input.
"""
from fractions import Fraction as Fr
from pathlib import Path
import hashlib
import json

D = 4
N = 16


def idx(a, b):
    return 4 * a + b


def zeros():
    return [[(Fr(0), Fr(0)) for _ in range(N)] for _ in range(N)]


def cmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def cadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def conj(x):
    return (x[0], -x[1])


def kron_left(S):
    """S (x) I."""
    M = zeros()
    for a in range(D):
        for b in range(D):
            if S[a][b] != (0, 0):
                for k in range(D):
                    M[idx(a, k)][idx(b, k)] = S[a][b]
    return M


def kron_right(R):
    """I (x) R."""
    M = zeros()
    for a in range(D):
        for b in range(D):
            if R[a][b] != (0, 0):
                for k in range(D):
                    M[idx(k, a)][idx(k, b)] = R[a][b]
    return M


def madd(A, B):
    return [[cadd(x, y) for x, y in zip(ra, rb)] for ra, rb in zip(A, B)]


def dag(A):
    return [[conj(A[j][i]) for j in range(N)] for i in range(N)]


def mvec(A, v):
    out = []
    for i in range(N):
        s = (Fr(0), Fr(0))
        for j in range(N):
            if v[j] != (0, 0) and A[i][j] != (0, 0):
                s = cadd(s, cmul(A[i][j], v[j]))
        out.append(s)
    return out


def inner(u, v):
    s = (Fr(0), Fr(0))
    for a, b in zip(u, v):
        s = cadd(s, cmul(conj(a), b))
    return s


def unit(i):
    v = [(Fr(0), Fr(0))] * N
    v = list(v)
    v[i] = (Fr(1), Fr(0))
    return v


def small(entries):
    M = [[(Fr(0), Fr(0)) for _ in range(D)] for _ in range(D)]
    for (a, b), val in entries.items():
        M[a][b] = val
    return M


E01 = small({(0, 1): (Fr(1), Fr(0))})
X0 = madd(kron_left(E01), kron_right(E01))
X0d = dag(X0)

# Spectral data of X0^dag X0 (verified below): eigenvalue 2 on |11>, (|10>+|01>)/sqrt2;
# eigenvalue 1 on |12>,|13>,|21>,|31>; eigenvalue 0 on the rest.
top_vectors = []  # (unnormalized vector, weight = 1/||v||^2)
v11 = unit(idx(1, 1))
w = [cadd(a, b) for a, b in zip(unit(idx(1, 0)), unit(idx(0, 1)))]
top_vectors.append((v11, Fr(1)))
top_vectors.append((w, Fr(1, 2)))
ones = [unit(idx(1, 2)), unit(idx(1, 3)), unit(idx(2, 1)), unit(idx(3, 1))]


def apply_G(u):
    """G = P1 + (1/2) P0, with P0 = I - Pi - P1."""
    # component along top space
    top = [(Fr(0), Fr(0))] * N
    top = list(top)
    for v, wt in top_vectors:
        c = inner(v, u)
        for i in range(N):
            top[i] = cadd(top[i], cmul((c[0] * wt, c[1] * wt), v[i]))
    p1 = [(Fr(0), Fr(0))] * N
    p1 = list(p1)
    for v in ones:
        c = inner(v, u)
        for i in range(N):
            p1[i] = cadd(p1[i], cmul(c, v[i]))
    # G u = P1 u + 1/2 (u - top - P1 u)
    return [(p1[i][0] + (u[i][0] - top[i][0] - p1[i][0]) / 2, p1[i][1] + (u[i][1] - top[i][1] - p1[i][1]) / 2) for i in range(N)]


def check_spectrum():
    H0 = [[(Fr(0), Fr(0)) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        col = mvec(X0d, mvec(X0, unit(i)))
        for j in range(N):
            H0[j][i] = col[j]
    ok = True
    for v, _ in top_vectors:
        ok &= mvec(H0, v) == [(2 * a[0], 2 * a[1]) for a in v]
    for v in ones:
        ok &= mvec(H0, v) == v
    # the remaining 10-dimensional complement must be annihilated: check H0 G' = 0 on P0 range by trace count
    tr = sum(H0[i][i][0] for i in range(N))
    ok &= tr == 2 + 2 + 4  # 2*2 + 1*4 + 0*10
    return ok


def c2(S, R):
    Y = madd(kron_left(S), kron_right(R))
    Yd = dag(Y)
    total = Fr(0)
    for v, wt in top_vectors:
        Yv = mvec(Y, v)
        total += wt * inner(Yv, Yv)[0]
        H1v = [cadd(a, b) for a, b in zip(mvec(X0d, Yv), mvec(Yd, mvec(X0, v)))]
        total += wt * inner(H1v, apply_G(H1v))[0]
    normY = sum(x[0] * x[0] + x[1] * x[1] for row in Y for x in row)
    return total - normY / 2


# real basis of sl_4 (15 complex dims -> 30 real): off-diagonal E_ab and i E_ab; diagonal E_00-E_kk and i(E_00-E_kk)
def sl4_basis():
    basis = []
    for a in range(D):
        for b in range(D):
            if a != b:
                basis.append(small({(a, b): (Fr(1), Fr(0))}))
                basis.append(small({(a, b): (Fr(0), Fr(1))}))
    for k in range(1, D):
        basis.append(small({(0, 0): (Fr(1), Fr(0)), (k, k): (Fr(-1), Fr(0))}))
        basis.append(small({(0, 0): (Fr(0), Fr(1)), (k, k): (Fr(0), Fr(-1))}))
    return basis


ZERO4 = small({})
sl = sl4_basis()
directions = [(B, ZERO4) for B in sl] + [(ZERO4, B) for B in sl]


def mat_add4(A, B):
    return [[cadd(x, y) for x, y in zip(ra, rb)] for ra, rb in zip(A, B)]


def build_form():
    n = len(directions)
    diag = [c2(*d) for d in directions]
    M = [[Fr(0)] * n for _ in range(n)]
    for i in range(n):
        M[i][i] = diag[i]
        for j in range(i + 1, n):
            Si = mat_add4(directions[i][0], directions[j][0])
            Ri = mat_add4(directions[i][1], directions[j][1])
            val = (c2(Si, Ri) - diag[i] - diag[j]) / 2
            M[i][j] = M[j][i] = val
    return M


def inertia(M):
    """Exact inertia of a real symmetric matrix by symmetric elimination with 1x1/2x2 pivots."""
    A = [row[:] for row in M]
    n = len(A)
    alive = list(range(n))
    pos = neg = 0
    while alive:
        piv = next((i for i in alive if A[i][i] != 0), None)
        if piv is not None:
            p = A[piv][piv]
            if p > 0:
                pos += 1
            else:
                neg += 1
            rest = [i for i in alive if i != piv]
            for i in rest:
                if A[i][piv] != 0:
                    f = A[i][piv] / p
                    for j in rest:
                        A[i][j] -= f * A[piv][j]
            alive = rest
            continue
        pair = next(((i, j) for i in alive for j in alive if i < j and A[i][j] != 0), None)
        if pair is None:
            break  # remaining block is zero
        i, j = pair
        # zero diagonal, nonzero off-diagonal 2x2 pivot has eigenvalues of both signs
        pos += 1
        neg += 1
        rest = [k for k in alive if k not in (i, j)]
        b = A[i][j]
        for k in rest:
            for l in rest:
                # Schur complement for pivot [[0,b],[b,0]]: inverse [[0,1/b],[1/b,0]]
                A[k][l] -= (A[k][i] * A[j][l] + A[k][j] * A[i][l]) / b
        alive = rest
    zero = n - pos - neg
    return pos, neg, zero


spectrum_ok = check_spectrum()
M = build_form()
pos, neg, zero = inertia(M)
null_checks = {
    'c2_along_X0_is_0': c2(E01, E01) == 0,
    'c2_along_iX0_is_0': c2(small({(0, 1): (Fr(0), Fr(1))}), small({(0, 1): (Fr(0), Fr(1))})) == 0,
    'c2_along_unitary_tangent_site1_is_0': c2(small({(2, 1): (Fr(0), Fr(1))}), ZERO4) == 0,
}


def make_G(c1, c0):
    def G(u):
        top = [(Fr(0), Fr(0))] * N
        for v, wt in top_vectors:
            c = inner(v, u)
            for i in range(N):
                top[i] = cadd(top[i], cmul((c[0] * wt, c[1] * wt), v[i]))
        p1 = [(Fr(0), Fr(0))] * N
        for v in ones:
            c = inner(v, u)
            for i in range(N):
                p1[i] = cadd(p1[i], cmul(c, v[i]))
        return [(c1 * p1[i][0] + c0 * (u[i][0] - top[i][0] - p1[i][0]), c1 * p1[i][1] + c0 * (u[i][1] - top[i][1] - p1[i][1])) for i in range(N)]
    return G


correct_G = apply_G
faults = {}
for label, c1, c0 in (('denominator_for_eigenvalue0_set_to_1', Fr(1), Fr(1)), ('both_denominators_halved', Fr(2), Fr(1))):
    apply_G = make_G(c1, c0)
    fp, fn, fz = inertia(build_form())
    faults[label] = {'positive': fp, 'negative': fn, 'zero': fz, 'detected_as_indefinite': fp > 0}
apply_G = correct_G
status_ok = spectrum_ok and all(null_checks.values()) and all(f['detected_as_indefinite'] for f in faults.values())
record = {
    'status': 'PASS' if status_ok else 'FAIL',
    'null_direction_checks': null_checks,
    'fault_controls_overestimating_second_order_term': faults,
    'equality_point': 'X0 = |0><1|(x)I + I(x)|0><1| (dual side), sigma1^2+sigma2^2 = 4 = ||X0||^2/2',
    'spectrum_check': spectrum_ok,
    'real_dimension': len(directions),
    'second_order_form_inertia': {'positive': pos, 'negative': neg, 'zero': zero},
    'verdict': ('NEGATIVE SEMIDEFINITE: X0 is a second-order local maximum of f; no counterexample along any second-order direction'
                if pos == 0 else 'INDEFINITE: a direction with f>0 to second order exists (candidate counterexample)'),
    'arithmetic': 'fractions.Fraction Gaussian rationals; exact symmetric elimination; no floats',
    'scope': 'Second-order necessary-condition test at one equality point only; not a proof of T2 or of local maximality beyond second order along the null directions.',
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
out = Path(__file__).resolve().parent / 'frontier-20261029-t2-cross-sector-hessian-exact-check-results-v1.json'
out.write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
print(json.dumps(record, sort_keys=True))
