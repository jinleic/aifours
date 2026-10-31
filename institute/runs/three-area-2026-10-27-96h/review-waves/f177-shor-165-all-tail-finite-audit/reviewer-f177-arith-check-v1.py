#!/usr/bin/env python3
"""reviewer-f177-arith-check-v1.py -- independent finite-arithmetic audit.

Review wave : f177-shor-165-all-tail-finite-audit
Reviewer    : ReviewF177ShorArithmetic (same-harness; not human, not an
              independent model family, not formal/kernel, not novelty)
Candidate   : frontier-20261029-165-family-all-q-anchored-border-no-go-v1.md
              SHA-256 20169ac9e398d9d1ef37d263f9b51d0f9168c095c3e3eb21ade47572822d39c6

Written from the candidate's prose. The author checker was read (manifest
read order) but is never imported, executed or opened by this script.
Standard library only; exact integers; finite exhaustive loops.

Representation. A residue x mod 330 is handled through its CRT coordinates
T = (x mod 2, x mod 3, x mod 5, x mod 11). For two types T, U the odd prime
p in {3,5,11} divides x - x' iff T and U agree in the p-coordinate, and the
difference is odd iff the parity coordinates differ. Sands consequences
(SQ)/(SP) are evaluated from these shared coordinates; gcd- and
valuation-based cross-checks are separate sections.

Usage: python3 -B reviewer-f177-arith-check-v1.py [--out FILE]
FILE is created exclusively; an existing FILE is never overwritten.
Exit status 0 iff every registered check holds.
"""
import argparse
import json
import math
import sys
from collections import deque
from itertools import combinations, product

# ---------------------------------------------------------------------------
# 0. Data transcribed from the candidate prose (section numbers of the prose).
# ---------------------------------------------------------------------------
HEADS = (0, 3, 8, 11)                       # §1 A (old heads, in P)
TAILS = (0, 1, 7, 13, 14)                   # §1 Y (old tails, in Q)
ODD_PRIMES = (3, 5, 11)
COORD = {2: 0, 3: 1, 5: 2, 11: 3}
G_OF_R5 = (0, 1, 7, 2, 3)                   # §7 g(0..4)
ANCHOR_TABLE_E15 = {                        # §7 table: anchor -> ((r3, r5), parity, r11)
    0: ((0, 0), 0, 0), 1: ((1, 1), 1, 1), 7: ((1, 2), 1, 7),
    13: ((1, 3), 1, 2), 14: ((2, 4), 0, 3)}
LEMMA3_ROWS = {                             # §5 table: (m, r): ((x-0, x-8), (x-3, x-11), third prime)
    (15, 4): ((4, 11), (1, 8), 11),
    (33, 1): ((1, 26), (31, 23), 5),
    (55, 2): ((2, 49), (54, 46), 3)}
CLAIM_E55_STATES = {3: [(1, 2)], 24: [(1, 2)], 25: [(0, 0), (0, 2)]}            # §8 item 2
CLAIM_E33_STATES = {22: [(1, 0)], 3: [(0, 0), (0, 4)], 4: [(1, 1), (1, 2), (1, 3)],
                    15: [(0, 0), (0, 4), (1, 0)]}                                 # §8 item 2
CLAIM_E15_SIZES = [18, 9, 2, 2, 1, 8, 2, 9, 2, 8, 1, 2, 2, 9, 18]                 # §8 item 3
CLAIM_E15_TYPES = [0, 1, 7, 13, 14, 55, 56, 62, 68, 110, 234, 276, 282, 288, 289]  # §8 item 3
CLAIM_SCREENS = {1: (6, 47), 2: (42, 118), 3: (112, 286), 4: (224, 658),
                 5: (448, 1316), 6: (896, 2632)}                                  # §8 item 6
CLAIM_CONTROL_2640 = (0, 1, 7, 13, 14, 288, 289, 385, 1376, 1712, 1760, 2048,
                      2256, 2544, 2592)                                           # §9
CLAIM_GA_2640 = [3, 5, 8, 11]                                                     # §9

# §6 bullets: (e, f, subject class r, subject parity, comparator, bracket, k, relation, residue)
# comparator = ('anchor', a) or ('elem', class s, parity, residue mod f)
BULLETS = [
    (55, 3, 3, 0, ('anchor', 1), 2, 0, 'ne', 1),
    (55, 3, 3, 0, ('anchor', 13), -10, 1, 'eq', 1),
    (55, 3, 3, 1, ('anchor', 0), 3, 0, 'ne', 0),
    (55, 3, 3, 1, ('anchor', 14), -11, 1, 'eq', 2),
    (55, 3, 24, 0, ('anchor', 1), 23, 0, 'ne', 1),
    (55, 3, 24, 0, ('anchor', 13), 11, 1, 'eq', 1),
    (55, 3, 24, 1, ('anchor', 0), 24, 0, 'ne', 0),
    (55, 3, 24, 1, ('anchor', 14), 10, 1, 'eq', 2),
    (55, 3, 25, 1, ('anchor', 0), 25, 1, 'eq', 0),
    (55, 3, 25, 1, ('anchor', 14), 11, 1, 'eq', 2),
    (55, 3, 25, 0, ('anchor', 1), 24, 0, 'ne', 1),
    (55, 3, 25, 0, ('anchor', 7), 18, 0, 'ne', 1),
    (55, 3, 25, 0, ('anchor', 13), 12, 0, 'ne', 1),
    (55, 3, 25, 0, ('elem', 3, 1, 2), 22, 1, 'eq', 2),
    (55, 3, 25, 0, ('elem', 24, 1, 2), 1, 0, 'ne', 2),
    (33, 5, 22, 0, ('anchor', 1), 21, 1, 'eq', 1),
    (33, 5, 22, 0, ('anchor', 7), 15, 1, 'eq', 2),
    (33, 5, 22, 1, ('anchor', 0), 22, 1, 'eq', 0),
    (33, 5, 3, 1, ('anchor', 0), 3, 1, 'eq', 0),
    (33, 5, 3, 1, ('anchor', 14), -11, 1, 'eq', 4),
    (33, 5, 3, 0, ('anchor', 1), 2, 0, 'ne', 1),
    (33, 5, 3, 0, ('anchor', 7), -4, 0, 'ne', 2),
    (33, 5, 3, 0, ('anchor', 13), -10, 0, 'ne', 3),
    (33, 5, 4, 0, ('anchor', 1), 3, 1, 'eq', 1),
    (33, 5, 4, 0, ('anchor', 7), -3, 1, 'eq', 2),
    (33, 5, 4, 1, ('anchor', 0), 4, 0, 'ne', 0),
    (33, 5, 4, 1, ('anchor', 14), -10, 0, 'ne', 4),
    (33, 5, 15, 1, ('anchor', 0), 15, 1, 'eq', 0),
    (33, 5, 15, 0, ('anchor', 1), 14, 0, 'ne', 1),
    (33, 5, 15, 0, ('anchor', 7), 8, 0, 'ne', 2),
    (33, 5, 15, 0, ('anchor', 13), 2, 0, 'ne', 3),
    (33, 5, 3, 0, ('elem', 22, 1, 0), -19, 0, 'ne', 0),
    (33, 5, 15, 1, ('elem', 3, 0, 4), 12, 1, 'eq', 4),
    (33, 5, 15, 0, ('elem', 22, 1, 0), -7, 0, 'ne', 0),
    (33, 5, 4, 1, ('elem', 15, 0, 4), 11, 1, 'eq', 4),
]

CHECKS = []


def check(cid, claim, ok, observed=None, expected=None):
    CHECKS.append({'id': cid, 'claim': claim, 'ok': bool(ok),
                   'observed': observed, 'expected': expected})
    return bool(ok)


# ---------------------------------------------------------------------------
# 1. Arithmetic primitives (own implementations).
# ---------------------------------------------------------------------------
def inv_mod(a, m):
    a %= m
    r0, r1, s0, s1 = m, a, 0, 1
    while r1:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if r0 != 1:
        raise ValueError('not invertible')
    return s0 % m


def crt(pairs):
    x, M = 0, 1
    for r, m in pairs:
        k = ((r - x) * inv_mod(M, m)) % m
        x += M * k
        M *= m
    return x % M, M


def typ(x):
    return (x % 2, x % 3, x % 5, x % 11)


TYPES = [(a, b, c, d) for a in range(2) for b in range(3) for c in range(5) for d in range(11)]
RES = {T: crt([(T[0], 2), (T[1], 3), (T[2], 5), (T[3], 11)])[0] for T in TYPES}


def shared(T, U):
    return tuple(p for p in ODD_PRIMES if T[COORD[p]] == U[COORD[p]])


