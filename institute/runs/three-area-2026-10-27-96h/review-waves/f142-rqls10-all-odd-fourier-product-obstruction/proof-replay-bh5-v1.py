#!/usr/bin/env python3
"""proof-replay-bh5-v1.py (review f142): independent same-harness replay of the
BH(10,5) half-frame no-matching certificate. Standard library only. Reads only
the frozen certificate JSON (and the frozen f72 receipt purely as DATA for an
index-binding cross-check); imports/executes no author or prior-reviewer code.
Everything below is derived from the written theorem text and the reviewer's
own mathematics."""
import hashlib, itertools, json, os, platform, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
CERT = '/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/rqls10/frontier-20261028-bh10-structural-cert-v1.json'
CERT_SHA = '67bc6f39a6d2bbd6a3c181dc4a7e5baaa7e5406b4ad8a50eb997b44e41197eb2'
F72_RECEIPT = '/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f72-all-bh10-5-product-obstruction/receipt-v1.json'
F72_SHA = 'e131fa267ed4edf0992064dc8d493923a1e8a1d217f82a29a37d38175123a011'
OUT = os.path.join(HERE, 'proof-replay-bh5-receipt-v1.json')
T0 = time.time()

def native_clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True, check=True).stdout.strip()

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def fail(msg):
    print('FAIL', msg); sys.exit(1)

START_CLOCK = native_clock()
R = {'kind': 'F142_INDEPENDENT_BH5_REPLAY', 'observed_start_native_clock': START_CLOCK,
     'python': sys.version, 'platform': platform.platform(), 'checks': {}, 'controls': {}}

# ---------- exact integer cyclotomic arithmetic ----------
def poly_divmod(num, den):
    num = list(num); q = [0] * max(len(num) - len(den) + 1, 1)
    for i in range(len(num) - len(den), -1, -1):
        c = num[i + len(den) - 1]
        if c:
            q[i] = c
            for j, d in enumerate(den):
                num[i + j] -= c * d
    return q, num[:len(den) - 1]

def poly_mul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    return r

_PHI = {}
def cyclotomic(n):
    if n in _PHI:
        return _PHI[n]
    num = [-1] + [0] * (n - 1) + [1]
    den = [1]
    for d in range(1, n):
        if n % d == 0:
            den = poly_mul(den, cyclotomic(d))
    q, r = poly_divmod(num, den)
    if any(r):
        fail('cyclotomic division remainder')
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    _PHI[n] = q
    return q

def root_sum_is_zero(n, exps):
    counts = [0] * n
    for e in exps:
        counts[e % n] += 1
    _, r = poly_divmod(counts, cyclotomic(n))
    return not any(r)

if cyclotomic(5) != [1, 1, 1, 1, 1] or cyclotomic(10) != [1, -1, 1, -1, 1]:
    fail('cyclotomic sanity')

# ---------- A. exact fifth-root zero-sum criterion ----------
def balanced(seq, mult):
    cnt = [0] * 5
    for v in seq:
        cnt[v % 5] += 1
    return all(c == mult for c in cnt)

n5 = n10 = 0
for ms in itertools.combinations_with_replacement(range(5), 5):
    if root_sum_is_zero(5, ms) != balanced(ms, 1):
        fail('5-term fifth-root criterion')
    n5 += 1
for ms in itertools.combinations_with_replacement(range(5), 10):
    if root_sum_is_zero(5, ms) != balanced(ms, 2):
        fail('10-term fifth-root criterion')
    n10 += 1
R['checks']['fifth_root_criterion'] = {'multisets_5': n5, 'multisets_10': n10, 'result': 'PASS'}
print('A fifth-root criterion exact over', n5, 'and', n10, 'multisets')

# ---------- B. normalized rows, candidates, compatibility graph ----------
SECOND = (0, 0, 1, 1, 2, 2, 3, 3, 4, 4)
tails = set(itertools.permutations((0, 1, 1, 2, 2, 3, 3, 4, 4)))
rows_all = sorted((0,) + t for t in tails)
def orth(r1, r2):
    return balanced([(a - b) % 5 for a, b in zip(r1, r2)], 2)
cands = [r for r in rows_all if orth(r, SECOND)]
N = len(cands)
print('B balanced rows', len(rows_all), 'candidates', N)
if len(rows_all) != 22680 or N != 1075:
    fail('row counts')
if any(not orth(r, (0,) * 10) for r in cands) or SECOND in cands or (0,) * 10 in cands:
    fail('candidate sanity')
