#!/usr/bin/env python3
"""Replay all three central predecessor symbolic horizontal-kernel certificates."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('horizontal_replay', ROOT / 'frontier-20261028-horizontal-independent-replay.py')
replay = importlib.util.module_from_spec(spec)
spec.loader.exec_module(replay)


def main():
    results = []
    for name in ('221', '222', '223'):
        src = json.loads((ROOT / f'frontier-20261028-{name}-horizontal-minors-v1.json').read_text(encoding='utf-8'))
        assert len(src['cases']) == 16 and src['all_classes_covered']
        cases = []
        for case in src['cases']:
            if case['status'] == 'ZERO_HORIZONTAL_KERNEL':
                # These producer records omit complement labels. Construct one
                # independently before asking the replay to verify its rank.
                degree = tuple(src['degree'])
                r = 4 if case['r_class'] == '>=4' else case['r_class']
                s = 4 if case['s_class'] == '>=4' else case['s_class']
                combined = replay.ind.ReducedSpace(
                    replay.ind.formal_ideal_generators(degree, r, s))
                labels = []
                for word in replay.ind.words(degree):
                    if replay.ind.lyndon(word) and combined.insert(
                            replay.ind.standard_bracket(word)):
                        labels.append(word)
                case = {**case, 'source_basis_lyndon_words': labels}
            cases.append(replay.replay(src['degree'], case))
        results.append({'degree': src['degree'], 'cases': cases,
                        'all_classes_passed': True,
                        'determinant_evaluations': sum(c['determinant_checks'] for c in cases)})
    out = ROOT / 'frontier-20261028-central-predecessor-replay-v1.json'
    if out.exists(): raise FileExistsError(out)
    out.write_text(json.dumps({'degrees': results, 'total_classes': 48,
                               'determinant_evaluations': sum(r['determinant_evaluations'] for r in results),
                               'not_a_formal_proof_or_external_review': True}, indent=2) + '\n', encoding='utf-8')
    print('PASS: 3 degrees, 48 parameter classes;',
          sum(r['determinant_evaluations'] for r in results), 'determinants;', out.name)


if __name__ == '__main__': main()
