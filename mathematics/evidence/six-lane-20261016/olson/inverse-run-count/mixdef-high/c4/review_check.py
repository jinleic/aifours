# review_check.py -- c4 README Sec. 3 P1 (T1, T2).  Exact integer arithmetic; aid only ([F]).
# (1) For every prime 11 <= p <= PMAX: DOB(p) (c3/proof-NOBCplus.md: 3kB >= p + 5 and rho(p + kB) - sigma < p + 1),
#     NOLIFT(a)/(b) evaluated EXACTLY from lambda (anti pair / aligned pairs, adjacent and non-adjacent), and
#     DOB*(p) := {kB in DOB(p) : no aligned pair certified}; reports DOB(p) - DOB*(p) and checks it equals
#     {(p+5)/3} if p = 1 (mod 6) and (p+5)/3 in DOB(p), else empty.
# (2) For every prime p = 1 (mod 6), 13 <= p <= PMAX, kB0 = (p+5)/3: the certification steps of the generalised
#     W(19, 8) argument on the TYPE level (lambda depends only on (y = D_Q, m = m(Q))):
#     aligned pairs; anti triples {0,s,t} by adjoining the anti singleton to the aligned pair {s,t} (all (m', m));
#     CW-type induction for all patterns with 3 <= |Q| <= kB0 + 1 (remove an aligned end of a block with >= 2 runs,
#     m' = m, else an aligned singleton block, m' = m - 1; anti triples by the anti adjoin route);
#     pin pair P = {0,2,4}, P^c built as {1}, {1,3}, {1,3,5}, {1,3,5,6}, ..., {1,3,5,...,n} (n = p + kB0).
# Usage: python3 -B review_check.py PMAX
import sys
from fractions import Fraction as Fr
PMAX = int(sys.argv[1])
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
def lam(p, kB, y, m):           # lambda of a proper pattern of W(p,kB) with D_Q = y, m blocks (B = 1)
    return min(p - m + 1, y + m - kB, (y + 1) // 2 + 1)
def lamc(p, kB, y, m):          # lambda of its complement (D = p + kB - 1 - y, same m)
    return lam(p, kB, p + kB - 1 - y, m)
def h(j, kB): return min(2 * j - kB, (j + 1) // 2 + 1)
def h0(j, kB): return -kB if j == 0 else min(2 * j - kB, j // 2 + 1)
def rho(kB): return max(Fr(h(j, kB), j) for j in range(1, 4 * kB + 21))
def sigma(kB, r): return min(r * j0 - h0(j0, kB) for j0 in range(0, 4 * kB + 21))
def nobcplus(p, kB): r = rho(kB); return r * (p + kB) - sigma(kB, r) < p + 1
def step_ok(p, kB, yq1, mq1, yt, mt, y, m):
    """(A), (B) of Lemma L for Q = Q' u {t}: Q' = (yq1, mq1), {t} = (yt, mt = 1), Q = (y, m). Returns (A-slack, B-slack)."""
    A = lam(p, kB, yq1, mq1) + lam(p, kB, yt, mt) + lamc(p, kB, y, m) - 1
    Bv = lam(p, kB, y, m) + lamc(p, kB, yq1, mq1) + lamc(p, kB, yt, mt) - (p + 1)
    return A, Bv
def aligned_pairs_cert(p, kB):
    # {s} -> {s,t}: non-adjacent (m = 2) and adjacent (m = 1)
    return all(min(step_ok(p, kB, 1, 1, 1, 1, 2, m)) >= 0 for m in (1, 2))
def anti_pairs_cert(p, kB):
    # {v} -> {0, v} (equivalently {0} -> {0, v}): y = 0, m = 2 (non-adjacent) or 1 (adjacent)
    return [min(step_ok(p, kB, 1, 1, -1, 1, 0, m)) >= 0 for m in (1, 2)]
out = []
bad = []
for p in range(11, PMAX + 1):
    if not isprime(p): continue
    ks = range(1, p - 3)
    dob = [kB for kB in ks if 3 * kB >= p + 5 and nobcplus(p, kB)]
    dobstar = [kB for kB in dob if not aligned_pairs_cert(p, kB)]
    diff = [kB for kB in dob if kB not in dobstar]
    exp = [(p + 5) // 3] if (p % 6 == 1 and (p + 5) // 3 in dob) else []
    if diff != exp: bad.append(('DOB-DOB*', p, diff, exp))
    # NOLIFT exact vs the closed forms of c3/proof-NOBCplus.md Sec. 2
    for kB in ks:
        a_closed = 3 * kB >= p + 5
        b_closed = (3 * kB >= p + 7) if kB % 2 else (3 * kB >= p + 6)
        anti = anti_pairs_cert(p, kB)
        if a_closed != (not anti[1]): bad.append(('NOLIFT(a) non-adjacent', p, kB))
        if b_closed != (not aligned_pairs_cert(p, kB)): bad.append(('NOLIFT(b)', p, kB))
    beyond = [kB for kB in ks if 3 * kB >= p + 5]
    pairs_beyond = [kB for kB in beyond if aligned_pairs_cert(p, kB)]
    out.append((p, (min(dob), max(dob)) if dob else None, len(dob), diff, pairs_beyond))
for row in out:
    print('p=%d DOB=%s |DOB|=%d DOB-DOB*=%s | beyond-W-ALL kB with aligned pairs certified: %s' % row)
print({'checks': 'DOB-DOB* closed form and NOLIFT closed forms', 'mismatches': bad})
# (2) generalised W(19,8) certification, type level
res = []
for p in range(13, PMAX + 1):
    if not isprime(p) or p % 6 != 1: continue
    kB = (p + 5) // 3
    if kB > p - 4: continue
    n = p + kB; k = n + 1
    worst = {}
    def rec(name, A, Bv):
        w = worst.get(name, (10 ** 9, 10 ** 9)); worst[name] = (min(w[0], A), min(w[1], Bv))
    # aligned pairs
    for m in (1, 2): rec('aligned pair', *step_ok(p, kB, 1, 1, 1, 1, 2, m))
    # anti triples via {s,t} -> {0,s,t}: (m', m) in {(1,1),(1,2),(2,1),(2,2),(2,3)}; t = anti run: y_t = -1
    for (mq1, m) in ((1, 1), (1, 2), (2, 1), (2, 2), (2, 3)):
        rec('anti triple', *step_ok(p, kB, 2, mq1, -1, 1, 1, m))
    # CW-type induction, sizes 3..kB+1 (e = 0: y = j; e = 1: y = j - 1, size j + 1); skip anti triples (done above)
    for size in range(3, kB + 2):
        for e in (0, 1):
            j = size - e; y = j - e
            for m in range(1, size + 1):
                if m > k - size: continue            # complement needs >= m runs
                if e == 1 and size == 3: continue      # anti triples: anti adjoin route
                if m < size:                            # some block has >= 2 runs: remove an aligned end, m' = m
                    rec('CW size %d' % size if size <= 4 else 'CW size>=5', *step_ok(p, kB, y - 1, m, 1, 1, y, m))
                else:                                   # all blocks singletons: remove an aligned singleton, m' = m - 1
                    if m - 1 >= 1:
                        rec('CW size %d' % size if size <= 4 else 'CW size>=5', *step_ok(p, kB, y - 1, m - 1, 1, 1, y, m))
    # pin pair: P = {0,2,4} (y = 1, m = 3) via {2,4} -> {0,2,4}
    rec('pin P', *step_ok(p, kB, 2, 2, -1, 1, 1, 3))
    # P^c chain: Q1 = {1} (1,1); Q2 = {1,3} (2,2); Q3 = {1,3,5} (3,3); Q_i = {1,3,5,6,..,i+2} (i, 3) for i >= 4, up to i = n - 2
    rec('P^c chain', *step_ok(p, kB, 1, 1, 1, 1, 2, 2))
    rec('P^c chain', *step_ok(p, kB, 2, 2, 1, 1, 3, 3))
    for i in range(4, n - 1):
        rec('P^c chain', *step_ok(p, kB, i - 1, 3, 1, 1, i, 3))
    pin = lam(p, kB, 1, 3) + lamc(p, kB, 1, 3)
    ok = all(min(v) >= 0 for v in worst.values()) and pin >= 1
    res.append((p, kB, ok, pin, worst))
    if not ok: bad.append(('kB0 cert', p, kB, worst, pin))
for p, kB, ok, pin, worst in res:
    print('p=%d kB0=%d ok=%s lambda(P)+lambda(P^c)=%d min slacks (A-1, B-(p+1)): %s' % (p, kB, ok, pin, worst))
print({'kB0_primes_checked': len(res), 'failures': [b for b in bad if b[0] == 'kB0 cert']})
