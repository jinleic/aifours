#!/usr/bin/env python3
"""Generate symbolic full-column minors for all new (2,b,n) predecessors.

The first coordinate is at most two, the second at most one.  The
previously proved horizontal-a<=1 rectangle supplies the other predecessors.
All parameter classes are complete at alpha_3<=4.  Each result is conditional
on exact replay and the accompanying general basis/ideal correctness proof.
"""
import importlib.util
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('minors', ROOT / 'frontier-20261028-symbolic-minors.py')
minors = importlib.util.module_from_spec(spec)
spec.loader.exec_module(minors)


def main():
    classes = (1, 2, 3, '>=4')
    degrees = [(2, 0, n) for n in range(1, 5)] + [(2, 1, n) for n in range(1, 4)]
    results = []
    for degree in degrees:
        cases = [minors.case(degree, r, s) for r, s in itertools.product(classes, repeat=2)]
        results.append({
            'degree': degree,
            'cases': cases,
            'all_parameter_classes_algebraically_covered': all(
                c['status'] in ('ZERO_SOURCE', 'CERTIFIED_ONE_SIGN') for c in cases),
        })
    out = ROOT / 'frontier-20261028-predecessor-certificates-v1.json'
    if out.exists():
        raise FileExistsError(out)
    out.write_text(json.dumps({'degrees': results, 'not_a_formal_proof': True}, indent=2) + '\n', encoding='utf-8')
    covered = sum(d['all_parameter_classes_algebraically_covered'] for d in results)
    print(f'degrees={len(results)} fully-one-signed-or-zero={covered}; {out.name}')


if __name__ == '__main__':
    main()
