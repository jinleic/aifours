#!/usr/bin/env python3
"""map6.py -- [F] exact CLASS-level map of RUNS item (iii) after W-ALL (c3), SEED (c5 r2/r3), SEED-B (c6 r2), IND* (c4) and
C/C+ (c3, c5/c6), task OlsonRunCount5 cycle 6 (parent request 2026-10-17 16:3x).
Item-(iii) parameter classes: p prime, k runs (p + 1 <= k <= 2p - 2), kappa, B with R = 2p - k + 2 kappa, k <= R <= 2p - 3,
E := R - k (excess, even), 1 <= B <= kappa - 1, B <= A = R - B <= 2p - 1; kB = kappa - B.  (Words of a class differ in the
run structure; ZSI-B words have k = p + 1 and kB = 1 and are not item (iii); such classes are marked.)
Classification of a class (first match):
  E = 0 (all single letters; then k = p + kappa):
    W     B = 1: c3 Theorem W-ALL (3kB <= p + 4) or c5 Theorem SEED (3kB >= p + 5)                       [W, uniform]
    SB    B >= 2, 2B + kB <= p - 2 and (5kB + B + 13 <= 3p or 2kB + 7B + 28 <= 4p): c6 Theorem SEED-B       [W, uniform]
    IS    otherwise, if the class-level hypotheses of Theorem IND* hold (c4/ind_star3.py 'covered')       [W + F per class]
    OPEN0 otherwise
  E >= 2 (some multi-letter run or (1,1)-pair):
    IE    the worst-case class-level hypotheses of Theorem IND* hold (c4/ind_star_ex.py 'covered')       [W + F per class]
    OPENE otherwise (individual words may still be excluded by Theorem C / C+ under (H) [W + F per word] or by IND* with
          their own T [W + F per word])
The functions 'covered' are taken verbatim from the frozen c4/ind_star3.py and c4/ind_star_ex.py (source lines exec'ed
read-only).  Usage: python3 map6.py PMAX
"""
import sys, time, json
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
s3 = open('../c4/ind_star3.py').read().splitlines()
g3 = {}
exec('\n'.join(s3[24:65]), g3)                     # isprime, fl, arcs, lift_range, check, covered (all-single-letter)
sx = open('../c4/ind_star_ex.py').read()
a = sx.index('def isprime'); b = sx.index("for fn, p in (('../c3/out/map3_p11.txt'")
gx = {}
exec(sx[a:b], gx)                                  # isprime, fl, arcs, covered (general classes, worst-case N)
def seedB_region(p, kB, B):
    return B >= 2 and kB >= 1 and 2 * B + kB <= p - 2 and (5 * kB + B + 13 <= 3 * p or 2 * kB + 7 * B + 28 <= 4 * p)
def classify(p, k, kappa, B):
    R = 2 * p - k + 2 * kappa; E = R - k; kB = kappa - B
    if E == 0:
        if B == 1: return 'W'
        if seedB_region(p, kB, B): return 'SB'
        return 'IS' if g3['covered'](p, k, B) else 'OPEN0'
    return 'IE' if gx['covered'](p, k, kB, B, E) else 'OPENE'
def main():
    PMAX = int(sys.argv[1])
    t0 = time.time()
    print('== map6.py PMAX=%d start %s' % (PMAX, time.strftime('%Y-%m-%dT%H:%M:%S')), flush=True)
    grand = {}
    for p in [q for q in range(11, PMAX + 1) if isprime(q)]:
        cnt = {}; open0 = []; openE = {}; zsi = 0
        for k in range(p + 1, 2 * p - 1):
            for kappa in range(max(k - p, 1), (k - 3) // 2 + 1):
                R = 2 * p - k + 2 * kappa
                if R < k or R > 2 * p - 3: continue
                for B in range(1, kappa):
                    A = R - B
                    if B > A or A > 2 * p - 1: continue
                    c = classify(p, k, kappa, B)
                    cnt[c] = cnt.get(c, 0) + 1
                    if k == p + 1 and kappa - B == 1: zsi += 1
                    if c == 'OPEN0': open0.append((k, B, kappa - B))
                    if c == 'OPENE':
                        E = R - k
                        openE[E] = openE.get(E, 0) + 1
        for c, v in cnt.items(): grand[c] = grand.get(c, 0) + v
        print(json.dumps({'p': p, 'classes': sum(cnt.values()), 'by_label': dict(sorted(cnt.items())), 'classes_with_k=p+1,kB=1(ZSI-B possible)': zsi,
                          'OPEN0 (k, B, kB)': open0, 'OPENE by excess E': dict(sorted(openE.items())), 't': round(time.time() - t0, 1)}), flush=True)
    print(json.dumps({'totals': dict(sorted(grand.items()))}), flush=True)
    print('== map6.py end %.1f s' % (time.time() - t0), flush=True)
if __name__ == '__main__':
    main()
