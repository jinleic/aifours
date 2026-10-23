# nobcplus.py -- c3 proof-NOBCplus.md: exact evaluation of the Lemma NOBC+ criterion rho(p + kB) - sigma < p + 1 for
# W(p, kB) (B = 1, all singletons), the lifting range 3kB <= p + 4 of Theorem W-ALL, the aligned-pair certification
# threshold, and the "doubly obstructed" range; cross-check against c2/out/nobc_bound.txt (type-count DP, B = 1 rows,
# p <= 31): every NOBC+ value must be marked NOBC there.  Exact rational arithmetic.  Aid only.
# Usage: python3 nobcplus.py PMAX
import sys, re
from fractions import Fraction as Fr
PMAX = int(sys.argv[1])
def h(j, kB): return min(2 * j - kB, (j + 1) // 2 + 1)
def h0(j, kB): return -kB if j == 0 else min(2 * j - kB, j // 2 + 1)
def rho(kB):
    # h(j)/j <= 1/2 + 3/(2j) for all j, and h(j0)/j0 > 1/2 at j0 = ceil((2kB+3)/3) + 1 or nearby; scanning j <= 4kB + 20 suffices
    return max(Fr(h(j, kB), j) for j in range(1, 4 * kB + 21))
def sigma(kB, r):
    return min(r * j0 - h0(j0, kB) for j0 in range(0, 4 * kB + 21))
def nobcplus(p, kB):
    r = rho(kB); return r * (p + kB) - sigma(kB, r) < p + 1
def lifting(p, kB): return 3 * kB <= p + 4
def aligned_pair_cert(p, kB):   # condition (A) for {s} -> {s, t}, t aligned (exact floor)
    lamQc = min(p, (p + kB - 2) // 2 + 1)   # complement of an aligned pair, m in {1, 2}: middle term >= p - 2 > floor term here
    return (2 - kB) + (2 - kB) + lamQc >= 1
primes = [q for q in range(11, PMAX + 1) if all(q % r for r in range(2, int(q ** 0.5) + 1))]
dp = {}
try:
    for line in open('../c2/out/nobc_bound.txt'):
        m = re.match(r'p=(\d+) (.*)', line)
        if not m: continue
        P = int(m.group(1))
        for tok in m.group(2).split():
            mm = re.match(r'k(\d+)/B1/kB(\d+):(\d+)(\*?)', tok)
            if mm: dp[(P, int(mm.group(2)))] = (mm.group(4) == '*')
except FileNotFoundError:
    pass
bad_cross = []
for p in primes:
    ks = range(1, p - 3)
    nob = [kB for kB in ks if nobcplus(p, kB)]
    lift = [kB for kB in ks if lifting(p, kB)]
    dbl = [kB for kB in nob if not lifting(p, kB)]
    nopair = [kB for kB in ks if not aligned_pair_cert(p, kB)]
    for kB in nob:
        if (p, kB) in dp and not dp[(p, kB)]: bad_cross.append((p, kB))
    print(p, 'NOBC+ kB:', (min(nob), max(nob)) if nob else None, 'contiguous:', nob == list(range(min(nob), max(nob) + 1)) if nob else True,
          '| W-ALL kB <=', max(lift), '| doubly obstructed kB:', (min(dbl), max(dbl)) if dbl else None, len(dbl),
          '| no aligned pair certified from kB =', min(nopair) if nopair else None, flush=True)
print({'primes': len(primes), 'cross_check_pairs': len([1 for key in dp if key[0] <= PMAX]), 'NOBC+_not_marked_in_c2_DP': bad_cross})
