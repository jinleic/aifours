#!/usr/bin/env python3
"""Unchanged full B100 ms09 cover through reviewed-v2 measured transport; explicit parent PASS/GO before launch.
Primary queue: ascending COMPLETE placement count then interval index. Validation queue: the14 frozen identities,
seven calibration inputs first, then seven historical inputs; invoke only after parent's open-M2 priority release.
No original/calibration file is changed. One _k1 attempt/input; UNKNOWN is never automatically retried. All native
work lives inside unchanged supervise_r3 while the outer owner holds token+bigmem through known quiescence/veto.
One <=3h chunk INCLUDING waits. Same Kissat600/check1200 and proof caps; COUNT<=2; no proof/CNF disk copies.
"""
import argparse
import datetime
import hashlib
import json
import os
import time
from pathlib import Path

import lane_new_data_accounting as ACCOUNT
import m2_item_owner_v2 as OWNER
import m2_ms09_contract as C
import m2_ms09_evidence as E
import m2_supervised_runtime_v2 as R

L = C.LANE


def claim(path,contract_sha,ident):
    p = L/path
    p.parent.mkdir(parents=True,exist_ok=True)
    try: fd = os.open(p,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o644)
    except FileExistsError: return False
    try: os.write(fd,('%d %s %s %s\n' % (os.getpid(),time.strftime('%Y-%m-%dT%H:%M:%S%z'),contract_sha,ident)).encode())
    finally: os.close(fd)
    return True


def release_unattempted(path,reason):
    src = L/path
    dst = L/'archive'/'k1-unattempted-claims'/('%s.%d' % (src.name,time.time_ns()))
    dst.parent.mkdir(parents=True,exist_ok=True)
    assert not dst.exists()
    h = E.digest(src)
    os.rename(src,dst)
    with (L/'archive'/'MANIFEST.tsv').open('a') as f:
        f.write('%s\t%s\t%s\t%s\t%s\n' % (time.strftime('%Y-%m-%dT%H:%M:%S%z'),path,str(dst.relative_to(L)),h,reason))


def item_paths(it,stage):
    base = L/it['new_record']
    return {'id':it['id'],'pin':L/it['pin'],'staging':stage,'job':Path(str(base)+'.job.json'),
            'supervisor':Path(str(base)+'.supervisor.json'),'quarantine':Path(str(base)+'.quarantine.json'),
            'worker_result':Path(str(base)+'.worker.json'),
            'workdir':L/'scratch'/'fifo'/('m2k1_t%d_' % it['tier']+it['id'].replace(':','_').replace('-','_'))}


def work_items(c,byid,order):
    """After the last tier1 input for a case in this queue, consider its exact eligible tier2s in index order."""
    last = {byid[ident][0]['b_index']:i for i,ident in enumerate(order)}
    for i,ident in enumerate(order):
        yield ident,1
        ca,_ = byid[ident]
        if last[ca['b_index']] == i:
            tasks = [ca['direct_task']] if ca.get('direct') else ca['intervals']
            for task in tasks:
                if C.tier2_eligible(c,ca,task):
                    yield task['id'],2


