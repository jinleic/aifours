#!/usr/bin/env python3
"""Reviewer-written exact Shannon-cone separation check for the contracted nine-variable inequality.

Data: the 512 rational values `nine_variable_primal_values` are taken from the pinned author receipt
(SHA 486fe82f...) as DATA ONLY; no author code is executed or imported. Everything else is reviewer code:
elemental-inequality enumeration for n=9 (9 + C(9,2)*2^7 = 4617 rows), full polymatroid axioms
(all 512*512 submodular pairs and all single-element monotonicity steps), the contraction of the
hand-transcribed 12-variable inequality to 9 variables, the exact value of L3_9 at the witness, the
twelve 9-variable CMIs, positive controls (uniform matroids, a modular function, an entropic vector of a
random 9-bit law) and negative controls (altered coefficient, perturbed/missing/nonzero-empty coordinates).
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json, random, subprocess

getcontext().prec = 50
HERE = Path(__file__).resolve().parent
RECEIPT = Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus/frontier-20261028-nine-variable-gluing-separation-check-result.json')
RECEIPT_SHA = '486fe82f61fe70bef56027897f08422f8812115265bd5443c75cb524b6aea60c'
OUT = HERE / 'reviewer-nine-variable-witness-check-receipt.json'
N = 9
NINE = ('b', 'd', 'e', 'f', 'g', 'i', 'j', 'D', 'F')
BACKGROUND = frozenset('ach')
L3_TERMS_12 = [
    (-1, 'abcehi'), (-1, 'acefghi'), (+2, 'abcdefghij'),
    (+1, 'abcefhiD'), (+1, 'acefghiD'), (-1, 'acefhijD'), (+1, 'abcefhijD'), (-2, 'abcdefghijD'),
    (+1, 'abcehiF'), (-1, 'acefhiF'), (+1, 'acefghiF'), (-1, 'abcefghiF'),
    (-1, 'abcdfhjF'), (+1, 'abcdfghjF'), (+1, 'acefhijF'), (-1, 'abcefhijF'),
    (+1, 'abcdefhijF'), (-1, 'abcdefghijF'),
]
CMI_ROWS_12 = [('b','g','acefhiDF'),('b','F','acefhijD'),('d','D','abcefhijF'),('d','D','abcefghiF'),
               ('e','g','abcdfhjDF'),('f','F','abcehiD'),('g','i','abcdefhjDF'),('g','D','abcdfhjF'),
               ('j','D','abcdefghiF'),('j','D','acefhiF'),('D','F','acefghi'),('D','F','abcehi')]
EXPECTED_VALUE = Fraction(-7123, 3450000)


def clock():
    return subprocess.run(['/bin/date', '-u', '+%Y-%m-%dT%H:%M:%S.%NZ'], capture_output=True, text=True).stdout.strip()


def mask(labels):
    s = frozenset(labels) - BACKGROUND
    if not frozenset(labels) >= BACKGROUND:
        raise ValueError(('NO_BACKGROUND', labels))
    return sum(1 << NINE.index(v) for v in s)


def contract():
    coeff = {}
    for c, labels in L3_TERMS_12:
        m = mask(labels); coeff[m] = coeff.get(m, 0) + c
    return {m: c for m, c in coeff.items() if c}


def elemental_rows(n):
    """Reviewer enumeration of Yeung's elemental inequalities as (plus-masks, minus-masks) pairs."""
    full = (1 << n) - 1; rows = []
    for i in range(n):
        rows.append(((full,), (full ^ (1 << i),)))
    for i, j in combinations(range(n), 2):
        a, b = 1 << i, 1 << j; rest = [k for k in range(n) if k not in (i, j)]
        for bits in product((0, 1), repeat=n - 2):
            k = sum(1 << r for r, on in zip(rest, bits) if on)
            rows.append(((k | a, k | b), (k | a | b, k)))
    return rows


ROWS = elemental_rows(N)


def check_elemental(h):
    if len(h) != 1 << N: raise ValueError('LENGTH')
    if h[0] != 0: raise ValueError('EMPTY_SET_NONZERO')
    viol = 0
    for plus, minus in ROWS:
        if sum(h[m] for m in plus) - sum(h[m] for m in minus) < 0: viol += 1
    return viol


