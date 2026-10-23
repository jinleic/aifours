#!/usr/bin/env python3
"""Explicit ms09 whole-case/interval registry. No legacy aggregate15/16 acceptance is imported.
Progress can use pre-child pins; FINAL formula mode recomputes every consumed CNF. SAT candidates veto the entire
component. Missing/invalid inputs or commits fail closed; only exact B3 has a separately bound parent math proof.
Calibration reservations stay pending unless an exact read-only parent disposition authorizes their pinned inputs.
"""
import hashlib
import json
import os
import time
from pathlib import Path

import encode_skel_b as ENC
import m2_ms09_evidence_v6 as E
import structural_b3_acceptance as B3
import m2_supervised_runtime_v6 as supervised_runtime

LANE = Path(__file__).resolve().parent.parent
P0 = [4,3,3,3,3,3]
SCHEMA = 'PA19-MS09-K1-v6'
SKELETON_SHA = '7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0'
MAP_SHA = 'd06bb6fce38a2fbf96cf7d84d18331ec8233b54ccdccfc4b4ec759f281aa5282'
ENCODER_SHA = 'd0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5'
PHASE_PATH = 'cycle2/ms09-batch-denominators-v2-20261018T015110.json'
PHASE_SHA = 'd0d0d7fa9dae6ab263b05af800c0967916adf840c7583613d98c15d41d810d33'
SOURCE_FILES = ('src/encode_skel_b.py','src/gen_skel_b.py','src/extend_b.py','src/extend_b_x.py',
                'src/stream_check15.py','src/calibration_chunk_budget.py','src/m2_ms09_evidence_v6.py',
                'src/m2_ms09_contract_v6.py','src/freeze_m2_ms09_k1_v6.py','src/run_m2_ms09_k1_v6.py','src/final_m2_ms09_inventory_v6.py',
                'src/m2_supervised_runtime_v6.py','src/m2_native_staged_v6.py','src/m2_item_owner_v6.py','src/m2_supervised_evidence_v6.py',
                'src/lane_new_data_accounting.py','src/structural_b3_acceptance.py','src/run_m2_ms06_direct_v6.py','src/check_m2_ms09_k1_v6.py',
                'src/supervise_pa19_v3.py')


def key(bi,lo,hi):
    return 'b%05d:%05d-%05d' % (bi,lo,hi)


CALIBRATION_VALIDATION_IDS = [key(9,0,99),key(4,100,199),key(70,0,24),key(13,0,99),key(20,0,99),key(31,0,99),key(55,0,99)]
HISTORICAL_VALIDATION_IDS = [key(0,0,40),key(2,0,99),key(2,100,143),key(4,0,99),key(4,200,299),key(4,300,399),'b00001:direct']


def new_task(bi,indices):
    if indices is None:
        base,ident,suffix = 'cycle2/m2skel_drat/ms09_b%05d' % bi,'b%05d:direct' % bi,'direct'
    else:
        lo,hi = indices
        base,ident,suffix = ('cycle2/m2part_drat/ms09_b%05d/batch_%05d_%05d' % (bi,lo,hi),
                             key(bi,lo,hi),'%05d_%05d' % (lo,hi))
    tail = '_k1_v6'
    return {'id':ident,'indices':indices,'original':base+'.json','new_record':base+tail+'.json',
            'pin':base+tail+'.cnf-pin.json','commit':base+tail+'.receipt.json',
            'claim':'cycle2/claims/m2k1_v6_ms09_b%05d_%s.claim' % (bi,suffix),'baseline':None}


def read(p):
    return json.loads(Path(p).read_bytes())


def publish_bytes(path,raw,staging):
    """Atomic NO-REPLACE publication; both own staging/final hardlinks remain (no deletion/overwrite)."""
    path,staging = Path(path),Path(staging)
    assert path.parent.resolve().is_relative_to(LANE.resolve()) and staging.resolve().is_relative_to(LANE.resolve()), 'publication escapes owned lane'
    staging.mkdir(parents=True,exist_ok=True)
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp = staging/(path.name+'.%d-%d' % (os.getpid(),time.time_ns()))
    with tmp.open('xb') as f:
        f.write(raw)
    os.link(tmp,path)


def publish_json(path,value,staging):
    raw = (json.dumps(value,indent=1)+'\n').encode()
    publish_bytes(path,raw,staging)
    return hashlib.sha256(raw).hexdigest()


