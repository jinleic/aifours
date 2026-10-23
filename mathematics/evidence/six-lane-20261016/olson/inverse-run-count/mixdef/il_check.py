#!/usr/bin/env python3
"""Exact test of the intermediate lemmas IL and DG (mixdef/README.md Sec. 3).
Data: all reflection runs odd, every run pure or a (1,1)-pair, 1 <= B < kappa, B <= A, no full
window.  phi: every interval-feasible phi (../hwsingle, family m <= 1), up to a cap per datum.
Modes:  il_check.py exhaustive p kmin kmax cap      (all run data, p small)
        il_check.py sample p trials seed cap         (random run data)
"""
import os, sys, random, itertools, subprocess
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from scl_closure import tables  # noqa: E402


def feasible_phis(p, a, b, l, cap):
    k = len(a)
    args = [os.path.join(os.path.dirname(HERE), 'hwsingle'), str(p), '1', str(k)] + \
        [str(x) for x in a + b + l] + [str(cap), str(cap)]
    out = subprocess.run(args, capture_output=True, text=True, timeout=1200).stdout
    return [list(map(int, ln.split()[1:])) for ln in out.splitlines() if ln.startswith('phi:')]


def gap_rep(U, L, P, s, p):
    lo, hi = -L[P], U[P]
    return hi + 1 + ((s - (hi + 1)) % p)


def comps(P, k):
    return sum(1 for j in range(k) if (P >> j) & 1 and not (P >> ((j - 1) % k)) & 1)


def test(p, a, b, l, cap, st, ex):
    k = len(a); full = (1 << k) - 1
    A, B = sum(a), sum(b); H = sum(x // 2 for x in l); kappa = p - 1 - H; kB = kappa - B
    U, L = tables(a, b, l, p)
    if any(U[P] + L[P] + 1 >= p for P in range(1, full)):
        st['data_fullwindow_skipped'] += 1
        return
    st['data'] += 1
    d = [x - y for x, y in zip(a, b)]
    ivals = []
    for i in range(k):
        for ln in range(1, k):
            ivals.append(sum(1 << ((i + j) % k) for j in range(ln)))
    for phi in feasible_phis(p, a, b, l, cap):
        st['phi'] += 1
        x = [gap_rep(U, L, 1 << t, phi[t], p) for t in range(k)]
        il_ok = True
        for Q in ivals:
            if U[Q] + L[Q] < 0:
                st['empty_interval_window'] += 1
                continue
            s = sum(phi[t] for t in range(k) if (Q >> t) & 1) % p
            if gap_rep(U, L, Q, s, p) != sum(x[t] for t in range(k) if (Q >> t) & 1):
                il_ok = False
                break
        if not il_ok:
            st['IL_FAIL'] += 1
            if len(ex) < 6:
                ex.append(('IL_FAIL', p, a, b, l, phi, x, sum(x)))
            continue
        st['IL_ok'] += 1
        bh = [2 * x[t] - d[t] for t in range(k)]
        Z = sorted([t for t in range(k) if bh[t] <= 0], key=lambda t: -bh[t])
        if not Z:
            st['DG_noZ'] += 1
            continue
        def Phi(P):
            return sum(d[u] - bh[u] for u in range(k) if (P >> u) & 1) + 2 * comps(P, k)
        target = 2 * kB + 2; P = 0
        for t in Z:
            if P and Phi(P) >= target:
                break
            P |= 1 << t
        for f in [t for t in range(k) if bh[t] == 1 and d[t] > 0]:
            if Phi(P) >= target:
                break
            if (P >> f) & 1 or (P >> ((f + 1) % k)) & 1 or (P >> ((f - 1) % k)) & 1:
                continue
            P |= 1 << f
        X = sum(x[u] for u in range(k) if (P >> u) & 1)
        if P != full and Phi(P) >= target and -L[P] <= X <= U[P]:
            st['DG_ok'] += 1
        else:
            st['DG_FAIL'] += 1
            if len(ex) < 12:
                ex.append(('DG_FAIL', p, a, b, l, phi, bh, [u for u in range(k) if (P >> u) & 1]))


def splits(r):
    opts = []
    for x in r:
        o = [(x, 0), (0, x)]
        if x == 2:
            o.append((1, 1))
        opts.append(o)
    for ch in itertools.product(*opts):
        yield [c[0] for c in ch], [c[1] for c in ch]


def compositions(n, parts):
    if parts == 1:
        yield [n]; return
    for first in range(1, n - parts + 2):
        for rest in compositions(n - first, parts - 1):
            yield [first] + rest


def main():
    mode = sys.argv[1]; st = Counter(); ex = []
    if mode == 'exhaustive':
        p, kmin, kmax, cap = map(int, sys.argv[2:6]); N = 4 * p - 2
        for k in range(kmin, kmax + 1):
            for F in range(k, N - k + 1):
                if (F - k) % 2:
                    continue
                H = (F - k) // 2; kappa = p - 1 - H; R = N - F
                if kappa < 2:
                    continue
                for l2 in compositions((F - k) // 2 + k, k):   # l = 2*l2 - 1 (odd parts)
                    l = [2 * y - 1 for y in l2]
                    for r in compositions(R, k):
                        for a, b in splits(r):
                            A, B = sum(a), sum(b)
                            if B < 1 or B >= kappa or A < B:
                                continue
                            test(p, a, b, l, cap, st, ex)
    else:
        p, T, seed, cap = map(int, sys.argv[2:6]); N = 4 * p - 2
        rng = random.Random(seed); done = 0
        while done < T:
            k = rng.randint(3, 2 * p - 3); R = rng.randint(k, 3 * p - 2); F = N - R
            if F < k or (F - k) % 2:
                continue
            H = (F - k) // 2; kappa = p - 1 - H
            if kappa < 2:
                continue
            c = sorted(rng.sample(range(1, R), k - 1)); r = [y - x for x, y in zip([0] + c, c + [R])]
            a, b = [], []
            for x in r:
                u = rng.random()
                if x == 2 and u < 0.15: a.append(1); b.append(1)
                elif u < 0.35: a.append(0); b.append(x)
                else: a.append(x); b.append(0)
            if sum(b) < 1 or sum(b) >= kappa or sum(a) < sum(b):
                continue
            l = [1] * k
            for _ in range(H): l[rng.randrange(k)] += 2
            before = st['data']
            test(p, a, b, l, cap, st, ex)
            if st['data'] > before:
                done += 1
    print(dict(st))
    for e in ex:
        print(e)


if __name__ == '__main__':
    main()
