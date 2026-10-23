#!/usr/bin/env python3
"""seedX3.py -- new immutable revision after the star/cls reviews: same arithmetic, current citations and source hashes.
[F] class-level exact-seed coverage (supersedes seedX.py, whose profile test wrongly accepted an empty seed of a weight that need not occur) for Corollary X of c6/proof-SEEDG-cls-r1.md (Theorem SEED-G with exact seeds of
always-available configuration types), task OlsonRunCount5 cycle 6.  Usage: python3 seedX3.py MODE PMAX
MODE 0: real.  1: (QS) tightened by one on both sides (fewer classes must pass).  2: families SA and PA dropped (only single-letter
singles S1 and pairs P1; fewer classes must pass).
For every item-(iii) class (p, k, kappa, B) with p <= PMAX, E = R - k >= 0 (E = 0 uses the explicit single profile), and every
run-length profile (a*, b*, n_pr) allowed by Lemma PR (n_al = k - B + e_an, e_an >= (b* - 1)^+, n1 >= k - B - E + 2(b* - 1)^+ + n_pr +
a* - 2 if a* >= 2, n1 = n_al if a* = 1), the exact seed of every weight d of the profile is the intersection, over the families
S1 (m single-letter aligned runs, m <= ceil((n1 - 3)/2), y = m), P1 (m blocks of two single-letter aligned runs, m <= ceil((2 n1 - k - 4)/3),
y = 2m), SA (m isolated aligned runs, m <= ceil((n_al - 3)/2), y in [m, m + E - e_t]) and PA (m blocks of two adjacent aligned runs,
m <= ceil((n_al - B - 4)/3), y in [2m, 2m + E - e_t]) and all admissible m, of the hull over y of [lam(y + d, m + 1) - U(y, m),
U(y + d, m + 1) - lam(y, m)], each used only if the no-wrap condition holds for every y of its range, intersected with the canonical
range [lambda({t}), U({t})].  A profile passes if (i) every weight d of its range has a seed that is empty (runs of weight d exclude
their words) or satisfies (QS), or (ii) one of the weights that every word of the profile contains -- a*, -b* (if b* >= 1), 0 (if
n_pr >= 1) -- has an empty seed; a class passes if all its profiles pass and C+'s class condition (E <= 4, or 2kB <= p and E <= 2(k - kB - 2B) - 1) holds.  Output per p:
counts by the c6 map label (c6/map6.py classify, exec'ed read-only) and by the written regions of proof-SEEDG-r2.md (SA, PA, RA).
"""
import sys, time, json, hashlib
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
def profiles(p, k, kappa, B):
    R = 2 * p - k + 2 * kappa; E = R - k
    out = []
    for astar in range(1, E + 2):
        for bstar in range(0, min(B, E + 1) + 1):
            for npr in range(0, min(B, E) + 1):
                if bstar == 0 and npr != B: continue
                ean = max(bstar - 1, 0)
                if bstar >= 1 and npr + ean + 1 > B: continue      # n_an >= 1
                if astar == 1:
                    ean = E - npr                                   # no long aligned run: the rest of the excess is anti
                    if bstar == 0 and ean != 0: continue
                    if bstar >= 1 and (ean < bstar - 1 or (bstar == 1 and ean > 0)): continue
                    if bstar >= 1 and npr + ean + 1 > B: continue
                    nal = k - B + ean; n1 = nal
                else:
                    eal = E - npr - ean
                    if eal < astar - 1: continue
                    nal = k - B + ean; n1 = nal - (eal - astar + 2)
                out.append((n1, nal, astar, bstar, npr > 0))
    return out
