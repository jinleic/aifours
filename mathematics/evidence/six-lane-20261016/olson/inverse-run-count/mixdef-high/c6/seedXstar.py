#!/usr/bin/env python3
"""seedXstar.py -- [F] class-level check of Corollary X* of c6/proof-SEEDG-star.md (Theorem SEED-G* with exact seeds), task
OlsonRunCount5 cycle 6.  Usage: python3 seedXstar.py MODE PMAX
The exact seeds, profiles and families are those of c6/seedX2.py (its functions exec'ed read-only).  For every allowed profile the
live weights (nonempty seeds) must satisfy (QS*) -- a_t >= 1 - ceil(L_A(d)), b_t <= ceil(L_B(d)) - 1 with L_A, L_B the minima of the nine
displayed lower bounds of the proof of Lemma SCW-G (proof-SEEDG-r1.md Sec. 2) -- and (P2): for every two live weights d1, d2 with
e(d1) + e(d2) <= E and m in {1, 2}, a1 + a2 >= 1 - lamc(d1 + d2, m) and b1 + b2 <= p + lam(d1 + d2, m) - 1, and (PIN): some live d with
b_d - lam(d, 1) <= p - 1; a profile also passes if a guaranteed weight (a*, -b*, 0 with pairs) has an empty seed.  Class: all profiles
pass, plus C+'s class condition.
MODE 0 real; 1: (QS) in place of (QS*) (must reproduce seedX2.py MODE 0); 2: every seed widened by one on both sides (fewer must pass).
"""
import sys, time, json, math
SRC = open('seedX2.py').read()
GUARD = "if __name__ == '__main__':\n    main()"
assert SRC.count(GUARD) == 1
NS = {'__name__': 'sx2lib'}
exec(compile(SRC.replace(GUARD, ''), 'c6/seedX2.py', 'exec'), NS)
cdiv = NS['cdiv']
def bounds(p, k, kappa, B, d, mode):
    R = 2 * p - k + 2 * kappa; E = R - k; D0 = 2 * p - R
    if mode == 1: return cdiv(d - D0, 2) + 1, (d + D0) // 2 - 1
    mn, mx = min(d, 0), max(d, 0)
    LA = min(D0 + E + 2, D0 + E / 2 + 1 - mn, (D0 + E) / 2 + 2, D0 + E / 2 - mn, D0 + E - d + 1, (D0 + E - d - mn + 3) / 2,
             (D0 + E + 3) / 2 - d + mx / 2, (R - d) / 2 + 1)
    LB = min(D0 + E + 2, D0 + E / 2 + mx, (D0 + E) / 2 + 2, D0 + E / 2 + mx + 1, D0 + E + d + 1, (D0 + E + mx + d + 3) / 2,
             (D0 + E + 3) / 2 + d - mn / 2, (R + d) / 2 + 1)
    return 1 - math.ceil(LA), math.ceil(LB) - 1
def class_pass(p, k, kappa, B, mode):
    R = 2 * p - k + 2 * kappa; E = R - k; kB = kappa - B; A = R - B
    lam = lambda y, m: min(p - m + 1, y + m - kB, (y + B) // 2 + 1)
    lamc = lambda y, m: min(p - m + 1, A - kappa - y + m, (A - y) // 2 + 1)
    prof = [(p + kB, p + kB, 1, 1, False)] if E == 0 else NS['profiles'](p, k, kappa, B)
    if not prof: return 'no-profile'
    w = 1 if mode == 2 else 0
    cache = {}
    ex = lambda d: (d - 1) if d >= 1 else ((-d - 1) if d <= -1 else 1)
    for (n1, nal, a_, b_, hp) in prof:
        ws = list(range(1, a_ + 1)) + list(range(-b_, 0)) + ([0] if hp else [])
        guaranteed = [a_] + ([-b_] if b_ >= 1 else []) + ([0] if hp else [])
        live = {}; gempty = False
        for d in ws:
            key = (n1, nal, d)
            if key not in cache: cache[key] = NS['exact_seed'](p, k, kappa, B, n1, nal, d, ('S1', 'P1', 'SA', 'PA'))
            s = cache[key]
            if s is None:
                if d in guaranteed: gempty = True
                continue
            live[d] = (s[0] - w, s[1] + w)
        if gempty: continue
        ok = all(bounds(p, k, kappa, B, d, mode)[0] <= a and b <= bounds(p, k, kappa, B, d, mode)[1] for d, (a, b) in live.items())
        if ok:
            for d1, (a1, b1) in live.items():
                for d2, (a2, b2) in live.items():
                    if ex(d1) + ex(d2) > E: continue
                    for m in (1, 2):
                        if a1 + a2 < 1 - lamc(d1 + d2, m) or b1 + b2 > p + lam(d1 + d2, m) - 1: ok = False
            if ok and not any(b - lam(d, 1) <= p - 1 for d, (a, b) in live.items()): ok = False
        if not ok: return 'fail'
    cplus = (E <= 4) or (2 * kB <= p and E <= 2 * (k - kB - 2 * B) - 1)
    return 'pass' if cplus else 'pass-noC+'
def main():
    mode = int(sys.argv[1]); PMAX = int(sys.argv[2])
    ns = {'__name__': 'map6mod'}
    exec(open('map6.py').read(), ns)
    t0 = time.time()
    print('== seedXstar.py MODE=%d PMAX=%d start %s' % (mode, PMAX, time.strftime('%Y-%m-%dT%H:%M:%S')), flush=True)
    for p in [q for q in range(11, PMAX + 1) if NS['isprime'](q)]:
        cnt = {}
        for (k, kappa, B) in NS['classes'](p):
            lab = ns['classify'](p, k, kappa, B)
            r = class_pass(p, k, kappa, B, mode)
            key = lab + ':' + r
            cnt[key] = cnt.get(key, 0) + 1
        print(json.dumps({'p': p, 'counts': dict(sorted(cnt.items())), 't': round(time.time() - t0, 1)}), flush=True)
    print('== end %.1f s' % (time.time() - t0), flush=True)
if __name__ == '__main__':
    main()
