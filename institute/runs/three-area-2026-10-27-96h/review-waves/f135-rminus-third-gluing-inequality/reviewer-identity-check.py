#!/usr/bin/env python3
"""Reviewer-written exact check: third gluing inequality L3 = sum_{k=1}^{12} I_k - 2 I(D;F|X).

Independent of all author checkers. The 18 entropy terms and the 12 CMI rows are hand-transcribed
from the candidate markdown by the reviewer; a reviewer-written parser of the LaTeX block and of the
CMI table then binds the transcription to the frozen text. Entropy expressions are exact integer
coefficient maps frozenset(variables) -> int. No floating point anywhere.
"""
from hashlib import sha256
from pathlib import Path
import json, re, subprocess

HERE = Path(__file__).resolve().parent
CAND = Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus/frontier-20261028-third-gluing-inequality-v1.md')
CAND_SHA = 'dc51023de716613629fbcd11e57f19098e50af1a16b84c05f268153c9e6a2a61'
OUT = HERE / 'reviewer-identity-check-receipt.json'

X = tuple('abcdefghij')                 # original ten variables
AUX = ('D', 'F')
BACKGROUND = frozenset('ach')
NINE_ORDER = ('b', 'd', 'e', 'f', 'g', 'i', 'j', 'D', 'F')   # contraction order used for 9-variable masks

# ---- reviewer hand transcription of the displayed 18 terms (coefficient, variables) ----
L3_TERMS = [
    (-1, 'abcehi'), (-1, 'acefghi'), (+2, 'abcdefghij'),
    (+1, 'abcefhiD'), (+1, 'acefghiD'), (-1, 'acefhijD'), (+1, 'abcefhijD'), (-2, 'abcdefghijD'),
    (+1, 'abcehiF'), (-1, 'acefhiF'), (+1, 'acefghiF'), (-1, 'abcefghiF'),
    (-1, 'abcdfhjF'), (+1, 'abcdfghjF'), (+1, 'acefhijF'), (-1, 'abcefhijF'),
    (+1, 'abcdefhijF'), (-1, 'abcdefghijF'),
]
# ---- reviewer hand transcription of the 12 CMI rows (A, B, conditioning) ----
CMI_ROWS = [
    ('b', 'g', 'acefhiDF'),
    ('b', 'F', 'acefhijD'),
    ('d', 'D', 'abcefhijF'),
    ('d', 'D', 'abcefghiF'),
    ('e', 'g', 'abcdfhjDF'),
    ('f', 'F', 'abcehiD'),
    ('g', 'i', 'abcdefhjDF'),
    ('g', 'D', 'abcdfhjF'),
    ('j', 'D', 'abcdefghiF'),
    ('j', 'D', 'acefhiF'),
    ('D', 'F', 'acefghi'),
    ('D', 'F', 'abcehi'),
]
NEG_WEIGHT = -2   # coefficient of I(D;F|X)


def clock():
    return subprocess.run(['/bin/date', '-u', '+%Y-%m-%dT%H:%M:%S.%NZ'], capture_output=True, text=True).stdout.strip()


def add(expr, key, coeff):
    expr[key] = expr.get(key, 0) + coeff
    if expr[key] == 0:
        del expr[key]


def H(vars_):
    return {frozenset(vars_): 1}


def scale(expr, k):
    return {s: k * c for s, c in expr.items()}


def plus(*exprs):
    out = {}
    for e in exprs:
        for s, c in e.items():
            add(out, s, c)
    return out


def cmi(a, b, cond):
    a, b, c = frozenset(a), frozenset(b), frozenset(cond)
    if a & b or a & c or b & c:
        raise ValueError(('OVERLAP', a, b, c))
    return plus(H(a | c), H(b | c), scale(H(a | b | c), -1), scale(H(c), -1))


def build_l3(terms):
    out = {}
    for coeff, labels in terms:
        add(out, frozenset(labels), coeff)
    return out