adj = [0] * N
edges = 0
for i in range(N):
    ri = cands[i]
    for j in range(i + 1, N):
        if orth(ri, cands[j]):
            adj[i] |= 1 << j; adj[j] |= 1 << i; edges += 1
print('B compatibility edges', edges)
if edges != 26715:
    fail('edge count')

def bits(x):
    while x:
        b = x & -x
        yield b.bit_length() - 1
        x ^= b

eligible = {}
tri = 0
for i in range(N):
    ai = adj[i]
    for j in bits(ai >> (i + 1) << (i + 1)):
        cij = ai & adj[j]
        for k in bits(cij >> (j + 1) << (j + 1)):
            tri += 1
            cn = (cij & adj[k]).bit_count()
            if cn >= 5:
                eligible[(i, j, k)] = cn
print('B triangles', tri, 'eligible', len(eligible))
if tri != 53065 or len(eligible) != 16064:
    fail('triangle counts')
R['checks']['finite_objects'] = {'balanced_rows': len(rows_all), 'candidates': N, 'edges': edges,
                                 'triangles': tri, 'eligible_triples': len(eligible)}

# ---------- C. half-column graph and perfect matching ----------
def gamma(E_rows):
    g = [0] * 10
    for c in range(10):
        for d in range(c + 1, 10):
            if len({(r[d] - r[c]) % 5 for r in E_rows}) == 5:
                g[c] |= 1 << d; g[d] |= 1 << c
    return g

def has_perfect_matching(g, n=10):
    def rec(rem):
        if not rem:
            return True
        v = (rem & -rem).bit_length() - 1
        rem ^= 1 << v
        cand = g[v] & rem
        while cand:
            b = cand & -cand; cand ^= b
            if rec(rem ^ b):
                return True
        return False
    return rec((1 << n) - 1)

# matching-routine controls
if not has_perfect_matching([0b10, 0b01, 0b1000, 0b0100] + [0] * 6, 4):
    fail('matching control positive')
if has_perfect_matching([0b110, 0b001, 0b001, 0] , 4):
    fail('matching control negative (odd component)')
cycle10 = [((1 << ((v + 1) % 10)) | (1 << ((v - 1) % 10))) for v in range(10)]
if not has_perfect_matching(cycle10):
    fail('matching control 10-cycle')
star = [0b1111111110] + [1] * 9
if has_perfect_matching(star):
    fail('matching control star')

# ---------- D. certificate parse (complete, strict) ----------
with open(CERT, 'rb') as f:
    raw = f.read()
if sha256_bytes(raw) != CERT_SHA or len(raw) != 612365 or raw.count(b'\n') != 1:
    fail('certificate hash/bytes/LF')
def no_dup(pairs):
    d = {}
    for k, v in pairs:
        if k in d:
            raise ValueError('duplicate key ' + k)
        d[k] = v
    return d
cert = json.loads(raw.decode('utf-8'), object_pairs_hook=no_dup)
if set(cert) != {'candidate_count', 'certificates', 'row_order', 'scope', 'triples_examined'}:
    fail('certificate top-level keys')
if cert['candidate_count'] != 1075 or cert['triples_examined'] != 53065:
    fail('certificate header counts')
recs = cert['certificates']
if not isinstance(recs, list) or len(recs) != 16064:
    fail('record count')
seen = set(); n_iso = n_odd = 0; iso_hist = {}; odd_sizes = {}
dp_rejections = 0
for rec in recs:
    if not isinstance(rec, dict):
        fail('record type')
    keys = set(rec)
    if keys not in ({'triple', 'isolated'}, {'triple', 'odd_component'}):
        fail('record keys ' + str(keys))
    t = rec['triple']
    if (not isinstance(t, list) or len(t) != 3 or any(type(v) is not int for v in t)
            or not (0 <= t[0] < t[1] < t[2] < N)):
        fail('triple format ' + str(t))
    t = tuple(t)
    if t in seen:
        fail('duplicate triple ' + str(t))
    seen.add(t)
    if t not in eligible:
        fail('unexpected triple ' + str(t))
    E_rows = [(0,) * 10, SECOND, cands[t[0]], cands[t[1]], cands[t[2]]]
    g = gamma(E_rows)
    iso_count = sum(1 for v in range(10) if g[v] == 0)
    iso_hist[iso_count] = iso_hist.get(iso_count, 0) + 1
    if 'isolated' in rec:
        v = rec['isolated']
        if type(v) is not int or not (0 <= v < 10):
            fail('isolate format ' + str(v))
        if g[v] != 0:
            fail('reported isolate not isolated ' + str(t))
        n_iso += 1
    else:
        S = rec['odd_component']
        if (not isinstance(S, list) or any(type(v) is not int or not (0 <= v < 10) for v in S)
                or len(set(S)) != len(S) or len(S) % 2 == 0 or not (0 < len(S) < 10)):
            fail('odd cut format ' + str(S))
        mask = 0
        for v in S:
            mask |= 1 << v
        if any(g[v] & ~mask & 0x3FF for v in S):
            fail('odd cut has crossing edge ' + str(t))
        odd_sizes[len(S)] = odd_sizes.get(len(S), 0) + 1
        n_odd += 1
    if has_perfect_matching(g):
        fail('independent DP found a perfect matching ' + str(t))
    dp_rejections += 1
