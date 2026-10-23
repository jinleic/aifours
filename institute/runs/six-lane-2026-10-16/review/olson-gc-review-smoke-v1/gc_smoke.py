#!/usr/bin/env python3
"""Independent stdlib smoke for P/c6/proof-GC.md (desk OlsonGCReviewDesk, 2026-10-18).

Written from the definitions only: lambda from Lemma H with beta = 0 (proof-SEEDG-r2.md Sec. 0), "generic" and the seed
bounds of Lemma GS (a)/(b), Lemma NW and (QS) (proof-SEEDG-r2.md Sec. 1), and the colouring walk exactly as stated in
proof-GC.md Sec. 3.  Part G checks the THEOREM'S CONCLUSION (an identity 2p-subword) directly in D_(2p), using no lemma.
No claimant code is imported, read or executed.  Native limits only (RLIMIT_CPU, RLIMIT_FSIZE); one process.
Usage: /usr/bin/python3 -B gc_smoke.py OUTDIR      (OUTDIR exists and is empty; outputs are created with mode 'x')
"""
import hashlib
import itertools
import json
import random
import resource
import sys
import time
from pathlib import Path

CPU_SOFT = 120
resource.setrlimit(resource.RLIMIT_CPU, (CPU_SOFT, CPU_SOFT + 5))
resource.setrlimit(resource.RLIMIT_FSIZE, (8 << 20, 8 << 20))
OUT = Path(sys.argv[1])
LOG = open(OUT / 'smoke.jsonl', 'x')
sys.stderr = open(OUT / 'smoke.stderr.txt', 'x')
T0 = time.process_time()
BUDGET = {'A': 14.0, 'B': 50.0, 'probe': 72.0, 'G': 108.0}   # cumulative CPU seconds at which a part stops sampling


def cpu():
    return time.process_time() - T0


def emit(rec):
    rec['cpu_s'] = round(cpu(), 2)
    LOG.write(json.dumps(rec, sort_keys=True) + '\n')
    LOG.flush()
    print(json.dumps(rec, sort_keys=True), flush=True)


