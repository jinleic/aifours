#!/usr/bin/env python3
"""ReviewF176ShorProof -- independent bounded exact controls, wave
f176-shor-165-all-tail-written-proof (candidate SHA-256 20169ac9...).

Independently authored by the reviewer.  It does NOT import, exec or call the
author's checker; the checker file is only hashed (bytes read) to bind this run
to the frozen inputs.  Standard library only: integers, gcd, exact integer
polynomial division, a seeded PRNG for bounded samples, and an exact-cover
search (Algorithm X with minimum-remaining-values column choice).

Writes reviewer-f176-controls-v1-output.json next to this file.  Exit status 0
iff every stated expectation below is observed; 1 otherwise.

Expectations for R9 were first observed in a reviewer-only in-memory prototype
(same session) and are re-run here from scratch; this is disclosed in review-v1.md.
"""
import hashlib
import json
import os
import platform
import random
import sys
import time
from functools import lru_cache
from itertools import combinations, product
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPATH = os.path.join(HERE, 'reviewer-f176-controls-v1-output.json')
SRC = ('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/'
       'parallel-18/shor-completion/')
INPUTS = {
    'candidate': (SRC + 'frontier-20261029-165-family-all-q-anchored-border-no-go-v1.md',
                  '20169ac9e398d9d1ef37d263f9b51d0f9168c095c3e3eb21ade47572822d39c6'),
    'author_checker_hash_only': (SRC + 'frontier-20261029-165-family-all-q-check.py',
                                 '4c550a5750a822235f20a9862d582082f3427c307f6196575099149638a4538e'),
}
T_START = time.time()
OUT = {'meta': {'python': sys.version, 'platform': platform.platform(),
                'start_unix': T_START}, 'checks': {}, 'data': {}}
FAILED = []


def jsonable(x):
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple, set)):
        seq = sorted(x) if isinstance(x, set) else x
        return [jsonable(v) for v in seq]
    return x


def expect(name, cond, **detail):
    OUT['checks'][name] = {'pass': bool(cond), **jsonable(detail)}
    if not cond:
        FAILED.append(name)


# R0 -- bind run to the frozen inputs (hash only; nothing is executed).
for key, (path, want) in INPUTS.items():
    with open(path, 'rb') as fh:
        raw = fh.read()
    got = hashlib.sha256(raw).hexdigest()
    expect('R0_input_sha256_' + key, got == want, sha256=got, bytes=len(raw),
           LF=raw.count(b'\n'))

A = (0, 3, 8, 11)
Y = (0, 1, 7, 13, 14)
G11 = {0: 0, 1: 1, 2: 7, 3: 2, 4: 3}       # g(u): mod-11 residue of the anchor that is u mod 5
S_CLAIM = [0, 1, 7, 13, 14, 55, 56, 62, 68, 110, 234, 276, 282, 288, 289]


def nz_div(xs, n):
    """Div_n restricted to nonzero differences."""
    return {gcd((s - u) % n, n) for s in xs for u in xs if (s - u) % n}


def nprimes(u):
    return sum(1 for p in (3, 5, 11) if u % p == 0)


def sq_ok(x, y):
    """(SQ) at type level: opposite parity => not exactly one of 3,5,11 divides."""
    return (x - y) % 2 == 0 or nprimes(x - y) != 1


def sp_ok(x, y):
    """(SP) at type level: opposite parity => at least one of 3,5,11 divides."""
    return (x - y) % 2 == 0 or nprimes(x - y) >= 1


# R1 -- Lemma 1, anchor divisor sets and the t=1 boundary.
r1 = {}
for t in range(1, 9):
    n = 165 * 2 ** t
    dA, dY = nz_div(A, n), nz_div(Y, n)
    r1[t] = {'n': n, 'DivA': sorted(dA), 'DivY': sorted(dY), 'common': sorted(dA & dY)}
OUT['data']['R1_anchor_divisor_sets'] = jsonable(r1)
expect('R1a_t1_anchor_divisor_collision_is_exactly_2', r1[1]['common'] == [2])
expect('R1b_t2_to_t8_no_anchor_divisor_collision', all(not r1[t]['common'] for t in range(2, 9)))
expect('R1c_3_5_11_in_DivA_and_1_in_DivY_t1_to_t8',
       all({3, 5, 11} <= set(r1[t]['DivA']) and 1 in r1[t]['DivY'] for t in r1))
