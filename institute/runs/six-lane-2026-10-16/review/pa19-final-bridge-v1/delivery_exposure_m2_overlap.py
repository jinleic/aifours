#!/usr/bin/env python3
"""Read-only follow-up to delivery-exposure-census-v1.json: for each M1 case whose counted coverage carries no
positive CNF-delivery evidence, classify the CURRENT independent M2 coverage of the same case (compare-map a_to_b;
m2skel_drat direct record, or m2part_drat split coverage) with the same evidence classes, plus the separately
pinned structural row ms09_b00003.  Live M2 trees are read at this instant (they are still growing); metadata only.
"""
import glob
import json
import os
import re
import subprocess
from collections import Counter

import delivery_exposure_census as C

LANE = C.LANE
HERE = os.path.dirname(os.path.abspath(__file__))


def m2_class(mi, bi):
    r = C.jl(os.path.join(LANE, 'cycle2', 'm2skel_drat', 'ms%02d_b%05d.json' % (mi, bi)))
    if C.certified(r):
        return 'direct:' + C.klass(r)
    d = os.path.join(LANE, 'cycle2', 'm2part_drat', 'ms%02d_b%05d' % (mi, bi))
    E = C.jl(os.path.join(d, 'ext.json'))
    if not E:
        return 'OPEN'
    n = E.get('num_placements')
    if n == 0:
        return 'STRUCTURAL-EMPTY' if (mi, bi) == (9, 3) else 'EMPTY-NOT-ACCEPTED'
    best = {}
    for f in sorted(glob.glob(os.path.join(d, 'batch_*.json'))):
        if f.endswith('_r2.json'):
            continue
        r = C.jl(f)
        if not C.certified(r):
            continue
        idx = r.get('indices') or []
        if 'multiset' in r and len(idx) == 2:
            idx = list(range(idx[0], idx[1] + 1))
        k = C.klass(r)
        rank = 0 if k in ('LRAT', 'REPLAY') else 1
        for i in idx:
            if i not in best or rank < best[i][0]:
                best[i] = (rank, k)
    if n is None or len(set(best) & set(range(n))) != n:
        return 'OPEN(partial split %d/%s)' % (len(set(best) & set(range(n or 0))), n)
    ks = Counter(k for _, k in best.values())
    return 'split:' + ('REPLAY' if set(ks) <= {'REPLAY', 'LRAT'} else 'MIXED' + json.dumps(dict(ks)))


def main():
    t = subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip()
    census = json.load(open(os.path.join(HERE, 'delivery-exposure-census-v1.json')))
    maps = {mi: json.load(open(os.path.join(LANE, 'cycle2', 'skel-b', 'compare-map-ms%02d.json' % mi)))['a_to_b']
            for mi in range(1, 10)}
    per, counts = {}, Counter()
    for tag in sorted(census['case_detail']):
        m = re.fullmatch(r'ms(\d\d)_s(\d+)', tag)
        mi, si = int(m.group(1)), int(m.group(2))
        bi = maps[mi][si]
        k = m2_class(mi, bi)
        per[tag] = {'b_index': bi, 'm2': k}
        counts[k.split('(')[0] if k.startswith('OPEN') else k] += 1
    out = {'recorded_at': t, 'input_census_sha256': C.hashlib.sha256(open(os.path.join(HERE, 'delivery-exposure-census-v1.json'), 'rb').read()).hexdigest(),
           'counts': dict(counts), 'per_case': per,
           'note': 'Live M2 state at recorded_at; REPLAY = staged rev11-15 with proof > 64 KiB; NONE classes as in v1.'}
    with open(os.path.join(HERE, 'delivery-exposure-m2-overlap-v1.json'), 'x') as f:
        json.dump(out, f, indent=1)
    print(json.dumps({'recorded_at': t, 'counts': dict(counts)}, indent=1))


if __name__ == '__main__':
    main()
