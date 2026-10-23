#!/usr/bin/env python3
"""Freeze COMPLETE unchanged ms09 independent-B denominator, production queue and14 exact-input validation tasks.
Historical/calibration records remain ORIGINAL-QUALIFIED only, never final evidence. No old record is rewritten.
All numerical validation CNFs are regenerated/pinned here BEFORE any later measured-v2 validation solve.
"""
import hashlib
import json
import time
import os
import sys
from pathlib import Path

import lane_new_data_accounting as ACCOUNT
import m2_ms09_contract_v6_3 as C
import m2_ms09_evidence_v6_3 as E
import m2_supervised_runtime_v6_3 as R

L = C.LANE
PHASE = L/'cycle2'/'ms09-batch-denominators-v2-20261018T015110.json'
CAL1 = 'cycle2/m2-kissat-calibration-contract-20261018T022704.json'
CAL1_SHA = '4565dcc9a2a99eba9efa565409d00ebbc37aa3bf8a6c3793895d4de7a39eef71'
CAL2 = 'cycle2/m2-kissat-strata-contract-20261018T030136.json'
CAL2_SHA = '9c3e76a2d9c001724d902b4d40923284b629919dd508f163a7fcc02728e57d74'
CAL_BATCHES = [(CAL1,CAL1_SHA,'m2-kissat-calibration-20261018T022704',9,0,99),
              (CAL1,CAL1_SHA,'m2-kissat-calibration-20261018T022704',4,100,199)] + [
    (CAL2,CAL2_SHA,'m2-kissat-strata-calibration-20261018T030136',bi,0,24 if bi == 70 else 99) for bi in (70,13,20,31,55)]


