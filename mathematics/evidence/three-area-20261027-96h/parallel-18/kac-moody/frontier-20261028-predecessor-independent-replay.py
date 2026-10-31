#!/usr/bin/env python3
"""Replay symbolic predecessor certificates by independent exact word spans."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('independent', ROOT / 'frontier-20261028-214-independent-replay.py')
independent = importlib.util.module_from_spec(spec)
spec.loader.exec_module(independent)


def main():
    data = json.loads((ROOT / 'frontier-20261028-predecessor-certificates-v1.json').read_text(encoding='utf-8'))
    outputs = []
    for item in data['degrees']:
        independent.ALPHA = tuple(item['degree'])
        rows = [independent.replay(case) for case in item['cases']]
        assert len(rows) == 16
        outputs.append({'degree': item['degree'], 'cases': rows,
                        'all_classes_passed': True,
                        'determinant_evaluations': sum(row['determinant_checks'] for row in rows)})
    assert len(outputs) == 7
    out = ROOT / 'frontier-20261028-predecessor-independent-replay-v1.json'
    if out.exists():
        raise FileExistsError(out)
    out.write_text(json.dumps({'degrees': outputs,
                               'total_classes': 112,
                               'determinant_evaluations': sum(x['determinant_evaluations'] for x in outputs),
                               'not_a_formal_proof_or_external_review': True}, indent=2) + '\n', encoding='utf-8')
    print('PASS: 7 degrees, 112 parameter classes;',
          sum(x['determinant_evaluations'] for x in outputs), 'determinants;', out.name)


if __name__ == '__main__':
    main()
