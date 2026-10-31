#!/opt/homebrew/bin/python3
"""Reviewer-authored exact controls, review wave f183-nl242-four-zero-branch-empty (v1).

Independent of the author's checker: no author code is imported, executed or exec'd.
The author's result JSON is parsed completely as DATA.  Two DATA constants were transcribed
by hand from the read-only author checker source: the ordered 8-entry candidate-weight list
(used only to cross-check which weight vector the JSON reports as the first certifying one
and the JSON's no-odd-law flags) and the relaxed type-count point (re-verified here from
first principles).  Certificate arithmetic is exact Python int; Boolean-function arithmetic
is exact numpy int64 (all magnitudes far below 2**31).

Usage: reviewer-f183-controls-v1.py OUTPUT.json   (exclusive create; '-' = stdout only)
"""
import collections
import functools
import hashlib
import itertools
import json
import operator
import pathlib
import platform
import random
import sys
import time

import numpy as np

T_START = time.monotonic()
OUT_ARG = sys.argv[1]
if OUT_ARG != '-' and pathlib.Path(OUT_ARG).exists():
    raise FileExistsError(OUT_ARG)

POS, NEG, UNKNOWN, INFO = [], [], [], {}


def pos(name, ok, **detail):
    POS.append({'name': name, 'pass': bool(ok), **detail})


def neg(name, intended, **detail):
    NEG.append({'name': name, 'intended_failure_observed': bool(intended), **detail})