def ceil2(x):
    return -((-x) // 2)


def popcount(x):
    return bin(x).count('1')


# ----------------------------------------------------------------------------------------------------------- words
def classes(p, delta0_exact=None):
    """NMH parameter classes (k, kappa, B): p+1 <= k <= 2p-2, 1 <= B <= kappa-1, B <= A <= 2p-1, R >= k; in scope Delta0 >= 3."""
    out = []
    for k in range(p + 1, 2 * p - 1):
        for kappa in range(2, k):
            R = 2 * p - k + 2 * kappa
            if R < k:
                continue
            D0 = 2 * p - R
            if (delta0_exact is None and D0 < 3) or (delta0_exact is not None and D0 != delta0_exact):
                continue
            for B in range(1, kappa):
                A = R - B
                if B <= A <= 2 * p - 1:
                    out.append((k, kappa, B))
    return out


def params(p, runs):
    k = len(runs)
    A = sum(a for a, b in runs)
    B = sum(b for a, b in runs)
    R = A + B
    assert (R - 2 * p + k) % 2 == 0
    kappa = (R - 2 * p + k) // 2
    return {'p': p, 'k': k, 'A': A, 'B': B, 'R': R, 'E': R - k, 'kappa': kappa, 'kB': kappa - B, 'D': A - B, 'D0': 2 * p - R}


def nmh_ok(P, runs, max_R):
    p = P['p']
    return (p + 1 <= P['k'] <= 2 * p - 2 and 1 <= P['B'] <= P['kappa'] - 1 and P['B'] <= P['A'] <= 2 * p - 1
            and P['R'] <= max_R and all((a >= 1 and b == 0) or (a == 0 and b >= 1) or (a == 1 and b == 1) for a, b in runs))


def composition(rng, total, parts, conc):
    if parts == 0:
        return []
    if conc:
        out = [1] * parts
        out[rng.randrange(parts)] += total - parts
        return out
    cuts = sorted(rng.sample(range(1, total), parts - 1))
    return [b - a for a, b in zip([0] + cuts, cuts + [total])]


def random_word(rng, p, k, kappa, B, style):
    R = 2 * p - k + 2 * kappa
    A = R - B
    for _ in range(200):
        n_pr = rng.randint(0, min(B, R - k))
        rb, ra = B - n_pr, A - n_pr
        n_an = 0 if rb == 0 else rng.randint(1, rb)
        n_al = k - n_pr - n_an
        if n_al >= 1 and ra >= n_al:
            break
    else:
        return None
    conc = style in ('conc', 'conc-adj')
    runs = [(1, 1)] * n_pr + [(0, b) for b in composition(rng, rb, n_an, conc)] + [(a, 0) for a in composition(rng, ra, n_al, conc)]
    if style == 'antiblock':
        neg = [r for r in runs if r[0] == 0 or r == (1, 1)]
        pos = [r for r in runs if not (r[0] == 0 or r == (1, 1))]
        rng.shuffle(pos)
        runs = neg + pos
    elif style in ('conc-adj', 'longadj'):
        runs.sort(key=lambda r: -(r[0] + r[1]))
        tail = runs[2:]
        rng.shuffle(tail)
        runs = runs[:2] + tail
    else:
        rng.shuffle(runs)
    off = rng.randrange(k)
    return runs[off:] + runs[:off]


class Word:
    def __init__(self, p, runs):
        self.p, self.runs, self.k = p, runs, len(runs)
        self.P = params(p, runs)
        self.d = [a - b for a, b in runs]
        self.full = (1 << self.k) - 1

    def D_of(self, mask):
        return sum(self.d[i] for i in range(self.k) if mask >> i & 1)

    def m_of(self, mask):
        prev = ((mask << 1) | (mask >> (self.k - 1))) & self.full      # bit i set iff run i-1 (cyclic) is in mask
        return popcount(mask & ~prev)

    def lam(self, mask):                                                 # Lemma H, beta = 0, proper patterns only
        assert 0 < mask < self.full
        P = self.P
        y, m = self.D_of(mask), self.m_of(mask)
        return min(P['p'] - m + 1, y + m - P['kB'], (y + P['B']) // 2 + 1)

    def U(self, mask):
        return self.P['p'] - self.lam(self.full ^ mask)

    def generic(self, mask):                                             # Lemma GS (b) definition, explicit complement
        y = self.D_of(mask)
        return self.lam(mask) == (y + self.P['B']) // 2 + 1 and self.lam(self.full ^ mask) == (self.P['A'] - y) // 2 + 1


def gen_closed(P, m, y, slack=0):                                        # Lemma GEN closed form (slack != 0: mutation)
    return abs(4 * m - (P['k'] + 2)) + abs(2 * y - P['D']) <= P['E'] + 2 * P['D0'] + slack


# ---------------------------------------------------------------------------------------- Part A (GEN on patterns)
def part_a_word(w, st):
    k, full, P = w.k, w.full, w.P
    Dm = [0] * (full + 1)
    for mask in range(1, full + 1):
        low = mask & -mask
        Dm[mask] = Dm[mask ^ low] + w.d[low.bit_length() - 1]
    gen = bytearray(full + 1)
    for mask in range(1, full):
        y, m = Dm[mask], w.m_of(mask)
        comp = full ^ mask
        yc, mc = Dm[comp], w.m_of(comp)
        lq = min(P['p'] - m + 1, y + m - P['kB'], (y + P['B']) // 2 + 1)
        lc = min(P['p'] - mc + 1, yc + mc - P['kB'], (yc + P['B']) // 2 + 1)
        g = lq == (y + P['B']) // 2 + 1 and lc == (P['A'] - y) // 2 + 1
        gen[mask] = g
        st['patterns'] += 1
        st['generic'] += g
        st['complement_param_mismatch'] += (m != mc or yc != P['D'] - y)
        st['gen_mismatch'] += (g != gen_closed(P, m, y))
        st['MUT_gen_bound_minus1_mismatch'] += (g != gen_closed(P, m, y, -1))
        st['MUT_gen_bound_plus1_mismatch'] += (g != gen_closed(P, m, y, +1))
        st['MUT_gen_kplus1_mismatch'] += (g != (abs(4 * m - (k + 1)) + abs(2 * y - P['D']) <= P['E'] + 2 * P['D0']))
    for mask in range(1, full):
        st['complement_symmetry_fail'] += (gen[mask] != gen[full ^ mask])
    return gen


def exist_check(w, gen, st):
    full = w.full
    for t in range(w.k):
        bt = 1 << t
        cnt = 0
        for mask in range(1, full):
            if mask & bt or (mask | bt) == full:
                continue
            cnt += gen[mask] and gen[mask | bt]
        st['exist_targets'] += 1
        st['exist_targets_without_generic_config'] += (cnt == 0)
        st['exist_min_count'] = cnt if st['exist_min_count'] is None else min(st['exist_min_count'], cnt)


# -------------------------------------------------------------------------------------------- Part B (Lemma GC)
def gc_target(w, t, st, probe=False):
    """Run the walk of proof-GC.md Sec. 3 literally for target t.  probe=True records instead of asserting."""
    P, k, d, p = w.P, w.k, w.d, w.p
    L = k - 1
    at = [(t + i) % k for i in range(1, L + 1)]                         # position i (1-based) -> run t + i
    m = (k + 4) // 4
    c = abs(4 * m - (k + 2))
    Wp = P['E'] + 2 * P['D0'] - c
    assert c <= 2 and m >= 2 and 2 * m <= L - 1
    dt, D, D0 = d[t], P['D'], P['D0']
    lo = ceil2(D - Wp) + max(0, -dt)
    hi = (D + Wp) // 2 - max(0, dt)
    full_check = k <= 25

    def col_from_b(bv):
        col, prev = [], 0
        for j, bj in enumerate(list(bv) + [L], start=1):
            col.extend([j % 2 == 1] * (bj - prev))
            prev = bj
        return col

    def in_C(col):
        nx = sum(1 for i in range(L) if col[i] and (i == 0 or not col[i - 1]))
        ny = sum(1 for i in range(L) if not col[i] and (i == 0 or col[i - 1]))
        return col[0] and not col[-1] and nx == m and ny == m

    def vX(col):
        return sum(d[at[i]] for i in range(L) if col[i])

    chi0 = [(i <= 2 * m - 1 and i % 2 == 1) for i in range(1, L + 1)]
    star = [not x for x in chi0]
    star[0], star[L - 1] = True, False
    assert in_C(chi0) and in_C(star)
    b0 = [i for i in range(1, L) if chi0[i - 1] != chi0[i]]
    bs = [i for i in range(1, L) if star[i - 1] != star[i]]
    assert b0 == list(range(1, 2 * m)) and len(bs) == 2 * m - 1 and col_from_b(bs) == star
    st['bstar_formula_mismatch'] += (bs != [j + 1 for j in range(1, 2 * m - 1)] + [L - 1])
    b, col = list(b0), list(chi0)
    v = vX(col)
    vs, bseq, npass2 = [v], [tuple(b)], 0

    def move(j, delta):
        nonlocal v
        old = b[j]
        b[j] += delta
        upper = b[j + 1] if j + 1 < len(b) else L
        lower = b[j - 1] if j > 0 else 0
        assert lower < b[j] < upper                                      # strictly increasing boundary vector
        pos = old + 1 if delta > 0 else old                               # the one recoloured position (1-based)
        newc = (j + 1) % 2 == 1 if delta > 0 else (j + 2) % 2 == 1        # colour of the block it joins
        assert col[pos - 1] != newc
        col[pos - 1] = newc
        a = at[pos - 1]
        assert a != t
        v += d[a] if newc else -d[a]
        if full_check:
            assert col_from_b(b) == col and in_C(col) and v == vX(col)
        vs.append(v)
        bseq.append(tuple(b))

    for j in range(2 * m - 2, -1, -1):
        while b[j] < bs[j]:
            move(j, +1)
    for j in range(0, 2 * m - 1):
        while b[j] > bs[j]:
            move(j, -1)
            npass2 += 1
    assert b == bs and col == star and v == vX(col)
    N = len(vs) - 1
    st['walk_len_not_L_minus_2'] += (N != L - 2)
    st['pass2_moves'] += npass2
    st['src_bound_(2m-1)(L-2)_max'] = max(st['src_bound_(2m-1)(L-2)_max'], (2 * m - 1) * (L - 2))
    st['walk_len_max'] = max(st['walk_len_max'], N)
    sigma = D - dt + d[(t + 1) % k] - d[(t - 1) % k]
    maxstep = max(abs(d[a]) for a in range(k) if a != t)
    checks = {
        'sigma_identity': vs[0] + vs[-1] == sigma,
        'S_step_le_Wp_minus_absd': maxstep <= Wp - abs(dt),
        'S_Wp_minus_absd_le_width': Wp - abs(dt) <= hi - lo + 1,
        'M_three_runs_le_E_plus_3_le_Wp': abs(dt) + abs(d[(t + 1) % k]) + abs(d[(t - 1) % k]) <= P['E'] + 3 <= Wp,
        'eq33_lo': 2 * lo <= sigma + 1,
        'eq33_hi': 2 * hi >= sigma - 1,
        'window_nonempty': lo <= hi,
    }
    istar = next((i for i, vv in enumerate(vs) if lo <= vv <= hi), None)
    checks['crossing_found'] = istar is not None
    res = {'checks': checks, 'istar': istar}
    if istar is not None:
        cs = col_from_b(bseq[istar])
        Q = sum(1 << at[i] for i in range(L) if cs[i])
        Y = sum(1 << at[i] for i in range(L) if not cs[i])
        bt = 1 << t
        Qt = Q | bt
        assert not Q & bt and Q and Y and Qt == w.full ^ Y and Qt != w.full
        assert w.m_of(Q) == m and w.m_of(Y) == m and w.D_of(Q) == vs[istar]
        checks['Q_generic'] = w.generic(Q)
        checks['Qt_generic'] = w.generic(Qt)
        checks['Y_generic'] = w.generic(Y)
        checks['Q_contains_t_plus_1'] = bool(Q >> ((t + 1) % k) & 1)
        lam_t, U_t = w.lam(bt), w.U(bt)
        s_lo = w.lam(Qt) - w.U(Q)
        s_hi = w.U(Qt) - w.lam(Q)
        checks['GSb_s_lo'] = 2 * s_lo >= dt - D0 + 2
        checks['GSb_s_hi'] = 2 * s_hi <= dt + D0 - 2
        checks['NW'] = lam_t - s_hi > -p and U_t - s_lo < p
        a_, b_ = max(lam_t, s_lo), min(U_t, s_hi)
        res['actual_empty'] = a_ > b_
        if a_ <= b_:
            checks['seed_is_quality'] = lam_t <= a_ <= b_ <= U_t and 2 * a_ >= dt - D0 + 2 and 2 * b_ <= dt + D0 - 2
        qs_lo, qs_hi = ceil2(dt - D0 + 2), (dt + D0 - 2) // 2
        res['qs_window_meets_canonical'] = max(qs_lo, lam_t) <= min(qs_hi, U_t)
        if not probe:
            # sensitivity mutations on the same walk
            def pick(lo_, hi_):
                i = next((i for i, vv in enumerate(vs) if lo_ <= vv <= hi_), None)
                if i is None:
                    return None
                cc = col_from_b(bseq[i])
                q = sum(1 << at[j] for j in range(L) if cc[j])
                return w.generic(q) and w.generic(q | bt)
            r1 = pick(lo - 1, hi + 1)
            st['MUT_widen1_picks_not_generic'] += (r1 is False)
            r2 = pick(ceil2(D - Wp), (D + Wp) // 2)
            st['MUT_Xonly_picks_not_generic'] += (r2 is False)
            st['MUT_sigma_without_end_terms_wrong'] += (vs[0] + vs[-1] != D - dt)
    return res


def run_target_main(w, t, st, fails):
    st['targets'] += 1
    st['targets_E>=4'] += (w.P['E'] >= 4)
    st['targets_pair'] += (w.runs[t] == (1, 1))
    st['targets_anti'] += (w.d[t] < 0)
    res = gc_target(w, t, st)
    bad = [name for name, ok in res['checks'].items() if ok is False and name != 'Q_contains_t_plus_1']
    if not res['checks'].get('Q_contains_t_plus_1', True):
        st['Q_without_t_plus_1'] += 1
    if res.get('actual_empty'):
        st['actual_empty'] += 1
        st['actual_empty_with_qs_window_nonempty'] += res['qs_window_meets_canonical']
    if res['istar'] is not None:
        st['istar_max'] = max(st['istar_max'], res['istar'])
    if bad:
        st['failures'] += 1
        if len(fails) < 10:
            fails.append({'p': w.p, 'runs': w.runs, 't': t, 'bad': bad})


# -------------------------------------------------------------------------------------------- Part G (group level)
def group_ops(p):
    full = (1 << p) - 1
    REV = [0] * (1 << p)
    for msk in range(1 << p):
        r = 0
        for j in range(p):
            if msk >> j & 1:
                r |= 1 << ((-j) % p)
        REV[msk] = r

    def rot(x, s):
        s %= p
        return (((x << s) | (x >> (p - s))) & full) if s else x

    def mul_rot(mask, s):                       # right multiplication by r^s: (f, j) -> (f, j + s)
        return rot(mask & full, s) | (rot(mask >> p, s) << p)

    def mul_ref(mask, v):                       # right multiplication by s r^v: (f, j) -> (1 - f, v - j)
        return rot(REV[mask >> p], v) | (rot(REV[mask & full], v) << p)
    return mul_rot, mul_ref


def dp_extend(reach, top, letters, p, ops):
    mul_rot, mul_ref = ops
    reach = list(reach)
    n2 = 2 * p
    for kind, val in letters:
        for c in range(min(top, n2 - 1), -1, -1):
            if reach[c]:
                reach[c + 1] |= mul_rot(reach[c], val) if kind == 'r' else mul_ref(reach[c], val)
        top += 1
    return reach, top


def has_identity_subword(letters, p, ops):
    reach, _ = dp_extend([1] + [0] * (2 * p), 0, letters, p, ops)
    return bool(reach[2 * p] & 1)


def el_mul(x, y, p):                            # (f1, j1)(f2, j2) = s^f1 r^j1 s^f2 r^j2
    return ((x[0] + y[0]) % 2, ((-x[1] if y[0] else x[1]) + y[1]) % p)


def brute_identity(letters, p):
    els = [(0, v % p) if kind == 'r' else (1, v % p) for kind, v in letters]
    for comb in itertools.combinations(range(len(els)), 2 * p):
        e = (0, 0)
        for i in comb:
            e = el_mul(e, els[i], p)
        if e == (0, 0):
            return True
    return False


def word_letters(w, lens, ys):
    out = []
    for j, (a, b) in enumerate(w.runs):
        out += [('r', 1)] * a + [('r', -1)] * b + [('f', ys[j])] * lens[j]
    return out


def random_reflection(rng, w):
    H2 = 4 * w.p - 2 - w.P['R'] - w.k                                    # = 2H
    assert H2 >= 0 and H2 % 2 == 0
    xs = [0] * w.k
    for _ in range(H2 // 2):
        xs[rng.randrange(w.k)] += 1
    return [1 + 2 * x for x in xs], [rng.randrange(w.p) for _ in range(w.k)]


def p5_exhaustive(ops):
    p, k = 5, 7
    rot_letters = [[('r', -1)]] + [[('r', 1)]] * 6                       # anti single at run 0 (cyclic rotation WLOG)
    pats = set()
    for i in range(k):
        l = [1] * k
        l[i] = 5
        pats.add(tuple(l))
        for j in range(i + 1, k):
            l = [1] * k
            l[i] = l[j] = 3
            pats.add(tuple(l))
    tot = {'words': 0, 'with_identity_2p_subword': 0, 'patterns': len(pats), 'avoiders': []}
    for lens in sorted(pats):
        assert sum(lens) == 4 * p - 2 - 7
        stack = [(0, [1] + [0] * (2 * p), 0)]
        while stack:
            j, reach, top = stack.pop()
            if reach[2 * p] & 1:
                cnt = p ** (k - j)                                       # every completion keeps the subword
                tot['words'] += cnt
                tot['with_identity_2p_subword'] += cnt
                continue
            if j == k:
                tot['words'] += 1
                if len(tot['avoiders']) < 5:
                    tot['avoiders'].append(lens)
                continue
            r2, t2 = dp_extend(reach, top, rot_letters[j], p, ops)
            for y in ([0] if j == 0 else range(p)):                     # y_0 = 0 by conjugation WLOG
                r3, t3 = dp_extend(r2, t2, [('f', y)] * lens[j], p, ops)
                stack.append((j + 1, r3, t3))
    return tot


# ------------------------------------------------------------------------------------------------------------ main
def make_words(rng, p, per_class, delta0_exact=None, max_classes=None, e_min=None):
    cls = classes(p, delta0_exact)
    if e_min is not None:
        cls = [c for c in cls if 2 * p - c[0] + 2 * c[1] - c[0] >= e_min] or cls
    if max_classes is not None and len(cls) > max_classes:
        cls = sorted(rng.sample(cls, max_classes))
    styles = ['spread', 'conc', 'conc-adj', 'antiblock', 'longadj']
    words = []
    max_R = 2 * p - 3 if delta0_exact is None else 2 * p - delta0_exact
    for (k, kappa, B) in cls:
        for i in range(per_class):
            runs = random_word(rng, p, k, kappa, B, styles[i % len(styles)])
            if runs is None:
                continue
            w = Word(p, runs)
            assert nmh_ok(w.P, runs, max_R) and (w.P['k'], w.P['kappa'], w.P['B']) == (k, kappa, B), (p, runs)
            words.append(w)
    return words


def main():
    rng = random.Random(20261018)
    src = Path(__file__).read_bytes()
    emit({'event': 'start', 'script_sha256': hashlib.sha256(src).hexdigest(), 'python': sys.version.split()[0], 'seed': 20261018,
          'cpu_soft_limit_s': CPU_SOFT, 'budgets': BUDGET})
    # word sample (deterministic)
    W = {}
    W[5] = [Word(5, [(0, 1) if i == j else (1, 0) for i in range(7)]) for j in range(7)]
    W[7] = make_words(rng, 7, 16)
    W[11] = make_words(rng, 11, 3)
    W[13] = make_words(rng, 13, 2, max_classes=120)
    W[17] = make_words(rng, 17, 1, max_classes=110, e_min=4)
    W[19] = make_words(rng, 19, 1, max_classes=70, e_min=4)
    W[23] = make_words(rng, 23, 1, max_classes=45, e_min=4)
    emit({'event': 'sample', 'words': {p: len(ws) for p, ws in W.items()},
          'classes_total': {p: len(classes(p)) for p in W},
          'words_E>=4': {p: sum(w.P['E'] >= 4 for w in ws) for p, ws in W.items()}})

    # Part A: GEN versus the floor-term definition on EVERY proper pattern of actual words with k <= 14
    stA = {k: 0 for k in ('words', 'patterns', 'generic', 'gen_mismatch', 'complement_param_mismatch', 'complement_symmetry_fail',
                          'MUT_gen_bound_minus1_mismatch', 'MUT_gen_bound_plus1_mismatch', 'MUT_gen_kplus1_mismatch',
                          'exist_targets', 'exist_targets_without_generic_config')}
    stA['exist_min_count'] = None
    truncA = False
    for p in (5, 7, 11, 13):
        for w in W[p]:
            if w.k > 14:
                continue
            if cpu() > BUDGET['A']:
                truncA = True
                break
            gen = part_a_word(w, stA)
            stA['words'] += 1
            if w.k <= 11:
                exist_check(w, gen, stA)
    emit({'part': 'A', 'truncated': truncA, **stA})

    # Part B: the walk of Lemma GC, every target of every sampled word
    keys = ('targets', 'targets_E>=4', 'targets_pair', 'targets_anti', 'failures', 'actual_empty',
            'actual_empty_with_qs_window_nonempty', 'Q_without_t_plus_1', 'bstar_formula_mismatch', 'walk_len_not_L_minus_2',
            'pass2_moves', 'MUT_widen1_picks_not_generic', 'MUT_Xonly_picks_not_generic', 'MUT_sigma_without_end_terms_wrong')
    stB = {k: 0 for k in keys}
    stB.update({'istar_max': 0, 'walk_len_max': 0, 'src_bound_(2m-1)(L-2)_max': 0, 'by_p': {}})
    fails, truncB = [], False
    for p in (5, 7, 11, 13, 17, 19, 23):
        done = 0
        for w in W[p]:
            if cpu() > BUDGET['B']:
                truncB = True
                break
            for t in range(w.k):
                run_target_main(w, t, stB, fails)
            done += 1
        stB['by_p'][p] = done
    emit({'part': 'B', 'truncated': truncB, 'first_failures': fails, **stB})

    # Probe (hypothesis sensitivity): the same recipe on R = 2p-2 words (Delta0 = 2, outside the target's scope)
    stP = {'words': 0, 'targets': 0, 'fail_M': 0, 'fail_eq33': 0, 'no_crossing': 0, 'pick_not_generic': 0,
           'fail_GSb_or_NW': 0, 'any_recipe_failure': 0, 'exist_targets': 0, 'exist_targets_without_generic_config': 0}
    examples, truncP = [], False
    for p in (7, 11, 13):
        for w in make_words(rng, p, 6, delta0_exact=2):
            if cpu() > BUDGET['probe']:
                truncP = True
                break
            stP['words'] += 1
            gen = None
            if w.k <= 11:
                tmp = {k: 0 for k in ('patterns', 'generic', 'gen_mismatch', 'complement_param_mismatch', 'complement_symmetry_fail',
                                      'MUT_gen_bound_minus1_mismatch', 'MUT_gen_bound_plus1_mismatch', 'MUT_gen_kplus1_mismatch',
                                      'exist_targets', 'exist_targets_without_generic_config')}
                tmp['exist_min_count'] = None
                gen = part_a_word(w, tmp)
                exist_check(w, gen, tmp)
                stP['exist_targets'] += tmp['exist_targets']
                stP['exist_targets_without_generic_config'] += tmp['exist_targets_without_generic_config']
            for t in range(w.k):
                stP['targets'] += 1
                res = gc_target(w, t, {'bstar_formula_mismatch': 0, 'walk_len_not_L_minus_2': 0, 'pass2_moves': 0,
                                       'src_bound_(2m-1)(L-2)_max': 0, 'walk_len_max': 0}, probe=True)
                ch = res['checks']
                f = {'fail_M': not ch['M_three_runs_le_E_plus_3_le_Wp'], 'fail_eq33': not (ch['eq33_lo'] and ch['eq33_hi']),
                     'no_crossing': not ch['crossing_found'],
                     'pick_not_generic': ch['crossing_found'] and not (ch['Q_generic'] and ch['Qt_generic']),
                     'fail_GSb_or_NW': ch['crossing_found'] and not (ch['GSb_s_lo'] and ch['GSb_s_hi'] and ch['NW'])}
                for kk, vv in f.items():
                    stP[kk] += vv
                if any(f.values()):
                    stP['any_recipe_failure'] += 1
                    if len(examples) < 4:
                        examples.append({'p': p, 'runs': w.runs, 't': t, 'fails': [kk for kk, vv in f.items() if vv]})
    emit({'part': 'probe_Delta0_eq_2', 'truncated': truncP, 'examples': examples, **stP})

    # Part G: theorem conclusion directly in D_(2p) (no lemma used)
    out = {}
    ops5 = group_ops(5)
    mism = 0
    for _ in range(250):
        n = rng.randint(10, 13)
        letters = [('r', rng.choice((1, -1))) if rng.random() < 0.5 else ('f', rng.randrange(5)) for _ in range(n)]
        mism += has_identity_subword(letters, 5, ops5) != brute_identity(letters, 5)
    out['dp_vs_bruteforce_p5_random_words'] = 250
    out['dp_vs_bruteforce_mismatches'] = mism
    ctrl = {}
    for p in (5, 7, 11, 13):
        ops = group_ops(p)
        ctrl[p] = {'avoider_r^(2p-1)s^(2p-1)_has_subword': has_identity_subword([('r', 1)] * (2 * p - 1) + [('f', 0)] * (2 * p - 1), p, ops),
                   'positive_r^(2p)s^(2p-2)_has_subword': has_identity_subword([('r', 1)] * (2 * p) + [('f', 0)] * (2 * p - 2), p, ops)}
    out['controls'] = ctrl
    out['p5_exhaustive'] = p5_exhaustive(ops5)
    emit({'part': 'G1', **out})
    gst, truncG = {}, False
    for p in (7, 11, 13):
        ops = group_ops(p)
        n_ok = n = 0
        for w in W[p]:
            if cpu() > BUDGET['G']:
                truncG = True
                break
            lens, ys = random_reflection(rng, w)
            assert sum(lens) + w.P['R'] == 4 * p - 2 and all(l % 2 == 1 for l in lens)
            n += 1
            n_ok += has_identity_subword(word_letters(w, lens, ys), p, ops)
        gst[p] = {'words': n, 'with_identity_2p_subword': n_ok, 'words_E>=4': sum(1 for w in W[p][:n] if w.P['E'] >= 4)}
    emit({'part': 'G2', 'truncated': truncG, 'random_letterings': gst})
    ru = resource.getrusage(resource.RUSAGE_SELF)
    emit({'event': 'done', 'peak_rss_bytes_macos': ru.ru_maxrss, 'user_s': ru.ru_utime, 'sys_s': ru.ru_stime})


if __name__ == '__main__':
    main()
