#!/usr/bin/env python3
"""seedG.py -- [F] exact controls for c6/proof-SEEDG.md (Theorem SEED-G, Lemmas P0, GS, NW, SCW-G, Corollaries SA, PA,
Propositions RA2, RA3), task OlsonRunCount5 cycle 6.  Aids only, never hypotheses.
Usage: python3 seedG.py PART   (PART in A, B, C, D, E, M)
Classes: item-(iii) parameter classes (p, k, kappa, B): p + 1 <= k <= 2p - 2, R = 2p - k + 2 kappa, k <= R <= 2p - 3,
1 <= B <= kappa - 1, B <= A = R - B <= 2p - 1; E = R - k, kB = kappa - B, Delta0 = 2p - R.
Arcs (Lemma H, beta = 0): lam(y, m) = min(p - m + 1, y + m - kB, floor((y + B)/2) + 1),
lamc(y, m) = min(p - m + 1, A - kappa - y + m, floor((A - y)/2) + 1), U = p - lamc.
Weights d of a run: -min(B, E + 1) <= d <= E + 1.
Part A: Lemma SCW-G, case s >= 3: for every weight d, every y' in [-B - min(d, 0), A - max(d, 0)], every m in [1, k // 2] and
  m' in {m - 1, m} (m' >= 1): lam(y', m') + lamc(y' + d, m) >= floor((Delta0 - d)/2) and lam(y' + d, m) + lamc(y', m') >=
  floor((Delta0 + d)/2) (the largest possible targets 1 - a_t, b_t + 1 under (QS)).  Exhaustive for p <= 23, every y' and every
  m; for 29 <= p <= 43 every y' and every m on a stride (stated).  Also the minimum slack.
Part B: Lemma P0, Lemma NW (with the extreme quality seeds), the 2-run steps (all weight pairs (d1, d2) allowed by the excess and
  anti-letter budgets, m in {1, 2}, worst quality seeds intersected with the canonical ranges) and the pin, every class, primes
  11 <= p <= 61.
Part C: Propositions RA2, RA3 for every prime 11 <= p <= 2000 (resp. 13 / 11): the seeds of the pairs configuration computed from
  lam/lamc equal the stated values, the availability bound, quality, no wrap, and (RA2) sum = -2 not 0 mod p.
Part D: Corollaries SA and PA: every class, primes 11 <= p <= 61, satisfying the stated region (with b* = min(B, E + 1) and the
  smallest admissible m): for every b <= b* (smaller maximal anti length), every weight d in [-b, E + 1] and every type y in the
  family's range coupled with d (y + d <= m + E + 1 resp. 2m + E + 1 for aligned d; y <= m + E - e_t in general), the four arcs of
  Q and Q + t are generic, and the resulting seed satisfies (QS).
Part E: class-level counts of the written regions (SA, PA, RA2, RA3) and of C+'s class condition against the c6 map labels
  (map6.py classify, exec'ed read-only), primes 11 <= p <= 61.
Part M: mutation controls: (M1) Part A/B with seeds widened by one (targets + 1); (M2) Part D with m - 1 instead of m (lower end
  of the region) ; (M3) RA2/RA3 with m - 1 and m + 1; (M4) SA region with the (b2)-bound weakened by one.
"""
import sys, time, json
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
def cdiv(a, b): return -((-a) // b)
def classes(p):
    out = []
    for k in range(p + 1, 2 * p - 1):
        for kappa in range(max(k - p, 1), (k - 3) // 2 + 1):
            R = 2 * p - k + 2 * kappa
            if R < k or R > 2 * p - 3: continue
            for B in range(1, kappa):
                A = R - B
                if B > A or A > 2 * p - 1: continue
                out.append((k, kappa, B))
    return out
class C:
    def __init__(s, p, k, kappa, B):
        s.p, s.k, s.kappa, s.B = p, k, kappa, B
        s.R = 2 * p - k + 2 * kappa; s.A = s.R - B; s.E = s.R - k; s.kB = kappa - B; s.D0 = 2 * p - s.R
    def lam(s, y, m): return min(s.p - m + 1, y + m - s.kB, (y + s.B) // 2 + 1)
    def lamc(s, y, m): return min(s.p - m + 1, s.A - s.kappa - y + m, (s.A - y) // 2 + 1)
    def U(s, y, m): return s.p - s.lamc(y, m)
    def weights(s): return list(range(-min(s.B, s.E + 1), s.E + 2))
    def qs(s, d, widen=0):   # extreme quality seed (integer), widened
        return (cdiv(d - s.D0, 2) + 1 - widen, (d + s.D0) // 2 - 1 + widen)
def partA(widen=0):
    t0 = time.time(); tot = 0; fails = []; minslack = None; per = {}
    for p in [q for q in range(11, 44) if isprime(q)]:
        stride = 1 if p <= 23 else 3
        n = 0
        for (k, kappa, B) in classes(p):
            c = C(p, k, kappa, B)
            for d in c.weights():
                tA = (c.D0 - d) // 2 + widen; tB = (c.D0 + d) // 2 + widen
                ylo = -B - min(d, 0); yhi = c.A - max(d, 0)
                for yp in range(ylo, yhi + 1, stride if stride == 1 else 1):
                    y = yp + d
                    for m in range(1, k // 2 + 1, stride):
                        for mp in (m - 1, m):
                            if mp < 1: continue
                            sA = c.lam(yp, mp) + c.lamc(y, m); sB = c.lam(y, m) + c.lamc(yp, mp)
                            n += 1
                            sl = min(sA - tA, sB - tB)
                            minslack = sl if minslack is None else min(minslack, sl)
                            if sl < 0 and len(fails) < 10: fails.append((p, k, kappa, B, d, yp, m, mp, sA, sB, tA, tB))
        per[p] = n; tot += n
        print(json.dumps({'partA_p': p, 'stride_m': stride, 'triples': n, 't': round(time.time() - t0, 1)}), flush=True)
    return {'partA_widen': widen, 'triples': tot, 'min_slack': minslack, 'failures_first10': fails, 'nfail_shown': len(fails)}
def two_run_budget_ok(c, d1, d2):
    ex = lambda d: (d - 1) if d >= 1 else ((-d - 1) if d <= -1 else 1)
    antil = lambda d: (-d) if d < 0 else (1 if d == 0 else 0)
    return ex(d1) + ex(d2) <= c.E and antil(d1) + antil(d2) <= c.B
def partB(widen=0):
    t0 = time.time(); stats = {'classes': 0, 'P0': 0, 'NW': 0, 'two_run': 0, 'pin': 0, 'empty_seed_ranges': 0}; fails = []
    for p in [q for q in range(11, 62) if isprime(q)]:
        for (k, kappa, B) in classes(p):
            c = C(p, k, kappa, B); stats['classes'] += 1
            rng = {}
            for d in c.weights():
                L1, U1 = c.lam(d, 1), c.U(d, 1)
                stats['P0'] += 1
                if L1 + c.lamc(d, 1) < 1: fails.append(('P0', p, k, kappa, B, d))
                lo, hi = c.qs(d, widen)
                stats['NW'] += 1
                if not (L1 - hi > -p and U1 - lo < p): fails.append(('NW', p, k, kappa, B, d))
                a, b = max(L1, lo), min(U1, hi)
                if a > b: stats['empty_seed_ranges'] += 1
                rng[d] = (a, b)
            for d1 in c.weights():
                for d2 in c.weights():
                    if not two_run_budget_ok(c, d1, d2): continue
                    if rng[d1][0] > rng[d1][1] or rng[d2][0] > rng[d2][1]: continue
                    y = d1 + d2
                    for m in (1, 2):
                        stats['two_run'] += 1
                        if rng[d1][0] + rng[d2][0] < 1 - c.lamc(y, m) or rng[d1][1] + rng[d2][1] > p + c.lam(y, m) - 1:
                            if len(fails) < 20: fails.append(('2run', p, k, kappa, B, d1, d2, m))
            for d in c.weights():
                if rng[d][0] > rng[d][1]: continue
                stats['pin'] += 1
                yc = c.A - B - d
                if not (rng[d][0] + c.lam(yc, 1) >= 1 and rng[d][1] + c.U(yc, 1) <= 2 * p - 1):
                    if len(fails) < 20: fails.append(('pin', p, k, kappa, B, d))
        print(json.dumps({'partB_p': p, 'stats': stats, 'nfail': len(fails), 't': round(time.time() - t0, 1)}), flush=True)
    return {'partB_widen': widen, 'stats': stats, 'failures_first20': fails[:20], 'nfail': len(fails)}
def pairs_seed(c, m, d):
    return (c.lam(2 * m + d, m + 1) - c.U(2 * m, m), c.U(2 * m + d, m + 1) - c.lam(2 * m, m))
def partC(shift=0):
    t0 = time.time(); res = {'RA2': 0, 'RA3a': 0, 'RA3b': 0}; fails = []
    for p in [q for q in range(11, 2001) if isprime(q)]:
        for (name, B, kB, m0, pmin, want_al, want_an) in (('RA2', 2, p - 5, (p - 3) // 2, 11, (0, 0), (-1, -1)),
                                                          ('RA3a', 3, p - 6, (p - 3) // 2, 13, (0, 1), (-1, 0)),
                                                          ('RA3b', 3, p - 7, (p - 5) // 2, 11, (0, 1), (-1, 0))):
            if p < pmin: continue
            kappa = kB + B; k = p + kappa
            c = C(p, k, kappa, B)
            assert c.E == 0 and k <= 2 * p - 3 and 2 * B + kB >= p - 1 and kB >= 1
            m = m0 + shift
            n = p + kB
            ok_av = m >= 1 and m <= cdiv(n - B - 4, 3) and m + 1 <= k // 2
            sal = pairs_seed(c, m, 1); san = pairs_seed(c, m, -1)
            qal = c.qs(1); qan = c.qs(-1)
            ok = ok_av and sal == want_al and san == want_an and qal[0] <= sal[0] and sal[1] <= qal[1] and qan[0] <= san[0] and san[1] <= qan[1]
            # no wrap (Lemma NW / explicit)
            ok = ok and c.lam(1, 1) - sal[1] > -p and c.U(1, 1) - sal[0] < p and c.lam(-1, 1) - san[1] > -p and c.U(-1, 1) - san[0] < p
            if name == 'RA2': ok = ok and ((n * 0 + B * (-1)) % p != 0)
            if ok: res[name] += 1
            elif len(fails) < 12: fails.append((name, p, m, ok_av, sal, san))
    print(json.dumps({'partC_shift': shift, 't': round(time.time() - t0, 1)}), flush=True)
    return {'partC_shift': shift, 'passed': res, 'failures_first12': fails, 'nfail_shown': len(fails)}
def region_SA(c, bstar, weaken=0):
    p, k, B, E, kB, D0 = c.p, c.k, c.B, c.E, c.kB, c.D0
    lo = max(cdiv(2 * kB + B + max(2, bstar) - weaken, 3), B + 2 - D0, 1)
    hi = min((2 * p - B - E - 3) // 3, D0 + B - bstar - 2, cdiv(k - B - 3, 2))
    return lo if lo <= hi else None
def region_PA(c, bstar):
    p, k, B, E, kB, D0 = c.p, c.k, c.B, c.E, c.kB, c.D0
    if not (D0 >= B + 1 and bstar <= D0 + B - 1): return None
    lo = max(cdiv(kB + B // 2 + 1, 2), cdiv(kB + bstar + (B - bstar) // 2, 2), 1)
    hi = min((p - (E + B) // 2) // 2, (p - 1 - (E + B + 1) // 2) // 2, cdiv(k - 2 * B - 4, 3))
    return lo if lo <= hi else None
def generic(c, y, m):
    return c.lam(y, m) == (y + c.B) // 2 + 1 and c.lamc(y, m) == (c.A - y) // 2 + 1
def check_family(c, fam, m, bmax):
    """every b <= bmax, every weight d in [-b, E + 1], every y of the family coupled with d."""
    bad = 0; seeds_ok = True
    for b in range(0, bmax + 1):
        for d in range(-b, c.E + 2):
            et = (d - 1) if d >= 1 else ((-d - 1) if d <= -1 else 1)
            if et > c.E: continue
            base = m if fam == 'SA' else 2 * m
            for y in range(base, base + c.E - et + 1):
                if not (generic(c, y, m) and generic(c, y + d, m + 1)): bad += 1; continue
                slo = c.lam(y + d, m + 1) - c.U(y, m); shi = c.U(y + d, m + 1) - c.lam(y, m)
                q = c.qs(d)
                if not (q[0] <= slo and shi <= q[1]): seeds_ok = False
    return bad, seeds_ok
def partD(shiftm=0):
    t0 = time.time(); st = {'SA_classes': 0, 'PA_classes': 0, 'SA_bad': 0, 'PA_bad': 0, 'seed_quality_fail': 0}; fails = []
    for p in [q for q in range(11, 62) if isprime(q)]:
        for (k, kappa, B) in classes(p):
            c = C(p, k, kappa, B); bstar = min(B, c.E + 1)
            for fam, reg in (('SA', region_SA), ('PA', region_PA)):
                m = reg(c, bstar)
                if m is None: continue
                st[fam + '_classes'] += 1
                bad, sq = check_family(c, fam, m + shiftm, bstar) if m + shiftm >= 1 else (1, False)
                if bad: st[fam + '_bad'] += 1
                if not sq: st['seed_quality_fail'] += 1
                if (bad or not sq) and len(fails) < 10: fails.append((fam, p, k, kappa, B, m, bad, sq))
        print(json.dumps({'partD_p': p, 'stats': st, 't': round(time.time() - t0, 1)}), flush=True)
    return {'partD_shiftm': shiftm, 'stats': st, 'failures_first10': fails}
def partE():
    ns = {'__name__': 'map6mod'}
    exec(open('map6.py').read(), ns)
    out = {}
    for p in [q for q in range(11, 62) if isprime(q)]:
        cnt = {}
        for (k, kappa, B) in classes(p):
            c = C(p, k, kappa, B); lab = ns['classify'](p, k, kappa, B)
            bstar = min(B, c.E + 1)
            cplus = (c.E <= 4) or (2 * c.kB <= p and c.E <= 2 * (k - c.kB - 2 * B) - 1)
            ra = c.E == 0 and ((B == 2 and c.kB == p - 5) or (B == 3 and c.kB == p - 6 and p >= 13) or (B == 3 and c.kB == p - 7))
            if ra: cov = 'RA'
            elif region_SA(c, bstar) is not None: cov = 'SA'
            elif region_PA(c, bstar) is not None: cov = 'PA'
            else: cov = '-'
            if cov in ('SA', 'PA') and not cplus: cov += '(noC+)'
            key = lab + ':' + cov
            cnt[key] = cnt.get(key, 0) + 1
        out[p] = dict(sorted(cnt.items()))
        print(json.dumps({'partE_p': p, 'counts': out[p]}), flush=True)
    return {'partE': 'done'}
def main():
    part = sys.argv[1]
    t0 = time.time()
    print('== seedG.py part %s start %s' % (part, time.strftime('%Y-%m-%dT%H:%M:%S')), flush=True)
    if part == 'A': r = partA()
    elif part == 'B': r = partB()
    elif part == 'C': r = partC()
    elif part == 'D': r = partD()
    elif part == 'E': r = partE()
    elif part == 'M':
        r = {'M1_partB_widen1': partB(widen=1)['nfail'], 'M2_partD_m_minus_1': partD(shiftm=-1)['stats'],
             'M3_RA_m_minus_1': partC(shift=-1)['passed'], 'M3_RA_m_plus_1': partC(shift=1)['passed']}
        # M4: SA region with the (b2)/(a2) lower bound weakened by one: some classes must fail the generic check
        st = {'classes': 0, 'bad': 0}
        for p in [q for q in range(11, 44) if isprime(q)]:
            for (k, kappa, B) in classes(p):
                c = C(p, k, kappa, B); bstar = min(B, c.E + 1)
                m0 = region_SA(c, bstar); m1 = region_SA(c, bstar, weaken=3)
                if m1 is None or (m0 is not None and m1 >= m0): continue
                st['classes'] += 1
                bad, sq = check_family(c, 'SA', m1, bstar)
                if bad or not sq: st['bad'] += 1
        r['M4_SA_weakened'] = st
    print(json.dumps({'result': r}), flush=True)
    print('== end %.1f s' % (time.time() - t0), flush=True)
if __name__ == '__main__':
    main()
