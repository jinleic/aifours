#!/usr/bin/env python3
"""fco_candidate_verify_v1: standard-library EXACT verifier for a single FCO(n) square (lane note
evidence/fourier-co-ansatz-v1.md): q_ij(t) = zeta^(t j + pi(t) rho(i)) / sqrt n, zeta = exp(2 pi i / n), classes
{(i, j): j - i = s mod n}. Written as a second code path for any (pi, rho) reported by code/fourier_co_enum_v1.py; it
shares no function with that probe. Same author: NOT an independent checker in the contract's sense.

Arithmetic: elements of Z[zeta_n] as integer coefficient lists, products by convolution modulo x^n - 1, zero test by
exact reduction modulo the cyclotomic polynomial Phi_n (obtained here by exact division of x^n - 1 by Phi_d, d | n,
d < n). Vectors are kept unscaled (entries zeta^e, squared norm n).
Checks:
  O  for each of the 3n lines (rows, columns, classes) and each pair of distinct cells in the line, the inner product
     sum_t conj(zeta^e(t)) zeta^e'(t) is computed as a ring element and tested for zero; diagonal entries equal n.
  P  for ALL pairs of distinct cells, s = <q, q'> (unscaled) and N = s * conj(s) are computed exactly; the two cells
     hold the same projective ray iff N = n^2 (Cauchy-Schwarz equality; exact test N - n^2 = 0 in Z[zeta_n]).
  L  B Latin; pi, rho permutations.
Usage: fco_candidate_verify_v1.py IN.json OUT.json   (IN: {"n": n, "pi": [...], "rho": [...]}, or a fourier_co_enum
       output whose "stop" payload holds n, pi, rho). Output: exclusive create. No GO protocol (single small check).
"""
import hashlib, json, sys, time

T0 = time.monotonic()
IN, OUT = sys.argv[1], sys.argv[2]


def poly_div_exact(a, b):
    a = list(a)
    q = [0] * (len(a) - len(b) + 1)
    for i in range(len(a) - len(b), -1, -1):
        c = a[i + len(b) - 1] // b[-1]
        q[i] = c
        for j, bj in enumerate(b):
            a[i + j] -= c * bj
    if any(a):
        raise ValueError("inexact division")
    return q


MEMO = {}


def phi(n):
    if n not in MEMO:
        p = [-1] + [0] * (n - 1) + [1]
        for d in range(1, n):
            if n % d == 0:
                p = poly_div_exact(p, phi(d))
        MEMO[n] = p
    return MEMO[n]


def is_zero(v, n):
    r = list(v)
    f = phi(n)
    k = len(f) - 1
    for i in range(len(r) - 1, k - 1, -1):
        c = r[i]
        if c:
            for j in range(k + 1):
                r[i - k + j] -= c * f[j]
    return all(x == 0 for x in r[:k])


def mono(e, n):
    v = [0] * n
    v[e % n] = 1
    return v


def add(u, w):
    return [x + y for x, y in zip(u, w)]


def mul(u, w, n):
    r = [0] * n
    for i, x in enumerate(u):
        if x:
            for j, y in enumerate(w):
                if y:
                    r[(i + j) % n] += x * y
    return r


def conj(u, n):
    return [u[(-k) % n] for k in range(n)]


def inner(x, y, n):
    s = [0] * n
    for a, b in zip(x, y):
        s = add(s, mul(conj(a, n), b, n))
    return s


with open(IN, "rb") as fh:
    raw = fh.read()
src = json.loads(raw.decode("utf-8"))
if "pi" not in src and "stop" in src:
    src = src["stop"]["payload"]
n, pi, rho = int(src["n"]), [int(x) for x in src["pi"]], [int(x) for x in src["rho"]]
res = {"verifier": "fco_candidate_verify_v1", "input": {"path": IN, "sha256": hashlib.sha256(raw).hexdigest()},
       "n": n, "pi": pi, "rho": rho}
res["L_permutations"] = sorted(pi) == list(range(n)) and sorted(rho) == list(range(n))
Q = {(i, j): [mono(t * j + pi[t] * rho[i], n) for t in range(n)] for i in range(n) for j in range(n)}
fams = {"rows": [[(i, j) for j in range(n)] for i in range(n)],
        "columns": [[(i, j) for i in range(n)] for j in range(n)],
        "classes": [[(i, (i + s) % n) for i in range(n)] for s in range(n)]}
O = {}
for f, lines in fams.items():
    bad, diag_bad = 0, 0
    for L in lines:
        for x in range(n):
            if not is_zero(add(inner(Q[L[x]], Q[L[x]], n), mono(0, n) and [-n] + [0] * (n - 1)), n):
                diag_bad += 1
            for y in range(x + 1, n):
                if not is_zero(inner(Q[L[x]], Q[L[y]], n), n):
                    bad += 1
    O[f] = {"offdiag_nonzero": bad, "diag_not_n": diag_bad}
res["O_gram"] = O
cells = sorted(Q)
same = 0
examples = []
nsq = [n * n] + [0] * (n - 1)
for a in range(len(cells)):
    for b in range(a + 1, len(cells)):
        s = inner(Q[cells[a]], Q[cells[b]], n)
        N = mul(s, conj(s, n), n)
        if is_zero([x - y for x, y in zip(N, nsq)], n):
            same += 1
            if len(examples) < 20:
                examples.append([list(cells[a]), list(cells[b])])
res["P_projective_coincident_pairs"] = same
res["P_examples"] = examples
res["all_rays_distinct"] = same == 0
res["is_1RQLS"] = res["L_permutations"] and all(v["offdiag_nonzero"] == 0 and v["diag_not_n"] == 0 for v in O.values())
res["elapsed_s"] = round(time.monotonic() - T0, 3)
with open(OUT, "x", encoding="utf-8") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps({k: res[k] for k in ("n", "is_1RQLS", "O_gram", "P_projective_coincident_pairs", "all_rays_distinct",
                                      "elapsed_s")}))
