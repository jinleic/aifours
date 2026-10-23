#!/usr/bin/env python3
"""Check (aid only) the deficiency form of the untranslated kill test against the HW window test.
For random run data, random integer lifts x_t, random P (bitmask over runs):
  HW-untranslated:  -g(E-) <= X_P <= g(E+),  X_P = sum_{t in P} x_t,
  deficiency form (proof-RUNS.md Lemma KW): with bh_t = 2x_t - d_t, e_t = 1 - bh_t,
    max(tau + 2(kappa-B) + 2 + 2beta - 2m, |P| - B + epsP, |P| + D_P - 2p + 2m) <= e(P)
    e(P) <= min(|P| + A - epsM, |P| + 2A - D_P - 2kappa - 2 + 2m - 2beta, |P| + 2p - 2m + D_P)
  where kappa = p-1-H, beta = #even boundary runs, epsP = [E+ odd], epsM = [E- odd],
  tau = sum_P (1 - d_t), D_P = sum_P d_t.  (P nonempty proper; m >= 1.)
"""
import random, sys


def hw_g(p, m, h, E):
    return min(p - m, E + m + h - p, E // 2)


def check(trials, seed):
    rng = random.Random(seed)
    bad = 0; tot = 0
    for _ in range(trials):
        p = rng.choice([5, 7, 11, 13])
        k = rng.randint(2, 12)
        a = [rng.randint(0, p - 1) for _ in range(k)]
        b = [rng.randint(0, p - 1) for _ in range(k)]
        for i in range(k):
            if a[i] + b[i] == 0:
                a[i] = 1
        l = [rng.randint(1, 6) for _ in range(k)]
        A, B = sum(a), sum(b); R = A + B; H = sum(x // 2 for x in l); kappa = p - 1 - H
        x = [rng.randint(-2 * p, 2 * p) for _ in range(k)]
        for _ in range(30):
            P = rng.randint(1, (1 << k) - 2)
            z = [(P >> i) & 1 for i in range(k)]
            f = [1 if z[j] != z[(j + 1) % k] else 0 for j in range(k)]
            m = sum(f) // 2
            beta = sum(1 for j in range(k) if f[j] and l[j] % 2 == 0)
            h = sum((l[j] - f[j]) // 2 for j in range(k))
            assert h == H - beta
            Ep = sum(a[i] if z[i] else b[i] for i in range(k)); Em = R - Ep
            XP = sum(x[i] for i in range(k) if z[i])
            hw = (-hw_g(p, m, h, Em) <= XP <= hw_g(p, m, h, Ep))
            d = [a[i] - b[i] for i in range(k)]
            DP = sum(d[i] for i in range(k) if z[i]); nP = sum(z)
            e = sum(1 - (2 * x[i] - d[i]) for i in range(k) if z[i])
            tau = nP - DP
            lo = max(tau + 2 * (kappa - B) + 2 + 2 * beta - 2 * m, nP - B + (Ep % 2), nP + DP - 2 * p + 2 * m)
            hi = min(nP + A - (Em % 2), nP + 2 * A - DP - 2 * kappa - 2 + 2 * m - 2 * beta, nP + 2 * p - 2 * m + DP)
            form = (lo <= e <= hi)
            tot += 1
            if form != hw:
                bad += 1
                if bad < 5:
                    print('MISMATCH', p, a, b, l, x, P, hw, form, lo, e, hi)
    return tot, bad


if __name__ == '__main__':
    print(check(int(sys.argv[1]), int(sys.argv[2])))