def verify_sources(c):
    assert c['schema'] == SCHEMA and [x['b_index'] for x in c['cases']] == list(range(71))
    assert all(type(x['b_index']) is int for x in c['cases'])
    assert c['skeleton_path'] == 'cycle2/skel-b/skeletons-b-ms09.json' and c['skeleton_sha256'] == SKELETON_SHA
    assert c['map_path'] == 'cycle2/skel-b/compare-map-ms09.json' and c['map_sha256'] == MAP_SHA
    assert c['source_sha256']['src/encode_skel_b.py'] == ENCODER_SHA
    assert set(c['source_sha256']) == set(SOURCE_FILES), 'required frozen source set differs'
    assert c['supervisor']['path'] == str(supervised_runtime.SUP_PATH) and c['supervisor']['sha256'] == supervised_runtime.SUP_SHA
    assert E.digest(supervised_runtime.SUP_PATH) == supervised_runtime.SUP_SHA, 'reviewed supervisor source changed'
    for rel,h in c['source_sha256'].items():
        assert not Path(rel).is_absolute() and (LANE/rel).resolve().is_relative_to(LANE.resolve())
        assert E.digest(LANE/rel) == h, ('frozen source changed',rel)
    assert E.digest(LANE/c['skeleton_path']) == SKELETON_SHA and E.digest(LANE/c['map_path']) == MAP_SHA
    d,mp = read(LANE/c['skeleton_path']),read(LANE/c['map_path'])
    assert d['c0'] == 5 and d['L'] == 0 and len(d['skeletons']) == 71 and mp['bijection'] is True
    assert sorted(mp['a_to_b']) == list(range(71))
    assert c['phase_path'] == PHASE_PATH and c['phase_sha256'] == PHASE_SHA
    assert E.digest(LANE/PHASE_PATH) == PHASE_SHA, 'original complete denominator authority changed'
    phase = read(LANE/c['phase_path'])
    phase_rows = phase['pending_batch_jobs']+phase['already_complete_cases']+phase['structural_pending_parent']
    for ref in c.get('frozen_original_records',[]):
        assert E.digest(LANE/ref['path']) == ref['sha256'], ('frozen original receipt changed',ref['path'])
    order = []
    for ca in c['cases']:
        bi = ca['b_index']
        assert ca['mapped_A2_tag'] == 'ms09_s%05d' % mp['a_to_b'].index(bi)
        assert ca['skeleton_sha256'] == hashlib.sha256(json.dumps(d['skeletons'][bi],sort_keys=True).encode()).hexdigest()
        ls = ca.get('list')
        if ls:
            assert ls['path'] == 'cycle2/m2part_drat/ms09_b%05d/ext.json' % bi
            eraw = (LANE/ls['path']).read_bytes()
            assert hashlib.sha256(eraw).hexdigest() == ls['sha256'], ('frozen list changed',bi)
            ed = json.loads(eraw)
            n = ls['n']
            assert all(type(ed[k]) is int for k in ('num_placements','raw_class_assignments','automorphisms'))
            assert type(n) is int and type(ls['raw']) is int and type(ls['aut']) is int
            assert 0 <= n == ed['num_placements'] == len(ed['placements']) <= ls['raw'] == ed['raw_class_assignments']
            assert ls['aut'] == ed['automorphisms'] > 0
            ph = next(x for x in phase_rows if x['job'] == '9:%d' % bi)
            assert ls['sha256'] == ph['list_sha256'] and n == ph['complete_placement_denominator']
            expected = [[lo,min(n,lo+100)-1] for lo in range(0,n,100)]
            assert [it['indices'] for it in ca['intervals']] == expected and sum(hi-lo+1 for lo,hi in expected) == n
            for it in ca['intervals']:
                lo,hi = it['indices']
                assert all(type(v) is int for v in it['indices']) and it['id'] == key(bi,lo,hi)
                base = 'cycle2/m2part_drat/ms09_b%05d/batch_%05d_%05d' % (bi,lo,hi)
                assert it['original'] == base+'.json' and it['new_record'] == base+'_k1_v6.json'
                assert it['pin'] == base+'_k1_v6.cnf-pin.json' and it['commit'] == base+'_k1_v6.receipt.json'
                assert it['claim'] == 'cycle2/claims/m2k1_v6_ms09_b%05d_%05d_%05d.claim' % (bi,lo,hi)
                if it.get('baseline'):
                    ex = it['baseline']['expected']
                    assert it['baseline']['path'] == it['original'] and ex['multiset'] == 9 and ex['b_index'] == bi and ex['indices'] == [lo,hi]
        else:
            assert bi == 1 and not ca['intervals'] and ca['direct'], 'only pinned direct B1 lacks a list'
        if ca.get('direct'):
            ex = ca['direct']['expected']
            assert ca['direct']['path'] == 'cycle2/m2skel_drat/ms09_b%05d.json' % bi
            assert ex['multiset'] == 9 and ex['b_index'] == bi and ex['indices'] is None and ex['encoder'] == 'encode_skel_b.build_v2'
    assert len(c['reserved_ids']) == len(set(c['reserved_ids'])) == 7
    required_reserved = {key(9,0,99),key(4,100,199),key(70,0,24),key(13,0,99),key(20,0,99),key(31,0,99),key(55,0,99)}
    assert set(c['reserved_ids']) == required_reserved
    assert {r['id'] for r in c['calibration_reservations']} == required_reserved
    bycase = {ca['b_index']:ca for ca in c['cases']}
    for ref in c['calibration_reservations']:
        bi,idx = ref['b_index'],ref['indices']
        assert type(bi) is int and isinstance(idx,list) and len(idx) == 2 and all(type(v) is int for v in idx)
        assert ref['id'] == key(bi,*idx) and ref['list_sha256'] == bycase[bi]['list']['sha256']
        assert ref['expected']['multiset'] == 9 and ref['expected']['b_index'] == bi and ref['expected']['indices'] == idx
        assert E.digest(LANE/ref['record']) == ref['record_sha256'] and E.digest(LANE/ref['pin']) == ref['pin_sha256']
        assert E.digest(LANE/ref['calibration_contract']) == ref['calibration_contract_sha256']
        for rel,h in ref['source_sha256'].items():
            assert E.digest(LANE/rel) == h, ('frozen calibration source changed',rel)
    for ca in sorted(c['cases'],key=lambda x:((x['list'] or {}).get('n',-1),x['b_index'])):
        if ca['direct'] or not ca['list'] or ca['list']['n'] == 0:
            continue
        order += [it['id'] for it in ca['intervals'] if not it['baseline'] and it['id'] not in required_reserved]
    assert c['pending_order'] == order, 'compute order is not the exact deterministic full unresolved partition'
    validations = c['validation_tasks']
    assert [x['id'] for x in validations] == CALIBRATION_VALIDATION_IDS+HISTORICAL_VALIDATION_IDS
    assert len({x['id'] for x in validations}) == 14 and c['validation_order'] == [x['id'] for x in validations]
    bytask = {it['id']:(ca,it) for ca in c['cases'] for it in ca['intervals']}
    direct_ca = c['cases'][1]
    assert direct_ca['direct_task'] == new_task(1,None)
    bytask['b00001:direct'] = direct_ca,direct_ca['direct_task']
    for val in validations:
        ca,it = bytask[val['id']]
        assert val['b_index'] == ca['b_index'] and val['indices'] == it['indices']
        ex = val['expected']
        assert ex['multiset'] == 9 and ex['b_index'] == ca['b_index'] and ex['indices'] == it['indices']
        assert val['source_class'] == ('CALIBRATION_ORIGINAL_COUNT_FALSE' if val['id'] in required_reserved else 'HISTORICAL_ORIGINAL_QUALIFIED')
        assert val['original_records'] and all(E.digest(LANE/x['path']) == x['sha256'] for x in val['original_records'])
        assert val['native_seconds'] == 600 and val['check_seconds'] == 1200
    assert c['reuse_policy'] == 'WITHDRAWN: only new measured-v3 exact-input validation may qualify historical inputs'