if seen != set(eligible):
    fail('certificate triple set differs from eligible set')
print('D certificate records', len(recs), 'isolated', n_iso, 'odd cuts', n_odd, 'hist', iso_hist, 'odd sizes', odd_sizes)
R['checks']['certificate'] = {'records': len(recs), 'exactly_once_equal_to_eligible': True,
                              'isolated_witnesses_verified': n_iso, 'odd_cut_witnesses_verified': n_odd,
                              'odd_cut_sizes': odd_sizes, 'isolate_count_histogram': iso_hist,
                              'independent_matching_dp_rejections': dp_rejections}

# ---------- E. index binding vs f72 receipt sample (data only) ----------
with open(F72_RECEIPT, 'rb') as f:
    f72raw = f.read()
if sha256_bytes(f72raw) != F72_SHA:
    fail('f72 receipt hash')
f72 = json.loads(f72raw.decode('utf-8'))
sample = f72['sample_bh_control']
srows = [tuple(int(ch) for ch in s) for s in sample['exponent_rows']]
sidx = sample['clique_indices']
if srows[0] != (0,) * 10 or srows[1] != SECOND:
    fail('f72 sample first rows')
if [cands[i] for i in sidx] != srows[2:]:
    fail('index binding differs from f72 sample')
R['checks']['index_binding_vs_f72_sample'] = {'clique_indices': sidx, 'result': 'PASS'}

def is_bh5(rows):
    if len(rows) != 10:
        return False
    for a, b in itertools.combinations(rows, 2):
        if not orth(a, b):
            return False
    cols = [tuple(r[c] for r in rows) for c in range(10)]
    for a, b in itertools.combinations(cols, 2):
        if not orth(a, b):
            return False
    return True
if not is_bh5(srows):
    fail('f72 sample not BH(10,5)')

# ---------- F. own 8-clique search for full BH(10,5) matrices ----------
found = []
def clique_search(cur, candmask, limit):
    if len(found) >= limit:
        return
    if len(cur) == 8:
        found.append(tuple(cur)); return
    while candmask:
        b = candmask & -candmask; v = b.bit_length() - 1; candmask ^= b
        if 8 - len(cur) - 1 > (candmask & adj[v]).bit_count():
            continue
        clique_search(cur + [v], candmask & adj[v], limit)
        if len(found) >= limit:
            return
clique_search([], (1 << N) - 1, 12)
bh_list = []
for cl in found:
    rows = [(0,) * 10, SECOND] + [cands[i] for i in cl]
    if not is_bh5(rows):
        fail('clique rows not BH(10,5)')
    bh_list.append(rows)
print('F own 8-cliques found', len(found), 'first', found[0] if found else None)
R['checks']['own_bh5_cliques'] = {'found': len(found), 'first_clique': list(found[0]) if found else None,
                                  'all_verified_hadamard_exact': True}

# ---------- G. all 252 halves of each found BH: certified no-matching; component parity ----------
def normalize(rows, E, p, q, c0):
    base = rows[p]
    out = []
    for t in E:
        r = tuple((rows[t][c] - rows[t][c0] - base[c] + base[c0]) % 5 for c in range(10))
        out.append(r)
    return out
