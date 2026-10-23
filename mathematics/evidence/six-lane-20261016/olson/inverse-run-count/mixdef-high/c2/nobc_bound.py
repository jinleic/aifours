# nobc_bound.py -- type-count upper bound for Lemma BC condition (a) on all-singleton NMH words (R = k):
# k - B aligned singletons (d = +1), B anti singletons (d = -1), kappa = k - p, kB = kappa - B.
# For a part with j aligned and e anti singletons, lambda <= UB(j, e) := max over 1 <= m <= j + e of
#   min(p - m + 1, (j - e) + m - kB, floor((j - e + B)/2) + 1)   (m <= |P|; geometry ignored).
# MAXSUM = max over partitions of the multiset into >= 2 nonempty parts of sum UB.  If MAXSUM <= p, then no
# ordered partition satisfies Lemma BC (a), so the word has no Lemma BC certificate.  Aid only.
import sys
from functools import lru_cache
def run(p, B, k):
    kap = k - p; kB = kap - B
    def UB(j, e):
        best = None
        for m in range(1, j + e + 1):
            v = min(p - m + 1, (j - e) + m - kB, (j - e + B) // 2 + 1)
            best = v if best is None else max(best, v)
        return best
    NA, NB = k - B, B
    @lru_cache(maxsize=None)
    def f(ja, jb):   # max sum over partitions of (ja aligned, jb anti) into >= 1 nonempty parts
        if ja == 0 and jb == 0: return 0
        best = -10**9
        # choose the part containing the "first" remaining element: enumerate part types (x, y)
        for x in range(0, ja + 1):
            for y in range(0, jb + 1):
                if x + y == 0: continue
                best = max(best, UB(x, y) + f(ja - x, jb - y))
        return best
    # at least 2 parts: exclude the single part (NA, NB)
    best2 = -10**9
    for x in range(0, NA + 1):
        for y in range(0, NB + 1):
            if x + y == 0 or (x == NA and y == NB): continue
            best2 = max(best2, UB(x, y) + f(NA - x, NB - y))
    return kB, best2
for p in [5, 7, 11, 13, 17, 19, 23, 29, 31]:
    rows = []
    for k in range(p + 2, 2 * p - 2):          # R = k <= 2p - 3
        for B in range(1, k - p):              # kappa = k - p >= B + 1
            kB, ms = run(p, B, k)
            if kB < 1: continue
            if 2 * (k - p) > k - 3: continue   # R <= 2p - 3 <=> 2 kappa <= k - 3
            rows.append((k, B, kB, ms, 'NOBC' if ms <= p else ''))
    print('p=%d' % p, ' '.join('k%d/B%d/kB%d:%d%s' % (k, B, kB, ms, '*' if t else '') for (k, B, kB, ms, t) in rows))
