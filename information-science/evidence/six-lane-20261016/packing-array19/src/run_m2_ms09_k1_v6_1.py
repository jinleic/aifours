#!/usr/bin/env python3
"""Frozen complete independent-B ms09 cover through measured v3. Parent source PASS/GO before native controls/run.
One attempt/input, no automatic retry. All supervisor stops remain UNKNOWN plus persistent safety hold. Primary
ascending complete-list size/index queue precedes14 explicitly released exact-input validations. Old outcomes stay.
"""
import argparse
import datetime
import hashlib
import json
import os
import time
from pathlib import Path

import m2_item_owner_v6_1 as OWNER
import m2_ms09_contract_v6_1 as C
import m2_ms09_evidence_v6_1 as E
import m2_supervised_runtime_v6_1 as R

L = C.LANE


def claim(path,contract_sha,ident):
    p = L/path; p.parent.mkdir(parents=True,exist_ok=True)
    try: fd = os.open(p,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o644)
    except FileExistsError: return False
    try: os.write(fd,('%d %s %s %s\n' % (os.getpid(),time.strftime('%Y-%m-%dT%H:%M:%S%z'),contract_sha,ident)).encode())
    finally: os.close(fd)
    return True


def release_unattempted(path,reason):
    src = L/path; dst = L/'archive/k1-v6_1-unattempted'/('%s.%d' % (src.name,time.time_ns()))
    dst.parent.mkdir(parents=True,exist_ok=True); assert not dst.exists()
    h = E.digest(src); os.rename(src,dst)
    with (L/'archive/MANIFEST.tsv').open('a') as f:
        f.write('%s\t%s\t%s\t%s\t%s\n' % (time.strftime('%Y-%m-%dT%H:%M:%S%z'),path,str(dst.relative_to(L)),h,reason))


def retire_unattempted_after_pin(it,paths,reason):
    """refusal rule2: own pin/job/claim only, after proving no worker/supervisor/quarantine artifact exists."""
    for key in ('supervisor','worker_result','quarantine'):
        assert not Path(paths[key]).exists(), ('worker group evidence exists; not unattempted',key)
    assert not (L/it['new_record']).exists() and not (L/it['commit']).exists()
    for rel in (it['pin'],str(Path(paths['job']).relative_to(L)),it['claim']):
        if (L/rel).exists(): release_unattempted(rel,reason)


def item_paths(it,stage):
    base = L/it['new_record']
    return {'id':it['id'],'pin':L/it['pin'],'staging':stage,'job':Path(str(base)+'.job.json'),
        'supervisor':Path(str(base)+'.supervisor.json'),'quarantine':Path(str(base)+'.quarantine.json'),
        'worker_result':Path(str(base)+'.worker.json'),
        'workdir':L/'scratch/fifo'/('m2k1_v6_1_'+it['id'].replace(':','_').replace('-','_'))}


