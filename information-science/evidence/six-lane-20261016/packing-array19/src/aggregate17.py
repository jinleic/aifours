#!/usr/bin/env python3
"""Add ONLY the exact parent-accepted B3 structural row to immutable aggregate16.
No solver predicate change. M2_certified/M2_solver_checked_cases retain solver-only counts; M2_resolved_cases adds
an independently source-bound exact structural exclusion, separately exposed. All other empty covers stay pending.
"""
import contextlib
import io
import json
import os

import aggregate16 as BASE
import structural_b3_acceptance as STRUCTURAL

LANE = BASE.LANE
TAG = 'ms09_s00003'


def apply_structural(out):
    result = STRUCTURAL.verify()
    out['structural_parent_accepted_rows'] = []
    for p in out['per_multiset'].values():
        p['M2_solver_checked_cases'] = p['M2_certified']
        p['M2_structural_parent_math_cases'] = 0
        p['M2_resolved_cases'] = p['M2_certified']
    if result['accepted']:
        result['contributes_new_case'] = False
        if TAG in out['M2_open_tags']:
            candidates = [r for r in out['structural_empty_covers_pending_parent']
                          if r.get('tag') == TAG and r.get('multiset') == 9 and r.get('b_index') == 3
                          and r.get('complete_placement_denominator') == 0
                          and r.get('list_sha256') == STRUCTURAL.EXPECTED['empty_list_receipt']['sha256']]
            if len(candidates) != 1 or out['M2_open_tags'].count(TAG) != 1:
                result = STRUCTURAL.pending('base_case_identity', 'exact pending B3 row/open tag is not unique and bound')
            else:
                out['M2_open_tags'].remove(TAG)
                out['M2_open'] = len(out['M2_open_tags'])
                out['structural_empty_covers_pending_parent'].remove(candidates[0])
                p = out['per_multiset']['ms09']
                p['M2_structural_parent_math_cases'] = 1
                p['M2_resolved_cases'] += 1
                if TAG not in out['M1_open_tags']:
                    p['both'] += 1
                result['contributes_new_case'] = True
    if result['accepted']:
        out['structural_parent_accepted_rows'].append(result)
    else:
        out['structural_b3_binding_failure'] = result
    out['M2_solver_checked_cases'] = sum(p['M2_solver_checked_cases'] for p in out['per_multiset'].values())
    out['M2_structural_parent_math_cases'] = sum(p['M2_structural_parent_math_cases'] for p in out['per_multiset'].values())
    out['M2_resolved_cases'] = sum(p['M2_resolved_cases'] for p in out['per_multiset'].values())
    out['M2_count_semantics'] = ('M2_certified and M2_solver_checked_cases are solver-only; M2_resolved_cases also includes '
                                 'the separately bound exact parent structural case. both counts M1 and either M2 route; '
                                 'no structural row claims solver invocation/DRAT hash/s VERIFIED. Global bridge audit pending.')
    return out


def main():
    with contextlib.redirect_stdout(io.StringIO()):
        BASE.main()
    with open(os.path.join(LANE, 'STATUS16_BASE.json')) as f:
        out = apply_structural(json.load(f))
    with open(os.path.join(LANE, 'STATUS17_BASE.json'), 'w') as f:
        json.dump(out, f, indent=1)
    print(json.dumps({k:v for k,v in out.items() if not k.endswith('_tags') and k != 'uncertified_list'}, indent=1))


if __name__ == '__main__':
    main()
