#!/usr/bin/env python3
"""proof-oddq-controls-v3.py (review f142; v1 stopped at a wrong reviewer expectation for q=10, v2 at a reviewer arithmetic slip 5g vs 10g mod 3 in the dephasing control; no receipts were written): exact finite controls for the odd-q
Fourier-product reduction. numpy + standard library; no author code read,
imported or executed. Controls:
  B  complete 5-term zero-sum enumeration of q-th roots (q odd up to 105, even q=10,30)
  C  complete 10-term zero-sum enumeration (exact meet-in-the-middle) q=15,21,35,45
  D  q=105 constructive 5+5 / 3+7 LOW/HIGH G-profiles
  E  even-q countercontrols showing where the odd-q hypothesis is load-bearing
  F  matched-pair / row-quotient parity lemma instances at q=15
  G  dephasing procedure on a gauged matrix
  H  physical opposite-row identity, gauge covariance, exact transversal search in Z[zeta_30]
"""
import hashlib, itertools, json, os, platform, random, subprocess, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'proof-oddq-controls-receipt-v3.json')
T0 = time.time()
def native_clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True, check=True).stdout.strip()
def fail(msg):
    print('FAIL', msg); sys.exit(1)
R = {'kind': 'F142_ODDQ_EXACT_CONTROLS', 'observed_start_native_clock': native_clock(),
     'python': sys.version, 'numpy': np.__version__, 'platform': platform.platform(), 'controls': {}}

# ---------- exact cyclotomic arithmetic ----------
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
    num = [-1] + [0] * (n - 1) + [1]; den = [1]
    for d in range(1, n):
        if n % d == 0:
            den = poly_mul(den, cyclotomic(d))
    q, r = poly_divmod(num, den)
    if any(r):
        fail('cyclotomic remainder')
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    _PHI[n] = q
    return q
_TAB = {}
def table(n):
    """T[k] = integer coordinate vector of zeta_n^k in the power basis of Z[x]/Phi_n."""
    if n in _TAB:
        return _TAB[n]
    phi = cyclotomic(n); deg = len(phi) - 1
    T = np.zeros((n, deg), dtype=np.int64)
    for k in range(n):
        p = [0] * n; p[k] = 1
        _, r = poly_divmod(p, phi)
        T[k, :len(r)] = r
    _TAB[n] = T
    return T
def exact_sum(n, exps):
    return table(n)[[e % n for e in exps]].sum(axis=0)
def is_zero(n, exps):
    return not exact_sum(n, exps).any()
if cyclotomic(30) != [1, 1, 0, -1, -1, -1, 0, 1, 1]:
    fail('Phi_30')
if cyclotomic(15) != [1, -1, 0, 1, -1, 1, 0, -1, 1]:
    fail('Phi_15')
