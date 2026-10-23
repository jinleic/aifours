#!/usr/bin/env python3
"""seedLB.py -- [F] class-level check of Corollary LB of c6/proof-LB.md for the all-single-letter item-(iii) classes with B >= 2 and
2B + kB >= p - 1 (large B), task OlsonRunCount5.  Usage: python3 seedLB.py MODE PMAX
For a class (p, kB, B): n = p + kB aligned and B anti single-letter runs, k = n + B, kappa = kB + B, E = 0, Delta0 = p - kappa.
RZ types: (y, m) with m = i + j, y = j - i, 0 <= i <= floor((B - 3)/2), 2m <= n - 3, 2m + 2 <= k (Lemma RZ: i pairwise non-adjacent anti
runs and j aligned runs, all pairwise non-adjacent and not adjacent to t, exist at every run t of every word).  For d = +1 (aligned t)
and d = -1 (anti t) the seed of a type is [max(lambda({t}), s_lo), min(U({t}), s_hi)], s_lo = lam(y + d, m + 1) - U(y, m),
s_hi = U(y + d, m + 1) - lam(y, m), used only if the no-wrap condition holds.  Route E: some RZ type gives an EMPTY seed for d = +1 or
d = -1 (every word has both kinds of runs): no avoider.  Route S: types for d = +1 and d = -1 whose seeds satisfy (QS*) (c6/proof-
SEEDGstar.md) and, together, (P2) (pairs of weights (1,1), (1,-1), (-1,-1), m = 1, 2) and (PIN); then Theorem SEED-G* and Lemma C0+ (i)
(n_ev,al = 0) exclude the class.  Route X: Corollary X* with the aligned singles/pairs families (c6/seedXstar2.py class_pass,
exec'ed read-only).  MODE 0: all routes; MODE 1 (control): (QS*) tightened by one on both sides in route S (fewer must pass);
MODE 2 (control): RZ with i <= floor((B - 3)/2) replaced by i <= 0 (aligned singles only; fewer must pass).
"""
import sys, time, json, math
SRC = open('seedXstar2.py').read()
GUARD = "if __name__ == '__main__':\n    main()"
NS = {'__name__': 'sxs2lib'}
exec(compile(SRC.replace(GUARD, ''), 'c6/seedXstar2.py', 'exec'), NS)
NSX = NS['NS']
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
def route_SE(p, kB, B, mode):
    n = p + kB; k = n + B; kappa = kB + B; A = n
    lam = lambda y, m: min(p - m + 1, y + m - kB, (y + B) // 2 + 1)
    lamc = lambda y, m: min(p - m + 1, A - kappa - y + m, (A - y) // 2 + 1)
    U = lambda y, m: p - lamc(y, m)
    imax = (B - 3) // 2 if mode != 2 else 0
    best = {}
    for d in (1, -1):
        L1, U1 = lam(d, 1), U(d, 1)
        alo, bhi = NS['bounds'](p, k, kappa, B, d, 0)
        if mode == 1: alo, bhi = alo + 1, bhi - 1
        cand = []
        for m in range(1, (n - 3) // 2 + 1):
            if 2 * m + 2 > k: break
            for i in range(0, min(m, max(imax, 0)) + 1):
                y = m - 2 * i
                slo = lam(y + d, m + 1) - U(y, m); shi = U(y + d, m + 1) - lam(y, m)
                if not (L1 - shi > -p and U1 - slo < p): continue
                a, b = max(L1, slo), min(U1, shi)
                if a > b: return ('E', d, (y, m))
                if a >= alo and b <= bhi: cand.append((b - a, a, b, y, m))
        if not cand: return ('noS', d, None)
        best[d] = min(cand)
    s = {d: (best[d][1], best[d][2]) for d in (1, -1)}
    for d1 in (1, -1):
        for d2 in (1, -1):
            for m in (1, 2):
                y = d1 + d2
                if s[d1][0] + s[d2][0] < 1 - lamc(y, m) or s[d1][1] + s[d2][1] > p + lam(y, m) - 1: return ('P2fail', (d1, d2, m), s)
    for d in (1, -1):
        if s[d][1] - lam(d, 1) > p - 1: return ('PINfail', d, s)
    return ('S', {d: best[d][3:] for d in (1, -1)}, s)
def main():
    mode = int(sys.argv[1]); PMAX = int(sys.argv[2])
    t0 = time.time()
    print('== seedLB.py MODE=%d PMAX=%d start %s' % (mode, PMAX, time.strftime('%Y-%m-%dT%H:%M:%S')), flush=True)
    grand = {}
    for p in [q for q in range(11, PMAX + 1) if isprime(q)]:
        cnt = {}; left = []
        for kB in range(1, p):
            for B in range(2, p):
                if kB + B > p - 3 or 2 * B + kB < p - 1: continue
                kappa = kB + B; k = p + kappa
                r = route_SE(p, kB, B, mode)
                if r[0] in ('E', 'S'): key = r[0]
                else:
                    rx = NS['class_pass'](p, k, kappa, B, 0) if mode != 2 else 'skip'
                    key = 'X' if rx == 'pass' else 'open'
                    if key == 'open': left.append((k, B, kB))
                cnt[key] = cnt.get(key, 0) + 1
        for kk, v in cnt.items(): grand[kk] = grand.get(kk, 0) + v
        print(json.dumps({'p': p, 'counts': dict(sorted(cnt.items())), 'open (k, B, kB)': left, 't': round(time.time() - t0, 1)}), flush=True)
    print(json.dumps({'totals': dict(sorted(grand.items()))}), flush=True)
    print('== end %.1f s' % (time.time() - t0), flush=True)
if __name__ == '__main__':
    main()
