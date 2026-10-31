#!/usr/bin/env python3
"""Stronger fifth-boundary certificate: exact positivity, not Hensel lifting.

For each of fourteen boundary lines, divide both specialized minor polynomials
by their integer gcd g. Check every coefficient of g(z-1) has one weak sign and
its constant is nonzero. Verify quotient coprimality by an explicit mod-prime
Bezout identity with both degrees preserved. Hence the two minors never vanish
simultaneously at any REAL remaining coordinate >=-1.
"""
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location('boundary_source', ROOT / 'frontier-20261028-level6-boundary-five.py')
b = importlib.util.module_from_spec(sp)
sp.loader.exec_module(b)
f = b.f


def main():
    out = ROOT / 'frontier-20261028-level6-boundary-five-positive-v1.json'
    if out.exists():
        raise FileExistsError(out)
    pins, report = [], []
    for ab in ('22', '32', '33', '43', '44', '55', '66'):
        A, B = b.pair(ab, pins)
        rows = []
        for idx in (0, 1):
            aa, bb = f.axis_polynomial(A, idx, -1), f.axis_polynomial(B, idx, -1)
            g = aa.gcd(bb)
            qa, ra = divmod(aa, g)
            qb, rb = divmod(bb, g)
            assert not ra and not rb and g * qa == aa and g * qb == bb
            shifted = g(f.flint.fmpz_poly([-1, 1]))
            cs = list(shifted)
            assert shifted[0] and (all(c >= 0 for c in cs) or all(c <= 0 for c in cs))
            p = 1009
            while True:
                if f.flint.fmpz(p).is_prime() and qa.leading_coefficient() % p and qb.leading_coefficient() % p:
                    am = f.flint.nmod_poly([int(c % p) for c in qa], p)
                    bm = f.flint.nmod_poly([int(c % p) for c in qb], p)
                    h, u, v = am.xgcd(bm)
                    if h == 1:
                        assert u * am + v * bm == 1
                        break
                p += 1
            rows.append({'fixed_variable_index': idx, 'fixed_value': -1, 'other_coordinate_lower_bound': -1,
                         'gcd': [str(c) for c in g], 'quotient_A': [str(c) for c in qa], 'quotient_B': [str(c) for c in qb],
                         'gcd_shifted_by_minus_one': [str(c) for c in shifted],
                         'prime': p, 'bezout_u': [int(c) for c in u], 'bezout_v': [int(c) for c in v]})
        report.append({'degree': [int(ab[0]), int(ab[1]), 6], 'boundaries': rows})
    packet = {'variables': 'x=r-6,y=s-6', 'inputs': pins, 'types': report,
              'status': 'ALL_FOURTEEN_BOUNDARY_LINES_HAVE_NO_SIMULTANEOUS_REAL_MINOR_ZERO_FOR_OTHER_COORDINATE_GE_MINUS_ONE',
              'source_loader_sha256': hashlib.sha256((ROOT / 'frontier-20261028-level6-boundary-five.py').read_bytes()).hexdigest(),
              'scope': 'polynomial certificate only; actual-source identification on r=5/s=5 is a separate written argument'}
    with out.open('x') as stream:
        json.dump(packet, stream, indent=2)
        stream.write('\n')
    print('PASS fourteen real boundary lines by positive shifted gcd and explicit modular Bezout', out.name)


if __name__ == '__main__':
    main()
