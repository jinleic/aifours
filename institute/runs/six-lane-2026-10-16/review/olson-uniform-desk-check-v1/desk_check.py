"""Desk spot-check (OlsonUniformReviewDesk), own code, no lane imports, no claimant code.
Exact integer arithmetic only.  Parts:
 R: RZ-wide class arithmetic (recipe, availability inequalities, genericity of the four arcs, GS(b) quality bounds, NW).
 S: S2-wide class arithmetic (recipe, footprint, exceptional set, genericity, exceptional seed table, QS) + c=1 ablation.
 K: constructive availability smoke on explicit cyclic words (proof algorithms of Lemma R1 / packing lemma, followed literally).
 C: C0-all chain on random NMH run structures and random integer vectors in singleton windows with sum p
    (A0 first-prefix kill, Case-B identity (2.2), bound (3.1), (B1+) count, (B2+) kill for cases (i)/(iii), C0W kill for (ii)).
Mutation controls: R-mut (c forced to 1), S-mut (no exception split), C-mut (A0 target g instead of g+1).
"""
import json, random, sys, time
from math import isqrt

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, isqrt(n) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]

def fl2(a): return a // 2            # floor(a/2), Python floor division is exact for negatives
def ce2(a): return -((-a) // 2)      # ceil(a/2)

class Par:
    def __init__(s, p, g, B, E=0):
        s.p, s.g, s.B, s.E = p, g, B, E
        s.kappa = g + B; s.A = p + g + E // 2; s.Delta0 = p - s.kappa - E // 2
    def lam(s, v, b): return min(s.p - b + 1, v + b - s.g, fl2(v + s.B) + 1)
    def lamc(s, v, b): return min(s.p - b + 1, (s.A - s.kappa) - v + b, fl2(s.A - v) + 1)
    def U(s, v, b): return s.p - s.lamc(v, b)
    def generic(s, v, b): return s.lam(v, b) == fl2(v + s.B) + 1 and s.lamc(v, b) == fl2(s.A - v) + 1
    def seed(s, y, m, d):
        slo = s.lam(y + d, m + 1) - s.U(y, m); shi = s.U(y + d, m + 1) - s.lam(y, m)
        return slo, shi
    def qs(s, slo, shi, d):  # 2*slo >= d - Delta0 + 2 and 2*shi <= d + Delta0 - 2
        return 2 * slo >= d - s.Delta0 + 2 and 2 * shi <= d + s.Delta0 - 2
    def nw(s, slo, shi, d):
        l1, u1 = s.lam(d, 1), s.U(d, 1)
        return l1 - shi > -s.p and u1 - slo < s.p

def part_R(P, force_c1=False):
    res = {'classes': 0, 'targets': 0, 'fail': 0, 'fails': [], 'actual_empty_class_signs': 0}
    for p in primes_upto(P):
        if p < 7: continue
        for g in range(1, p):
            for B in range(g + 1, p):
                if g + B > p - 3: break
                pr = Par(p, g, B); kap = g + B; n = p + g; k = p + kap
                m = ce2(kap); r = m - g
                c = 1 if (force_c1 or r % 2 == 1) else 2
                y = g + c
                ok = (r >= 1) and ((m - y) % 2 == 0) and (m - y >= 0)
                i = (m - y) // 2; j = (m + y) // 2
                ok = ok and i >= 0 and j >= 0 and i + j == m and j - i == y
                ok = ok and (i == 0 or 2 * i <= B - 3) and 2 * m <= n - 3 and 2 * m + 2 <= k
                res['classes'] += 1
                for d in (1, -1):
                    res['targets'] += 1
                    good = ok and pr.generic(y, m) and pr.generic(y + d, m + 1)
                    slo, shi = pr.seed(y, m, d)
                    good = good and pr.qs(slo, shi, d) and pr.nw(slo, shi, d)
                    if good and max(pr.lam(d, 1), slo) > min(pr.U(d, 1), shi): res['actual_empty_class_signs'] += 1
                    if not good:
                        res['fail'] += 1
                        if len(res['fails']) < 5: res['fails'].append((p, g, B, d))
    return res

TABLE = {(3, 0): ((0, 1, 1, 1, 0, 0), (0, 1), (-1, 0)), (3, 2): ((0, 0, 0, 0, -1, 0), (0, 0), (-1, 0)),
         (3, 4): ((-1, -1, -1, -1, -2, -1), (0, 0), (-1, 0)), (4, 1): ((0, 1, 1, 1, 0, 0), (0, 1), (-1, 0)),
         (5, 0): ((0, 2, 1, 2, 0, 1), (-1, 2), (-2, 1))}

def part_S(P, force_c1=False, no_split=False):
    res = {'classes': 0, 'default': 0, 'exceptional': {}, 'fail': 0, 'fails': [], 'table_mismatch': 0}
    for p in primes_upto(P):
        if p < 7: continue
        for B in range(2, p):
            for g in range(B, p):
                if g + B > p - 3: break
                pr = Par(p, g, B); kap = g + B; n = p + g; Delta = p - kap; h = g - B; q = h // 2
                m = ce2(kap); assert m == B + ce2(h)
                c = 1 if (force_c1 or q % 2 == 1) else 2
                y = g + c; j2 = y - m; j1 = 2 * m - y
                res['classes'] += 1
                fits = 3 * j2 + 2 * j1 <= n - B - 4
                assert 3 * j2 + 2 * j1 == m + y and (m + y) - (n - B - 4) == c + 4 - Delta - q
                good = True
                if fits or no_split:
                    res['default'] += 1
                    good = fits and j2 >= 0 and j1 >= 0
                    for d in (1, -1):
                        slo, shi = pr.seed(y, m, d)
                        good = good and pr.generic(y, m) and pr.generic(y + d, m + 1) and pr.qs(slo, shi, d) and pr.nw(slo, shi, d)
                else:
                    key = (Delta, h)
                    res['exceptional'][str(key)] = res['exceptional'].get(str(key), 0) + 1
                    if key not in TABLE: good = False
                    else:
                        if key == (3, 4): mm, yy, jj2, jj1 = g - 1, g, 1, g - 2; good = 3 * jj2 + 2 * jj1 <= n - B - 4 and jj1 >= 0
                        else: mm, yy = g, g; good = 2 * g <= n - 3
                        vals = (pr.lam(yy, mm) - g, pr.U(yy, mm) - g, pr.lam(yy + 1, mm + 1) - g, pr.U(yy + 1, mm + 1) - g,
                                pr.lam(yy - 1, mm + 1) - g, pr.U(yy - 1, mm + 1) - g)
                        if vals != TABLE[key][0]: res['table_mismatch'] += 1; good = False
                        for d, want in ((1, TABLE[key][1]), (-1, TABLE[key][2])):
                            slo, shi = pr.seed(yy, mm, d)
                            good = good and (slo, shi) == want and pr.qs(slo, shi, d) and pr.nw(slo, shi, d)
                if not good:
                    res['fail'] += 1
                    if len(res['fails']) < 8: res['fails'].append((p, g, B))
    return res

# ---------- K: constructive availability on explicit cyclic words ----------
def path_from(k, t):
    return [(t + 2 + s) % k for s in range(k - 3)]  # t+2, ..., t-2

def intervals(seq, pred):
    out, cur = [], []
    for u in seq:
        if pred(u): cur.append(u)
        else:
            if cur: out.append(cur); cur = []
    if cur: out.append(cur)
    return out

def blocks_cyclic(Q, k):
    if not Q: return 0
    if len(Q) == k: return 0
    return sum(1 for u in Q if (u - 1) % k not in Q)

def construct_R1(signs, t, i, j):
    k = len(signs); path = path_from(k, t); pos = {u: s for s, u in enumerate(path)}
    anti_cands = [iv[s] for iv in intervals(path, lambda u: signs[u] < 0) for s in range(0, len(iv), 2)]
    if len(anti_cands) < i: return None
    chosen_anti = anti_cands[:i]
    removed = set(chosen_anti)
    for u in chosen_anti:
        sidx = pos[u]
        for nb in (sidx - 1, sidx + 1):
            if 0 <= nb < len(path): removed.add(path[nb])
    al_cands = [iv[s] for iv in intervals(path, lambda u: signs[u] > 0 and u not in removed) for s in range(0, len(iv), 2)]
    if len(al_cands) < j: return None
    return set(chosen_anti) | set(al_cands[:j])

def construct_pack(signs, t, j2, j1):
    k = len(signs); path = path_from(k, t)
    ivs = intervals(path, lambda u: signs[u] > 0)
    plan = [[iv, 0] for iv in ivs]; need = j2
    for e in plan:
        take = min(need, (len(e[0]) + 1) // 3); e[1] = take; need -= take
    if need: return None
    Q = set(); singles_needed = j1
    for iv, npairs in plan:
        s = 0
        for _ in range(npairs): Q.add(iv[s]); Q.add(iv[s + 1]); s += 3
        while singles_needed and s < len(iv): Q.add(iv[s]); singles_needed -= 1; s += 2
    if singles_needed: return None
    return Q

def check_config(signs, t, Q, want_y, want_m):
    k = len(signs)
    if Q is None or t in Q: return False
    if (t - 1) % k in Q or (t + 1) % k in Q: return False
    y = sum(signs[u] for u in Q); m = blocks_cyclic(Q, k)
    Qt = Q | {t}
    return y == want_y and m == want_m and blocks_cyclic(Qt, k) == want_m + 1 and 0 < len(Q) and len(Qt) < k

def part_K(rng, primes, per_class):
    res = {'R_words': 0, 'R_targets': 0, 'R_fail': 0, 'S_words': 0, 'S_targets': 0, 'S_fail': 0, 'fails': []}
    for p in primes:
        for g in range(1, p):
            for B in range(1, p):
                kap = g + B
                if kap > p - 3 or not (B >= g + 1 or g >= B >= 2): continue
                n = p + g; k = n + B
                if B >= g + 1:
                    m = ce2(kap); r = m - g; c = 1 if r % 2 else 2; y = g + c; i = (m - y) // 2; j = (m + y) // 2
                    for _ in range(per_class):
                        anti = set(rng.sample(range(k), B)); signs = [-1 if u in anti else 1 for u in range(k)]
                        res['R_words'] += 1
                        for t in range(k):
                            res['R_targets'] += 1
                            if not check_config(signs, t, construct_R1(signs, t, i, j), y, m):
                                res['R_fail'] += 1
                                if len(res['fails']) < 5: res['fails'].append(('R', p, g, B, t))
                elif g >= B >= 2:
                    Delta = p - kap; h = g - B; q = h // 2; m = ce2(kap); c = 1 if q % 2 else 2; y = g + c
                    if (Delta, h) in TABLE:
                        if (Delta, h) == (3, 4): m, y, j2, j1 = g - 1, g, 1, g - 2
                        else: m, y, j2, j1 = g, g, 0, g
                    else: j2, j1 = y - m, 2 * m - y
                    for _ in range(per_class):
                        anti = set(rng.sample(range(k), B)); signs = [-1 if u in anti else 1 for u in range(k)]
                        res['S_words'] += 1
                        for t in range(k):
                            res['S_targets'] += 1
                            if not check_config(signs, t, construct_pack(signs, t, j2, j1), y, m):
                                res['S_fail'] += 1
                                if len(res['fails']) < 5: res['fails'].append(('S', p, g, B, t))
    return res

def part_K_block_layouts(primes):
    """deterministic adversarial layouts: anti runs in one block, alternating, and block adjacent to t."""
    res = {'words': 0, 'targets': 0, 'fail': 0, 'fails': []}
    for p in primes:
        for g in range(1, p):
            for B in range(1, p):
                kap = g + B
                if kap > p - 3: continue
                if not (B >= g + 1 or g >= B >= 2): continue
                n = p + g; k = n + B
                layouts = [set(range(B)), set(range(0, 2 * B, 2)) if 2 * B <= k else set(range(B)), set(range(k - B // 2, k)) | set(range(B - B // 2))]
                for anti in layouts:
                    signs = [-1 if u in anti else 1 for u in range(k)]; res['words'] += 1
                    if B >= g + 1:
                        m = ce2(kap); r = m - g; c = 1 if r % 2 else 2; y = g + c; i = (m - y) // 2; j = (m + y) // 2
                        build = lambda t: construct_R1(signs, t, i, j)
                    else:
                        Delta = p - kap; h = g - B; q = h // 2; m = ce2(kap); c = 1 if q % 2 else 2; y = g + c
                        if (Delta, h) in TABLE:
                            if (Delta, h) == (3, 4): m, y, j2, j1 = g - 1, g, 1, g - 2
                            else: m, y, j2, j1 = g, g, 0, g
                        else: j2, j1 = y - m, 2 * m - y
                        build = lambda t: construct_pack(signs, t, j2, j1)
                    for t in range(k):
                        res['targets'] += 1
                        if not check_config(signs, t, build(t), y, m):
                            res['fail'] += 1
                            if len(res['fails']) < 5: res['fails'].append((p, g, B, sorted(anti), t))
    return res

# ---------- C: C0-all chain on random NMH run structures ----------
def random_nmh(rng, p, tries=2000):
    for _ in range(tries):
        k = rng.randint(p + 1, 2 * p - 3)
        runs = []
        for _t in range(k):
            r = rng.random()
            if r < 0.70: runs.append(('al', rng.choice([1, 1, 1, 1, 2, 2, 3])))
            elif r < 0.92: runs.append(('an', rng.choice([1, 1, 1, 2, 3])))
            else: runs.append(('pr', 0))
        if not any(tp == 'al' for tp, _ in runs): continue
        A = sum(a for tp, a in runs if tp == 'al') + sum(1 for tp, _ in runs if tp == 'pr')
        B = sum(b for tp, b in runs if tp == 'an') + sum(1 for tp, _ in runs if tp == 'pr')
        R = A + B; E = R - k
        if E % 2 or B < 1: continue
        kappa = R - p - E // 2; g = kappa - B
        if g < 1 or A > 2 * p - 1 or k < 2 * kappa + 3 or R + k > 4 * p - 2: continue
        d = [(a if tp == 'al' else (-a if tp == 'an' else 0)) for tp, a in runs]
        return dict(p=p, k=k, runs=runs, d=d, A=A, B=B, E=E, kappa=kappa, g=g)
    return None

def composition(rng, total, parts):
    """random composition of total into `parts` positive integers"""
    if parts == 0: return [] if total == 0 else None
    if total < parts: return None
    cuts = sorted(rng.sample(range(1, total), parts - 1)) if parts > 1 else []
    bounds = [0] + cuts + [total]
    return [bounds[i + 1] - bounds[i] for i in range(parts)]

def random_nmh_param(rng, p, tries=200):
    """uniform admissible (g, B, E) for p, then a random run structure with exactly these parameters"""
    tuples = [(g, B, E) for g in range(1, p) for B in range(1, p) for E in range(0, p, 2) if g + B + E // 2 <= p - 3]
    for _ in range(tries):
        g, B, E = rng.choice(tuples)
        kappa = g + B; k = p + kappa - E // 2; A = p + g + E // 2
        n_pr = rng.randint(0, min(B, E))
        n_an = rng.randint(1 if B - n_pr >= 1 else 0, B - n_pr) if B - n_pr >= 1 else 0
        if B - n_pr >= 1 and n_an == 0: continue
        n_al = k - n_an - n_pr
        if n_al < 1 or A - n_pr < n_al: continue
        al = composition(rng, A - n_pr, n_al); an = composition(rng, B - n_pr, n_an)
        if al is None or an is None: continue
        runs = [('al', a) for a in al] + [('an', b) for b in an] + [('pr', 0)] * n_pr
        rng.shuffle(runs)
        Aw = sum(a for tp, a in runs if tp == 'al') + n_pr; Bw = sum(b for tp, b in runs if tp == 'an') + n_pr
        R = Aw + Bw; Ew = R - k
        if Ew != E or Aw != A or Bw != B: continue
        if A > 2 * p - 1 or k < 2 * kappa + 3 or k < p + 1 or R + k > 4 * p - 2: continue
        d = [(a if tp == 'al' else (-a if tp == 'an' else 0)) for tp, a in runs]
        return dict(p=p, k=k, runs=runs, d=d, A=A, B=B, E=E, kappa=kappa, g=g)
    return None

def run_C(rng, words_per_p, vecs_per_word, primes, mut_target_g=False, gen=None, biased=False):
    res = {'words': 0, 'vectors': 0, 'caseA': 0, 'caseB': 0, 'B_i': 0, 'B_ii': 0, 'B_iii': 0, 'fail': 0, 'fails': [],
           'identity22_checked': 0, 'bound31_checked': 0}
    for p in primes:
        for _w in range(words_per_p):
            W = (gen or random_nmh)(rng, p)
            if W is None: continue
            res['words'] += 1
            k, d, g, B, E = W['k'], W['d'], W['g'], W['B'], W['E']
            pr = Par(p, g, B, E)
            assert pr.A == W['A'] and pr.Delta0 == 2 * p - (W['A'] + W['B'])
            lo = [pr.lam(dt, 1) for dt in d]; hi = [pr.U(dt, 1) for dt in d]
            if sum(lo) > p or sum(hi) < p: continue
            types = [tp for tp, _ in W['runs']]
            def lamQ(Q): return pr.lam(sum(d[u] for u in Q), blocks_cyclic(Q, k))
            blo, bhi = lo[:], hi[:]
            if biased:  # steer towards Case B: aligned non-defects, anti/pair defects with c <= 0
                for t in range(k):
                    if types[t] == 'al': blo[t] = max(lo[t], ce2(d[t] + 1))
                    else: blo[t], bhi[t] = max(lo[t], d[t]), min(hi[t], fl2(d[t]))
                if any(blo[t] > bhi[t] for t in range(k)) or sum(blo) > p or sum(bhi) < p: blo, bhi = lo[:], hi[:]
            for _v in range(vecs_per_word):
                x = []; rem_lo = sum(blo); rem_hi = sum(bhi); s = 0
                for t in range(k):
                    rem_lo -= blo[t]; rem_hi -= bhi[t]
                    a = max(blo[t], p - s - rem_hi); b = min(bhi[t], p - s - rem_lo)
                    v = rng.randint(a, b); x.append(v); s += v
                assert s == p and all(lo[t] <= x[t] <= hi[t] for t in range(k))
                res['vectors'] += 1
                bh = [2 * x[t] - d[t] for t in range(k)]; c = [d[t] - x[t] for t in range(k)]
                Z = [t for t in range(k) if bh[t] <= 0]; Zs = set(Z)
                assert 0 < len(Z) < k
                Phi = lambda Q: sum(c[u] for u in Q) + blocks_cyclic(set(Q), k)
                target = g if mut_target_g else g + 1
                killed = None
                if Phi(Z) >= g + 1:
                    res['caseA'] += 1
                    order = Z[:]; rng.shuffle(order); P = []
                    for t in order:
                        P.append(t)
                        if Phi(P) >= target: break
                    Ps = set(P); X = sum(x[u] for u in Ps); m = blocks_cyclic(Ps, k)
                    ok = (Phi(P) >= g + 1 and sum(bh[u] for u in Ps) <= B and X + m <= p and X < lamQ(Ps) and 0 < len(Ps) < k)
                    killed = ok
                else:
                    res['caseB'] += 1
                    Delta = g - Phi(Z)
                    f = [fl2(d[t] - 1) for t in range(k)]
                    eps = [c[t] - f[t] for t in range(k)]
                    sur = -sum(eps[t] for t in range(k) if t not in Zs)
                    n_ev = sum(1 for t in range(k) if d[t] % 2 == 0)
                    mZ = blocks_cyclic(Zs, k)
                    ident = (2 * Delta == -2 * sum(f[t] for t in Z) - 2 * mZ - n_ev - 2 * sur) and sur >= 0
                    res['identity22_checked'] += 1
                    n_ev_al = sum(1 for t in range(k) if types[t] == 'al' and d[t] % 2 == 0)
                    n_an = sum(1 for t in range(k) if types[t] == 'an'); n_pr = sum(1 for t in range(k) if types[t] == 'pr')
                    b31 = n_ev_al <= B + n_an - 2
                    res['bound31_checked'] += 1
                    Xset = [u for u in range(k) if types[u] == 'al' and u not in Zs and eps[u] == 0
                            and (u - 1) % k not in Zs and (u + 1) % k not in Zs]
                    Xo = [u for u in Xset if d[u] % 2 == 1]
                    s0x2 = 2 * (k - g - 2 * B) + (n_pr - n_ev_al)
                    b1 = 2 * len(Xo) >= 4 * Delta + s0x2  # |Xo| >= 2Delta + s0 (doubled)
                    if len(Xo) == 2 * Delta + 1: res['tight_Xo'] = res.get('tight_Xo', 0) + 1
                    ok = ident and b31 and b1
                    if B <= g or 3 * g + 1 > p:
                        if B <= g: res['B_i'] += 1; ok = ok and s0x2 >= 2
                        else: res['B_iii'] += 1; ok = ok and s0x2 >= 1
                        Xos = set(Xo); S2 = []
                        seqZ = [(Z[0] + s) % k for s in range(k)]  # start inside Z (disjoint from Xo): cyclic blocks become paths
                        for iv in intervals(seqZ, lambda u: u in Xos):
                            S2 += iv[0::2]
                        assert all((u + 1) % k not in S2 for u in S2)
                        if len(S2) < Delta + 1: ok = False
                        else:
                            Q = Zs | set(S2[:Delta + 1])
                            X = sum(x[u] for u in Q); m = blocks_cyclic(Q, k)
                            ok = ok and (Phi(list(Q)) >= g + 1 and sum(bh[u] for u in Q) <= B and X + m <= p and X < lamQ(Q) and len(Q) < k)
                    else:
                        res['B_ii'] += 1
                        cheap = [t for t in range(k) if c[t] >= 0 and bh[t] <= 1]
                        w = {t: c[t] + 1 for t in cheap}
                        ok = ok and all(1 <= w[t] <= g for t in cheap)
                        cs = set(cheap)
                        if len(cheap) < k:
                            start = next(t for t in range(k) if t not in cs)
                            seq = [(start + s) % k for s in range(k)]
                            U = []
                            for iv in intervals(seq, lambda u: u in cs):
                                e0, e1 = iv[0::2], iv[1::2]
                                U += e0 if sum(w[u] for u in e0) >= sum(w[u] for u in e1) else e1
                        else:
                            t0 = 0; seq = [(t0 + 1 + s) % k for s in range(k - 1)]
                            e0, e1 = seq[0::2], seq[1::2]
                            U = e0 if sum(w[u] for u in e0) >= sum(w[u] for u in e1) else e1
                        ok = ok and sum(w[u] for u in U) >= g + 1
                        U.sort(key=lambda u: -w[u]); S = []; acc = 0
                        for u in U:
                            S.append(u); acc += w[u]
                            if acc >= g + 1: break
                        S.sort(key=lambda u: bh[u] > 0); P = []; acc = 0
                        for u in S:
                            P.append(u); acc += w[u]
                            if acc >= g + 1: break
                        Ps = set(P); X = sum(x[u] for u in Ps); m = blocks_cyclic(Ps, k)
                        ok = ok and (Phi(P) >= g + 1 and sum(bh[u] for u in Ps) <= B and X + m <= p and X < lamQ(Ps) and len(Ps) < k)
                    killed = ok
                if not killed:
                    res['fail'] += 1
                    if len(res['fails']) < 5: res['fails'].append((p, W['runs'], x))
    return res

def main():
    t0 = time.time(); out = {}
    out['R'] = part_R(401); out['R_mut_c1'] = part_R(401, force_c1=True)
    out['S'] = part_S(401); out['S_mut_c1'] = part_S(401, force_c1=True); out['S_mut_nosplit'] = part_S(401, no_split=True)
    rng = random.Random(20261017)
    out['K_random'] = part_K(rng, [7, 11, 13, 17, 19, 23, 29, 31], 6)
    out['K_layouts'] = part_K_block_layouts([7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43])
    rngC = random.Random(1017)
    out['C'] = run_C(rngC, 40, 25, [5, 7, 11, 13, 17, 19, 23])
    out['C_mut_target_g'] = run_C(random.Random(1017), 40, 25, [5, 7, 11, 13, 17, 19, 23], mut_target_g=True)
    out['C_param'] = run_C(random.Random(2017), 60, 20, [7, 11, 13, 17, 19, 23, 29, 31], gen=random_nmh_param)
    out['C_param_mut_target_g'] = run_C(random.Random(2017), 60, 20, [7, 11, 13, 17, 19, 23, 29, 31], mut_target_g=True, gen=random_nmh_param)
    out['C_param_biasedB'] = run_C(random.Random(3017), 80, 20, [7, 11, 13, 17, 19, 23, 29, 31, 37, 41], gen=random_nmh_param, biased=True)
    out['seconds'] = round(time.time() - t0, 1)
    text = json.dumps(out, indent=1, default=str) + '\n'
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'x') as f: f.write(text)   # exclusive create; never overwrite
    sys.stdout.write(text)

if __name__ == '__main__':
    main()
