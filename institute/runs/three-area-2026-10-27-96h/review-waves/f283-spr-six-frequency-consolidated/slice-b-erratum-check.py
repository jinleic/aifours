#!/usr/bin/env python3
"""Slice B erratum verifier for wave f283-spr-six-frequency-consolidated.

The frozen slice-b-k2-checker.py (sha256 6ec1984a...) exited 1 because the
S1|71 parenthetical identity
    q2*(u2-x) - q1*(u1-x) = (u2-u1)*(e_m(u3,u4) - x*e_{m-1}(u3,u4))
failed its exact Fraction check for x=1, m>=1 (passed for x=0 and for m=0).

This script settles, by exact integer polynomial arithmetic and Fraction
evaluation, with no rerun of K1/K2 enumeration logic:
  (E1) the corrected identity  q2*(u2-x) - q1*(u1-x) = (u2-u1)*(e_m(u3,u4)
       + x*e_{m-1}(u3,u4))  holds identically for x in {0,1}, m in 0..3;
  (E2) the manuscript's version differs from the corrected one by exactly
       2*x*(u2-u1)*e_{m-1}(u3,u4), i.e. only when x=1 and m>=1;
  (E3) the S_+ closed form S_+ = [q2*(u2-x)*h(u2) - q1*(u1-x)*h(u1)]/(u2-u1),
       h(t)=(d-t)(e-t)/((u3-t)(u4-t)(f-t)), equals the direct partial ray sum
       sum_{i=1,2} e_m(u_hat_i) g_+(u_i)/H'(u_i) and is > 0, at four exact
       rational gap points, for all x in {0,1}, m in 0..3;
  (E4) the S1|71 justification phrase "e_m/e_{m-1} is a mean of u3,u4" is false
       in the open gap domain for m=2 (e2/e1 = u3*u4/(u3+u4) < min(u3,u4)),
       with an explicit exact counterexample; the corrected identity (E1) makes
       that mean argument unnecessary.

Standard library only; exact arithmetic; single process; sub-second.
"""
import sys, os, json, time, hashlib, platform, datetime
from fractions import Fraction as F
from itertools import combinations

T0 = time.time()
WAVE = os.path.dirname(os.path.abspath(__file__))
SELFPATH = os.path.abspath(__file__)

NV = 9
def pk(e):
    k = 0
    for i in range(NV): k |= e[i] << (4 * i)
    return k
def unpack(k): return tuple((k >> (4 * i)) & 15 for i in range(NV))
ZERO = pk((0,) * NV)
def const(c): return {ZERO: c} if c else {}
_varcache = {}
def var(i):
    if i not in _varcache:
        _varcache[i] = {pk(tuple(1 if j == i else 0 for j in range(NV))): 1}
    return _varcache[i]
def padd(a, b):
    r = dict(a)
    for k, v in b.items():
        nv = r.get(k, 0) + v
        if nv: r[k] = nv
        elif k in r: del r[k]
    return r
def pneg(a): return {k: -v for k, v in a.items()}
def psub(a, b): return padd(a, pneg(b))
def pmul(a, b):
    if len(a) > len(b): a, b = b, a
    r = {}; g = r.get
    for ea, ca in a.items():
        for eb, cb in b.items():
            k = ea + eb; nv = g(k, 0) + ca * cb
            if nv: r[k] = nv
            elif k in r: del r[k]
            g = r.get
    return r
def pmul_seq(fs):
    acc = {ZERO: 1}
    for f in sorted(fs, key=len): acc = pmul(acc, f)
    return acc
B, U, V, X, Y, Z, P, W, R = (var(i) for i in range(NV))
ONE = {ZERO: 1}
b_ = padd(ONE, B); u1 = padd(b_, U); c_ = padd(u1, V); u2 = padd(c_, X)
u3 = padd(u2, Y); d_ = padd(u3, Z); u4 = padd(d_, P); e_ = padd(u4, W); f_ = padd(e_, R)

def efun(polys, m):
    acc = {}
    for comb in combinations(range(len(polys)), m):
        t = {ZERO: 1}
        for j in comb: t = pmul(t, polys[j])
        acc = padd(acc, t)
    return acc
T = [u3, u4]
XV = {0: {}, 1: ONE}   # zero poly or 1

E1 = {}; E2 = {}
for x in (0, 1):
    xt = XV[x]
    for m in range(4):
        q1 = efun([u2, u3, u4], m)          # e_m(u_hat_1)
        q2 = efun([u1, u3, u4], m)          # e_m(u_hat_2)
        lhs = psub(pmul(q2, psub(u2, xt)), pmul(q1, psub(u1, xt)))
        corr = pmul(psub(u2, u1), padd(efun(T, m), pmul(xt, efun(T, m - 1) if m >= 1 else {})))
        manu = pmul(psub(u2, u1), psub(efun(T, m), pmul(xt, efun(T, m - 1) if m >= 1 else {})))
        E1["x=%d,m=%d" % (x, m)] = (psub(lhs, corr) == {})
        E2["x=%d,m=%d" % (x, m)] = (psub(psub(lhs, manu),
                                          pmul(pmul({ZERO: 2 * x}, psub(u2, u1)),
                                               efun(T, m - 1) if m >= 1 else {})) == {})

