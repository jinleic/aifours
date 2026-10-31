#!/usr/bin/env python3
"""Independent exact arithmetic checks for f64; no author code or floating point.

The unbounded root-count and privacy arguments are in review-v1.md; this file
checks polynomial identities, bounded rational instances, and fault controls.
Run once in this directory: python3 -B checker-v1.py.  Receipt is exclusive-create.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "checker-receipt-v1.json"
if RECEIPT.exists():
    raise SystemExit("Refusing to overwrite existing receipt")

# A sparse polynomial in two independent indeterminates (g,m).
def clean(p):
    return {k: F(v) for k, v in p.items() if v}

def c(v):
    return clean({(0, 0): v})

def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return clean(out)

def scale(p, t):
    return clean({k: t * v for k, v in p.items()})

def sub(p, q):
    return add(p, scale(q, -1))

def mul(p, q):
    out = {}
    for (i, j), a in p.items():
        for (k, ell), b in q.items():
            key = (i + k, j + ell)
            out[key] = out.get(key, F(0)) + a * b
    return clean(out)

def power(p, n):
    out = c(1)
    for _ in range(n):
        out = mul(out, p)
    return out

def dg(p):
    return clean({(i - 1, j): i * a for (i, j), a in p.items() if i})

def evaluate(p, g, m):
    return sum((a * g ** i * m ** j for (i, j), a in p.items()), F(0))

def replace_g(p, expr):
    return add(*(scale(mul(power(expr, i), power(M, j)), a)
                 for (i, j), a in p.items()))

def stirling2(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    return stirling2(n - 1, k - 1) + k * stirling2(n - 1, k)

def geom_moment(n):
    # K~Geom(success=1-b) on {0,1,...}; E[(K)_j]=j!m^j.
    terms = []
    for j in range(n + 1):
        for k in range(j + 1):
            coeff = comb(n, j) * stirling2(j, k) * factorial(k)
            terms.append(scale(mul(power(G, n - j), power(M, k)), coeff))
    return add(*terms)

G = {(1, 0): F(1)}
M = {(0, 1): F(1)}
O = c(1)
T = add(O, scale(M, 2))
V = mul(M, add(O, M))
checks = []
controls = []

def require(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

def reject(name, condition, intended_reason):
    if condition:
        raise AssertionError("Mutation not detected: " + name)
    controls.append({"mutation": name, "rejected": True, "reason": intended_reason})

D, U, H = (geom_moment(n) for n in (2, 3, 4))
D_claim = add(power(G, 2), scale(mul(M, G), 2), M, scale(power(M, 2), 2))
U_claim = add(power(G, 3), scale(mul(M, power(G, 2)), 3),
              scale(mul(add(M, scale(power(M, 2), 2)), G), 3),
              M, scale(power(M, 2), 6), scale(power(M, 3), 6))
H_claim = add(power(G, 4), scale(mul(M, power(G, 3)), 4),
              scale(mul(add(M, scale(power(M, 2), 2)), power(G, 2)), 6),
              scale(mul(add(M, scale(power(M, 2), 6), scale(power(M, 3), 6)), G), 4),
              M, scale(power(M, 2), 14), scale(power(M, 3), 36), scale(power(M, 4), 24))
require("geometric factorial moments D, M3, M4", (D, U, H) == (D_claim, U_claim, H_claim))
reject("normalizer omits 2m^2", D == sub(D_claim, scale(power(M, 2), 2)),
       "the geometric second moment contains E[K(K-1)]=2m^2")
reject("fourth layer moment omits 6m^2", H == sub(H_claim, scale(power(M, 2), 6)),
       "the fourth raw geometric moment has 14m^2")

Q = add(power(G, 4), scale(mul(M, power(G, 3)), 4),
        scale(mul(power(M, 2), power(G, 2)), 6),
        scale(mul(mul(M, add(O, scale(M, 3))), G), -2), power(M, 2))
P = add(power(G, 5), scale(mul(M, power(G, 4)), 5),
        mul(add(scale(M, 2), scale(power(M, 2), 12)), power(G, 3)),
        mul(add(scale(power(M, 3), 12), scale(M, -2)), power(G, 2)),
        scale(mul(mul(mul(M, add(O, scale(M, 2))), add(O, scale(M, 6))), G), -1),
        mul(power(M, 2), add(O, scale(M, 2))))
R = add(scale(power(G, 3), 2), scale(mul(M, power(G, 2)), 6),
        scale(mul(add(O, scale(M, 6)), G), -1), M)
require("L derivative numerator", sub(mul(dg(U), D), mul(U, dg(D))) == Q)
require("W derivative numerator", sub(mul(dg(H), D), mul(H, dg(D))) == scale(P, 2))
reject("quartic derivative has extra g^2", sub(mul(dg(U), D), mul(U, dg(D))) == add(Q, power(G, 2)),
       "quotient-rule numerator differs by g^2")
require("P=(g+m)Q+vR", P == add(mul(add(G, M), Q), mul(V, R)))
# Substitute g=x-m; G now denotes x in the two right-hand sides.
require("shifted quartic", replace_g(Q, sub(G, M)) == add(power(G, 4), scale(mul(mul(V, T), G), -2), scale(power(V, 2), 3)))
require("shifted cubic", replace_g(R, sub(G, M)) == add(scale(power(G, 3), 2), scale(mul(add(O, scale(V, 6)), G), -1), scale(mul(V, T), 2)))
require("t^2=4v+1", power(T, 2) == add(scale(V, 4), O))
# G stands for z. This is the denominator-cleared strict-factor identity.
left = sub(sub(power(add(power(G, 2), c(3)), 2), scale(G, 16)),
           scale(power(sub(G, O), 2), 12))
factor = mul(power(sub(G, O), 3), add(G, c(3)))
require("strict z-factor polynomial", left == factor)
reject("strict factor uses (z-1)^2", left == mul(power(sub(G, O), 2), add(G, c(3))),
       "the denominator-cleared polynomial has a triple, not double, zero at z=1")
# An independent rational negative Q witness, g=m/(1+2m), for every m>0.
pivot_cleared = add(*(scale(mul(mul(power(M, i + j), power(T, 4 - i)), O), a)
                      for (i, j), a in Q.items()))
require("all-m rational quartic negative pivot", pivot_cleared == scale(mul(power(V, 2), add(scale(V, 8), O)), -1))
require("quartic endpoint polynomials", replace_g(Q, c(0)) == power(M, 2) and replace_g(Q, c(1)) == power(add(O, M), 2))
require("quintic endpoint polynomials", replace_g(P, c(0)) == mul(power(M, 2), T) and replace_g(P, c(1)) == mul(power(add(O, M), 2), T))
require("endpoint normalizer scaling", mul(replace_g(D, c(0)), add(O, M)) == mul(M, replace_g(D, c(1))))
# P' termwise bound, using |12m^3-2m| <= 12m^3+2m.
B = add(c(5), scale(M, 31), scale(power(M, 2), 44), scale(power(M, 3), 36))
bound_terms = add(c(5), scale(M, 20), scale(add(scale(M, 2), scale(power(M, 2), 12)), 3),
                  scale(add(scale(power(M, 3), 12), scale(M, 2)), 2),
                  mul(mul(M, add(O, scale(M, 2))), add(O, scale(M, 6))))
require("global |P'| bound", B == bound_terms)
require("diamond angular integral", F(1, 3) + F(1, 3) == F(2, 3))
reject("Euclidean-to-l1-square factor 1/2", F(1, 2) == F(2, 3),
       "integral_0^1 (s^2+(1-s)^2) ds is 2/3")

# Exact interval isolation; proofs of all-m root counts do not depend on this sample.
def bisect(poly, m, lo, hi, steps=90):
    flo, fhi = evaluate(poly, lo, m), evaluate(poly, hi, m)
    if flo * fhi >= 0:
        raise AssertionError("invalid root bracket")
    for _ in range(steps):
        mid = (lo + hi) / 2
        fm = evaluate(poly, mid, m)
        if fm == 0:
            return mid, mid
        if flo * fm < 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return lo, hi

def frac(v):
    return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"

def W(g, m):
    return evaluate(H, g, m) / (2 * evaluate(D, g, m))

samples = []
for m in (F(1, 10000), F(1, 10), F(1), F(10), F(1000)):
    pivot = m / (1 + 2 * m)
    require(f"Q pivot negative m={m}", evaluate(Q, pivot, m) < 0)
    qlo, qhi = bisect(Q, m, pivot, F(1))
    bnd = evaluate(B, F(0), m)
    p_lower = -evaluate(P, qhi, m) - bnd * (qhi - qlo)
    require(f"P(mean) certified negative m={m}", p_lower > 0)
    plo, phi = bisect(P, m, qhi, F(1))
    require(f"root separation exact intervals m={m}", qhi < plo)
    half_step = min((1 - qhi) / 2, p_lower / (4 * bnd))
    comp = qhi + half_step
    require(f"rational comparator decreases W m={m}", W(qhi, m) > W(comp, m))
    h_lower = min((1 - qhi) / 2, p_lower / (2 * bnd))
    dmax = (1 + m) * (1 + 2 * m)
    gap_lower = p_lower * h_lower / (3 * dmax ** 2)
    require(f"certified positive explicit J gap m={m}", gap_lower > 0)
    samples.append({"m": frac(m), "mean_root_interval": [frac(qlo), frac(qhi)],
                    "square_root_interval": [frac(plo), frac(phi)],
                    "p0_lower": frac(p_lower), "J_gap_lower": frac(gap_lower),
                    "rational_comparator": frac(comp),
                    "W_drop_from_mean_upper": frac(W(qhi, m) - W(comp, m))})

# Finite controls of layer boundaries and endpoints, not a substitute for all shifts.
def ceil_frac(x):
    return -((-x.numerator) // x.denominator)

def layer(r, gam):
    return max(0, ceil_frac(r - gam))

radii = {F(j, 8) for j in range(33)}
for gam in (F(0), F(1, 4), F(1, 2), F(1)):
    rs = set(radii)
    for j in range(4):
        threshold = gam + j
        rs.update(r for r in (threshold - F(1, 1000), threshold, threshold + F(1, 1000)) if r >= 0)
    require(f"closed-boundary layers gamma={gam}", all(abs(layer(r, gam) - layer(s, gam)) <= 1 for r in rs for s in rs if abs(r - s) <= 1))
require("endpoint laws have identical nonzero-radius weights", all(layer(r, F(0)) == layer(r, F(1)) + 1 for r in radii if r > 0))
require("endpoint origin is a null exception", layer(F(0), F(0)) == layer(F(0), F(1)) == 0)

# Actual Borel events A={||x||_1<=1/8}, gamma=1/2, beta=1/2.
# h=(1,0) has layer 1 throughout A+h, h=(7/4,0) has layer 2.
beta = F(1, 2)
require("closed unit shift event saturates privacy", F(1) == beta / beta)
reject("privacy extended to shift 7/4", F(1) <= beta ** 2 / beta,
       "A is entirely layer 0 while A+(7/4,0) is entirely layer 2")

root = Path("/Users/jinleic/repos/aifours")
inputs = [
    (root / "institute/runs/three-area-2026-10-23-96h/privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md", "75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3"),
    (root / "information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-universal-pmlr-selector-separation-v1.md", "4c92d56867a959298836063d0045634cd61a0efb8f3175fcb701c4ac4a722fc6"),
    (root / "institute/runs/three-area-2026-10-27-96h/public-sources/kulesza-suresh-wang-pmlr258-2025.pdf", "4e67a46d80e705df6b23a92e8fb88599a8b14c874af3f7b434a0ed217ca71df3"),
]
pins = []
for path, expected in inputs:
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise AssertionError(f"input hash mismatch: {path}")
    pins.append({"path": str(path), "sha256": actual})
clock = subprocess.check_output(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z %Z"], text=True).strip()
receipt = {"kind": "INDEPENDENT_EXACT_CHECK_RECEIPT", "observed_clock_before_creation": clock,
           "python": sys.version.split()[0], "checker": str(Path(__file__).resolve()),
           "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "input_pins": pins, "exact_checks_passed": checks, "intended_reason_controls": controls,
           "fraction_sample_certificates": samples,
           "prior_execution": "First run stopped at the first rational comparator with TypeError: W() missing m; no receipt was created. Both omitted arguments were fixed before this complete rerun.",
           "limits": "Finite controls and symbolic algebra only; not an all-law theorem, formal proof, human or independent-family certification."}
with RECEIPT.open("x", encoding="utf-8") as f:
    json.dump(receipt, f, indent=2, sort_keys=True)
    f.write("\n")
print(f"PASS: {len(checks)} exact checks, {len(controls)} intended-reason controls, {len(samples)} rational parameter certificates")
print(f"Receipt creation clock: {clock}")
print(f"Receipt: {RECEIPT}")
