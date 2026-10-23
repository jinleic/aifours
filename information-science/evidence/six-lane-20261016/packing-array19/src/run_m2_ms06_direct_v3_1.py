#!/usr/bin/env python3
"""Exact106-item ms06 initial pass, common v3 transport: CaDiCaL300/check1200, no automatic retries.
All original outcomes (24 UNSAT,4 UNKNOWN at the v2 freeze) remain immutable. Only78 unattempted original IDs run.
Scientific failed certification stays UNKNOWN with separate integrity/safety veto. Miss set freezes ONCE only after
this initial pass is complete; no enumeration/helper launches from this file. Parent source PASS/GO required.
"""
import argparse
import datetime
import hashlib
import json
import os
import sys
import time
from pathlib import Path

import encode_skel_b as ENC
import m2_item_owner_v3_1 as OWNER
import m2_ms09_contract_v3_1 as COMMON
import m2_ms09_evidence_v3_1 as E
import m2_supervised_runtime_v3 as R
import run_m2_ms09_k1_v3_1 as TX

L = COMMON.LANE
QUEUE = 'cycle2/m2-jobs-hard-direct.txt'
SK = 'cycle2/skel-b/skeletons-b-ms06.json'
SCHEMA = 'PA19-MS06-INITIAL-DIRECT-v3.1'


def task(bi):
    base = 'cycle2/m2skel_drat/ms06_b%05d_v31' % bi
    return {'id':'ms06_b%05d' % bi,'indices':None,'new_record':base+'.json','pin':base+'.cnf-pin.json',
            'commit':base+'.receipt.json','claim':'cycle2/claims/ms06_direct_v31_b%05d.claim' % bi}


def queue_ids():
    ids = []
    for line in (L/QUEUE).read_text().splitlines():
        mi,interval = line.split(':'); lo,hi = map(int,interval.split('-'))
        assert mi == '6' and lo == hi and lo not in ids
        ids.append(lo)
    assert len(ids) == 106
    return ids


def freeze():
    rows = []
    for bi in queue_ids():
        old = L/'cycle2/m2skel_drat'/('ms06_b%05d.json' % bi)
        r = COMMON.read(old) if old.exists() else None
        if r is not None: assert r['multiset'] == 6 and r['b_index'] == bi and r['status'] != 'SAT'
        assert not (L/task(bi)['new_record']).exists()
        rows.append({'b_index':bi,'original_record':str(old.relative_to(L)) if r is not None else None,
                     'original_sha256':E.digest(old) if r is not None else None,'original_status':r.get('status') if r is not None else None})
    out = {'schema':SCHEMA,'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'queue':QUEUE,'queue_sha256':E.digest(L/QUEUE),
        'skeleton_path':SK,'skeleton_sha256':E.digest(L/SK),'source_sha256':{p:E.digest(L/p) for p in COMMON.SOURCE_FILES},
        'supervisor_path':str(R.SUP_PATH),'supervisor_sha256':R.SUP_SHA,'resource_policy':COMMON.resource_policy(),
        'binary_authority':{kind:{'path':path,'sha256':E.digest(path)} for kind,path in
            [('python',os.path.abspath(sys.executable)),('solver','/opt/homebrew/bin/cadical'),('checker',str(L/'tools/drat-trim/drat-trim'))]},
        'rows':rows,'pending_order':[x['b_index'] for x in rows if x['original_record'] is None],
        'native_seconds':300,'check_seconds':1200,'count_ceiling':2,'automatic_retry_allowed':False,
        'no_helper_from_this_adapter':True,'original_outcomes_are_not_backfilled_or_final_qualified':True}
    dest = L/'cycle2'/('m2-ms06-initial-v31-contract-'+time.strftime('%Y%m%dT%H%M%S')+'.json')
    h = COMMON.publish_json(dest,out,L/'scratch/m2k1-v31-publish'/('ms06-freeze-'+str(time.time_ns())))
    print(dest,h,'pending',len(out['pending_order']),flush=True)


