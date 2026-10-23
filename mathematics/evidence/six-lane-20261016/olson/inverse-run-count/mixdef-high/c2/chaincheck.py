# chaincheck.py -- checks the certification steps used in proof-W4.md for W(p, 4) (k = p + 5, anti run at 0,
# aligned runs 1..p+4), for primes 11 <= p <= 199: (i) the interval chain I_1 c I_2 c ... c I_{p+4},
# I_i = {1..i}; (ii) one representative of each small pattern type used (pairs, anti pairs, triples, anti
# triples), each built by singleton extension; (iii) the range argument X_[k] = p.  Aid only.
def run(p):
    kB = 4; k = p + 5; B = 1; kappa = kB + 1; full = (1 << k) - 1
    def lam(Q):
        rot = ((Q << 1) | (Q >> (k - 1))) & full
        m = (Q & ~rot).bit_count(); e = Q & 1; j = Q.bit_count() - e; D = j - e
        return min(p - m + 1, D + B - kappa + m, (D + B) // 2 + 1)
    def step(Qp, t):
        Q = Qp | t
        return lam(Qp) + lam(t) + lam(full ^ Q) >= 1 and lam(Q) + lam(full ^ Qp) + lam(full ^ t) >= p + 1
    ok = True
    I = lambda i: sum(1 << s for s in range(1, i + 1))
    for i in range(1, p + 4): ok &= step(I(i), 1 << (i + 1))
    # small patterns: aligned non-adjacent pair {2,4}; anti pair {0,3}; triple {2,4,6}; anti triple {0,3,5}
    ok &= step(1 << 2, 1 << 4) and lam((1 << 2) | (1 << 4)) == 0
    ok &= step(1 << 3, 1 << 0) and lam(1 | (1 << 3)) == -2
    ok &= step((1 << 2) | (1 << 4), 1 << 6) and lam((1 << 2) | (1 << 4) | (1 << 6)) == 2
    ok &= step((1 << 3) | (1 << 5), 1 << 0) and lam(1 | (1 << 3) | (1 << 5)) == 0
    ok &= lam(1 << 2) == -2 and lam(1) == -4
    A = I(p + 4)
    lo = lam(A) + lam(1); hi = (p - lam(1)) + (p - lam(A))
    ok &= (0 < lo) and (hi < 2 * p)
    return ok, lam(A), lam(1), lo, hi
primes = [q for q in range(11, 200) if all(q % r for r in range(2, int(q ** 0.5) + 1))]
res = {p: run(p) for p in primes}
print('all ok:', all(v[0] for v in res.values()))
for p in primes[:6]: print(p, res[p])
print('failures:', [p for p, v in res.items() if not v[0]])
