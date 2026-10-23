#!/usr/bin/env python3
"""Assemble the exact power-of-two sub-question certificate from local searches."""
import json
from pathlib import Path


def main():
    sources = ['evidence/power-two-factors-small.json',
               'evidence/power-two-factor-t8.json',
               'evidence/power-two-factors-t9plus.json']
    found = {}
    for source in sources:
        for row in json.loads(Path(source).read_text())['rows']:
            if row['proper_factor'] is not None:
                found[row['t']] = row
    rows = []
    t = 3
    while t in found:
        a = 3**t; q = found[t]['proper_factor']
        assert 1 < q < (1 << (2*a))+(1 << a)+1
        assert ((1 << (2*a))+(1 << a)+1) % q == 0
        r = pow(2, a, q)
        assert (r*r+r+1) % q == 0
        rows.append(dict(t=t, a=a, proper_factor=q, two_to_a_mod_factor=r))
        t += 1
    result = dict(max_exponent_exclusive=3**t, first_unresolved_t=t,
                  exponent_reduction_proof='evidence/POWER-TWO-LEMMA.md',
                  excluded_small_exponent=9,
                  small_collision_source='evidence/controls.json',
                  factors=rows,
                  statement='For every integer a with 3<a<%d, p=2^(2a)+2^a+1 is composite except a=9, whose multiplicative subgroup D is verified not planar. This is only the power-of-two order family.' % (3**t),
                  novelty='unknown')
    Path('evidence/power-two-family.json').write_text(json.dumps(result, indent=2)+'\n')
    broken = json.loads(json.dumps(result))
    broken['factors'][0]['proper_factor'] += 1
    Path('evidence/power-two-family-broken.json').write_text(json.dumps(broken, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