def structural_acceptance(c,ca):
    if not (type(ca['b_index']) is int and ca['b_index'] == 3 and type(ca['list']['n']) is int and ca['list']['n'] == 0
            and c['skeleton_sha256'] == SKELETON_SHA
            and ca['list']['sha256'] == B3.EXPECTED['empty_list_receipt']['sha256']):
        return {'accepted':False,'scope':'no generic empty-cover acceptance'}
    return B3.verify()


def load(path,h):
    assert E.digest(path) == h, 'production contract SHA differs'
    c = read(path)
    verify_sources(c)
    assert (c['native_seconds'],c['check_seconds'],c['chunk_seconds'],c['allowance_seconds']) == (600,1200,10800,2400)
    assert c['batch_size'] == 100 and c['count_ceiling'] == 2
    assert c['resource_policy'] == resource_policy()
    assert c['binary_authority']['solver']['path'] == '/opt/homebrew/bin/kissat'
    assert c['binary_authority']['checker']['path'] == str(LANE/'tools/drat-trim/drat-trim')
    assert set(c['binary_authority']) == {'python','solver','checker'}
    for authority in c['binary_authority'].values():
        assert Path(authority['path']).is_absolute() and E.SHA.fullmatch(authority['sha256'])
    return c


def resource_policy():
    return {'automatic_retry_allowed':False,'normal_group_rss_bytes':supervised_runtime.GROUP_RSS_CAP,
        'census_ttl_seconds':600,'other_writer_margin_bytes':256*1024**2,'fresh_statvfs_base_bytes':supervised_runtime.BASE_GATE,
        'whole_plan_remaining_bound_bytes':supervised_runtime.ALL_PLANNED_RETAINED_BOUND,
        'residual':'whole-plan bound covers route writes; no other lane writer adds>256MiB within600s',
        'explicit_leader_wait_and_group_quiescence':True,'guards_are_sampled_not_instantaneous':True}


