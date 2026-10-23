#!/usr/bin/env python3
"""Parent spot-check of c6/proof-SEEDGstar.md Lemma LF, the (QS*) relaxation, SCW-G* case s >= 3 and Lemma QQ
(subagent SeedGReviewDesk; own code, formulas transcribed from proof-SEEDGstar.md Sec. 1-2 and proof-SEEDG-r2.md Secs. 0-2;
no lane code imported or run).  Exec with OUT set."""
import json, time
from fractions import Fraction as Fr
from math import ceil, floor
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
def classes(p):
    out = []
    for k in range(p + 1, 2 * p - 2):
        for kappa in range(max(k - p, 1), (k - 3) // 2 + 1):
            R = 2 * p - k + 2 * kappa
            if R < k or R > 2 * p - 3: continue
            for B in range(1, kappa):
                A = R - B
                if B > A or A > 2 * p - 1: continue
                out.append((k, kappa, B))
    return out
def setup(p, k, kappa, B):
    R = 2 * p - k + 2 * kappa; E = R - k; A = R - B; kB = kappa - B; D0 = 2 * p - R
    lam = lambda y, m: min(p - m + 1, y + m - kB, (y + B) // 2 + 1)
    lamc = lambda y, m: min(p - m + 1, A - kappa - y + m, (A - y) // 2 + 1)
    return R, E, A, kB, D0, lam, lamc
def LA_LB(R, E, D0, d):
    mn, mx = min(d, 0), max(d, 0); h = Fr(1, 2)
    LA = min(Fr(D0 + E + 2), D0 + h * E + 1 - mn, h * (D0 + E) + 2, D0 + h * E - mn, Fr(D0 + E - d + 1),
             h * (D0 + E - d - mn + 3), h * (D0 + E + 3) - d + h * mx, h * (R - d) + 1)
    LB = min(Fr(D0 + E + 2), D0 + h * E + mx, h * (D0 + E) + 2, D0 + h * E + mx + 1, Fr(D0 + E + d + 1),
             h * (D0 + E + mx + d + 3), h * (D0 + E + 3) + d - h * mn, h * (R + d) + 1)
    return LA, LB
def LF(E, D0, d):
    h = Fr(1, 2)
    if d >= 1: return min(h * (D0 + E - d + 3), Fr(D0 + E - d + 1)), h * (D0 + E) + 2
    if d == 0: return h * (D0 + E + 3), h * (D0 + E + 3)
    return h * (D0 + E) + 2, min(h * (D0 + E + d + 3), Fr(D0 + E + d + 1))
def weights(B, E):
    bs = min(B, E + 1)
    return list(range(-bs, 0)) + list(range(1, E + 2)) + ([0] if E >= 2 else [])
res = {'label': 'parent spot-check of SEEDGstar (subagent SeedGReviewDesk); own code', 'started': time.strftime('%Y-%m-%dT%H:%M:%S')}
# 1. Lemma LF closed forms and the relaxation, primes 5..PLF, every class and weight
PLF = 61
n = 0; lf_fail = []; minrelA = None; minrelB = None; min_int_relA = None; min_int_relB = None; at_min = {}
for p in [q for q in range(5, PLF + 1) if isprime(q)]:
    for (k, kappa, B) in classes(p):
        R, E, A, kB, D0, lam, lamc = setup(p, k, kappa, B)
        for d in weights(B, E):
            n += 1
            LA, LB = LA_LB(R, E, D0, d)
            if (LA, LB) != LF(E, D0, d) and len(lf_fail) < 10: lf_fail.append((p, k, kappa, B, d, str(LA), str(LB)))
            ra = LA - Fr(D0 - d, 2); rb = LB - Fr(D0 + d, 2)
            # integer relaxation: (QS) 1 - a <= floor((D0 - d)/2), (QS*) 1 - a <= ceil(LA); same for b + 1
            ia = ceil(LA) - floor(Fr(D0 - d, 2)); ib = ceil(LB) - floor(Fr(D0 + d, 2))
            if minrelA is None or ra < minrelA: minrelA = ra; at_min['A'] = (p, k, kappa, B, E, D0, d)
            if minrelB is None or rb < minrelB: minrelB = rb; at_min['B'] = (p, k, kappa, B, E, D0, d)
            min_int_relA = ia if min_int_relA is None else min(min_int_relA, ia)
            min_int_relB = ib if min_int_relB is None else min(min_int_relB, ib)
res['LF'] = {'primes': [5, PLF], 'class_weight_instances': n, 'closed_form_mismatches': lf_fail, 'min_real_relaxation_A': str(minrelA),
             'min_real_relaxation_B': str(minrelB), 'argmin (p,k,kappa,B,E,D0,d)': at_min, 'min_integer_relaxation_A': min_int_relA, 'min_integer_relaxation_B': min_int_relB}
# 2. SCW-G* case s >= 3: actual (A^s) and (B^s) sums >= ceil(L_A(d)), ceil(L_B(d)) on the whole (2.1) domain, primes 5..PS
PS = 17
n = 0; fails = []; tight = {'A': 0, 'B': 0}
for p in [q for q in range(5, PS + 1) if isprime(q)]:
    for (k, kappa, B) in classes(p):
        R, E, A, kB, D0, lam, lamc = setup(p, k, kappa, B)
        for d in weights(B, E):
            LA, LB = LA_LB(R, E, D0, d); cA, cB = ceil(LA), ceil(LB)
            for yp in range(-B - min(d, 0), A - max(d, 0) + 1):
                y = yp + d
                if not (-B + max(d, 0) <= y <= A + min(d, 0)): continue
                for m in range(1, k // 2 + 1):
                    for mp in (m - 1, m):
                        if mp < 1: continue
                        n += 1
                        sA = lam(yp, mp) + lamc(y, m); sB = lam(y, m) + lamc(yp, mp)
                        if sA < cA or sB < cB:
                            if len(fails) < 10: fails.append((p, k, kappa, B, d, yp, m, mp, sA, cA, sB, cB))
                        tight['A'] += sA == cA; tight['B'] += sB == cB
res['SCWGstar_s_ge_3'] = {'primes': [5, PS], 'instances': n, 'failures': fails, 'instances_attaining_ceil_A': tight['A'], 'instances_attaining_ceil_B': tight['B']}
# 3. Lemma QQ: extreme (QS) seeds (intersected with the canonical range) satisfy (P2) for every admissible pair and (PIN), primes 5..PQ
PQ = 43
n = 0; p2_fail = []; pin_fail = []; empty = 0
for p in [q for q in range(5, PQ + 1) if isprime(q)]:
    for (k, kappa, B) in classes(p):
        R, E, A, kB, D0, lam, lamc = setup(p, k, kappa, B)
        U1 = lambda d: p - lamc(d, 1)
        seeds = {}
        for d in weights(B, E):
            a = max(lam(d, 1), -((-(d - D0)) // 2) + 1); b = min(U1(d), (d + D0) // 2 - 1)
            if a > b: empty += 1; continue
            seeds[d] = (a, b)
            if b - lam(d, 1) > p - 1: pin_fail.append((p, k, kappa, B, d))
        ex = lambda d: d - 1 if d >= 1 else (-d - 1 if d <= -1 else 1)
        an = lambda d: -d if d < 0 else (1 if d == 0 else 0)          # anti letters of a run of weight d
        for d1, (a1, b1) in seeds.items():
            for d2, (a2, b2) in seeds.items():
                if ex(d1) + ex(d2) > E or an(d1) + an(d2) > B: continue
                for m in (1, 2):
                    n += 1
                    if a1 + a2 < 1 - lamc(d1 + d2, m) or b1 + b2 > p + lam(d1 + d2, m) - 1:
                        if len(p2_fail) < 10: p2_fail.append((p, k, kappa, B, d1, d2, m))
res['QQ'] = {'primes': [5, PQ], 'pair_instances': n, 'P2_failures': p2_fail, 'PIN_failures': pin_fail[:10], 'n_PIN_failures': len(pin_fail),
             'weights_without_quality_seed': empty}
res['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S')
with open(OUT, 'x') as f: json.dump(res, f, indent=1, default=str); f.write('\n')
