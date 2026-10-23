#!/usr/bin/env python3
"""Exact checks for Lemma GR / Corollary GR-W (proof-GR.md).

(a) Lemma GR (exact criterion) vs exact DP on random RGR words, lengths 4p-1, 4p-2,
    4p-3 (the shorter lengths supply genuine NO instances = counter-controls).
(b) obstruction family w_p: |Ach(z*)| for z* = (-,+,+), p = 5..31, and DP at 5,7,11.
(c) p = 5 exhaustive count over ordered run data (k <= KMAX) of RGR words passing the
    y-independent Res filters (not EGZ, not P, not Davenport-alpha, not T0, no run
    with >= p equal rotations, Lemma A bound < p for every pattern): how many have a
    full window (Corollary GR-W) and how many do not; for the latter, all reflection
    values (y_1 = 0, not all equal) are decided by Lemma GR.
Writes evidence/gr_window.json.  Usage: gr_window.py [KMAX]
"""
import sys, os, json, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import coverage_all as ca

def ach(z, a, b, l, p):
    k = len(z); F = sum(l); R = sum(a) + sum(b)
    f = [int(z[i] != z[(i + 1) % k]) for i in range(k)]
    Phi = sum(f)
    delta = sum(1 for i in range(k) if (l[i] - f[i]) % 2)
    Cmax = F - delta
    Ep = sum(a[i] if z[i] == 1 else b[i] for i in range(k)); Em = R - Ep
    s0 = 2 * p - Cmax; s1 = 2 * p - Phi
    lo = max(-s1, s0 - 2 * Em, -Em); hi = min(s1, 2 * Ep - s0, Ep)
    if lo % 2: lo += 1
    if hi % 2: hi -= 1
    return lo, hi

def tau(z, y, p):
    k = len(z)
    inv2 = pow(2, p - 2, p)
    return (-inv2 * sum(z[i] * (y[i] - y[i - 1]) for i in range(k))) % p

def criterion(a, b, l, y, p):
    k = len(a)
    for z in itertools.product((1, -1), repeat=k):
        lo, hi = ach(z, a, b, l, p)
        if lo > hi: continue
        tz = tau(z, y, p)
        if hi - lo >= 2 * (p - 1): return True
        for t in range(lo, hi + 1, 2):
            if (t - tz) % p == 0: return True
    return False

def full_window(a, b, l, p):
    for z in itertools.product((1, -1), repeat=len(a)):
        lo, hi = ach(z, a, b, l, p)
        if lo <= hi and (hi - lo) // 2 + 1 >= p: return True
    return False

def build(a, b, l, y, rng=None):
    w = []
    for i in range(len(a)):
        rot = [('R', 1)] * a[i] + [('R', -1)] * b[i]
        if rng: rng.shuffle(rot)
        w += rot + [('F', y[i])] * l[i]
    return w

def random_rgr(p, N, rng):
    while True:
        k = rng.randrange(1, 7)
        parts = [1] * (2 * k)
        for _ in range(N - 2 * k):
            parts[rng.randrange(2 * k)] += 1
        if N - 2 * k < 0: continue
        r = parts[0::2]; l = parts[1::2]
        a = [rng.randrange(0, ri + 1) for ri in r]; b = [ri - ai for ri, ai in zip(r, a)]
        y = [rng.randrange(p) for _ in range(k)]
        return a, b, l, y

def main():
    KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    rng = random.Random(20261016)
    out = {'a_criterion_vs_dp': {}, 'b_wp': {}, 'c_count_p5': {}}
    for p in (5, 7, 11):
        for N in (4 * p - 1, 4 * p - 2, 4 * p - 3):
            agree = dis = yes = no = 0
            for _ in range(300 if p < 11 else 120):
                a, b, l, y = random_rgr(p, N, rng)
                w = [(c, v % p) for c, v in build(a, b, l, y, rng)]
                c1 = criterion(a, b, l, [v % p for v in y], p)
                c2 = ca.has_solution(w, p)
                agree += c1 == c2; dis += c1 != c2; yes += c2; no += (not c2)
            out['a_criterion_vs_dp'][f'p{p}_N{N}'] = {'agree': agree, 'disagree': dis, 'dp_yes': yes, 'dp_no': no}
    for p in range(5, 33):
        if all(p % q for q in range(2, int(p ** 0.5) + 1)):
            a, b, l = [p - 2, p - 2, 3], [0, 0, 0], [p - 2, 4, p - 2]
            lo, hi = ach((-1, 1, 1), a, b, l, p)
            rec = {'window': [lo, hi], 'evens': (hi - lo) // 2 + 1}
            if p <= 11:
                y = [1, 2, 0]
                w = build(a, b, l, y)
                rec['criterion'] = criterion(a, b, l, y, p)
                rec['dp'] = ca.has_solution([(c, v % p) for c, v in w], p)
            out['b_wp'][p] = rec
    p = 5; N = 4 * p - 1
    stats = {}
    for k in range(1, KMAX + 1):
        tot = passed = full = notfull = undecided_pairs = pairs = 0
        for cuts in itertools.combinations(range(1, N), 2 * k - 1):
            bounds = (0,) + cuts + (N,)
            parts = [bounds[i + 1] - bounds[i] for i in range(2 * k)]
            r = parts[0::2]; l = parts[1::2]
            for a in itertools.product(*[range(ri + 1) for ri in r]):
                b = [ri - ai for ri, ai in zip(r, a)]
                tot += 1
                R = sum(r); F = sum(l)
                if R >= 3 * p - 1: continue
                if F + sum(ri // 2 for ri in r) >= 3 * p - 1: continue
                if F >= 2 and R + sum(li // 2 for li in l) >= 3 * p - 1: continue
                if sum(li % 2 for li in l) <= 1: continue
                if any(ai >= p or bi >= p for ai, bi in zip(a, b)): continue
                lam = 0
                for z in itertools.product((1, -1), repeat=k):
                    Ep = sum(a[i] if z[i] == 1 else b[i] for i in range(k))
                    lam = max(lam, min(Ep, R - Ep) + 1)
                if lam >= p: continue
                passed += 1
                if full_window(a, b, l, p):
                    full += 1; continue
                notfull += 1
                for yt in itertools.product(range(p), repeat=k - 1):
                    y = [0] + list(yt)
                    if len(set(y)) == 1: continue
                    pairs += 1
                    if not criterion(a, b, l, y, p): undecided_pairs += 1
        stats[k] = {'ordered_run_data': tot, 'pass_y_independent_Res_filters': passed,
                    'full_window': full, 'no_full_window': notfull,
                    'nonrigid_y_assignments_checked': pairs, 'criterion_false': undecided_pairs}
        print('k', k, stats[k], flush=True)
    out['c_count_p5'] = stats
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'evidence', 'gr_window.json')
    json.dump(out, open(path, 'w'), indent=1)
    print(json.dumps(out['a_criterion_vs_dp'])); print(json.dumps(out['b_wp']))

if __name__ == '__main__':
    main()
