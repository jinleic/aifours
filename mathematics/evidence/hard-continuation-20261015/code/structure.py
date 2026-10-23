#!/usr/bin/env python3
"""Finite checks accompanying proofs/FORCED-SUBGROUP.md (math-p0039 continuation).

1. <2> mod P_a = 4^a + 2^a + 1 has order 3a and is a Sidon set for 1 <= a <= A,
   with a = 2 the only failure (P_2 = 21).
2. T_s = {2^i w^k : 0 <= i < s, k = 0,1,2} is a Sidon set in Z[w] (exhaustive, s <= S).
3. The Z[w] facts used in the proof: coordinates of (N - w)E' for the twelve E' of
   norm 1 or 3, and the coordinate bound 2N that kills every norm-3 orbit.
4. Desarguesian shadow for a = 3, 9: a Singer planar difference set of PG(2, 2^a) in
   Z/P contains <2>; for a = 9 it meets mu_(n+1) exactly in <2>.
5. Forced-subgroup tests: n = 512 (n = 8 mod 24) passes every collision test inside
   K = <2, divisors of n, mu_3> and every lemma-5 non-membership test, so its known
   exclusion needs non-forced elements; n = 24, 90 fail inside K (positive controls).
Negative control: --broken replaces P_a by P_a + 2 for a = 9 and must exit 1.
"""
import argparse
import json
import sys
import time


def need(ok, message):
    if not ok:
        raise ValueError(message)


def sidon_mod(a, P=None):
    N = 1 << a
    P = P or N * N + N + 1
    S = [pow(2, i, P) for i in range(3 * a)]
    need(pow(2, 3 * a, P) == 1, 'order relation')
    seen = {}
    for i in range(len(S)):
        for j in range(i, len(S)):
            s = (S[i] + S[j]) % P
            if s in seen:
                return dict(distinct=len(set(S)) == 3 * a, sidon=False, witness=[seen[s], [i, j]])
            seen[s] = [i, j]
    return dict(distinct=len(set(S)) == 3 * a, sidon=True)


def sidon_char0(s):
    # 2^i w^k as (A, B) with A + B w;  w^2 = -1 - w
    T = [((1 << i), 0) for i in range(s)] + [(0, 1 << i) for i in range(s)] + \
        [(-(1 << i), -(1 << i)) for i in range(s)]
    sums = set()
    for i in range(len(T)):
        for j in range(i, len(T)):
            key = (T[i][0] + T[j][0], T[i][1] + T[j][1])
            need(key not in sums, 'characteristic-0 Sidon relation at s=%d' % s)
            sums.add(key)
    return len(T)


def coordinates():
    """(N - w)(x + y w) = (N x + y) + ((N + 1) y - x) w for the 12 elements of norm 1, 3."""
    small = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1),            # units
             (1, -1), (-1, 1), (1, 2), (-1, -2), (2, 1), (-2, -1)]           # norm 3
    norm = lambda x, y: x * x - x * y + y * y
    need(sorted(norm(*e) for e in small) == [1] * 6 + [3] * 6, 'norms')
    rows = []
    for a in range(3, 41):
        N = 1 << a
        for x, y in small:
            A, B = N * x + y, (N + 1) * y - x
            # direct product check in Z[w]: (N - w)(x + y w) = N x + (N y - x) w - y w^2
            A2, B2 = N * x + y, N * y - x + y
            need((A, B) == (A2, B2), 'coordinate formula')
            rows.append((a, x, y, max(abs(A), abs(B)) > 2 * N))
    killed = sorted({(x, y) for a, x, y, big in rows if big})
    need(killed == [(-2, -1), (-1, -2), (1, 2), (2, 1)], 'unexpected out-of-bound set %s' % killed)
    return dict(out_of_bound_elements=killed, note='each mu_6-orbit of norm-3 elements contains one of these')


# ------------------------------------------------------------ GF(2^d) Singer set ---

def mulmod(x, y, poly, deg):
    r = 0
    while y:
        if y & 1:
            r ^= x
        y >>= 1
        x <<= 1
        if x >> deg & 1:
            x ^= poly
    return r


def powmod(x, e, poly, deg):
    r = 1
    while e:
        if e & 1:
            r = mulmod(r, x, poly, deg)
        x = mulmod(x, x, poly, deg)
        e >>= 1
    return r


