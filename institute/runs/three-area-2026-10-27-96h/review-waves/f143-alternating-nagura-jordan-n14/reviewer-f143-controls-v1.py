#!/usr/bin/env python3
"""reviewer-f143-controls-v1.py

Independent same-harness reviewer controls for review wave
f143-alternating-nagura-jordan-n14 (candidate
frontier-20261028-alternating-nagura-jordan-v1.md, SHA256
521a823bd2d27618cde002b72c742f7bb12116985f0ae2bc3d501545c8738d6a).

Authored by the reviewer. No author code is imported or executed. The only
author DATA parsed is the 36-degree markdown table (read from the frozen file
after an in-script hash check) so it can be compared with the reviewer's own
literal transcription.

Nothing here proves Nagura (1952) or Jordan/Jones Thm 1.1. Bounded numeric
checks of the imported Nagura statement are consistency controls only.
All arithmetic is exact Python integers / Fractions.
"""
import hashlib
import os
import subprocess
import sys
import time
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, gcd

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "reviewer-f143-controls-v1.log")
CAND = ("/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/"
        "parallel-18/sun-coset8/frontier-20261028-alternating-nagura-jordan-v1.md")
CAND_SHA = "521a823bd2d27618cde002b72c742f7bb12116985f0ae2bc3d501545c8738d6a"

LINES = []
FAILS = []


def log(s=""):
    LINES.append(str(s))
    print(s)


def check(cond, msg):
    if cond:
        log("  ok   " + msg)
    else:
        FAILS.append(msg)
        log("  FAIL " + msg)
    return cond


def clock():
    return subprocess.run(["/bin/date", "-u", "+%Y-%m-%dT%H:%M:%SZ"],
                          capture_output=True, text=True).stdout.strip()


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def sieve(N):
    s = bytearray([1]) * (N + 1)
    s[0] = s[1] = 0
    i = 2
    while i * i <= N:
        if s[i]:
            s[i * i::i] = bytearray(len(range(i * i, N + 1, i)))
        i += 1
    return s


def legendre(n, p):
    v, q = 0, p
    while q <= n:
        v += n // q
        q *= p
    return v


def parity(perm):
    """0 even / 1 odd for a permutation given as a tuple of images of 0..k-1."""
    seen = [False] * len(perm)
    par = 0
    for i in range(len(perm)):
        if not seen[i]:
            j, L = i, 0
            while not seen[j]:
                seen[j] = True
                j = perm[j]
                L += 1
            par ^= (L - 1) & 1
    return par


def compose(p, q):
    """(p*q)(x) = p(q(x))."""
    return tuple(p[q[x]] for x in range(len(q)))


def closure(gens, n):
    ident = tuple(range(n))
    group = {ident}
    frontier = [ident]
    gens = list(gens)
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                x = compose(h, g)
                if x not in group:
                    group.add(x)
                    new.append(x)
        frontier = new
    return group


log("reviewer-f143-controls-v1  start " + clock())
log("python " + sys.version.split()[0])

# ----------------------------------------------------------------------------
log("\n== C0: candidate hash recheck before parsing its table ==")
with open(CAND, "rb") as fh:
    data = fh.read()
sha = hashlib.sha256(data).hexdigest()
check(sha == CAND_SHA, "candidate SHA256 == %s" % CAND_SHA)
check(len(data) == 7999 and data.count(b"\n") == 71, "candidate bytes=7999 LF=71")

# ----------------------------------------------------------------------------
log("\n== C1: 36-degree prime table n=14..49 ==")
# Reviewer's literal transcription of the candidate's table (row-major as displayed).
TRANSCRIBED = {
    14: 11, 26: 17, 38: 23,
    15: 11, 27: 17, 39: 23,
    16: 11, 28: 17, 40: 23,
    17: 11, 29: 17, 41: 23,
    18: 11, 30: 17, 42: 23,
    19: 11, 31: 17, 43: 23,
    20: 11, 32: 17, 44: 23,
    21: 11, 33: 17, 45: 23,
    22: 13, 34: 19, 46: 29,
    23: 13, 35: 19, 47: 29,
    24: 13, 36: 19, 48: 29,
    25: 13, 37: 19, 49: 29,
}
# Parse the table out of the frozen candidate text (data, not code).
parsed = {}
for ln in data.decode("utf-8").splitlines():
    if ln.startswith("|") and ln.count("|") == 7:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if all(c.isdigit() for c in cells):
            for k in range(0, 6, 2):
                parsed[int(cells[k])] = int(cells[k + 1])
