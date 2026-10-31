import sys
import time

START = time.perf_counter()
DEADLINE = START + 50.0

class Failure(Exception):
    def __init__(self, code, detail):
        self.code = code
        super().__init__(code + ': ' + str(detail))

class BudgetExceeded(Exception):
    pass

def need(ok, code, detail=''):
    if not ok:
        raise Failure(code, detail)

def budget():
    if time.perf_counter() >= DEADLINE:
        raise BudgetExceeded('50-second cooperative deadline; no VALID result')

def parity(x):
    return x.bit_count() & 1

def chi(s, x):
    return 1 - 2 * parity(s & x)

def fwht(values):
    a = list(values)
    n = len(a)
    need(n > 0 and n & (n - 1) == 0, 'TRANSFORM_LENGTH', n)
    step = 1
    while step < n:
        for base in range(0, n, 2 * step):
            for j in range(step):
                p = base + j
                x, y = a[p], a[p + step]
                a[p], a[p + step] = x + y, x - y
        step *= 2
    return tuple(a)

def direct(values):
    return tuple(sum(v * chi(s, x) for x, v in enumerate(values))
                 for s in range(len(values)))

NEG4 = tuple(sum((parity(s & x) << x) for x in range(16))
             for s in range(16))
SUBSETS = tuple(sum(1 << m for m in range(16) if m & x == m)
                for x in range(16))

def boolean_walsh(t):
    return tuple(16 - 2 * (t ^ mask).bit_count() for mask in NEG4)

def anf(t):
    a = [(t >> x) & 1 for x in range(16)]
    for bit in (1, 2, 4, 8):
        for x in range(16):
            if x & bit:
                a[x] ^= a[x ^ bit]
    return sum(v << x for x, v in enumerate(a))

def evaluate_anf(a):
    return sum(parity(a & SUBSETS[x]) << x for x in range(16))

def degree(a):
    return max((m.bit_count() for m in range(16) if (a >> m) & 1),
               default=-1)

