#!/usr/bin/env python3
"""seeds.py -- [F] type-level receipt for c5/proof-SEED.md (task OlsonRunCount5).

W(p, kB): anti run 0 (d = -1), aligned runs 1..n (d = +1), n = p + kB, k = n + 1 runs on a cycle, B = 1, kappa = kB + 1,
all reflection runs odd (beta = 0).  For a proper pattern Q with y := D_Q and m := m(Q) blocks (c3/proof-WALL.md (0.1),(0.2)):
  lam(y, m)  = min(p - m + 1, y + m - kB, floor((y + 1)/2) + 1)            [lambda(Q)]
  lamc(y, m) = min(p - m + 1, p - 1 - y + m, floor((p + kB - y)/2) + 1)    [lambda(Q^c)]
  U(y, m) = p - lamc(y, m).
Part A (primes 11..400, every kB with 3kB >= p + 5, kB <= p - 4): closed forms of the pair seed (Lemma PS), containment in
  the canonical singleton range, the realizability count, the pair steps and the pin (Lemma SCW).
Part B (primes 5..113, same kB): every type step (j, e, m) of every size in the Lemma CW order: (A^s), (B^s) evaluated
  exactly, and each of the 18 term sums against the bound claimed in proof-SEED.md Sec. 3.
Part C (primes 37..61): optimal seed over ALL pattern types (D, m) -> (D + 1, m'), m' in {m - 1, m, m + 1}: the pair seed
  is optimal (no type gives a shorter usable seed).
Part D (mutation controls, type level): (D1) plain singleton ranges instead of seeds (Lemma NOLIFT: the anti pair steps
  must fail for every kB here); (D2) seed lower end lowered by w until some step fails (records the first failing w);
  (D3) arc formula with lambda + 1 (windows widened) must make some pair seed empty or some step fail.
"""
import sys, time