check(parsed == TRANSCRIBED, "parsed table equals reviewer transcription (%d entries)" % len(parsed))
check(sorted(parsed) == list(range(14, 50)), "table covers every n in 14..49 exactly once")
allok = True
for n in range(14, 50):
    r = TRANSCRIBED[n]
    t = n - r
    conds = (is_prime(r), 2 * r > n, r > 8, t >= 3, r > t, legendre(n, r) == 1)
    if not all(conds):
        allok = False
        log("  BAD n=%d r=%d conds=%s" % (n, r, conds))
check(allok, "every table entry: r prime, 2r>n, r>8, t=n-r>=3, r>t, v_r(n!)=1")
check(all(is_prime(p) for p in (11, 13, 17, 19, 23, 29)), "the six displayed primes are prime (trial division)")
# Independent: list ALL admissible primes per n and show the table value is among them;
# negative control: for n<=13 the admissible set {prime r: 2r>n, r>8, n-r>=3} is empty.
log("  admissible prime sets (r prime, 2r>n, r>8, n-r>=3):")
for n in range(5, 50):
    adm = [r for r in range(9, n - 2) if is_prime(r) and 2 * r > n]
    if n <= 13:
        check(adm == [], "n=%d admissible set empty (explains threshold n>=14)" % n)
    else:
        check(TRANSCRIBED[n] in adm, "n=%d table r=%d in admissible %s" % (n, TRANSCRIBED[n], adm))

# ----------------------------------------------------------------------------
log("\n== C2: bounded consistency of the imported Nagura statement ==")
M = 2_000_000
S = sieve(int(6 * M / 5) + 10)
nextprime = [0] * (len(S) + 1)
nxt = 0
for i in range(len(S) - 1, -1, -1):
    if S[i]:
        nxt = i
    nextprime[i] = nxt
# positive: for every integer m in [25, M] there is a prime p with m<p and 5p<6m
bad = [m for m in range(25, M + 1) if not (nextprime[m + 1] and 5 * nextprime[m + 1] < 6 * m)]
check(bad == [], "integer m in [25, %d]: prime p with m<p<6m/5 exists (first failures: %s)" % (M, bad[:5]))
# negative: list m<25 with NO prime in the open interval (m,6m/5)
fails_small = [m for m in range(1, 25) if not (nextprime[m + 1] and 5 * nextprime[m + 1] < 6 * m)]
log("  m<25 with no prime in (m,6m/5): %s" % fails_small)
check(24 in fails_small and max(fails_small) == 24, "m=24 fails and is the largest failure (Nagura a_5=25 sharp)")
# derived chain for n>=50 in a bounded range: m=floor(n/2), r=next prime > m
chain_ok = True
for n in range(50, 2 * M + 1):
    m = n // 2
    r = nextprime[m + 1]
    if not (5 * r < 6 * m and 2 * r > n and n - r >= 21 and r > n - r and r > 8 and legendre(n, r) == 1):
        chain_ok = False
        log("  BAD chain n=%d m=%d r=%d" % (n, m, r))
        break
check(chain_ok, "n in [50, %d]: Nagura prime r gives 2r>n, t=n-r>=21, r>t, r>8, v_r(n!)=1" % (2 * M))

# ----------------------------------------------------------------------------
log("\n== C3: binomial gcd collision, 3<=i<=j<n/2, exact integers ==")
NMAX = 400      # full-range exact gcd>=9 check (integers only)
NBOUND = 80     # range for the identity / divisibility / product-bound verification (Fractions)
worst = None
ok3 = True
for n in range(14, NMAX + 1):
    jmax = (n - 1) // 2  # j < n/2
    binom = [comb(n, u) for u in range(jmax + 1)]
    for j in range(3, jmax + 1):
        for i in range(3, j + 1):
            g = gcd(binom[i], binom[j])
            if g < 9:
                ok3 = False
                log("  BAD n=%d i=%d j=%d g=%d" % (n, i, j, g))
            if worst is None or g < worst[0]:
                worst = (g, n, i, j)
