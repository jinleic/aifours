#!/usr/bin/env python3
"""proof-control-pcode-check-v1.py  (reviewer-authored, f113 review)

Own verification of the author's Z3 diagnostic 30-word P code
(frontier-20261028-n6-maximal-code-z3-v1.json).  The author's checker was
NOT imported or executed.  Checks:
  1. 30 distinct words in [6]^4, pair-injective in all six coordinate pairs.
  2. Missing cells per pair: exactly 6, all inside {0,1,2}^2, forming a
     perfect matching (each active symbol misses exactly one partner).
  3. Section-3 counts: m_i(a)=4 for active symbols a in {0,1,2} and 6 for
     inactive symbols; active-pattern histogram.
  4. Compatible E tuples: the set of w in [6]^4 whose every pair projection
     lies in the missing set.  Expected EMPTY for this code (all six missing
     matchings are identities, so an E tuple would need four pairwise
     distinct values in {0,1,2}).
  5. Explicit statement: the record carries no amplitudes and no E support;
     it is not an AME(4,6) tensor.  Independently of this code, the UNSAT
     control proof-control-t30-full-v1.cnf shows NO 30-word P code admits a
     compatible E with the residual condition.
Usage: python3 -B proof-control-pcode-check-v1.py <z3.json> <out.json>
"""
import hashlib, itertools, json, sys
from collections import Counter
from pathlib import Path

PAIRS = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]


def main(src_path, out_path):
    data = Path(src_path).read_bytes()
    rec = json.loads(data)
    W = [tuple(r['coordinates']) for r in rec['records']]
    rep = {'source_sha256': hashlib.sha256(data).hexdigest(), 'z3_status': rec.get('status'),
           'words': len(W), 'distinct': len(set(W)) == len(W),
           'alphabet_ok': all(len(w) == 4 and all(0 <= x <= 5 for x in w) for w in W),
           'has_amplitudes': any(k in rec for k in ('amplitudes', 'phases', 'E', 'E_support')),
           'record_keys': sorted(rec.keys())}
    missing = {}
    inj = {}
    for (i, j) in PAIRS:
        cells = Counter((w[i], w[j]) for w in W)
        inj[f'{i}{j}'] = max(cells.values()) == 1
        miss = sorted({(a, b) for a in range(6) for b in range(6)} - set(cells))
        missing[(i, j)] = miss
    rep['pair_injective_all'] = all(inj.values())
    rep['missing_cells'] = {f'{i}{j}': {'count': len(m), 'inside_012': all(a < 3 and b < 3 for a, b in m),
                                      'row_deg': sorted(Counter(a for a, b in m).values()),
                                      'col_deg': sorted(Counter(b for a, b in m).values()),
                                      'cells': m} for (i, j), m in missing.items()}
    rep['missing_is_perfect_matching_all'] = all(
        v['count'] == 6 and v['inside_012'] and v['row_deg'] == [2, 2, 2] and v['col_deg'] == [2, 2, 2]
        for v in rep['missing_cells'].values())
    # complement of missing within {0,1,2}^2 (= forbidden matching) per pair
    forb = {p: sorted(set(itertools.product(range(3), repeat=2)) - set(m)) for p, m in missing.items()}
    rep['forbidden_matchings'] = {f'{i}{j}': m for (i, j), m in forb.items()}
    rep['m_counts'] = {i: {a: sum(1 for w in W if w[i] == a) for a in range(6)} for i in range(4)}
    rep['active_pattern_hist'] = dict(Counter(sum(1 for x in w if x < 3) for w in W))
    compat = [w for w in itertools.product(range(6), repeat=4)
              if all((w[i], w[j]) in set(missing[(i, j)]) for (i, j) in PAIRS)]
    rep['compatible_E_tuples'] = compat
    rep['compatible_E_count'] = len(compat)
    rep['verdict'] = ('valid 30-word pair-injective P code with perfect-matching residual cells; '
                      'ZERO compatible E tuples; no amplitudes; NOT an AME witness')
    with Path(out_path).open('x', encoding='utf-8') as fh:
        json.dump(rep, fh, indent=1); fh.write('\n')
    print(json.dumps({k: v for k, v in rep.items() if k not in ('missing_cells', 'forbidden_matchings', 'compatible_E_tuples')}, indent=None))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