def publish_item(r,c,contract_sha,ca,it,stage):
    """Actual production transaction; used directly by required receipt/resume controls too."""
    idx = it['indices']
    r.update(multiset=9,b_index=ca['b_index'],indices=idx,
        encoder='encode_skel_b.build_v2' if idx is None else 'encode_skel_b.build_partbatch',
        runner='run_m2_ms09_k1.py',production_contract_sha256=contract_sha,count_for_scientific_coverage=True)
    if idx is not None:
        r.update(list_sha256=ca['list']['sha256'],complete_denominator=ca['list']['n'],enumerator='extend_b.py')
    if r['status'] in ('SAT','INVALID'):
        assert (L/'cycle2'/('m2k1-'+r['status']+'.flag')).exists(), 'owner must persist veto before releasing locks'
    elif r.get('halt_production'):
        assert (L/'cycle2'/'m2k1-HALT.flag').exists() or (L/'cycle2'/'m2k1-QUARANTINE.flag').exists()
    raw = (json.dumps(r,indent=1)+'\n').encode()
    assert len(raw) <= 16*1024**2, 'single halting diagnostic bound exceeded'
    rh = hashlib.sha256(raw).hexdigest()
    commit = {'schema':'PA19-K1-RECEIPT-v2','production_contract_sha256':contract_sha,'b_index':ca['b_index'],
              'indices':idx,'tier':it['tier'],'record_sha256':rh,'pin_sha256':r.get('pre_child_pin_sha256'),
              'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z')}
    C.publish_json(L/it['commit'],commit,stage)
    C.publish_bytes(L/it['new_record'],raw,stage)  # PRIMARY LAST; immutable pin/commit already visible
    n = r.get('native_result') or {}
    return {'id':it['id'],'record':it['new_record'],'record_sha256':rh,'pin_sha256':r.get('pre_child_pin_sha256'),
            'status':r['status'],'checked':r.get('checked') is True,'solve_seconds':n.get('solve_seconds'),
            'check_seconds':n.get('check_seconds'),'proof_bytes':n.get('proof_stream',{}).get('raw_bytes'),
            'cnf_sha256':r.get('cnf_sha256'),'halt_production':r.get('halt_production')}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('contract'); ap.add_argument('sha256')
    ap.add_argument('--max-attempts',type=int)
    ap.add_argument('--queue',choices=('open','validation'),default='open')
    ap.add_argument('--parent-priority-release',help='Exact parent decision reference required to invoke validation queue')
    args = ap.parse_args()
    if args.max_attempts is not None: assert args.max_attempts > 0
    if args.queue == 'validation': assert args.parent_priority_release, 'do not silently reorder validation ahead of open M2 work'
    R.install_handlers()
    cutoff = datetime.datetime.fromisoformat('2026-10-18T18:31:43-07:00').timestamp()
    deadline = min(time.monotonic()+10800,time.monotonic()+max(0,cutoff-time.time()))
    runid = '%s-%d-%d' % (time.strftime('%Y%m%dT%H%M%S'),os.getpid(),time.time_ns())
    stage,logs = L/'scratch'/'m2k1-publish'/runid,L/'cycle2'/'m2k1-chunks'/runid
    logs.mkdir(parents=True,exist_ok=False)
    try:
        with R.Capacity(deadline,metadata=True,wait_allowance=60):
            c = C.load(args.contract,args.sha256)
            assert E.digest('/opt/homebrew/bin/kissat') == c['kissat_binary_sha256'] and E.digest(L/'tools/drat-trim/drat-trim') == c['drat_trim_binary_sha256']
            initial = C.inventory(c,args.sha256)
            assert not initial['sat_veto'] and not initial['integrity_issues'], 'persistent SAT/INVALID/safety veto'
            byid = {it['id']:(ca,it) for ca in c['cases'] for it in ca['intervals']}
            byid['b00001:direct'] = c['cases'][1],c['cases'][1]['direct_task']
            order = c['pending_order'] if args.queue == 'open' else c['validation_order']
            if args.queue == 'validation':
                assert all((L/byid[x][1]['new_record']).exists() for x in c['pending_order']), 'unattempted ms09 primary work takes priority'
            accounting = ACCOUNT.account(L)
            allids = c['pending_order']+c['validation_order']
            remaining = 2*sum(not (L/byid[x][1]['new_record']).exists() for x in allids)
            remaining += sum(C.tier2_eligible(c,*byid[x]) and not (L/C.new_task(byid[x][0]['b_index'],byid[x][1]['indices'],2)['new_record']).exists() for x in allids)
            bound = R.ALL_PLANNED_RETAINED_BOUND
            assert accounting['known'] and accounting['new_data_usage_upper_bytes']+bound <= ACCOUNT.ENFORCED_CAP_BYTES
            envelope = {'known':True,'upper_bytes':accounting['new_data_usage_upper_bytes']+bound,
                        'policy':'fresh chunk census plus ALL remaining normal inputs and one capacity-held halting diagnostic reserve',
                        'ordinary_bytes_per_input':R.ITEM_ORDINARY_BOUND,'one_failure_reserve_bytes':R.ROUTE_FAILURE_RESERVE}
            tranche = min(remaining,args.max_attempts) if args.max_attempts is not None else remaining
            fresh = (lambda s:s.f_bavail*s.f_frsize)(os.statvfs(L))
            required = R.BASE_GATE+tranche*R.ITEM_ORDINARY_BOUND+R.ROUTE_FAILURE_RESERVE
            assert fresh >= required, 'full planned retained tranche does not fit fresh growth gate'
            C.publish_json(logs/'admission.json',{'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
                'contract_sha256':args.sha256,'fresh_free_bytes':fresh,'required_free_bytes':required,
                'current_new_data':accounting,'accounting_envelope':envelope,'queue':args.queue,
                'parent_priority_release':args.parent_priority_release,'deadline_monotonic':deadline},stage)
    except BaseException as exc:
        C.publish_json(logs/'initialization-deferred.json',{'status':'UNKNOWN/deferred','reason':repr(exc),
            'native_has_started':False,'contract_sha256':args.sha256,'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z')},stage)
        print(logs,repr(exc),flush=True)
        return
    records,attempts,stop = [],0,None
    for ident,tier in work_items(c,byid,order):
        if args.max_attempts is not None and attempts >= args.max_attempts:
            stop = 'operational tranche reached; mathematical target unchanged'; break
        if R._CANCEL[0] or time.monotonic()+2550 > deadline:
            stop = 'deadline/cancellation; no new native'; break
        ca,first = byid[ident]
        it = first if tier == 1 else C.new_task(ca['b_index'],first['indices'],2)
        prior = None if tier == 1 else {'path':first['new_record'],'sha256':E.digest(L/first['new_record'])}
        if (L/it['new_record']).exists():
            q = C.inspect_new(c,args.sha256,ca,it)
            if q['state'] in ('INVALID','SAT','HALT_UNKNOWN'):
                stop = 'existing persistent veto '+ident; break
            continue  # QUALIFIED or preserved first-attempt UNKNOWN; no retry.
        if not claim(it['claim'],args.sha256,ident):
            continue  # another/stale owner; never reclaim or infer completion.
        recipe = {'mode':'direct' if it['indices'] is None else 'partbatch','multiset':9,'b_index':ca['b_index'],
            'indices':it['indices'],'skeleton_path':c['skeleton_path'],'skeleton_sha256':c['skeleton_sha256'],
            'encoder_sha256':c['source_sha256']['src/encode_skel_b.py']}
        if it['indices'] is not None:
            recipe.update(list_path=ca['list']['path'],list_sha256=ca['list']['sha256'],complete_denominator=ca['list']['n'])
        def build():
            assert E.digest(args.contract) == args.sha256
            for rel,h in c['source_sha256'].items():
                assert E.digest(L/rel) == h, ('source changed after token wait',rel)
            assert not (L/it['new_record']).exists()
            raw = C.formula(c,ca,it['indices'])
            val = next((x for x in c['validation_tasks'] if x['id'] == ident),None)
            if val:
                assert len(raw) == val['expected']['cnf_bytes'] and hashlib.sha256(raw).hexdigest() == val['expected']['cnf_sha256']
            return raw
        paths = item_paths(it,stage)
        try:
            r = OWNER.execute(build,recipe,args.sha256,c['source_sha256'],paths,deadline,envelope,tier=tier,prior=prior)
        except BaseException as exc:
            C.publish_json(logs/('owner-exception-'+ident.replace(':','_')+'.json'),{'status':'UNKNOWN','reason':repr(exc),'id':ident},stage)
            stop = 'owner admission/exception; no automatic retry: '+repr(exc)
            if not (L/it['pin']).exists(): release_unattempted(it['claim'],'owner refused before immutable pin/native group')
            break
        if not r.get('pre_child_pin_sha256'):
            C.publish_json(logs/('deferred-'+ident.replace(':','_')+'.json'),r,stage)
            release_unattempted(it['claim'],'constructor/pin incomplete; no native group could start')
            stop = 'pre-pin deferred'; break
        attempts += 1
        item = publish_item(r,c,args.sha256,ca,it,stage)
        records.append(item)
        print(json.dumps(item),flush=True)
        if r['status'] in ('SAT','INVALID') or r.get('halt_production'):
            stop = 'persistent '+r['status']+'/safety veto'; break
    C.publish_json(logs/'summary.json',{'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'production_contract_sha256':args.sha256,'queue':args.queue,'attempts':attempts,'records':records,
        'stop_reason':stop,'all_original_outcomes_unchanged':True,'no_global_PA19_verdict':True},stage)
    print(logs,flush=True)


if __name__ == '__main__':
    main()