norm_checks = 0; comp_odd = 0; comp_total = 0; halves_no_matching = 0
for rows in bh_list + [srows]:
    for E in itertools.combinations(range(10), 5):
        E_rows = [rows[t] for t in E]
        if has_perfect_matching(gamma(E_rows)):
            fail('found half with perfect matching in a genuine BH(10,5)')
        halves_no_matching += 1
        # component parity of the E-half column orthogonality structure
        cg = [0] * 10
        for c in range(10):
            for d in range(c + 1, 10):
                if len({(r[d] - r[c]) % 5 for r in E_rows}) != 5:
                    cg[c] |= 1 << d; cg[d] |= 1 << c
        unseen = (1 << 10) - 1
        while unseen:
            start = unseen & -unseen; comp = start; frontier = start
            while frontier:
                nxt = 0
                for v in bits(frontier):
                    nxt |= cg[v]
                nxt &= ~comp
                comp |= nxt; frontier = nxt
            unseen &= ~comp
            comp_total += 1
            if comp.bit_count() % 2:
                comp_odd += 1
        # normalization binding: every ordered (p,q) in E with pivot column 0
        for p in E:
            for q in E:
                if p == q:
                    continue
                nr = normalize(rows, E, p, q, 0)
                # second row must become (0,0,1,1,2,2,3,3,4,4) after a column permutation
                sec = nr[E.index(q)]
                if sec[0] != 0 or sorted(sec) != sorted(SECOND):
                    fail('normalized second row shape')
                order = [0] + sorted(range(1, 10), key=lambda c: (sec[c], c))
                perm_rows = [tuple(r[c] for c in order) for r in nr]
                if perm_rows[E.index(q)] != SECOND or perm_rows[E.index(p)] != (0,) * 10:
                    fail('normalization failed')
                others = sorted(perm_rows[i] for i in range(5) if E[i] not in (p, q))
                idx = tuple(cands.index(r) for r in others)
                if idx not in eligible:
                    fail('normalized triple not eligible ' + str(idx))
                # relabeled graph must equal the graph of the normalized rows
                g1 = gamma(E_rows); g2 = gamma(perm_rows)
                for c in range(10):
                    for d in range(10):
                        if ((g1[order[c]] >> order[d]) & 1) != ((g2[c] >> d) & 1):
                            fail('graph relabeling mismatch')
                norm_checks += 1
print('G halves without matching', halves_no_matching, 'normalizations', norm_checks,
      'components', comp_total, 'odd components', comp_odd)
if comp_odd:
    fail('odd component in a tight E-half')
R['checks']['sample_bh_halves'] = {'matrices': len(bh_list) + 1, 'halves_no_matching': halves_no_matching,
                                   'ordered_pair_pivot0_normalizations_eligible_and_graph_equal': norm_checks,
                                   'E_half_orthogonality_components': comp_total, 'odd_components': comp_odd}

# ---------- H. tight-frame parity toy controls (exact, Fourier-5 columns) ----------
def f5col(i):
    return tuple((i * t) % 5 for t in range(5))
def half_ip_zero(colA, colB):  # sum_t conj(a_t) b_t over 5 rows, fifth roots
    return len({(b - a) % 5 for a, b in zip(colA, colB)}) == 5
def components_of(cols):
    n = len(cols); cg = [0] * n
    for c in range(n):
        for d in range(c + 1, n):
            if not half_ip_zero(cols[c], cols[d]):
                cg[c] |= 1 << d; cg[d] |= 1 << c
    sizes = []; unseen = (1 << n) - 1
    while unseen:
        start = unseen & -unseen; comp = start; frontier = start
        while frontier:
            nxt = 0
            for v in bits(frontier):
                nxt |= cg[v]
            nxt &= ~comp; comp |= nxt; frontier = nxt
        unseen &= ~comp; sizes.append(comp.bit_count())
    return sorted(sizes)
def gram_is_10I(cols):  # rows of the 5x10 matrix orthogonal with squared norm 10, exact
    for s in range(5):
        for t in range(5):
            exps = [(col[t] - col[s]) % 5 for col in cols]
            z = root_sum_is_zero(5, exps)
            if (s != t) != z:
                return False
    return True
tight = [f5col(i) for i in range(5) for _ in range(2)]
loose = [f5col(0)] * 3 + [f5col(1)] * 2 + [f5col(2)] * 2 + [f5col(3)] * 2 + [f5col(4)]
R['controls']['tight_frame_parity'] = {
    'tight_doubled_F5': {'gram_10I': gram_is_10I(tight), 'component_sizes': components_of(tight)},
    'non_tight_3_2_2_2_1': {'gram_10I': gram_is_10I(loose), 'component_sizes': components_of(loose)}}
if not gram_is_10I(tight) or components_of(tight) != [2] * 5:
    fail('tight toy control')
if gram_is_10I(loose) or all(s % 2 == 0 for s in components_of(loose)):
    fail('loose toy control')