def build_rhs(rows, neg_weight):
    parts = [cmi(a, b, c) for a, b, c in rows]
    parts.append(scale(cmi('D', 'F', X), neg_weight))
    return plus(*parts)


def canon(s):
    return ''.join(v for v in X + AUX if v in s)


# ---- reviewer-written binding of the transcription to the frozen candidate text ----
def parse_candidate(text):
    begin = text.index('L_3={}')
    end = text.index(r'\end{aligned}', begin)
    body = re.sub(r'\s|&|\\\\', '', text[begin:end])
    body = body[body.index('={}') + 3:]
    found = re.findall(r'([+-]?)(\d*)H\(([a-jDF]+)\)', body)
    parsed = {}
    for sign, num, labels in found:
        c = int(num) if num else 1
        add(parsed, frozenset(labels), -c if sign == '-' else c)
    # CMI table rows: | n | `I(x;y | ...)` | `cond` |
    rows = re.findall(r'^\|\s*(\d+)\s*\|\s*`I\(([a-jDF]);([a-jDF]) \| \.\.\.\)`\s*\|\s*`([a-jDF,]+)`\s*\|\s*$', text, flags=re.M)
    table = [(a, b, cond.replace(',', '')) for _, a, b, cond in rows]
    return parsed, len(found), table


