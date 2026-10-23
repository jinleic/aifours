#!/usr/bin/env python3
"""Historical-M2 (A2 ms01..ms08) measured re-solve over the v6_1 transport (= reviewed v6 owner/worker/evidence with the
supervisor pin moved to supervise_pa19_v4.py; nothing else changed in the transport).
Each item regenerates its ORIGINAL independent-B formula and must reproduce the bound historical CNF bytes/SHA before any
pin; otherwise it is refused unattempted (no record/HALT; a binding receipt is kept) and the chunk ends. CaDiCaL at the
original 300/600 limit, drat-trim 1200, the same exact measured predicate, one attempt, no automatic retry. Shared
registry veto/resource-stop scan before any claim; v6 refusal rules. The whole-plan retained-data bound is the runtime
plan bound PLUS every M2H item at the ordinary per-item bound. Historical receipts stay ORIGINAL-QUALIFIED only.
Parent source GO required before running.
"""
import argparse
import datetime
import hashlib
import json
import os
import time

import encode_skel_b as ENC
import m2_item_owner_v6_1 as OWNER
import m2_ms09_contract_v6_1 as COMMON
import m2_ms09_evidence_v6_1 as E
import m2_supervised_runtime_v6_1 as R
import run_m2_ms09_k1_v6_1 as TX

L = COMMON.LANE
SCHEMA = 'PA19-M2H-A2-v6_1'
EXTRA_SOURCES = ('src/freeze_m2h_v6_1.py','src/run_m2h_v6_1.py','src/final_m2h_inventory_v6_1.py')


def resource_policy(n_items):
    p = COMMON.resource_policy()
    p['whole_plan_remaining_bound_bytes'] = R.ALL_PLANNED_RETAINED_BOUND+n_items*R.ITEM_ORDINARY_BOUND
    p['m2h_items_added_at_ordinary_bound'] = n_items
    return p


def task(item):
    if item['mode'] == 'direct':
        base = 'cycle2/m2skel_drat/ms%02d_b%05d_h6_1' % (item['multiset'],item['b_index'])
        claim = 'cycle2/claims/m2h6_1_ms%02d_b%05d.claim' % (item['multiset'],item['b_index'])
    else:
        lo,hi = item['indices']
        base = 'cycle2/m2part_drat/ms%02d_b%05d/batch_%05d_%05d_h6_1' % (item['multiset'],item['b_index'],lo,hi)
        claim = 'cycle2/claims/m2h6_1_ms%02d_b%05d_%05d_%05d.claim' % (item['multiset'],item['b_index'],lo,hi)
    return {'id':item['id'],'indices':item['indices'],'new_record':base+'.json','pin':base+'.cnf-pin.json',
            'commit':base+'.receipt.json','claim':claim}


def verify_sources(c):
    assert c['schema'] == SCHEMA and set(c['source_sha256']) == set(tuple(COMMON.SOURCE_FILES)+EXTRA_SOURCES)
    for p,h in c['source_sha256'].items(): assert E.digest(L/p) == h, ('frozen source changed',p)
    assert c['supervisor'] == {'path':str(R.SUP_PATH),'sha256':R.SUP_SHA} and E.digest(R.SUP_PATH) == R.SUP_SHA


def verify(c):
    verify_sources(c)
    assert c['resource_policy'] == resource_policy(len(c['items'])) and c['automatic_retry_allowed'] is False and c['check_seconds'] == 1200
    assert c['binary_authority']['solver']['path'] == '/opt/homebrew/bin/cadical'
    assert c['binary_authority']['checker']['path'] == str(L/'tools/drat-trim/drat-trim')
    for mi,s in c['skeletons'].items(): assert s['path'] == 'cycle2/skel-b/skeletons-b-ms%02d.json' % int(mi) and E.digest(L/s['path']) == s['sha256']
    assert c['order'] == [x['id'] for x in c['items']] and len(set(c['order'])) == len(c['order'])
    lists = {}
    for x in c['items']:
        assert x['solver'] == 'cadical' and x['native_seconds'] in (300,600) and type(x['multiset']) is int and 1 <= x['multiset'] <= 8
        assert E.digest(L/x['historical']['path']) == x['historical']['sha256'], ('historical receipt changed',x['id'])
        if x['mode'] == 'partbatch':
            lists.setdefault(x['list']['path'],(x['list']['sha256'],x['list']['n'],(x['multiset'],x['b_index'])))
            assert lists[x['list']['path']] == (x['list']['sha256'],x['list']['n'],(x['multiset'],x['b_index']))
        else: assert x['mode'] == 'direct' and x['indices'] is None
    for path,(h,n,case) in lists.items():
        assert E.digest(L/path) == h
        got = sorted(x['indices'] for x in c['items'] if x['mode'] == 'partbatch' and (x['multiset'],x['b_index']) == case)
        assert got == [[lo,min(n,lo+100)-1] for lo in range(0,n,100)], ('split item set is not the exact complete B100 partition',case)