def verify(c):
    assert c['schema'] == SCHEMA and c['queue'] == QUEUE and E.digest(L/QUEUE) == c['queue_sha256']
    assert c['skeleton_path'] == SK and E.digest(L/SK) == c['skeleton_sha256']
    assert set(c['source_sha256']) == set(COMMON.SOURCE_FILES)
    for p,h in c['source_sha256'].items(): assert E.digest(L/p) == h
    assert c['supervisor_sha256'] == R.SUP_SHA and E.digest(R.SUP_PATH) == R.SUP_SHA
    assert c['native_seconds'] == 300 and c['check_seconds'] == 1200 and c['count_ceiling'] == 2
    assert c['resource_policy'] == COMMON.resource_policy() and c['automatic_retry_allowed'] is False
    assert c['binary_authority']['solver']['path'] == '/opt/homebrew/bin/cadical'
    assert c['binary_authority']['checker']['path'] == str(L/'tools/drat-trim/drat-trim')
    assert c['pending_order'] == [x['b_index'] for x in c['rows'] if x['original_record'] is None]
    assert [x['b_index'] for x in c['rows']] == queue_ids()
    for x in c['rows']:
        if x['original_record']: assert E.digest(L/x['original_record']) == x['original_sha256']


def inspect(c,h,bi):
    it = task(bi)
    if not (L/it['new_record']).exists(): return {'state':'MISSING','record':None,'errors':[]}
    try:
        pin,k = COMMON.read(L/it['pin']),COMMON.read(L/it['commit'])
        assert pin['schema'] == 'PA19-K1-CNF-PIN-v3.1' and k['schema'] == 'PA19-K1-RECEIPT-v3.1'
        assert pin['production_contract_sha256'] == k['production_contract_sha256'] == h
        assert type(pin['multiset']) is int and pin['multiset'] == 6 and type(pin['b_index']) is int and pin['b_index'] == k['b_index'] == bi
        assert pin['indices'] is None and pin['source_sha256'] == c['source_sha256'] and pin['binary_authority'] == c['binary_authority']
        recipe = pin['recipe']
        assert recipe['mode'] == 'direct' and recipe['multiset'] == 6 and recipe['b_index'] == bi and recipe['indices'] is None
        assert recipe['skeleton_path'] == SK and recipe['skeleton_sha256'] == c['skeleton_sha256']
        assert recipe['encoder_sha256'] == c['source_sha256']['src/encode_skel_b.py']
        assert k['pin_sha256'] == E.digest(L/it['pin']) and k['record_sha256'] == E.digest(L/it['new_record'])
        ex = E.expected(6,bi,None,pin['cnf_sha256'],pin['cnf_bytes'],'encode_skel_b.build_v2',300,False)
        ex.update(binary_authority=c['binary_authority'],lane_root=str(L),source_sha256=c['source_sha256'],recipe=recipe)
        return E.inspect(L/it['new_record'],ex,k['record_sha256'])
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as exc:
        return {'state':'INTEGRITY_VETO','errors':[repr(exc)]}