def formula(c,ca,indices):
    """EXACT original run_m2_15 constructor/arguments; no M1 encoder/clauses or new symmetry."""
    sp = LANE/c['skeleton_path']
    raw = sp.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == c['skeleton_sha256']
    D = json.loads(raw)
    sk = D['skeletons'][ca['b_index']]
    assert hashlib.sha256(json.dumps(sk,sort_keys=True).encode()).hexdigest() == ca['skeleton_sha256']
    special = [p for p in D['profiles'] if list(p) != P0]
    if indices is None:
        nv,cl = ENC.build_v2(D['c0'],[tuple(t) for t in sk['types']],sk['empty'],special)
    else:
        ls = ca['list']
        raw = (LANE/ls['path']).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == ls['sha256']
        data = json.loads(raw)
        assert data['num_placements'] == len(data['placements']) == ls['n'] > 0
        assert data['raw_class_assignments'] == ls['raw'] and data['automorphisms'] == ls['aut']
        lo,hi = indices
        nv,cl = ENC.build_partbatch(D['c0'],[tuple(t) for t in sk['types']],sk['empty'],special,
                                   [data['placements'][i] for i in range(lo,hi+1)])
    return ENC.cnf_bytes(nv,cl)


def context(bi,indices,sha,nbytes,kissat=False):
    return E.expected(9,bi,indices,sha,nbytes,'encode_skel_b.build_v2' if indices is None else 'encode_skel_b.build_partbatch',600,kissat)




def sat_scan():
    """Scan all actual ms09 scientific/calibration JSON, including unrecognized extra records; not controls."""
    paths = set((LANE/'cycle2'/'m2skel_drat').glob('ms09_b*.json'))
    for d in (LANE/'cycle2'/'m2part_drat').glob('ms09_b*'):
        if d.is_dir():
            paths.update(d.glob('*.json'))
    for pattern in ('m2-kissat-calibration-*','m2-kissat-strata-calibration-*'):
        for d in (LANE/'cycle2').glob(pattern):
            if d.is_dir():
                paths.update(d.glob('*.json'))
    paths.update((LANE/'cycle2'/'m2k1-chunks').glob('*/SAT-*.json'))
    paths.update((LANE/'cycle2'/'witness').glob('m2k1*.json'))
    aborted = LANE/'cycle2'/'aborted'
    paths.update(aborted.glob('*.json'))
    for name in supervised_runtime.PERSISTENT_VETO_FLAGS:
        flag = LANE/'cycle2'/name
        if flag.exists():
            paths.add(flag)
    sats,invalid = [],[]
    for p in sorted(paths):
        try:
            r = read(p)
        except (OSError,ValueError,UnicodeError) as exc:
            invalid.append({'path':str(p.relative_to(LANE)),'error':repr(exc)})
            continue
        if not isinstance(r,dict):
            invalid.append({'path':str(p.relative_to(LANE)),'error':'scientific JSON is not an object'})
            continue
        if p.parent == aborted and not (r.get('multiset') == 9 or 'ms09_' in str(r.get('fifo_dir','')) or str(r.get('tag','')).startswith('ms09_')):
            continue
        inner = r.get('native_result') if isinstance(r.get('native_result'),dict) else {}
        checker = inner.get('checker_collector') if isinstance(inner.get('checker_collector'),dict) else {}
        if r.get('status') == 'SAT' or inner.get('status') == 'SAT' or r.get('sat_candidate') is True or inner.get('sat_candidate') is True or p.name in supervised_runtime.SAT_VETO_FLAGS:
            sats.append({'path':str(p.relative_to(LANE)),'sha256':E.digest(p)})
        if r.get('integrity_status') == 'INVALID' or inner.get('integrity_status') == 'INVALID' or r.get('status') == 'INVALID' or inner.get('status') == 'INVALID' or any('NOT VERIFIED' in str(v) for v in checker.get('status_lines',[])) or p.name in supervised_runtime.NONSAT_VETO_FLAGS:
            invalid.append({'path':str(p.relative_to(LANE)),'error':'persistent INVALID/safety veto','sha256':E.digest(p)})
    return sats,invalid


