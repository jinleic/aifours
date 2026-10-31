#!/usr/bin/env python3
"""f134 reviewer-written exact integer controls (independent structure; NOT the author's checker).

Usage: python3 reviewer-arith-controls-v1.py OUTPUT_LOG
Every line is PASS/FAIL (positive control) or NEG-OK/NEG-FAIL (negative control: the candidate's
inequality or conclusion is EXPECTED to break exactly where its hypothesis is violated).
Exit status 0 iff no FAIL and no NEG-FAIL.
"""
import sys, time, datetime
from math import comb, gcd, factorial


class Tee:
    def __init__(self, path):
        self.f = open(path, "w")
    def __call__(self, s=""):
        print(s)
        self.f.write(s + "\n")
        self.f.flush()


out = Tee(sys.argv[1])
BAD = 0


def pos(tag, ok, detail):
    global BAD
    if not ok:
        BAD += 1
    out(f"[{tag}] {'PASS' if ok else 'FAIL'}: {detail}")


def neg(tag, violated, detail):
    """violated=True means the candidate's inequality/conclusion fails here, as expected."""
    global BAD
    if not violated:
        BAD += 1
    out(f"[{tag}] {'NEG-OK' if violated else 'NEG-FAIL'}: {detail}")


def is_prime(n):
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in small:  # deterministic Miller-Rabin for n < 3.3e24
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def max_clique(vertices, compatible):
    """Exact maximum clique (Bron-Kerbosch with pivot) on an explicit compatibility predicate."""
    adj = {v: {w for w in vertices if w != v and compatible(v, w)} for v in vertices}
    best = []

    def bk(R, P, X):
        nonlocal best
        if not P and not X:
            if len(R) > len(best):
                best = list(R)
            return
        if len(R) + len(P) <= len(best):
            return
        u = max(P | X, key=lambda v: len(adj[v] & P))
        for v in list(P - adj[u]):
            bk(R + [v], P & adj[v], X & adj[v])
            P.remove(v)
            X.add(v)

    bk([], set(vertices), set())
    return sorted(best)


out(f"reviewer-arith-controls-v1 start {datetime.datetime.now(datetime.timezone.utc).isoformat()}")
t0 = time.time()