def freeze_misses(c,h):
    dest = L/'cycle2/ms06-initial-v31-UNKNOWN-misses-ONCE.json'; assert not dest.exists()
    rows = []
    for x in c['rows']:
        bi = x['b_index']
        if x['original_record']: r,rel = COMMON.read(L/x['original_record']),x['original_record']
        else:
            q = inspect(c,h,bi)
            assert q['state'] not in ('MISSING','INTEGRITY_VETO','SAT_VETO','HALT_UNKNOWN'), ('initial pass incomplete/veto',bi,q)
            r,rel = q['record'],task(bi)['new_record']
        if r.get('status') != 'UNSAT' or r.get('checked') is not True:
            rows.append({'job':'6:%d' % bi,'b_index':bi,'record':rel,'record_sha256':E.digest(L/rel),
                'cnf_sha256':r['cnf_sha256'],'cnf_bytes':r['cnf_bytes'],'status':'UNKNOWN','already_enumerated':bi in (68,73)})
    out = {'schema':'PA19-MS06-UNKNOWN-SET-v3.1','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'initial_contract_sha256':h,
        'source_sha256':c['source_sha256'],'skeleton_sha256':c['skeleton_sha256'],'jobs':rows,
        'scope':'exact accumulated initial-pass UNKNOWN set; NO helper admission/denominator supplied here',
        'requires_new_source_denominator_growth_review_before_any_helper':True}
    rh = COMMON.publish_json(dest,out,L/'scratch/m2k1-v31-publish'/('ms06-misses-'+str(time.time_ns())))
    print(dest,rh,'UNKNOWN',len(rows),flush=True)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('contract',nargs='?'); ap.add_argument('sha256',nargs='?')
    ap.add_argument('--freeze',action='store_true'); ap.add_argument('--freeze-misses',action='store_true'); ap.add_argument('--max-attempts',type=int,default=8)
    args = ap.parse_args(); R.install_handlers()
    cutoff = datetime.datetime.fromisoformat('2026-10-18T18:31:43-07:00').timestamp()
    deadline = min(time.monotonic()+10800,time.monotonic()+max(0,cutoff-time.time()))
    with R.Capacity(deadline,metadata=True,wait_allowance=60):
        st = os.statvfs(L); assert st.f_bavail*st.f_frsize >= R.BASE_GATE+1024**2
        if args.freeze: freeze(); return
        assert args.contract and args.sha256 and E.digest(args.contract) == args.sha256
        c = COMMON.read(args.contract); verify(c)
        if args.freeze_misses: freeze_misses(c,args.sha256); return
        assert args.max_attempts > 0 and all(v['matches'] for v in R.binary_observations(c['binary_authority']).values())
        reference = R.create_census(); census = R.census_for_gate(reference)
        assert census['current_data_upper_bytes']+R.ALL_PLANNED_RETAINED_BOUND+R.OTHER_WRITER_MARGIN <= R.DATA_CAP
        admission = {'binary_authority':c['binary_authority'],'census_reference':reference,
                     'whole_plan_remaining_bound_bytes':c['resource_policy']['whole_plan_remaining_bound_bytes']}
        D = COMMON.read(L/SK); special = [p for p in D['profiles'] if list(p) != COMMON.P0]
    stage = L/'scratch/m2k1-v31-publish'/('ms06-'+str(time.time_ns())); attempts = 0
    for bi in c['pending_order']:
        if attempts >= args.max_attempts or R._CANCEL[0] or time.monotonic()+2550 > deadline: return
        it = task(bi)
        if (L/it['new_record']).exists():
            q = inspect(c,args.sha256,bi)
            if q['state'] in ('INTEGRITY_VETO','SAT_VETO','HALT_UNKNOWN'): raise RuntimeError('persistent existing veto '+repr(q))
            continue  # every previous UNKNOWN remains, no direct retry
        if not TX.claim(it['claim'],args.sha256,it['id']): continue
        recipe = {'mode':'direct','multiset':6,'b_index':bi,'indices':None,'skeleton_path':SK,
                  'skeleton_sha256':c['skeleton_sha256'],'encoder_sha256':c['source_sha256']['src/encode_skel_b.py']}
        def build():
            verify(c)
            sk = D['skeletons'][bi]
            nv,cl = ENC.build_v2(D['c0'],[tuple(t) for t in sk['types']],sk['empty'],special)
            return ENC.cnf_bytes(nv,cl)
        paths = TX.item_paths(it,stage)
        r = OWNER.execute(build,recipe,args.sha256,c['source_sha256'],paths,deadline,admission,'cadical',300)
        if r.get('unattempted') == 'before-pin' and not (L/it['pin']).exists():
            TX.release_unattempted(it['claim'],'v3.1 rule1: direct refused before pin/job; no record or HALT'); return
        if r.get('unattempted') == 'after-pin-before-worker':
            TX.retire_unattempted_after_pin(it,paths,'v3.1 rule2: direct refused before worker; no record or HALT'); return
        if not r.get('pre_child_pin_sha256'):
            TX.release_unattempted(it['claim'],'v3.1 direct construction incomplete before immutable pin/native'); return
        r.update(runner='run_m2_ms06_direct_v3_1.py',count_for_scientific_coverage=True)
        raw = (json.dumps(r,indent=1)+'\n').encode(); rh = hashlib.sha256(raw).hexdigest()
        COMMON.publish_json(L/it['commit'],{'schema':'PA19-K1-RECEIPT-v3.1','production_contract_sha256':args.sha256,
            'b_index':bi,'record_sha256':rh,'pin_sha256':r['pre_child_pin_sha256']},stage)
        COMMON.publish_bytes(L/it['new_record'],raw,stage)
        attempts += 1
        print(json.dumps({'job':'6:%d' % bi,'record':it['new_record'],'sha256':rh,'status':r['status'],
                          'checked':r['checked'],'integrity_status':r['integrity_status']}),flush=True)
        for gate in (r.get('native_result') or {}).get('gates') or []:
            if gate.get('census'): admission['census_reference'] = gate['census']['reference']
        if r.get('sat_candidate') or r.get('integrity_status') == 'INVALID' or r.get('halt_production') or r.get('chunk_stop'): return


if __name__ == '__main__':
    main()