def inspect_new(c,contract_sha,ca,it,verify_formula=False):
    p = LANE/it['new_record']
    if not p.exists():
        return {'state':'MISSING','errors':[],'sat':False}
    try:
        pin,commit = read(LANE/it['pin']),read(LANE/it['commit'])
        assert pin['schema'] == 'PA19-K1-CNF-PIN-v6' and commit['schema'] == 'PA19-K1-RECEIPT-v6'
        assert pin['production_contract_sha256'] == commit['production_contract_sha256'] == contract_sha
        assert type(pin['multiset']) is int and pin['multiset'] == 9
        assert type(pin['b_index']) is int and type(commit['b_index']) is int
        assert pin['b_index'] == commit['b_index'] == ca['b_index']
        idx = it['indices']
        assert pin['indices'] == commit['indices'] == idx
        val = next((x for x in c['validation_tasks'] if x['id'] == it['id']),None)
        if val:
            assert pin['cnf_sha256'] == val['expected']['cnf_sha256'] and pin['cnf_bytes'] == val['expected']['cnf_bytes']
        if idx is not None:
            assert isinstance(pin['indices'],list) and all(type(v) is int for v in pin['indices']+commit['indices'])
        recipe = pin['recipe']
        assert recipe['multiset'] == 9 and recipe['b_index'] == ca['b_index'] and recipe['indices'] == idx
        assert recipe['mode'] == ('direct' if idx is None else 'partbatch')
        if idx is not None:
            assert recipe['list_path'] == ca['list']['path'] and recipe['list_sha256'] == ca['list']['sha256'] and recipe['complete_denominator'] == ca['list']['n']
        assert recipe['skeleton_path'] == c['skeleton_path'] and recipe['skeleton_sha256'] == c['skeleton_sha256']
        assert recipe['encoder_sha256'] == c['source_sha256']['src/encode_skel_b.py']
        assert pin['source_sha256'] == c['source_sha256'] and pin['supervisor_sha256'] == c['supervisor']['sha256']
        assert pin['binary_authority'] == c['binary_authority']
        assert commit['pin_sha256'] == E.digest(LANE/it['pin']) and commit['record_sha256'] == E.digest(p)
        ctx = context(ca['b_index'],idx,pin['cnf_sha256'],pin['cnf_bytes'],True)
        ctx.update(lane_root=str(LANE),binary_authority=c['binary_authority'],source_sha256=c['source_sha256'],recipe=recipe)
        if verify_formula:
            raw = formula(c,ca,idx)
            assert hashlib.sha256(raw).hexdigest() == pin['cnf_sha256'] and len(raw) == pin['cnf_bytes']
        r = E.inspect(p,ctx,commit['record_sha256'])
        obj = r.get('record') or {}
        assert isinstance(obj,dict)
        assert obj.get('production_contract_sha256') == contract_sha and obj.get('pre_child_pin_sha256') == commit['pin_sha256']
        assert obj.get('count_for_scientific_coverage') is True and obj.get('runner') == 'run_m2_ms09_k1_v6.py'
        assert obj.get('pipeline_schema') == 'PA19-SUPERVISED-DRAT-v6'
        if idx is not None:
            assert obj.get('list_sha256') == ca['list']['sha256'] and obj.get('enumerator') == 'extend_b.py'
            assert type(obj.get('complete_denominator')) is int and obj['complete_denominator'] == ca['list']['n']
        return r
    except (OSError,ValueError,KeyError,AssertionError,TypeError) as exc:
        return {'state':'INTEGRITY_VETO','errors':['new record/pin/commit binding failed: '+repr(exc)],'sat':False}






