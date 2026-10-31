#!/usr/bin/env python3
"""Verify a two-CMI exact obstruction to one partial-point extension."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-source-closure-primal-frozen.json'
OUTPUT=ROOT/'frontier-20261028-extension-two-cmi-check-result.json'
EXPECTED='97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec'


def main():
    raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    rows=json.loads(raw)['primal_values']
    h={frozenset(row['entropy_variables']):Fraction(row['value']) for row in rows}
    if len(h)!=len(rows):raise ValueError('DUPLICATE')
    K=frozenset(('a','b','c','d','e','g','h'))
    dp="d'1";ep="e'1";f='f'
    def H(*new):return h[K|set(new)]
    unknown=K|{dp,f}
    if unknown in h:raise ValueError('UNKNOWN_ALREADY_SPECIFIED')
    upper=H(f)+H(dp)-H()
    lower=H(dp,f,ep)+H(dp)-H(dp,ep)
    if upper!=Fraction(35,92):raise ValueError(('UPPER',str(upper)))
    if lower!=Fraction(2057,276):raise ValueError(('LOWER',str(lower)))
    gap=lower-upper
    if gap!=Fraction(488,69) or gap<=0:raise ValueError(('GAP',str(gap)))
    coordinates={'.'.join(sorted(k)):str(v) for k,v in h.items()
                 if k in (K,K|{f},K|{dp},K|{dp,ep},K|{dp,f,ep})}
    out={'partial_point_sha256':EXPECTED,'base_conditioning_K':sorted(K),
         'unknown_entropy_variables':sorted(unknown),'unknown_absent_from_frozen_point':True,
         'known_entropy_coordinates':coordinates,
         'upper_CMI':'I(f; d\'1 | K) >= 0',
         'upper_bound_expression':'H(K f)+H(K d\'1)-H(K)', 'upper_exact':str(upper),
         'lower_CMI':'I(f; e\'1 | K d\'1) >= 0',
         'lower_bound_expression':'H(K d\'1 f e\'1)+H(K d\'1)-H(K d\'1 e\'1)',
         'lower_exact':str(lower),'gap_lower_minus_upper':str(gap),
         'limits':'Disproves extension of this particular partial point to the source second-branch Shannon cone. It does not exclude another extension of its original-variable projection, nor prove an R-minus bound.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