def main():
    t0 = clock()
    raw = CAND.read_bytes()
    if sha256(raw).hexdigest() != CAND_SHA:
        raise SystemExit('CANDIDATE_HASH_MISMATCH')
    text = raw.decode('utf-8')
    parsed_l3, n_text_terms, table = parse_candidate(text)
    l3 = build_l3(L3_TERMS)

    receipt = {'candidate_sha256': CAND_SHA, 'clock_start_utc': t0}
    receipt['text_binding'] = {
        'latex_terms_found': n_text_terms,
        'latex_block_equals_hand_transcription': parsed_l3 == l3,
        'table_rows_found': len(table),
        'table_equals_hand_transcription': table == CMI_ROWS,
    }
    if not (parsed_l3 == l3 and table == CMI_ROWS and n_text_terms == 18 and len(table) == 12):
        raise SystemExit(('TEXT_BINDING_FAILED', receipt['text_binding']))

    # structural facts about L3
    receipt['l3_structure'] = {
        'distinct_terms': len(l3),
        'coefficient_sum': sum(l3.values()),
        'mixed_DF_terms': sum(1 for s in l3 if 'D' in s and 'F' in s),
        'terms_without_D_or_F': sum(1 for s in l3 if 'D' not in s and 'F' not in s),
        'terms_with_D_only': sum(1 for s in l3 if 'D' in s and 'F' not in s),
        'terms_with_F_only': sum(1 for s in l3 if 'F' in s and 'D' not in s),
        'all_terms_contain_background_ach': all(BACKGROUND <= s for s in l3),
        'max_abs_coefficient': max(abs(c) for c in l3.values()),
    }

    # the identity, exact
    rhs = build_rhs(CMI_ROWS, NEG_WEIGHT)
    # mixed-term bookkeeping before cancellation
    raw_mixed = {}
    for a, b, c in CMI_ROWS:
        for s, k in cmi(a, b, c).items():
            if 'D' in s and 'F' in s:
                raw_mixed[s] = raw_mixed.get(s, 0) + k
    for s, k in scale(cmi('D', 'F', X), NEG_WEIGHT).items():
        if 'D' in s and 'F' in s:
            raw_mixed[s] = raw_mixed.get(s, 0) + k
    receipt['identity'] = {
        'rhs_rows': {'CMI': len(CMI_ROWS), 'I(D;F|X)_weight': NEG_WEIGHT},
        'distinct_mixed_DF_subsets_appearing_before_cancellation': len(raw_mixed),
        'mixed_DF_subsets_surviving': sum(1 for v in raw_mixed.values() if v != 0),
        'L3_equals_rhs_exactly': l3 == rhs,
        'difference_terms': {canon(s): c for s, c in plus(l3, scale(rhs, -1)).items()},
    }
    if l3 != rhs:
        raise SystemExit(('IDENTITY_FAILED', receipt['identity']))

    # 9-variable contraction (remove background a,c,h; coefficient sum zero makes this exact)
    nine = {}
    for s, c in l3.items():
        if not BACKGROUND <= s:
            raise SystemExit(('BACKGROUND_MISSING', canon(s)))
        add(nine, s - BACKGROUND, c)
    nine_masks = {sum(1 << NINE_ORDER.index(v) for v in s): c for s, c in nine.items()}
    # the 9-variable identity with a,c,h deleted from every conditioning set
    nine_rows = [(a, b, ''.join(v for v in c if v not in BACKGROUND)) for a, b, c in CMI_ROWS]
    X9 = tuple(v for v in X if v not in BACKGROUND)
    rhs9 = plus(*[cmi(a, b, c) for a, b, c in nine_rows], scale(cmi('D', 'F', X9), NEG_WEIGHT))
    receipt['nine_variable_contraction'] = {
        'order': list(NINE_ORDER),
        'distinct_terms': len(nine),
        'coefficient_sum': sum(nine.values()),
        'mask_coefficients_sorted': sorted(nine_masks.items()),
        'nine_variable_identity_holds': nine == rhs9,
        'nine_variable_rows': [f'I({a};{b}|{c})' for a, b, c in nine_rows] + [f'{NEG_WEIGHT}*I(D;F|{"".join(X9)})'],
    }
    if nine != rhs9:
        raise SystemExit('NINE_VARIABLE_IDENTITY_FAILED')

    # ---- negative controls: each must break the identity ----
    controls = {}

    def expect_break(tag, l3_terms=L3_TERMS, rows=CMI_ROWS, w=NEG_WEIGHT):
        ok = build_l3(l3_terms) != build_rhs(rows, w)
        controls[tag] = 'rejected' if ok else 'ACCEPTED_UNEXPECTEDLY'
        if not ok:
            raise SystemExit(('CONTROL_FAILED', tag))

    t = list(L3_TERMS); t[0] = (+1, 'abcehi'); expect_break('altered_coefficient_sign_H(abcehi)', l3_terms=t)
    t = list(L3_TERMS); t[2] = (+1, 'abcdefghij'); expect_break('altered_coefficient_2_to_1_H(abcdefghij)', l3_terms=t)
    t = list(L3_TERMS); del t[12]; expect_break('removed_term_H(abcdfhjF)', l3_terms=t)
    for k in range(len(CMI_ROWS)):
        r = list(CMI_ROWS); removed = r.pop(k)
        expect_break(f'removed_CMI_row_{k+1}_I({removed[0]};{removed[1]}|{removed[2]})', rows=r)
    expect_break('independence_weight_-2_to_-1', w=-1)
    expect_break('independence_weight_-2_to_0', w=0)
    r = list(CMI_ROWS); r[5] = ('f', 'F', 'abcehijD'); expect_break('altered_conditioning_row6_add_j', rows=r)
    r = list(CMI_ROWS); r[0] = ('b', 'g', 'acefhiD'); expect_break('altered_conditioning_row1_drop_F', rows=r)
    r = list(CMI_ROWS); r[10] = ('D', 'F', 'abcehi'); expect_break('duplicated_row12_in_place_of_row11', rows=r)
    receipt['negative_controls'] = controls
    receipt['negative_control_count'] = len(controls)

    receipt['verdict_identity'] = 'EXACT_IDENTITY_HOLDS'
    receipt['script_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    receipt['clock_end_utc'] = clock()
    with OUT.open('x', encoding='utf-8') as fh:
        json.dump(receipt, fh, indent=1); fh.write('\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'nine_variable_contraction'}, indent=1))
    print('nine_variable_contraction:', json.dumps({k: v for k, v in receipt['nine_variable_contraction'].items() if k != 'mask_coefficients_sorted'}))
    print('nine masks:', receipt['nine_variable_contraction']['mask_coefficients_sorted'])


if __name__ == '__main__':
    main()
