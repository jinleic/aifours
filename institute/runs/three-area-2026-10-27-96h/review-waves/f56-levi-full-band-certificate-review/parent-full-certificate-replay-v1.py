#!/usr/bin/env python3
"""Parent replay of inspected Kac quotient engines with coverage enforcement.

The mathematical source/ideal and full-Cartan proof is a separate obligation.
This calls existing independently-written author replay engines: it is NOT a
third implementation of their Lie algebra or exact elimination algorithms.
"""
import copy
import hashlib
import importlib.util
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody')
OUT = Path(__file__).with_name('parent-full-certificate-result-v1.json')
PFX = 'frontier-20261028-'
PINS = {
    '214-independent-replay.py': '02e8e0c0432f18b67edd7a75ad687e90599834d741f994a8c09100d8250a82f1',
    'horizontal-independent-replay.py': 'ab2643d44ed90e8679d34e40f67f8ea6b8fed83a74191a72efda0f2ed81e1e4f',
    'levi-critical-independent-replay.py': '4b79f8cb58e34a28fdd9c046e3cc91d4619c971bbc8d5c6e059ff1c54e79bae6',
    'levi-critical-minors-v1.json': '2c8796b67242f52ba63321bdf8e163138ed41594cf354c6f5547b465f401661b',
    'levi-critical-alternates-v1.json': '232fe13aec9be941681fa4251a535631a85bbd4cce55a8ca41abf8460bf5c980',
    '214-symbolic-minors-v1.json': '15ee23511638af13eaebe332c3dbad0ec194da1a4c9b59385c41436be4fe0683',
    'predecessor-certificates-v1.json': '39742fa183d9290835e25b29ab246a66e3065d1fecb1c2796210e59dbb8388c2',
    '221-horizontal-minors-v1.json': 'aa9f38f92f58303b20d021e4c7102572bdf8239246716ce43f695ea3f2e848d7',
    '222-horizontal-minors-v1.json': '94e2bac395862b645f1ef463546ad6e244021a3143e67aa22d59c5f0c30536b9',
    '223-horizontal-minors-v1.json': 'a4c58943bb39cd8624faa298ddb087596825db4ef6c183a2cd805ce2807310e2',
    '224-horizontal-minors-v1.json': '08725d2fdcd7b5738e677b04c2ba9b4cbfd374de49505ede4b967282414b91ba',
    '224-alternate-minors-v1.json': '46b037e9f5c5f2c57444e71c44200427a3acb55cc6cad14f1262aa01a6b61979',
}
CLASSES = set(itertools.product((1, 2, 3, '>=4'), repeat=2))
CRITICAL = {(3, 2, 4), (3, 3, 3), (3, 3, 4), (4, 4, 4)}
PREDECESSORS = {(2, 0, n) for n in range(1, 5)} | {(2, 1, n) for n in range(1, 4)}
CRITICAL_ALT = {((3, 2, 4), '>=4', 3), ((3, 2, 4), '>=4', '>=4'), ((4, 4, 4), '>=4', '>=4')}
CENTRAL_ALT = {('>=4', 3), ('>=4', '>=4')}


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / (PFX + filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def key(case):
    return case['r_class'], case['s_class']


def require_classes(cases):
    if len(cases) != 16 or {key(c) for c in cases} != CLASSES:
        raise ValueError('CLASS_SET')


def polynomial(case, size):
    terms = case['determinant_coefficients']
    powers = [(t['x_power'], t['y_power']) for t in terms]
    if not terms or len(set(powers)) != len(powers):
        raise ValueError('POLYNOMIAL_TERMS')
    if any(type(e) is not int or e < 0 or e > size for pair in powers for e in pair):
        raise ValueError('POLYNOMIAL_DEGREE')
    if any((case['r_class'] != '>=4' and x) or (case['s_class'] != '>=4' and y) for x, y in powers):
        raise ValueError('INACTIVE_VARIABLE')
    coef = [Fraction(t['coefficient']) for t in terms]
    if (0, 0) not in powers or not coef[powers.index((0, 0))]:
        raise ValueError('CONSTANT')
    if not (all(c > 0 for c in coef) or all(c < 0 for c in coef)):
        raise ValueError('SIGN')


def main():
    if OUT.exists():
        raise FileExistsError(OUT)
    data = {}
    for filename, expected in PINS.items():
        raw = (ROOT / (PFX + filename)).read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected:
            raise ValueError('HASH ' + filename)
        if filename.endswith('.json'):
            data[filename] = json.loads(raw)
    full = load_module('parent_rectangle', '214-independent-replay.py')
    hor = load_module('parent_horizontal', 'horizontal-independent-replay.py')
    crit = load_module('parent_critical', 'levi-critical-independent-replay.py')
    records = []
    polynomials = 0

    def record(kind, degree, cases, replay, size_key):
        nonlocal polynomials
        require_classes(cases)
        checked = []
        for case in cases:
            if case['status'] not in ('ZERO_SOURCE', 'ZERO_HORIZONTAL_KERNEL'):
                polynomial(case, case[size_key])
                polynomials += 1
            checked.append(replay(case))
        count = sum(x.get('determinants', x.get('determinant_checks', 0)) for x in checked)
        records.append({'kind': kind, 'degree': list(degree), 'classes': checked, 'determinants': count})
        print('PASS', kind, degree, '16 exact classes,', count, 'determinants', flush=True)

    original = data['levi-critical-minors-v1.json']
    blocks = original['degrees']
    if len(blocks) != 4 or {tuple(b['degree']) for b in blocks} != CRITICAL:
        raise ValueError('CRITICAL_DEGREES')
    alt_rows = data['levi-critical-alternates-v1.json']['cases']
    alt = {(tuple(x['degree']), *key(x['case'])): x['case'] for x in alt_rows}
    if len(alt_rows) != 3 or set(alt) != CRITICAL_ALT:
        raise ValueError('CRITICAL_ALT_SET')
    for block in blocks:
        degree = tuple(block['degree'])
        require_classes(block['cases'])
        cases = [alt.get((degree, *key(c)), c) for c in block['cases']]
        record('critical', degree, cases, lambda c: crit.replay(degree, c), 'horizontal_kernel_dim')

    selected = data['214-symbolic-minors-v1.json']
    if tuple(selected['selected_degree']) != (2, 1, 4):
        raise ValueError('SELECTED_DEGREE')
    full.ALPHA = (2, 1, 4)
    record('rectangle_full', full.ALPHA, selected['cases'], full.replay, 'quotient_source_dim')

    pred = data['predecessor-certificates-v1.json']['degrees']
    if len(pred) != 7 or {tuple(x['degree']) for x in pred} != PREDECESSORS:
        raise ValueError('PREDECESSOR_DEGREES')
    for block in pred:
        full.ALPHA = tuple(block['degree'])
        record('rectangle_predecessor', full.ALPHA, block['cases'], full.replay, 'quotient_source_dim')

    for n in (1, 2, 3, 4):
        block = data[f'22{n}-horizontal-minors-v1.json']
        degree = tuple(block['degree'])
        if degree != (2, 2, n):
            raise ValueError('CENTRAL_DEGREE')
        cases = block['cases']
        if n == 4:
            replacement = data['224-alternate-minors-v1.json']['cases']
            central_alt = {key(c): c for c in replacement}
            if len(replacement) != 2 or set(central_alt) != CENTRAL_ALT:
                raise ValueError('CENTRAL_ALT_SET')
            cases = [central_alt.get(key(c), c) for c in cases]
        repaired = []
        for case in cases:
            if case['status'] == 'ZERO_HORIZONTAL_KERNEL' and 'source_basis_lyndon_words' not in case:
                r0, s0 = (4 if v == '>=4' else v for v in key(case))
                combined = hor.ind.ReducedSpace(hor.ind.formal_ideal_generators(degree, r0, s0))
                labels = [w for w in hor.ind.words(degree) if hor.ind.lyndon(w) and combined.insert(hor.ind.standard_bracket(w))]
                case = {**case, 'source_basis_lyndon_words': labels}
            repaired.append(case)
        record('rectangle_horizontal', degree, repaired, lambda c: hor.replay(degree, c), 'horizontal_kernel_dim')

    controls = {}
    try:
        require_classes(selected['cases'][:-1])
    except ValueError as exc:
        controls['missing_class'] = str(exc) == 'CLASS_SET'
    try:
        require_classes([selected['cases'][0]] * 16)
    except ValueError as exc:
        controls['duplicate_classes'] = str(exc) == 'CLASS_SET'
    sample = copy.deepcopy(next(c for c in selected['cases'] if c['status'] != 'ZERO_SOURCE'))
    sample['determinant_coefficients'][0]['x_power'] = sample['quotient_source_dim'] + 1
    try:
        polynomial(sample, sample['quotient_source_dim'])
    except ValueError as exc:
        controls['degree_bound'] = str(exc) == 'POLYNOMIAL_DEGREE'
    full.ALPHA = (2, 1, 4)
    sample = copy.deepcopy(next(c for c in selected['cases'] if key(c) == (1, 3)))
    sample['determinant_coefficients'][0]['coefficient'] = '4'
    try:
        full.replay(sample)
    except AssertionError as exc:
        controls['wrong_minor'] = bool(exc.args and isinstance(exc.args[0], tuple) and exc.args[0][0] == 'determinant polynomial mismatch')
    if set(controls) != {'missing_class', 'duplicate_classes', 'degree_bound', 'wrong_minor'} or not all(controls.values()):
        raise ValueError('CONTROL ' + str(controls))
    count = sum(len(b['classes']) for b in records)
    determinants = sum(b['determinants'] for b in records)
    if (count, determinants, polynomials) != (256, 760, 144):
        raise ValueError('TOTALS ' + str((count, determinants, polynomials)))
    result = {'verdict': 'PASS', 'input_sha256': PINS, 'degree_class_records': count,
              'exact_determinants': determinants, 'enforced_nonzero_polynomials': polynomials,
              'controls': controls, 'blocks': records,
              'scope': 'Parent execution of existing independent replay engines with new exact class/degree/alternate/polynomial input checks. Not an independent Lie/linear-algebra implementation, physical/source theorem proof or formal proof.'}
    text = json.dumps(result, indent=2, sort_keys=True) + '\n'
    with OUT.open('x', encoding='utf-8') as f:
        f.write(text)
    print('PASS all', count, 'classes;', determinants, 'exact determinants;', polynomials, 'degree-bounded one-sign polynomials;', controls, flush=True)


if __name__ == '__main__':
    main()