check(ok3, "all 3<=i<=j<n/2, 14<=n<=%d: gcd(C(n,i),C(n,j)) >= 9" % NMAX)
log("  smallest gcd over the range: g=%d at (n,i,j)=(%d,%d,%d)" % worst)
okb = True
for n in range(14, NBOUND + 1):
    jmax = (n - 1) // 2
    for j in range(3, jmax + 1):
        for i in range(3, j):
            A, B = comb(n, i), comb(n, j)
            g = gcd(A, B)
            ident = A * comb(n - i, j - i) == B * comb(j, i)
            div = comb(j, i) % (A // g) == 0
            prod = Fraction(1)
            for h in range(i):
                prod *= Fraction(n - h, j - h)
            bound = (g >= prod) and (prod >= Fraction(n, j) ** i) and (Fraction(n, j) ** i > 2 ** i) and (2 ** i >= 8)
            if not (ident and div and bound):
                okb = False
                log("  BAD n=%d i=%d j=%d g=%d ident=%s div=%s bound=%s" % (n, i, j, g, ident, div, bound))
check(okb, "3<=i<j<n/2, 14<=n<=%d: identity C(n,i)C(n-i,j-i)=C(n,j)C(j,i); (A/g)|C(j,i); g>=prod>=(n/j)^i>2^i>=8" % NBOUND)
# negative control: with i<3 the bound can fail; enumerate every (n,i,j) with gcd<=8
low = []
for n in range(14, NMAX + 1):
    jmax = (n - 1) // 2
    for j in range(1, jmax + 1):
        for i in range(1, j + 1):
            if i < 3:
                g = gcd(comb(n, i), comb(n, j))
                if g <= 8:
                    low.append((n, i, j, g))
log("  (n,i,j,gcd) with gcd<=8 and i<3, 14<=n<=%d: count=%d" % (NMAX, len(low)))
log("  those with i=2: %s" % [x for x in low if x[1] == 2])
log("  those with i=1 and n<=20: %s" % [x for x in low if x[1] == 1 and x[0] <= 20])
log("  (info, over-broad u-range) collisions with i=2: %s" % [x for x in low if x[1] == 2])
check([x for x in low if x[2] == 2] == [(14, 1, 2, 7), (16, 1, 2, 8)],
      "u=1 vs u=2 collisions <=8 for n>=14 are exactly n=14 (7) and n=16 (8)")
# restricted to the proof's actual range u<=t=n-r (table r), u=2 never collides <=8 with any u>=3
okr = True
for n in range(14, 50):
    t = n - TRANSCRIBED[n]
    for j in range(3, t + 1):
        if gcd(comb(n, 2), comb(n, j)) <= 8:
            okr = False
            log("  BAD restricted n=%d t=%d j=%d" % (n, t, j))
check(okr, "n=14..49 within u<=t=n-r: u=2 vs u>=3 never <=8 (the n=16 (2,6) collision has u=6>t=5)")
check(comb(16, 6) % 11 == 0 and 16 - 11 == 5, "C(16,6)=8008 is 11-divisible: u=6 is unreachable for an 11-free index at n=16")
# gcd(n, C(n,2)) formula
okf = True
for n in range(14, NMAX + 1):
    g = gcd(n, comb(n, 2))
    exp = n if n % 2 else n // 2
    if g != exp or ((g > 8) != (n not in (14, 16))):
        okf = False
        log("  BAD gcd(n,C(n,2)) n=%d g=%d" % (n, g))
check(okf, "gcd(n,C(n,2)) = n (odd) / n/2 (even); >8 iff n not in {14,16}, for 14<=n<=%d" % NMAX)
check(comb(14, 3) == 364 and all(comb(n, u) >= 364 for n in range(14, NMAX + 1) for u in range(3, (n - 1) // 2 + 1)),
      "C(n,u) >= 364 for 3<=u<n/2, n>=14 (same-type u>=3 collision)")
check(all(comb(n, u) >= n >= 14 for n in range(14, NMAX + 1) for u in range(1, (n - 1) // 2 + 1)),
      "C(n,u) >= n >= 14 > 8 for every 1<=u<n/2 (repeated same-type indices collide)")

# ----------------------------------------------------------------------------
log("\n== C4: maximum pairwise-compatible set of u-types at threshold 8 (upward clique search) ==")


def max_clique(n, umax):
    us = list(range(1, umax + 1))
    compat = {(a, b): gcd(comb(n, a), comb(n, b)) <= 8 for a in us for b in us if a < b}
    best = (1, (us[0],)) if us else (0, ())
    for k in range(2, len(us) + 1):
        found = None
        for sub in combinations(us, k):
            if all(compat[(a, b)] for a, b in combinations(sub, 2)):
                found = sub
                break
        if found is None:
            return best
        best = (k, found)
    return best


def smallest_prime_above(x):
    r = x + 1
    while not is_prime(r):
        r += 1
    return r


C4MAX = 160
ok4 = True
for n in range(14, C4MAX + 1):
    r = TRANSCRIBED[n] if n <= 49 else smallest_prime_above(n // 2)
    t = n - r
    k, sub = max_clique(n, t)
    if k > 2:
        ok4 = False
        log("  BAD n=%d r=%d t=%d clique %s" % (n, r, t, sub))
check(ok4, "14<=n<=%d, u<=t=n-r (table r / smallest prime > n/2): at most 2 u-types pairwise gcd<=8" % C4MAX)
for n in (14, 16):
    r = TRANSCRIBED[n]
    k, sub = max_clique(n, n - r)
    log("  n=%d r=%d t=%d max compatible set size %d e.g. %s" % (n, r, n - r, k, sub))
k16, sub16 = max_clique(16, 7)
log("  info: n=16 WITHOUT the u<=t restriction (u<=7): size %d e.g. %s -> u<=t is load-bearing at n=16" % (k16, sub16))
log("  negative control n<14 (u<=(n-1)//2):")
for n in range(5, 14):
    k, sub = max_clique(n, (n - 1) // 2)
    log("    n=%d max compatible u-set size %d e.g. %s" % (n, k, sub))
check(max_clique(7, 3)[0] == 3, "n=7: u-types {1,2,3} (7,21,35) pairwise gcd 7<=8 -> size 3")

# ----------------------------------------------------------------------------
log("\n== C5: exceptional degrees n=14 (t=3) and n=16 (t=5), full gcd matrices ==")
for n, t in ((14, 3), (16, 5)):
    vals = [comb(n, u) for u in range(1, t + 1)]
    log("  n=%d factors %s" % (n, vals))
    for a in range(t):
        log("    gcd row u=%d: %s" % (a + 1, [gcd(vals[a], vals[b]) for b in range(t)]))
check([comb(14, u) for u in (1, 2, 3)] == [14, 91, 364], "n=14 factors 14,91,364")
check((gcd(14, 91), gcd(14, 364), gcd(91, 364)) == (7, 14, 91), "n=14 gcds 7,14,91 as displayed")
check([comb(16, u) for u in range(1, 6)] == [16, 120, 560, 1820, 4368], "n=16 factors 16,120,560,1820,4368")
check(gcd(16, 120) == 8 and (gcd(120, 560), gcd(120, 1820), gcd(120, 4368)) == (40, 20, 24), "n=16 displayed gcds 8;40,20,24")
log("  note: gcd(16,1820)=%d (u=1,u=4 compatible; not displayed by the candidate, harmless)" % gcd(16, 1820))
check(max_clique(14, 3)[0] == 2 and max_clique(16, 5)[0] == 2, "n=14,16 restricted to u<=t: max compatible set size 2")
# alternative r=13 at n=16 (t=3) also works
check(max_clique(16, 3)[0] == 2 and is_prime(13) and 26 > 16 and 16 - 13 >= 3, "n=16 with r=13,t=3 would also give <=2")

# ----------------------------------------------------------------------------
log("\n== C6: order-r elements of S_n are r-cycles when n<2r (partition enumeration) ==")


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for p in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest


from math import lcm as _lcm
ok6 = True
for n in range(14, 50):
    r = TRANSCRIBED[n]
    for part in partitions(n):
        L = 1
        for p in part:
            L = _lcm(L, p)
        if L % r == 0:
            if part.count(r) != 1 or any(p % r == 0 and p != r for p in part):
                ok6 = False
                log("  BAD n=%d r=%d part=%s" % (n, r, part))
        if L == r and part != (r,) + (1,) * (n - r):
            ok6 = False
            log("  BAD order-r non-cycle n=%d part=%s" % (n, part))
check(ok6, "n=14..49 with table r: every cycle type of order divisible by r has exactly one r-part; order exactly r <=> (r,1^(n-r))")
check(all((TRANSCRIBED[n] % 2 == 1) for n in range(14, 50)), "table r odd => r-cycle is even (lies in A_n)")

# ----------------------------------------------------------------------------
log("\n== C7: block systems: every nontrivial block size b and block count k satisfy b<r and k<r ==")
ok7 = True
for n in range(14, 50):
    r = TRANSCRIBED[n]
    for b in range(2, n):
        if n % b == 0:
            k = n // b
            if not (b < r and k < r and b <= n // 2 and k <= n // 2):
                ok7 = False
                log("  BAD n=%d r=%d b=%d k=%d" % (n, r, b, k))
check(ok7, "n=14..49: all nontrivial (b,k) have b<=n/2<r and k<=n/2<r")

# ----------------------------------------------------------------------------
log("\n== C8: A_n is transitive on u-subsets (BFS with A_n generators), n=14 u<=3 and n=16 u<=5 ==")


def an_gens(n):
    c3 = list(range(n)); c3[0], c3[1], c3[2] = 1, 2, 0
    if n % 2 == 1:
        cyc = [(i + 1) % n for i in range(n)]
    else:
        cyc = [0] + [1 + ((i) % (n - 1)) for i in range(1, n)]  # (1 2 ... n-1) fixing 0
    return [tuple(c3), tuple(cyc)]


ok8 = True
for n, t in ((14, 3), (16, 5)):
    gens = an_gens(n)
    assert all(parity(g) == 0 for g in gens)
    for u in range(1, t + 1):
        start = frozenset(range(u))
        seen = {start}
        fr = [start]
        while fr:
            nf = []
            for s in fr:
                for g in gens:
                    img = frozenset(g[x] for x in s)
                    if img not in seen:
                        seen.add(img)
                        nf.append(img)
            fr = nf
        if len(seen) != comb(n, u):
            ok8 = False
            log("  BAD n=%d u=%d orbit %d != C(n,u) %d" % (n, u, len(seen), comb(n, u)))
check(ok8, "orbit of a u-set under <A_n generators> has size C(n,u) for n=14 (u<=3), n=16 (u<=5)")

# ----------------------------------------------------------------------------
log("\n== C9: small-n countercontrol in the actual group A_7 (pure-Python enumeration) ==")
n = 7
A7 = {p for p in permutations(range(7)) if parity(p) == 0}
check(len(A7) == 2520, "|A_7| = 2520")
# H1: point stabiliser of 0
H1 = {p for p in A7 if p[0] == 0}
# H2: GL(3,2) acting on the 7 nonzero vectors of F_2^3 (vectors 1..7 as bitmasks -> points 0..6)
H2 = set()
for c1 in range(1, 8):
    for c2 in range(1, 8):
        if c2 == c1:
            continue
        for c3 in range(1, 8):
            if c3 in (c1, c2, c1 ^ c2):
                continue
            img = []
            for v in range(1, 8):
                w = (c1 if v & 1 else 0) ^ (c2 if v & 2 else 0) ^ (c3 if v & 4 else 0)
                img.append(w - 1)
            H2.add(tuple(img))
# H3: setwise stabiliser of {5,6}; H4: setwise stabiliser of {4,5,6}
H3 = {p for p in A7 if {p[5], p[6]} == {5, 6}}
H4 = {p for p in A7 if {p[4], p[5], p[6]} == {4, 5, 6}}


def is_subgroup(H):
    ident = tuple(range(7))
    if ident not in H:
        return False
    hl = list(H)
    for a in hl:
        for b in hl[:40]:
            if compose(a, b) not in H:
                return False
    return closure(hl[:6], 7) <= H and len(closure(hl, 7)) == len(H)


for name, H, order in (("H1=Stab(pt)", H1, 360), ("H2=GL(3,2)", H2, 168), ("H3=Stab(2-set)", H3, 120), ("H4=Stab(3-set)", H4, 72)):
    check(len(H) == order and H <= A7 and is_subgroup(H), "%s: subgroup of A_7 of order %d, index %d" % (name, order, 2520 // order))
idx = [2520 // len(H) for H in (H1, H2, H3, H4)]
pg = [gcd(a, b) for a, b in combinations(idx, 2)]
log("  indices %s pairwise gcds %s" % (idx, pg))
check(idx == [7, 15, 21, 35] and max(pg) == 7, "A_7 has FOUR DISTINCT proper subgroups with all pairwise index gcd <= 7 < 9 (four-index statement fails at n=7)")
# overlay A7 counterexample replay: seven cosets {g: g(i)=0}, i=0..6
cos = [frozenset(p for p in A7 if p[i] == 0) for i in range(7)]
stabs = [frozenset(p for p in A7 if p[i] == i) for i in range(7)]
ok9 = all(len(c) == 360 for c in cos)
ok9 &= all(cos[a].isdisjoint(cos[b]) for a, b in combinations(range(7), 2))
ok9 &= (frozenset().union(*cos) == frozenset(A7))
for i in range(7):
    gi = next(iter(cos[i]))
    left = frozenset(compose(gi, h) for h in stabs[i])
    ok9 &= (left == cos[i]) and len(stabs[i]) == 360 and (2520 // 360 == 7)
check(ok9, "overlay replay: seven left cosets g_i Stab(i) of index-7 subgroups partition A_7 (pairwise gcd 7)")

# ----------------------------------------------------------------------------
log("\n== C10: sample of genuine A_14 subgroup indices: any four contain a pair with gcd>=9 ==")
n = 14
A14 = comb(14, 7) * 7 * 6 * 5 * 4 * 3 * 2 * 1 * 5040 // 2  # 14!/2
from math import factorial
assert A14 == factorial(14) // 2
sample = {}
for u in range(1, 8):
    sample["Stab(%d-set)" % u] = comb(14, u)
for k in range(2, 13):
    sample["A_%d pointwise" % (14 - k)] = factorial(14) // factorial(14 - k)  # [A_14 : A_{14-k}], 14-k>=2
sample["(S7 wr S2)^+"] = factorial(14) // (factorial(7) ** 2 * 2)
sample["(S2 wr S7)^+"] = factorial(14) // (2 ** 7 * factorial(7))
sample["N(11-cycle)^+"] = A14 // 330
sample["trivial"] = A14
vals = list(sample.items())
worst10 = None
for quad in combinations(vals, 4):
    mx = max(gcd(a[1], b[1]) for a, b in combinations(quad, 2))
    if worst10 is None or mx < worst10[0]:
        worst10 = (mx, [q[0] for q in quad])
log("  sample size %d; minimum over 4-subsets of (max pairwise gcd) = %d at %s" % (len(vals), worst10[0], worst10[1]))
check(worst10[0] >= 9, "no four sampled genuine indices of A_14 have all pairwise gcd <= 8 (sanity, not a proof)")
check(all((v % 11 == 0) or any(v % comb(14, u) == 0 for u in (1, 2, 3)) for v in sample.values()),
      "every sampled index is 11-divisible or a multiple of 14, 91 or 364 (consistent with Section 3 at n=14)")

# ----------------------------------------------------------------------------
log("\n== summary ==")
log("failures: %d" % len(FAILS))
for f in FAILS:
    log("  " + f)
log("end " + clock())
with open(LOG, "w") as fh:
    fh.write("\n".join(LINES) + "\n")
print("log written:", LOG)
sys.exit(1 if FAILS else 0)
