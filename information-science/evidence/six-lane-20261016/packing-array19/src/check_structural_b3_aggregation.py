#!/usr/bin/env python3
"""Exact-case in-memory presentation controls and nine single-guard mutants. Not solver/proof mutation checks.
Run behind with_token15. No scientific input changes; output is one unique metadata receipt with x-mode.
"""
import copy
import hashlib
import json
import time
import types
from pathlib import Path

import aggregate17 as A


def case():
    return {'per_multiset': {'ms09': {'cases': 1, 'M1_certified': 1, 'M2_certified': 0, 'both': 0}},
            'M1_open_tags': [], 'M2_open_tags': [A.TAG], 'M2_open': 1,
            'structural_empty_covers_pending_parent': [{'tag': A.TAG, 'multiset': 9, 'b_index': 3,
                'complete_placement_denominator': 0,
                'list_sha256': A.STRUCTURAL.EXPECTED['empty_list_receipt']['sha256']}]}


def controls(mod):
    out = mod.apply_structural(case())
    assert out['M2_open'] == 0 and out['M2_solver_checked_cases'] == 0 and out['M2_structural_parent_math_cases'] == 1
    assert out['M2_resolved_cases'] == 1 and out['per_multiset']['ms09']['M2_certified'] == 0
    row = out['structural_parent_accepted_rows'][0]
    assert row['solver_checked'] is False and row['checker_invocation'] is None and row['drat_proof_sha256'] is None and row['s_verified'] is False
    checks = ['valid exact row resolves one mathematical case, zero solver cases']
    fixtures = []
    for key, val in [('tag', 'ms09_s00004'), ('multiset', 8), ('b_index', 4),
                     ('complete_placement_denominator', 1), ('list_sha256', '0' * 64)]:
        d = case()
        d['structural_empty_covers_pending_parent'][0][key] = val
        fixtures.append(('bad pending identity field ' + key, d))
    d = case()
    d['structural_empty_covers_pending_parent'].append(copy.deepcopy(d['structural_empty_covers_pending_parent'][0]))
    fixtures.append(('duplicate pending exact row', d))
    d = case()
    d['M2_open_tags'].append(A.TAG)
    fixtures.append(('duplicate exact open tag', d))
    d = case()
    d['structural_empty_covers_pending_parent'] = []
    fixtures.append(('missing pending exact row', d))
    for label, d in fixtures:
        out = mod.apply_structural(d)
        assert out['M2_open'] == 1 and out['M2_solver_checked_cases'] == 0 and out['M2_structural_parent_math_cases'] == 0, label
        assert not out['structural_parent_accepted_rows'] and out['structural_b3_binding_failure']['error_kind'] == 'base_case_identity', label
        checks.append(label)
    # If a solver already closed the exact case, retain the mathematical note but do not double-count it.
    d = case()
    d['per_multiset']['ms09'].update(M2_certified=1, both=1)
    d.update(M2_open_tags=[], M2_open=0, structural_empty_covers_pending_parent=[])
    out = mod.apply_structural(d)
    assert out['M2_solver_checked_cases'] == 1 and out['M2_structural_parent_math_cases'] == 0 and out['M2_resolved_cases'] == 1
    assert out['structural_parent_accepted_rows'][0]['contributes_new_case'] is False
    checks.append('already solver-closed exact case not double-counted')
    real_verify = mod.STRUCTURAL.verify
    try:
        mod.STRUCTURAL.verify = lambda: mod.STRUCTURAL.pending('digest', 'simulated changed required binding')
        out = mod.apply_structural(case())
        assert out['M2_open'] == 1 and out['M2_structural_parent_math_cases'] == 0 and out['M2_resolved_cases'] == 0
        assert not out['structural_parent_accepted_rows']
    finally:
        mod.STRUCTURAL.verify = real_verify
    checks.append('failed evidence binding never resolves a case')
    return checks


def main():
    baseline = controls(A)
    source = Path(A.__file__).read_text()
    mutations = {
      'exact_tag': ("r.get('tag') == TAG and ", ''),
      'exact_multiset': ("r.get('multiset') == 9 and ", ''),
      'exact_b_index': ("r.get('b_index') == 3", 'True'),
      'empty_denominator': ("r.get('complete_placement_denominator') == 0", 'True'),
      'exact_list_sha': ("r.get('list_sha256') == STRUCTURAL.EXPECTED['empty_list_receipt']['sha256']", 'True'),
      'unique_pending_row': ("len(candidates) != 1", 'False'),
      'unique_open_tag': ("out['M2_open_tags'].count(TAG) != 1", 'False'),
      'no_double_count': ("if TAG in out['M2_open_tags']:", 'if True:'),
      'binding_required': ("if result['accepted']:\n        result['contributes_new_case'] = False", "if True:\n        result['contributes_new_case'] = False")}
    kills = []
    for name,(anchor,replacement) in mutations.items():
        assert source.count(anchor) == 1, name
        changed = source.replace(anchor,replacement,1)
        mod = types.ModuleType('aggregate17_mutant_' + name)
        mod.__file__ = A.__file__
        exec(compile(changed, 'in-memory-aggregate17-' + name, 'exec'), mod.__dict__)
        failure = None
        try:
            controls(mod)
        except Exception as exc:
            failure = repr(exc)[:1000]
        kills.append({'removed_protection':name,'mutant_sha256':hashlib.sha256(changed.encode()).hexdigest(),
                      'killed':failure is not None,'observed_failure':failure})
        assert failure is not None, ('SURVIVED',name)
    record = {'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'module_sha256':hashlib.sha256(source.encode()).hexdigest(),
              'controls':baseline, 'control_count':len(baseline), 'single_guard_mutants':kills,
              'all_mutants_killed':all(r['killed'] for r in kills),
              'scope':'in-memory exact-case accounting/identity controls, not solver or proof mutations'}
    dest = Path(A.LANE) / 'cycle2' / ('structural-b3-aggregation-controls-%d.json' % time.time_ns())
    with dest.open('x') as f:
        json.dump(record,f,indent=1)
    print(dest)
    print(json.dumps({'controls':len(baseline),'single_guard_mutants':len(kills),'all_killed':record['all_mutants_killed']}))


if __name__ == '__main__':
    main()