def publish_item(r,c,contract_sha,ca,it,stage):
    idx = it['indices']
    r.update(multiset=9,b_index=ca['b_index'],indices=idx,encoder='encode_skel_b.build_v2' if idx is None else 'encode_skel_b.build_partbatch',
             runner='run_m2_ms09_k1_v6_1.py',production_contract_sha256=contract_sha,count_for_scientific_coverage=True)
    if idx is not None: r.update(list_sha256=ca['list']['sha256'],complete_denominator=ca['list']['n'],enumerator='extend_b.py')
    if r.get('sat_candidate'): assert (L/'cycle2/m2k3-SAT.flag').exists()
    elif r.get('integrity_status') == 'INVALID': assert (L/'cycle2/m2k3-INTEGRITY.flag').exists()
    elif r.get('halt_production'): assert (L/'cycle2/m2k3-HALT.flag').exists() or (L/'cycle2/m2k3-QUARANTINE.flag').exists()
    raw = (json.dumps(r,indent=1)+'\n').encode(); assert len(raw) <= 16*1024**2
    rh = hashlib.sha256(raw).hexdigest()
    C.publish_json(L/it['commit'],{'schema':'PA19-K1-RECEIPT-v6_1','production_contract_sha256':contract_sha,
        'b_index':ca['b_index'],'indices':idx,'record_sha256':rh,'pin_sha256':r.get('pre_child_pin_sha256'),
        'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z')},stage)
    C.publish_bytes(L/it['new_record'],raw,stage)  # primary LAST, immutable pin and commit already exist
    n = r.get('native_result') or {}
    return {'id':it['id'],'record':it['new_record'],'record_sha256':rh,'status':r['status'],'checked':r.get('checked') is True,
        'integrity_status':r.get('integrity_status'),'halt_production':r.get('halt_production'),
        'solve_seconds':n.get('solve_seconds'),'check_seconds':n.get('check_seconds'),'proof_bytes':n.get('proof_stream',{}).get('raw_bytes'),
        'cnf_sha256':r.get('cnf_sha256')}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('contract'); ap.add_argument('sha256')
    ap.add_argument('--max-attempts',type=int); ap.add_argument('--queue',choices=('open','validation'),default='open')
    ap.add_argument('--parent-priority-release')
    args = ap.parse_args()
    if args.max_attempts is not None: assert args.max_attempts > 0
    if args.queue == 'validation': assert args.parent_priority_release, 'explicit parent open-M2 priority release required'
    R.install_handlers()
    cutoff = datetime.datetime.fromisoformat('2026-10-18T18:31:43-07:00').timestamp()
    deadline = min(time.monotonic()+10800,time.monotonic()+max(0,cutoff-time.time()))
    runid = '%s-%d-%d' % (time.strftime('%Y%m%dT%H%M%S'),os.getpid(),time.time_ns())
    stage,logs = L/'scratch/m2k1-v6_1-publish'/runid,L/'cycle2/m2k3-chunks'/runid
    logs.mkdir(parents=True,exist_ok=False)
    init = {'stage':'capacity','veto_detail':None}
    try:
        with R.Capacity(deadline,metadata=True,wait_allowance=60):
            init['stage'] = 'load'
            c = C.load(args.contract,args.sha256)
            init['stage'] = 'binary'
            assert all(o['matches'] for o in R.binary_observations(c['binary_authority']).values()), 'contract binary drift'
            init['stage'] = 'inventory'
            initial = C.inventory(c,args.sha256)
            init['veto_detail'] = {'sat_veto':initial['sat_veto'],'integrity_issues':initial['integrity_issues'][:50],
                                   'veto_markers':R.present_vetoes(L),'admission_union':R.admission_union(L)}
            assert not initial['sat_veto'] and not initial['integrity_issues'], 'persistent SAT/integrity/safety veto'
            init['stage'] = 'resource-stop'
            assert not R.present_resource_stops(L), 'resource STOP present (distinct from persistent veto)'
            init['stage'] = 'queue'
            byid = {it['id']:(ca,it) for ca in c['cases'] for it in ca['intervals']}
            byid['b00001:direct'] = c['cases'][1],c['cases'][1]['direct_task']
            order = c['pending_order'] if args.queue == 'open' else c['validation_order']
            if args.queue == 'validation': assert all((L/byid[x][1]['new_record']).exists() for x in c['pending_order'])
            init['stage'] = 'census'  # exact census at chunk start; later admissions refresh at age/wait>600s
            reference = R.create_census()
            admission = {'binary_authority':c['binary_authority'],'census_reference':reference,
                         'whole_plan_remaining_bound_bytes':c['resource_policy']['whole_plan_remaining_bound_bytes']}
            live = R.census_for_gate(reference)
            assert live['current_data_upper_bytes']+admission['whole_plan_remaining_bound_bytes']+R.OTHER_WRITER_MARGIN <= R.DATA_CAP
            fresh = (lambda s:s.f_bavail*s.f_frsize)(os.statvfs(L))
            assert fresh >= R.BASE_GATE+R.ITEM_GROWTH
            init['stage'] = 'admission-receipt'
            C.publish_json(logs/'admission.json',{'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'contract_sha256':args.sha256,
                'fresh_free_bytes':fresh,'admission':admission,'chunk_start_census':live,'queue':args.queue,
                'parent_priority_release':args.parent_priority_release,'deadline_monotonic':deadline,
                'accounting_residual':c['resource_policy']['residual']},stage)
    except BaseException as exc:
        C.publish_json(logs/'initialization-deferred.json',{'status':'UNKNOWN','reason':repr(exc),'init_stage':init['stage'],
            'veto_detail':init['veto_detail'],'native_has_started':False,'contract_sha256':args.sha256,
            'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z')},stage)
        print(logs,repr(exc),flush=True); return
    records,attempts,stop = [],0,None
    for ident in order:
        if args.max_attempts is not None and attempts >= args.max_attempts: stop = 'operational tranche reached'; break
        if R._CANCEL[0] or time.monotonic()+2550 > deadline: stop = 'deadline/cancellation; no new native'; break
        ca,it = byid[ident]
        if (L/it['new_record']).exists():
            q = C.inspect_new(c,args.sha256,ca,it)
            if q['state'] in ('INTEGRITY_VETO','SAT_VETO','HALT_UNKNOWN'): stop = 'existing persistent veto '+ident; break
            continue  # UNKNOWN is preserved, never automatically retried.
        if not claim(it['claim'],args.sha256,ident): continue
        recipe = {'mode':'direct' if it['indices'] is None else 'partbatch','multiset':9,'b_index':ca['b_index'],'indices':it['indices'],
            'skeleton_path':c['skeleton_path'],'skeleton_sha256':c['skeleton_sha256'],'encoder_sha256':c['source_sha256']['src/encode_skel_b.py']}
        if it['indices'] is not None: recipe.update(list_path=ca['list']['path'],list_sha256=ca['list']['sha256'],complete_denominator=ca['list']['n'])
        def build():
            assert E.digest(args.contract) == args.sha256
            for rel,h in c['source_sha256'].items(): assert E.digest(L/rel) == h, ('source changed after capacity wait',rel)
            assert not (L/it['new_record']).exists()
            raw = C.formula(c,ca,it['indices'])
            val = next((x for x in c['validation_tasks'] if x['id'] == ident),None)
            if val: assert len(raw) == val['expected']['cnf_bytes'] and hashlib.sha256(raw).hexdigest() == val['expected']['cnf_sha256']
            return raw
        paths = item_paths(it,stage)
        try: r = OWNER.execute(build,recipe,args.sha256,c['source_sha256'],paths,deadline,admission)
        except BaseException as exc:
            C.publish_json(logs/('owner-exception-'+ident.replace(':','_')+'.json'),{'status':'UNKNOWN','reason':repr(exc),'id':ident},stage)
            if not (L/it['pin']).exists(): release_unattempted(it['claim'],'owner refused before immutable pin/native')
            stop = 'owner admission/exception; no automatic retry'; break
        if r.get('unattempted') == 'before-pin' and not (L/it['pin']).exists():
            C.publish_json(logs/('unattempted-'+ident.replace(':','_')+'.json'),r,stage)
            release_unattempted(it['claim'],'refusal rule1: admission refused before pin/job; no record or HALT')
            stop = 'pre-pin admission refusal; item remains MISSING'; break
        if r.get('unattempted') == 'after-pin-before-worker':
            C.publish_json(logs/('unattempted-'+ident.replace(':','_')+'.json'),r,stage)
            retire_unattempted_after_pin(it,paths,'refusal rule2: refused after pin/job before any worker process; no record or HALT')
            stop = 'pre-worker admission refusal; item remains MISSING'; break
        if not r.get('pre_child_pin_sha256'):
            C.publish_json(logs/('deferred-'+ident.replace(':','_')+'.json'),r,stage)
            release_unattempted(it['claim'],'constructor/pin incomplete; no native group could start')
            stop = 'pre-pin deferred'; break
        attempts += 1
        item = publish_item(r,c,args.sha256,ca,it,stage); records.append(item); print(json.dumps(item),flush=True)
        newest = (r.get('owner_prespawn_gate') or {}).get('census')
        for gate in (r.get('native_result') or {}).get('gates') or []:
            if gate.get('census'): newest = gate['census']
        if newest: admission['census_reference'] = newest['reference']
        if r.get('sat_candidate') or r.get('integrity_status') == 'INVALID' or r.get('halt_production'):
            stop = 'persistent SAT/integrity/safety veto'; break
        if r.get('chunk_stop'):
            stop = 'worker admission refusal recorded UNKNOWN; chunk ends without persistent HALT'; break
    C.publish_json(logs/'summary.json',{'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'production_contract_sha256':args.sha256,
        'queue':args.queue,'attempts':attempts,'records':records,'stop_reason':stop,'all_original_outcomes_unchanged':True,
        'automatic_retry_allowed':False,'no_global_PA19_verdict':True},stage)
    print(logs,flush=True)


if __name__ == '__main__':
    main()