def exact_seed(p, k, kappa, B, n1, nal, d, fams):
    R = 2 * p - k + 2 * kappa; A = R - B; E = R - k; kB = kappa - B
    lam = lambda y, m: min(p - m + 1, y + m - kB, (y + B) // 2 + 1)
    lamc = lambda y, m: min(p - m + 1, A - kappa - y + m, (A - y) // 2 + 1)
    U = lambda y, m: p - lamc(y, m)
    L1, U1 = lam(d, 1), U(d, 1)
    lo, hi = L1, U1
    et = (d - 1) if d >= 1 else ((-d - 1) if d <= -1 else 1)
    er = max(E - et, 0)
    F = {'S1': (lambda m: [m], cdiv(n1 - 3, 2)), 'P1': (lambda m: [2 * m], cdiv(2 * n1 - k - 4, 3)),
         'SA': (lambda m: range(m, m + er + 1), cdiv(nal - 3, 2)), 'PA': (lambda m: range(2 * m, 2 * m + er + 1), cdiv(nal - B - 4, 3))}
    for f in fams:
        yr, M = F[f]
        for m in range(1, max(M, 0) + 1):
            if 2 * m + 2 > k: break
            hl = hh = None; ok = True
            for y in yr(m):
                slo = lam(y + d, m + 1) - U(y, m); shi = U(y + d, m + 1) - lam(y, m)
                if not (L1 - shi > -p and U1 - slo < p): ok = False; break
                hl = slo if hl is None else min(hl, slo); hh = shi if hh is None else max(hh, shi)
            if ok and hl is not None: lo = max(lo, hl); hi = min(hi, hh)
    return None if lo > hi else (lo, hi)
def class_pass(p, k, kappa, B, mode):
    R = 2 * p - k + 2 * kappa; E = R - k; kB = kappa - B; D0 = 2 * p - R
    fams = ('S1', 'P1') if mode == 2 else ('S1', 'P1', 'SA', 'PA')
    tight = 1 if mode == 1 else 0
    prof = [(p + kB, p + kB, 1, 1, False)] if E == 0 else profiles(p, k, kappa, B)
    if not prof: return 'no-profile'
    cache = {}
    for (n1, nal, a_, b_, hp) in prof:
        ws = list(range(1, a_ + 1)) + list(range(-b_, 0)) + ([0] if hp else [])
        guaranteed = [a_] + ([-b_] if b_ >= 1 else []) + ([0] if hp else [])
        bad = False; gempty = False
        for d in ws:
            key = (n1, nal, d)
            if key not in cache: cache[key] = exact_seed(p, k, kappa, B, n1, nal, d, fams)
            s = cache[key]
            if s is None:
                if d in guaranteed: gempty = True
                continue
            if not (s[0] >= cdiv(d - D0, 2) + 1 + tight and s[1] <= (d + D0) // 2 - 1 - tight): bad = True
        if bad and not gempty: return 'fail'
    cplus = (E <= 4) or (2 * kB <= p and E <= 2 * (k - kB - 2 * B) - 1)
    return 'pass' if cplus else 'pass-noC+'
def region_SA(p, k, kappa, B):
    R = 2 * p - k + 2 * kappa; E = R - k; kB = kappa - B; D0 = 2 * p - R; bs = min(B, E + 1)
    lo = max(cdiv(2 * kB + B + max(2, bs), 3), B + 2 - D0, 1)
    hi = min((2 * p - B - E - 3) // 3, D0 + B - bs - 2, cdiv(k - B - 3, 2))
    return lo <= hi
def region_PA(p, k, kappa, B):
    R = 2 * p - k + 2 * kappa; E = R - k; kB = kappa - B; D0 = 2 * p - R; bs = min(B, E + 1)
    if not (D0 >= B + 1 and bs <= D0 + B - 1): return False
    lo = max(cdiv(kB + B // 2 + 1, 2), cdiv(kB + bs + (B - bs) // 2, 2), 1)
    hi = min((p - (E + B) // 2) // 2, (p - 1 - (E + B + 1) // 2) // 2, cdiv(k - 2 * B - 4, 3))
    return lo <= hi
def source_manifest():
    return {p: hashlib.sha256(open(p, 'rb').read()).hexdigest() for p in
            ('seedX3.py', 'map6.py', '../c4/ind_star3.py', '../c4/ind_star_ex.py')}
def main():
    mode = int(sys.argv[1]); PMAX = int(sys.argv[2])
    detail = len(sys.argv) > 3 and sys.argv[3] == 'detail'
    print(json.dumps({'source_sha256': source_manifest()}), flush=True)
    ns = {'__name__': 'map6mod'}
    exec(open('map6.py').read(), ns)
    t0 = time.time()
    print('== seedX3.py MODE=%d PMAX=%d start %s' % (mode, PMAX, time.strftime('%Y-%m-%dT%H:%M:%S')), flush=True)
    for p in [q for q in range(11, PMAX + 1) if isprime(q)]:
        cnt = {}
        for (k, kappa, B) in classes(p):
            lab = ns['classify'](p, k, kappa, B)
            R = 2 * p - k + 2 * kappa; E = R - k; kB = kappa - B
            cplus = (E <= 4) or (2 * kB <= p and E <= 2 * (k - kB - 2 * B) - 1)
            written = (E == 0 and ((B == 2 and kB == p - 5) or (B == 3 and kB == p - 6 and p >= 13) or (B == 3 and kB == p - 7))) or \
                      (cplus and (region_SA(p, k, kappa, B) or region_PA(p, k, kappa, B)))
            r = class_pass(p, k, kappa, B, mode)
            if detail:
                print(json.dumps({'class': [p, k, kappa, B], 'label': lab, 'written': written, 'verdict': r}), flush=True)
            key = '%s:%s:%s' % (lab, 'written' if written else 'notwritten', r)
            cnt[key] = cnt.get(key, 0) + 1
        print(json.dumps({'p': p, 'counts': dict(sorted(cnt.items())), 't': round(time.time() - t0, 1)}), flush=True)
    print('== end %.1f s' % (time.time() - t0), flush=True)
if __name__ == '__main__':
    main()
