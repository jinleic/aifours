#!/usr/bin/env python3
"""Replay of the proof of Theorem KB_HIGH (kappaB-high/proof-KBH.md) -- aid only, never a hypothesis.

Words w: RGR of length 4p-2 with ARBITRARY rotation runs (any mix of rho_1, rho_-1), arbitrary
reflection-run parities, A >= B = kappa >= 1, o_F >= p+1 odd reflection runs, A <= 2p-1.
For each w: Lemma OR -> w~ (merge segments); for EVERY window W of p consecutive runs of w~ build the
greedy theta of the proof and check against the EXACT half windows of w~ (general formula, written
here independently): theta_t <= max(0, d_t), sum theta <= D, and tau(Q) = D_Q - theta(Q) in
[-L_Q, U_Q] for every subinterval Q of W.  End-to-end (p <= pmaxdp): random reflection values y,
pigeonhole collision Q~ in w~, mapped back to w (union of segments), exact window test in w, and the
raw ordered-product DP (../hw.py dp_has) must find an identity 2p-subword.
Control: the same greedy on all-odd data with kappa = B + 1 must FAIL for some window (the checker is
not vacuous; ZS is not claimed there).
Usage: zs_replay.py p trials seed pmaxdp
"""
import os, sys, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from hw import dp_has, word_of, phi_of_y  # noqa: E402


