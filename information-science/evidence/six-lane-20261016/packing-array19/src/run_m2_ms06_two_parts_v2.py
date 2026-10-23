#!/usr/bin/env python3
"""STATIC pending separate parent review: measured-v2 replay of the ALREADY APPROVED ms06 b68/b73 complete covers.
No enumeration, mathematical split, seed, native/check budget or proof-cap change. Original phase2 SHA fc5b8619...
is the denominator authority:117 original B100 intervals,10459+1115 placements. Source/contract freeze before run;
CaDiCaL300/check1200, common token/tier1-3.5GiB and sole-RSS-only exclusive tier2-7GiB transport. Original JSON stays.
This file is NOT in the currently reviewed19-file production pack; never infer launch GO from its existence.
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
import m2_ms09_contract as COMMON
import m2_ms09_evidence as E
import m2_supervised_runtime_v2 as R
import run_m2_ms09_k1 as TX

L = COMMON.LANE
PHASE = 'cycle2/ms06-two-batch-denominators-20261018T024846.json'
PHASE_SHA = 'fc5b86191bb977f7f08fa1996a2011f9f086be6bcce954887146a3035476f83c'
SK = 'cycle2/skel-b/skeletons-b-ms06.json'
SCHEMA = 'PA19-MS06-TWO-PARTS-v2'


def task(bi,indices,tier=1):
    lo,hi = indices
    base = 'cycle2/m2part_drat/ms06_b%05d/batch_%05d_%05d' % (bi,lo,hi)
    tail = '_v2' if tier == 1 else '_v2_t2'
    return {'id':'ms06_b%05d:%05d-%05d' % (bi,lo,hi),'indices':indices,'tier':tier,'new_record':base+tail+'.json',
            'pin':base+tail+'.cnf-pin.json','commit':base+tail+'.receipt.json',
            'claim':'cycle2/claims/ms06_two_parts_v2_t%d_b%05d_%05d_%05d.claim' % (tier,bi,lo,hi)}


def freeze():
    assert E.digest(L/PHASE) == PHASE_SHA
    phase,D = COMMON.read(L/PHASE),COMMON.read(L/SK)
    source = {rel:E.digest(L/rel) for rel in COMMON.SOURCE_FILES}
    source[str(Path(__file__).relative_to(L))] = E.digest(__file__)
    out = {'schema':SCHEMA,'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'phase_path':PHASE,'phase_sha256':PHASE_SHA,
           'skeleton_path':SK,'skeleton_sha256':E.digest(L/SK),'source_sha256':source,
           'solver_binary_sha256':E.digest('/opt/homebrew/bin/cadical'),'checker_binary_sha256':E.digest(L/'tools/drat-trim/drat-trim'),
           'native_seconds':300,'check_seconds':1200,'count_ceiling':2,'cases':[],
           'mathematical_scope':'ONLY the already approved6:68/6:73 complete first-P1 B100 covers; no new representation',
           'no_retry_except_exactly_one_sole_RSS_tier2':True,'no_empty_vacuity':True}
    assert [x['job'] for x in phase['cases']] == ['6:68','6:73']
    for entry in phase['cases']:
        bi = int(entry['job'].split(':')[1]); ep = entry['list_path']; ed = COMMON.read(L/ep)
        n = entry['exact_complete_orbit_denominator']
        assert E.digest(L/ep) == entry['list_sha256'] and n == ed['num_placements'] == len(ed['placements']) > 0
        assert ed['raw_class_assignments'] == entry['exact_raw_assignment_denominator'] and ed['automorphisms'] == entry['automorphisms']
        assert E.digest(L/entry['complete_pin']['path']) == entry['complete_pin']['sha256']
        sk = D['skeletons'][bi]; individual = hashlib.sha256(json.dumps(sk,sort_keys=True).encode()).hexdigest()
        assert individual == entry['skeleton_sha256']
        expected = [[lo,min(n,lo+100)-1] for lo in range(0,n,100)]
        assert [x['indices'] for x in entry['batches']] == expected and sum(b-a+1 for a,b in expected) == n
        ca = {'b_index':bi,'skeleton_sha256':individual,'list':{'path':ep,'sha256':entry['list_sha256'],
              'n':n,'raw':ed['raw_class_assignments'],'aut':ed['automorphisms']},'complete_pin':entry['complete_pin'],
              'source_direct_cnf_sha256':entry['source_cnf_sha256'],'intervals':[task(bi,idx) for idx in expected]}
        assert all(not (L/it['new_record']).exists() and not (L/it['claim']).exists() for it in ca['intervals'])
        out['cases'].append(ca)
    assert sum(len(x['intervals']) for x in out['cases']) == 117
    out['pending_order'] = [it['id'] for ca in sorted(out['cases'],key=lambda x:(x['list']['n'],x['b_index'])) for it in ca['intervals']]
    dest = L/'cycle2'/('m2-ms06-two-parts-v2-contract-'+time.strftime('%Y%m%dT%H%M%S')+'.json')
    h = COMMON.publish_json(dest,out,L/'scratch'/'m2k1-publish'/('ms06-two-parts-freeze-'+str(time.time_ns())))
    print(dest,h,flush=True)


def verify(c):
    assert c['schema'] == SCHEMA and c['phase_path'] == PHASE and c['phase_sha256'] == PHASE_SHA and E.digest(L/PHASE) == PHASE_SHA
    assert c['skeleton_path'] == SK and E.digest(L/SK) == c['skeleton_sha256']
    expected_sources = set(COMMON.SOURCE_FILES)|{str(Path(__file__).relative_to(L))}
    assert set(c['source_sha256']) == expected_sources
    for rel,h in c['source_sha256'].items(): assert E.digest(L/rel) == h
    assert c['native_seconds'] == 300 and c['check_seconds'] == 1200 and c['count_ceiling'] == 2
    assert [x['b_index'] for x in c['cases']] == [68,73]
    phase = COMMON.read(L/PHASE)
    for ca,authority in zip(c['cases'],phase['cases']):
        ed = COMMON.read(L/ca['list']['path']); n = ca['list']['n']
        assert ca['list']['sha256'] == authority['list_sha256'] == E.digest(L/ca['list']['path'])
        assert n == authority['exact_complete_orbit_denominator'] == ed['num_placements'] == len(ed['placements']) > 0
        assert ca['list']['raw'] == ed['raw_class_assignments'] == authority['exact_raw_assignment_denominator']
        assert ca['list']['aut'] == ed['automorphisms'] == authority['automorphisms']
        assert ca['skeleton_sha256'] == authority['skeleton_sha256'] and ca['complete_pin'] == authority['complete_pin']
        assert E.digest(L/ca['complete_pin']['path']) == ca['complete_pin']['sha256']
        assert [it['indices'] for it in ca['intervals']] == [[lo,min(n,lo+100)-1] for lo in range(0,n,100)]
        assert all(it == task(ca['b_index'],it['indices']) for it in ca['intervals'])
    order = [it['id'] for ca in sorted(c['cases'],key=lambda x:(x['list']['n'],x['b_index'])) for it in ca['intervals']]
    assert c['pending_order'] == order and len(order) == 117


def inspect(c,h,ca,it):
    p = L/it['new_record']
    if not p.exists(): return {'state':'MISSING','errors':[]}
    try:
        pin,commit = COMMON.read(L/it['pin']),COMMON.read(L/it['commit'])
        assert pin['schema'] == 'PA19-K1-CNF-PIN-v2' and commit['schema'] == 'PA19-K1-RECEIPT-v2'
        assert pin['production_contract_sha256'] == commit['production_contract_sha256'] == h
        assert pin['multiset'] == 6 and pin['b_index'] == commit['b_index'] == ca['b_index'] and pin['indices'] == commit['indices'] == it['indices']
        assert pin['tier'] == commit['tier'] == it['tier'] and pin['source_sha256'] == c['source_sha256']
        assert pin['recipe'] == recipe(c,ca,it)
        assert commit['pin_sha256'] == E.digest(L/it['pin']) and commit['record_sha256'] == E.digest(p)
        ex = E.expected(6,ca['b_index'],it['indices'],pin['cnf_sha256'],pin['cnf_bytes'],'encode_skel_b.build_partbatch',300,False)
        ex.update(lane_root=str(L),tier=it['tier'],tier1_prior=pin.get('tier1_prior'),source_sha256=c['source_sha256'],recipe=pin['recipe'],
                  solver_binary_sha256=c['solver_binary_sha256'],checker_binary_sha256=c['checker_binary_sha256'])
        return E.inspect(p,ex,commit['record_sha256'])
    except (OSError,ValueError,TypeError,KeyError,AssertionError) as exc:
        return {'state':'INVALID','errors':[repr(exc)]}


def recipe(c,ca,it):
    return {'mode':'partbatch','multiset':6,'b_index':ca['b_index'],'indices':it['indices'],
        'skeleton_path':c['skeleton_path'],'skeleton_sha256':c['skeleton_sha256'],
        'encoder_sha256':c['source_sha256']['src/encode_skel_b.py'],'list_path':ca['list']['path'],
        'list_sha256':ca['list']['sha256'],'complete_denominator':ca['list']['n']}


def work_items(c):
    for ca in sorted(c['cases'],key=lambda x:(x['list']['n'],x['b_index'])):
        for it in ca['intervals']: yield ca,it,None
        if all((L/it['new_record']).exists() for it in ca['intervals']):
            for first in ca['intervals']:
                r = COMMON.read(L/first['new_record'])
                if r.get('status') == 'UNKNOWN' and r.get('rss_retry_eligible') is True and R.rss_only_retry(r.get('supervisor'),1,r.get('native_result')):
                    yield ca,task(ca['b_index'],first['indices'],2),{'path':first['new_record'],'sha256':E.digest(L/first['new_record'])}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('contract',nargs='?'); ap.add_argument('sha256',nargs='?')
    ap.add_argument('--freeze',action='store_true'); ap.add_argument('--max-attempts',type=int,default=100)
    args = ap.parse_args(); R.install_handlers()
    cutoff = datetime.datetime.fromisoformat('2026-10-18T18:31:43-07:00').timestamp()
    deadline = min(time.monotonic()+10800,time.monotonic()+max(0,cutoff-time.time()))
    with R.Capacity(deadline,metadata=True,wait_allowance=60):
        st = os.statvfs(L); assert st.f_bavail*st.f_frsize >= R.BASE_GATE+1024**2
        if args.freeze: freeze(); return
        assert args.contract and E.digest(args.contract) == args.sha256
        c = COMMON.read(args.contract); verify(c)
        account = ACCOUNT.account(L)
        assert account['known'] and account['new_data_usage_upper_bytes']+R.ALL_PLANNED_RETAINED_BOUND <= R.DATA_CAP
        envelope = {'known':True,'upper_bytes':account['new_data_usage_upper_bytes']+R.ALL_PLANNED_RETAINED_BOUND,
                    'policy':'fresh census plus common full planned retained-output upper bound'}
    stage = L/'scratch/m2k1-publish'/('ms06-two-parts-'+str(time.time_ns()))
    attempts = 0
    for ca,it,prior in work_items(c):
        if attempts >= args.max_attempts or R._CANCEL[0] or time.monotonic()+2550 > deadline: return
        if (L/it['new_record']).exists():
            q = inspect(c,args.sha256,ca,it)
            if q['state'] in ('INVALID','SAT','HALT_UNKNOWN'): raise RuntimeError('persistent existing veto '+repr(q))
            continue
        if not TX.claim(it['claim'],args.sha256,it['id']): continue
        def build():
            verify(c)
            return COMMON.formula(c,ca,it['indices'])
        r = OWNER.execute(build,recipe(c,ca,it),args.sha256,c['source_sha256'],TX.item_paths(it,stage),deadline,envelope,'cadical',300,it['tier'],prior)
        if not r.get('pre_child_pin_sha256'):
            TX.release_unattempted(it['claim'],'two-parts admission refused before immutable pin/native'); return
        r.update(runner='run_m2_ms06_two_parts_v2.py',count_for_scientific_coverage=True,
                 list_sha256=ca['list']['sha256'],complete_denominator=ca['list']['n'],enumerator='extend_b.py')
        raw = (json.dumps(r,indent=1)+'\n').encode(); rh = hashlib.sha256(raw).hexdigest()
        COMMON.publish_json(L/it['commit'],{'schema':'PA19-K1-RECEIPT-v2','production_contract_sha256':args.sha256,
            'b_index':ca['b_index'],'indices':it['indices'],'tier':it['tier'],'record_sha256':rh,'pin_sha256':r['pre_child_pin_sha256']},stage)
        COMMON.publish_bytes(L/it['new_record'],raw,stage)
        attempts += 1
        print(json.dumps({'id':it['id'],'tier':it['tier'],'record':it['new_record'],'sha256':rh,'status':r['status'],'checked':r['checked']}),flush=True)
        if r['status'] in ('SAT','INVALID') or r.get('halt_production'): return


if __name__ == '__main__':
    main()