def recipe(c,x):
    r = {'mode':x['mode'],'multiset':x['multiset'],'b_index':x['b_index'],'indices':x['indices'],
         'skeleton_path':c['skeletons'][str(x['multiset'])]['path'],'skeleton_sha256':c['skeletons'][str(x['multiset'])]['sha256'],
         'encoder_sha256':c['source_sha256']['src/encode_skel_b.py']}
    if x['mode'] == 'partbatch': r.update(list_path=x['list']['path'],list_sha256=x['list']['sha256'],complete_denominator=x['list']['n'])
    return r


def inspect(c,h,x):
    it = task(x)
    if not (L/it['new_record']).exists(): return {'state':'MISSING','record':None,'errors':[]}
    try:
        pin,k = COMMON.read(L/it['pin']),COMMON.read(L/it['commit'])
        assert pin['schema'] == 'PA19-K1-CNF-PIN-v6_1' and k['schema'] == 'PA19-K1-RECEIPT-v6_1'
        assert pin['production_contract_sha256'] == k['production_contract_sha256'] == h
        assert type(pin['multiset']) is int and pin['multiset'] == x['multiset'] and type(pin['b_index']) is int and pin['b_index'] == k['b_index'] == x['b_index']
        assert pin['indices'] == x['indices'] == k['indices'] and pin['recipe'] == recipe(c,x)
        assert pin['source_sha256'] == c['source_sha256'] and pin['binary_authority'] == c['binary_authority']
        assert pin['cnf_sha256'] == x['expected_cnf_sha256'] and pin['cnf_bytes'] == x['expected_cnf_bytes']
        assert k['pin_sha256'] == E.digest(L/it['pin']) and k['record_sha256'] == E.digest(L/it['new_record'])
        enc = 'encode_skel_b.build_v2' if x['mode'] == 'direct' else 'encode_skel_b.build_partbatch'
        ex = E.expected(x['multiset'],x['b_index'],x['indices'],pin['cnf_sha256'],pin['cnf_bytes'],enc,x['native_seconds'],False)
        ex.update(binary_authority=c['binary_authority'],lane_root=str(L),source_sha256=c['source_sha256'],recipe=pin['recipe'])
        return E.inspect(L/it['new_record'],ex,k['record_sha256'])
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as exc:
        return {'state':'INTEGRITY_VETO','errors':[repr(exc)]}