def g165(T, U):
    g = 1
    for p in shared(T, U):
        g *= p
    return g


def gcd_n(u, t):
    """gcd(u, 165*2^t) from p-adic valuations (independent of math.gcd)."""
    n = 165 << t
    u %= n
    if u == 0:
        return n
    g = 1
    for p in ODD_PRIMES:
        if u % p == 0:
            g *= p
    e = 0
    while e < t and u % 2 == 0:
        u //= 2
        e += 1
    return g << e


def odd_gcd_set(anchors):
    out = set()
    for a, b in combinations(anchors, 2):
        if (a - b) % 2:
            g = 1
            for p in ODD_PRIMES:
                if (a - b) % p == 0:
                    g *= p
            out.add(g)
    return frozenset(out)


class Rules:
    def __init__(self, label, heads=HEADS, tails=TAILS, qban=None, spset=None,
                 parity_required=True):
        self.label = label
        self.heads = tuple(heads)
        self.tails = tuple(tails)
        self.qban = frozenset(qban) if qban is not None else odd_gcd_set(self.heads)
        self.spset = frozenset(spset) if spset is not None else odd_gcd_set(self.tails)
        self.parity_required = parity_required

    def _conf(self, T, U, banned):
        if self.parity_required and T[0] == U[0]:
            return False
        return g165(T, U) in banned

    def qc(self, T, U):
        return self._conf(T, U, self.qban)

    def pc(self, T, U):
        return self._conf(T, U, self.spset)

    def describe(self):
        return {'label': self.label, 'heads': list(self.heads), 'tails': list(self.tails),
                'qban': sorted(self.qban), 'spset': sorted(self.spset),
                'parity_required': self.parity_required}


def class_types(e, r):
    return [T for T in TYPES if RES[T] % e == r]


def qdomain(R, e, r):
    return [T for T in class_types(e, r) if not any(R.qc(T, typ(y)) for y in R.tails)]


def ac3(D0, conflict):
    D = {r: list(v) for r, v in D0.items()}
    keys = sorted(D)
    queue = deque((r, s) for r in keys for s in keys if r != s)
    log = []
    while queue:
        r, s = queue.popleft()
        keep = []
        for z in D[r]:
            if any(not conflict(z, w) for w in D[s]):
                keep.append(z)
            else:
                log.append((r, RES[z], s))
        if len(keep) != len(D[r]):
            D[r] = keep
            for q in keys:
                if q != r:
                    queue.append((q, r))
    return D, log


def replay(D0, log, conflict):
    D = {r: list(v) for r, v in D0.items()}
    for r, x, s in log:
        T = typ(x)
        if T not in D[r]:
            return False, ('missing', r, x, s)
        if not all(conflict(T, w) for w in D[s]):
            return False, ('unjustified', r, x, s)
        D[r].remove(T)
    return True, D


def transversals(D, compat, max_nodes=300000, max_solutions=1000):
    order = sorted(D, key=lambda r: (len(D[r]), r))
    sols, chosen = [], []
    state = {'nodes': 0, 'capped': False}

    def rec(i):
        if state['capped']:
            return
        if i == len(order):
            sols.append(tuple(RES[z] for z in chosen))
            if len(sols) >= max_solutions:
                state['capped'] = True
            return
        for z in D[order[i]]:
            state['nodes'] += 1
            if state['nodes'] > max_nodes:
                state['capped'] = True
                return
            if all(compat(z, w) for w in chosen):
                chosen.append(z)
                rec(i + 1)
                chosen.pop()
    rec(0)
    return {'count': len(sols), 'capped': state['capped'], 'nodes': state['nodes'],
            'solutions_sample': [sorted(s) for s in sols[:3]]}


# ---------------------------------------------------------------------------
# 2. Polynomial and finite-field helpers (own implementations).
# ---------------------------------------------------------------------------
def p_trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def p_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return p_trim(out)


def p_divmod_monic(a, m):
    m = p_trim(m)
    if m[-1] != 1:
        raise ValueError('divisor not monic')
    a = list(a)
    dm = len(m) - 1
    if len(a) - 1 < dm:
        return [0], p_trim(a)
    q = [0] * (len(a) - dm)
    for k in range(len(a) - 1 - dm, -1, -1):
        c = a[k + dm]
        q[k] = c
        if c:
            for j in range(dm + 1):
                a[k + j] -= c * m[j]
    rem = p_trim(a[:dm]) if dm > 0 else [0]
    return p_trim(q), rem


def mobius(k):
    res, d = 1, 2
    while d * d <= k:
        if k % d == 0:
            k //= d
            if k % d == 0:
                return 0
            res = -res
        d += 1
    if k > 1:
        res = -res
    return res


def cyclotomic(m):
    """Phi_m from the Moebius product of (X^d - 1); exact division checked."""
    num, den = [1], [1]
    for d in range(1, m + 1):
        if m % d == 0:
            mu = mobius(m // d)
            f = [-1] + [0] * (d - 1) + [1]
            if mu == 1:
                num = p_mul(num, f)
            elif mu == -1:
                den = p_mul(den, f)
    q, r = p_divmod_monic(num, den)
    if r != [0]:
        raise ArithmeticError('Moebius quotient not exact')
    return q


def euler_phi(m):
    return sum(1 for k in range(1, m + 1) if math.gcd(k, m) == 1)


def is_prime(p):
    if p < 2:
        return False
    i = 2
    while i * i <= p:
        if p % i == 0:
            return False
        i += 1
    return True


def prime_factors(n):
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def primitive_root(p):
    fs = prime_factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fs):
            return g
    raise ValueError


def eval_mod(coeffs, x, p):
    acc = 0
    for c in reversed(coeffs):
        acc = (acc * x + c) % p
    return acc


