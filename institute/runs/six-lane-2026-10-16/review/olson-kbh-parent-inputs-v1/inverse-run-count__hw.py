#!/usr/bin/env python3
"""Half-window form (README Sec. 2) of Lemma WAS, plus a fresh raw DP over D_{2p}.

Written for olson/inverse-run-count (task OlsonRunCount), independent of ../code/.
Group law (v,e)(v',e') = (v + e v', e e'); rho_x = (x,+1), sigma_y = (y,-1).
"""
import itertools, random, sys


def rot(mask, s, p):
    s %= p
    full = (1 << p) - 1
    return ((mask << s) | (mask >> (p - s))) & full if s else mask


def dp_has(word, p):
    """word: list of (x, s) with s = +1 rotation rho_x, s = -1 reflection sigma_x.
    True iff some increasing 2p-subword has ordered product (0,+1)."""
    n2 = 2 * p
    # reach[c][e] bitmask over v of products (v,e) of increasing c-subwords
    reach = [[0, 0] for _ in range(n2 + 1)]  # index e: 0 -> +1, 1 -> -1
    reach[0][0] = 1
    for (x, s) in word:
        for c in range(n2 - 1, -1, -1):
            for ei in (0, 1):
                m = reach[c][ei]
                if not m:
                    continue
                e = 1 if ei == 0 else -1
                nm = rot(m, e * x, p)
                nei = ei if s == 1 else 1 - ei
                reach[c + 1][nei] |= nm
    return bool(reach[n2][0] & 1)


def word_of(a, b, l, y, p, shuffle=None):
    """explicit cyclic-run word R_1 S_1 ... R_k S_k; y[j] value of S_j (j = 0..k-1 means S_1..S_k)."""
    w = []
    for i in range(len(a)):
        rots = [(1, 1)] * a[i] + [(p - 1, 1)] * b[i]
        if shuffle is not None:
            shuffle.shuffle(rots)
        w += rots + [(y[i] % p, -1)] * l[i]
    return w


def windows(a, b, l, p):
    """dict P(bitmask over runs 0..k-1, run index i = R_{i+1}) -> (lo, hi) of I(P) (lo > hi: empty).
    Boundary f_j at S_j (between R_j and R_{j+1}); with 0-based runs, S index j sits after run j."""
    k = len(a)
    R = sum(a) + sum(b)
    H = sum(x // 2 for x in l)
    out = {}
    for P in range(1 << k):
        z = [(P >> i) & 1 for i in range(k)]
        f = [1 if z[j] != z[(j + 1) % k] else 0 for j in range(k)]  # S after run j
        m2 = sum(f)
        m = m2 // 2
        h = sum((l[j] - f[j]) // 2 for j in range(k))
        Ep = sum(a[i] if z[i] else b[i] for i in range(k))
        Em = R - Ep

        def g(E):
            return min(p - m, E + m + h - p, E // 2)
        out[P] = (-g(Em), g(Ep))
    return out


def phi_of_y(y, p):
    """phi_i (0-based run i = R_{i+1}) = (y_{S before} - y_{S after})/2; S before run i is S index i-1."""
    k = len(y)
    inv2 = (p + 1) // 2
    return [((y[(i - 1) % k] - y[i]) * inv2) % p for i in range(k)]


def hw_avoids(a, b, l, y, p, W=None):
    k = len(a)
    if W is None:
        W = windows(a, b, l, p)
    phi = phi_of_y(y, p)
    for P, (lo, hi) in W.items():
        if lo > hi:
            continue
        s = sum(phi[i] for i in range(k) if (P >> i) & 1) % p
        if hi - lo + 1 >= p:
            return False
        if (s - lo) % p <= hi - lo:
            return False
    return True


def random_rgr(p, N, rng, kmin=1, kmax=None):
    while True:
        k = rng.randint(kmin, kmax if kmax else N // 2)
        if 2 * k > N:
            continue
        # composition of N into 2k positive parts
        cuts = sorted(rng.sample(range(1, N), 2 * k - 1))
        parts = [y - x for x, y in zip([0] + cuts, cuts + [N])]
        r = parts[0::2]
        l = parts[1::2]
        a, b = [], []
        for ri in r:
            ai = rng.randint(0, ri)
            a.append(ai)
            b.append(ri - ai)
        y = [rng.randrange(p) for _ in range(k)]
        return a, b, l, y


def selftest(p, N, trials, seed):
    rng = random.Random(seed)
    agree = dis = yes = no = 0
    for _ in range(trials):
        a, b, l, y = random_rgr(p, N, rng)
        w = word_of(a, b, l, y, p, shuffle=rng)
        d = dp_has(w, p)
        hw = not hw_avoids(a, b, l, y, p)
        if d == hw:
            agree += 1
        else:
            dis += 1
            print('DISAGREE', p, N, a, b, l, y, d, hw)
        yes += d
        no += (not d)
    return agree, dis, yes, no


if __name__ == '__main__':
    p = int(sys.argv[1]); N = int(sys.argv[2]); T = int(sys.argv[3]); seed = int(sys.argv[4])
    print(p, N, selftest(p, N, T, seed))
