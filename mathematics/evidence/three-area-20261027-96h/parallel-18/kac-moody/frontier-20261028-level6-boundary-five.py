#!/usr/bin/env python3
"""Exact two-minor tests on r=5 or s=5, with the other parameter >=5.

At level six the node-3 relation modules first appearing at r=5/s=5 have
lowest degrees (1,0,6)/(0,1,6), of finite-Levi types (4,7)/(7,4), distinct from
the seven critical primitive types. The applicability of this representation
argument is WRITTEN separately; this script tests ONLY the corresponding free
pencil minors on x=-1 or y=-1, using x=r-6,y=s-6.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location('fast_pair_arithmetic', ROOT / 'frontier-20261028-level6-fast-pair.py')
f = importlib.util.module_from_spec(sp)
sp.loader.exec_module(f)


def read(name, pins):
    raw = (ROOT / name).read_bytes()
    pins.append({'file': name, 'sha256': hashlib.sha256(raw).hexdigest()})
    return json.loads(raw)


def polynomial(terms):
    data = {(t['x_power'], t['y_power']): Fraction(t['coefficient']) for t in terms}
    assert len(data) == len(terms)
    denominator = math.lcm(*(q.denominator for q in data.values()))
    integers = {mon: int(q * denominator) for mon, q in data.items()}
    content = math.gcd(*integers.values())
    return f.CTX.from_dict({mon: c // content for mon, c in integers.items()})


def pair(ab, pins):
    if ab == '22':
        A = read('frontier-20261028-level6-free-22-determinant-v1.json', pins)
        B = read('frontier-20261028-level6-226-two-minor-resultant-v1.json', pins)
        return polynomial(A['determinant_coefficients']), polynomial(B['P2_coefficients'])
    if ab in ('32', '66'):
        C = read(f'frontier-20261028-level6-{ab}6-two-minor-certificate-v1.json', pins)
        result = []
        for label in ('P1', 'P2'):
            # The serialized nonzero scalar has no effect on the zero set.
            assert Fraction(C['minor_factorizations'][label]['content']) != 0
            p = f.CTX.constant(1)
            for entry in C['minor_factorizations'][label]['factors']:
                p *= f.CTX.from_dict({(t['x_power'], t['y_power']): int(t['coefficient'])
                                     for t in entry['coefficients']})**entry['multiplicity']
            result.append(p)
        return tuple(result)
    A = read(f'frontier-20261028-level6-{ab}6-minor-baseline-v1.json', pins)
    B = read(f'frontier-20261028-level6-{ab}6-minor-seed1-v1.json', pins)
    assert A['pencil_sha256'] == B['pencil_sha256']
    return polynomial(A['coefficients']), polynomial(B['coefficients'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--types', nargs='+', default=['22', '32', '33', '43', '44', '55', '66'])
    ap.add_argument('--tag', required=True)
    args = ap.parse_args()
    out = ROOT / ('frontier-20261028-level6-boundary-five-' + args.tag + '-v1.json')
    if out.exists():
        raise FileExistsError(out)
    result, pins = [], []
    for ab in args.types:
        A, B = pair(ab, pins)
        entries = []
        for idx in (0, 1):
            aa = f.axis_polynomial(A, idx, -1)
            bb = f.axis_polynomial(B, idx, -1)
            assert aa and bb, 'identically-zero boundary minor needs another minor'
            g = aa.gcd(bb)
            assert g
            if g.degree() == 0:
                roots, cert = [], {'status': 'UNIT_GCD'}
            else:
                repeated = g.gcd(g.derivative())
                squarefree, rem = divmod(g, repeated)
                assert not rem and repeated * squarefree == g
                roots, cert = f.integer_root_certificate(squarefree, 1000)
            unresolved = [r for r in roots if r >= -1]
            entries.append({'fixed_variable': 'x' if idx == 0 else 'y', 'fixed_value': -1,
                            'other_variable_lower_bound': -1, 'minor_degrees': [aa.degree(), bb.degree()],
                            'gcd_coefficients_low_to_high': [str(c) for c in g], 'gcd_degree': g.degree(),
                            'all_integer_gcd_roots': roots, 'unresolved_integer_coordinates': unresolved,
                            'root_certificate': cert})
        result.append({'degree': [int(ab[0]), int(ab[1]), 6], 'boundaries': entries,
                       'status': 'BOTH_BOUNDARY_ROWS_FULL_COLUMN_RANK' if all(not e['unresolved_integer_coordinates'] for e in entries)
                                 else 'UNRESOLVED_CANDIDATE_POINTS'})
        print('BOUNDARY', ab, [(e['fixed_variable'], e['gcd_degree'], e['unresolved_integer_coordinates']) for e in entries], flush=True)
    status = 'ALL_SELECTED_BOUNDARY_ROWS_CERTIFIED' if all(e['status'] == 'BOTH_BOUNDARY_ROWS_FULL_COLUMN_RANK' for e in result) else 'CANDIDATE_POINTS_REMAIN'
    with out.open('x') as stream:
        json.dump({'variables': 'x=r-6,y=s-6', 'inputs': pins, 'types': result, 'status': status,
                   'scope': 'exact minor-polynomial boundary test; actual-source transport and independent full verification are separate'}, stream, indent=2)
        stream.write('\n')
    print('DONE', status, out.name)


if __name__ == '__main__':
    main()
