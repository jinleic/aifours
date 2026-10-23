#!/usr/bin/env python3
"""Phase2: after the parent-reviewed H3/v5 exclusive helpers, pin COMPLETE exact lists and B100 intervals before
any solve. No enumeration/solver/proof copy. Run under an existing token or a no-stage exclusive boundary.
Missing/ambiguous/guard-tripped pins fail; empty lists are structural-pending, never generic0/0 acceptance.
"""
import hashlib
import json
import os
import time
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
INV = LANE/'cycle2'/'ms06-two-split-inventory-20261018T021822.json'
INV_SHA = '93d0c33ccc45e0cd156eb879a1bd100fe15169a06973b6efef65fabf83ec8b21'
WRAPPER_SHA = '72e6ff1837f284dd3f2958dc7350ef7703ad906cbb619e896ffcf72e7e20b3b2'


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    assert digest(INV) == INV_SHA
    inv = json.loads(INV.read_text())
    assert [r['job'] for r in inv['jobs']] == ['6:68','6:73']
    assert digest(LANE/'src'/'extend_ms06_two_growth_guarded_v5.py') == WRAPPER_SHA
    for rel,expected in inv['source_sha256'].items():
        assert digest(LANE/'src'/rel) == expected
    assert digest(LANE/inv['skeleton_file_path']) == inv['skeleton_file_sha256']
    assert digest(LANE/inv['case_map_path']) == inv['case_map_sha256']
    for old in inv['hard_lists_unchanged']:
        assert digest(LANE/old['path']) == old['sha256']
    cases = []
    for job in inv['jobs']:
        assert digest(LANE/job['source_direct_record']) == job['source_direct_record_sha256']
        assert digest(LANE/job['mapped_A2_spec_path']) == job['mapped_A2_spec_sha256']
        d = LANE/'cycle2'/'m2part_drat'/('ms06_b%05d' % job['b_index'])
        ep = d/'ext.json'
        E = json.loads(ep.read_text())
        n,raw,aut = E['num_placements'],E['raw_class_assignments'],E['automorphisms']
        assert type(n) is int and type(raw) is int and type(aut) is int and aut > 0
        assert 0 <= n == len(E['placements']) <= raw <= job['raw_assignment_dp_upper']
        assert ep.stat().st_size <= job['complete_output_upper_bytes']
        seen = set()
        for place in E['placements']:
            assert len(place) == 3 and [len(b) for b in place] == [4,4,2]
            flat = [v for block in place for v in block]
            assert len(set(flat)) == 10 and all(type(v) is int and 0 <= v < 19 for v in flat)
            assert all(block == sorted(block) for block in place)
            code = tuple(tuple(block) for block in place)
            assert code not in seen
            seen.add(code)
        pins = []
        for pinpath in sorted(d.glob('complete-denominator-*.json')):
            pin = json.loads(pinpath.read_text())
            if pin.get('inventory_sha256') != INV_SHA or pin.get('job') != job['job']:
                continue
            helper = pin.get('helper') or {}
            assert pin.get('sha256') == digest(ep) and pin.get('bytes') == ep.stat().st_size
            assert pin.get('num_placements') == n and pin.get('raw_class_assignments') == raw and pin.get('automorphisms') == aut
            assert helper.get('rc') == 0 and helper.get('stop') == 'self' and helper.get('guard_tripped') is False
            assert (helper.get('admission') or {}).get('projected_plan_within_enforced_cap') is True
            pins.append({'path':str(pinpath.relative_to(LANE)),'sha256':digest(pinpath)})
        assert len(pins) == 1, ('missing/ambiguous complete H3/v5 denominator pin',job['job'])
        batches = [{'indices':[lo,min(n,lo+100)-1],'placements':min(n,lo+100)-lo,
                    'result_path':str((d/('batch_%05d_%05d.json' % (lo,min(n,lo+100)-1))).relative_to(LANE))}
                   for lo in range(0,n,100)]
        assert sum(b['placements'] for b in batches) == n
        cases.append({'job':job['job'],'mapped_A2_tag':job['mapped_A2_tag'],'source_cnf_sha256':job['source_cnf_sha256'],
            'skeleton_sha256':job['skeleton_sha256'],'list_path':str(ep.relative_to(LANE)),'list_sha256':digest(ep),
            'list_bytes':ep.stat().st_size,'exact_raw_assignment_denominator':raw,'automorphisms':aut,
            'exact_complete_orbit_denominator':n,'complete_pin':pins[0],'batch_size':100,'batches':batches,
            'partition_sum':sum(b['placements'] for b in batches),
            'status':'STRUCTURAL/EMPTY-COVER pending its own parent argument; NOT solverchecked' if n == 0 else 'COMPLETE denominator pinned; solver coverage pending'})
    out = {'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'inventory_sha256':INV_SHA,'wrapper_sha256':WRAPPER_SHA,
           'cases':cases,'all_prior_70_ms09_list_hashes_unchanged':True,'no_truncation':True,
           'settings':{'solve_seconds':300,'check_seconds':1200,'batch':100,'count_ceiling':2,
                       'scope':'conservative original ms06 native300 ceiling; no budget increase inferred from ms09 native600'},
           'acceptance':'every pinned interval must have strict rc0 s VERIFIED with matching CNF/list/input bindings; unknown leaves case open; empty requires parent structural check; direct/split/structural separate'}
    dest = LANE/'cycle2'/('ms06-two-batch-denominators-'+time.strftime('%Y%m%dT%H%M%S')+'.json')
    with dest.open('x') as f:
        json.dump(out,f,indent=1)
    print(dest)
    print(json.dumps([{'job':c['job'],'raw':c['exact_raw_assignment_denominator'],'orbits':c['exact_complete_orbit_denominator'],
                       'batches':len(c['batches']),'list_sha256':c['list_sha256'],'partition_sum':c['partition_sum']} for c in cases]))


if __name__ == '__main__':
    main()