expect('R1d_lemma1_exhaustive_odd_u_t1_to_t6',
       all(gcd(u, 165 * 2 ** t) == gcd(u, 165) for t in range(1, 7) for u in range(1, 165 * 2 ** t, 2)))
ok = True
for t in range(1, 5):
    n = 165 * 2 ** t
    for u in range(1, n, 2):
        g = gcd(u, n)
        if (g in (3, 5, 11)) != (nprimes(u) == 1) or (g == 1) != (nprimes(u) == 0):
            ok = False
expect('R1e_type_rules_equal_actual_gcd_rules_on_odd_differences_t1_to_t4', ok)

# R2 -- Lemma 3 and exhaustiveness of d.
CLASSES3 = ((15, 4), (33, 1), (55, 2))
r2 = {}
for (m, r) in CLASSES3:
    cls = [z for z in range(330) if z % m == r]
    passing = [z for z in cls if all(sp_ok(z, a) for a in A)]
    odd_pair = (r % m, (r - 8) % m)
    even_pair = ((r - 3) % m, (r - 11) % m)
    pm = [p for p in (3, 5, 11) if m % p == 0]
    third = [p for p in (3, 5, 11) if m % p][0]
    r2['%d mod %d' % (r, m)] = {
        'passing_types_mod330': passing, 'odd_x_minus_0_and_8_mod_m': odd_pair,
        'even_x_minus_3_and_11_mod_m': even_pair,
        'diffs_coprime_to_class_primes': all(v % p for v in odd_pair + even_pair for p in pm),
        'third_prime': third, 'third_prime_divides_8': 8 % third == 0}
OUT['data']['R2_lemma3'] = jsonable(r2)
expect('R2a_lemma3_no_admissible_head_type_mod330', all(not v['passing_types_mod330'] for v in r2.values()))
expect('R2b_lemma3_table_values_and_reason',
       r2['4 mod 15']['odd_x_minus_0_and_8_mod_m'] == (4, 11)
       and r2['4 mod 15']['even_x_minus_3_and_11_mod_m'] == (1, 8)
       and r2['1 mod 33']['odd_x_minus_0_and_8_mod_m'] == (1, 26)
       and r2['1 mod 33']['even_x_minus_3_and_11_mod_m'] == (31, 23)
       and r2['2 mod 55']['odd_x_minus_0_and_8_mod_m'] == (2, 49)
       and r2['2 mod 55']['even_x_minus_3_and_11_mod_m'] == (54, 46)
       and all(v['diffs_coprime_to_class_primes'] and not v['third_prime_divides_8'] for v in r2.values()))
odd_divs = [d for d in range(1, 166) if 165 % d == 0]
allowed = [d for d in odd_divs if not any(d % m == 0 for m, _ in CLASSES3)]
expect('R2c_d_exhaustive_is_1_3_5_11', allowed == [1, 3, 5, 11], allowed=allowed)
drops = {}
for drop in A:
    Ad = [a for a in A if a != drop]
    drops[drop] = {'%d mod %d' % (r, m): len([z for z in range(330) if z % m == r and all(sp_ok(z, a) for a in Ad)])
                   for (m, r) in CLASSES3}
expect('R2d_negative_control_each_head_needed_for_lemma3', all(any(v > 0 for v in drops[a].values()) for a in A),
       passing_counts_when_one_head_dropped=drops)
ok = True
for t in range(1, 7):
    n = 165 * 2 ** t
    for x in range(n):
        if x % 15 == 4 or x % 33 == 1 or x % 55 == 2:
            if not any((x - a) % 2 == 1 and gcd((x - a) % n, n) == 1 for a in A):
                ok = False
expect('R2e_lemma3_with_actual_gcd_every_residue_t1_to_t6', ok)


# R3 -- Section 6, cases d=1,3,5.
def dom(e, r, yset=Y):
    return [z for z in range(330) if z % e == r and all(sq_ok(z, y) for y in yset)]


def states(zs, f):
    return sorted({(z % 2, z % f) for z in zs})


expect('R3a_e165_class2_empty', dom(165, 2) == [],
       primes_dividing_2_minus_13=nprimes(2 - 13), primes_dividing_167_minus_14=nprimes(167 - 14))
