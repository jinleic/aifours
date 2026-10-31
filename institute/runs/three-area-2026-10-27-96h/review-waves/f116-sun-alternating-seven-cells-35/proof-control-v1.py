#!/usr/bin/env python3
"""proof-control-v1.py -- f116 reviewer-authored independent finite control.

Review: f116-sun-alternating-seven-cells-35 (same-harness scientific review).
Standard library only. Exact integers. Permutation groups by explicit closure.

POSITIVE controls must pass. NEGATIVE mutations deliberately falsify one step of
a written lemma and must be DETECTED (AssertionError). Exit status 0 only if every
positive control passes and every mutation is detected.

Scope: finite checks of the WRITTEN LEMMAS only --
  A. exact alternating-block quotient [A_n:H] = C(n,u)*[A_U:P]*c, c = u!/(h|L|) | u!,
     P transitive on U and containing the long cycle, and index preservation under
     transitive point-stabiliser descent -- on ACTUAL subgroups of A_8 / A_9 that
     contain a 5-cycle (small-degree analogue; the lemma is degree-independent);
  C. seven-cell counts, direct possible-prime counts, window divisibility
     (r+h)/gcd(r+h,u!) | C(r+j,u), 7-free no-cell windows, no-7p inequalities,
     the mod-15 possible-prime sieve, and a hypothesis-boundary witness;
  D. the elementary repunit-density count at X = 10^6;
  E. the effective per-t scope r >= 7*t! and the least eligible prime for each t.
They do NOT prove the general theorem, do NOT replay arXiv:2307.13976v2
Theorem 2(i)(d), and do NOT enumerate subgroups of any A_(r+t) with r >= 419.
Author scripts were neither imported nor executed.
"""
import os
import platform
import random
import sys
import time
from math import comb, factorial, gcd, isqrt

random.seed(116)
LINES = []


def say(s=''):
    print(s, flush=True)
    LINES.append(s)


# ------------------------------------------------------------------ permutations
def compose(p, q):
    """(p*q)(i) = p[q[i]]: apply q first, then p."""
    return tuple(p[i] for i in q)


def sign(p):
    n = len(p)
    seen = [False] * n
    s = 1
    for i in range(n):
        if not seen[i]:
            j = i
            length = 0
            while not seen[j]:
                seen[j] = True
                j = p[j]
                length += 1
            if length % 2 == 0:
                s = -s
    return s


def closure(gens, n):
    e = tuple(range(n))
    G = {e}
    frontier = [e]
    gens = [g for g in gens if g != e]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = compose(g, x)
                if y not in G:
                    G.add(y)
                    nxt.append(y)
        frontier = nxt
    return G


def orbit_of(gens, pt):
    seen = {pt}
    stack = [pt]
    while stack:
        x = stack.pop()
        for g in gens:
            y = g[x]
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return frozenset(seen)


def restrict(p, S):
    """Permutation of sorted(S) induced by p; requires p(S) = S."""
    order = sorted(S)
    idx = {x: i for i, x in enumerate(order)}
    return tuple(idx[p[x]] for x in order)


def cycle_perm(points, n):
    p = list(range(n))
    for a, b in zip(points, points[1:] + points[:1]):
        p[a] = b
    return tuple(p)


def random_even(n):
    while True:
        p = list(range(n))
        random.shuffle(p)
        p = tuple(p)
        if sign(p) == 1:
            return p


def random_block(U, V, n, even_each):
    """Random element of (S_U x S_V) n A_n, or of A_U x A_V when even_each."""
    U = sorted(U)
    V = sorted(V)
    while True:
        p = list(range(n))
        pu = U[:]
        random.shuffle(pu)
        for a, b in zip(U, pu):
            p[a] = b
        pv = V[:]
        random.shuffle(pv)
        for a, b in zip(V, pv):
            p[a] = b
        p = tuple(p)
        if even_each:
            if sign(restrict(p, U)) == 1 and sign(restrict(p, V)) == 1:
                return p
        elif sign(p) == 1:
            return p