# ---------------------------------------------------------------- C1: binomial pair lemma (Section 2)
pairs = 0
ok_all = True
for n in range(5, 201):
    for i in range(3, n):
        if 2 * i >= n:
            break
        A = comb(n, i)
        if A <= 7:
            ok_all = False
            out(f"  C1 witness: C({n},{i})={A} <= 7")
        for j in range(i + 1, n):
            if 2 * j >= n:
                break
            B = comb(n, j)
            g = gcd(A, B)
            cji = comb(j, i)
            pairs += 1
            ident = A * comb(n - i, j - i) == B * cji
            divis = cji % (A // g) == 0
            ratio = n ** i > 8 * j ** i          # (n/j)^i > 8 exactly
            strong = A > 8 * cji                 # A/C(j,i) > 8 hence > 7
            big = g > 7
            if not (ident and divis and ratio and strong and big):
                ok_all = False
                out(f"  C1 witness: n={n} i={i} j={j} ident={ident} divis={divis} ratio={ratio} strong={strong} gcd={g}")
pos("C1", ok_all, f"{pairs} pairs 3<=i<j<n/2, n<=200: identity, (A/g)|C(j,i), (n/j)^i>8, A>8*C(j,i), gcd>7, C(n,i)>7 all hold")

# ---------------------------------------------------------------- C2: NEGATIVE controls, j >= n/2 (hypothesis violated)
ineq_fail, concl_fail = [], []
for n in range(5, 41):
    for i in range(3, n):
        for j in range(i + 1, n):
            if 2 * j < n:
                continue  # hypothesis satisfied; not a negative case
            A, B, cji = comb(n, i), comb(n, j), comb(j, i)
            if A <= 7 * cji:
                ineq_fail.append((n, i, j, A, 7 * cji))
            if gcd(A, B) <= 7:
                concl_fail.append((n, i, j, A, B, gcd(A, B)))
neg("C2a", len(ineq_fail) > 0, f"{len(ineq_fail)} triples with 2j>=n where A<=7*C(j,i); first: {ineq_fail[:4]}")
neg("C2b", len(concl_fail) > 0, f"{len(concl_fail)} triples with 2j>=n where gcd(C(n,i),C(n,j))<=7: {concl_fail}")
neg("C2c", gcd(comb(6, 3), comb(6, 4)) == 5 and comb(6, 3) < 7 * comb(4, 3),
    f"explicit: n=6,i=3,j=4 (j>=n/2): C(6,3)=20 < 7*C(4,3)=28 and gcd(20,15)={gcd(20,15)}<=7")
# i<3 hypothesis violated: n=14 with (i,j)=(1,2)
neg("C2d", gcd(comb(14, 1), comb(14, 2)) == 7, f"i=1<3: gcd(C(14,1),C(14,2))=gcd(14,91)={gcd(14, 91)} <= 7 (lemma conclusion fails)")

# ---------------------------------------------------------------- C4: gcd(n, C(n,2)) (Section 3 u in {1,2})
ok_all = True
tbl = []
for n in range(5, 61):
    g = gcd(n, comb(n, 2))
    expect = n if n % 2 else n // 2
    tbl.append((n, g))
    if g != expect:
        ok_all = False
pos("C4a", ok_all, "gcd(n,C(n,2)) == n (n odd) or n/2 (n even) for 5<=n<=60")
pos("C4b", all(g > 7 for n, g in tbl if n >= 15), "gcd(n,C(n,2)) > 7 for all 15<=n<=60")
neg("C4c", dict(tbl)[14] == 7, f"n=14: gcd(14,91)={dict(tbl)[14]} is NOT > 7 (the candidate's n>=15 hypothesis is necessary at n=14)")
out("  C4 table n:gcd for 10..20 = " + ", ".join(f"{n}:{g}" for n, g in tbl if 10 <= n <= 20))

# ---------------------------------------------------------------- C5: n=14 explicit labels
L14 = [comb(14, u) for u in (1, 2, 3)]
pos("C5a", L14 == [14, 91, 364], f"n=14 labels C(14,1..3) = {L14}")
pos("C5b", gcd(14, 364) > 7 and gcd(91, 364) > 7 and gcd(14, 91) == 7,
    f"gcd(14,364)={gcd(14, 364)}, gcd(91,364)={gcd(91, 364)} >7; gcd(14,91)={gcd(14, 91)} (u=1,u=2 may coexist)")
cl = max_clique(L14 + [11], lambda a, b: gcd(a, b) <= 7)
pos("C5c", len(cl) == 3, f"max pairwise-gcd<=7 clique over labels {{14,91,364,11}} = {cl} (size {len(cl)}; bound 3 holds and is label-tight)")

# ---------------------------------------------------------------- C6: n=15,16 with r=11
for n in (15, 16):
    r, t = 11, n - 11
    labels = [comb(n, u) for u in range(1, t + 1)]
    grpA = labels[:2]
    grpB = labels[2:]
    a_ok = gcd(grpA[0], grpA[1]) > 7 and all(x > 7 for x in grpA)
    b_ok = all(gcd(x, y) > 7 for k, x in enumerate(grpB) for y in grpB[k + 1:]) and all(x > 7 for x in grpB)
    cl = max_clique(labels + [r], lambda a, b: gcd(a, b) <= 7)
    pos(f"C6-n{n}", is_prime(r) and 2 * r > n and t >= 3 and a_ok and b_ok and len(cl) <= 3,
        f"r=11 prime, t={t}>=3; labels={labels}; {{u=1,2}} pairwise>7: {a_ok}; {{u>=3}} pairwise>7: {b_ok}; max gcd<=7 clique={cl} (size {len(cl)})")

# ---------------------------------------------------------------- C7: Section 4 prime choices for 14<=n<=5000 (Bertrand verified numerically in range only)
NMAX = 5000
sieve = bytearray([1]) * (2 * NMAX + 2)
sieve[0] = sieve[1] = 0
for p in range(2, int((2 * NMAX + 1) ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = bytearray(len(sieve[p * p::p]))
primes = [p for p in range(2 * NMAX + 2) if sieve[p]]
ok_all = True
branch_counts = {"explicit11": 0, "odd_t>=3": 0, "odd_t=2": 0, "even_composite": 0, "even_halfprime": 0}
odd_t2_cases = []
for n in range(14, NMAX + 1):
    if n in (14, 15, 16):
        r = 11
        t = n - r
        if not (sieve[r] and 2 * r > n and t >= 3 and r > 7):
            ok_all = False
            out(f"  C7 witness n={n}: explicit r=11 fails")
        branch_counts["explicit11"] += 1
        continue
    if n % 2:
        m = (n - 1) // 2
        cands = [p for p in primes if m < p < 2 * m]
        if not cands or m < 8:
            ok_all = False
            out(f"  C7 witness n={n}: no Bertrand prime in ({m},{2*m}) or m<8")
        for r in cands:
            t = n - r
            if not (2 * r > n and r > 7 and t >= 2 and t % 2 == 0):
                ok_all = False
                out(f"  C7 witness n={n} r={r}: Section 4 odd-case conditions fail")
            if t >= 3:
                branch_counts["odd_t>=3"] += 1
                if not (gcd(n, comb(n, 2)) > 7 and n >= 15):
                    ok_all = False
                    out(f"  C7 witness n={n}: u1/u2 share fails")
            else:
                branch_counts["odd_t=2"] += 1
                # Section 5: intransitive labels n, C(n,2) both multiples of n>7
                if not (comb(n, 2) % n == 0 and n > 7):
                    ok_all = False
                    out(f"  C7 witness n={n}: Section 5 intransitive labels not multiples of n")
                q = r + 1
                if q & (q - 1) == 0:  # q is a power of two: Mersenne prime r, Jones PGL/PGammaL cases live
                    e = q.bit_length() - 1
                    a = (q + 1) // 3
                    ok_j = (is_prime(e) and e >= 5 and e % 2 == 1 and (q + 1) % 3 == 0 and a > e and a <= q - 2
                            and len({2, 3, e, a}) == 4 and factorial(q - 2) % (2 * e * (q + 1)) == 0
                            and all((factorial(q - 2) // (2 * d)) % (q + 1) == 0 for d in (1, e)))
                    odd_t2_cases.append((n, r, e, ok_j))
                    if not ok_j:
                        ok_all = False
                        out(f"  C7 witness n={n}: Jones/Mersenne divisibility fails")
    else:
        m = n // 2
        if sieve[m]:
            r = m
            idxM = comb(2 * r, r) // 2
            if not (r >= 11 and comb(2 * r, r) % 2 == 0 and idxM >= n and n > 7):
                ok_all = False
                out(f"  C7 witness n={n}: half-prime case fails")
            branch_counts["even_halfprime"] += 1
        else:
            cands = [p for p in primes if m - 1 < p < 2 * m - 2]
            if not cands or m - 1 < 2:
                ok_all = False
                out(f"  C7 witness n={n}: no Bertrand prime in ({m-1},{2*m-2})")
            for r in cands:
                t = n - r
                if not (2 * r > n and r > 7 and t >= 3 and gcd(n, comb(n, 2)) > 7):
                    ok_all = False
                    out(f"  C7 witness n={n} r={r}: even composite case fails")
            branch_counts["even_composite"] += 1
pos("C7", ok_all, f"Section 4/5 branch conditions hold for every admissible prime, 14<=n<={NMAX}; branches={branch_counts}; Mersenne t=2 cases in range (n,r,e,ok)={odd_t2_cases}")

# ---------------------------------------------------------------- C8: Jones t=2 Mersenne divisibility (Section 5)
for e in (5, 7, 13, 17, 19, 31, 61):
    q = 2 ** e
    r = q - 1
    n = q + 1
    a = n // 3
    structural = (is_prime(e) and is_prime(r) and e % 2 == 1 and e >= 5 and n % 3 == 0 and a > e and a <= q - 2
                  and len({2, 3, e, a}) == 4 and 2 * 3 * e * a == 2 * e * n)
    detail = f"e={e} q={q} r={r} prime={is_prime(r)} n={n} a={a}: 2,3,e,a distinct<=q-2 so 2e(q+1)|(q-2)!"
    if e <= 19:
        t1 = time.time()
        F = factorial(q - 2)
        direct = all((F // (2 * d)) % n == 0 and F % (2 * d) == 0 for d in (1, e))
        detail += f"; direct (q-2)!/(2d) mod n == 0 for d in (1,e): {direct} [{time.time()-t1:.1f}s]"
        structural = structural and direct
    pos(f"C8-e{e}", structural, detail)
# orders divide |A_n| for the two smallest cases (Lagrange sanity only)
for e in (5, 7):
    q = 2 ** e
    n = q + 1
    pos(f"C8-lagrange-e{e}", all((factorial(n) // 2) % (q * (q * q - 1) * d) == 0 for d in (1, e)),
        f"q(q^2-1)d divides |A_{n}| for d in (1,{e})")

# ---------------------------------------------------------------- C9: NEGATIVE controls for Section 5 (r>7 / e>=5 violated)
q, e, n = 8, 3, 9
I_pgl, I_pgammal = factorial(q - 2) // 2, factorial(q - 2) // (2 * e)
neg("C9a", I_pgammal % n != 0 and I_pgl % n == 0,
    f"e=3 (r=7, excluded by r>7): (q-2)!/(2e)={I_pgammal} mod 9 = {I_pgammal % n} != 0 while (q-2)!/2={I_pgl} mod 9 = {I_pgl % n}; the e>=5 hypothesis is necessary")
neg("C9b", (2 ** 3 + 1) // 3 == 3 and not ((2 ** 3 + 1) // 3 > 3), "e=3: a=(q+1)/3=3 is not > e=3, so 2,3,e,a are not distinct")

# ---------------------------------------------------------------- C10: even half-prime overgroup index
ok_all = True
for r in [p for p in primes if 11 <= p <= 500]:
    idxM = comb(2 * r, r) // 2
    if not (comb(2 * r, r) % 2 == 0 and idxM >= 2 * r and idxM > 7 and comb(2 * r, r) % r != 0):
        ok_all = False
        out(f"  C10 witness r={r}")
pos("C10", ok_all, "[A_2r : (S_r wr S_2) cap A_2r] = C(2r,r)/2 is an integer >= 2r > 7 and r-free, for primes 11<=r<=500")

# ---------------------------------------------------------------- C11: small table n=5..13 and boundary n=14..17
def divisors(N):
    ds = [1]
    m = N
    p = 2
    fac = []
    while p * p <= m:
        if m % p == 0:
            k = 0
            while m % p == 0:
                m //= p
                k += 1
            fac.append((p, k))
        p += 1
    if m > 1:
        fac.append((m, 1))
    for p, k in fac:
        ds = [d * p ** j for d in ds for j in range(k + 1)]
    return sorted(ds), fac


table_bound = {5: 0, 6: 0, 7: 4, 8: 4, 9: 4, 10: 4, 11: 5, 12: 5, 13: 6}
for n in range(5, 18):
    An = factorial(n) // 2
    ds, fac = divisors(An)
    v7 = dict(fac).get(7, 0)
    non7 = [p for p, _ in fac if p != 7]
    sevens = [d for d in ds if d % 7 == 0]
    cl_all = max_clique([d for d in sevens if d > 1], lambda a, b: gcd(a, b) == 7)
    cl_idx = max_clique([d for d in sevens if d >= n], lambda a, b: gcd(a, b) == 7)
    line = (f"n={n}: |A_n|={An}, v7={v7}, non-7 primes={non7}; max DISTINCT divisor set with pairwise gcd exactly 7: "
            f"size {len(cl_all)} {cl_all} (d>1), size {len(cl_idx)} {cl_idx} (d>=n)")
    if n <= 13:
        pos(f"C11-n{n}", v7 <= 1 and len(cl_all) == table_bound[n] and len(cl_all) < 7 and (v7 == 0 or len(non7) == table_bound[n] - 1),
            line + f"; table bound {table_bound[n]} reproduced exactly")
    elif n <= 16:
        neg(f"C11-n{n}", v7 == 2 and len(cl_all) >= 7 and len(cl_idx) == 6,
            line + "; the elementary bound fails for d>1 (seven values) but still gives 6 under index>=n")
    else:
        neg(f"C11-n{n}", len(cl_idx) >= 7, line + "; elementary bound fails even with index>=n (so Sections 3-5 are needed)")

# ---------------------------------------------------------------- C12: multiset / repeated index 7 at n=7 (arithmetic part only)
pos("C12a", gcd(7, 7) == 7 and all(gcd(a, b) == 7 for a in [7] * 7 for b in [7] * 7),
    "seven copies of the index 7 have every pairwise gcd exactly 7 (the candidate's 'at most one a_i is 1' needs DISTINCT values)")
from fractions import Fraction
dens = 6 * Fraction(1, 7) + Fraction(1, 21) + Fraction(1, 35)
pos("C12b", dens < 1, f"index multiset (7x6,21,35) has coset density {dens} < 1; arithmetic alone does not exclude it")
pos("C12c", (factorial(7) // 2) % 7 == 0 and (factorial(7) // 2) % 49 != 0 and all((factorial(n) // 2) % 7 != 0 for n in (5, 6)),
    "7 || |A_7|; 7 does not divide |A_5|, |A_6|")

# ---------------------------------------------------------------- C13: A5 witness arithmetic
idx = (5, 6, 15, 20)
g6 = [gcd(a, b) for k, a in enumerate(idx) for b in idx[k + 1:]]
pos("C13a", g6 == [1, 5, 5, 3, 2, 5] and all(g <= 7 for g in g6), f"pairwise gcds of {idx} = {g6} (all <= 7, order (5,6),(5,15),(5,20),(6,15),(6,20),(15,20))")
pos("C13b", all(60 % i == 0 for i in idx), "all four indices divide |A_5|=60")
neg("C13c", gcd(10, 20) > 7, f"adding index 10 breaks the <=7 condition: gcd(10,20)={gcd(10, 20)}")

out(f"SUMMARY: {'ALL CONTROLS AS EXPECTED' if BAD == 0 else str(BAD) + ' UNEXPECTED RESULT(S)'}; elapsed {time.time()-t0:.1f}s; end {datetime.datetime.now(datetime.timezone.utc).isoformat()}")
sys.exit(0 if BAD == 0 else 1)
