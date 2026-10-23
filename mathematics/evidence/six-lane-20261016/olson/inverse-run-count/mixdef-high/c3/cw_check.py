# cw_check.py -- c3 proof-WALL.md Lemma CW: type-level replay of conditions (A), (B) for every step type used in the
# proof of (a) (patterns with j aligned, e anti runs, m blocks, j + e <= kB + 1; an aligned end run removed, or an
# aligned singleton block when all blocks are single runs) and for every step I_i -> I_{i+1} of (b), with the exact
# lambda formulas (0.1), (0.2).  For every prime 5 <= p <= PMAX and 1 <= kB <= p - 4 report whether all hold, and
# compare with the predicate 3kB <= p + 4.  Aid only.  Usage: python3 cw_check.py PMAX
import sys
PMAX = int(sys.argv[1])
def lam(p, kB, j, e, m):          # (0.1)
    y = j - e
    return min(p - m + 1, y + m - kB, (y + 1) // 2 + 1)
def lamc(p, kB, j, e, m):         # (0.2): complement of a (j, e, m) pattern
    y = j - e
    return min(p - m + 1, p - 1 - y + m, (p + kB - y) // 2 + 1)
def step(p, kB, jp, ep, mp, j, e, m):   # Q' = (jp, ep, mp) -> Q = (j, e, m), added run t aligned
    lt = 2 - kB; ltc = (p + kB - 1) // 2 + 1
    A = lam(p, kB, jp, ep, mp) + lt + lamc(p, kB, j, e, m) >= 1
    Bc = lam(p, kB, j, e, m) + lamc(p, kB, jp, ep, mp) + ltc >= p + 1
    return A and Bc
def check(p, kB):
    k = p + 1 + kB
    assert 2 - kB == lam(p, kB, 1, 0, 1) and (p + kB - 1) // 2 + 1 == lamc(p, kB, 1, 0, 1)
    for e in (0, 1):
        for j in range(1, kB + 2 - e):
            if j + e < 2: continue
            for m in range(1, j + e + 1):
                if m > k - (j + e): continue
                if m < j + e:
                    if not step(p, kB, j - 1, e, m, j, e, m): return False, ('a', j, e, m)
                else:
                    if not step(p, kB, j - 1, e, m - 1, j, e, m): return False, ('a', j, e, m)
    for i in range(1, p + kB):
        if not step(p, kB, i, 0, 1, i + 1, 0, 1): return False, ('b', i)
    L0 = lam(p, kB, p + kB, 0, 1); assert L0 == (p + kB + 1) // 2 + 1
    if not (L0 - kB >= 1): return False, ('pin',)
    return True, None
primes = [q for q in range(5, PMAX + 1) if all(q % r for r in range(2, int(q ** 0.5) + 1))]
mism = []; ncases = 0
for p in primes:
    good = []
    for kB in range(1, p - 3):
        ncases += 1
        ok, why = check(p, kB)
        if ok: good.append(kB)
        if ok != (3 * kB <= p + 4): mism.append((p, kB, ok, why))
    print(p, 'all steps hold for kB in', (min(good), max(good)) if good else None, ' predicate max =', min(p - 4, (p + 4) // 3), flush=True)
print({'primes': len(primes), 'cases': ncases, 'mismatches_with_3kB_le_p_plus_4': mism[:10], 'n_mismatch': len(mism)})