D55 = {r: dom(55, r) for r in (3, 24, 25)}
st55 = {r: states(D55[r], 3) for r in D55}
expect('R3b_e55_states_parity_mod3', st55 == {3: [(1, 2)], 24: [(1, 2)], 25: [(0, 0), (0, 2)]}, states=st55)
expect('R3c_e55_no_pairwise_compatible_triple',
       not any(sq_ok(a, b) and sq_ok(a, c) and sq_ok(b, c) for a in D55[3] for b in D55[24] for c in D55[25]))
D33 = {r: dom(33, r) for r in (22, 3, 4, 15)}
st33 = {r: states(D33[r], 5) for r in D33}
expect('R3d_e33_states_parity_mod5',
       st33 == {22: [(1, 0)], 3: [(0, 0), (0, 4)], 4: [(1, 1), (1, 2), (1, 3)], 15: [(0, 0), (0, 4), (1, 0)]},
       states=st33)
expect('R3e_e33_no_pairwise_compatible_4tuple',
       not any(all(sq_ok(u, v) for u, v in combinations(tt, 2))
               for tt in product(D33[22], D33[3], D33[4], D33[15])))
# Bracketed class differences r-y and k exactly as printed in the candidate.
BR = {55: [(3, 1, 2, 0), (3, 13, -10, 1), (3, 0, 3, 0), (3, 14, -11, 1), (24, 1, 23, 0), (24, 13, 11, 1),
           (24, 0, 24, 0), (24, 14, 10, 1), (25, 0, 25, 1), (25, 14, 11, 1), (25, 1, 24, 0), (25, 7, 18, 0),
           (25, 13, 12, 0), (25, 3, 22, 1), (25, 24, 1, 0)],
      33: [(22, 1, 21, 1), (22, 7, 15, 1), (22, 0, 22, 1), (3, 0, 3, 1), (3, 14, -11, 1), (3, 1, 2, 0),
           (3, 7, -4, 0), (3, 13, -10, 0), (4, 1, 3, 1), (4, 7, -3, 1), (4, 0, 4, 0), (4, 14, -10, 0),
           (15, 0, 15, 1), (15, 1, 14, 0), (15, 7, 8, 0), (15, 13, 2, 0), (3, 22, -19, 0), (15, 3, 12, 1),
           (15, 22, -7, 0), (4, 15, 11, 1)]}
bracket_issues = []
for e, rows in BR.items():
    fixed = [p for p in (3, 5, 11) if e % p == 0]
    for (r, y, printed, kp) in rows:
        diff = r - (y % e)
        k = sum(1 for p in fixed if diff % p == 0)
        if diff != printed or k != kp:
            bracket_issues.append({'e': e, 'class': r, 'against': y, 'printed': printed, 'r_minus_y': diff,
                                   'printed_k': kp, 'k': k})
expect('R3f_brackets_only_known_sign_typo', bracket_issues ==
       [{'e': 33, 'class': 4, 'against': 15, 'printed': 11, 'r_minus_y': -11, 'printed_k': 1, 'k': 1}],
       issues=bracket_issues)


def full_selections(e, yset=Y, cap=10 ** 6, fixed=None):
    D = {r: dom(e, r, yset) for r in range(e)}
    if fixed is not None:
        D[fixed[0]] = [fixed[1]]
    empty = [r for r in range(e) if not D[r]]
    if empty:
        return 0, empty, []
    order = sorted(range(e), key=lambda r: len(D[r]))
    sols = []

    def rec(i, chosen):
        if len(sols) >= cap:
            return
        if i == len(order):
            sols.append(sorted(chosen))
            return
        for z in D[order[i]]:
            if all(sq_ok(z, w) for w in chosen):
                chosen.append(z)
                rec(i + 1, chosen)
                chosen.pop()
    rec(0, [])
    return len(sols), empty, sols[:3]


glob = {e: full_selections(e) for e in (165, 55, 33, 15)}
OUT['data']['R3_global_one_per_class_selections'] = jsonable(
    {e: {'count': c, 'empty_classes_first': emp[:12], 'first': s[:1]} for e, (c, emp, s) in glob.items()})
expect('R3g_global_backtracking_counts_e165_55_33_zero_e15_one',
       glob[165][0] == 0 and 2 in glob[165][1] and glob[55][0] == 0 and glob[33][0] == 0
       and glob[15][0] == 1 and glob[15][2][0] == S_CLAIM)