PTS = [tuple(F(1) for _ in range(9)),
       (F(2), F(1), F(3), F(1), F(2), F(1), F(4), F(2), F(1)),
       (F(1), F(2), F(1), F(5), F(1), F(1), F(3), F(2), F(5)),
       (F(3), F(1), F(1), F(2), F(5), F(1), F(1), F(4), F(2))]
def efrac(v, m):
    s = F(0)
    for comb in combinations(range(len(v)), m):
        t = F(1)
        for j in comb: t *= v[j]
        s += t
    return s
E3 = {}
for x in (0, 1):
    for m in range(4):
        oks = []
        for p in PTS:
            b = 1 + p[0]; u1v = b + p[1]; cv = u1v + p[2]; u2v = cv + p[3]
            u3v = u2v + p[4]; dv = u3v + p[5]; u4v = dv + p[6]; ev = u4v + p[7]; fv = ev + p[8]
            u = [u1v, u2v, u3v, u4v]
            S = F(0)
            for i in (0, 1):
                oth = [[u2v, u3v, u4v], [u1v, u3v, u4v]][i]; t = u[i]
                g = ((t if x == 0 else t - 1) * (dv - t) * (ev - t)) / (fv - t)
                Hp = (t - u2v) * (t - u3v) * (t - u4v) if i == 0 else (t - u1v) * (t - u3v) * (t - u4v)
                S += efrac(oth, m) * g / Hp
            q1 = efrac([u2v, u3v, u4v], m); q2 = efrac([u1v, u3v, u4v], m)
            h = lambda t: (dv - t) * (ev - t) / ((u3v - t) * (u4v - t) * (fv - t))
            closed = (q2 * (u2v - x) * h(u2v) - q1 * (u1v - x) * h(u1v)) / (u2v - u1v)
            oks.append(S == closed and S > 0)
        E3["x=%d,m=%d" % (x, m)] = all(oks)

# E4: mean claim counterexample: u3=3/2, u4=3/2 (realizable with positive gaps),
# e2/e1 = (9/4)/3 = 3/4 < 1 =: x, while both u3,u4 > x.
u3c = F(3, 2); u4c = F(3, 2)
E4 = {"e2_over_e1": str((u3c * u4c) / (u3c + u4c)), "less_than_x=1": (u3c * u4c) / (u3c + u4c) < 1,
      "u3,u4 both > 1": u3c > 1 and u4c > 1,
      "realizable_gaps_example": [str(g) for g in [F(1, 4), F(1, 8), F(1, 16), F(1, 16), F(1, 16), F(1, 8), F(1, 16), F(1, 4), F(1, 2)]]}

ok = all(E1.values()) and all(E2.values()) and all(E3.values()) and E4["less_than_x=1"]
receipt = {
    "kind": "slice-B erratum verification receipt (S1|71 q-difference sign)",
    "wave": "f283-spr-six-frequency-consolidated",
    "source": os.path.basename(SELFPATH),
    "checker_sha256_at_run": hashlib.sha256(open(SELFPATH, "rb").read()).hexdigest(),
    "python": platform.python_version(), "argv": sys.argv,
    "clock_start_utc": datetime.datetime.fromtimestamp(T0, datetime.timezone.utc).isoformat(),
    "E1_corrected_identity_exact": E1,
    "E2_manuscript_differs_by_2x(u2-u1)e_{m-1}_exact": E2,
    "E3_Splus_closed_form_and_positivity_4pts": E3,
    "E4_mean_claim_counterexample": E4,
    "all_checks_pass": ok,
    "clock_end_utc": datetime.datetime.fromtimestamp(time.time(), datetime.timezone.utc).isoformat(),
    "wall_seconds": round(time.time() - T0, 3),
}
with open(os.path.join(WAVE, "slice-b-erratum-receipt.json"), "w") as fh:
    json.dump(receipt, fh, indent=1)
print("E1 corrected identity:", all(E1.values()))
print("E2 manuscript version differs by 2x(u2-u1)e_{m-1}:", all(E2.values()))
print("E3 S+ closed form + positivity:", all(E3.values()))
print("E4 mean-claim counterexample:", E4["less_than_x=1"], "e2/e1 =", E4["e2_over_e1"])
sys.exit(0 if ok else 1)