def fp_values_at_primitive_roots(poly, m, p, g):
    w = pow(g, (p - 1) // m, p)
    return [eval_mod(poly, pow(w, k, p), p) for k in range(1, m + 1) if math.gcd(k, m) == 1]


# ---------------------------------------------------------------------------
# 3. Sections.
# ---------------------------------------------------------------------------
def sec_types():
    bij = sorted(RES.values()) == list(range(330)) and all(typ(RES[T]) == T for T in TYPES)
    check('types.crt_bijection', 'CRT coordinates (mod 2,3,5,11) biject with Z_330', bij)
    ok = all(g165(T, U) == math.gcd(RES[T] - RES[U], 165) and
             ((T[0] != U[0]) == ((RES[T] - RES[U]) % 2 == 1)) for T in TYPES for U in TYPES)
    check('types.shared_coordinate_rule', 'shared odd coordinates == gcd(x-x\',165); parity coordinate == parity of difference (all 330^2 pairs)', ok)
    return {'types': len(TYPES), 'bijection': bij, 'pairs_checked': len(TYPES) ** 2}


def sec_gcd_sets(tmax=12):
    out = {}
    all_ok = True
    for t in range(1, tmax + 1):
        n = 165 << t
        GA = sorted({gcd_n(a - b, t) for a, b in combinations(HEADS, 2)})
        GY = sorted({gcd_n(a - b, t) for a, b in combinations(TAILS, 2)})
        GA_ref = sorted({math.gcd(a - b, n) for a, b in combinations(HEADS, 2)})
        GY_ref = sorted({math.gcd(a - b, n) for a, b in combinations(TAILS, 2)})
        all_ok &= GA == GA_ref and GY == GY_ref
        out[t] = {'n': n, 'G_A': GA, 'G_Y': GY,
                  'odd_G_A': [g for g in GA if g % 2], 'odd_G_Y': [g for g in GY if g % 2],
                  'G_A_cap_G_Y': sorted(set(GA) & set(GY))}
    check('gcd.valuation_vs_math_gcd', 'valuation gcd equals math.gcd on anchor differences, t=1..%d' % tmax, all_ok)
    check('gcd.odd_parts_t_independent', 'odd part of G_A(n) is {3,5,11} and of G_Y(n) is {1} for t=1..%d' % tmax,
          all(v['odd_G_A'] == [3, 5, 11] and v['odd_G_Y'] == [1] for v in out.values()))
    check('gcd.anchor_odd_sets', 'odd-difference gcd sets from the anchors: heads {3,5,11}, tails {1}',
          sorted(odd_gcd_set(HEADS)) == [3, 5, 11] and sorted(odd_gcd_set(TAILS)) == [1],
          [sorted(odd_gcd_set(HEADS)), sorted(odd_gcd_set(TAILS))])
    inter = {t: out[t]['G_A_cap_G_Y'] for t in out}
    check('gcd.t1_endpoint_direct_sands_collision',
          'reviewer observation: G_A(330) and G_Y(330) share gcd 2 (gcd(8,330)=gcd(14,330)=2); disjoint for t>=2',
          inter[1] == [2] and all(inter[t] == [] for t in out if t >= 2), inter)
    check('gcd.anchors_distinct', 'anchors are distinct residues mod n for n>=330',
          len(set(HEADS)) == 4 and len(set(TAILS)) == 5 and max(HEADS + TAILS) < 330)
    return out


def sec_lemma1(tmax=10):
    out = {}
    ok = True
    for t in range(1, tmax + 1):
        n = 165 << t
        bad = 0
        for u in range(1, n, 2):
            a = gcd_n(u, t)
            b = math.gcd(u, n)
            c = math.gcd(u, 165)
            d = 1
            for p in ODD_PRIMES:
                if u % p == 0:
                    d *= p
            if not (a == b == c == d):
                bad += 1
        out[t] = {'n': n, 'odd_u_checked': n // 2, 'mismatches': bad}
        ok &= bad == 0
    check('lemma1.bounded', 'Lemma 1: gcd(u,n)=gcd(u,165) for every odd u mod n, t=1..%d (bounded test; all-t is the one-line written proof)' % tmax, ok)
    # t = 0 is outside the reduction: parity is not a function on Z_165.
    t0 = {'n': 165, 'residue_1_equals_166': (166 - 1) % 165 == 0, 'integer_parities': [1 % 2, 166 % 2]}
    check('lemma1.t0_parity_ill_defined', 't=0 excluded: 1 and 166 are the same residue mod 165 but have different integer parity',
          t0['residue_1_equals_166'] and t0['integer_parities'] == [1, 0], t0)
    return {'per_t': out, 't0': t0}


def sec_rule_R(R):
    out = {}
    ok = True
    for e, fixed, f in ((55, (5, 11), 3), (33, (3, 11), 5), (15, (3, 5), 11)):
        pairs = mism = kmax = 0
        for T in TYPES:
            for U in TYPES:
                if T[0] == U[0] or RES[T] % e == RES[U] % e:
                    continue
                pairs += 1
                k = sum(1 for p in fixed if T[COORD[p]] == U[COORD[p]])
                kmax = max(kmax, k)
                same_f = T[COORD[f]] == U[COORD[f]]
                rule = (k == 0 and same_f) or (k == 1 and not same_f) or k >= 2
                if rule != R.qc(T, U):
                    mism += 1
        out[e] = {'opposite_parity_distinct_class_pairs': pairs, 'mismatches': mism, 'max_k': kmax}
        ok &= mism == 0 and kmax <= 1
    check('ruleR.equivalence', 'rule (R) (and the e=15 shared-coordinate form) is equivalent to (SQ) on every opposite-parity distinct-class type pair; k<2', ok, out)
    return out


def lemma3_status(R):
    out = {}
    for (m, r) in LEMMA3_ROWS:
        ts = class_types(m, r)
        kill = {RES[T]: [a for a in R.heads if R.pc(T, typ(a))] for T in ts}
        surv = sorted(x for x, k in kill.items() if not k)
        out['%d mod %d' % (r, m)] = {
            'types': len(ts), 'even': sum(1 for T in ts if T[0] == 0),
            'odd': sum(1 for T in ts if T[0] == 1), 'survivors': surv,
            'survivor_parities': sorted({x % 2 for x in surv}),
            'status': 'SAT' if surv else 'UNSAT', 'killers': kill}
    return out


def sec_lemma3(R):
    rows = {}
    for (m, r), (odd_d, even_d, third) in LEMMA3_ROWS.items():
        two = [p for p in ODD_PRIMES if m % p == 0]
        q = [p for p in ODD_PRIMES if m % p][0]
        c_odd = ((r - 0) % m, (r - 8) % m)
        c_even = ((r - 3) % m, (r - 11) % m)
        ok = (c_odd == odd_d and c_even == even_d and q == third and
              all(d % p for d in c_odd + c_even for p in two) and 8 % q != 0 and
              all(a % m != r for a in HEADS))
        rows['%d mod %d' % (r, m)] = {'computed_odd': c_odd, 'computed_even': c_even,
                                      'third_prime': q, 'row_ok': ok}
    check('lemma3.prose_rows', '§5 table rows: differences, determined primes, third prime and 8 not divisible by it',
          all(v['row_ok'] for v in rows.values()), rows)
    st = lemma3_status(R)
    check('lemma3.exhaustive', 'Lemma 3: every type mod 330 in 4 mod 15, 1 mod 33, 2 mod 55 fails (SP) against A',
          all(v['status'] == 'UNSAT' for v in st.values()),
          {k: (v['types'], v['status']) for k, v in st.items()})
    check('lemma3.coverage', 'coverage: 22, 10, 6 types (both parities) enumerated',
          [v['types'] for v in st.values()] == [22, 10, 6] and
          all(v['even'] == v['odd'] for v in st.values()))
    pa = [(a, b) for a, b in combinations(HEADS, 2) if R.pc(typ(a), typ(b))]
    qa = [(a, b) for a, b in combinations(TAILS, 2) if R.qc(typ(a), typ(b))]
    check('anchors.self_consistent', 'old heads pairwise (SP)-consistent and old tails pairwise (SQ)-consistent', not pa and not qa, [pa, qa])
    # d in {1,3,5,11}
    divs = [d for d in range(1, 166) if 165 % d == 0]
    excl = {}
    for d in divs:
        bad = [m for (m, r) in LEMMA3_ROWS if d % m == 0]
        excl[d] = bad
    allowed = [d for d in divs if not excl[d]]
    check('lemma3.d_values', 'odd parts d of |P| with two of 3,5,11 dividing d contain an excluded modulus; remaining d = 1,3,5,11 and e = 165,55,33,15',
          allowed == [1, 3, 5, 11] and all(excl[d] for d in divs if sum(1 for p in ODD_PRIMES if d % p == 0) >= 2),
          {'allowed_d': allowed, 'excluded_by_modulus': {d: excl[d] for d in divs if excl[d]}})
    t2 = all(sum(1 for x in (P, (165 << t) // P) if x % p == 0) == 1
             for t in range(1, 7) for P in range(1, (165 << t) + 1) if (165 << t) % P == 0 for p in ODD_PRIMES)
    check('t2.hypothesis_arithmetic', 'for every factorization |P||Q|=165*2^t (t=1..6) each of 3,5,11 divides exactly one cardinality', t2)
    return {'rows': rows, 'status': {k: {kk: vv for kk, vv in v.items() if kk != 'killers'} for k, v in st.items()},
            'killers': {k: v['killers'] for k, v in st.items()}}


def d1_status(R, representative_only=False):
    ts = [typ(2)] if representative_only else class_types(165, 2)
    kill = {RES[T]: [(y, g165(T, typ(y))) for y in R.tails if R.qc(T, typ(y))] for T in ts}
    surv = sorted(x for x, k in kill.items() if not k)
    return {'types': sorted(kill), 'killers': kill, 'survivors': surv,
            'status': 'SAT' if surv else 'UNSAT'}


def sec_d1(R):
    st = d1_status(R)
    check('d1.class2_empty', 'd=1: both lifts 2 (even) and 167 (odd) of 2 mod 165 fail (SQ) against Y', st['status'] == 'UNSAT', st)
    check('d1.coverage', 'class 2 mod 165 lifts to exactly the two types 2 and 167 mod 330, one of each parity',
          st['types'] == [2, 167])
    pros = {'even_minus_13': (2 - 13, [p for p in ODD_PRIMES if (2 - 13) % p == 0]),
            'odd_minus_14': (2 - 14, [p for p in ODD_PRIMES if (2 - 14) % p == 0])}
    check('d1.prose_reasons', 'prose reasons: x-13 = -11 mod 165 divisible by 11 alone; x-14 = -12 divisible by 3 alone; both gcds lie in {3,5,11}',
          pros['even_minus_13'] == (-11, [11]) and pros['odd_minus_14'] == (-12, [3]) and
          (13, 11) in [tuple(k) for k in st['killers'][2]] and [tuple(k) for k in st['killers'][167]] == [(14, 3)], pros)
    return st


def sec_bullets(R):
    rows = []
    for (e, f, r, par, comp, br, k_claim, rel_claim, rho_claim) in BULLETS:
        fixed = [p for p in ODD_PRIMES if e % p == 0]
        if comp[0] == 'anchor':
            a = comp[1]
            s, cpar, crho, W = a % e, a % 2, a % f, typ(a)
        else:
            _, s, cpar, crho = comp
            cands = [T for T in class_types(e, s) if T[0] == cpar and T[COORD[f]] == crho]
            assert len(cands) == 1
            W = cands[0]
        bracket = r - s
        k = sum(1 for p in fixed if bracket % p == 0)
        rel = 'ne' if k == 0 else 'eq'
        allowed = sorted({T[COORD[f]] for T in class_types(e, r) if T[0] == par and not R.qc(T, W)})
        exp_allowed = [crho] if rel == 'eq' else [v for v in range(f) if v != crho]
        rows.append({'e': e, 'subject_class': r, 'subject_parity': par, 'comparator': list(comp),
                     'claimed_bracket': br, 'computed_bracket': bracket,
                     'bracket_exact': bracket == br, 'bracket_abs': abs(bracket) == abs(br),
                     'k_ok': k == k_claim, 'relation_ok': rel == rel_claim and crho == rho_claim,
                     'semantics_ok': allowed == exp_allowed,
                     'opposite_parity': par != cpar, 'distinct_class': r != s})
    math_ok = all(x['k_ok'] and x['relation_ok'] and x['semantics_ok'] and x['opposite_parity'] and
                  x['distinct_class'] and x['bracket_abs'] for x in rows)
    check('s6.bullets_math', 'every §6 bullet: opposite parity, distinct classes, k, relation and brute-force (SQ) semantics agree (%d bullets)' % len(rows), math_ok)
    sign = [(x['e'], x['subject_class'], x['comparator'], x['claimed_bracket'], x['computed_bracket'])
            for x in rows if not x['bracket_exact']]
    check('s6.bracket_sign_nit', 'reviewer nit: exactly one bracket violates the stated r-y convention by sign only (e=33, x_4 vs x_15: printed [11], r-y = -11); k unaffected',
          sign == [(33, 4, ['elem', 15, 0, 4], 11, -11)], sign)
    return rows


def abstract_compat(e, f, a, b):
    (ca, pa, ra), (cb, pb, rb) = a, b
    if pa == pb:
        return True
    fixed = [p for p in ODD_PRIMES if e % p == 0]
    k = sum(1 for p in fixed if (ca - cb) % p == 0)
    return (ra != rb) if k == 0 else (ra == rb)


def e_table(R, e, f, classes):
    D = {r: qdomain(R, e, r) for r in classes}
    states = {r: sorted({(T[0], T[COORD[f]]) for T in D[r]}) for r in classes}
    sols = [c for c in product(*[D[r] for r in classes])
            if all(not R.qc(a, b) for a, b in combinations(c, 2))]
    Dac, log = ac3(D, R.qc)
    wipe = any(not v for v in Dac.values())
    abstract = [c for c in product(*[[(r, p, v) for (p, v) in states[r]] for r in classes])
                if all(abstract_compat(e, f, a, b) for a, b in combinations(c, 2))]
    return {'domain_sizes': {r: len(D[r]) for r in classes}, 'states': states,
            'product_size': math.prod(len(D[r]) for r in classes),
            'pairwise_compatible_tuples': len(sols),
            'witness': [RES[T] for T in sols[0]] if sols else None,
            'ac_wipeout': wipe, 'abstract_state_solutions': len(abstract),
            'status': 'SAT' if sols else 'UNSAT'}


def sec_e55_e33(R):
    t55 = e_table(R, 55, 3, (3, 24, 25))
    t33 = e_table(R, 33, 5, (22, 3, 4, 15))
    check('e55.states', 'e=55 (parity, mod 3) states equal §8: {(1,2)}, {(1,2)}, {(0,0),(0,2)}',
          t55['states'] == CLAIM_E55_STATES, t55['states'])
    check('e55.unsat', 'e=55: no pairwise-compatible triple (exhaustive product, AC wipeout, abstract states agree)',
          t55['status'] == 'UNSAT' and t55['ac_wipeout'] and t55['abstract_state_solutions'] == 0,
          {k: t55[k] for k in ('product_size', 'pairwise_compatible_tuples', 'ac_wipeout', 'abstract_state_solutions')})
    check('e33.states', 'e=33 (parity, mod 5) states equal §8', t33['states'] == CLAIM_E33_STATES, t33['states'])
    check('e33.unsat', 'e=33: no pairwise-compatible 4-tuple (exhaustive product, AC wipeout, abstract states agree)',
          t33['status'] == 'UNSAT' and t33['ac_wipeout'] and t33['abstract_state_solutions'] == 0,
          {k: t33[k] for k in ('product_size', 'pairwise_compatible_tuples', 'ac_wipeout', 'abstract_state_solutions')})
    check('e55_e33.coverage', 'each used class lifts to 330/e types: 6 per class for e=55, 10 per class for e=33',
          all(len(class_types(55, r)) == 6 for r in (3, 24, 25)) and all(len(class_types(33, r)) == 10 for r in (22, 3, 4, 15)))
    return {'e55': t55, 'e33': t33}


def lemma4_types():
    out = {}
    for c in range(15):
        r3, u = c % 3, c % 5
        T = (1 if r3 == 1 else 0, r3, u, G_OF_R5[u])
        out[c] = RES[T]
    return out


def e15_status(R, base_types=None):
    D0 = {r: qdomain(R, 15, r) for r in range(15)}
    Dac, log = ac3(D0, R.qc)
    ok_replay, Drep = replay(D0, log, R.qc)
    sizes = [len(Dac[r]) for r in range(15)]
    singles = all(s == 1 for s in sizes)
    final = {r: sorted(RES[T] for T in Dac[r]) for r in range(15)}
    eq_base = None
    if base_types is not None:
        eq_base = singles and all(final[r] == [base_types[r]] for r in range(15))
    tv = transversals(D0, lambda a, b: not R.qc(a, b))
    return {'initial_sizes': [len(D0[r]) for r in range(15)], 'ac_sizes': sizes,
            'ac_singletons': singles, 'ac_wipeout': any(s == 0 for s in sizes),
            'ac_removals': len(log), 'replay_ok': ok_replay and Drep == Dac,
            'final_types': final, 'equals_lemma4_types': eq_base, 'transversals': tv}


def sec_e15(R):
    L4 = lemma4_types()
    st = e15_status(R, L4)
    check('e15.initial_sizes', '§8: initial e=15 domain sizes', st['initial_sizes'] == CLAIM_E15_SIZES, st['initial_sizes'])
    check('e15.lemma4_types_claim', 'Lemma 4 types (parity by r3, r11=g(r5)) equal the §8 list',
          sorted(L4.values()) == CLAIM_E15_TYPES, sorted(L4.values()))
    check('e15.ac_fixpoint', 'AC-3 fixpoint (own worklist algorithm) is exactly the Lemma 4 singleton types',
          st['ac_singletons'] and st['equals_lemma4_types'], st['final_types'])
    check('e15.ac_replay', 'removal log replays: each removal is justified against the then-current domain', st['replay_ok'])
    tv = st['transversals']
    check('e15.unique_transversal', 'exhaustive backtracking over the initial domains: exactly one pairwise-compatible transversal, the Lemma 4 types',
          tv['count'] == 1 and not tv['capped'] and tv['solutions_sample'][0] == CLAIM_E15_TYPES, tv)
    S = [typ(x) for x in L4.values()]
    check('e15.types_properties', 'Lemma 4 types contain Y, are pairwise (SQ)-consistent, reduce mod 55 to {0,1,7,13,14} (three each)',
          set(TAILS) <= set(L4.values()) and all(not R.qc(a, b) for a, b in combinations(S, 2)) and
          sorted(x % 55 for x in L4.values()) == sorted([0, 1, 7, 13, 14] * 3))
    check('e15.coverage', 'all 15 classes, 22 types each (both parities, all residues mod 11) enumerated',
          all(len(class_types(15, r)) == 22 for r in range(15)))
    return st, L4


def sec_lemma4_mirror(R):
    def cls(r3, r5):
        return crt([(r3, 3), (r5, 5)])[0]
    A = {a: typ(a) for a in TAILS}
    rows = {a: ((a % 3, a % 5), a % 2, a % 11) for a in TAILS}
    check('lemma4.anchor_table', '§7 anchor table and g(r5) agree with the anchors',
          rows == ANCHOR_TABLE_E15 and all(G_OF_R5[a % 5] == a % 11 for a in TAILS), {a: list(v) for a, v in rows.items()})
    steps = {}
    s1 = True
    for u in range(5):
        c = cls(1, u)
        outside = [a for a in (1, 7, 13) if a % 15 != c]
        s1 &= len(outside) >= 2
        for T in class_types(15, c):
            if T[0] == 0 and not any(R.qc(T, A[a]) for a in outside):
                s1 = False
    steps['1'] = s1
    c10, c14 = cls(1, 0), cls(1, 4)
    odd10 = sorted({T[3] for T in class_types(15, c10) if T[0] == 1 and not R.qc(T, A[0])})
    odd14 = sorted({T[3] for T in class_types(15, c14) if T[0] == 1 and not R.qc(T, A[14])})
    steps['2'] = odd10 == [0] and odd14 == [3]
    ref10 = [T for T in class_types(15, c10) if T[0] == 1 and T[3] == 0][0]
    ref14 = [T for T in class_types(15, c14) if T[0] == 1 and T[3] == 3][0]
    refs = [ref10, ref14, A[1], A[7], A[13]]
    s3 = [ref[2] for ref in refs] == [0, 4, 1, 2, 3] and all(ref[1] == 1 for ref in refs)
    even_type = {}
    for r3 in (0, 2):
        for u in range(5):
            c = cls(r3, u)
            okr = sorted({T[3] for T in class_types(15, c) if T[0] == 0 and all(not R.qc(T, w) for w in refs)})
            share_one = all(sum(1 for w in refs if (T[1] == w[1]) + (T[2] == w[2]) >= 1) == 1
                            for T in class_types(15, c))
            s3 &= okr == [G_OF_R5[u]] and share_one
            even_type[c] = [T for T in class_types(15, c) if T[0] == 0 and T[3] == G_OF_R5[u]][0]
    steps['3'] = s3
    s4 = True
    for u in (1, 2, 3, 4):
        c = cls(0, u)
        s4 &= sorted({T[3] for T in class_types(15, c) if T[0] == 1 and not R.qc(T, A[0])}) == [0]
        if u == 4:
            s4 &= not any(T[0] == 1 and not R.qc(T, A[0]) and not R.qc(T, A[14]) for T in class_types(15, c))
    for u in (0, 1, 2, 3):
        c = cls(2, u)
        s4 &= sorted({T[3] for T in class_types(15, c) if T[0] == 1 and not R.qc(T, A[14])}) == [3]
        if u == 0:
            s4 &= not any(T[0] == 1 and not R.qc(T, A[14]) and not R.qc(T, A[0]) for T in class_types(15, c))
    s4 &= even_type[cls(0, 4)][3] == 3 and even_type[cls(2, 0)][3] == 0
    steps['4'] = s4
    e20, e04 = even_type[cls(2, 0)], even_type[cls(0, 4)]
    s5 = True
    for u in (1, 2, 3):
        c = cls(0, u)
        cand = [T for T in class_types(15, c) if T[0] == 1 and T[3] == 0]
        s5 &= bool(cand) and all(R.qc(T, e20) for T in cand) and all(T[1] != e20[1] and T[2] != e20[2] for T in cand)
        c = cls(2, u)
        cand = [T for T in class_types(15, c) if T[0] == 1 and T[3] == 3]
        s5 &= bool(cand) and all(R.qc(T, e04) for T in cand) and all(T[1] != e04[1] and T[2] != e04[2] for T in cand)
    c = cls(0, 0)
    s5 &= sorted({T[3] for T in class_types(15, c) if T[0] == 1 and not R.qc(T, e04)}) == [3]
    s5 &= not any(T[0] == 1 and not R.qc(T, e04) and not R.qc(T, A[14]) for T in class_types(15, c))
    c = cls(2, 4)
    s5 &= sorted({T[3] for T in class_types(15, c) if T[0] == 1 and not R.qc(T, e20)}) == [0]
    s5 &= not any(T[0] == 1 and not R.qc(T, e20) and not R.qc(T, A[0]) for T in class_types(15, c))
    steps['5'] = s5
    s6 = True
    for u in range(5):
        c = cls(1, u)
        s6 &= sorted({T[3] for T in class_types(15, c) if T[0] == 1 and not R.qc(T, even_type[cls(0, u)])}) == [G_OF_R5[u]]
    steps['6'] = s6
    check('lemma4.steps', 'Lemma 4 Steps 1-6 each verified on all types of the named classes, using only facts from earlier steps',
          all(steps.values()), steps)
    return steps


def sec_algebra(L4):
    out = {}
    W = [0] * 110
    for x in L4.values():
        W[x % 110] += 1
    Wclaim = [((2 if z % 2 == 0 else 1) if z % 55 in (0, 1, 7, 13, 14) else 0) for z in range(110)]
    check('lemma5.fold_weights', 'fold of the Lemma 4 types mod 110 has weights 2 (even) / 1 (odd) on z mod 55 in Y, else 0 (b=0; general b multiplies by 2^b)',
          W == Wclaim and sum(W) == 15)
    check('lemma5.crt_formula', 'z = 55*(z mod 2) + 56*(z mod 55) (mod 110) for all z',
          all((55 * (z % 2) + 56 * (z % 55)) % 110 == z for z in range(110)))
    rhs = [0] * 110
    for y in TAILS:
        rhs[(56 * y) % 110] += 2
        rhs[(55 + 56 * y) % 110] += 1
    check('lemma5.factorization', 'sum_z W(z) X^z == (2 + X^55) Y(X^56) mod X^110 - 1 (exact coefficients)', rhs == W)
    ms = (1, 2, 5, 10, 11, 22, 55, 110)
    cyc = {m: cyclotomic(m) for m in ms}
    check('cyclo.degrees', 'deg Phi_m = phi(m) for the m used', all(len(cyc[m]) - 1 == euler_phi(m) for m in ms),
          {m: len(cyc[m]) - 1 for m in ms})
    rem_nz = {m: p_divmod_monic(W, cyc[m])[1] != [0] for m in ms}
    primes = []
    p = 111
    while len(primes) < 4:
        if is_prime(p) and p % 110 == 1:
            primes.append(p)
        p += 110
    fp = {}
    for p in primes:
        g = primitive_root(p)
        fp[p] = {m: fp_values_at_primitive_roots(W, m, p, g) for m in ms}
    fp_nonzero = {m: all(all(v != 0 for v in fp[p][m]) for p in primes) for m in ms}
    fp_zero = {m: all(all(v == 0 for v in fp[p][m]) for p in primes) for m in ms}
    out['exact_remainder_nonzero'] = rem_nz
    out['fp_primes'] = primes
    out['fp_all_nonzero'] = fp_nonzero
    out['fp_all_zero'] = fp_zero
    check('lemma5.nonvanishing', 'W mod Phi_m is nonzero for m in {11,22,55,110} (exact division) and W is nonzero at every primitive m-th root in F_p for four primes p = 1 mod 110 (certifies Phi_m does not divide W)',
          all(rem_nz[m] and fp_nonzero[m] for m in (11, 22, 55, 110)), {m: [rem_nz[m], fp_nonzero[m]] for m in ms})
    check('lemma5.diagnostic_m', '§8 item 4 diagnostics: nonzero for m=1,2; zero remainder for m=5,10',
          rem_nz[1] and rem_nz[2] and not rem_nz[5] and not rem_nz[10] and fp_zero[5] and fp_zero[10])
    Yp = [1 if i in TAILS else 0 for i in range(15)]
    y_nz = {m: p_divmod_monic(Yp, cyc[m])[1] != [0] for m in (11, 55)}
    y_fp = {m: all(all(v != 0 for v in fp_values_at_primitive_roots(Yp, m, p, primitive_root(p))) for p in primes) for m in (11, 55)}
    red11 = sorted({i % 11 for i in TAILS})
    check('lemma5.Y_nonvanishing', 'Y nonzero mod Phi_55 and Phi_11 (exact and F_p); degree facts 14 < 40, reduction mod X^11-1 has exponents {0,1,2,3,7} of degree 7 < 10',
          all(y_nz.values()) and all(y_fp.values()) and len(Yp) - 1 == 14 < euler_phi(55) == 40 and red11 == [0, 1, 2, 3, 7] and max(red11) < euler_phi(11))
    orders = {m: m // math.gcd(m, 56) for m in (11, 22, 55, 110)}
    oddpart = {m: m // (2 if m % 2 == 0 else 1) for m in orders}
    check('lemma5.beta_order', 'ord(xi^56) = odd part of ord(xi) in {11,55} for ord(xi) in {11,22,55,110}',
          orders == oddpart and set(orders.values()) == {11, 55}, orders)
    psi = [1]
    for m in (11, 22, 55, 110):
        psi = p_mul(psi, cyc[m])
    check('lemma6.product', 'Phi_11 Phi_22 Phi_55 Phi_110 = 1 + X^10 + ... + X^100',
          psi == [1 if i % 10 == 0 else 0 for i in range(101)])
    x10m1 = [-1] + [0] * 9 + [1]
    check('lemma6.quotient', '(X^10 - 1) * (1 + X^10 + ... + X^100) = X^110 - 1 and {11,22,55,110} are the divisors of 110 divisible by 11',
          p_mul(psi, x10m1) == [-1] + [0] * 109 + [1] and [d for d in range(1, 111) if 110 % d == 0 and d % 11 == 0] == [11, 22, 55, 110])
    basis = [p_mul([0] * j + [1], psi) for j in range(10)]
    per = all(b + [0] * (110 - len(b)) == [1 if i % 10 == j else 0 for i in range(110)] for j, b in enumerate(basis))
    check('lemma6.periodicity_basis', 'X^j * Psi (j<10) has coefficients exactly on i = j mod 10 (so every R*Psi with deg R<10 is 10-periodic)', per)
    check('lemma6.divides_n', '11, 22, 55, 110 divide n = 165*2^t for every t>=1 (checked t=1..12; 110 | n iff 2 | n)',
          all((165 << t) % m == 0 for t in range(1, 13) for m in (11, 22, 55, 110)) and 165 % 110 != 0)
    ok2 = True
    for e in (3, 5, 11, 15, 33, 55, 165):
        prod_ = [1]
        for m in range(2, e + 1):
            if e % m == 0:
                prod_ = p_mul(prod_, cyclotomic(m))
        ok2 &= prod_ == [1] * e
    check('lemma2.cyclotomic_product', 'Lemma 2(b) algebra: product of Phi_m over 1<m|e equals 1+X+...+X^(e-1) for e in {3,5,11,15,33,55,165}', ok2)
    return out


def final_status(R):
    X1 = class_types(110, 1)
    allowed = {a: sorted(T[1] for T in X1 if not R.pc(T, typ(a))) for a in R.heads}
    surv = sorted(RES[T] for T in X1 if not any(R.pc(T, typ(a)) for a in R.heads))
    return {'types': sorted(RES[T] for T in X1), 'allowed_r3_by_head': allowed, 'survivors': surv,
            'status': 'SAT' if surv else 'UNSAT'}


def sec_final(R):
    st = final_status(R)
    check('final.certificate', 'x = 1 mod 110 (types 1,111,221): (SP) vs 0 allows only r3=0, vs 8 only r3=2; together none',
          st['types'] == [1, 111, 221] and st['allowed_r3_by_head'][0] == [0] and st['allowed_r3_by_head'][8] == [2] and st['status'] == 'UNSAT', st)
    check('final.premise_arith', '11 = 1 mod 10, 11 mod 110 = 11 (so P_110(1) = P_110(11) >= 1 under Lemma 6); x = 1 mod 110 is odd and differs from 0, 8 mod 110',
          11 % 10 == 1 % 10 and 1 % 2 == 1 and 1 % 110 not in (0, 8))
    ind = {a: [RES[T] for T in class_types(110, 1) if not R.pc(T, typ(a))] for a in (0, 8)}
    check('control.P_side_individual', 'P-side positive control: each final (SP) constraint alone is satisfiable (vs 0: 111; vs 8: 221)',
          ind[0] == [111] and ind[8] == [221], ind)
    # Without Lemma 6: (SP) + A + nonempty classes mod 11 is satisfiable at type level.
    chosen = [typ(a) for a in HEADS]
    wit = []
    for c in range(11):
        if any(T[3] == c for T in chosen):
            continue
        cand = [T for T in TYPES if T[3] == c and all(not R.pc(T, w) for w in chosen)]
        if not cand:
            wit = None
            break
        chosen.append(cand[0])
        wit.append(RES[cand[0]])
    ok = wit is not None and sorted({T[3] for T in chosen}) == list(range(11)) and \
        all(not R.pc(a, b) for a, b in combinations(chosen, 2))
    check('control.P_side_without_lemma6', 'reviewer control: without Lemma 6, a type set containing A, pairwise (SP)-consistent and meeting every class mod 11 exists (so Lemma 6 is load-bearing)',
          ok, wit)
    return {'final': st, 'individual': ind, 'no_lemma6_witness': wit}


def sec_q_control():
    t, n = 4, 2640
    GA = sorted({gcd_n(a - b, t) for a, b in combinations(HEADS, 2)})
    ctrl = CLAIM_CONTROL_2640
    own = sorted(crt([(r, 15), (G_OF_R5[r % 5], 11), ((r if r in TAILS else (1 if r % 3 == 1 else 0)), 16)])[0]
                 for r in range(15))
    bad_pairs = [(u, v, gcd_n(u - v, t)) for u, v in combinations(ctrl, 2) if gcd_n(u - v, t) in GA]
    props = {
        'GA_2640': GA,
        'size_distinct': len(set(ctrl)) == 15 and all(0 <= x < n for x in ctrl),
        'contains_Y': set(TAILS) <= set(ctrl),
        'one_per_class_mod15': sorted(x % 15 for x in ctrl) == list(range(15)),
        'lemma4_parity_and_mod11': all((x % 2 == (1 if x % 3 == 1 else 0)) and x % 11 == G_OF_R5[x % 5] for x in ctrl),
        'mod16_residues': all(x % 16 == (x if x in TAILS else x % 2) for x in ctrl),
        'own_crt_equals_claim': own == sorted(ctrl),
        'types_equal_lemma4': sorted(x % 330 for x in ctrl) == CLAIM_E15_TYPES,
        'pairwise_gcd_hits_GA': bad_pairs}
    check('control.Q_side_2640', '§9 Q-side control at n=2640 reproduced: G_A={3,5,8,11}, 15 elements, contains Y, one per class mod 15, Lemma 4 parity/mod 11, 16-adic residues, own CRT equal, no pairwise gcd in G_A (SAT, Q-only)',
          GA == CLAIM_GA_2640 and all(v for k, v in props.items() if k not in ('GA_2640', 'pairwise_gcd_hits_GA')) and not bad_pairs, props)
    # Negative controls on the Q-side control set.
    neg = {}
    flip_par = crt([(10, 15), (0, 11), (0, 16)])[0]
    m1 = [x for x in ctrl if x != 385] + [flip_par]
    hits1 = sorted({(min(u, v), max(u, v), gcd_n(u - v, t)) for u, v in combinations(m1, 2) if gcd_n(u - v, t) in GA and flip_par in (u, v)})
    neg['parity_flip_385'] = {'replacement': flip_par, 'conflicts': hits1}
    flip11 = crt([(3, 15), (1, 11), (0, 16)])[0]
    m2 = [x for x in ctrl if x != 288] + [flip11]
    hits2 = sorted({(min(u, v), max(u, v), gcd_n(u - v, t)) for u, v in combinations(m2, 2) if gcd_n(u - v, t) in GA and flip11 in (u, v)})
    neg['mod11_flip_288'] = {'replacement': flip11, 'conflicts': hits2}
    check('control.Q_negative_parity_flip', 'negative: making the class-(1,0) element even rejects it with gcd 3 against the odd anchors 1, 7, 13 (Step 1 reason)',
          sorted(h[2] for h in hits1 if {h[0], h[1]} & {1, 7, 13}) == [3, 3, 3] and all(h[2] == 3 for h in hits1), hits1)
    check('control.Q_negative_mod11_flip', 'negative: moving the class-(0,3) element to residue 1 mod 11 rejects it exactly by gcd 5 vs anchor 13 (shared r5 forces 2 mod 11) and gcd 11 vs anchor 1 (no shared coordinate forbids 1 mod 11) -- Step 3 reason',
          hits2 == sorted([(1, flip11, 11), (13, flip11, 5)]), hits2)
    return {'props': props, 'negatives': neg}


def sec_diagnostics(tmax=8):
    out = {}
    L4 = lemma4_types()
    R = Rules('baseline')
    doms = {(e, r): {RES[T] for T in qdomain(R, e, r)}
            for e, rs in ((55, (3, 24, 25)), (33, (22, 3, 4, 15)), (15, range(15))) for r in rs}
    ok_claim = True
    for t in range(1, tmax + 1):
        n = 165 << t
        GA = {gcd_n(a - b, t) for a, b in combinations(HEADS, 2)}
        GY = {gcd_n(a - b, t) for a, b in combinations(TAILS, 2)}
        Ph = [x for x in range(n) if all(x == a or gcd_n(x - a, t) not in GY for a in HEADS)]
        Qt = [x for x in range(n) if all(x == y or gcd_n(x - y, t) not in GA for y in TAILS)]
        l3 = [x for x in Ph if x % 15 == 4 or x % 33 == 1 or x % 55 == 2]
        c2 = [x for x in Qt if x % 165 == 2]
        incl = all((x % 330) in doms[(e, r)] for (e, r) in doms for x in Qt if x % e == r)
        rec = {'n': n, 'P_screen': len(Ph), 'Q_screen': len(Qt), 'lemma3_hits': len(l3),
               'class2_hits': len(c2), 'Q_types_inside_domains': incl,
               'heads_in_P_screen': [a for a in HEADS if a in Ph], 'tails_in_Q_screen': [y for y in TAILS if y in Qt]}
        if t in CLAIM_SCREENS:
            rec['claimed'] = CLAIM_SCREENS[t]
            ok_claim &= (len(Ph), len(Qt)) == CLAIM_SCREENS[t]
        out[t] = rec
    check('diag.screen_sizes', '§8 item 6 screen sizes for t=1..6 reproduced with own valuation gcd', ok_claim,
          {t: (out[t]['P_screen'], out[t]['Q_screen']) for t in out})
    check('diag.exclusions', 'for t=1..%d the actual screens avoid the Lemma 3 classes and 2 mod 165, and Q-screen types lie in every used domain' % tmax,
          all(v['lemma3_hits'] == 0 and v['class2_hits'] == 0 and v['Q_types_inside_domains'] for v in out.values()))
    check('diag.t1_anchor_screen_anomaly', 'reviewer observation: at t=1 the actual screens exclude anchors themselves (gcd 2 collision); from t=2 all anchors pass',
          out[1]['heads_in_P_screen'] != list(HEADS) and all(out[t]['heads_in_P_screen'] == list(HEADS) and out[t]['tails_in_Q_screen'] == list(TAILS) for t in out if t >= 2),
          {t: [out[t]['heads_in_P_screen'], out[t]['tails_in_Q_screen']] for t in out})
    return out


def sec_class2_lifts(tmax=8):
    out = {}
    ok = True
    for t in range(1, tmax + 1):
        lifts = [2 + 165 * k for k in range(1 << t)]
        ev = [x for x in lifts if x % 2 == 0]
        od = [x for x in lifts if x % 2 == 1]
        ok_e = all(gcd_n(x - 13, t) == 11 and gcd_n(x - 7, t) == 5 for x in ev)
        ok_o = all(gcd_n(x - 14, t) == 3 for x in od)
        GA = {gcd_n(a - b, t) for a, b in combinations(HEADS, 2)}
        ok &= ok_e and ok_o and {3, 5, 11} <= GA and len(ev) == len(od) == (1 << (t - 1))
        out[t] = {'lifts': len(lifts), 'even': len(ev), 'odd': len(od), 'even_reason_ok': ok_e, 'odd_reason_ok': ok_o}
    check('d1.actual_lifts', 'all 2^t lifts of 2 mod 165 in Z_n (t=1..%d): even lifts have gcd(x-13,n)=11 and gcd(x-7,n)=5, odd lifts gcd(x-14,n)=3; half of each parity' % tmax, ok, out)
    return out


def analyze(R, base_types):
    res = {'rules': R.describe()}
    res['anchors_P_conflicts'] = [(a, b) for a, b in combinations(R.heads, 2) if R.pc(typ(a), typ(b))]
    res['anchors_Q_conflicts'] = [(a, b) for a, b in combinations(R.tails, 2) if R.qc(typ(a), typ(b))]
    l3 = lemma3_status(R)
    res['lemma3'] = {k: {'status': v['status'], 'survivors': v['survivors'], 'survivor_parities': v['survivor_parities']} for k, v in l3.items()}
    res['d1'] = {k: v for k, v in d1_status(R).items() if k != 'killers'}
    res['d1_representative_only'] = d1_status(R, True)['status']
    for key, e, f, cl in (('e55', 55, 3, (3, 24, 25)), ('e33', 33, 5, (22, 3, 4, 15))):
        t = e_table(R, e, f, cl)
        res[key] = {'status': t['status'], 'witness': t['witness'], 'tuples': t['pairwise_compatible_tuples'],
                    'ac_wipeout': t['ac_wipeout']}
    s15 = e15_status(R, base_types)
    res['e15'] = {'ac_sizes': s15['ac_sizes'], 'ac_singletons': s15['ac_singletons'], 'ac_wipeout': s15['ac_wipeout'],
                  'equals_lemma4_types': s15['equals_lemma4_types'], 'replay_ok': s15['replay_ok'],
                  'transversals': {k: s15['transversals'][k] for k in ('count', 'capped', 'nodes')}}
    fs = final_status(R)
    res['final'] = {'status': fs['status'], 'survivors': fs['survivors']}
    return res


def sec_mutations(base_types):
    base = Rules('baseline')
    B = analyze(base, base_types)
    muts = [
        ('M01_drop_head_0', Rules('drop head 0', heads=(3, 8, 11))),
        ('M02_drop_head_3', Rules('drop head 3', heads=(0, 8, 11))),
        ('M03_drop_head_8', Rules('drop head 8', heads=(0, 3, 11))),
        ('M04_drop_head_11', Rules('drop head 11', heads=(0, 3, 8))),
        ('M05_drop_tail_0', Rules('drop tail 0', tails=(1, 7, 13, 14))),
        ('M06_drop_tail_1', Rules('drop tail 1', tails=(0, 7, 13, 14))),
        ('M07_drop_tail_7', Rules('drop tail 7', tails=(0, 1, 13, 14))),
        ('M08_drop_tail_13', Rules('drop tail 13', tails=(0, 1, 7, 14))),
        ('M09_drop_tail_14', Rules('drop tail 14', tails=(0, 1, 7, 13))),
        ('M10_drop_gcd3_from_SQ', Rules('(SQ) without gcd class 3', qban={5, 11})),
        ('M11_drop_gcd5_from_SQ', Rules('(SQ) without gcd class 5', qban={3, 11})),
        ('M12_drop_gcd11_from_SQ', Rules('(SQ) without gcd class 11', qban={3, 5})),
        ('M13_drop_gcd1_from_SP', Rules('(SP) without gcd class 1', spset=set())),
        ('M14_drop_parity_restriction', Rules('rules applied to all pairs (parity dropped)', parity_required=False)),
    ]
    out = {'BASELINE': B}
    for name, R in muts:
        out[name] = analyze(R, base_types)

    def l3stat(r):
        return [r['lemma3'][k]['status'] for k in ('4 mod 15', '1 mod 33', '2 mod 55')]

    def l3par(r):
        return sorted({p for k in r['lemma3'] for p in r['lemma3'][k]['survivor_parities']})

    check('mut.baseline', 'baseline: all tables UNSAT, Lemma 4 types, anchors consistent',
          l3stat(B) == ['UNSAT'] * 3 and B['d1']['status'] == 'UNSAT' and B['e55']['status'] == 'UNSAT' and
          B['e33']['status'] == 'UNSAT' and B['e15']['equals_lemma4_types'] and B['final']['status'] == 'UNSAT' and
          not B['anchors_P_conflicts'] and not B['anchors_Q_conflicts'])
    o = out
    check('mut.M01', 'drop head 0: Lemma 3 classes SAT with odd survivors only (odd x keeps one opposite anchor); final SAT {221}; d=1 still UNSAT (anchor 7 gcd 5)',
          l3stat(o['M01_drop_head_0']) == ['SAT'] * 3 and l3par(o['M01_drop_head_0']) == [1] and
          o['M01_drop_head_0']['final']['survivors'] == [221] and o['M01_drop_head_0']['d1']['status'] == 'UNSAT')
    check('mut.M02', 'drop head 3: Lemma 3 SAT with even survivors only; final UNSAT (needs only 0 and 8); d=1 UNSAT',
          l3stat(o['M02_drop_head_3']) == ['SAT'] * 3 and l3par(o['M02_drop_head_3']) == [0] and
          o['M02_drop_head_3']['final']['status'] == 'UNSAT' and o['M02_drop_head_3']['d1']['status'] == 'UNSAT')
    check('mut.M03', 'drop head 8: Lemma 3 SAT with odd survivors only; final SAT {111}; d=1 UNSAT',
          l3stat(o['M03_drop_head_8']) == ['SAT'] * 3 and l3par(o['M03_drop_head_8']) == [1] and
          o['M03_drop_head_8']['final']['survivors'] == [111] and o['M03_drop_head_8']['d1']['status'] == 'UNSAT')
    check('mut.M04', 'drop head 11: Lemma 3 SAT with even survivors only; final table still UNSAT but its premise 11 in P is gone; d=1 UNSAT',
          l3stat(o['M04_drop_head_11']) == ['SAT'] * 3 and l3par(o['M04_drop_head_11']) == [0] and
          o['M04_drop_head_11']['final']['status'] == 'UNSAT' and o['M04_drop_head_11']['d1']['status'] == 'UNSAT')
    check('mut.M08', 'drop tail 13: d=1 still UNSAT (even lift 2 killed by anchor 7 with gcd 5) -- passes for the backup reason',
          o['M08_drop_tail_13']['d1']['status'] == 'UNSAT')
    check('mut.M09', 'drop tail 14: d=1 SAT with survivor exactly 167 (odd lift); representative-only check (2 only) wrongly UNSAT -> full-lift coverage is load-bearing',
          o['M09_drop_tail_14']['d1']['survivors'] == [167] and o['M09_drop_tail_14']['d1_representative_only'] == 'UNSAT')
    check('mut.M10_M12', 'gcd-class drops on (SQ): without 3 -> d=1 SAT {167}; without 5 or 11 -> d=1 UNSAT (other killer survives)',
          o['M10_drop_gcd3_from_SQ']['d1']['survivors'] == [167] and o['M11_drop_gcd5_from_SQ']['d1']['status'] == 'UNSAT' and
          o['M12_drop_gcd11_from_SQ']['d1']['status'] == 'UNSAT')
    check('mut.M10_M12_P_side_unchanged', 'gcd-class drops on (SQ) leave the P-side Lemma 3 and final tables UNSAT',
          all(l3stat(o[k]) == ['UNSAT'] * 3 and o[k]['final']['status'] == 'UNSAT'
              for k in ('M10_drop_gcd3_from_SQ', 'M11_drop_gcd5_from_SQ', 'M12_drop_gcd11_from_SQ')))
    check('mut.M13', 'drop gcd class 1 from (SP): Lemma 3 and final become SAT with every type surviving; Q-side unaffected',
          l3stat(o['M13_drop_gcd1_from_SP']) == ['SAT'] * 3 and o['M13_drop_gcd1_from_SP']['final']['survivors'] == [1, 111, 221] and
          o['M13_drop_gcd1_from_SP']['d1']['status'] == 'UNSAT' and o['M13_drop_gcd1_from_SP']['e15']['equals_lemma4_types'])
    m14 = o['M14_drop_parity_restriction']
    real = {t: {'gcd(8,n)': gcd_n(8, t), 'gcd(6,n)': gcd_n(6, t),
                'G_Y': sorted({gcd_n(a - b, t) for a, b in combinations(TAILS, 2)}),
                'G_A': sorted({gcd_n(a - b, t) for a, b in combinations(HEADS, 2)})} for t in (1, 2, 3, 4)}
    spurious = all(real[t]['gcd(6,n)'] not in real[t]['G_A'] and real[t]['gcd(8,n)'] not in real[t]['G_Y'] for t in (2, 3, 4))
    check('mut.M14', 'drop parity restriction: the mutated rule flags the literal anchors ((0,8),(3,11) in P; (1,7),(1,13),(7,13) in Q) although for t>=2 their actual gcds (8 or 4; 6) are not Sands collisions -> rejected as unsound (Lemma 1 needs odd u)',
          sorted(map(tuple, m14['anchors_P_conflicts'])) == [(0, 8), (3, 11)] and
          sorted(map(tuple, m14['anchors_Q_conflicts'])) == [(1, 7), (1, 13), (7, 13)] and spurious, real)
    return out


SUMMARY_MAP = {
    'Lemma 3 classes 4 mod 15, 1 mod 33, 2 mod 55: UNSAT (22+10+6 types)': ['lemma3.prose_rows', 'lemma3.exhaustive', 'lemma3.coverage', 'lemma3.d_values'],
    'd=1 class 2 mod 165: UNSAT (types 2, 167; all 2^t actual lifts t<=8)': ['d1.class2_empty', 'd1.coverage', 'd1.prose_reasons', 'd1.actual_lifts'],
    'e=55 triple: UNSAT (product, AC wipeout, abstract states)': ['e55.states', 'e55.unsat', 's6.bullets_math'],
    'e=33 quadruple: UNSAT (product, AC wipeout, abstract states)': ['e33.states', 'e33.unsat', 's6.bullets_math'],
    'e=15 Lemma 4 structure: unique AC fixpoint / unique transversal / step mirror': ['e15.initial_sizes', 'e15.lemma4_types_claim', 'e15.ac_fixpoint', 'e15.ac_replay', 'e15.unique_transversal', 'e15.types_properties', 'lemma4.anchor_table', 'lemma4.steps', 'ruleR.equivalence'],
    'Lemma 5 nonvanishing (exact + F_p) and CRT factorization': ['lemma5.fold_weights', 'lemma5.crt_formula', 'lemma5.factorization', 'lemma5.nonvanishing', 'lemma5.Y_nonvanishing', 'lemma5.beta_order', 'cyclo.degrees'],
    'Lemma 6 product identity and 10-periodicity': ['lemma6.product', 'lemma6.quotient', 'lemma6.periodicity_basis', 'lemma6.divides_n'],
    'Final certificate x = 1 mod 110: UNSAT (3 types)': ['final.certificate', 'final.premise_arith'],
    'Q-side control n=2640: SAT (Q-only witness) and its negatives rejected': ['control.Q_side_2640', 'control.Q_negative_parity_flip', 'control.Q_negative_mod11_flip'],
    'P-side controls: SAT individually and SAT without Lemma 6': ['control.P_side_individual', 'control.P_side_without_lemma6'],
    'Bounded actual-n screens t=1..8 (claims t=1..6)': ['diag.screen_sizes', 'diag.exclusions', 'gcd.odd_parts_t_independent', 'lemma1.bounded'],
    'Pre-registered mutations': ['mut.baseline', 'mut.M01', 'mut.M02', 'mut.M03', 'mut.M04', 'mut.M08', 'mut.M09', 'mut.M10_M12', 'mut.M10_M12_P_side_unchanged', 'mut.M13', 'mut.M14'],
}


def summarize():
    ok = {c['id']: c['ok'] for c in CHECKS}
    return {k: ('VERIFIED' if all(ok.get(i, False) for i in ids) else 'NOT VERIFIED') + ' [' + ', '.join(ids) + ']'
            for k, ids in SUMMARY_MAP.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out')
    args = ap.parse_args()
    R = Rules('baseline')
    sections = {}
    sections['types'] = sec_types()
    sections['gcd_sets'] = sec_gcd_sets()
    sections['lemma1'] = sec_lemma1()
    sections['rule_R'] = sec_rule_R(R)
    sections['lemma3'] = sec_lemma3(R)
    sections['d1'] = sec_d1(R)
    sections['bullets'] = sec_bullets(R)
    sections['e55_e33'] = sec_e55_e33(R)
    e15, L4 = sec_e15(R)
    sections['e15'] = e15
    sections['lemma4_mirror'] = sec_lemma4_mirror(R)
    sections['algebra'] = sec_algebra(L4)
    sections['final'] = sec_final(R)
    sections['q_control'] = sec_q_control()
    sections['diagnostics'] = sec_diagnostics()
    sections['class2_lifts'] = sec_class2_lifts()
    sections['mutations'] = sec_mutations(L4)
    missing = sorted({i for ids in SUMMARY_MAP.values() for i in ids} - {c['id'] for c in CHECKS})
    check('meta.summary_ids_exist', 'every summary row cites only registered check ids', not missing, missing)
    n_ok = sum(1 for c in CHECKS if c['ok'])
    report = {
        'script': 'reviewer-f177-arith-check-v1.py',
        'python': sys.version.split()[0],
        'candidate_sha256': '20169ac9e398d9d1ef37d263f9b51d0f9168c095c3e3eb21ade47572822d39c6',
        'checks_total': len(CHECKS), 'checks_ok': n_ok,
        'failed_checks': [c['id'] for c in CHECKS if not c['ok']],
        'summary': summarize(),
        'checks': CHECKS,
        'sections': sections,
        'result': 'ALL_REGISTERED_CHECKS_HOLD' if n_ok == len(CHECKS) else 'SOME_CHECK_FAILED'}
    text = json.dumps(report, indent=1, sort_keys=True, default=lambda o: sorted(o) if isinstance(o, (set, frozenset)) else str(o)) + '\n'
    if args.out:
        with open(args.out, 'x', encoding='utf-8') as fh:
            fh.write(text)
        print(json.dumps({'checks_total': len(CHECKS), 'checks_ok': n_ok,
                          'failed_checks': report['failed_checks'], 'result': report['result']}))
    else:
        print(text)
    return 0 if n_ok == len(CHECKS) else 1


if __name__ == '__main__':
    sys.exit(main())
