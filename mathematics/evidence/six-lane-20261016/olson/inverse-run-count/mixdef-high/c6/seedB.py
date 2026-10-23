#!/usr/bin/env python3
"""seedB.py -- [F] receipt for c6/proof-SEEDB.md (Theorem SEED-B), task OlsonRunCount5 cycle 6.
All-single-letter words: n = p + kB aligned runs, B anti runs (any positions), k = n + B, delta = p - kB.
Arcs (Lemma H, all reflection runs odd): lam(y, m) = min(p - m + 1, y + m - kB, floor((y + B)/2) + 1),
lamc(y, m) = min(p - m + 1, p - B - y + m, floor((p + kB - y)/2) + 1), U(y, m) = p - lamc(y, m).
Region R: B >= 2, kB >= 1, 2B + kB <= p - 2, and (E): 5kB + B + 13 <= 3p (singles, m_S = ceil((2kB + B + 2)/3)) or
kB + 3.5B + 14 <= 2p (pairs, m_P = ceil((kB + floor(B/2) + 1)/2)).
Part A (primes 11..PA): for every class of R: the configuration of Lemma IS, every generic-regime inequality, realisability,
  the exact seeds (from lam/U) = the closed parity formulas, the real bounds, no wrap-around, the 2-run steps (canonical-or-seed),
  the pin, and target <= analytic bound for the >= 3-run steps.
Part B (primes 11..PB): the analytic bounds of Lemma SCW-B over ALL (y, m, m') in the domain (aligned removal: 1 - B <= y <= n;
  anti removal: -B <= y <= n - 1; 1 <= m <= floor(k/2); m' in {m, m - 1}, m' >= 1): lam(y - d, m') + lamc(y, m) >=
  (delta - B + 2)/2 and lam(y, m) + lamc(y - d, m') >= (delta - B + 2)/2 (d = +1 aligned, d = -1 anti), plus all exact type
  steps (j, e, m) of every size for primes <= PT.
Part C: Claim E for every prime 19 <= p <= PC (every class with B >= 2, kB >= 1, 2B + kB <= p - 2 satisfies (E)); the
  classes of the small-B region failing (E) for p <= 17.
Part D (mutation controls): (D1) canonical ranges instead of seeds: some type steps fail; (D2) seeds widened by w: smallest w
  breaking a step (slack); (D3) one step outside the region (2B + kB = p - 1): generic-regime or bound failures.
Usage: python3 seedB.py PA PB PT PC
"""
import sys, time
from math import ceil
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
def cdiv(a, b): return -((-a) // b)
class Cls:
    def __init__(self, p, kB, B):
        self.p, self.kB, self.B = p, kB, B
        self.n = p + kB; self.k = self.n + B; self.delta = p - kB
    def lam(self, y, m):
        p, kB, B = self.p, self.kB, self.B
        return min(p - m + 1, y + m - kB, (y + B) // 2 + 1)
    def lamc(self, y, m):
        p, kB, B = self.p, self.kB, self.B
        return min(p - m + 1, p - B - y + m, (p + kB - y) // 2 + 1)
    def U(self, y, m): return self.p - self.lamc(y, m)

def in_region(p, kB, B): return B >= 2 and kB >= 1 and 2 * B + kB <= p - 2
def cond_E(p, kB, B): return 5 * kB + B + 13 <= 3 * p or 2 * kB + 7 * B + 28 <= 4 * p
def config(c):
    """returns ('S', m) or ('P', m) per the rule of Lemma IS, or None."""
    p, kB, B = c.p, c.kB, c.B
    if 5 * kB + B + 13 <= 3 * p: return ('S', cdiv(2 * kB + B + 2, 3))
    if 2 * kB + 7 * B + 28 <= 4 * p: return ('P', cdiv(kB + B // 2 + 1, 2))
    return None
def generic_ok(c, kind, m):
    """every generic-regime inequality of Lemma IS (exact), and realisability."""
    p, kB, B, n, d0 = c.p, c.kB, c.B, c.n, c.delta
    chk = {}
    if kind == 'S':
        y = m
        chk['S1'] = 2 * m - kB >= (m + B) // 2 + 1
        chk['S2'] = p - m >= (m + 1 + B) // 2 + 1
        chk['S3'] = m <= d0 - 3
        chk['S4_realisable'] = m <= cdiv(n - 3, 2)
    else:
        y = 2 * m
        chk['P1'] = 2 * m >= kB + B // 2 + 1
        chk['P2'] = 2 * m <= p - (B + 1) // 2 - 1
        chk['P3_realisable'] = m <= cdiv(n - B - 4, 3)
    chk['smallB'] = d0 >= 2 * B + 2
    # the generic values themselves (consequences, checked directly)
    for d in (+1, -1):
        chk['lamQ_gen'] = c.lam(y, m) == (y + B) // 2 + 1
        chk['lamQt_gen_%d' % d] = c.lam(y + d, m + 1) == (y + d + B) // 2 + 1
        chk['UQ_gen'] = c.U(y, m) == cdiv(d0 + y, 2) - 1
        chk['UQt_gen_%d' % d] = c.U(y + d, m + 1) == cdiv(d0 + y + d, 2) - 1
    return chk, y
def seeds(c, y, m):
    out = {}
    for d in (+1, -1):
        lo = c.lam(y + d, m + 1) - c.U(y, m); hi = c.U(y + d, m + 1) - c.lam(y, m)
        out[d] = (lo, hi)
    return out
def closed_seed(c, y, d):
    B, D = c.B, c.delta
    if d == 1:
        return ((B + 1) // 2 + 2 - cdiv(D, 2), D // 2 - B // 2 - 1) if y % 2 == 0 else (B // 2 + 2 - D // 2, cdiv(D, 2) - (B + 1) // 2 - 1)
    return ((B - 1) // 2 + 2 - cdiv(D, 2), D // 2 - B // 2 - 2) if y % 2 == 0 else (B // 2 + 1 - D // 2, cdiv(D, 2) - (B + 1) // 2 - 2)

def partA(PA):
    stats = {'classes': 0, 'fail': 0, 'region_not_E': [], 'by_kind': {'S': 0, 'P': 0}}
    fails = []
    for p in [q for q in range(11, PA + 1) if isprime(q)]:
        for kB in range(1, p):
            for B in range(2, p):
                if not in_region(p, kB, B): continue
                c = Cls(p, kB, B)
                cf = config(c)
                if cf is None:
                    stats['region_not_E'].append((p, kB, B)); continue
                stats['classes'] += 1; stats['by_kind'][cf[0]] += 1
                kind, m = cf
                chk, y = generic_ok(c, kind, m)
                sd = seeds(c, y, m)
                D = c.delta
                L1a, U1a = c.lam(1, 1), c.U(1, 1); L1n, U1n = c.lam(-1, 1), c.U(-1, 1)
                (al, ah), (nl, nh) = sd[1], sd[-1]
                chk['closed_al'] = sd[1] == closed_seed(c, y, 1)
                chk['closed_an'] = sd[-1] == closed_seed(c, y, -1)
                chk['realbound_al'] = 2 * al >= B - D + 3 and 2 * ah <= D - B - 1
                chk['realbound_an'] = 2 * nl >= B - D + 1 and 2 * nh <= D - B - 3
                chk['nowrap_al'] = al + p > U1a and ah - p < L1a and ah >= L1a
                chk['nowrap_an'] = nl + p > U1n and nh - p < L1n and nh >= L1n
                chk['canon'] = L1a == 2 - kB and L1n == -kB
                lo_al, hi_al = max(L1a, al), min(U1a, ah)
                lo_an, hi_an = max(L1n, nl), min(U1n, nh)
                chk['nonempty'] = lo_al <= hi_al and lo_an <= hi_an
                # 2-run steps: types y in {2, 0, -2}, m in {1, 2}
                ok2 = True
                for (ya, la, ha, lb, hb) in ((2, lo_al, hi_al, lo_al, hi_al), (0, lo_al, hi_al, lo_an, hi_an), (-2, lo_an, hi_an, lo_an, hi_an)):
                    for mm in (1, 2):
                        if not (la + lb >= c.U(ya, mm) + 1 - p and ha + hb <= p + c.lam(ya, mm) - 1): ok2 = False
                chk['two_run_steps'] = ok2
                # pin: anti singleton {a}, complement type (n - (B - 1), 1)
                yc = c.n - (B - 1)
                chk['pin'] = lo_an + c.lam(yc, 1) >= 1 and hi_an + c.U(yc, 1) <= 2 * p - 1
                # targets of the >= 3-run steps vs the analytic bound ceil((delta - B + 2)/2)
                bound = cdiv(D - B + 2, 2)
                chk['targets'] = max(1 - lo_al, hi_al + 1, 1 - lo_an, hi_an + 1) <= bound
                bad = [kk for kk, v in chk.items() if not v]
                if bad:
                    stats['fail'] += 1
                    if len(fails) < 10: fails.append((p, kB, B, kind, m, bad))
    return stats, fails

def partB(PB, PT):
    out = {'classes': 0, 'triples': 0, 'bound_fail': 0, 'type_steps': 0, 'type_fail': 0, 'min_slack': None}
    ex = []
    for p in [q for q in range(11, PB + 1) if isprime(q)]:
        for kB in range(1, p):
            for B in range(2, p):
                if not in_region(p, kB, B): continue
                c = Cls(p, kB, B)
                cf = config(c)
                if cf is None: continue
                out['classes'] += 1
                n, k, D = c.n, c.k, c.delta
                half = (D - B + 2) / 2
                for d, ylo, yhi in ((+1, 1 - B, n), (-1, -B, n - 1)):
                    for y in range(ylo, yhi + 1):
                        for m in range(1, k // 2 + 1):
                            for mp in (m, m - 1):
                                if mp < 1: continue
                                out['triples'] += 1
                                s1 = c.lam(y - d, mp) + c.lamc(y, m)
                                s2 = c.lam(y, m) + c.lamc(y - d, mp)
                                sl = min(s1, s2) - half
                                out['min_slack'] = sl if out['min_slack'] is None else min(out['min_slack'], sl)
                                if s1 < half or s2 < half:
                                    out['bound_fail'] += 1
                                    if len(ex) < 6: ex.append((p, kB, B, d, y, m, mp, s1, s2, half))
                if p <= PT:
                    kind, m0 = cf
                    chk, y0 = generic_ok(c, kind, m0)
                    sd = seeds(c, y0, m0)
                    L1a, U1a = c.lam(1, 1), c.U(1, 1); L1n, U1n = c.lam(-1, 1), c.U(-1, 1)
                    rng = {1: (max(L1a, sd[1][0]), min(U1a, sd[1][1])), -1: (max(L1n, sd[-1][0]), min(U1n, sd[-1][1]))}
                    for s in range(2, k):
                        for e in range(0, min(B, s) + 1):
                            j = s - e
                            if j > n or j < 0: continue
                            for m in range(1, min(s, k - s) + 1):
                                y = j - e
                                kinds = []
                                if j >= 1:
                                    if s > m: kinds.append((1, m))
                                    if m >= 2: kinds.append((1, m - 1))
                                if e >= 1:
                                    if s > m: kinds.append((-1, m))
                                    if m >= 2: kinds.append((-1, m - 1))
                                for (dt, mp) in kinds:
                                    yp = y - dt
                                    if s == 2:
                                        rem_al = j - (1 if dt == 1 else 0)
                                        lo1, hi1 = rng[1] if rem_al == 1 else rng[-1]
                                    else:
                                        lo1, hi1 = c.lam(yp, mp), c.U(yp, mp)
                                    at, bt = rng[dt]
                                    out['type_steps'] += 1
                                    if not (lo1 + at >= c.U(y, m) + 1 - p and hi1 + bt <= p + c.lam(y, m) - 1):
                                        out['type_fail'] += 1
                                        if len(ex) < 12: ex.append(('type', p, kB, B, s, j, e, m, dt, mp))
    return out, ex

def partC(PC):
    fails = []; n = 0; small = []
    for p in [q for q in range(11, PC + 1) if isprime(q)]:
        for kB in range(1, p):
            for B in range(2, p):
                if not in_region(p, kB, B): continue
                n += 1
                if not cond_E(p, kB, B):
                    if p >= 19: fails.append((p, kB, B))
                    else: small.append((p, kB, B))
                else:
                    c = Cls(p, kB, B); kind, m = config(c)
                    chk, y = generic_ok(c, kind, m)
                    if not all(chk.values()) and p >= 19: fails.append((p, kB, B, kind, m, [kk for kk, v in chk.items() if not v]))
    return {'classes': n, 'fail_p_ge_19': len(fails), 'examples': fails[:5], 'region_minus_E_p_le_17': small}

def partD(PB):
    res = {}
    # D1: canonical ranges for all runs; D2: seeds widened by w
    for label, widen, canon in (('D1_canonical', 0, True), ('D2_w1', 1, False), ('D2_w2', 2, False), ('D2_w3', 3, False)):
        steps = fails = 0
        for p in [q for q in range(11, PB + 1) if isprime(q)]:
            for kB in range(1, p):
                for B in range(2, p):
                    if not in_region(p, kB, B) or not cond_E(p, kB, B): continue
                    c = Cls(p, kB, B); kind, m0 = config(c)
                    chk, y0 = generic_ok(c, kind, m0); sd = seeds(c, y0, m0)
                    L1a, U1a = c.lam(1, 1), c.U(1, 1); L1n, U1n = c.lam(-1, 1), c.U(-1, 1)
                    if canon: rng = {1: (L1a, U1a), -1: (L1n, U1n)}
                    else: rng = {1: (max(L1a, sd[1][0]) - widen, min(U1a, sd[1][1]) + widen), -1: (max(L1n, sd[-1][0]) - widen, min(U1n, sd[-1][1]) + widen)}
                    n, k = c.n, c.k
                    for s in range(2, k):
                        for e in range(0, min(B, s) + 1):
                            j = s - e
                            if j > n or j < 0: continue
                            for m in range(1, min(s, k - s) + 1):
                                y = j - e
                                kinds = []
                                if j >= 1:
                                    if s > m: kinds.append((1, m))
                                    if m >= 2: kinds.append((1, m - 1))
                                if e >= 1:
                                    if s > m: kinds.append((-1, m))
                                    if m >= 2: kinds.append((-1, m - 1))
                                for (dt, mp) in kinds:
                                    yp = y - dt
                                    if s == 2:
                                        rem_al = j - (1 if dt == 1 else 0)
                                        lo1, hi1 = rng[1] if rem_al == 1 else rng[-1]
                                    else:
                                        lo1, hi1 = c.lam(yp, mp), c.U(yp, mp)
                                    at, bt = rng[dt]
                                    steps += 1
                                    if not (lo1 + at >= c.U(y, m) + 1 - p and hi1 + bt <= p + c.lam(y, m) - 1): fails += 1
        res[label] = (steps, fails)
    # D3: just outside the small-B region (2B + kB = p - 1): count classes where some generic check or real bound fails
    cnt = tot = 0
    for p in [q for q in range(11, 200) if isprime(q)]:
        for kB in range(1, p):
            B2 = p - 1 - kB
            if B2 % 2: continue
            B = B2 // 2
            if B < 2: continue
            c = Cls(p, kB, B)
            for kind, m in (('S', cdiv(2 * kB + B + 2, 3)), ('P', cdiv(kB + B // 2 + 1, 2))):
                tot += 1
                chk, y = generic_ok(c, kind, m)
                if not all(chk.values()): cnt += 1
    res['D3_outside_region_generic_fail'] = (cnt, tot)
    return res

if __name__ == '__main__':
    PA, PB, PT, PC = (int(v) for v in sys.argv[1:5])
    t0 = time.time()
    print('== seedB.py start', time.strftime('%Y-%m-%dT%H:%M:%S'), flush=True)
    A, fa = partA(PA)
    print('Part A (primes 11..%d):' % PA, {'classes': A['classes'], 'fail': A['fail'], 'by_kind': A['by_kind'], 'region_not_E': A['region_not_E'][:20], 'n_region_not_E': len(A['region_not_E'])}, 'first_failures', fa, flush=True)
    Bo, eb = partB(PB, PT)
    print('Part B (bounds primes 11..%d, type steps primes 11..%d):' % (PB, PT), Bo, 'examples', eb, flush=True)
    C = partC(PC)
    print('Part C (Claim E, primes 11..%d):' % PC, C, flush=True)
    D = partD(min(PB, 23))
    print('Part D (mutation controls, primes 11..%d; D3 primes < 200):' % min(PB, 23), D, flush=True)
    print('== seedB.py end %.1f s' % (time.time() - t0), flush=True)