def plain(o):
    if isinstance(o, dict):
        return {str(k): plain(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [plain(v) for v in o]
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


# =====================================================================================
# Part P. Parse the author's result JSON completely (data only).
# =====================================================================================
AUTHOR_RESULT = pathlib.Path(
    '/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/'
    'parallel-18/balanced-nl242/frontier-20261029-fourzero-block-energy-check-result.json')
AUTHOR_RESULT_SHA256 = '52d0ba2accae27e15d71d06daaa33406d93a0064b9a1460eb7c2cdd090e6fe61'
raw = AUTHOR_RESULT.read_bytes()
sha = hashlib.sha256(raw).hexdigest()
pos('P01_author_result_sha256_bytes_LF', sha == AUTHOR_RESULT_SHA256 and len(raw) == 19220
    and raw.count(b'\n') == 1103 and b'\r' not in raw, sha256=sha, bytes=len(raw),
    lf=raw.count(b'\n'))


def _no_dup(pairs):
    keys = [k for k, _ in pairs]
    if len(keys) != len(set(keys)):
        raise ValueError('duplicate JSON key')
    return dict(pairs)


def _no_float(s):
    raise ValueError('non-integer JSON number ' + s)


def _no_const(s):
    raise ValueError('JSON constant ' + s)


TEXT = raw.decode('utf-8')
J = json.loads(TEXT, object_pairs_hook=_no_dup, parse_float=_no_float, parse_constant=_no_const)
pos('P02_canonical_reserialization_byte_identical',
    json.dumps(J, indent=2, sort_keys=True) + '\n' == TEXT)

NODES = collections.Counter()


def walk(o):
    if isinstance(o, dict):
        NODES['object'] += 1
        for v in o.values():
            walk(v)
    elif isinstance(o, list):
        NODES['array'] += 1
        for v in o:
            walk(v)
    elif isinstance(o, bool):
        NODES['bool'] += 1
    elif isinstance(o, int):
        NODES['int'] += 1
    elif isinstance(o, str):
        NODES['string'] += 1
    elif o is None:
        NODES['null'] += 1
    else:
        raise TypeError(type(o))


walk(J)
INFO['author_json_node_counts'] = dict(NODES)


def isint(x):
    return type(x) is int


def ilist(x, n=None):
    return isinstance(x, list) and all(isint(v) for v in x) and (n is None or len(x) == n)


TOP_KEYS = {'all_cases_certified', 'cases', 'control_no_candidate_certifies_without_odd_law',
            'control_relaxed_point', 'even_types', 'odd_pattern_count', 'partA_identity_control',
            'scope'}
CASE_KEYS = {'N', 'certificate', 'form', 'h', 'multiplicity_of_(T,nu)',
             'without_odd_law_any_candidate_certifies'}
CERT_KEYS = {'capNZ', 'capOddByClass', 'capZ0', 'capacity', 'certifies', 'required', 'weights'}
RELAX_KEYS = {'NZ_count', 'Z0_count', 'affine_class_distribution', 'all_equal_4096',
              'block_energies', 'distribution_realizable_elliptic', 'odd_count'}
ok = set(J) == TOP_KEYS
CASES = J['cases']
ok &= isinstance(CASES, list) and len(CASES) == 32
for cs in CASES:
    ok &= isinstance(cs, dict) and set(cs) == CASE_KEYS
    ok &= cs['form'] in ('elliptic', 'hyperbolic') and isint(cs['h']) and cs['h'] in (0, 1)
    ok &= ilist(cs['N'], 4) and sum(cs['N']) == 64 and isint(cs['multiplicity_of_(T,nu)'])
    ok &= type(cs['without_odd_law_any_candidate_certifies']) is bool
    ce = cs['certificate']
    ok &= isinstance(ce, dict) and set(ce) == CERT_KEYS
    ok &= all(isint(ce[k]) for k in ('capNZ', 'capZ0', 'capacity', 'required'))
    ok &= type(ce['certifies']) is bool and ilist(ce['weights'], 4) and ilist(ce['capOddByClass'], 4)
JKEY = {(cs['form'], cs['h'], tuple(cs['N'])): cs for cs in CASES}
ok &= len(JKEY) == 32
ET = J['even_types']
ok &= isinstance(ET, dict) and set(ET) == {'NZ_fibre_contributions', 'Z0_nonzero_fibre_contributions'}
ok &= all(ilist(v, 4) for v in ET['NZ_fibre_contributions'])
ok &= all(ilist(v, 4) for v in ET['Z0_nonzero_fibre_contributions'])
ok &= isint(J['odd_pattern_count'])
PA = J['partA_identity_control']
ok &= isinstance(PA, dict) and set(PA) == {'checks', 'degree_failures', 'failures', 'seed'}
ok &= all(isint(v) for v in PA.values())
RP = J['control_relaxed_point']
ok &= isinstance(RP, dict) and set(RP) == RELAX_KEYS
ok &= ilist(RP['block_energies'], 4) and ilist(RP['affine_class_distribution'], 4)
ok &= all(isint(RP[k]) for k in ('NZ_count', 'Z0_count', 'odd_count'))
ok &= type(RP['all_equal_4096']) is bool and type(RP['distribution_realizable_elliptic']) is bool
ok &= type(J['all_cases_certified']) is bool
ok &= type(J['control_no_candidate_certifies_without_odd_law']) is bool
ok &= isinstance(J['scope'], str)
pos('P03_schema_complete_all_fields_typed', ok, cases=len(CASES))
INFO['author_claims_recorded_not_reproduced'] = {
    'partA_identity_control': PA, 'all_cases_certified': J['all_cases_certified'],
    'control_no_candidate_certifies_without_odd_law': J['control_no_candidate_certifies_without_odd_law'],
    'scope': J['scope']}

# =====================================================================================
# Part A. Fibre algebra on R = F2^2 from first principles.
#   r, c are 2-bit ints; bit0 <-> rho_1 (dual: lambda-hat coordinate), bit1 <-> rho_2.
#   chi_r(c) = (-1)^{r.c};  lambda(r) = r.(1,0);  nu_h(r) = h*r1*r2.
# =====================================================================================


def dot(a, b):
    return bin(a & b).count('1') & 1


def chi(r, c):
    return 1 - 2 * dot(r, c)


LAMBDA = 1


def lam(r):
    return dot(LAMBDA, r)


def nu(h, r):
    return h & (r & 1) & (r >> 1)


def uvec(k4):
    out = []
    for c in range(4):
        s = sum(chi(r, c) * k4[r] for r in range(4))
        assert s % 2 == 0
        out.append((s // 2) ** 2)
    return tuple(out)


def wdot(w, u):
    return sum(a * b for a, b in zip(w, u))


# Even fibres with Q6(s)=0, s!=0: k in {+-4}^4 (k = 0 mod 4, |k|<=7, no zero off R).
Z0_K = list(itertools.product((4, -4), repeat=4))
Z0 = sorted({uvec(e) for e in Z0_K})
pos('A01_Z0_types_are_64_at_one_block_or_16_at_all',
    Z0 == sorted({tuple(64 * (c == j) for c in range(4)) for j in range(4)} | {(16, 16, 16, 16)}),
    types=Z0)


def e8_pairwise(e, qval):
    # (E8) at every base point of the fibre: k(a+r) = k(a) + 4 lambda(r) q(a) (mod 8)
    return all((e[rp ^ r] - e[rp] - 4 * lam(r) * qval) % 8 == 0 for r in range(4) for rp in range(4))


pos('A02_Z0_vectors_satisfy_E8_trivially', all(e8_pairwise(e, 0) for e in Z0_K))
NZ_ALL_K = list(itertools.product((2, -2, 6, -6), repeat=4))
NZ_K = [e for e in NZ_ALL_K if e8_pairwise(e, 1)]
NZ = sorted({uvec(e) for e in NZ_K})
shortcut = [e for e in NZ_ALL_K
            if len({((e[r] // 2) * (1 - 2 * lam(r))) % 4 for r in range(4)}) == 1]
pos('A03_E8_pairwise_equals_candidate_shortcut_(k/2)(-1)^lambda_const_mod4',
    sorted(NZ_K) == sorted(shortcut), admissible_vectors=len(NZ_K))
BY_E = collections.defaultdict(set)
for e in NZ_K:
    BY_E[sum(1 for x in e if abs(x) == 2)].add(uvec(e))
tab_ok = sorted(BY_E) == [0, 1, 2, 3, 4]
for ne, S in BY_E.items():
    for u in S:
        lb, ot = u[LAMBDA], sorted(u[c] for c in range(4) if c != LAMBDA)
        tab_ok &= {0: (lb == 144 and ot == [0, 0, 0]), 1: (lb == 64 and ot == [16, 16, 16]),
                   2: (lb == 16 and ot == [0, 0, 64]), 3: (lb == 0 and ot == [16, 16, 16]),
                   4: (lb == 16 and ot == [0, 0, 0])}[ne]
pos('A04_section6_e_table_exact', tab_ok, by_e={str(k): sorted(v) for k, v in sorted(BY_E.items())})

# Odd fibres: k odd, |k|<=7, common residue mod 4 (rho = 0), omega-pattern in a class.
ODD = []
for o in itertools.product((1, -1, 3, -3, 5, -5, 7, -7), repeat=4):
    if len({x % 4 for x in o}) != 1:
        continue
    g = 1 if o[0] % 4 == 1 else -1
    om = tuple(1 if abs(x) in (3, 5) else 0 for x in o)
    om_def = tuple(((x - g) // 4) % 2 for x in o)
    cls = {h: tuple(x for x in range(4)
                    if all(om[r] == om[0] ^ dot(x, r) ^ nu(h, r) for r in range(4)))
           for h in (0, 1)}
    ODD.append({'k': o, 'g': g, 'om': om, 'om_def': om_def, 'u': uvec(o), 'cls': cls})
pos('A05_odd_pattern_count_512', len(ODD) == 512, n=len(ODD))
pos('A06_omega_def_equals_|k|_in_{3,5}', all(d['om'] == d['om_def'] for d in ODD))
pos('A07_each_pattern_in_exactly_one_(h,class)',
    all(len(d['cls'][0]) + len(d['cls'][1]) == 1 for d in ODD))
PER = collections.Counter((h, x) for d in ODD for h in (0, 1) for x in d['cls'][h])
pos('A08_64_patterns_per_(h,class)', all(PER[(h, x)] == 64 for h in (0, 1) for x in range(4)),
    counts={f'{h},{x}': PER[(h, x)] for h in (0, 1) for x in range(4)})


def swapbits(r):
    return ((r & 1) << 1) | (r >> 1)


rep_ok = True
for d in ODD:
    for h in (0, 1):
        for x in d['cls'][h]:
            for rp in range(4):  # base point b+rp: class shifts by beta(., rp) = h*(rp2, rp1)
                xr = x ^ (h * swapbits(rp))
                rep_ok &= all(d['om'][rp ^ r] ^ d['om'][rp] == dot(xr, r) ^ nu(h, r) for r in range(4))
pos('A09_fibre_law_consistent_at_every_representative', rep_ok)


def cap_set(S, w):
    return max(wdot(w, u) for u in S)


def cap_odd(w, h, x):
    best, arg = None, None
    for d in ODD:
        if x in d['cls'][h]:
            v = wdot(w, d['u'])
            if best is None or v > best:
                best, arg = v, d['k']
    return best, arg


def cap_odd_nolaw(w):
    return max(wdot(w, d['u']) for d in ODD)


def in_class(k4, h, x):
    for d in ODD:
        if d['k'] == tuple(k4):
            return x in d['cls'][h]
    return False


# =====================================================================================
# Part D. Class distributions N for both nondegenerate six-dimensional forms.
#   l_{b_s} = Q6(s)*lambda-hat + T(s) + nu-hat.  First coordinate P = Q6 + alpha1,
#   second coordinate alpha2, alpha_i arbitrary affine (bijective with (T, nu-hat)).
# =====================================================================================


def q_hyp(s):
    return (s & 1 & (s >> 1)) ^ ((s >> 2) & (s >> 3) & 1) ^ ((s >> 4) & (s >> 5) & 1)


def q_ell(s):
    return q_hyp(s) ^ ((s >> 4) & 1) ^ ((s >> 5) & 1)


def rank_f2(vecs):
    rows, r = list(vecs), 0
    for bit in reversed(range(16)):
        piv = next((i for i in range(r, len(rows)) if rows[i] >> bit & 1), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i] >> bit & 1:
                rows[i] ^= rows[r]
        r += 1
    return r


def polar_rank(Q):
    rows = []
    for i in range(6):
        row = 0
        for j in range(6):
            ei, ej = 1 << i, 1 << j
            if Q(ei ^ ej) ^ Q(ei) ^ Q(ej) ^ Q(0):
                row |= 1 << j
        rows.append(row)
    return rank_f2(rows)


def dists(Q):
    Qv = [Q(s) for s in range(64)]
    L = [[dot(v, s) for s in range(64)] for v in range(64)]
    cnt = collections.Counter()
    for v1 in range(64):
        for c1 in (0, 1):
            P = [Qv[s] ^ L[v1][s] ^ c1 for s in range(64)]
            for v2 in range(64):
                Lv = L[v2]
                for c2 in (0, 1):
                    N = [0, 0, 0, 0]
                    for s in range(64):
                        N[P[s] | ((Lv[s] ^ c2) << 1)] += 1
                    cnt[tuple(N)] += 1
    return cnt


CAND_N = {(0, 0, 28, 36), (0, 0, 36, 28), (12, 20, 16, 16), (16, 16, 12, 20), (16, 16, 20, 12),
          (20, 12, 16, 16), (28, 36, 0, 0), (36, 28, 0, 0)}
FORMS = {'elliptic': q_ell, 'hyperbolic': q_hyp}
ZEROS = {f: sum(1 for s in range(64) if Q(s) == 0) for f, Q in FORMS.items()}
pos('D01_zero_counts_elliptic28_hyperbolic36', ZEROS == {'elliptic': 28, 'hyperbolic': 36}, zeros=ZEROS)
pos('D02_both_forms_nondegenerate_polar_rank6', all(polar_rank(Q) == 6 for Q in FORMS.values()))
DIST = {f: dists(Q) for f, Q in FORMS.items()}
for f in FORMS:
    pos(f'D03_{f}_distribution_set_is_the_eight_vectors', set(DIST[f]) == CAND_N,
        vectors={str(list(k)): v for k, v in sorted(DIST[f].items())}, total=sum(DIST[f].values()))
rng_gl = random.Random(int.from_bytes(hashlib.sha256(b'reviewer-f183-GL6').digest()[:8], 'big'))
gl_ok, gl_used = True, []
while len(gl_used) < 2:
    cols = [rng_gl.randrange(1, 64) for _ in range(6)]
    if rank_f2(cols) != 6:
        continue
    gl_used.append(cols)

    def apply(s, cols=cols):
        v = 0
        for i in range(6):
            if s >> i & 1:
                v ^= cols[i]
        return v
    for f, Q in FORMS.items():
        Qt = (lambda s, Q=Q, apply=apply: Q(apply(s)))
        gl_ok &= sum(1 for s in range(64) if Qt(s) == 0) == ZEROS[f] and dict(dists(Qt)) == dict(DIST[f])
pos('D04_distribution_multiset_invariant_under_two_seeded_GL6_changes', gl_ok, gl_columns=gl_used)

# =====================================================================================
# Part C. Capacity certificates: all 32 cases x both weight vectors, exact integers.
# =====================================================================================
W1, W2 = (2, 3, 6, 6), (12, 5, 12, 9)
AUTHOR_CANDIDATES = [(2, 3, 6, 6), (0, 1, 2, 2), (1, 2, 4, 4), (3, 4, 8, 8), (2, 2, 5, 5),
                     (4, 2, 5, 5), (12, 5, 12, 9), (20, 11, 20, 15)]  # transcribed data


def capacity(w, form, h, N, law=True, nz_set=None):
    nZ0, nNZ = ZEROS[form] - 1, 64 - ZEROS[form]
    capZ = cap_set(Z0, w)
    capN = cap_set(NZ if nz_set is None else nz_set, w)
    capO = [cap_odd(w, h, x)[0] if law else cap_odd_nolaw(w) for x in range(4)]
    total = capZ * nZ0 + capN * nNZ + sum(capO[x] * N[x] for x in range(4))
    return {'capZ0': capZ, 'capNZ': capN, 'capOddByClass': capO, 'capacity': total,
            'required': 4096 * sum(w), 'certifies': total < 4096 * sum(w), 'nZ0': nZ0, 'nNZ': nNZ}


def rule(h, N):
    if h == 1 or N[2] + N[3] in (0, 32):
        return W1
    assert N[0] == 0 and N[1] == 0
    return W2


TABLE, all_cert, json_match, first_ok, nolaw_flag_ok = [], True, True, True, True
for form in ('elliptic', 'hyperbolic'):
    for h in (0, 1):
        for N in sorted(DIST[form]):
            w = rule(h, N)
            c1, c2 = capacity(W1, form, h, N), capacity(W2, form, h, N)
            chosen = c1 if w == W1 else c2
            all_cert &= chosen['certifies']
            js = JKEY[(form, h, N)]
            jc = js['certificate']
            first = next((tuple(cw) for cw in AUTHOR_CANDIDATES if capacity(cw, form, h, N)['certifies']), None)
            first_ok &= first == tuple(jc['weights'])
            jw = capacity(tuple(jc['weights']), form, h, N)
            json_match &= (jc['capZ0'] == jw['capZ0'] and jc['capNZ'] == jw['capNZ']
                           and jc['capOddByClass'] == jw['capOddByClass'] and jc['capacity'] == jw['capacity']
                           and jc['required'] == jw['required'] and jc['certifies'] == jw['certifies']
                           and js['multiplicity_of_(T,nu)'] == DIST[form][N])
            nolaw_any = any(capacity(cw, form, h, N, law=False)['certifies'] for cw in AUTHOR_CANDIDATES)
            nolaw_flag_ok &= js['without_odd_law_any_candidate_certifies'] == nolaw_any
            TABLE.append({'form': form, 'h': h, 'N': N, 'multiplicity': DIST[form][N], 'rule_weight': w,
                          'W1': c1, 'W2': c2, 'slack_rule': chosen['required'] - chosen['capacity'],
                          'json_weight': jc['weights'], 'first_certifying_author_candidate': first})
pos('C01_all_32_cases_certified_by_rule_weights', all_cert and len(TABLE) == 32)
pos('C02_every_json_case_matches_reviewer_recomputation', json_match)
pos('C03_json_weight_is_first_certifying_in_transcribed_candidate_order', first_ok)
pos('C04_json_no_law_flags_match', nolaw_flag_ok)
pos('C05_json_all_cases_certified_true', J['all_cases_certified'] is True)

# literal numbers of the candidate's section 7
lit = {}
lit['i_capZ_384_capNZ_432'] = cap_set(Z0, W1) == 384 and cap_set(NZ, W1) == 432
lit['i_h1_odd_668_every_class'] = all(cap_odd(W1, 1, x)[0] == 668 for x in range(4))
lit['i_example_(1,-7,-7,5)_h1_value668'] = (wdot(W1, uvec((1, -7, -7, 5))) == 668
                                           and any(in_class((1, -7, -7, 5), 1, x) for x in range(4)))
lit['i_totals_68672_68288_lt_69632'] = (384 * 27 + 432 * 36 + 668 * 64 == 68672
                                        and 384 * 35 + 432 * 28 + 668 * 64 == 68288 and 4096 * 17 == 69632)
lit['ii_h0_odd_456_456_872_872'] = [cap_odd(W1, 0, x)[0] for x in range(4)] == [456, 456, 872, 872]
lit['ii_example_(5,5,-7,-7)_class2_value872'] = (in_class((5, 5, -7, -7), 0, 2)
                                                 and wdot(W1, uvec((5, 5, -7, -7))) == 872)
lit['ii_affine_formula'] = all(
    capacity(W1, f, 0, N)['capacity'] == {'elliptic': 55104, 'hyperbolic': 54720}[f] + 416 * (N[2] + N[3])
    for f in FORMS for N in DIST[f])
lit['ii_at32_68416_68032'] = 55104 + 416 * 32 == 68416 and 54720 + 416 * 32 == 68032
lit['iii_capZ_768_capNZ_848'] = cap_set(Z0, W2) == 768 and cap_set(NZ, W2) == 848
lit['iii_odd_class2_1776_class3_1344'] = cap_odd(W2, 0, 2)[0] == 1776 and cap_odd(W2, 0, 3)[0] == 1344
lit['iii_bound_152832_and_152192_lt_155648'] = (
    768 * 27 + 848 * 36 + 1776 * 36 + 1344 * 28 == 152832 and 768 * 35 + 848 * 28 + 1776 * 36 + 1344 * 28 == 152192
    and 4096 * 38 == 155648
    and max(capacity(W2, 'elliptic', 0, N)['capacity'] for N in DIST['elliptic'] if N[0] == N[1] == 0) == 152832
    and max(capacity(W2, 'hyperbolic', 0, N)['capacity'] for N in DIST['hyperbolic'] if N[0] == N[1] == 0) == 152192)
pos('C06_section7_literal_numbers', all(lit.values()), detail=lit)
pos('C07_json_even_types_equal_reviewer_sets',
    sorted(map(tuple, ET['Z0_nonzero_fibre_contributions'])) == Z0
    and sorted(map(tuple, ET['NZ_fibre_contributions'])) == NZ)
pos('C08_json_odd_pattern_count_512', J['odd_pattern_count'] == 512)

# =====================================================================================
# Part N. Negative controls for the certificate (intended reasons).
# =====================================================================================
# N1: drop the odd mod-8 law (all 512 common-residue patterns allowed in every fibre).
n1 = all(not capacity(cw, f, h, N, law=False)['certifies']
         for f in FORMS for h in (0, 1) for N in DIST[f] for cw in AUTHOR_CANDIDATES)
n1_detail = {str(cw): cap_odd_nolaw(cw) for cw in (W1, W2)}
neg('N1_drop_odd_law_no_candidate_weight_certifies_any_case', n1,
    odd_capacity_without_law=n1_detail)

# N2: relaxed type-count point (transcribed data), re-verified from first principles.
RELAX_EVEN = [((0, 64, 0, 0), 3, 'Z0'), ((0, 0, 64, 0), 24, 'Z0'), ((0, 144, 0, 0), 20, 'NZ'),
              ((16, 64, 16, 16), 16, 'NZ')]
RELAX_ODD = [((5, 1, 1, 5), 1), ((5, -7, -7, 5), 12), ((-3, -7, -7, -3), 5), ((-7, 5, 5, -7), 14),
             ((-7, -7, 5, 5), 16), ((-7, -7, -7, -7), 16)]
blocks = [0, 0, 0, 0]
adm = True
for u, n, kind in RELAX_EVEN:
    adm &= u in (Z0 if kind == 'Z0' else NZ)
    for c in range(4):
        blocks[c] += u[c] * n
cls_count = collections.Counter()
for k4, n in RELAX_ODD:
    d = next(d for d in ODD if d['k'] == k4)
    adm &= len(d['cls'][0]) == 1
    cls_count[d['cls'][0][0]] += n
    for c in range(4):
        blocks[c] += d['u'][c] * n
Nrel = tuple(cls_count[x] for x in range(4))
counts_ok = (sum(n for _, n, k in RELAX_EVEN if k == 'Z0') == ZEROS['elliptic'] - 1
             and sum(n for _, n, k in RELAX_EVEN if k == 'NZ') == 64 - ZEROS['elliptic']
             and sum(n for _, n in RELAX_ODD) == 64)
pos('N2a_relaxed_point_admissible_counts_and_four_block_energies_4096',
    adm and counts_ok and blocks == [4096] * 4, blocks=blocks, N=Nrel)
pos('N2b_relaxed_point_matches_author_json', list(Nrel) == RP['affine_class_distribution']
    and blocks == RP['block_energies'] and RP['all_equal_4096'] is True
    and RP['Z0_count'] == 27 and RP['NZ_count'] == 36 and RP['odd_count'] == 64
    and RP['distribution_realizable_elliptic'] is False)
neg('N2c_(16,0,16,32)_not_realizable_in_either_form',
    Nrel == (16, 0, 16, 32) and all(Nrel not in DIST[f] for f in FORMS))
tight = all(sum(wdot(w, u) * n for u, n, _ in RELAX_EVEN)
            + sum(wdot(w, next(d for d in ODD if d['k'] == k4)['u']) * n for k4, n in RELAX_ODD)
            == 4096 * sum(w) for w in AUTHOR_CANDIDATES)
neg('N2d_no_weight_certifies_at_unrealizable_point_(weak_duality_tight)',
    tight and not capacity(W1, 'elliptic', 0, Nrel)['certifies']
    and not capacity(W2, 'elliptic', 0, Nrel)['certifies'],
    W1=capacity(W1, 'elliptic', 0, Nrel)['capacity'], W2=capacity(W2, 'elliptic', 0, Nrel)['capacity'])

# N3: case split is essential: W1 fails for h=0, N2+N3=64.
n3 = {f'{f}:{N}': capacity(W1, f, 0, N)['capacity'] for f in FORMS for N in DIST[f] if N[2] + N[3] == 64}
neg('N3_W1_fails_when_h0_and_N2+N3_eq_64', all(v >= 69632 for v in n3.values()), capacities=n3)

# N4: reviewer-constructed no-law feasible points for BOTH forms.  They also satisfy
# the affine odd law, but their distribution (20,0,20,24) is geometrically unrealizable.
# No-law removal lets these same patterns be used in every N/h case.  Exact block
# energies establish by weak duality that NO weight vector can certify either form.
NOLAW_POINTS = {
    'elliptic': {
        'Z0': [((64, 0, 0, 0), 1), ((0, 64, 0, 0), 1),
               ((0, 0, 64, 0), 17), ((0, 0, 0, 64), 8)],
        'NZ': [((0, 144, 0, 0), 28), ((16, 0, 16, 16), 8)],
        'odd_k': [((-7, -7, -7, -7), 19), ((1, 1, 1, 1), 1),
                  ((-7, -7, 5, 5), 20), ((-7, 5, 5, -7), 24)]
    },
    'hyperbolic': {
        'Z0': [((64, 0, 0, 0), 5), ((0, 64, 0, 0), 1),
               ((0, 0, 64, 0), 19), ((0, 0, 0, 64), 10)],
        'NZ': [((0, 144, 0, 0), 28)],
        'odd_k': [((-7, -7, -7, -7), 18), ((-3, -3, -3, -3), 2),
                  ((-7, -7, 5, 5), 20), ((-7, 5, 5, -7), 24)]
    }
}
for form, point in NOLAW_POINTS.items():
    blocks4, distribution = [0] * 4, [0] * 4
    admissible = (sum(n for _, n in point['Z0']) == ZEROS[form] - 1
                  and sum(n for _, n in point['NZ']) == 64 - ZEROS[form]
                  and sum(n for _, n in point['odd_k']) == 64)
    for kind, allowed in (('Z0', Z0), ('NZ', NZ)):
        for u, n in point[kind]:
            admissible &= u in allowed and type(n) is int and n >= 0
            for c in range(4):
                blocks4[c] += n * u[c]
    for k4, n in point['odd_k']:
        d = next((d for d in ODD if d['k'] == k4), None)
        admissible &= d is not None and len(d['cls'][0]) == 1
        if d is not None:
            distribution[d['cls'][0][0]] += n
            for c in range(4):
                blocks4[c] += n * d['u'][c]
    neg(f'N4_{form}_no_law_type_count_point_meets_all_four_block_equations',
        admissible and blocks4 == [4096] * 4 and tuple(distribution) not in DIST[form],
        blocks=blocks4, distribution=distribution)
    point['blocks'] = blocks4
    point['distribution'] = distribution
INFO['no_law_points'] = NOLAW_POINTS

# S1 (sensitivity, informational): drop the (E8) restriction on the Q6=1 even fibres.
NZ_NOE8 = sorted({uvec(e) for e in NZ_ALL_K})
s1 = {f'{f}|h{h}|{N}': capacity(rule(h, N), f, h, N, nz_set=NZ_NOE8)['certifies']
      for f in FORMS for h in (0, 1) for N in DIST[f]}
INFO['S1_rule_weights_without_E8_on_q1_even_fibres_certify'] = s1
INFO['S1_count_certified_without_E8'] = sum(s1.values())

# =====================================================================================
# Part B. Seeded balanced Boolean functions on F2^9: Lemma 1, its mod-8 form, deg Q^r <= 2,
#   the standard mod-4 fact, tau linearity, Lemma 4 block energies on 7-flats.
# =====================================================================================
IDX = np.arange(512, dtype=np.int64)
POPC = np.array([bin(i).count('1') for i in range(512)], dtype=np.int64)
PAR = np.array([[bin(a & y).count('1') & 1 for y in range(512)] for a in range(512)], dtype=np.int64)
HAD = 1 - 2 * PAR
XORT = IDX[:, None] ^ IDX[None, :]


def anf(Mat):
    A = (Mat & 1).copy()
    for i in range(9):
        bit = 1 << i
        rows = IDX[(IDX & bit) != 0]
        A[rows] ^= A[rows ^ bit]
    return A


def degrees(Mat):
    return np.where(anf(Mat) == 1, POPC[:, None], -1).max(axis=0)


def seeded(tag):
    return random.Random(int.from_bytes(hashlib.sha256(tag.encode()).digest()[:8], 'big'))


def analyse(Ms):
    Ms = sorted(Ms)
    m = np.zeros(512, dtype=np.int64)
    m[Ms] = 1
    F = 1 - 2 * m
    W = HAD @ F
    k = W // 4
    N = PAR[:, Ms].sum(axis=1)
    T = functools.reduce(operator.xor, Ms, 0)
    xT = PAR[:, T]
    PM = PAR[:, Ms]
    G = PM @ PM.T  # G[x, r] = N^r(x)
    tau = np.array([functools.reduce(operator.xor, [y for y in Ms if bin(r & y).count('1') & 1], 0)
                    for r in range(512)], dtype=np.int64)
    return {'Ms': Ms, 'F': F, 'W': W, 'k': k, 'N': N, 'T': T, 'xT': xT, 'G': G, 'tau': tau}


lucas_ok = all((n * (n - 1) // 2) % 2 == (n >> 1) & 1 for n in range(513))
pos('B00_Lucas_second_bit_equals_C(n,2)_mod2_for_n<=512', lucas_ok)
BOOL = collections.defaultdict(lambda: True)
BNEG = collections.defaultdict(lambda: True)
BCOUNT = collections.Counter()
NF = 12
for fi in range(NF):
    rng = seeded(f'reviewer-f183-boolean-{fi}')
    D_ = analyse(rng.sample(range(512), 256))
    k, N, G, tau, xT, W = D_['k'], D_['N'], D_['G'], D_['tau'], D_['xT'], D_['W']
    BOOL['balanced_W0_eq_0_and_W_div_4'] &= int(W[0]) == 0 and bool((W % 4 == 0).all())
    BOOL['k_eq_N_minus_128_and_k0_eq_0'] &= bool((k[1:] == N[1:] - 128).all()) and int(k[0]) == 0
    BOOL['k_parity_is_a.T'] &= bool(((k % 2) == xT).all())
    e2 = (N >> 1) & 1
    Km, Hm = xT == 0, xT == 1
    BOOL['even_half_(k/2)_mod2_eq_e2'] &= bool(((((k // 2) % 2) == e2)[Km]).all())
    BOOL['odd_half_k_mod4_eq_(-1)^e2_standard_fact'] &= bool((((k % 4) == ((1 + 2 * e2) % 4))[Hm]).all())
    BNEG['odd_half_wrong_sign_-(-1)^e2_fails_at_every_odd_point'] &= bool((((k % 4) != ((-(1 + 2 * e2)) % 4))[Hm]).all())
    BOOL['deg_e2_le_2'] &= int(degrees(e2[:, None])[0]) <= 2
    Bpol = e2[XORT] ^ e2[:, None] ^ e2[None, :] ^ e2[0]
    BOOL['polar_e2_eq_(x.T)(y.T)+x^T A y'] &= bool((Bpol == ((np.outer(xT, xT) + G) % 2)).all())
    BOOL['tau_r_linear_in_r'] &= bool((tau[XORT] == (tau[:, None] ^ tau[None, :])).all())
    srng = seeded(f'reviewer-f183-sample-{fi}')
    for _ in range(64):
        x, r = srng.randrange(512), srng.randrange(1, 512)
        Mr = [y for y in D_['Ms'] if bin(r & y).count('1') & 1]
        BOOL['direct_count_N^r(x)_and_|M^r|'] &= (int(G[x, r]) == sum(bin(x & y).count('1') & 1 for y in Mr)
                                                  and len(Mr) == int(N[r]))
        BCOUNT['direct_samples'] += 1
    Dm = k[XORT] - k[:, None]
    RHS = N[None, :] - 2 * G
    off = np.ones((512, 512), dtype=bool)
    off[0, :] = False
    off[:, 0] = False
    off[IDX, IDX] = False
    BOOL['lemma1_exact_for_x_not_in_{0,r}'] &= bool((Dm == RHS)[off].all())
    BCOUNT['lemma1_exact_checks'] += int(off.sum())
    diff = Dm - RHS
    BNEG['lemma1_exact_fails_at_x=0_by_-128'] &= bool((diff[0, 1:] == -128).all())
    BNEG['lemma1_exact_fails_at_x=r_by_+128'] &= bool((diff[IDX[1:], IDX[1:]] == 128).all())
    xt = PAR[IDX[:, None], tau[None, :]]
    Qr = (G >> 1) & 1
    BOOL['bit0_of_N^r_eq_x.tau^r'] &= bool(((G % 2) == xt).all())
    BOOL['lemma1_mod8_all_x_all_r'] &= bool(((((Dm - N[None, :] + 2 * xt + 4 * Qr) % 8) == 0)[:, 1:]).all())
    BCOUNT['lemma1_mod8_checks'] += 512 * 511
    dq = degrees(Qr)
    BOOL['deg_Q^r_le_2_all_511_r'] &= bool((dq[1:] <= 2).all())
    BCOUNT['degree_checks'] += 511
    d3 = degrees((G >> 2) & 1)
    BCOUNT['r_with_deg(third_bit_of_N^r)>2'] += int((d3[1:] > 2).sum())
    f4 = (((Dm - N[None, :] + 2 * xt) % 8) != 0)[:, 1:]
    BNEG['drop_-4Q^r_term_fails_exactly_where_Q^r=1'] &= bool((f4 == (Qr[:, 1:] == 1)).all()) and bool(f4.any())
    fs = (((Dm - N[None, :] - 2 * xt + 4 * Qr) % 8) != 0)[:, 1:]
    BNEG['flip_sign_of_2x.tau^r_fails_exactly_where_x.tau^r=1'] &= bool((fs == (xt[:, 1:] == 1)).all()) and bool(fs.any())
    C = np.array([int((k * k[IDX ^ r]).sum()) for r in range(512)], dtype=np.int64)
    BOOL['correlations_C0=16384_Cr=0'] &= int(C[0]) == 16384 and bool((C[1:] == 0).all())
    prng = seeded(f'reviewer-f183-planes-{fi}')
    ksh = k.copy()
    perm = list(range(1, 512))
    prng.shuffle(perm)
    ksh[1:] = k[perm]
    Csh = {}
    for _ in range(8):
        while True:
            r1, r2 = prng.randrange(1, 512), prng.randrange(1, 512)
            if r1 != r2:
                break
        R4 = [0, r1, r2, r1 ^ r2]
        reps = IDX[(IDX <= (IDX ^ r1)) & (IDX <= (IDX ^ r2)) & (IDX <= (IDX ^ r1 ^ r2))]
        for arr, tag in ((k, 'bool'), (ksh, 'shuffled')):
            S = np.array([sum(chi(rt, c) * arr[IDX ^ R4[rt]] for rt in range(4)) for c in range(4)])
            E = [int((S[c][reps] ** 2).sum()) for c in range(4)]
            Cv = [int((arr * arr[IDX ^ R4[rt]]).sum()) for rt in range(4)]
            ident = all(sum(chi(r0, c) * E[c] for c in range(4)) == 4 * Cv[r0] for r0 in range(4))
            if tag == 'bool':
                BOOL['lemma4_block_sums_16384_each_(4096_after_/4)'] &= len(reps) == 128 and E == [16384] * 4
                BOOL['lemma4_equivalence_identity_sum_c_chi_E=4C'] &= ident
                for c in range(4):
                    mask = ((PAR[:, r1] == (c & 1)) & (PAR[:, r2] == (c >> 1))).astype(np.int64)
                    Wc = HAD @ (D_['F'] * mask)
                    BOOL['lemma4_restricted_Walsh_eq_sum_chi_k'] &= bool((Wc == S[c]).all())
                BCOUNT['planes'] += 1
            else:
                BOOL['lemma4_equivalence_identity_holds_for_non_Boolean_array_too'] &= ident
                bad = E != [16384] * 4
                BCOUNT['shuffled_planes_with_block_violation'] += int(bad)
                if bad:
                    BNEG['shuffled_array_block_violation_explained_by_nonzero_C(r)_r_in_plane'] &= any(Cv[rt] != 0 for rt in (1, 2, 3))
                BNEG['shuffled_array_keeps_Parseval_C0=16384'] &= Cv[0] == 16384
    BCOUNT['functions'] += 1
for name, v in BOOL.items():
    pos('B_' + name, v)
for name, v in BNEG.items():
    neg('BN_' + name, v)
neg('BN_third_bit_of_N^r_not_quadratic_(only_second_bit_is)', BCOUNT['r_with_deg(third_bit_of_N^r)>2'] > 0,
    count=BCOUNT['r_with_deg(third_bit_of_N^r)>2'])
neg('BN_shuffled_array_violates_some_block_equation', BCOUNT['shuffled_planes_with_block_violation'] > 0,
    count=BCOUNT['shuffled_planes_with_block_violation'])
INFO['boolean_counts'] = dict(BCOUNT)

# =====================================================================================
# Part K. Constructed real balanced functions with tau^r = 0 on a 2-plane R' and
#   |M^r| = 0 mod 4 (|M^rho1| = 4 mod 8): Lemma-2 law, cocycle, affine derivative,
#   fibre law on H, and where the target-only beta-constancy input matters.
# =====================================================================================


def construct(rng, rho1, rho2, max_iter):
    r3 = rho1 ^ rho2
    pts = list(range(512))
    rng.shuffle(pts)
    M, O = pts[:256], pts[256:]

    def d(y, r):
        return bin(y & r).count('1') & 1
    t1 = t2 = c1 = c2 = c3 = 0
    for y in M:
        if d(y, rho1):
            t1 ^= y
            c1 += 1
        if d(y, rho2):
            t2 ^= y
            c2 += 1
        c3 += d(y, r3)

    def obj(a, b, x1, x2, x3):
        return bin(a).count('1') + bin(b).count('1') + (x1 % 8 != 4) + (x2 % 4 != 0) + (x3 % 4 != 0)
    cur, it = obj(t1, t2, c1, c2, c3), 0
    while cur and it < max_iter:
        it += 1
        i, j = rng.randrange(256), rng.randrange(256)
        y, z = M[i], O[j]
        a1, b1, a2, b2 = d(y, rho1), d(z, rho1), d(y, rho2), d(z, rho2)
        n1 = t1 ^ (y if a1 else 0) ^ (z if b1 else 0)
        n2 = t2 ^ (y if a2 else 0) ^ (z if b2 else 0)
        m1, m2, m3 = c1 - a1 + b1, c2 - a2 + b2, c3 - d(y, r3) + d(z, r3)
        new = obj(n1, n2, m1, m2, m3)
        if new <= cur:
            M[i], O[j] = z, y
            t1, t2, c1, c2, c3, cur = n1, n2, m1, m2, m3, new
    return (sorted(M), it) if cur == 0 else (None, it)


KOK = collections.defaultdict(lambda: True)
KNEG = collections.defaultdict(lambda: True)
KCOUNT = collections.Counter()
for fi in range(4):
    rng = seeded(f'reviewer-f183-construct-{fi}')
    while True:
        rho1, rho2 = rng.randrange(1, 512), rng.randrange(1, 512)
        if rho1 != rho2:
            break
    Ms, iters = None, 0
    for attempt in range(6):
        Ms, it = construct(rng, rho1, rho2, 300000)
        iters += it
        if Ms is not None:
            break
    if Ms is None:
        UNKNOWN.append(f'K_construct_{fi}_not_found_within_budget')
        continue
    D_ = analyse(Ms)
    k, N, G, tau, xT = D_['k'], D_['N'], D_['G'], D_['tau'], D_['xT']
    R4 = [0, rho1, rho2, rho1 ^ rho2]
    KOK['tau^r=0_on_plane_and_|M^r|=0_mod4'] &= all(int(tau[r]) == 0 for r in R4) and all(int(N[r]) % 4 == 0 for r in R4)
    Qr = (G >> 1) & 1
    phi = {0: np.zeros(512, dtype=np.int64)}
    for r in R4[1:]:
        phi[r] = ((int(N[r]) // 4) + Qr[:, r]) % 2
    for r in R4:
        KOK['lemma2_law_k(x+r)-k(x)=4phi_r(x)_mod8_all_x'] &= bool((((k[IDX ^ r] - k - 4 * phi[r]) % 8) == 0).all())
        KOK['k_mod4_invariant_under_plane'] &= bool((((k[IDX ^ r] - k) % 4) == 0).all())
        KOK['deg_phi_r_le_2'] &= int(degrees(phi[r][:, None])[0]) <= 2
    KNEG['omit_|M^rho1|/4_term_(=1_mod2)_fails_at_every_x'] &= (int(N[rho1]) % 8 == 4 and bool(
        (((k[IDX ^ rho1] - k - 4 * Qr[:, rho1]) % 8) != 0).all()))
    nonconst_H = 0
    for r in R4:
        for rp in R4:
            KOK['cocycle_phi_{r+r\'}(x)=phi_r\'(x+r)+phi_r(x)'] &= bool((phi[r ^ rp] == (phi[rp][IDX ^ r] ^ phi[r])).all())
            Dv = phi[rp][IDX ^ r] ^ phi[rp]
            KOK['D_r_phi_r\'_affine'] &= int(degrees(Dv[:, None])[0]) <= 1
            cK = len(set(Dv[xT == 0].tolist())) == 1
            cH = len(set(Dv[xT == 1].tolist())) == 1
            KOK['D_r_phi_r\'_constant_on_K_iff_on_H'] &= cK == cH
            nonconst_H += int(not cH)
    KCOUNT['pairs_(r,r\')_with_D_r_phi_r\'_nonconstant_on_H'] += nonconst_H
    g = np.where(k % 4 == 1, 1, -1)
    om = ((k - g) // 4) % 2
    Hidx = IDX[xT == 1]
    for r in R4:
        KOK['fibre_law_omega(b+r)=omega(b)+phi_r(b)_on_H'] &= bool((om[Hidx ^ r] == (om[Hidx] ^ phi[r][Hidx])).all())
    KCOUNT['constructed_functions'] += 1
    KCOUNT['construction_iterations'] += iters
for name, v in KOK.items():
    pos('K_' + name, v)
for name, v in KNEG.items():
    neg('KN_' + name, v)
if KCOUNT['pairs_(r,r\')_with_D_r_phi_r\'_nonconstant_on_H'] > 0:
    neg('KN_beta_constancy_fails_without_target_input_phi_r|K_R-invariant', True,
        count=KCOUNT['pairs_(r,r\')_with_D_r_phi_r\'_nonconstant_on_H'])
else:
    UNKNOWN.append('KN_beta_constancy_negative_not_exercised (all constructed D_r phi_r\' constant on H)')
INFO['constructed_counts'] = dict(KCOUNT)

# =====================================================================================
ELAPSED = time.monotonic() - T_START
summary = {'positive_pass': sum(p['pass'] for p in POS), 'positive_total': len(POS),
           'negative_intended': sum(n['intended_failure_observed'] for n in NEG), 'negative_total': len(NEG),
           'unknown': UNKNOWN, 'elapsed_seconds': round(ELAPSED, 3)}
result = {'schema': 'reviewer-f183-controls-v1', 'summary': summary, 'positive': POS, 'negative': NEG,
          'unknown': UNKNOWN, 'info': INFO, 'certificate_table': TABLE,
          'environment': {'python': platform.python_version(), 'numpy': np.__version__},
          'author_code_imported_or_executed': False}
payload = json.dumps(plain(result), indent=1, sort_keys=True) + '\n'
if OUT_ARG == '-':
    sys.stdout.write(payload)
else:
    with open(OUT_ARG, 'x', encoding='utf-8') as fh:
        fh.write(payload)
print(json.dumps(plain(summary), sort_keys=True), file=sys.stderr)
ALL_OK = (summary['positive_pass'] == summary['positive_total']
          and summary['negative_intended'] == summary['negative_total'])
sys.exit(0 if ALL_OK else 1)