def polar_rank(a):
    rows = [0, 0, 0, 0]
    for i in range(4):
        for j in range(i + 1, 4):
            if (a >> ((1 << i) | (1 << j))) & 1:
                rows[i] |= 1 << j
                rows[j] |= 1 << i
    rank = 0
    for col in range(4):
        pivot = next((k for k in range(rank, 4) if rows[k] & (1 << col)), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for k in range(4):
            if k != rank and rows[k] & (1 << col):
                rows[k] ^= rows[rank]
        rank += 1
    return rank

D = (1, 2, 4, 7)
BINDEX = {d: b for b, d in enumerate(D)}
RHO = (-1, -1, -1, 1)
Q = sum((1 ^ (((x >> 2) & 1) & ((x >> 3) & 1))) << x
        for x in range(16))
F = 0x8888
R = 0x6CA0
A_SMALL = {0, 1, 2, 4}

def build_a(f, r):
    out = []
    for h in range(8):
        for d in range(8):
            b = BINDEX.get(d)
            x = None if b is None else (h >> 1) | (b << 2)
            out.append(1 - 2 * ((r >> x) & 1)
                       if x is not None and (h & 1) == ((f >> x) & 1) else 0)
    return tuple(out)

def build_g(f, rho=RHO):
    out = []
    for h in range(8):
        for d in range(8):
            if d == 0:
                out.append(4 if h in (0, 1) else -2)
            elif d in BINDEX:
                b = BINDEX[d]
                x = (h >> 1) | (b << 2)
                on = (h & 1) == ((f >> x) & 1)
                out.append(rho[b] * (-2 + 3 * int(on)))
            else:
                out.append(0)
    return tuple(out)

def check_geometry(f, g):
    expected = build_g(f)
    need(len(g) == 64, 'G_LENGTH')
    for c, (v, e) in enumerate(zip(g, expected)):
        need(v == e, 'RHO_ALIGNMENT', (c, v, e))

def check_g_spectrum(gh):
    mags = sorted(abs(v) for v in gh)
    need(mags == [4] * 4 + [12] * 60, 'G_MAGNITUDES')
    need({s for s, v in enumerate(gh) if abs(v) == 4} == A_SMALL,
         'G_SMALL_POSITIONS')
    need(all(gh[s] == 4 for s in A_SMALL), 'G_SMALL_SIGNS')

def check_g_identity(f, gh, offset=Q):
    bw = boolean_walsh(f ^ offset)
    for y in range(8):
        for z in range(8):
            if y == 0:
                expected = -4 + 4 * (chi(z, 1) + chi(z, 2)
                                      + chi(z, 4) - chi(z, 7))
            elif not (y & 1):
                expected = 12
            else:
                w = parity(z & 3) | (parity(z & 5) << 1)
                expected = 3 * chi(z, 1) * bw[(y >> 1) | (w << 2)]
            need(gh[8 * y + z] == expected, 'G_OFFSET_SIGN', (y, z))

def check_a(f, r):
    a = build_a(f, r)
    ah = direct(a)
    need(ah == fwht(a), 'A_TRANSFORM_DISAGREEMENT')
    need(all(abs(v) == 4 for v in ah), 'A_FLAT')
    even, odd = boolean_walsh(r), boolean_walsh(r ^ f)
    for y in range(8):
        for z in range(8):
            w = parity(z & 3) | (parity(z & 5) << 1)
            expected = chi(z, 1) * (odd if y & 1 else even)[(y >> 1) | (w << 2)]
            need(ah[8 * y + z] == expected, 'A_COMMON_PHASE', (y, z))
    return ah

def partial(u):
    need(len(u) == 256 and all(v in (-1, 0, 1) for v in u), 'U_DOMAIN')
    blocks = [tuple(u[4 * c:4 * c + 4]) for c in range(64)]
    rows = []
    for block in blocks:
        row = direct(block)
        need(row == fwht(block), 'LOCAL_TRANSFORM_DISAGREEMENT')
        rows.append(row)
    return tuple(tuple(row[s] for row in rows) for s in range(4))

def check_local(f, r, u):
    us = partial(u)
    a, g = build_a(f, r), build_g(f)
    need(us[1] == tuple(3 * v for v in a), 'U1_BLOCK')
    need(us[2] == g, 'U2_BLOCK')
    need(sum(us[1][c] == 0 and abs(us[0][c]) == 4
             for c in range(64)) == 0, 'LOCAL_H0')
    return us

def check_support(u):
    n = sum(v != 0 for v in u)
    need(n >= 116, 'SUPPORT_UNDER', n)
    need(n <= 116, 'SUPPORT_OVER', n)

def check_padding(f, u):
    g = build_g(f)
    sizes = [sum(v != 0 for v in u[4 * c:4 * c + 4])
             for c in range(64) if g[c] == 0]
    need(len(sizes) == 24 and all(n in (0, 2) for n in sizes), 'ZERO_PADDING_SHAPE')
    need(sizes.count(2) == 8, 'EIGHT_ZERO_TWO_BLOCKS', sizes.count(2))

def build_u(f, r, padding=8):
    a, g = build_a(f, r), build_g(f)
    out = []
    added = 0
    for aa, gg in zip(a, g):
        if aa:
            hole = next(w for w in range(4) if chi(3, w) == -gg * aa)
            block = tuple(aa * chi(1, w) if w != hole else 0 for w in range(4))
        elif abs(gg) == 4:
            block = tuple((gg // 4) * chi(2, w) for w in range(4))
        elif gg:
            block = (gg // 2, gg // 2, 0, 0)
        elif added < padding:
            block = (1, 0, 0, 1)
            added += 1
        else:
            block = (0, 0, 0, 0)
        out.extend(block)
    need(added == padding, 'PADDING_AVAILABILITY')
    return tuple(out)

# Rows h=0..7; columns d=0..7; within each block w=0..3.
GOLDEN_BLOCKS = (
    ((1,1,-1,-1),(0,-1,1,-1),(0,-1,1,-1),(1,0,0,1),(0,-1,1,-1),(1,0,0,1),(1,0,0,1),(1,0,1,-1)),
    ((1,1,-1,-1),(1,1,0,0),(1,1,0,0),(1,0,0,1),(1,1,0,0),(1,0,0,1),(1,0,0,1),(-1,-1,0,0)),
    ((-1,-1,0,0),(0,-1,1,-1),(-1,0,-1,1),(1,0,0,1),(0,-1,1,-1),(1,0,0,1),(0,0,0,0),(0,1,-1,1)),
    ((-1,-1,0,0),(1,1,0,0),(1,1,0,0),(0,0,0,0),(1,1,0,0),(0,0,0,0),(0,0,0,0),(-1,-1,0,0)),
    ((-1,-1,0,0),(0,-1,1,-1),(0,-1,1,-1),(0,0,0,0),(-1,0,-1,1),(0,0,0,0),(0,0,0,0),(0,1,-1,1)),
    ((-1,-1,0,0),(1,1,0,0),(1,1,0,0),(0,0,0,0),(1,1,0,0),(0,0,0,0),(0,0,0,0),(-1,-1,0,0)),
    ((-1,-1,0,0),(1,1,0,0),(1,1,0,0),(0,0,0,0),(1,1,0,0),(0,0,0,0),(0,0,0,0),(-1,-1,0,0)),
    ((-1,-1,0,0),(0,-1,1,-1),(-1,0,-1,1),(0,0,0,0),(-1,0,-1,1),(0,0,0,0),(0,0,0,0),(1,0,1,-1)),
)
GOLDEN_W0 = (
    (12,-12,-8,-24,-8,-24,-28,-4),
    (-8,-16,-12,12,-12,12,8,16),
    (12,4,0,0,0,0,4,12),
    (-16,-8,-12,12,-12,12,16,8),
    (20,-4,0,0,0,0,-4,20),
    (-8,-16,-12,12,-12,12,8,16),
    (12,4,0,0,0,0,4,12),
    (8,16,12,-12,12,-12,-8,-16),
)
GOLDEN_W3 = (
    (12,-4,-8,0,-8,0,-12,20),
    (0,-8,-4,4,-4,4,0,8),
    (4,-4,0,0,-8,-8,4,12),
    (-8,8,4,4,-4,-4,0,0),
    (12,-12,-8,-8,0,0,-4,20),
    (0,0,-4,-4,4,4,-8,8),
    (4,4,0,-8,0,-8,-4,12),
    (-8,0,4,-4,4,-4,8,0),
)

def flatten(rows):
    return tuple(v for row in rows for v in row)

CONTROLS = []

def reject(name, code, fn):
    try:
        fn()
    except Failure as e:
        need(e.code == code, 'WRONG_REJECTION', (name, e.code, code))
        CONTROLS.append((name, code))
    else:
        raise Failure('MUTANT_ACCEPTED', name)

def main():
    need(Q == 0x0FFF, 'Q_ENCODING')
    bent = []
    degree_counts = {}
    for t in range(65536):
        if t % 256 == 0:
            budget()
        wh = boolean_walsh(t)
        need(wh == fwht(tuple(1 - 2 * ((t >> x) & 1) for x in range(16))),
             'BOOLEAN_TRANSFORM_DISAGREEMENT', t)
        an = anf(t)
        need(evaluate_anf(an) == t, 'ANF_ROUNDTRIP', t)
        deg = degree(an)
        degree_counts[deg] = degree_counts.get(deg, 0) + 1
        is_bent = all(abs(v) == 4 for v in wh)
        need(is_bent == (deg <= 2 and polar_rank(an) == 4), 'ANF_BENT_CLASSIFICATION', t)
        if is_bent:
            bent.append(t)
    need(len(bent) == 896, 'BENT_CENSUS', len(bent))
    bset = set(bent)
    ranks = {2: 0, 4: 0}
    pair_count = 0
    for k, t in enumerate(bent):
        if k % 8 == 0:
            budget()
        f = t ^ Q
        g = build_g(f)
        check_geometry(f, g)
        gh = direct(g)
        need(gh == fwht(g), 'G_TRANSFORM_DISAGREEMENT', f)
        check_g_spectrum(gh)
        check_g_identity(f, gh)
        an = anf(f)
        rank = polar_rank(an)
        need(degree(an) == 2 and rank in ranks, 'GRAPH_QUADRATIC_RANK', f)
        ranks[rank] += 1
        phases = [r for r in bent if r ^ f in bset]
        need(len(phases) == 384, 'PHASE_CENSUS', (f, len(phases)))
        pair_count += len(phases)
        check_a(f, phases[0])
    need(ranks == {2: 512, 4: 384}, 'GRAPH_RANK_CENSUS', ranks)
    need(pair_count == 344064, 'PAIR_CENSUS', pair_count)
    groups = {}
    for t in range(81):
        x, block = t, []
        for unused in range(4):
            block.append(x % 3 - 1)
            x //= 3
        block = tuple(block)
        row = direct(block)
        need(row == fwht(block), 'TERNARY_TRANSFORM_DISAGREEMENT', t)
        groups.setdefault((row[1], row[2]), []).append((block, row))
    for aa in (-1, 1):
        for gg in (-1, 1):
            options = groups[(3 * aa, gg)]
            need(len(options) == 2 and all(sum(v != 0 for v in b) == 3 for b, row in options),
                 'SUPPORT_LOCAL_OPTIONS', (aa, gg))
    for gg in (-4, 4):
        options = groups[(0, gg)]
        need(len(options) == 1 and options[0][1][0] == 0, 'FULL_LOCAL_OPTIONS', gg)
    for gg in (-2, 2):
        options = groups[(0, gg)]
        need(len(options) == 4 and all(sum(v != 0 for v in b) == 2 for b, row in options),
             'TWO_LOCAL_OPTIONS', gg)
    zero_options = groups[(0, 0)]
    need(len(zero_options) == 9 and sum(abs(row[0]) != 4 for b, row in zero_options) == 7,
         'ZERO_LOCAL_OPTIONS')
    need(F ^ Q in bset and R in bset and R ^ F in bset, 'EXPLICIT_PAIR')
    u = build_u(F, R)
    literal = tuple(v for row in GOLDEN_BLOCKS for block in row for v in block)
    need(u == literal, 'EXPLICIT_256_TABLE')
    us = check_local(F, R, u)
    check_support(u)
    check_padding(F, u)
    hats = tuple(direct(v) for v in us)
    need(all(hats[s] == fwht(us[s]) for s in range(4)), 'GLOBAL_TRANSFORM_DISAGREEMENT')
    need(all(abs(v) == 12 for v in hats[1]), 'ACTUAL_U1_FLAT')
    check_g_spectrum(hats[2])
    need(hats[1] == tuple(3 * v for v in check_a(F, R)), 'ACTUAL_A_RELATION')
    need(hats[0] == flatten(GOLDEN_W0), 'EXPLICIT_U0_WALSH')
    need(hats[3] == flatten(GOLDEN_W3), 'EXPLICIT_U3_WALSH')
    need(sum(u) == hats[0][0] == 12, 'DESCRIPTIVE_BALANCE')
    need(tuple(sum(v * v for v in us[s]) for s in range(4)) == (136,144,136,48),
         'PARTIAL_ENERGIES')
    reject('wrong_rho', 'RHO_ALIGNMENT',
           lambda: check_geometry(F, build_g(F, (1,-1,-1,1))))
    reject('wrong_f_offset_constant', 'G_OFFSET_SIGN',
           lambda: check_g_identity(F, hats[2], Q ^ 0xFFFF))
    bad = list(u)
    bad[4:8] = (1,0,1,-1)
    reject('wrong_sign_hole', 'U2_BLOCK', lambda: check_local(F, R, tuple(bad)))
    bad = list(u)
    bad[0] = 0
    reject('support_115', 'SUPPORT_UNDER', lambda: check_support(tuple(bad)))
    bad = list(u)
    bad[88] = 1
    reject('support_117', 'SUPPORT_OVER', lambda: check_support(tuple(bad)))
    seven = build_u(F, R, 7)
    check_local(F, R, seven)
    need(sum(v != 0 for v in seven) == 114, 'SEVEN_ARITHMETIC')
    reject('seven_not_eight_zero_two_blocks', 'EIGHT_ZERO_TWO_BLOCKS',
           lambda: check_padding(F, seven))
    reject('seven_support_114', 'SUPPORT_UNDER', lambda: check_support(seven))
    shifted = tuple(u[4*c+w] * chi(7, c & 7) for c in range(64) for w in range(4))
    shifted_us = partial(shifted)
    shifted_gh = direct(shifted_us[2])
    need(sorted(abs(v) for v in shifted_gh) == sorted(abs(v) for v in hats[2]),
         'SHIFT_NOT_HISTOGRAM_PRESERVING')
    need(all(abs(v) == 12 for v in direct(shifted_us[1])), 'SHIFT_NOT_A_FLAT')
    reject('right_magnitudes_wrong_small_positions', 'G_SMALL_POSITIONS',
           lambda: check_g_spectrum(shifted_gh))
    reject('negative_small_signs', 'G_SMALL_SIGNS',
           lambda: check_g_spectrum(tuple(-v for v in hats[2])))
    bad = list(u)
    bad[88:92] = (1,1,1,1)
    reject('constant_zero_block_H_peak', 'LOCAL_H0', lambda: check_local(F, R, tuple(bad)))
    budget()
    print('RESULT: VALID')
    print('SCOPE: labeled canonical two-fibre graphs and local physical lifts only')
    print('Boolean functions=65536; bent=896; graph ranks=' + repr(ranks))
    print('Common phases=384 per graph; labeled pairs=' + str(pair_count))
    print('ANF degree census=' + repr(degree_counts))
    print('Local ternary blocks=81; option counts=(2,1,4,9); H0-safe zero options=7')
    print('u256=' + repr(u))
    print('U0_Walsh=' + repr(hats[0]))
    print('U3_Walsh=' + repr(hats[3]))
    print('support=116; local_H=0; balance=12; NOT a balanced caller')
    print('CONTROLS=' + repr(CONTROLS))
    print('elapsed_seconds=' + repr(time.perf_counter() - START))

if __name__ == '__main__':
    try:
        main()
    except BudgetExceeded as e:
        print('RESULT: INCOMPLETE_BUDGET; ' + str(e))
        sys.exit(2)
    except Failure as e:
        print('RESULT: INVALID; ' + str(e))
        sys.exit(1)