def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def cdiv(a, b): return -((-a) // b)

class W:
    def __init__(self, p, kB, shift=0):
        self.p, self.kB, self.n = p, kB, p + kB
        self.k = self.n + 1; self.delta = p - kB; self.shift = shift
    def lam(self, y, m):
        p, kB = self.p, self.kB
        return min(p - m + 1, y + m - kB, (y + 1) // 2 + 1) + self.shift
    def lamc(self, y, m):
        p, kB = self.p, self.kB
        return min(p - m + 1, p - 1 - y + m, (p + kB - y) // 2 + 1) + self.shift
    def U(self, y, m):
        return self.p - self.lamc(y, m)

def partA(primes):
    out = {'pairs_checked': 0, 'failures': []}
    for p in primes:
        for kB in range(1, p - 3):
            if 3 * kB < p + 5: continue
            w = W(p, kB); d = w.delta; m = kB // 2 + 1
            a, b = 3 - cdiv(d, 2), d // 2 - 1
            chk = {
              'lamQ': w.lam(2*m, m) == m + 1,
              'UQ': w.U(2*m, m) == m - 1 + cdiv(d, 2),
              'lamQt': w.lam(2*m + 1, m) == m + 2,
              'UQt': w.U(2*m + 1, m) == m + d // 2,
              'seed': (w.lam(2*m+1, m) - w.U(2*m, m), w.U(2*m+1, m) - w.lam(2*m, m)) == (a, b),
              'proper': w.lam(2*m, m) + w.lamc(2*m, m) <= p and w.lam(2*m+1, m) + w.lamc(2*m+1, m) <= p,
              'canon': w.lam(1, 1) == 2 - kB and w.U(1, 1) == d // 2 and a >= 2 - kB and b <= d // 2 and (d // 2 + kB - 1) <= p - 1,
              'anticanon': w.lam(-1, 1) == -kB and w.U(-1, 1) == d // 2 - 1,
              'realize': 3 * (w.n - 7) >= 6 * (m - 1),      # (n - 7)/3 >= m - 1 = floor(kB/2)
              # pair steps: aligned pair {s,t} (m in {1,2}) and anti pair {0,t} (m in {1,2})
              'alpair': all(2*a >= w.U(2, mm) + 1 - p and 2*b <= p + w.lam(2, mm) - 1 for mm in (1, 2)),
              'antipair': all(-kB + a >= w.U(0, mm) + 1 - p and (d // 2 - 1) + b <= p + w.lam(0, mm) - 1 for mm in (1, 2)),
              'alpair_cf': all(w.lamc(2, mm) == p - cdiv(d, 2) for mm in (1, 2)) and 3 * cdiv(d, 2) <= p + 5,
              'antipair_cf': all(w.lamc(0, mm) == p - cdiv(d, 2) + 1 and w.lam(0, mm) == mm - kB for mm in (1, 2)),
              'pin': (w.lam(w.n, 1) - kB >= 1) and (w.U(w.n, 1) + d // 2 - 1 <= 2 * p - 1) and w.lam(w.n, 1) == (p + kB + 1)//2 + 1 and w.U(w.n, 1) == p + kB,
            }
            out['pairs_checked'] += 1
            bad = [key for key, v in chk.items() if not v]
            if bad: out['failures'].append((p, kB, bad))
    return out

def steps(w):
    """yield every CW-order step: Q type (j, e, m), Q' type (j - 1, e, m'), s = |Q| >= 2."""
    k, n = w.k, w.n
    for s in range(2, k):
        for e in (0, 1):
            j = s - e
            if j < 1 or j > n: continue
            for m in range(1, min(s, k - s) + 1):
                mp = m if m < s else m - 1
                yield (s, j, e, m, mp)

def partB(primes, seeds=True):
    res = {'steps': 0, 'fail_A': 0, 'fail_B': 0, 'fail_bound': 0, 'minslack_A_general': None, 'minslack_B_general': None,
           'first_failures': []}
    for p in primes:
        for kB in range(1, p - 3):
            if 3 * kB < p + 5: continue
            w = W(p, kB); d = w.delta
            if seeds:
                a, b = 3 - cdiv(d, 2), d // 2 - 1
            else:
                a, b = w.lam(1, 1), w.U(1, 1)
            a0, b0 = w.lam(-1, 1), w.U(-1, 1)
            for (s, j, e, m, mp) in steps(w):
                y = j - e
                if s == 2:
                    lo1, hi1 = (a, b) if e == 0 else (a0, b0)
                else:
                    lo1, hi1 = w.lam(y - 1, mp), w.U(y - 1, mp)
                okA = lo1 + a >= w.U(y, m) + 1 - p
                okB = hi1 + b <= p + w.lam(y, m) - 1
                res['steps'] += 1
                if s >= 3:
                    sA = (lo1 + a) - (w.U(y, m) + 1 - p); sB = (p + w.lam(y, m) - 1) - (hi1 + b)
                    res['minslack_A_general'] = sA if res['minslack_A_general'] is None else min(res['minslack_A_general'], sA)
                    res['minslack_B_general'] = sB if res['minslack_B_general'] is None else min(res['minslack_B_general'], sB)
                    # the 18 term sums and the bounds claimed in proof-SEED.md Sec. 3
                    U1, U2, U3 = p - mp + 1, y - 1 + mp - kB, y // 2 + 1
                    T1, T2, T3 = p - m + 1, p - 1 - y + m, (p + kB - y) // 2 + 1
                    V1, V2, V3 = p - m + 1, y + m - kB, (y + 1) // 2 + 1
                    S1, S2, S3 = p - mp + 1, p - y + mp, (p + kB - y + 1) // 2 + 1
                    claimsA = [(U1 + T1, d + 1), (U1 + T2, d), (2 * (U1 + T3), d + 3), (U2 + T1, d - 1), (U2 + T2, d - 1),
                               (2 * (U2 + T3), d + 1), (2 * (U3 + T1), d + 3), (U3 + T2, d // 2 + 1), (2 * (U3 + T3), p + kB + 2)]
                    claimsB = [(V1 + S1, d + 1), (V1 + S2, d), (2 * (V1 + S3), d + 3), (V2 + S1, d + 1), (V2 + S2, d + 1),
                               (2 * (V2 + S3), d + 4), (2 * (V3 + S1), d + 3), (V3 + S2, cdiv(d, 2) + 2), (2 * (V3 + S3), p + kB + 4)]
                    if any(v < c for v, c in claimsA) or any(v < c for v, c in claimsB): res['fail_bound'] += 1
                    # each claimed bound implies the target
                    tA, tB = cdiv(d, 2) - 2, d // 2
                    lowA = min([c if i not in (2, 5, 6, 8) else cdiv(c, 2) for i, (v, c) in enumerate(claimsA)])
                    lowB = min([c if i not in (2, 5, 6, 8) else cdiv(c, 2) for i, (v, c) in enumerate(claimsB)])
                    if lowA < tA or lowB < tB: res['fail_bound'] += 1
                if not okA: res['fail_A'] += 1
                if not okB: res['fail_B'] += 1
                if (not okA or not okB) and len(res['first_failures']) < 6:
                    res['first_failures'].append((p, kB, s, j, e, m, mp, okA, okB))
    return res

def partC(primes):
    """optimal seed over all types (D, m) -> (D + 1, m'); usable = residue interval inside the canonical range minus the
    forbidden singleton window, contiguous; report whether any type beats the pair seed."""
    out = []
    for p in primes:
        beats = 0; equal_pair = 0; ks = 0
        for kB in range(1, p - 3):
            if 3 * kB < p + 5: continue
            ks += 1
            w = W(p, kB); d = w.delta; n = w.n
            L1, U1 = w.lam(1, 1), w.U(1, 1)
            pair = (3 - cdiv(d, 2), d // 2 - 1)
            best = None
            for m in range(1, n):
                for D in range(m, n):
                    for mp in (m - 1, m, m + 1):
                        if mp < 1 or D + 1 + mp - 1 > n: continue
                        lo = w.lam(D + 1, mp) - w.U(D, m); hi = w.U(D + 1, mp) - w.lam(D, m)
                        if hi - lo + 1 >= p: continue
                        vals = sorted(set(((yv - L1) % p) + L1 for yv in range(lo, hi + 1)))
                        vals = [v for v in vals if v <= U1]
                        if not vals: continue
                        if vals[-1] - vals[0] + 1 != len(vals): continue
                        key = (vals[-1] - vals[0], -vals[0])
                        if best is None or key < best[0]: best = (key, (vals[0], vals[-1]), (D, m, mp))
            if best[1] == pair: equal_pair += 1
            if best[0] < (pair[1] - pair[0], -pair[0]): beats += 1
        out.append((p, ks, equal_pair, beats))
    return out

def partD(primes):
    out = {}
    # D1: plain singleton ranges -> NOLIFT(a): anti pair steps fail
    rB = partB(primes, seeds=False)
    out['D1_plain_ranges'] = {'steps': rB['steps'], 'fail_A': rB['fail_A'], 'fail_B': rB['fail_B']}
    # D2: lower the seed's lower end by w until a step fails
    firstw = {}
    for p in primes:
        for kB in range(1, p - 3):
            if 3 * kB < p + 5: continue
            w = W(p, kB); d = w.delta
            a, b = 3 - cdiv(d, 2), d // 2 - 1
            a0, b0 = w.lam(-1, 1), w.U(-1, 1)
            for ww in range(0, 3 * p):
                aw = a - ww
                bad = False
                for (s, j, e, m, mp) in steps(w):
                    if s != 2: continue
                    y = j - e
                    lo1 = aw if e == 0 else a0
                    if lo1 + aw < w.U(y, m) + 1 - p: bad = True; break
                if bad: firstw[(p, kB)] = ww; break
    out['D2_first_failing_widening'] = {'cases': len(firstw), 'min_w': min(firstw.values()) if firstw else None,
                                        'max_w': max(firstw.values()) if firstw else None}
    # D3: lambda + 1 in every window (shift): the pair arcs become empty or steps fail
    cnt = 0; tot = 0
    for p in primes:
        for kB in range(1, p - 3):
            if 3 * kB < p + 5: continue
            tot += 1
            w = W(p, kB, shift=1); m = kB // 2 + 1
            lo = w.lam(2*m + 1, m) - w.U(2*m, m); hi = w.U(2*m + 1, m) - w.lam(2*m, m)
            if hi < lo or w.lam(2*m, m) + w.lamc(2*m, m) > p: cnt += 1
    out['D3_shifted_pair_seed_empty_or_full_window'] = (cnt, tot)
    return out

if __name__ == '__main__':
    t0 = time.time()
    print('== seeds.py start', time.strftime('%Y-%m-%dT%H:%M:%S'), flush=True)
    PA = [p for p in range(11, 401) if isprime(p)]
    A = partA(PA)
    print('Part A (primes 11..400):', {'cases': A['pairs_checked'], 'failures': A['failures'][:10], 'n_fail': len(A['failures'])}, flush=True)
    PB = [p for p in range(5, 114) if isprime(p)]
    B = partB(PB)
    print('Part B (primes 5..113, all type steps, seeds):', B, flush=True)
    C = partC([37, 41, 43, 47, 53, 59, 61])
    print('Part C (p, #kB, #best==pair seed, #types beating the pair seed):', C, flush=True)
    D = partD([p for p in range(11, 62) if isprime(p)])
    print('Part D (mutation controls, primes 11..61):', D, flush=True)
    print('== seeds.py end, %.1f s' % (time.time() - t0), flush=True)