def check_full_polymatroid(h):
    full = (1 << N) - 1; mono = sub = 0
    for s in range(1 << N):
        for i in range(N):
            if not s & (1 << i) and h[s | (1 << i)] < h[s]: mono += 1
    for s in range(1 << N):
        for t in range(s + 1, 1 << N):
            if h[s] + h[t] < h[s | t] + h[s & t]: sub += 1
    return mono, sub


def value(h, coeff):
    return sum((Fraction(c) * h[m] for m, c in coeff.items()), Fraction(0))


def cmi9(h, a, b, cond):
    A = sum(1 << NINE.index(v) for v in a); B = sum(1 << NINE.index(v) for v in b); C = sum(1 << NINE.index(v) for v in cond)
    return h[A | C] + h[B | C] - h[A | B | C] - h[C]


def main():
    receipt = {'clock_start_utc': clock(), 'receipt_sha256_pinned': RECEIPT_SHA}
    raw = RECEIPT.read_bytes()
    if sha256(raw).hexdigest() != RECEIPT_SHA: raise SystemExit('RECEIPT_HASH_MISMATCH')
    doc = json.loads(raw)
    h = [Fraction(x) for x in doc['nine_variable_primal_values']]
    coeff = contract()
    author_table = {int(m): int(c) for m, c in doc['nine_variable_inequality']}
    receipt['contraction'] = {
        'reviewer_masks_sorted': sorted(coeff.items()),
        'equals_author_table': coeff == author_table,
        'coefficient_sum': sum(coeff.values()),
        'author_order_field': doc['nine_variable_order'],
        'reviewer_order': list(NINE),
    }
    if coeff != author_table: raise SystemExit('CONTRACTION_TABLE_MISMATCH')

    receipt['elemental_row_count'] = len(ROWS)
    if len(ROWS) != 4617: raise SystemExit('ROW_COUNT')
    receipt['witness'] = {
        'coordinates': len(h), 'empty_set_value': str(h[0]),
        'elemental_violations': check_elemental(h),
    }
    mono, sub = check_full_polymatroid(h)
    receipt['witness'].update({'full_monotonicity_violations': mono, 'full_submodularity_violations_over_all_pairs': sub,
                               'submodular_pairs_checked': (1 << N) * ((1 << N) - 1) // 2,
                               'monotonicity_steps_checked': (1 << N) * N // 2})
    v = value(h, coeff)
    ci = cmi9(h, 'D', 'F', 'bdefgij')
    cmis = [cmi9(h, a, b, ''.join(x for x in c if x not in BACKGROUND)) for a, b, c in CMI_ROWS_12]
    receipt['witness'].update({
        'L3_nine_value': str(v), 'L3_nine_value_equals_minus_7123_over_3450000': v == EXPECTED_VALUE,
        'L3_nine_negative': v < 0,
        'I(D;F|bdefgij)': str(ci), 'author_receipt_CI_field': doc['conditional_mutual_information_DF_given_X'],
        'CI_matches_author_receipt': ci == Fraction(doc['conditional_mutual_information_DF_given_X']),
        'twelve_CMIs_at_witness': [str(x) for x in cmis],
        'all_twelve_CMIs_nonnegative': all(x >= 0 for x in cmis),
        'sum_CMIs_minus_2CI_equals_L3': sum(cmis, Fraction(0)) - 2 * ci == v,
        'max_entropy_H(all)': str(h[511]),
    })
    if receipt['witness']['elemental_violations'] or mono or sub or v != EXPECTED_VALUE: raise SystemExit(('WITNESS_FAILED', receipt['witness']))

    # ---- positive controls (must satisfy all elemental rows AND L3 >= 0) ----
    pos = {}
    for k in range(1, N + 1):
        u = [Fraction(min(bin(s).count('1'), k)) for s in range(1 << N)]
        pos[f'uniform_matroid_U_{k}_{N}'] = {'elemental_violations': check_elemental(u), 'L3': str(value(u, coeff))}
    w = [Fraction(random.Random(7).randint(1, 9)) for _ in range(N)]
    mod = [sum((w[i] for i in range(N) if s & (1 << i)), Fraction(0)) for s in range(1 << N)]
    pos['modular_random_weights'] = {'elemental_violations': check_elemental(mod), 'L3': str(value(mod, coeff))}
    # entropic vector of a random 9-bit law (Decimal); tolerance 1e-40
    rng = random.Random(11); atoms = {a: Fraction(rng.randint(1, 60)) for a in product((0, 1), repeat=N)}
    tot = sum(atoms.values()); atoms = {a: p / tot for a, p in atoms.items()}
    LN2 = Decimal(2).ln(); ent = []
    for s in range(1 << N):
        m = {}
        for a, p in atoms.items():
            key = tuple(a[i] for i in range(N) if s & (1 << i)); m[key] = m.get(key, Fraction(0)) + p
        ent.append(sum((-(Decimal(p.numerator) / Decimal(p.denominator)) * (Decimal(p.numerator) / Decimal(p.denominator)).ln() / LN2 for p in m.values()), Decimal(0)))
    tol = Decimal('1e-40')
    ev = sum((Decimal(c) * ent[m] for m, c in coeff.items()), Decimal(0))
    eviol = sum(1 for plus, minus in ROWS if sum(ent[m] for m in plus) - sum(ent[m] for m in minus) < -tol)
    pos['entropic_random_9bit_law'] = {'elemental_violations_tol_1e-40': eviol, 'L3': str(ev.quantize(Decimal('1e-30'))), 'L3_nonnegative': ev > -tol}
    receipt['positive_controls'] = pos
    if any(c['elemental_violations'] for k, c in pos.items() if 'elemental_violations' in c) or any(Fraction(c['L3']) < 0 for k, c in pos.items() if k != 'entropic_random_9bit_law') or eviol or not pos['entropic_random_9bit_law']['L3_nonnegative']:
        raise SystemExit(('POSITIVE_CONTROL_FAILED', pos))

    # ---- negative controls ----
    neg = {}
    def expect_reject(tag, fn):
        try:
            r = fn()
        except (ValueError, IndexError) as e:
            neg[tag] = f'rejected ({e.args[0] if e.args else type(e).__name__})'; return
        neg[tag] = 'rejected' if r else 'ACCEPTED_UNEXPECTEDLY'
        if not r: raise SystemExit(('NEGATIVE_CONTROL_FAILED', tag))
    hh = list(h); hh[0] = Fraction(1); expect_reject('nonzero_empty_set', lambda: check_elemental(hh))
    hh = list(h); hh[511] -= Fraction(1, 10**6); expect_reject('full_set_lowered_by_1e-6_breaks_monotonicity', lambda: check_elemental(hh) > 0)
    hh = list(h); hh[37] += Fraction(1, 7); expect_reject('coordinate_37_raised_by_1_over_7_breaks_elemental', lambda: check_elemental(hh) > 0)
    hh = list(h); hh.pop(); expect_reject('missing_coordinate', lambda: check_elemental(hh))
    cc = dict(coeff); cc[37] = +1; expect_reject('altered_coefficient_mask37_-1_to_+1_changes_value', lambda: value(h, cc) != EXPECTED_VALUE)
    cc = dict(coeff); del cc[331]; expect_reject('removed_term_mask331_changes_value', lambda: value(h, cc) != EXPECTED_VALUE)
    cc = dict(coeff); cc[127] = 1; expect_reject('altered_coefficient_mask127_2_to_1_changes_value', lambda: value(h, cc) != EXPECTED_VALUE)
    neg['altered_coefficient_values'] = {'mask37_flipped': str(value(h, {**coeff, 37: 1})), 'mask331_removed': str(value(h, {m: c for m, c in coeff.items() if m != 331})), 'mask127_halved': str(value(h, {**coeff, 127: 1}))}
    receipt['negative_controls'] = neg

    receipt['verdict_separation'] = 'WITNESS_IS_A_9_VARIABLE_POLYMATROID_WITH_L3_NEGATIVE'
    receipt['script_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    receipt['clock_end_utc'] = clock()
    with OUT.open('x', encoding='utf-8') as fh:
        json.dump(receipt, fh, indent=1); fh.write('\n')
    print(json.dumps(receipt, indent=1))


if __name__ == '__main__':
    main()