print('H tight-frame toy controls', R['controls']['tight_frame_parity'])

# ---------- I. exact physical transversal brute force on sample arrays (q=5) ----------
def cell_orth_graph_q5(rows):
    # numerator of <psi_(r,c), psi_(s,d)> = sum_t zeta10^((s-r)t) zeta5^(a[t][d]-a[t][c])
    cells = [(r, c) for r in range(10) for c in range(10)]
    g = {x: set() for x in cells}
    for (r, c), (s, d) in itertools.combinations(cells, 2):
        exps = [((s - r) * t + 2 * (rows[t][d] - rows[t][c])) % 10 for t in range(10)]
        if root_sum_is_zero(10, exps):
            g[(r, c)].add((s, d)); g[(s, d)].add((r, c))
    return g
def find_transversal(g):
    chosen = []
    def rec(r, used):
        if r == 10:
            return list(chosen)
        for c in range(10):
            if used & (1 << c):
                continue
            x = (r, c)
            if all(x in g[y] for y in chosen):
                chosen.append(x)
                res = rec(r + 1, used | (1 << c))
                if res:
                    return res
                chosen.pop()
        return None
    return rec(0, 0)
basis_checks = 0
for rows in bh_list[:3] + [srows]:
    g = cell_orth_graph_q5(rows)
    # ONB sanity: each physical column (fixed c) and each physical row (fixed r) are 10 mutually orthogonal cells
    for c in range(10):
        for r, s in itertools.combinations(range(10), 2):
            if (s, c) not in g[(r, c)]:
                fail('Fourier column basis not orthogonal')
            basis_checks += 1
    for r in range(10):
        for c, d in itertools.combinations(range(10), 2):
            if (r, d) not in g[(r, c)]:
                fail('K row basis not orthogonal')
            basis_checks += 1
    # opposite-row identity: <psi_(r,c),psi_(r+5,d)> = 0 iff S_E(c,d)=0 and S_O(c,d)=0 (both fifth-root 5-sums)
    for r in range(5):
        for c in range(10):
            for d in range(10):
                if c == d:
                    continue
                SE = len({(rows[t][d] - rows[t][c]) % 5 for t in (0, 2, 4, 6, 8)}) == 5
                SO = len({(rows[t][d] - rows[t][c]) % 5 for t in (1, 3, 5, 7, 9)}) == 5
                if ((r + 5, d) in g[(r, c)]) != (SE and SO):
                    fail('opposite-row identity')
                if SE != SO:
                    fail('S_E=0 and S_O=0 should be equivalent under column orthogonality')
    if find_transversal(g) is not None:
        fail('transversal found in a BH(10,5) product array')
print('I exact q=5 transversal brute force: none in', len(bh_list[:3]) + 1, 'sample arrays; basis checks', basis_checks)
# planted positive control for the search routine: Fourier-10 vectors, diagonal cells distinct indices
planted = {}
for r in range(10):
    for c in range(10):
        planted[(r, c)] = r if r == c else (r + c) % 10
gp = {x: set() for x in planted}
for x, y in itertools.combinations(list(planted), 2):
    if planted[x] != planted[y]:
        gp[x].add(y); gp[y].add(x)
tv = find_transversal(gp)
if tv is None:
    fail('planted transversal not found')
print('I planted control transversal', tv)
R['controls']['planted_transversal_found'] = tv
R['checks']['physical_q5_sample_arrays'] = {'arrays': len(bh_list[:3]) + 1, 'basis_orthogonality_checks': basis_checks,
                                            'opposite_row_identity_checks': (len(bh_list[:3]) + 1) * 5 * 90,
                                            'transversals_found': 0}

# ---------- receipt ----------
with open(os.path.abspath(__file__), 'rb') as f:
    R['script_sha256'] = sha256_bytes(f.read())
R['inputs'] = [{'path': CERT, 'sha256': CERT_SHA, 'bytes': 612365, 'LF': 1},
               {'path': F72_RECEIPT, 'sha256': F72_SHA, 'role': 'data-only index-binding cross-check'}]
R['elapsed_seconds'] = round(time.time() - T0, 1)
R['result'] = 'PASS'
R['observed_clock_before_receipt_creation'] = native_clock()
if os.path.exists(OUT):
    fail('receipt exists; refusing to overwrite')
with open(OUT, 'x') as f:
    json.dump(R, f, indent=1, sort_keys=True); f.write('\n')
print('PASS receipt', OUT)