def formula(c,x,skeletons):
    D = skeletons[x['multiset']]; sk = D['skeletons'][x['b_index']]
    special = [p for p in D['profiles'] if list(p) != COMMON.P0]
    if x['mode'] == 'direct':
        nv,cl = ENC.build_v2(D['c0'],[tuple(t) for t in sk['types']],sk['empty'],special)
    else:
        assert E.digest(L/x['list']['path']) == x['list']['sha256']
        ed = COMMON.read(L/x['list']['path']); lo,hi = x['indices']
        assert ed['num_placements'] == len(ed['placements']) == x['list']['n']
        nv,cl = ENC.build_partbatch(D['c0'],[tuple(t) for t in sk['types']],sk['empty'],special,[ed['placements'][i] for i in range(lo,hi+1)])
    return ENC.cnf_bytes(nv,cl)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('contract'); ap.add_argument('sha256'); ap.add_argument('--max-attempts',type=int)
    args = ap.parse_args(); R.install_handlers()
    cutoff = datetime.datetime.fromisoformat('2026-10-18T18:31:43-07:00').timestamp()
    deadline = min(time.monotonic()+10800,time.monotonic()+max(0,cutoff-time.time()))
    logs = L/'cycle2/m2h6_1-chunks'/('%s-%d' % (time.strftime('%Y%m%dT%H%M%S'),time.time_ns())); logs.mkdir(parents=True,exist_ok=False)
    stage = L/'scratch/m2h-publish'/logs.name
    with R.Capacity(deadline,metadata=True,wait_allowance=60):
        st = os.statvfs(L); assert st.f_bavail*st.f_frsize >= R.BASE_GATE+1024**2
        assert E.digest(args.contract) == args.sha256
        c = COMMON.read(args.contract); verify(c)
        union = R.admission_union(L)
        record_vetoes = {x['id']:s for x in c['items'] if (L/task(x)['new_record']).exists()
                         for s in [inspect(c,args.sha256,x)['state']] if s in ('INTEGRITY_VETO','SAT_VETO','HALT_UNKNOWN')}
        if union['persistent_vetoes'] or union['resource_stops'] or record_vetoes:
            COMMON.publish_json(logs/'initialization-deferred.json',{'status':'UNKNOWN','admission_union':union,'record_vetoes':record_vetoes,
                'init_stage':'veto-scan' if (union['persistent_vetoes'] or record_vetoes) else 'resource-stop','native_has_started':False,
                'contract_sha256':args.sha256,'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z')},stage)
            print('M2H initialization refusal',union,record_vetoes,flush=True); return
        assert all(v['matches'] for v in R.binary_observations(c['binary_authority']).values())
        bound = c['resource_policy']['whole_plan_remaining_bound_bytes']
        reference = R.create_census(); census = R.census_for_gate(reference)
        assert census['current_data_upper_bytes']+bound+R.OTHER_WRITER_MARGIN <= R.DATA_CAP
        admission = {'binary_authority':c['binary_authority'],'census_reference':reference,'whole_plan_remaining_bound_bytes':bound}
        skeletons = {int(k):COMMON.read(L/v['path']) for k,v in c['skeletons'].items()}
    records,attempts,stop = [],0,None
    for x in c['items']:
        if args.max_attempts is not None and attempts >= args.max_attempts: stop = 'operational tranche reached'; break
        if R._CANCEL[0] or time.monotonic()+2550 > deadline: stop = 'deadline/cancellation; no new native'; break
        it = task(x)
        if (L/it['new_record']).exists():
            q = inspect(c,args.sha256,x)
            if q['state'] in ('INTEGRITY_VETO','SAT_VETO','HALT_UNKNOWN'): stop = 'existing persistent veto '+x['id']; break
            continue  # every previous UNKNOWN remains; no retry
        if not TX.claim(it['claim'],args.sha256,it['id']): continue

        def build():
            assert E.digest(args.contract) == args.sha256
            verify_sources(c)
            assert not (L/it['new_record']).exists()
            ref = c['skeletons'][str(x['multiset'])]
            assert E.digest(L/ref['path']) == ref['sha256'] and E.digest(L/x['historical']['path']) == x['historical']['sha256']
            raw = formula(c,x,skeletons)
            if len(raw) != x['expected_cnf_bytes'] or hashlib.sha256(raw).hexdigest() != x['expected_cnf_sha256']:
                raise LookupError('regenerated formula differs from bound historical receipt CNF')
            return raw
        paths = TX.item_paths(it,stage)
        try:
            r = OWNER.execute(build,recipe(c,x),args.sha256,c['source_sha256'],paths,deadline,admission,'cadical',x['native_seconds'])
        except BaseException as exc:
            COMMON.publish_json(logs/('owner-exception-'+x['id'].replace(':','_')+'.json'),{'status':'UNKNOWN','reason':repr(exc),'id':x['id']},stage)
            if not (L/it['pin']).exists(): TX.release_unattempted(it['claim'],'M2H owner refused before pin/native')
            stop = 'owner admission/exception'; break
        if r.get('unattempted') == 'before-pin' and not (L/it['pin']).exists():
            TX.release_unattempted(it['claim'],'refusal rule1: M2H refused before pin/job; no record or HALT'); stop = 'pre-pin refusal'; break
        if r.get('unattempted') == 'after-pin-before-worker':
            TX.retire_unattempted_after_pin(it,paths,'refusal rule2: M2H refused before worker; no record or HALT'); stop = 'pre-worker refusal'; break
        if not r.get('pre_child_pin_sha256'):
            COMMON.publish_json(logs/('binding-or-construction-'+x['id'].replace(':','_')+'.json'),r,stage)
            TX.release_unattempted(it['claim'],'M2H construction/binding refused before immutable pin/native'); stop = 'construction/binding refusal'; break
        r.update(runner='run_m2h_v6_1.py',count_for_scientific_coverage=True,historical_receipt=x['historical'])
        if x['mode'] == 'partbatch': r.update(list_sha256=x['list']['sha256'],complete_denominator=x['list']['n'],enumerator='extend_b.py')
        raw = (json.dumps(r,indent=1)+'\n').encode(); rh = hashlib.sha256(raw).hexdigest()
        COMMON.publish_json(L/it['commit'],{'schema':'PA19-K1-RECEIPT-v6_1','production_contract_sha256':args.sha256,'b_index':x['b_index'],
            'indices':x['indices'],'record_sha256':rh,'pin_sha256':r['pre_child_pin_sha256']},stage)
        COMMON.publish_bytes(L/it['new_record'],raw,stage)  # primary LAST
        attempts += 1
        item = {'id':x['id'],'record':it['new_record'],'sha256':rh,'status':r['status'],'checked':r['checked'],'integrity_status':r['integrity_status']}
        records.append(item); print(json.dumps(item),flush=True)
        for gate in (r.get('native_result') or {}).get('gates') or []:
            if gate.get('census'): admission['census_reference'] = gate['census']['reference']
        if r.get('sat_candidate') or r.get('integrity_status') == 'INVALID' or r.get('halt_production'): stop = 'persistent veto'; break
        if r.get('chunk_stop'): stop = 'worker admission refusal recorded UNKNOWN; chunk ends'; break
    COMMON.publish_json(logs/'summary.json',{'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'contract_sha256':args.sha256,'attempts':attempts,
        'records':records,'stop_reason':stop,'automatic_retry_allowed':False},stage)
    print(logs,flush=True)


if __name__ == '__main__':
    main()