def inventory(c,contract_sha,verify_formulas=False):
    """Final coverage consumes ONLY complete measured-v3 inputs; historical outcomes remain separately visible."""
    verify_sources(c)
    sats,issues = sat_scan()
    rows,covered_indices,open_indices,original_only = [],0,0,[]
    for ca in c['cases']:
        bi = ca['b_index']
        if ca.get('direct'):
            dr = ca['direct']
            historical = E.inspect(LANE/dr['path'],dr['expected'],dr['sha256'])
            if historical['state'] != 'QUALIFIED': issues.append({'case':bi,'historical_direct':historical['errors']})
            task = ca['direct_task']
            chk = inspect_new(c,contract_sha,ca,task,verify_formulas)
            done = chk['state'] == 'QUALIFIED'
            if chk['state'] in ('INTEGRITY_VETO','HALT_UNKNOWN','SAT_VETO'): issues.append({'case':bi,'new_direct':chk['errors']})
            if not done and historical['state'] == 'QUALIFIED': original_only.append(task['id'])
            rows.append({'b_index':bi,'state':'DIRECT_CHECKED' if done else 'OPEN','solver_checked':done,
                         'historical_class':'ORIGINAL-QUALIFIED, exact checker input delivery NOT_RETAINED',
                         'validation':chk['state']})
            continue
        if ca['list']['n'] == 0:
            proof = structural_acceptance(c,ca)
            rows.append({'b_index':bi,'state':'STRUCTURAL_PARENT_MATH' if proof.get('accepted') else 'OPEN_EMPTY_NO_VACUOUS_ACCEPTANCE',
                         'solver_checked':False,'structural':proof})
            continue
        states = []
        for it in ca['intervals']:
            ident = it['id']
            historical_state = None
            if it.get('baseline'):
                ref = it['baseline']
                old = E.inspect(LANE/ref['path'],ref['expected'],ref['sha256'])
                historical_state = 'ORIGINAL-QUALIFIED' if old['state'] == 'QUALIFIED' else 'INVALID'
                if historical_state == 'INVALID': issues.append({'interval':ident,'historical':old['errors']})
            if ident in c['reserved_ids']:
                historical_state = 'CALIBRATION_ORIGINAL_COUNT_FALSE'
            chk = inspect_new(c,contract_sha,ca,it,verify_formulas)
            state = 'COVERED' if chk['state'] == 'QUALIFIED' else chk['state']
            if state in ('INTEGRITY_VETO','HALT_UNKNOWN','SAT_VETO'): issues.append({'interval':ident,'new':chk['errors']})
            if historical_state and state != 'COVERED': original_only.append(ident)
            size = it['indices'][1]-it['indices'][0]+1
            if state == 'COVERED': covered_indices += size
            else: open_indices += size
            states.append({'id':ident,'indices':it['indices'],'state':state,'historical_class':historical_state})
        done = bool(states) and all(s['state'] == 'COVERED' for s in states)
        rows.append({'b_index':bi,'state':'FULL_INTERVAL_UNION_CHECKED' if done else 'OPEN','solver_checked':done,
                     'denominator':ca['list']['n'],'intervals':states})
    resolved = sum(r['state'] in ('DIRECT_CHECKED','FULL_INTERVAL_UNION_CHECKED','STRUCTURAL_PARENT_MATH') for r in rows)
    for row in rows:
        row['closed_for_final'] = bool(verify_formulas and not sats and not issues and row['state'] in
                                      ('DIRECT_CHECKED','FULL_INTERVAL_UNION_CHECKED','STRUCTURAL_PARENT_MATH'))
    return {'scope':'ms09 component ONLY; not a global PA19/M1/other-multiset verdict','rows':rows,'cases':71,
            'progress_receipt_resolved_cases':resolved,'closed_cases_for_final':sum(r['closed_for_final'] for r in rows),
            'progress_solver_receipt_cases':sum(r['solver_checked'] for r in rows),
            'structural_parent_math_cases':sum(r['state'] == 'STRUCTURAL_PARENT_MATH' for r in rows),
            'covered_placement_indices':covered_indices,'open_placement_indices':open_indices,'sat_veto':sats,'integrity_issues':issues,
            'formula_verification_mode':verify_formulas,'final_ms09_acceptance_ready':bool(verify_formulas and resolved == 71 and not sats and not issues),
            'historical_inputs_pending_measured_validation':sorted(set(original_only)),
            'historical_outcomes_never_final_counted':True,'parent_calibration_reuse_permission':'WITHDRAWN',
            'admission_union':supervised_runtime.admission_union(LANE)}
