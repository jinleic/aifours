#!/usr/bin/env python3
"""Re-enumerate five-row subcases via the separately written DFS solver.

The five-row subsets are rebuilt directly from the source, without loading the
breadth-first result. Each case uses the independent prefix-DFS/MRV list solver
and a fresh named output. The BFS census is read only after all DFS cases.
"""
import hashlib
import importlib.util
import itertools
import json
import sys
import time
from pathlib import Path

N = 11
helper_path = Path(__file__).with_name('frontier-20261028-exact-partial-completion-v1.py')
spec = importlib.util.spec_from_file_location('independent_partial_solver', helper_path)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


def compatible(rows):
    if len(set(r[0] for r in rows)) != len(rows) or len(set(r[-1] for r in rows)) != len(rows):
        return False
    for distance in (1,2):
        events = [(row[i],row[i+distance]) for row in rows for i in range(N-distance)]
        if len(events) != len(set(events)):
            return False
    return True


def main(argv):
    if len(argv) != 5:
        raise ValueError('usage: SCRIPT SOURCE FIRST_CENSUS OUTPUT_PREFIX AGGREGATE_JSON')
    source, first_census, prefix, aggregate = map(Path, argv[1:])
    raw = source.read_bytes()
    rows = json.loads(raw)['rows']
    if len(rows) != N or any(sorted(r) != list(range(N)) for r in rows):
        raise ValueError('invalid input rows')
    start = time.monotonic()
    subsets = [idx for idx in itertools.combinations(range(N),5)
               if compatible([rows[i] for i in idx])]
    observed = []
    for ordinal, subset in enumerate(subsets,1):
        index_list = ','.join(str(i+1) for i in subset)
        output = prefix.with_name(prefix.name + '-%02d.json' % ordinal)
        helper.main([str(helper_path), str(source), str(output), index_list,
                     '3', '400000', '100000'])
        payload = output.read_bytes()
        case = json.loads(payload)
        observed.append({'fixed_rows_1based': [i+1 for i in subset],
                         'status': case['status'], 'enumeration_complete': case['enumeration_complete'],
                         'exact_cover_complete': case['exact_cover_complete'],
                         'eligible_rows': case['eligible_row_count'], 'cover_nodes': case['cover_nodes'],
                         'output': str(output), 'output_sha256': hashlib.sha256(payload).hexdigest()})
        if case['status'] == 'candidate_witness_requires_independent_check':
            break
    # Compare only after all independently reconstructed subsets/cases have run.
    census_raw = first_census.read_bytes()
    census = json.loads(census_raw)
    if census['source_sha256'] != hashlib.sha256(raw).hexdigest():
        raise AssertionError('source hashes differ')
    first = {tuple(c['fixed_rows_1based']): c for c in census['cases']}
    matching = True
    for case in observed:
        other = first.get(tuple(case['fixed_rows_1based']))
        if other is None or other['eligible_rows'] != case['eligible_rows']:
            matching = False
        if (case['status'].startswith('no_completion_') and
                other is not None and other['status'] != 'no_completion_exhaustive'):
            matching = False
    complete_negative = (len(observed) == len(subsets) and all(
        c['enumeration_complete'] and c['exact_cover_complete'] and
        c['status'].startswith('no_completion_') for c in observed))
    out = {'source_sha256':hashlib.sha256(raw).hexdigest(),
           'helper_sha256':hashlib.sha256(helper_path.read_bytes()).hexdigest(),
           'compared_bfs_census_sha256':hashlib.sha256(census_raw).hexdigest(),
           'compatible_five_row_subsets':len(subsets), 'cases_run':len(observed),
           'all_exactly_excluded':complete_negative, 'all_case_counts_and_outcomes_match':matching,
           'cases':observed, 'elapsed_ms':round((time.monotonic()-start)*1000),
           'scope':'Exact row-string reuse from this candidate only; not an unrestricted no-go.'}
    with aggregate.open('x',encoding='utf-8') as stream:
        json.dump(out,stream,indent=2,sort_keys=True)
        stream.write('\n')
    print(json.dumps({k:out[k] for k in ('compatible_five_row_subsets','cases_run',
          'all_exactly_excluded','all_case_counts_and_outcomes_match','elapsed_ms')}))


if __name__ == '__main__':
    main(sys.argv)