# sanity: regular p-gons vanish, a single root does not, p-gon minus one root does not
for n, p in ((15, 3), (15, 5), (105, 7), (30, 2)):
    if not is_zero(n, [k * (n // p) for k in range(p)]) or is_zero(n, [k * (n // p) for k in range(1, p)]):
        fail('cyclotomic sanity')

def pentagon_set(q, a):
    return sorted((a + k * (q // 5)) % q for k in range(5))
def coset(q, p, a):
    return sorted((a + k * (q // p)) % q for k in range(p))

# ---------- B. complete 5-term enumeration (multisets containing exponent 0, WLOG by rotation) ----------
def five_term(q):
    z = np.exp(2j * np.pi * np.arange(q) / q)
    it = itertools.combinations_with_replacement(range(q), 4)
    total = 0; hits = []; min_nonzero = np.inf
    while True:
        chunk = list(itertools.islice(it, 1_000_000))
        if not chunk:
            break
        arr = np.array(chunk, dtype=np.int16)
        s = 1 + z[arr].sum(axis=1)
        mag = np.abs(s)
        idx = np.nonzero(mag < 1e-7)[0]
        for i in idx:
            exps = [0] + list(map(int, arr[i]))
            if not is_zero(q, exps):
                fail('numeric hit not exact zero')
            hits.append(sorted(exps))
        rest = mag[mag >= 1e-7]
        if rest.size:
            min_nonzero = min(min_nonzero, float(rest.min()))
        total += len(chunk)
    pent = pentagon_set(q, 0) if q % 5 == 0 else None
    ok = (hits == [pent]) if pent else (hits == [])
    return {'multisets_containing_0': total, 'zero_sums': len(hits), 'all_regular_pentagon': bool(ok),
            'min_nonzero_abs': min_nonzero, 'hits': hits if len(hits) <= 4 else len(hits)}
B = {}
for q in (3, 5, 7, 9, 15, 21, 25, 35, 45, 63, 75, 105):
    B[q] = five_term(q)
    if not B[q]['all_regular_pentagon']:
        fail('five-term structure at q=%d' % q)
    print('B q=%d multisets %d zero-sums %d min|nonzero| %.4g' % (q, B[q]['multisets_containing_0'], B[q]['zero_sums'], B[q]['min_nonzero_abs']))
for q in (10, 30):
    B[q] = five_term(q)
    print('B even q=%d zero-sums %d all-pentagon %s' % (q, B[q]['zero_sums'], B[q]['all_regular_pentagon']))
# q=10: 5 = 5 is the only odd-prime/2 partition (2+3 needs 3|q), so q=10 has ONLY pentagon 5-sums (expected True);
# q=30 (2*3*5) admits 2+3 five-term zero sums, so it is the genuine five-term countercontrol (expected False).
if not B[10]['all_regular_pentagon'] or B[30]['all_regular_pentagon']:
    fail('even-q five-term countercontrol expectations (q=10 pentagon-only, q=30 non-pentagon)')
R['controls']['B_five_term_complete'] = B

# ---------- C. complete 10-term enumeration by exact meet-in-the-middle ----------
def classify(q, ms):
    ms = sorted(ms); kinds = []
    if q % 5 == 0:
        for a in range(q // 5):
            for b in range(a, q // 5):
                if sorted(pentagon_set(q, a) + pentagon_set(q, b)) == ms:
                    kinds.append(('5+5', a, b))
    if q % 21 == 0:
        for a in range(q // 3):
            for b in range(q // 7):
                if sorted(coset(q, 3, a) + coset(q, 7, b)) == ms:
                    kinds.append(('3+7', a, b))
    return kinds
def g_profile(q, ms):
    m = q // 5; cnt = {}
    for e in ms:
        cnt[e % m] = cnt.get(e % m, 0) + 1
    return sorted(cnt.values(), reverse=True)
def ten_term(q):
    T = table(q)
    combos = np.array(list(itertools.combinations_with_replacement(range(q), 5)), dtype=np.int16)
    M = len(combos)
    S = np.zeros((M, T.shape[1]), dtype=np.int32)
    for k in range(5):
        S += T[combos[:, k]].astype(np.int32)
    S = np.ascontiguousarray(S); negS = np.ascontiguousarray(-S)
    buckets = {}
    for i in range(M):
        buckets.setdefault(S[i].tobytes(), []).append(i)
    zs = []
    for i in range(M):
        b = buckets.get(negS[i].tobytes())
        if not b:
            continue
        A = combos[i]; amax = int(A[-1])
        for j in b:
            Bc = combos[j]
            if int(Bc[0]) >= amax:
                zs.append(tuple(map(int, A)) + tuple(map(int, Bc)))
    if len(set(zs)) != len(zs):
        fail('duplicate 10-multiset')
    kinds = {}; profiles = {}; unclassified = 0
    for ms in zs:
        if not is_zero(q, ms):
            fail('MITM zero sum not exact')
        ks = classify(q, ms)
        if not ks:
            unclassified += 1; continue
        key = '+'.join(sorted({k[0] for k in ks}))
        kinds[key] = kinds.get(key, 0) + 1
        if q % 5 == 0:
            prof = tuple(g_profile(q, ms))
            label = 'LOW' if prof in ((10,), (5, 5)) else ('HIGH' if len(prof) >= 9 else 'OTHER')
            pk = key + ':' + label + ':' + str(prof)
            profiles[pk] = profiles.get(pk, 0) + 1
    return {'five_multisets': M, 'zero_ten_multisets': len(zs), 'kinds': kinds, 'unclassified': unclassified,
            'G_profiles': profiles}
C = {}
expected = {15: 6, 21: 21, 35: 28, 45: 45}
for q in (15, 21, 35, 45):
    t1 = time.time(); C[q] = ten_term(q); C[q]['seconds'] = round(time.time() - t1, 1)
    print('C q=%d' % q, C[q])
    if C[q]['unclassified'] or C[q]['zero_ten_multisets'] != expected[q]:
        fail('ten-term classification at q=%d' % q)
    if q % 5 == 0 and any(':OTHER:' in k or ':HIGH:' in k for k in C[q]['G_profiles']):
        fail('unexpected profile at q=%d' % q)
R['controls']['C_ten_term_complete'] = C

# ---------- D. q=105 constructive 5+5 and 3+7 profiles ----------
q = 105; D = {'5+5': {}, '3+7': {}}
for a in range(21):
    for b in range(a, 21):
        ms = pentagon_set(q, a) + pentagon_set(q, b)
        if not is_zero(q, ms):
            fail('5+5 not zero')
        prof = tuple(g_profile(q, ms)); D['5+5'][str(prof)] = D['5+5'].get(str(prof), 0) + 1
        if prof not in ((10,), (5, 5)):
            fail('5+5 profile')
for a in range(35):
    for b in range(15):
        ms = coset(q, 3, a) + coset(q, 7, b)
        if not is_zero(q, ms):
            fail('3+7 not zero')
        prof = tuple(g_profile(q, ms)); D['3+7'][str(prof)] = D['3+7'].get(str(prof), 0) + 1
        if len(prof) < 9:
            fail('3+7 profile not HIGH')
print('D q=105 profiles', D)
R['controls']['D_q105_constructive_profiles'] = D

# ---------- E. even-q countercontrols (exact) ----------
E = {}
ms = [0, 15, 0, 10, 20]
E['q30_five_term_non_pentagon'] = {'exps': ms, 'zero': bool(is_zero(30, ms)), 'G_values_mod6': sorted({e % 6 for e in ms})}
ms = [0, 10, 20, 6, 16, 26, 0, 15, 6, 21]
prof = {}
for e in ms:
    prof[e % 6] = prof.get(e % 6, 0) + 1
E['q30_ten_term_even_nonconstant_profile'] = {'exps': ms, 'zero': bool(is_zero(30, ms)), 'profile_mod6': prof,
                                              'all_even': all(v % 2 == 0 for v in prof.values()), 'distinct': len(prof)}
ms = [0, 5] * 5
E['q10_antipodal_pairs'] = {'exps': ms, 'zero': bool(is_zero(10, ms)), 'classify_5+5_or_3+7': classify(10, ms)}
print('E', E)
if not (E['q30_five_term_non_pentagon']['zero'] and len(E['q30_five_term_non_pentagon']['G_values_mod6']) > 1):
    fail('E1')
if not (E['q30_ten_term_even_nonconstant_profile']['zero'] and E['q30_ten_term_even_nonconstant_profile']['all_even']
        and E['q30_ten_term_even_nonconstant_profile']['distinct'] > 1):
    fail('E2')
if not E['q10_antipodal_pairs']['zero'] or E['q10_antipodal_pairs']['classify_5+5_or_3+7']:
    fail('E3')
R['controls']['E_even_q_countercontrols'] = E

# ---------- F. matched-pair / row-quotient parity lemma instances at q=15 ----------
def all_pairings(n=10):
    def rec(rem):
        if not rem:
            yield []
            return
        a = rem[0]
        for i in range(1, len(rem)):
            b = rem[i]
            for rest in rec(rem[1:i] + rem[i + 1:]):
                yield [(a, b)] + rest
    return list(rec(list(range(n))))
pairings = all_pairings()
if len(pairings) != 945:
    fail('pairings count')
F = {}
r0 = [0] * 10
r1 = [0, 3, 6, 9, 12, 1, 4, 7, 10, 13]          # two pentagons in distinct G-cosets: profile 5+5
r1c = [0, 3, 6, 9, 12, 0, 3, 6, 9, 12]           # same coset twice: profile 10
for name, row in (('profile_5_5', r1), ('profile_10', r1c)):
    quot = [(b - a) % 15 for a, b in zip(r0, row)]
    if not is_zero(15, quot):
        fail('rows not orthogonal')
    gq = [v % 3 for v in quot]
    good = [P for P in pairings if all(gq[a] == gq[b] for a, b in P)]
    F[name] = {'row': row, 'G_profile': sorted({v: gq.count(v) for v in set(gq)}.values(), reverse=True),
               'pairings_with_equal_G_in_every_pair': len(good)}
print('F', F)
if F['profile_5_5']['pairings_with_equal_G_in_every_pair'] != 0 or F['profile_10']['pairings_with_equal_G_in_every_pair'] != 945:
    fail('F lemma instance')
R['controls']['F_row_quotient_pairing_lemma'] = F

# ---------- G/H. gauged BH(10,5) sample as a BH(10,15) matrix; dephasing; physical caller in Z[zeta_30] ----------
SAMPLE = ["0000000000", "0011223344", "0103241423", "0134310242", "0230134124",
          "0242013431", "0312404213", "0324142301", "0421431032", "0443322110"]
H5 = [[int(ch) for ch in s] for s in SAMPLE]
for a, b in itertools.combinations(range(10), 2):
    if not is_zero(5, [(H5[b][c] - H5[a][c]) for c in range(10)]):
        fail('sample rows')
    if not is_zero(5, [(H5[t][b] - H5[t][a]) for t in range(10)]):
        fail('sample cols')
rng = random.Random(20261028)
rho = [rng.randrange(15) for _ in range(10)]; kappa = [rng.randrange(15) for _ in range(10)]
A15 = [[(3 * H5[t][c] + rho[t] + kappa[c]) % 15 for c in range(10)] for t in range(10)]   # entries zeta15^A15
# Hadamard check for the gauged matrix in Z[zeta_15]
for a, b in itertools.combinations(range(10), 2):
    if not is_zero(15, [(A15[b][c] - A15[a][c]) for c in range(10)]) or not is_zero(15, [(A15[t][b] - A15[t][a]) for t in range(10)]):
        fail('gauged matrix not Hadamard')
# G. dephasing procedure of candidate section 3/4 applied to the G-valued (mod 3) matrix
Ev = (0, 2, 4, 6, 8); Ov = (1, 3, 5, 7, 9)
Aw = [row[:] for row in A15]
for half, t0 in ((Ev, 0), (Ov, 1)):
    for s in half:
        gam = {(Aw[s][c] - Aw[t0][c]) % 3 for c in range(10)}
        if len(gam) != 1:
            fail('row quotient not constant in G')
        g = gam.pop()
        Aw[s] = [(v - 10 * g) % 15 for v in Aw[s]]       # multiply row by zeta15^(-10g): exponent residue 10g = g (mod 3), i.e. g^-1 in G = mu_15/mu_5
for c in range(10):
    g = Aw[0][c] % 3
    for t in range(10):
        Aw[t][c] = (Aw[t][c] - 10 * g) % 15
if any(Aw[t][c] % 3 for t in Ev for c in range(10)):
    fail('E rows not in mu_5 after dephasing')
delta = [Aw[1][c] % 3 for c in range(10)]
if any(Aw[t][c] % 3 != delta[c] for t in Ov for c in range(10)):
    fail('O rows not a single G pattern')
if len(set(delta)) != 1:
    fail('delta not constant for a gauged mu_5 matrix')
for t in Ov:
    Aw[t] = [(v - 10 * delta[0]) % 15 for v in Aw[t]]
if any(v % 3 for row in Aw for v in row):
    fail('final matrix not in mu_5')
K5 = [[v // 3 for v in row] for row in Aw]
for a, b in itertools.combinations(range(10), 2):
    if not is_zero(5, [(K5[b][c] - K5[a][c]) for c in range(10)]) or not is_zero(5, [(K5[t][b] - K5[t][a]) for t in range(10)]):
        fail('dephased matrix not BH(10,5)')
R['controls']['G_dephasing_procedure'] = {'rho': rho, 'kappa': kappa, 'result': 'PASS: recovered an exact BH(10,5) matrix'}
print('G dephasing PASS')

# H. physical array psi_(r,c)(t) = zeta10^(rt) zeta15^(A[t][c]) = zeta30^(3rt + 2A[t][c]); exact in Z[zeta_30]
def ip_vec(A, x, y):
    (r, c), (s, d) = x, y
    return exact_sum(30, [3 * (s - r) * t + 2 * (A[t][d] - A[t][c]) for t in range(10)])
cells = [(r, c) for r in range(10) for c in range(10)]
basis = 0
for c in range(10):
    for r, s in itertools.combinations(range(10), 2):
        if ip_vec(A15, (r, c), (s, c)).any():
            fail('Fourier column basis')
        basis += 1
for r in range(10):
    for c, d in itertools.combinations(range(10), 2):
        if ip_vec(A15, (r, c), (r, d)).any():
            fail('K row basis')
        basis += 1
opp = 0
for r in range(5):
    for c in range(10):
        for d in range(10):
            lhs = ip_vec(A15, (r, c), (r + 5, d))
            SE = exact_sum(30, [2 * (A15[t][d] - A15[t][c]) for t in Ev])
            SO = exact_sum(30, [2 * (A15[t][d] - A15[t][c]) for t in Ov])
            if not np.array_equal(lhs, SE - SO):
                fail('opposite-row identity')
            opp += 1
# gauge covariance: ungauged (3*H5) vs gauged A15: N_gauged = zeta15^(kappa_d-kappa_c) N_ungauged, row phases cancel
A0 = [[3 * H5[t][c] for c in range(10)] for t in range(10)]
T30 = table(30)
def mul_root(vec, k):
    # multiply an element (coordinate vector) of Z[zeta_30] by zeta_30^k exactly
    phi = cyclotomic(30); deg = len(phi) - 1
    p = [0] * (deg + k)
    for i, v in enumerate(vec):
        p[i + k] += int(v)
    _, rr = poly_divmod(p, phi)
    out = np.zeros(deg, dtype=np.int64); out[:len(rr)] = rr
    return out
cov = 0
for x, y in itertools.combinations(cells, 2):
    n0 = ip_vec(A0, x, y); n1 = ip_vec(A15, x, y)
    k = (2 * (kappa[y[1]] - kappa[x[1]])) % 30
    if not np.array_equal(mul_root(n0, k), n1):
        fail('gauge covariance')
    cov += 1
# exact transversal search on the gauged (q=15) array
orth = {x: set() for x in cells}
for x, y in itertools.combinations(cells, 2):
    if not ip_vec(A15, x, y).any():
        orth[x].add(y); orth[y].add(x)
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
tv = find_transversal(orth)
if tv is not None:
    fail('transversal found in gauged q=15 array')
# the orthogonality graph itself must be invariant under the gauge (same edge set as the ungauged array)
orth0 = {x: set() for x in cells}
for x, y in itertools.combinations(cells, 2):
    if not ip_vec(A0, x, y).any():
        orth0[x].add(y); orth0[y].add(x)
if orth0 != orth:
    fail('gauge changed orthogonality graph')
R['controls']['H_physical_caller_q15'] = {'basis_orthogonality_checks': basis, 'opposite_row_identity_checks': opp,
                                          'gauge_covariance_cell_pairs': cov, 'orthogonality_graph_gauge_invariant': True,
                                          'orthogonal_cell_pairs': sum(len(v) for v in orth.values()) // 2,
                                          'transversal_found': False}
print('H physical caller', R['controls']['H_physical_caller_q15'])

with open(os.path.abspath(__file__), 'rb') as f:
    R['script_sha256'] = hashlib.sha256(f.read()).hexdigest()
R['elapsed_seconds'] = round(time.time() - T0, 1)
R['result'] = 'PASS'
R['observed_clock_before_receipt_creation'] = native_clock()
if os.path.exists(OUT):
    fail('receipt exists')
with open(OUT, 'x') as f:
    json.dump(R, f, indent=1, sort_keys=True, default=lambda o: o.item() if hasattr(o, 'item') else str(o)); f.write('\n')
print('PASS receipt', OUT)