ydrop = {}
for drop in Y:
    yd = tuple(y for y in Y if y != drop)
    ydrop[drop] = {e: full_selections(e, yd, cap=1000)[0] for e in (55, 33, 15)}
OUT['data']['R3_drop_one_tail_selection_counts_capped_1000'] = jsonable(ydrop)
expect('R3h_negative_control_dropping_tail_0_or_14_frees_e55_e33',
       all(ydrop[y][55] > 0 and ydrop[y][33] > 0 for y in (0, 14)), counts=ydrop)
expect('R3i_negative_control_dropping_any_tail_breaks_e15_uniqueness', all(ydrop[y][15] > 1 for y in Y))

# R4 -- Section 7, Lemma 4 (e=15) at type level.
D15 = {r: dom(15, r) for r in range(15)}
sizes = [len(D15[r]) for r in range(15)]
expect('R4a_e15_initial_domain_sizes', sizes == [18, 9, 2, 2, 1, 8, 2, 9, 2, 8, 1, 2, 2, 9, 18], sizes=sizes)
extendable = {r: [z for z in D15[r] if full_selections(15, fixed=(r, z))[0] > 0] for r in range(15)}
expect('R4b_every_type_extending_to_a_consistent_selection_is_the_claimed_type',
       all(extendable[r] == [z for z in S_CLAIM if z % 15 == r] for r in range(15)), extendable=extendable)
pred = sorted(z for z in range(330) if (z % 2 == 1) == (z % 3 == 1) and z % 11 == G11[z % 5])
expect('R4c_claimed_S_equals_lemma4_prediction', pred == S_CLAIM, pred=pred)
expect('R4d_S_mod55_is_Y_and_S_pairwise_SQ',
       sorted({z % 55 for z in S_CLAIM}) == sorted(Y) and all(sq_ok(u, v) for u, v in combinations(S_CLAIM, 2)))
anchor_rows = {y: ((y % 3, y % 5), y % 2, y % 11) for y in Y}
expect('R4e_anchor_table', anchor_rows == {0: ((0, 0), 0, 0), 1: ((1, 1), 1, 1), 7: ((1, 2), 1, 7),
                                           13: ((1, 3), 1, 2), 14: ((2, 4), 0, 3)}, rows=anchor_rows)
cl = {(r % 3, r % 5): r for r in range(15)}
step1 = all(z % 2 == 1 for r in range(15) if r % 3 == 1 for z in D15[r])
step2 = (all(z % 2 == 1 and z % 11 == 0 for z in D15[cl[(1, 0)]])
         and all(z % 2 == 1 and z % 11 == 3 for z in D15[cl[(1, 4)]]))
refs = [z for z in D15[cl[(1, 0)]]] + [z for z in D15[cl[(1, 4)]]] + [1, 7, 13]
E = {r: [z for z in D15[r] if z % 2 == 0 and all(sq_ok(z, w) for w in refs)] for r in range(15) if r % 3 != 1}
step3 = all(len(E[r]) == 1 and E[r][0] % 11 == G11[r % 5] for r in E)
step4 = all(z % 2 == 0 for z in D15[cl[(0, 4)]] + D15[cl[(2, 0)]])
E20, E04 = E[cl[(2, 0)]], E[cl[(0, 4)]]
step5 = all(not all(sq_ok(z, w) for w in E20 + E04) for r in E for z in D15[r] if z % 2 == 1)
step6 = all(z % 11 == G11[r % 5] for r in range(15) if r % 3 == 1
            for z in D15[r] if all(sq_ok(z, w) for w in E[cl[(0, r % 5)]]))
expect('R4f_lemma4_steps_1_to_6_finite_content', step1 and step2 and step3 and step4 and step5 and step6,
       steps=[step1, step2, step3, step4, step5, step6], forced_even=E)


# R5 -- Lemmas 5 and 6: exact integer polynomial arithmetic.
def ptrim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pdivmod(a, m):
    a, m = list(a), ptrim(m)
    dm = len(m) - 1
    if m[-1] != 1:
        raise ValueError('divisor must be monic')
    if len(a) - 1 < dm:
        return [0], ptrim(a)
    q = [0] * (len(a) - dm)
    for i in range(len(a) - 1, dm - 1, -1):
        c = a[i]
        if c:
            q[i - dm] = c
            for j in range(dm + 1):
                a[i - dm + j] -= c * m[j]
    return ptrim(q), ptrim(a[:dm] if dm else [0])