def win(a, b, l, p, P):
    k = len(a); R = sum(a) + sum(b)
    z = [(P >> i) & 1 for i in range(k)]
    f = [1 if z[j] != z[(j + 1) % k] else 0 for j in range(k)]
    m = sum(f) // 2
    h = sum((l[j] - f[j]) // 2 for j in range(k))
    Ep = sum(a[i] if z[i] else b[i] for i in range(k)); Em = R - Ep
    g = lambda E: min(p - m, E + m + h - p, E // 2)
    return -g(Em), g(Ep)


def merge_OR(a, b, l):
    k = len(a); odd = [j for j in range(k) if l[j] % 2]
    segs = []
    for i, j0 in enumerate(odd):
        j1 = odd[(i + 1) % len(odd)]; runs = []; t = (j0 + 1) % k
        while True:
            runs.append(t)
            if t == j1:
                break
            t = (t + 1) % k
        segs.append(runs)
    a2 = [sum(a[t] for t in s) for s in segs]; b2 = [sum(b[t] for t in s) for s in segs]
    l2 = [sum(l[t] for t in s if l[t] % 2 == 0) + l[s[-1]] for s in segs]
    return segs, a2, b2, l2


def greedy_theta(d, s, p, B):
    k = len(d); W = [(s + i) % k for i in range(p)]
    th = []
    def lam(DQ):
        return max(0, -((B - DQ) // 2), DQ - p + 1)   # ceil((DQ-B)/2) = -floor((B-DQ)/2)
    for j in range(1, p + 1):
        best = 0
        for i in range(j):
            DQ = sum(d[W[t]] for t in range(i, j))
            prev = sum(th[t] for t in range(i, j - 1))
            best = max(best, lam(DQ) - prev)
        th.append(best)
    return W, th


def check_windows(a2, b2, l2, p, stats, tag):
    k = len(a2); full = (1 << k) - 1
    d = [x - y for x, y in zip(a2, b2)]; B = sum(b2); D = sum(d)
    bad = 0
    for s in range(k):
        W, th = greedy_theta(d, s, p, B)
        ok = all(th[i] <= max(0, d[W[i]]) and th[i] >= 0 for i in range(p)) and sum(th) <= D
        if ok:
            for i in range(p):
                for j in range(i + 1, p + 1):
                    Q = sum(1 << W[t] for t in range(i, j))
                    lo, hi = win(a2, b2, l2, p, Q)
                    tau = sum(d[W[t]] for t in range(i, j)) - sum(th[i:j])
                    if not (lo <= tau <= hi):
                        ok = False; break
                if not ok:
                    break
        if not ok:
            bad += 1
    stats[tag + ('_allwindows_ok' if bad == 0 else '_SOMEWINDOW_FAIL')] += 1
    return bad


def rand_word(p, rng, kappa_minus_B=0, allodd=False):
    while True:
        o = rng.randint(p + 1, 2 * p - 1)
        e = 0 if allodd else rng.randint(0, 3)
        B = rng.randint(1, p - 1)
        kappa = B + kappa_minus_B
        H = p - 1 - kappa
        if H < e or kappa > p - 1:
            continue
        k = o + e
        F = o + 2 * H
        R = 4 * p - 2 - F
        if R < k or R - B < B:
            continue
        A = R - B
        if A > 2 * p - 1:
            continue
        # reflection runs: o odd, e even (>= 2); distribute H units
        kinds = [1] * o + [0] * e; rng.shuffle(kinds)
        u = [0] * k
        for j in range(k):
            if kinds[j] == 0:
                u[j] = 1
        rest = H - e
        if rest < 0:
            continue
        for _ in range(rest):
            u[rng.randrange(k)] += 1
        l = [2 * u[j] + 1 if kinds[j] else 2 * u[j] for j in range(k)]
        # rotation runs: R letters, B of them rho_-1, arbitrary mix
        c = sorted(rng.sample(range(1, R), k - 1)); r = [y - x for x, y in zip([0] + c, c + [R])]
        letters = [1] * A + [0] * B; rng.shuffle(letters)
        a, b = [], []; pos = 0
        for x in r:
            seg = letters[pos:pos + x]; pos += x
            a.append(sum(seg)); b.append(x - sum(seg))
        assert sum(a) + sum(b) + sum(l) == 4 * p - 2
        return a, b, l


def main():
    p, T, seed, pmaxdp = map(int, sys.argv[1:5])
    rng = random.Random(seed); st = Counter()
    for _ in range(T):
        a, b, l = rand_word(p, rng)
        segs, a2, b2, l2 = merge_OR(a, b, l)
        H = sum(x // 2 for x in l); kappa = p - 1 - H
        assert sum(b2) == sum(b) == kappa and all(x % 2 for x in l2) and len(a2) >= p + 1
        assert sum(x // 2 for x in l2) == H
        check_windows(a2, b2, l2, p, st, 'KBH')
        if p <= pmaxdp:
            # end-to-end: random y, pigeonhole in w~ (window start 0), map back, exact test, raw DP
            k = len(a); k2 = len(a2)
            y = [rng.randrange(p) for _ in range(k)]
            phi = phi_of_y(y, p)
            phi2 = [sum(phi[t] for t in s) % p for s in segs]
            d2 = [x - z for x, z in zip(a2, b2)]
            W, th = greedy_theta(d2, 0, p, sum(b2))
            S = [0]; seen = {0: 0}; Qpair = None
            for j in range(1, p + 1):
                t = W[j - 1]
                S.append((S[-1] + phi2[t] - (d2[t] - th[j - 1])) % p)
                if S[-1] in seen:
                    Qpair = (seen[S[-1]], j); break
                seen[S[-1]] = j
            assert Qpair is not None
            i, j = Qpair
            Q2 = sum(1 << W[t] for t in range(i, j))
            lo2, hi2 = win(a2, b2, l2, p, Q2)
            s2 = sum(phi2[t] for t in range(k2) if (Q2 >> t) & 1) % p
            in2 = (s2 - lo2) % p <= hi2 - lo2 if lo2 <= hi2 else False
            Q = sum(1 << t for jj in range(k2) if (Q2 >> jj) & 1 for t in segs[jj])
            lo, hi = win(a, b, l, p, Q)
            s1 = sum(phi[t] for t in range(k) if (Q >> t) & 1) % p
            in1 = (s1 - lo) % p <= hi - lo if lo <= hi else False
            dp = dp_has(word_of(a, b, l, y, p), p)
            st['E2E_' + ('ok' if (in2 and in1 and (lo, hi) == (lo2, hi2) and dp) else 'FAIL')] += 1
    # control: kappa = B + 1, all-odd
    for _ in range(max(1, T // 4)):
        a, b, l = rand_word(p, rng, kappa_minus_B=1, allodd=True)
        check_windows(a, b, l, p, st, 'CONTROL_kappaB1')
    print(dict(st))


if __name__ == '__main__':
    main()
