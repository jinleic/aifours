#!/usr/bin/env python3
"""seedXX.py -- [F] effect of the count-free finishers of c6/proof-C0WB.md (Lemmas C0W, C0B; Theorem SEED-G**), task OlsonRunCount5.
Usage: python3 seedXX.py PART PMAX
PART R: every item-(iii) class with p <= PMAX inside the region SA or PA of c6/proof-SEEDG-r2.md: which class condition finishes it --
  C+ (E <= 4, or 2kB <= p and E <= 2(k - kB - 2B) - 1), else F2 (B >= kB + 1 and 3kB + 1 <= p), else F3 (k >= kB + 3B; the region
  seeds are quality seeds), else none; counts by the c6 map label.
PART X: every item-(iii) class with p <= PMAX: the seed part of Corollary X* (exact seeds of c6/seedXstar2.py / seedX2.py, functions
  exec'ed read-only; (QS*), (P2), (PIN) for live weights; a guaranteed weight with empty seed excludes the profile) and then the
  finisher: C+ class condition, else F2, else F3 (k >= kB + 3B and [2kB <= p, or min(kB - 1, d - a_d) <= p - kB - 1 for every live
  weight of every allowed profile]); counts by label.
PART A (ablations, p <= PMAX): PART X with F2 removed, with F3 removed, and with the seed alternative of F3 removed.
"""
import sys, time, json, math
SRC = open('seedXstar2.py').read()
GUARD = "if __name__ == '__main__':\n    main()"
assert SRC.count(GUARD) == 1
NS = {'__name__': 'sxs2lib'}
exec(compile(SRC.replace(GUARD, ''), 'c6/seedXstar2.py', 'exec'), NS)
NSX = NS['NS']           # seedX2 library (profiles, exact_seed, regions, classes)
cdiv = NSX['cdiv']
def seed_part(p, k, kappa, B):
    """returns (ok, list of live seed dicts per non-excluded profile)."""
    R = 2 * p - k + 2 * kappa; E = R - k; kB = kappa - B; A = R - B
    lam = lambda y, m: min(p - m + 1, y + m - kB, (y + B) // 2 + 1)
    lamc = lambda y, m: min(p - m + 1, A - kappa - y + m, (A - y) // 2 + 1)
    prof = [(p + kB, p + kB, 1, 1, False)] if E == 0 else NSX['profiles'](p, k, kappa, B)
    if not prof: return False, []
    ex = lambda d: (d - 1) if d >= 1 else ((-d - 1) if d <= -1 else 1)
    cache = {}; lives = []
    for (n1, nal, a_, b_, hp) in prof:
        ws = list(range(1, a_ + 1)) + list(range(-b_, 0)) + ([0] if hp else [])
        guaranteed = [a_] + ([-b_] if b_ >= 1 else []) + ([0] if hp else [])
        live = {}; gempty = False
        for d in ws:
            key = (n1, nal, d)
            if key not in cache: cache[key] = NSX['exact_seed'](p, k, kappa, B, n1, nal, d, ('S1', 'P1', 'SA', 'PA'))
            s = cache[key]
            if s is None:
                if d in guaranteed: gempty = True
                continue
            live[d] = s
        if gempty: continue
        for d, (a, b) in live.items():
            lo, hi = NS['bounds'](p, k, kappa, B, d, 0)
            if a < lo or b > hi: return False, []
        for d1, (a1, b1) in live.items():
            for d2, (a2, b2) in live.items():
                if ex(d1) + ex(d2) > E: continue
                for m in (1, 2):
                    if a1 + a2 < 1 - lamc(d1 + d2, m) or b1 + b2 > p + lam(d1 + d2, m) - 1: return False, []
        if not all(b - lam(d, 1) <= p - 1 for d, (a, b) in live.items()): return False, []
        lives.append(live)
    return True, lives
def finisher(p, k, kappa, B, lives, use_F2=True, use_F3=True, use_seedA=True, quality=False):
    R = 2 * p - k + 2 * kappa; E = R - k; kB = kappa - B
    if (E <= 4) or (2 * kB <= p and E <= 2 * (k - kB - 2 * B) - 1): return 'C+'
    if use_F2 and B >= kB + 1 and 3 * kB + 1 <= p: return 'F2'
    if use_F3 and k >= kB + 3 * B:
        if 2 * kB <= p or quality: return 'F3'
        if use_seedA and all(min(kB - 1, d - a) <= p - kB - 1 for live in lives for d, (a, b) in live.items()): return 'F3*'
    return 'none'
def main():
    part = sys.argv[1]; PMAX = int(sys.argv[2])
    ns = {'__name__': 'map6mod'}
    exec(open('map6.py').read(), ns)
    t0 = time.time()
    print('== seedXX.py PART=%s PMAX=%d start %s' % (part, PMAX, time.strftime('%Y-%m-%dT%H:%M:%S')), flush=True)
    for p in [q for q in range(11, PMAX + 1) if NSX['isprime'](q)]:
        cnt = {}
        for (k, kappa, B) in NSX['classes'](p):
            lab = ns['classify'](p, k, kappa, B)
            if part == 'R':
                if not (NSX['region_SA'](p, k, kappa, B) or NSX['region_PA'](p, k, kappa, B)): continue
                r = finisher(p, k, kappa, B, [], quality=True)
                key = lab + ':' + r
            else:
                ok, lives = seed_part(p, k, kappa, B)
                if not ok: key = lab + ':seedfail'
                elif part == 'X': key = lab + ':' + finisher(p, k, kappa, B, lives)
                else:
                    key = lab + ':' + '/'.join([finisher(p, k, kappa, B, lives, use_F2=False), finisher(p, k, kappa, B, lives, use_F3=False),
                                                finisher(p, k, kappa, B, lives, use_seedA=False)])
            cnt[key] = cnt.get(key, 0) + 1
        print(json.dumps({'p': p, 'counts': dict(sorted(cnt.items())), 't': round(time.time() - t0, 1)}), flush=True)
    print('== end %.1f s' % (time.time() - t0), flush=True)
if __name__ == '__main__':
    main()