def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return ptrim(out)


@lru_cache(None)
def phi(k):
    num = [-1] + [0] * (k - 1) + [1]
    for d in range(1, k):
        if k % d == 0:
            num, rem = pdivmod(num, list(phi(d)))
            if any(rem):
                raise ArithmeticError('cyclotomic division not exact')
    return tuple(num)


def fold(xs, k):
    f = [0] * k
    for x in xs:
        f[x % k] += 1
    return f


def phi_divides(xs, k):
    return not any(pdivmod(fold(xs, k), list(phi(k)))[1])


W = fold(S_CLAIM, 110)
W_formula = [(2 if z % 2 == 0 else 1) if z % 55 in Y else 0 for z in range(110)]
expect('R5a_fold_mod110_matches_lemma5_counts_b0', W == W_formula)
lhs = [0] * 110
for c0, e0 in ((2, 0), (1, 55)):
    for y in Y:
        lhs[(e0 + 56 * y) % 110] += c0
expect('R5b_identity_W_eq_(2+X^55)Y(X^56)_mod_X^110-1', lhs == W)
expect('R5c_crt_55_56', all((55 * (z % 2) + 56 * (z % 55)) % 110 == z for z in range(110)))
rem_zero = {m: not any(pdivmod(W, list(phi(m)))[1]) for m in (1, 2, 5, 10, 11, 22, 55, 110)}
expect('R5d_W_nonzero_mod_Phi_11_22_55_110_and_zero_exactly_at_5_10',
       [m for m, z in rem_zero.items() if z] == [5, 10], remainder_is_zero=rem_zero)
Ypoly = [1 if i in Y else 0 for i in range(15)]
expect('R5e_Y_nonzero_mod_Phi55_Phi11_and_degrees',
       any(pdivmod(Ypoly, list(phi(55)))[1]) and any(pdivmod(Ypoly, list(phi(11)))[1])
       and len(phi(55)) - 1 == 40 and len(phi(11)) - 1 == 10 and fold([i for i in Y], 11) == [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0])