def main():
    phase = C.read(PHASE)
    skpath = 'cycle2/skel-b/skeletons-b-ms09.json'
    mappath = 'cycle2/skel-b/compare-map-ms09.json'
    D,mp = C.read(L/skpath),C.read(L/mappath)
    assert len(D['skeletons']) == 71 and D['c0'] == 5 and D['L'] == 0
    assert mp['bijection'] is True and sorted(mp['a_to_b']) == list(range(71))
    source_names = C.SOURCE_FILES
    out = {'schema':C.SCHEMA,'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'scope':'ALL original ms09 cases; unchanged independent B encoder; full exact original B100 interval unions',
        'source_sha256':{p:E.digest(L/p) for p in source_names},'skeleton_path':skpath,'skeleton_sha256':E.digest(L/skpath),
        'map_path':mappath,'map_sha256':E.digest(L/mappath),'phase_path':str(PHASE.relative_to(L)),'phase_sha256':E.digest(PHASE),
        'supervisor':{'path':str(R.SUP_PATH),'sha256':R.SUP_SHA},
        'native_seconds':600,'check_seconds':1200,'batch_size':100,'count_ceiling':2,'chunk_seconds':10800,'allowance_seconds':2400,
        'binary_authority':{kind:{'path':path,'sha256':E.digest(path)} for kind,path in
            [('python',os.path.abspath(sys.executable)),('solver','/opt/homebrew/bin/kissat'),('checker',str(L/'tools/drat-trim/drat-trim'))]},
        'cases':[],'calibration_reservations':[],'reserved_ids':[],'pending_order':[],'frozen_original_records':[],
        'validation_tasks':[],'validation_order':C.CALIBRATION_VALIDATION_IDS+C.HISTORICAL_VALIDATION_IDS,
        'reuse_policy':'WITHDRAWN: only new measured-v3 exact-input validation may qualify historical inputs',
        'no_retry':'one new _k1_v6_3 attempt/input; pre-worker admission refusals stay unattempted; every supervisor stop and UNKNOWN preserved; individual re-admission needs explicit parent decision',
        'priority':'primary open-M2 work before14 measured validations; LEGACY5 repair E0 then ms01 only afterward',
        'final_gate':'all exact intervals measured-v3; scientific UNKNOWN on failed certification with separate persistent integrity/SAT/safety veto',
        'resource_policy':C.resource_policy()}
    frozen = {}
    def freeze_file(rel):
        h = E.digest(L/rel)
        frozen[rel] = h
        return h
    for bi in range(71):
        sk = D['skeletons'][bi]
        ca = {'b_index':bi,'mapped_A2_tag':'ms09_s%05d' % mp['a_to_b'].index(bi),
              'skeleton_sha256':hashlib.sha256(json.dumps(sk,sort_keys=True).encode()).hexdigest(),
              'list':None,'direct':None,'intervals':[]}
        dp = 'cycle2/m2skel_drat/ms09_b%05d.json' % bi
        if (L/dp).exists():
            r = C.read(L/dp)
            rh = freeze_file(dp)
            assert r.get('status') != 'SAT', ('SAT VETO',dp,rh)
            if r.get('status') == 'UNSAT' and r.get('checked') is True:
                raw = C.formula(out,ca,None)
                ex = C.context(bi,None,hashlib.sha256(raw).hexdigest(),len(raw))
                q = E.inspect(L/dp,ex,rh)
                assert q['state'] == 'QUALIFIED', (dp,q['errors'])
                ca['direct'] = {'path':dp,'sha256':rh,'expected':ex}
                ca['direct_task'] = C.new_task(bi,None)
        ep = 'cycle2/m2part_drat/ms09_b%05d/ext.json' % bi
        if (L/ep).exists():
            ed = C.read(L/ep)
            n,raw_n,aut = ed['num_placements'],ed['raw_class_assignments'],ed['automorphisms']
            assert type(n) is int and type(raw_n) is int and type(aut) is int and 0 <= n == len(ed['placements']) <= raw_n and aut > 0
            ca['list'] = {'path':ep,'sha256':E.digest(L/ep),'bytes':(L/ep).stat().st_size,'n':n,'raw':raw_n,'aut':aut}
            expected_phase = next((x for x in phase['pending_batch_jobs']+phase['already_complete_cases']+phase['structural_pending_parent'] if x['job'] == '9:%d' % bi),None)
            assert expected_phase and ca['list']['sha256'] == expected_phase['list_sha256']
            assert n == expected_phase['complete_placement_denominator']
            for lo in range(0,n,100):
                hi = min(n,lo+100)-1
                it = C.new_task(bi,[lo,hi])
                assert not (L/it['new_record']).exists() and not (L/it['claim']).exists(), 'new production namespace already exists'
                if (L/it['original']).exists():
                    r = C.read(L/it['original'])
                    rh = freeze_file(it['original'])
                    assert r.get('status') != 'SAT', ('SAT VETO',it['original'])
                    if r.get('status') == 'UNSAT' and r.get('checked') is True:
                        buf = C.formula(out,ca,[lo,hi])
                        ex = C.context(bi,[lo,hi],hashlib.sha256(buf).hexdigest(),len(buf))
                        q = E.inspect(L/it['original'],ex,rh)
                        assert q['state'] == 'QUALIFIED', (it['original'],q['errors'])
                        it['baseline'] = {'path':it['original'],'sha256':rh,'expected':ex}
                ca['intervals'].append(it)
        else:
            assert bi == 1 and ca['direct'], 'missing list not justified by exact complete direct case'
        if ca['list'] and ca['list']['n'] == 0:
            proof = C.B3.verify()
            assert bi == 3 and proof['accepted'], 'no generic empty-list acceptance'
            ca['parent_structural_note_sha256'] = proof['parent_note_sha256']
        out['cases'].append(ca)
    bycase = {x['b_index']:x for x in out['cases']}
    for cp,ch,folder,bi,lo,hi in CAL_BATCHES:
        assert E.digest(L/cp) == ch
        cc = C.read(L/cp)
        for rel,h in cc['source_and_input_sha256'].items():
            assert E.digest(L/rel) == h
        name = 'calibration_ms09_b%05d_%05d_%05d' % (bi,lo,hi)
        rp = 'cycle2/%s/%s.json' % (folder,name)
        pp = 'cycle2/%s/%s.cnf-pin.json' % (folder,name)
        ca = bycase[bi]
        buf = C.formula(out,ca,[lo,hi])
        ex = C.context(bi,[lo,hi],hashlib.sha256(buf).hexdigest(),len(buf),True)
        q = E.inspect(L/rp,ex)
        r,pin = q.get('record'),C.read(L/pp)
        assert q['state'] == 'QUALIFIED' and r['count_for_scientific_coverage'] is False and r['calibration_scope_bound'] is True and r['calibration_valid_unsat'] is True
        assert pin['contract_sha256'] == ch and pin['b_index'] == bi and pin['indices'] == [lo,hi]
        assert pin['cnf_sha256'] == ex['cnf_sha256'] and pin['cnf_bytes'] == ex['cnf_bytes']
        assert pin['list_sha256'] == ca['list']['sha256'] and pin['complete_placement_denominator'] == ca['list']['n']
        ref = {'id':C.key(bi,lo,hi),'record':rp,'record_sha256':q['sha256'],'pin':pp,'pin_sha256':E.digest(L/pp),
               'calibration_contract':cp,'calibration_contract_sha256':ch,'b_index':bi,'indices':[lo,hi],
               'cnf_sha256':ex['cnf_sha256'],'cnf_bytes':ex['cnf_bytes'],'list_sha256':ca['list']['sha256'],
               'complete_denominator':ca['list']['n'],'expected':ex,'source_sha256':cc['source_and_input_sha256'],
               'existing_original_also_covers':bool(next(it for it in ca['intervals'] if it['indices'] == [lo,hi]).get('baseline')),
               'solver_status_line':'NOT_RETAINED (guard15 stores solver_out only for rc10)',
               'solver_cnf_delivery':'NOT_RETAINED','checker_cnf_delivery':'NOT_RETAINED',
               'policy':'ORIGINAL count=false immutable; reuse permission withdrawn; measured-v2 validation required'}
        out['calibration_reservations'].append(ref)
        out['reserved_ids'].append(ref['id'])
    assert len(out['reserved_ids']) == len(set(out['reserved_ids'])) == 7
    for ca in sorted(out['cases'],key=lambda x:((x['list'] or {}).get('n',-1),x['b_index'])):
        if ca['direct'] or not ca['list'] or ca['list']['n'] == 0:
            continue
        for it in ca['intervals']:
            if not it['baseline'] and it['id'] not in out['reserved_ids']:
                out['pending_order'].append(it['id'])
    bytask = {it['id']:(ca,it) for ca in out['cases'] for it in ca['intervals']}
    bytask['b00001:direct'] = bycase[1],bycase[1]['direct_task']
    calrefs = {x['id']:x for x in out['calibration_reservations']}
    for ident in out['validation_order']:
        ca,it = bytask[ident]
        raw = C.formula(out,ca,it['indices'])
        ex = C.context(ca['b_index'],it['indices'],hashlib.sha256(raw).hexdigest(),len(raw),True)
        refs = []
        if ident in calrefs:
            cr = calrefs[ident]
            refs.append({'path':cr['record'],'sha256':cr['record_sha256']})
        original = ca['direct'] if it['indices'] is None else it.get('baseline')
        if original:
            refs.append({'path':original['path'],'sha256':original['sha256']})
        out['validation_tasks'].append({'id':ident,'b_index':ca['b_index'],'indices':it['indices'],'expected':ex,
            'source_class':'CALIBRATION_ORIGINAL_COUNT_FALSE' if ident in calrefs else 'HISTORICAL_ORIGINAL_QUALIFIED',
            'original_records':refs,'native_seconds':600,'check_seconds':1200,'proof_caps':'raw1200MiB,zstd500MiB',
            'one_attempt':True,'no_rewrite_or_flag_backfill':True})
    out['frozen_original_records'] = [{'path':p,'sha256':h} for p,h in sorted(frozen.items())]
    n_tasks = len(out['pending_order'])+len(out['validation_tasks'])
    out['resource_plan'] = {'current_new_data':ACCOUNT.account(L),'per_interval_retained_upper_bytes':R.ITEM_ORDINARY_BOUND,
        'all_new_compute_intervals':n_tasks,'all_new_compute_retained_upper_bytes':n_tasks*R.ITEM_ORDINARY_BOUND,
        'concurrent_halting_diagnostics_reserve_bytes':R.ROUTE_FAILURE_RESERVE,'contract_publish_bound_bytes':16*1024**2,
        'whole_planned_lane_retained_bound_bytes':R.ALL_PLANNED_RETAINED_BOUND,
        'no_proof_or_cnf_copies':True,'hardlinks_charged_per_path':True}
    a = out['resource_plan']['current_new_data']
    assert a['known'] and a['new_data_usage_upper_bytes']+R.ALL_PLANNED_RETAINED_BOUND+R.OTHER_WRITER_MARGIN+16*1024**2 <= ACCOUNT.ENFORCED_CAP_BYTES
    sats,invalid = C.sat_scan()
    assert not sats and not invalid, ('SAT/invalid JSON veto',sats,invalid)
    dest = L/'cycle2'/('m2-ms09-k1-v6_3-contract-'+time.strftime('%Y%m%dT%H%M%S')+'.json')
    stage = L/'scratch'/'m2k1-publish'/('contract-'+str(time.time_ns()))
    C.verify_sources(out)
    assert len((json.dumps(out,indent=1)+'\n').encode()) <= 8*1024**2, 'two contract hardlinks exceed16MiB frozen bound'
    h = C.publish_json(dest,out,stage)
    print(dest)
    print('contract_sha256',h,'primary_pending',len(out['pending_order']),'measured_validation_tasks',len(out['validation_tasks']))


if __name__ == '__main__':
    R.install_handlers()
    with R.Capacity(time.monotonic()+10800,metadata=True,wait_allowance=60):
        st = os.statvfs(L)
        assert st.f_bavail*st.f_frsize >= R.BASE_GATE+16*1024**2, 'fresh metadata growth floor'
        main()