def irreducible(deg):
    """Smallest irreducible polynomial of degree deg = 3^m over GF(2) (Rabin's test)."""
    divisors = [deg // 3] if deg % 3 == 0 else []
    for low in range(1, 1 << deg, 2):
        poly = 1 << deg | low
        y, xs = 2, {}
        for k in range(1, deg + 1):
            y = mulmod(y, y, poly, deg)
            xs[k] = y
        if xs[deg] != 2:
            continue
        ok = True
        for k in divisors:  # x^(2^k) - x must be coprime to poly: gcd over GF(2)
            g, h = poly, xs[k] ^ 2
            while h:
                while g.bit_length() >= h.bit_length() and g:
                    g ^= h << (g.bit_length() - h.bit_length())
                g, h = h, g
            ok = ok and g == 1
        if ok:
            return poly


def factors(m):
    out, d = [], 2
    while d * d <= m:
        while m % d == 0:
            out.append(d)
            m //= d
        d += 1
    if m > 1:
        out.append(m)
    return sorted(set(out))


def singer_shadow(a):
    q, deg = 1 << a, 3 * a
    P, n = q * q + q + 1, q
    poly = irreducible(deg)
    order = (1 << deg) - 1
    primes = factors(order)
    tr = lambda x: x ^ powmod(x, q, poly, deg) ^ powmod(x, q * q, poly, deg)
    theta = next(t for t in range(2, 1 << deg)
                 if tr(t) == 0 and all(powmod(t, order // r, poly, deg) != 1 for r in primes))
    th_q, th_q2 = powmod(theta, q, poly, deg), powmod(theta, q * q, poly, deg)
    x = x1 = x2 = 1
    DS = []
    for i in range(P):
        if x ^ x1 ^ x2 == 0:
            DS.append(i)
        x, x1, x2 = mulmod(x, theta, poly, deg), mulmod(x1, th_q, poly, deg), mulmod(x2, th_q2, poly, deg)
    S = set(DS)
    count = {}
    for u in DS:
        for v in DS:
            if u != v:
                count[(u - v) % P] = count.get((u - v) % P, 0) + 1
    planar = len(DS) == q + 1 and len(count) == P - 1 and set(count.values()) == {1}
    two = {pow(2, i, P) for i in range(3 * a)}
    D = {pow(x, n, P) for x in range(1, P)}
    return dict(a=a, P=P, poly=poly, theta=theta, singer_size=len(DS), singer_planar=planar,
                two_subgroup_in_singer=two <= S, mu_size=len(D), mu_contains_two=two <= D,
                mu_singer_intersection=len(D & S))


# ------------------------------------------------------------ forced subgroup ---

def forced_tests(n):
    p, m = n * n + n + 1, n + 1
    in_D = lambda x: pow(x % p, m, p) == 1
    gens = sorted({2, n} | {d for d in range(2, n + 1) if n % d == 0})
    K, todo = {1}, [1]
    while todo:
        x = todo.pop()
        for g in gens:
            y = x * g % p
            if y not in K:
                K.add(y)
                todo.append(y)
    Kl, seen, collision = sorted(K), {}, None
    for i, x in enumerate(Kl):
        for y in Kl[i:]:
            s = (x + y) % p
            if s in seen and collision is None:
                collision = [seen[s], [x, y]]
            seen.setdefault(s, [x, y])
    # Planarity would force K into D; a collision inside K therefore excludes n
    # whether or not K actually lies in D (it does for n = 8, 512).
    forced_in_D = all(in_D(x) for x in K)
    half = pow(2, -1, p)
    lemma5 = sorted(u for u in K if u not in (1, 2, half) and (in_D(u - 1) or in_D(1 - u)))
    return dict(n=n, p=p, forced_subgroup_size=len(K), forced_subgroup_in_D=forced_in_D,
                collision_inside_forced=collision, lemma5_violations=lemma5[:8],
                lemma5_violation_count=len(lemma5), minus3_in_D=in_D(-3))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--max-a', type=int, default=150)
    ap.add_argument('--char0', type=int, default=24)
    ap.add_argument('--broken', action='store_true')
    ap.add_argument('--output')
    args = ap.parse_args()
    began = time.monotonic()
    sid = {a: sidon_mod(a) for a in range(1, args.max_a + 1)}
    need(all(r['distinct'] for r in sid.values()), 'order of 2 is not 3a')
    failures = [a for a, r in sid.items() if not r['sidon']]
    need(failures == [2], 'Sidon failures %s' % failures)
    if args.broken:
        need(sidon_mod(9, (1 << 18) + (1 << 9) + 3)['sidon'], 'broken control: P altered')
    char0 = [sidon_char0(s) for s in range(1, args.char0 + 1)]
    coords = coordinates()
    shadow = [singer_shadow(3), singer_shadow(9)]
    need(all(s['singer_planar'] and s['two_subgroup_in_singer'] and s['mu_contains_two'] for s in shadow),
         'Singer shadow')
    need(shadow[0]['mu_singer_intersection'] == 9 and shadow[1]['mu_singer_intersection'] == 27,
         'mu_(n+1) meets the Singer set exactly in <2> (a = 9)')
    forced = [forced_tests(n) for n in (8, 512, 24, 90)]
    f8, f512, f24, f90 = forced
    need(f8['forced_subgroup_in_D'] and f8['collision_inside_forced'] is None
         and f8['lemma5_violation_count'] == 0, 'n=8 control')
    need(f512['forced_subgroup_in_D'] and f512['forced_subgroup_size'] == 27
         and f512['collision_inside_forced'] is None
         and f512['lemma5_violation_count'] == 0 and not f512['minus3_in_D'], 'n=512 forced tests')
    need(f24['collision_inside_forced'] is not None and f90['collision_inside_forced'] is not None,
         'n=24, 90 positive controls')
    result = dict(sidon_checked_a=[1, args.max_a], sidon_failures=failures, sidon_failure_witness_a2=sid[2]['witness'],
                  char0_sidon_checked_s=[1, args.char0], char0_set_sizes=char0[-1], coordinates=coords,
                  singer_shadow=shadow, forced_tests=forced, seconds=round(time.monotonic() - began, 3),
                  scope='Finite checks only; the general statements are proved in proofs/FORCED-SUBGROUP.md.')
    text = json.dumps(result, indent=1)
    if args.output:
        open(args.output, 'w').write(text + '\n')
    print(text)


if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print('CHECK FAILED: ' + str(e), file=sys.stderr)
        sys.exit(1)