expect('R5f_order_of_xi56_is_odd_part_of_order_xi',
       all(110 // gcd(56 * k, 110) == (110 // gcd(k, 110)) // gcd(2, 110 // gcd(k, 110)) for k in range(110)))
prod = [1]
for m in (11, 22, 55, 110):
    prod = pmul(prod, list(phi(m)))
expect('R5g_Phi11_Phi22_Phi55_Phi110_eq_sum_X^10k', prod == [1 if i % 10 == 0 else 0 for i in range(101)])
# xi = zeta_110^k gives xi^55 = (-1)^(55k mod 2), so 2 + xi^55 is 1 or 3.
expect('R5h_values_2_plus_xi55_in_1_3', all((2 + (-1) ** ((55 * k) % 2)) in (1, 3) for k in range(110)))

# R6 -- final certificate and its intended-reason negative controls.
X1 = [z for z in range(330) if z % 110 == 1]
p0 = [z for z in X1 if sp_ok(z, 0)]
p8 = [z for z in X1 if sp_ok(z, 8)]
expect('R6a_final_certificate', X1 == [1, 111, 221] and p0 == [111] and p8 == [221]
       and 111 % 3 == 0 and 221 % 3 == 2 and 11 % 10 == 1, pass_vs_0=p0, pass_vs_8=p8)
neg = {'drop8': [z for z in X1 if all(sp_ok(z, a) for a in (0, 3, 11))],
       'drop0': [z for z in X1 if all(sp_ok(z, a) for a in (3, 8, 11))],
       'drop3': [z for z in X1 if all(sp_ok(z, a) for a in (0, 8, 11))]}
expect('R6b_negative_controls_final_step_needs_both_0_and_8',
       neg['drop8'] == [111] and neg['drop0'] == [221] and neg['drop3'] == [], survivors=neg)

# R7 -- recompute the candidate's section-8 bounded diagnostics (non-load-bearing).
diag = {}
for t in range(1, 7):
    n = 165 * 2 ** t
    GY, GA = nz_div(Y, n), nz_div(A, n)
    Ph = [x for x in range(n) if all(x == a or gcd((x - a) % n, n) not in GY for a in A)]
    Qt = [x for x in range(n) if all(x == y or gcd((x - y) % n, n) not in GA for y in Y)]
    inside = all({x % 330 for x in Qt if x % e == r} <= set(dom(e, r))
                 for e, rs in ((55, (3, 24, 25)), (33, (22, 3, 4, 15)), (15, range(15))) for r in rs)
    diag[t] = {'n': n, 'P_screen': len(Ph), 'Q_screen': len(Qt),
               'P_screen_avoids_lemma3_classes': not any(x % 15 == 4 or x % 33 == 1 or x % 55 == 2 for x in Ph),
               'Q_screen_avoids_2_mod_165': not any(x % 165 == 2 for x in Qt),
               'Q_screen_types_inside_domains': inside,
               'anchors_A_in_P_screen': all(a in Ph for a in A), 'anchors_Y_in_Q_screen': all(y in Qt for y in Y)}
OUT['data']['R7_section8_diagnostics'] = jsonable(diag)
expect('R7a_screen_sizes_match_candidate',
       [diag[t]['P_screen'] for t in diag] == [6, 42, 112, 224, 448, 896]
       and [diag[t]['Q_screen'] for t in diag] == [47, 118, 286, 658, 1316, 2632])
expect('R7b_screen_properties_t1_to_t6', all(d['P_screen_avoids_lemma3_classes'] and d['Q_screen_avoids_2_mod_165']
                                              and d['Q_screen_types_inside_domains'] for d in diag.values()))
expect('R7c_t1_anchor_screen_failure_matches_sands_collision',
       not diag[1]['anchors_A_in_P_screen'] and all(diag[t]['anchors_A_in_P_screen'] for t in range(2, 7)))


# R8/R9 -- exact-cover countercontrols (Algorithm X, MRV), all tilings verified.
class Cap(Exception):
    pass


def cover(Q, n, forced, node_cap=5_000_000, time_cap=120.0):
    rows = {p: [(p + q) % n for q in Q] for p in range(n)}
    X = {c: set() for c in range(n)}
    for p, cols in rows.items():
        for c in cols:
            X[c].add(p)

    def select(r):
        saved = []
        for j in rows[r]:
            for i in X[j]:
                for k in rows[i]:
                    if k != j:
                        X[k].remove(i)
            saved.append(X.pop(j))
        return saved

    def deselect(r, saved):
        for j in reversed(rows[r]):
            X[j] = saved.pop()
            for i in X[j]:
                for k in rows[i]:
                    if k != j:
                        X[k].add(i)
    chosen = []
    for p in forced:
        if any(c not in X for c in rows[p]):
            return {'status': 'forced_overlap', 'nodes': 0, 'P': None}
        select(p)
        chosen.append(p)
    st = {'nodes': 0, 'P': None}
    t0 = time.time()

    def rec():
        st['nodes'] += 1
        if st['nodes'] > node_cap or (st['nodes'] % 4096 == 0 and time.time() - t0 > time_cap):
            raise Cap()
        if not X:
            st['P'] = sorted(chosen)
            return True
        c = min(X, key=lambda c: len(X[c]))
        for r in list(X[c]):
            saved = select(r)
            chosen.append(r)
            if rec():
                return True
            chosen.pop()
            deselect(r, saved)
        return False
    try:
        found = rec()
    except Cap:
        return {'status': 'cap', 'nodes': st['nodes'], 'P': None}
    return {'status': 'found' if found else 'none', 'nodes': st['nodes'], 'P': st['P']}


def is_tiling(P, Q, n):
    return sorted((p + q) % n for p in P for q in Q) == list(range(n))


def prime_powers(n):
    out, m, p = [], n, 2
    while p * p <= m:
        e = 0
        while m % p == 0:
            m //= p
            e += 1
        out += [(p, p ** k) for k in range(1, e + 1)]
        p += 1
    if m > 1:
        out.append((m, m))
    return out


def t2_holds(xs, n):
    sa = [(p, s) for (p, s) in prime_powers(n) if phi_divides(xs, s)]
    byp = {}
    for p, s in sa:
        byp.setdefault(p, []).append(s)
    for k in range(2, len(byp) + 1):
        for ps in combinations(sorted(byp), k):
            for ch in product(*[byp[p] for p in ps]):
                mm = 1
                for s in ch:
                    mm *= s
                if not phi_divides(xs, mm):
                    return False, sorted(s for _, s in sa)
    return True, sorted(s for _, s in sa)


def uniform_mod_odd_part(xs):
    d = len(xs)
    while d % 2 == 0:
        d //= 2
    f = fold(xs, d)
    return all(v == len(xs) // d for v in f)


def tilepair_checks(P, Q, n):
    f110 = fold(P, 110)
    return {'tiling': is_tiling(P, Q, n),
            'lemma6_P_fold_mod110_10_periodic': all(f110[z] == f110[z % 10] for z in range(110)),
            'sands_div_exclusion': not (nz_div(P, n) & nz_div(Q, n)),
            't2_P': t2_holds(P, n)[0], 't2_Q': t2_holds(Q, n)[0],
            'uniform_P': uniform_mod_odd_part(P), 'uniform_Q': uniform_mod_odd_part(Q),
            'tijdeman_P': all(len({r * p % n for p in P}) == len(P) and is_tiling([r * p % n for p in P], Q, n)
                              for r in (3, 5, 7, 9, 13) if gcd(r, len(P)) == 1),
            'tijdeman_Q': all(len({r * q % n for q in Q}) == len(Q) and is_tiling(P, [r * q % n for q in Q], n)
                              for r in (2, 4, 8, 11, 22) if gcd(r, len(Q)) == 1)}


SR = {z % 15: z for z in S_CLAIM}
NONANCHOR = [r for r in range(15) if SR[r] not in Y]

# R8 -- the candidate's n=2640 Q-side control set.
QS = [0, 1, 7, 13, 14, 288, 289, 385, 1376, 1712, 1760, 2048, 2256, 2544, 2592]
n = 2640
GA2640 = nz_div(A, n)
mod16_ok = all((x % 16 == x) if x in Y else (x % 16 == x % 2) for x in QS)
expect('R8a_2640_control_set_properties',
       GA2640 == {3, 5, 8, 11} and set(Y) <= set(QS) and sorted(x % 15 for x in QS) == list(range(15))
       and sorted(x % 330 for x in QS) == S_CLAIM and mod16_ok
       and all(gcd((u - v) % n, n) not in GA2640 for u, v in combinations(QS, 2)), GA=GA2640)
c8a = cover(QS, n, list(A))
c8z = cover(QS, n, [0])
expect('R8b_2640_control_set_has_no_complement_containing_A', c8a['status'] == 'none', nodes=c8a['nodes'])
expect('R8c_positive_2640_control_set_is_an_actual_tile', c8z['status'] == 'found' and is_tiling(c8z['P'], QS, n),
       nodes=c8z['nodes'], P_size=len(c8z['P'] or []))

# R9a -- n=330 (t=1): Q forced to S.
c330a, c330z = cover(S_CLAIM, 330, list(A)), cover(S_CLAIM, 330, [0])
expect('R9a_n330_no_anchored_complement_positive_unanchored_found',
       c330a['status'] == 'none' and c330z['status'] == 'found' and is_tiling(c330z['P'], S_CLAIM, 330))

# R9b -- n=660 (t=2), b=0: all 2^10 Lemma-4 tail sets; several forced head sets.
VARIANTS = {'A': list(A), '0': [0], '0,3': [0, 3], '0,5': [0, 5], '0,8': [0, 8], '0,11': [0, 11],
            '0,3,8': [0, 3, 8], '0,3,11': [0, 3, 11], '0,8,11': [0, 8, 11], '3,8,11': [3, 8, 11]}
EXPECTED_FOUND = {'0': 1024, '0,3': 1024, '0,5': 1024}
r9b = {}
pairs660 = []
for name, forced in VARIANTS.items():
    st = {'found': 0, 'none': 0, 'forced_overlap': 0, 'cap': 0}
    mx = 0
    for bits in product((0, 1), repeat=10):
        Q = sorted(list(Y) + [SR[r] + 330 * b for r, b in zip(NONANCHOR, bits)])
        res = cover(Q, 660, forced)
        st[res['status']] += 1
        mx = max(mx, res['nodes'])
        if res['status'] == 'found':
            if not is_tiling(res['P'], Q, 660):
                st['found'] = -10 ** 9
            if name == '0':
                pairs660.append((res['P'], Q))
    r9b[name] = {'counts': st, 'max_nodes': mx}
OUT['data']['R9b_n660_b0_all_1024'] = jsonable(r9b)
expect('R9b1_n660_b0_no_complement_contains_A', r9b['A']['counts'] == {'found': 0, 'none': 1024, 'forced_overlap': 0, 'cap': 0})
expect('R9b2_positive_n660_b0_every_lemma4_tail_set_is_a_tile_and_0_3_0_5_extendable',
       all(r9b[k]['counts']['found'] == v for k, v in EXPECTED_FOUND.items()))
expect('R9b3_all_other_variants_none_and_no_caps',
       all(r9b[k]['counts']['none'] == 1024 for k in VARIANTS if k not in EXPECTED_FOUND)
       and all(r9b[k]['counts']['cap'] == 0 for k in VARIANTS))
agg = {}
for P, Q in pairs660:
    for key, val in tilepair_checks(P, Q, 660).items():
        agg[key] = agg.get(key, 0) + (1 if val else 0)
expect('R9b4_positive_found_tilings_satisfy_lemma6_sands_t2_uniformity_tijdeman',
       len(pairs660) == 1024 and all(v == 1024 for v in agg.values()), counts=agg)

# R9c -- n=660, b=1: the unique Lemma-4 tail set S + {0,330}.
QB1 = sorted(S_CLAIM + [z + 330 for z in S_CLAIM])
c1a, c1z = cover(QB1, 660, list(A)), cover(QB1, 660, [0])
expect('R9c_n660_b1_no_anchored_complement_positive_unanchored_found',
       c1a['status'] == 'none' and c1z['status'] == 'found' and is_tiling(c1z['P'], QB1, 660))

# R9d -- bounded seeded random samples, t=3 (n=1320) and t=4 (n=2640); b<=2 only.
rng = random.Random(20261029176)


def sample_tail(t, b):
    lifts = 2 ** (t - 1)
    Q = []
    for r in range(15):
        base = SR[r]
        ks = ([0] + rng.sample(range(1, lifts), 2 ** b - 1)) if base in Y else rng.sample(range(lifts), 2 ** b)
        Q += [base + 330 * k for k in ks]
    return sorted(Q)


r9d = {}
for t, plan in ((3, ((0, 32), (1, 8), (2, 4))), (4, ((0, 8), (1, 4), (2, 2)))):
    n = 165 * 2 ** t
    for b, count in plan:
        st = {'A': {'found': 0, 'none': 0, 'forced_overlap': 0, 'cap': 0},
              '0': {'found': 0, 'none': 0, 'forced_overlap': 0, 'cap': 0}}
        ok_found = True
        for _ in range(count):
            Q = sample_tail(t, b)
            assert len(Q) == 15 * 2 ** b == len(set(Q)) and set(Y) <= set(Q)
            for name, forced in (('A', list(A)), ('0', [0])):
                res = cover(Q, n, forced, node_cap=2_000_000, time_cap=60.0)
                st[name][res['status']] += 1
                if res['status'] == 'found':
                    ok_found = ok_found and is_tiling(res['P'], Q, n)
                    if name == '0':
                        f110 = fold(res['P'], 110)
                        ok_found = ok_found and all(f110[z] == f110[z % 10] for z in range(110))
        r9d['t%d_b%d' % (t, b)] = {'samples': count, 'counts': st, 'found_tilings_verified_and_lemma6': ok_found}
OUT['data']['R9d_random_samples'] = jsonable(r9d)
expect('R9d_samples_no_complement_contains_A_and_found_ones_verified',
       all(v['counts']['A']['found'] == 0 and v['counts']['A']['cap'] == 0 and v['found_tilings_verified_and_lemma6']
           for v in r9d.values()))

OUT['meta']['elapsed_s'] = round(time.time() - T_START, 3)
OUT['meta']['failed'] = FAILED
OUT['result'] = 'ALL_EXPECTATIONS_OBSERVED' if not FAILED else 'EXPECTATION_FAILURE'
with open(OUTPATH, 'w') as fh:
    json.dump(OUT, fh, indent=1, sort_keys=True)
    fh.write('\n')
print(json.dumps({'result': OUT['result'], 'failed': FAILED, 'n_checks': len(OUT['checks']),
                  'elapsed_s': OUT['meta']['elapsed_s']}, sort_keys=True))
sys.exit(0 if not FAILED else 1)
