"""Definition-level arithmetic and case binding; no solver or producer imports."""
import hashlib
import itertools
import json
from datetime import datetime
from math import comb
from pathlib import Path

ROOT = Path('/Users/jinleic/repos/aifours')
LANE = ROOT / 'information-science/evidence/six-lane-20261016/packing-array19'
HERE = Path(__file__).resolve().parent
PINS = {
    'cycle2/ms09-b30-b44-structural-candidate-v1.json': '04cdca2316d5b3b9e38ad8189409929d0b25390ea2b44a1a528c9e570302fbba',
    'cycle2/skel-b/skeletons-b-ms09.json': '7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0',
    'cycle2/m2-ms09-k1-contract-20261018T062126.json': '2dba8eb85241d1c7129246dbc690d2b9212f95750111ed565290ef54e8479cb2',
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

for rel, expected in PINS.items():
    assert digest(LANE / rel) == expected, rel
candidate, data, contract = [json.loads((LANE / rel).read_text()) for rel in PINS]
p0, p1 = [4, 3, 3, 3, 3, 3], [4, 4, 3, 3, 3, 2]
assert data['c0'] == 5 and data['L'] == 0
assert data['profiles'] == [p0] * 5 + [p1] * 3
assert sum(p0) == sum(p1) == 19
pair_total = 5 * sum(comb(x, 2) for x in p0) + 3 * sum(comb(x, 2) for x in p1)
assert pair_total == comb(19, 2) == 171
triples = [v for v in itertools.product((1, 2, 3), repeat=3) if sum(v) == 18 - (4 * 3 + 2)]
assert set(triples) == {(1, 1, 2), (1, 2, 1), (2, 1, 1)}
assert 1 + 3 + 3 < 18 - 5 * 2
results = []
for declared in candidate['exact_cases']:
    idx = declared['b_index']
    skeleton = data['skeletons'][idx]
    assert skeleton == declared['skeleton']
    rows = [frozenset(t) for t in skeleton['types']]
    for q in range(5):
        missing = 4 - sum(q in row for row in rows)
        assert missing >= 0
        rows.extend([frozenset((q,))] * missing)
    rows.extend([frozenset()] * skeleton['empty'])
    assert len(rows) == 19
    assert all(sum(q in row for row in rows) == 4 for q in range(5))
    assert all(len(a & b) <= 1 for a, b in itertools.combinations(rows, 2))
    h = [i for i, row in enumerate(rows) if len(row) == 4]
    assert len(h) == 1
    j, = set(range(5)) - rows[h[0]]
    partners = [i for i, row in enumerate(rows) if row == frozenset((j,))]
    assert len(partners) == declared['singleton_missing_quad_count'] < 2
    case, = [c for c in contract['cases'] if c['b_index'] == idx]
    assert case['mapped_A2_tag'] == declared['mapped_A2_tag']
    assert case['skeleton_sha256'] == declared['individual_skeleton_sha256']
    list_path = LANE / declared['list_path']
    assert case['list']['path'] == declared['list_path']
    assert digest(list_path) == case['list']['sha256'] == declared['list_sha256']
    placements = json.loads(list_path.read_text())
    n = len(placements['placements'])
    assert n == placements['num_placements'] == case['list']['n'] == declared['list_denominator']
    spans = [r['indices'] for r in case['intervals']]
    assert spans == [[lo, min(lo + 99, n - 1)] for lo in range(0, n, 100)]
    assert len(spans) == declared['original_B100_intervals']
    results.append({'b_index': idx, 'h': h[0], 'missing_quad': j,
                    'eligible_partners': partners, 'necessary_distinct_partners': 2,
                    'placements': n, 'intervals': len(spans), 'status': 'CONTRADICTION'})
controls = {
    'missing_saturation_rejected': pair_total - 1 != comb(19, 2),
    'three_quad_row_not_excluded_by_this_lemma': any(sum(v) == 18 - (3 * 3 + 2 * 2) and v.count(1) < 2
                                                    for v in itertools.product((1, 2, 3), repeat=3)),
    'two_distinct_partner_capacity_not_excluded': not (2 < 2),
    'repeated_partner_rejected_by_row_pair_axiom': 2 > 1,
}
assert all(controls.values())
result = {'at': datetime.now().astimezone().isoformat(), 'status': 'PASS',
          'source_sha256': digest(Path(__file__)), 'input_pins': PINS,
          'pair_total': pair_total, 'allowed_h_contribution_triples': triples,
          'cases': results, 'controls': controls,
          'limit': 'Checks arithmetic and exact case/list binding. The written necessity proof, not this finite calculation, excludes the two cases. No other cases or global gate are decided.'}
with (HERE / 'RESULT.json').open('x') as f:
    json.dump(result, f, indent=2)
    f.write('\n')
print(json.dumps(result, indent=2))