# --------------------------------------------------------- Control A (actual groups)
def quotient_check(H, rho, n, mutate=None):
    """On an actual subgroup H <= A_n with rho in H (rho a long cycle whose support
    exceeds n/2), verify either
      transitive:   [A_n:H] = [A_(n-1):H_x] for a point x fixed by rho, or
      intransitive: [A_n:H] = C(n,u) * [A_U:P] * c with U the H-orbit of supp(rho),
                    V its complement (|V| = u), K = H n (A_U x A_V), h = [H:K] in {1,2},
                    P = pi_U(K), L = K n (1 x A_V), c = u!/(h|L|) | u!  (u >= 2), c = 1 (u = 1),
                    P transitive on U and rho|U in P."""
    gens = list(H)
    A_n = factorial(n) // 2
    assert A_n % len(H) == 0
    N = A_n // len(H)
    supp = [i for i in range(n) if rho[i] != i]
    U = orbit_of(gens, supp[0])
    if len(U) == n:
        x = next(i for i in range(n) if rho[i] == i)
        Hx = [g for g in H if g[x] == x]
        assert len(H) == n * len(Hx)
        A_prev = factorial(n - 1) // 2
        assert A_prev % len(Hx) == 0 and A_prev // len(Hx) == N
        return ('T', N)
    V = frozenset(range(n)) - U
    u, m = len(V), len(U)
    assert all(rho[i] == i for i in V)
    assert all(frozenset(g[i] for i in U) == U for g in H)
    K = [g for g in H if sign(restrict(g, U)) == 1]      # = H n (A_U x A_V) since g is even
    hh = len(H) // len(K)
    assert hh in (1, 2) and hh * len(K) == len(H)
    P = {restrict(k, U) for k in K}
    L = [k for k in K if all(k[i] == i for i in U)]
    assert len(K) == len(P) * len(L)
    assert len(orbit_of(list(P), 0)) == m                 # P transitive on U
    assert restrict(rho, U) in P                          # long cycle survives projection
    A_U = factorial(m) // 2
    if u == 1:
        assert hh == 1 and len(L) == 1
        c = 1
    else:
        A_V = factorial(u) // 2
        assert (2 * A_V) % (hh * len(L)) == 0
        c = (2 * A_V) // (hh * len(L))
        assert factorial(u) % c == 0
        if mutate == 'drop_2_over_h':
            c = A_V // len(L)
    assert A_U % len(P) == 0
    assert N == comb(n, u) * (A_U // len(P)) * c, (n, u, m, N, hh, len(L), c)
    return ('I', N, u, hh, len(L), c)


def control_A():
    say('== Control A: exact alternating-block quotient / transitive descent on ACTUAL subgroups')
    results = []
    sensitive = []          # (H, rho, n) with h = 1 and u >= 2: mutation-sensitive
    n = 8
    rho = cycle_perm([0, 1, 2, 3, 4], n)
    for _ in range(40):
        H = closure([rho, random_even(n)], n)
        res = quotient_check(H, rho, n)
        results.append((n, len(H), res))
    for u0 in (1, 2, 3):
        U0 = frozenset(range(n - u0))
        V0 = frozenset(range(n - u0, n))
        for even_each in (False, True):
            for _ in range(25):
                H = closure([rho, random_block(U0, V0, n, even_each),
                             random_block(U0, V0, n, even_each)], n)
                res = quotient_check(H, rho, n)
                results.append((n, len(H), res))
                if res[0] == 'I' and res[3] == 1 and res[2] >= 2:
                    sensitive.append((H, rho, n))
    n9 = 9
    rho9 = cycle_perm([0, 1, 2, 3, 4], n9)
    for u0 in (2, 4):
        U0 = frozenset(range(n9 - u0))
        V0 = frozenset(range(n9 - u0, n9))
        for even_each in (False, True):
            for _ in range(4):
                H = closure([rho9, random_block(U0, V0, n9, even_each),
                             random_block(U0, V0, n9, even_each)], n9)
                res = quotient_check(H, rho9, n9)
                results.append((n9, len(H), res))
                if res[0] == 'I' and res[3] == 1 and res[2] >= 2:
                    sensitive.append((H, rho9, n9))
    # deterministic witness: H = <rho> x <(5 6 7)> in A_8: U = supp(rho), u = 3, h = 1, |L| = 3, c = 2
    Hd = closure([rho, cycle_perm([5, 6, 7], n)], n)
    resd = quotient_check(Hd, rho, n)
    assert resd == ('I', 1344, 3, 1, 3, 2), resd
    results.append((n, len(Hd), resd))
    sensitive.append((Hd, rho, n))
    nT = sum(1 for _, _, r in results if r[0] == 'T')
    nI = sum(1 for _, _, r in results if r[0] == 'I')
    profile = {}
    for _, _, r in results:
        if r[0] == 'I':
            key = (r[2], r[3], r[4], r[5])
            profile[key] = profile.get(key, 0) + 1
    say(f'samples: {len(results)} actual subgroups (degree 8: {sum(1 for d,_,_ in results if d==8)}, '
        f'degree 9: {sum(1 for d,_,_ in results if d==9)}); transitive {nT}, intransitive {nI}; all PASS')
    say('intransitive profile (u, h=[H:K], |L|, c) -> count: ' +
        ', '.join(f'{k}:{v}' for k, v in sorted(profile.items())))
    say(f'deterministic witness <rho>x<(5 6 7)> in A_8: index 1344 = C(8,3)*[A_5:C_5]*c = 56*12*2, h=1, |L|=3: PASS')
    say(f'mutation-sensitive samples (h = 1, u >= 2): {len(sensitive)}')
    return sensitive


def mutation_A1(sensitive):
    """Drop the factor 2/h from c (i.e. use c' = |A_V|/|L| unconditionally)."""
    detected = 0
    for H, rho, n in sensitive:
        try:
            quotient_check(H, rho, n, mutate='drop_2_over_h')
        except AssertionError:
            detected += 1
    assert detected == len(sensitive), (detected, len(sensitive))
    say(f'mutation A1 (drop 2/h in c): detected on {detected}/{len(sensitive)} h=1,u>=2 samples: DETECTED')


# ----------------------------------------------------------------- arithmetic helpers
def sieve(limit):
    bs = bytearray([1]) * (limit + 1)
    bs[0] = bs[1] = 0
    for i in range(2, isqrt(limit) + 1):
        if bs[i]:
            bs[i * i::i] = bytearray(len(bs[i * i::i]))
    return bs


SMALL = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
MR_BOUND = 318665857834031151167461      # strong-pseudoprime bound for bases 2..37


def is_prime(n):
    if n < 2:
        return False
    for p in SMALL:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in SMALL:
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


def iroot(n, k):
    lo, hi = 1, 1 << ((n.bit_length() + k - 1) // k + 1)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** k <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo


def is_prime_power(q):
    if q < 2:
        return False
    for k in range(1, q.bit_length() + 1):
        p = iroot(q, k)
        if p < 2:
            break
        if p ** k == q and is_prime(p):
            return True
    return False


def repunit_form(r):
    """True iff r = (q^d-1)/(q-1) for some prime power q >= 2 and d >= 2."""
    if is_prime_power(r - 1):            # d = 2
        return True
    d = 3
    while (1 << d) - 1 <= r:
        lo, hi = 2, iroot(r, d - 1) + 1
        while lo <= hi:
            mid = (lo + hi) // 2
            val = (mid ** d - 1) // (mid - 1)
            if val == r:
                if is_prime_power(mid):
                    return True
                break
            if val < r:
                lo = mid + 1
            else:
                hi = mid - 1
        d += 1
    return False


# ---------------------------------------------------------------- Control C (arithmetic)
def control_C():
    say('== Control C: seven-cells, direct possible-prime counts, window divisibility, inequalities, sieve')
    LIM = 20000
    bs = sieve(LIM + 40)
    maxcells = 0
    maxprimes = 0
    arg = None
    nprimes = 0
    for r in range(419, LIM + 1):
        if not bs[r]:
            continue
        nprimes += 1
        for t in range(1, 36):
            cells = sum(1 for h in range(1, t + 1) if (r + h) % 7 == 0)
            assert cells <= 5
            cnt = sum(1 for q in range(r - 1, r + t + 1) if bs[q])
            assert cnt <= 10
            if cnt > maxprimes:
                maxprimes, arg = cnt, (r, t)
            maxcells = max(maxcells, cells)
    say(f'{nprimes} primes r in [419,{LIM}], all t<=35: max seven-cells = {maxcells} (<=5), '
        f'max ACTUAL primes in [r-1,r+t] = {maxprimes} (<=10) at (r,t)={arg}: PASS')
    for r in (419, 421, 431, 1009, 10007):
        for j in range(1, 36):
            for u in range(1, j + 1):
                W = range(j - u + 1, j + 1)
                B = comb(r + j, u)
                for h in W:
                    D = (r + h) // gcd(r + h, factorial(u))
                    assert B % D == 0
                if not any((r + h) % 7 == 0 for h in W):
                    assert u <= 6 and B % 7 != 0
    say('window divisibility (r+h)/gcd(r+h,u!) | C(r+j,u) for every h in the window, and '
        '7-free no-cell windows (u<=6): PASS for r in (419,421,431,1009,10007), all 1<=u<=j<=35')
    r = 419
    assert (r - 2) * (r - 3) > 7 * (r + 35) and comb(r + 1, 2) > 7 * (r + 35)
    assert factorial(r - 2) % (r + 1) == 0
    say(f'no-7p inequalities at r=419,t=35: (r-2)(r-3)={(r-2)*(r-3)} > 7(r+35)={7*(r+35)}; '
        f'C(r+1,2)={comb(r+1,2)} > {7*(r+35)}; (r+1) | (r-2)!: PASS')
    worst = 0
    for a in range(1, 15):
        if gcd(a, 15) != 1:
            continue
        for t in range(1, 36):
            E = t // 2
            upper = 1 + sum(1 for k in range(1, E + 1) if (a + 2 * k) % 3 and (a + 2 * k) % 5)
            worst = max(worst, upper)
    assert worst <= 10
    say(f'independent mod-15 sieve (1 + #odd offsets 2..2E coprime to 15), all 8 classes, t<=35: '
        f'worst = {worst} <= 10: PASS')
    rr, tt, hh = 419, 5, 1
    D = (rr + hh) // gcd(rr + hh, factorial(tt))
    say(f'hypothesis boundary witness: r=419, t=5, h=1: (r+h)/gcd(r+h,t!) = {D} (NOT > 7); '
        f'r+1 = {rr+1} = 7*5! exactly, so the hypothesis r+1 > 7t! fails here and the shared-cell step has no slack')
    return worst


def mutation_C1():
    """Pigeonhole beyond 35: claim <= 5 seven-cells for t in 36..41 (must fail at r=419, t=36)."""
    r = 419
    for t in range(36, 42):
        cells = sum(1 for h in range(1, t + 1) if (r + h) % 7 == 0)
        assert cells <= 5


def mutation_C2():
    """Weaken c | u! to c | (u+1)!: the 7-free conclusion for a no-cell window of length 6 must fail."""
    r, j, u = 419, 7, 6
    W = range(j - u + 1, j + 1)
    assert not any((r + h) % 7 == 0 for h in W)
    B = comb(r + j, u)
    for c in range(1, factorial(u + 1) + 1):
        if factorial(u + 1) % c == 0:
            assert (B * c) % 7 != 0


def mutation_C3(worst):
    """Tighten the sieve bound to 9 (must fail: 10 is attained)."""
    assert worst <= 9


# ---------------------------------------------------------------- Control D (density)
def control_D():
    say('== Control D: elementary repunit-density count at X = 10^6')
    X = 10 ** 6
    spf = list(range(X + 1))
    for i in range(2, isqrt(X) + 1):
        if spf[i] == i:
            for j in range(i * i, X + 1, i):
                if spf[j] == j:
                    spf[j] = i

    def prime_power_small(q):
        if q < 2:
            return False
        p = spf[q]
        while q % p == 0:
            q //= p
        return q == 1

    pi = sum(1 for n in range(2, X + 1) if spf[n] == n)
    bad = set()
    for q in range(2, X):
        if q + 1 <= X and spf[q + 1] == q + 1 and prime_power_small(q):
            bad.add(q + 1)
    for q in range(2, isqrt(X) + 2):
        if not prime_power_small(q):
            continue
        d = 3
        val = (q ** d - 1) // (q - 1)
        while val <= X:
            if spf[val] == val:
                bad.add(val)
            d += 1
            val = (q ** d - 1) // (q - 1)
    bound = X.bit_length() + isqrt(X) * (X + 1).bit_length()
    assert len(bad) <= bound
    big = sorted(p for p in bad if p >= 419)
    say(f'pi(10^6) = {pi}; repunit-form (bad) primes <= 10^6: {len(bad)}; ratio {len(bad)/pi:.6f}; '
        f'elementary pair bound {bound} >= {len(bad)}: PASS')
    say(f'bad primes in [419, 10^6]: {len(big)}; first 12: {big[:12]}; largest: {big[-1]}')
    for r in (419, 421, 431, 853):
        assert is_prime(r) and not repunit_form(r), r
    for r in (5, 7, 13, 17, 31, 257, 307, 65537):
        assert repunit_form(r), r
    say('eligibility helper agrees on 419, 421, 431, 853 (eligible) and 5, 7, 13, 17, 31, 257, 307, 65537 (repunit form): PASS')


# ---------------------------------------------------------------- Control E (scope)
def control_E():
    say('== Control E: effective scope per t  (r+1 > 7*t!  <=>  r >= 7*t!)')
    say('t | 7*t! | least eligible prime r >= max(419, 7*t!) | primality certification')
    for t in range(1, 36):
        T = 7 * factorial(t)
        r = max(419, T)
        while not (is_prime(r) and not repunit_form(r)):
            r += 1
        cert = 'deterministic (MR bases 2..37, n < 3.19e23)' if r < MR_BOUND else 'PROBABLE prime only (MR bases 2..37); NOT certified'
        say(f'{t} | {T} | {r} | {cert}')
    for r in (419, 421, 431, 853, 5003):
        ts = [t for t in range(1, 36) if r >= 7 * factorial(t)]
        say(f'fixed r={r}: hypothesis r+1 > 7*t! holds exactly for t in {ts}')


# ---------------------------------------------------------------------------- main
def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'proof-control-v1.txt')
    t0 = time.time()
    say(f'proof-control-v1.py start {time.strftime("%Y-%m-%dT%H:%M:%S%z")}  python {platform.python_version()}  {platform.platform()}')
    ok = False
    try:
        sensitive = control_A()
        worst = control_C()
        control_D()
        control_E()
        say('== Negative mutations (each must raise AssertionError)')
        mutation_A1(sensitive)
        for name, fn in (('C1 (pigeonhole claimed for t in 36..41 at r=419)', mutation_C1),
                         ('C2 (c | (u+1)! instead of c | u!, no-cell window u=6)', mutation_C2),
                         ('C3 (sieve bound tightened to 9)', lambda: mutation_C3(worst))):
            try:
                fn()
            except AssertionError:
                say(f'mutation {name}: DETECTED')
            else:
                raise AssertionError(f'mutation {name} NOT detected')
        ok = True
    finally:
        say(f'RESULT: {"ALL POSITIVE CONTROLS PASS, ALL MUTATIONS DETECTED" if ok else "FAILURE (see traceback)"}; '
            f'elapsed {time.time()-t0:.1f}s; end {time.strftime("%Y-%m-%dT%H:%M:%S%z")}')
        say('Finite controls only: no proof of the general theorem, no source replay, no subgroup enumeration at r >= 419.')
        with open(out, 'w') as f:
            f.write('\n'.join(LINES) + '\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
