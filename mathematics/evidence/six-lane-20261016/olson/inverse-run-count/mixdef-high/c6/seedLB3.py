#!/usr/bin/env python3
"""seedLB3.py -- [F] class-level checks for c6/proof-LB.md (Lemmas RZ, RZ2, RZX; Corollaries LB, LBX), task OlsonRunCount5.
Usage: python3 seedLB3.py PART PMAX
PART L: every all-single-letter item-(iii) class with B >= 2 and 2B + kB >= p - 1 (large B), primes 7 <= p <= PMAX (p = 7 included):
  route E/S (Lemma RZ types: i anti + j aligned single runs, i = 0 or 1 <= i <= floor((B - 3)/2), 2m <= n - 3), else route S2 (Lemma RZ2
  types: j2 blocks of two adjacent aligned runs and j1 single aligned runs, 3 j2 + 2 j1 <= n - B - 4), else route X (Corollary X*);
  E = an actual empty seed for d = +1 or -1; S, S2 = (QS*) seeds for d = +1, -1 with (P2) and (PIN).  The functions route_SE of
  c6/seedLB.py and class_pass of c6/seedXstar2.py are exec'ed read-only.
PART C (controls, p <= PMAX): route S2 with the capacity n - B - 4 replaced by n - B - 4 - 6 (fewer), and route S with i <= 0.
PART X: the class (p; k, kappa, B) = (31; 51, 24, 23) (E = 8) by Lemma RZX: for every allowed profile of Lemma PR, every weight d,
  RZX types (i anti + j aligned single runs of any lengths, i = 0 or 2i <= n_an - 3, 2m <= n_al - 3, mass y in [j - i - (E - e_d), j - i + (E - e_d)],
  n_an >= B - E + a* - 1; seed = hull over y), (QS*), (P2), (PIN) or an empty seed of a guaranteed weight; finisher (F2) of c6/proof-C0WB.md (B >= kB + 1,
  3kB + 1 <= p).
"""
# Supersedes seedLB2.py PART X only: anti-run availability uses a correct class/profile lower bound.
import sys, time, json, math
SRC = open('seedLB.py').read()
GUARD = "if __name__ == '__main__':\n    main()"
NSL = {'__name__': 'slblib'}
exec(compile(SRC.replace(GUARD, ''), 'c6/seedLB.py', 'exec'), NSL)
NS = NSL['NS']; NSX = NSL['NSX']
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
def route_S2(p, kB, B, shrink=0):
    n = p + kB; k = n + B; kappa = kB + B; A = n
    lam = lambda y, m: min(p - m + 1, y + m - kB, (y + B) // 2 + 1)
    lamc = lambda y, m: min(p - m + 1, A - kappa - y + m, (A - y) // 2 + 1)
    U = lambda y, m: p - lamc(y, m)
    cap = n - B - 4 - shrink
    best = {}
    for d in (1, -1):
        L1, U1 = lam(d, 1), U(d, 1)
        alo, bhi = NS['bounds'](p, k, kappa, B, d, 0)
        cand = []
        for j2 in range(0, max(cap, 0) // 3 + 1):
            for j1 in range(0, max(cap - 3 * j2, 0) // 2 + 1):
                m = j1 + j2
                if m < 1 or 2 * m + 2 > k: continue
                y = 2 * j2 + j1
                slo = lam(y + d, m + 1) - U(y, m); shi = U(y + d, m + 1) - lam(y, m)
                if not (L1 - shi > -p and U1 - slo < p): continue
                a, b = max(L1, slo), min(U1, shi)
                if a > b: return ('E', d, (y, m))
                if a >= alo and b <= bhi: cand.append((b - a, a, b, y, m, j2, j1))
        if not cand: return ('noS2', d, None)
        best[d] = min(cand)
    s = {d: (best[d][1], best[d][2]) for d in (1, -1)}
    for d1 in (1, -1):
        for d2 in (1, -1):
            for mm in (1, 2):
                y = d1 + d2
                if s[d1][0] + s[d2][0] < 1 - lamc(y, mm) or s[d1][1] + s[d2][1] > p + lam(y, mm) - 1: return ('P2fail', s, None)
    for d in (1, -1):
        if s[d][1] - lam(d, 1) > p - 1: return ('PINfail', s, None)
    return ('S2', {d: best[d][3:] for d in (1, -1)}, s)
def partL(PMAX, ctrl=False):
    grand = {}
    for p in [q for q in range(7, PMAX + 1) if isprime(q)]:
        cnt = {}; left = []; detail = []
        for kB in range(1, p):
            for B in range(2, p):
                if kB + B > p - 3 or 2 * B + kB < p - 1: continue
                kappa = kB + B; k = p + kappa
                r = NSL['route_SE'](p, kB, B, 2 if ctrl else 0)
                if r[0] in ('E', 'S'): key = r[0]
                else:
                    r2 = route_S2(p, kB, B, 6 if ctrl else 0)
                    if r2[0] in ('E', 'S2'): key = 'S2' if r2[0] == 'S2' else 'E2'
                    else:
                        rx = NS['class_pass'](p, k, kappa, B, 0) if not ctrl else 'skip'
                        key = 'X' if rx == 'pass' else 'open'
                        if key == 'open': left.append((k, B, kB))
                if p <= 11 and not ctrl: detail.append(((kB, B), key, r[1] if r[0] == 'S' else None))
                cnt[key] = cnt.get(key, 0) + 1
        for kk, v in cnt.items(): grand[kk] = grand.get(kk, 0) + v
        rec = {'p': p, 'counts': dict(sorted(cnt.items())), 'open (k, B, kB)': left}
        if detail: rec['detail'] = detail
        print(json.dumps(rec), flush=True)
    print(json.dumps({'totals': grand}), flush=True)
def partX():
    p, k, kappa, B = 31, 51, 24, 23
    R = 2 * p - k + 2 * kappa; A = R - B; E = R - k; kB = kappa - B
    lam = lambda y, m: min(p - m + 1, y + m - kB, (y + B) // 2 + 1)
    lamc = lambda y, m: min(p - m + 1, A - kappa - y + m, (A - y) // 2 + 1)
    U = lambda y, m: p - lamc(y, m)
    ex = lambda d: (d - 1) if d >= 1 else ((-d - 1) if d <= -1 else 1)
    prof = NSX['profiles'](p, k, kappa, B)
    res = {}
    for (n1, nal, a_, b_, hp) in prof:
        ean = nal - (k - B)
        nan_lo = B - E + a_ - 1  # n_an = B - (E - e_al), e_al >= a* - 1
        ws = list(range(1, a_ + 1)) + list(range(-b_, 0)) + ([0] if hp else [])
        guaranteed = [a_] + ([-b_] if b_ >= 1 else []) + ([0] if hp else [])
        live = {}; gempty = False; bad = None
        for d in ws:
            L1, U1 = lam(d, 1), U(d, 1); alo, bhi = NS['bounds'](p, k, kappa, B, d, 0)
            er = max(E - ex(d), 0); best = None; empty = False
            for m in range(1, (nal - 3) // 2 + 1):
                if 2 * m + 2 > k: break
                for i in range(0, min(m, max((nan_lo - 3) // 2, 0)) + 1):
                    j = m - i; lo = hi = None; ok = True
                    for y in range(j - i - er, j - i + er + 1):
                        if y < -B or y > A or y + d < -B or y + d > A: ok = False; break
                        slo = lam(y + d, m + 1) - U(y, m); shi = U(y + d, m + 1) - lam(y, m)
                        if not (L1 - shi > -p and U1 - slo < p): ok = False; break
                        lo = slo if lo is None else min(lo, slo); hi = shi if hi is None else max(hi, shi)
                    if not ok or lo is None: continue
                    a, b = max(L1, lo), min(U1, hi)
                    if a > b: empty = True; break
                    if a >= alo and b <= bhi and (best is None or b - a < best[1] - best[0]): best = (a, b)
                if empty: break
            if empty:
                if d in guaranteed: gempty = True
                continue
            if best is None: bad = d; break
            live[d] = best
        if gempty: key = 'guaranteed-empty'
        elif bad is not None: key = 'noseed'
        else:
            okp = all(not (ex(d1) + ex(d2) <= E and (s1[0] + s2[0] < 1 - lamc(d1 + d2, mm) or s1[1] + s2[1] > p + lam(d1 + d2, mm) - 1))
                      for d1, s1 in live.items() for d2, s2 in live.items() for mm in (1, 2))
            okp = okp and all(s[1] - lam(d, 1) <= p - 1 for d, s in live.items())
            key = 'ok' if okp else 'P2/PINfail'
        res[key] = res.get(key, 0) + 1
    f2 = B >= kB + 1 and 3 * kB + 1 <= p
    print(json.dumps({'class': [p, k, kappa, B], 'E': E, 'profiles': len(prof), 'outcomes': res, 'finisher F2 holds': f2}), flush=True)
def main():
    part = sys.argv[1]; PMAX = int(sys.argv[2])
    t0 = time.time()
    print('== seedLB3.py PART=%s PMAX=%d start %s' % (part, PMAX, time.strftime('%Y-%m-%dT%H:%M:%S')), flush=True)
    if part == 'L': partL(PMAX)
    elif part == 'C': partL(PMAX, ctrl=True)
    elif part == 'X': partX()
    print('== end %.1f s' % (time.time() - t0), flush=True)
if __name__ == '__main__':
    main()
