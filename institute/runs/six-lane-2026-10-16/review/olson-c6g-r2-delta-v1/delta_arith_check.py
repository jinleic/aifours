#!/usr/bin/env python3
"""Parent delta arithmetic for c6/proof-SEEDG-r2.md (subagent SeedGReviewDesk, own code; no lane code imported or run).
Formulas transcribed from r2 Sec. 0 (lam, lamc, U), Sec. 4 (Lemma CF, (SA), (PA)), Sec. 5 (classes, RA2, RA3) and
c6/proof-SEEDB-r3.md lines 35, 203-204 (region RB, condition (E), Claim E').  Usage: exec with OUT set to an output path."""
import json, time
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
def cdiv(a, b): return -((-a) // b)
class C:
    def __init__(s, p, k, kappa, B):
        s.p, s.k, s.kappa, s.B = p, k, kappa, B
        s.R = 2 * p - k + 2 * kappa; s.E = s.R - k; s.A = s.R - B; s.kB = kappa - B; s.D0 = 2 * p - s.R
        s.bs = min(B, s.E + 1)
    def lam(s, y, m): return min(s.p - m + 1, y + m - s.kB, (y + s.B) // 2 + 1)
    def lamc(s, y, m): return min(s.p - m + 1, s.A - s.kappa - y + m, (s.A - y) // 2 + 1)
    def U(s, y, m): return s.p - s.lamc(y, m)
    def sa(s):
        lo = max(cdiv(2 * s.kB + s.B + max(2, s.bs), 3), s.B + 2 - s.D0, 1)
        hi = min((2 * s.p - s.B - s.E - 3) // 3, s.D0 + s.B - s.bs - 2, cdiv(s.k - s.B - 3, 2))
        return lo, hi
    def pa(s):
        if not (s.D0 >= s.B + 1 and s.bs <= s.D0 + s.B - 1): return None
        lo = max(cdiv(s.kB + s.B // 2 + 1, 2), cdiv(s.kB + s.bs + (s.B - s.bs) // 2, 2), 1)
        hi = min((s.p - 1 - (s.E + s.B + 1) // 2) // 2, cdiv(s.k - 2 * s.B - 4, 3))
        return lo, hi
    def weights(s):
        ws = list(range(-s.bs, 0)) + list(range(1, s.E + 2))
        if s.E >= 2: ws.append(0)   # a (1,1)-pair carries excess 1
        return ws
def et(d): return d - 1 if d >= 1 else (-d - 1 if d <= -1 else 1)
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
def arc_check(c, fam, m, d, y):
    """four arcs of Q (fam SA: y in [m, m+E-e_t]; PA: [2m, 2m+E-e_t]) and Q+t; returns dict of booleans."""
    p = c.p
    lQ, lQc = c.lam(y, m), c.lamc(y, m)
    lQt, lQtc = c.lam(y + d, m + 1), c.lamc(y + d, m + 1)
    gen = (lQ == (y + c.B) // 2 + 1 and lQc == (c.A - y) // 2 + 1 and lQt == (y + d + c.B) // 2 + 1 and lQtc == (c.A - y - d) // 2 + 1)
    slo = lQt - (p - lQc); shi = (p - lQtc) - lQ
    qs = (2 * slo >= d - c.D0 + 2) and (2 * shi <= d + c.D0 - 2)
    nw = (c.lam(d, 1) - shi > -p) and (c.U(d, 1) - slo < p)
    avail = (2 * m + 2 <= c.k) and (m <= (cdiv(c.k - c.B - 3, 2) if fam == 'SA' else cdiv(c.k - 2 * c.B - 4, 3)))
    return dict(generic=gen, qs=qs, nw=nw, avail=avail, lam=(lQ, lQc, lQt, lQtc), seed=(max(c.lam(d, 1), slo), min(c.U(d, 1), shi)))
def region_family_check(c, fam, m, yshift=0):
    bad = []; n = 0
    for d in c.weights():
        base = m if fam == 'SA' else 2 * m
        for y in range(base, base + c.E - et(d) + 1 + yshift):
            r = arc_check(c, fam, m, d, y); n += 1
            if not (r['generic'] and r['qs'] and r['nw'] and r['avail']): bad.append((d, y))
    return n, bad
res = {'label': 'delegated parent delta check (subagent SeedGReviewDesk): own arithmetic, no lane code', 'started': time.strftime('%Y-%m-%dT%H:%M:%S')}
# A. six Claim E' classes, (11;5,3), p = 7 classes: notation (p; kB, B), E = 0
def e0(p, kB, B): kappa = kB + B; return C(p, p + kappa, kappa, B)
A = {}
for (p, kB, B, fam, m) in [(11, 4, 2, 'SA', 4), (11, 5, 2, 'PA', 4), (13, 6, 2, 'PA', 4), (13, 7, 2, 'PA', 5), (13, 5, 3, 'SA', 5), (17, 7, 4, 'SA', 7),
                           (11, 5, 3, None, None), (7, 2, 2, None, None), (7, 1, 3, None, None)]:
    c = e0(p, kB, B); ent = {'Delta0': c.D0, 'k': c.k, 'E': c.E, 'SA_region': c.sa(), 'PA_region': c.pa()}
    if fam:
        lo, hi = c.sa() if fam == 'SA' else c.pa()
        ent['m_in_region'] = lo <= m <= hi
        ent['arcs'] = {}
        for d in (1, -1):
            y = m if fam == 'SA' else 2 * m
            r = arc_check(c, fam, m, d, y); ent['arcs'][str(d)] = r
        ent['all_ok'] = ent['m_in_region'] and all(v['generic'] and v['qs'] and v['nw'] and v['avail'] and v['seed'][0] <= v['seed'][1] for v in ent['arcs'].values())
    else:
        sa = c.sa(); pa = c.pa()
        ent['outside_SA'] = sa[0] > sa[1]; ent['outside_PA'] = (pa is None) or (pa[0] > pa[1])
    A['(%d;%d,%d)' % (p, kB, B)] = ent
res['A_named_classes'] = A
# B. enumeration of E = 0, B in {2,3}, 2B + kB >= p - 1 classes (notation (B, kB))
Bres = {}
for p in [q for q in range(5, 200) if isprime(q)]:
    got = sorted((B, kB) for B in (2, 3) for kB in range(1, p) if kB + B <= p - 3 and 2 * B + kB >= p - 1)
    want = sorted([(2, p - 5), (3, p - 6), (3, p - 7)]) if p >= 11 else None
    Bres[p] = (got, want is None or got == want)
res['B_enumeration'] = {'p5': Bres[5][0], 'p7': Bres[7][0], 'p>=11 all exact (p<200)': all(v[1] for p, v in Bres.items() if p >= 11)}
# C. Corollary (large B) containment, E = 0, B >= 2, primes 11..199
def inRB(p, kB, B): return B >= 2 and kB >= 1 and 2 * B + kB <= p - 2
def condE(p, kB, B): return 5 * kB + B + 13 <= 3 * p or 2 * kB + 7 * B + 28 <= 4 * p
viol = []; rb_fail_E = []; cnt = {}
for p in [q for q in range(11, 200) if isprime(q)]:
    for B in range(2, p):
        for kB in range(1, p):
            if kB + B > p - 3: continue
            c = e0(p, kB, B)
            sa, pa = c.sa(), c.pa()
            inSA = sa[0] <= sa[1]; inPA = pa is not None and pa[0] <= pa[1]
            if inRB(p, kB, B) and not condE(p, kB, B):
                rb_fail_E.append((p, kB, B, 'SA' if inSA else ('PA' if inPA else 'none')))
            ra = (B == 2 and kB == p - 5) or (B == 3 and kB == p - 6 and p >= 13) or (B == 3 and kB == p - 7)
            cat = 'SB' if (inRB(p, kB, B) and condE(p, kB, B)) else ('SA/PA' if (inSA or inPA) else ('RA' if ra else 'rest'))
            cnt[cat] = cnt.get(cat, 0) + 1
            if cat == 'rest' and not ((B >= 4 and 2 * B + kB >= p - 1) or (p, kB, B) == (11, 5, 3)): viol.append((p, kB, B))
res['C_large_B'] = {'violations': viol, 'RB_failing_E': rb_fail_E, 'category_counts_p11_199': cnt}
# D. off-by-one equivalence
eq_fail = 0; old_fail = []; lb_fail = 0; n = 0
for kB in range(1, 31):
    for B in range(1, 31):
        for d in range(-40, 120):
            n += 1
            lhs = (d + B) // 2 + 1 < d + 1 - kB
            if lhs != (d > 2 * kB + B): eq_fail += 1
            if lhs != (d > 2 * kB + B - 1) and len(old_fail) < 3: old_fail.append((kB, B, d))
            if lhs and (d + B) // 2 + 1 < kB + B + 1: lb_fail += 1
res['D_off_by_one'] = {'instances': n, 'r2_equivalence_failures': eq_fail, 'r1_equivalence_counterexamples_first3': old_fail, 'lambda_bound_failures': lb_fail}
# E. cyclic distance of t+2, t-2
cyc = {}
for k in range(5, 201):
    dd = (4) % k; dist = min(dd, k - dd)
    cyc[k] = (dist, min(4, k - 4))
res['E_cyclic'] = {'formula_matches_k5_200': all(a == b for a, b in cyc.values()), 'k5': cyc[5], 'k6': cyc[6], 'k7': cyc[7],
                   'min_k_from_setting': 'kappa >= B + 1 >= 2 and k >= 2 kappa + 3 give k >= 7'}
# F. region brute force: every class p <= PMAXF, every m of each nonempty region, every weight and y of Lemma CF's range
PMAXF = 31
F = {'classes': 0, 'SA_classes': 0, 'PA_classes': 0, 'instances': 0, 'failures': 0, 'fail_examples': [],
     'mut_m_minus_1': {'instances': 0, 'failing_class_m': 0, 'tested_class_m': 0},
     'mut_y_plus_1': {'instances': 0, 'failing_class_m': 0, 'tested_class_m': 0}}
for p in [q for q in range(5, PMAXF + 1) if isprime(q)]:
    for (k, kappa, B) in classes(p):
        c = C(p, k, kappa, B); F['classes'] += 1
        for fam, reg in (('SA', c.sa()), ('PA', c.pa())):
            if reg is None or reg[0] > reg[1]: continue
            F[fam + '_classes'] += 1
            for m in range(reg[0], reg[1] + 1):
                n, bad = region_family_check(c, fam, m); F['instances'] += n
                if bad:
                    F['failures'] += len(bad)
                    if len(F['fail_examples']) < 10: F['fail_examples'].append((p, k, kappa, B, fam, m, bad[:3]))
            if reg[0] - 1 >= 1:
                n, bad = region_family_check(c, fam, reg[0] - 1); F['mut_m_minus_1']['instances'] += n
                F['mut_m_minus_1']['tested_class_m'] += 1; F['mut_m_minus_1']['failing_class_m'] += bool(bad)
            n, bad = region_family_check(c, fam, reg[1], yshift=1); F['mut_y_plus_1']['instances'] += n
            F['mut_y_plus_1']['tested_class_m'] += 1; F['mut_y_plus_1']['failing_class_m'] += bool(bad)
res['F_regions_p_le_%d' % PMAXF] = F
# G. Remark (1): RA2 and RA3 (b) generic and inside PA; RA3 (a) non-generic and outside SA, PA
G = {'RA2': [], 'RA3b': [], 'RA3a': []}
for p in [q for q in range(11, 200) if isprime(q)]:
    for key, B, kB, m, pmin in (('RA2', 2, p - 5, (p - 3) // 2, 11), ('RA3b', 3, p - 7, (p - 5) // 2, 11), ('RA3a', 3, p - 6, (p - 3) // 2, 13)):
        if p < pmin: continue
        c = e0(p, kB, B); pa = c.pa(); sa = c.sa()
        inPA = pa is not None and pa[0] <= m <= pa[1]
        arcs = [arc_check(c, 'PA', m, d, 2 * m) for d in (1, -1)]
        gen = all(a['generic'] for a in arcs)
        seeds = [a['seed'] for a in arcs]
        if key == 'RA3a':
            ok = (not gen) and (pa is None or pa[0] > pa[1]) and sa[0] > sa[1] and c.lamc(2 * m, m) == p - m - 3 and (c.A - 2 * m) // 2 + 1 == p - m - 2
        else:
            ok = gen and inPA
        exp = {'RA2': [(0, 0), (-1, -1)], 'RA3b': [(0, 1), (-1, 0)], 'RA3a': [(0, 1), (-1, 0)]}[key]
        G[key].append(ok and seeds == exp and all(a['qs'] and a['nw'] and a['avail'] for a in arcs))
res['G_remark1'] = {k: {'primes': len(v), 'all_ok': all(v)} for k, v in G.items()}
res['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S')
with open(OUT, 'x') as f: json.dump(res, f, indent=1, default=str); f.write('\n')
