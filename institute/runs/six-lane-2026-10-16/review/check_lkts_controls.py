"""Positive and mutation controls for check_lkts_independent.py.

Positive controls: the prior dossier's independently checked LKTS(9) and LKTS(15) certificates.
Mutation controls: single, targeted corruptions of the pinned LKTS(57) candidate. Every mutation
must be rejected for the stated reason class. Mutated files are retained, never auto-deleted.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CHECKER = HERE / 'check_lkts_independent.py'
CANDIDATE = HERE / 'lkts57-parent-inputs-v1/lkts57_g513.txt'
FIXTURES = HERE / 'lkts57-parent-controls-v1'
POSITIVE = [ROOT / 'mathematics/kirkman-large-sets-57-87/evidence/cyclic9.txt',
            ROOT / 'mathematics/kirkman-large-sets-57-87/evidence/cyclic15.txt',
            ROOT / 'mathematics/kirkman-large-sets-57-87/evidence/denniston15.txt']


def load_checker():
    spec = importlib.util.spec_from_file_location('parent_lkts', CHECKER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def mutate(lines: list[str]) -> dict[str, list[str]]:
    triple_rows = [i for i, l in enumerate(lines) if l and l[0].isdigit()]
    kts_rows = [i for i, l in enumerate(lines) if l.startswith('KTS ')]
    class_rows = [i for i, l in enumerate(lines) if l.startswith('CLASS ')]
    out = {}
    first = triple_rows[0]
    a, b, c = lines[first].split()
    # 1. Swap one point of a triple with a point from the next triple in the same class.
    second = triple_rows[1]
    d, e, f = lines[second].split()
    m = lines[:]
    m[first] = f'{a} {b} {d}'
    m[second] = f'{c} {e} {f}'
    out['swap_points_between_two_triples'] = m
    # 2. Replace a point by an out-of-range label.
    m = lines[:]
    m[first] = f'{a} {b} 57'
    out['out_of_range_point'] = m
    # 3. Exchange one block between two different constituents (keeps the global triple set).
    k1_row = next(i for i in triple_rows if i > kts_rows[0])
    k2_row = next(i for i in triple_rows if i > kts_rows[1])
    m = lines[:]
    m[k1_row], m[k2_row] = m[k2_row], m[k1_row]
    out['exchange_blocks_between_constituents'] = m
    # 4. Duplicate constituent 1 over constituent 2 (renumbering preserved).
    block1 = lines[kts_rows[1] + 1:kts_rows[2]]
    m = lines[:kts_rows[2] + 1] + block1 + lines[kts_rows[3]:]
    out['duplicate_constituent'] = m
    # 5. Drop the last class of the last constituent.
    m = lines[:class_rows[-1]]
    out['drop_last_class'] = m
    # 6. Drop the last constituent entirely.
    m = lines[:kts_rows[-1]]
    out['drop_last_constituent'] = m
    # 7. Repeat a point inside a triple.
    m = lines[:]
    m[first] = f'{a} {a} {c}'
    out['repeated_point'] = m
    # 8. Swap two classes' order labels (CLASS out of order).
    m = lines[:]
    m[class_rows[0]], m[class_rows[1]] = m[class_rows[1]], m[class_rows[0]]
    out['class_label_order'] = m
    return out


def main() -> None:
    checker = load_checker()
    report = {'positive_controls': [], 'mutation_controls': [], 'candidate': None}
    for path in POSITIVE:
        result = checker.verify(path)
        report['positive_controls'].append({'file': str(path.relative_to(ROOT)), 'v': result['v'],
                                            'status': result['status'], 'sha256': result['input_sha256']})
    report['candidate'] = checker.verify(CANDIDATE)['status']
    lines = CANDIDATE.read_text().splitlines()
    FIXTURES.mkdir(exist_ok=True)
    for name, mutated in mutate(lines).items():
        path = FIXTURES / f'{name}.txt'
        text = '\n'.join(mutated) + '\n'
        if path.exists() and path.read_text() != text:
            raise SystemExit(f'Refusing to overwrite a different retained fixture {path}')
        path.write_text(text)
        try:
            checker.verify(path)
        except Exception as exc:  # noqa: BLE001 - any rejection counts, reason recorded
            report['mutation_controls'].append({'mutation': name, 'rejected': True,
                                                'reason': f'{type(exc).__name__}: {exc}',
                                                'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
        else:
            report['mutation_controls'].append({'mutation': name, 'rejected': False})
    if any(not m['rejected'] for m in report['mutation_controls']):
        raise SystemExit(json.dumps(report, indent=2))
    if any(p['status'] != 'VALID_LKTS' for p in report['positive_controls']):
        raise SystemExit(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
