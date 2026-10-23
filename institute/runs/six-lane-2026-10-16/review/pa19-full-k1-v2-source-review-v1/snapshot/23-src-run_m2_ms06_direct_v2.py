#!/usr/bin/env python3
"""Finish ONLY the frozen106-item ms06 initial direct queue through the common measured-v2 transport.
Original recorded300s outcomes (including UNKNOWN68/73/162/77) are immutable and NEVER directly retried here.
Unattempted items keep CaDiCaL300/check1200, exact original build_v2 bytes and proof caps. Sole-RSS tier1 gets
exactly one7GiB exclusive tier2 after this one-input case's tier1 drains; every other UNKNOWN remains open.
--freeze creates the exact queue/source/old-record inventory before a later parent-reviewed run. After initial pass,
--freeze-misses pins the accumulated UNKNOWN set ONCE (no helper or split execution from this adapter).
"""
import argparse
import datetime
import hashlib
import json
import os
import time
from pathlib import Path

import encode_skel_b as ENC
import lane_new_data_accounting as ACCOUNT
import m2_item_owner_v2 as OWNER
import m2_ms09_contract as COMMON
import m2_ms09_evidence as E
import m2_supervised_runtime_v2 as R
import run_m2_ms09_k1 as TX

L = COMMON.LANE
QUEUE = 'cycle2/m2-jobs-hard-direct.txt'
SK = 'cycle2/skel-b/skeletons-b-ms06.json'
SCHEMA = 'PA19-MS06-INITIAL-DIRECT-v2'


def task(bi,tier=1):
    tail = '_v2' if tier == 1 else '_v2_t2'
    base = 'cycle2/m2skel_drat/ms06_b%05d' % bi
    return {'id':'ms06_b%05d' % bi,'indices':None,'tier':tier,'new_record':base+tail+'.json','pin':base+tail+'.cnf-pin.json',
            'commit':base+tail+'.receipt.json','claim':'cycle2/claims/ms06_direct_v2_t%d_b%05d.claim' % (tier,bi)}


def freeze():
    raw = (L/QUEUE).read_bytes()
    ids = []
    for line in raw.decode().splitlines():
        mi,interval = line.split(':'); lo,hi = map(int,interval.split('-'))
        assert mi == '6' and lo == hi and lo not in ids
        ids.append(lo)
    assert len(ids) == 106
    rows = []
    for bi in ids:
        old = L/'cycle2'/'m2skel_drat'/('ms06_b%05d.json' % bi)
        r = COMMON.read(old) if old.exists() else None
        if r is not None:
            assert r['multiset'] == 6 and r['b_index'] == bi and r['status'] != 'SAT'
        assert not (L/task(bi)['new_record']).exists(), 'new initial-pass namespace already used'
        rows.append({'b_index':bi,'original_record':str(old.relative_to(L)) if r is not None else None,
                     'original_sha256':E.digest(old) if r is not None else None,'original_status':r.get('status') if r is not None else None})
    out = {'schema':SCHEMA,'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'queue':QUEUE,'queue_sha256':hashlib.sha256(raw).hexdigest(),
           'source_sha256':{rel:E.digest(L/rel) for rel in COMMON.SOURCE_FILES},'skeleton_path':SK,'skeleton_sha256':E.digest(L/SK),
           'supervisor_path':str(R.SUP_PATH),'supervisor_sha256':R.SUP_SHA,'solver_sha256':E.digest('/opt/homebrew/bin/cadical'),
           'checker_sha256':E.digest(L/'tools/drat-trim/drat-trim'),'rows':rows,'pending_order':[x['b_index'] for x in rows if x['original_record'] is None],
           'native_seconds':300,'check_seconds':1200,'tier1_rss_bytes':R.GROUP_CAPS[1],'tier2_rss_bytes':R.GROUP_CAPS[2],
           'count_ceiling':2,'no_direct_retry_except_sole_RSS_tier2':True,'no_helper_from_this_adapter':True,
           'original_outcomes_are_not_backfilled_or_final_qualified':True}
    dest = L/'cycle2'/('m2-ms06-initial-v2-contract-'+time.strftime('%Y%m%dT%H%M%S')+'.json')
    h = COMMON.publish_json(dest,out,L/'scratch'/'m2k1-publish'/('ms06-freeze-'+str(time.time_ns())))
    print(dest,h,'pending',len(out['pending_order']),flush=True)


def verify(c):
    assert c['schema'] == SCHEMA and c['queue'] == QUEUE and E.digest(L/QUEUE) == c['queue_sha256']
    assert c['skeleton_path'] == SK and E.digest(L/SK) == c['skeleton_sha256']
    assert set(c['source_sha256']) == set(COMMON.SOURCE_FILES)
    for p,h in c['source_sha256'].items(): assert E.digest(L/p) == h
    assert c['supervisor_sha256'] == R.SUP_SHA and E.digest(R.SUP_PATH) == R.SUP_SHA
    assert c['native_seconds'] == 300 and c['check_seconds'] == 1200 and c['count_ceiling'] == 2
    assert c['pending_order'] == [x['b_index'] for x in c['rows'] if x['original_record'] is None]
    expected_ids = []
    for line in (L/QUEUE).read_text().splitlines():
        mi,interval = line.split(':'); lo,hi = map(int,interval.split('-'))
        assert mi == '6' and lo == hi
        expected_ids.append(lo)
    assert len(expected_ids) == len(set(expected_ids)) == 106 and [x['b_index'] for x in c['rows']] == expected_ids
    for x in c['rows']:
        if x['original_record']: assert E.digest(L/x['original_record']) == x['original_sha256']


def inspect(c,h,bi,tier=1):
    it = task(bi,tier)
    if not (L/it['new_record']).exists(): return {'state':'MISSING','record':None,'errors':[]}
    try:
        p,k = COMMON.read(L/it['pin']),COMMON.read(L/it['commit'])
        assert p['schema'] == 'PA19-K1-CNF-PIN-v2' and k['schema'] == 'PA19-K1-RECEIPT-v2'
        assert p['source_sha256'] == c['source_sha256'] and p['supervisor_sha256'] == R.SUP_SHA
        assert p['recipe']['skeleton_path'] == SK and p['recipe']['skeleton_sha256'] == c['skeleton_sha256']
        assert p['recipe']['encoder_sha256'] == c['source_sha256']['src/encode_skel_b.py'] and p['recipe']['indices'] is None
        if tier == 2:
            assert p['tier1_prior'] == {'path':task(bi)['new_record'],'sha256':E.digest(L/task(bi)['new_record'])}
        assert p['tier'] == k['tier'] == tier and p['production_contract_sha256'] == k['production_contract_sha256'] == h
        assert p['recipe']['multiset'] == 6 and p['recipe']['b_index'] == bi and p['recipe']['mode'] == 'direct'
        assert k['record_sha256'] == E.digest(L/it['new_record']) and k['pin_sha256'] == E.digest(L/it['pin'])
        ex = E.expected(6,bi,None,p['cnf_sha256'],p['cnf_bytes'],'encode_skel_b.build_v2',300,False)
        ex.update(tier=tier,tier1_prior=p.get('tier1_prior'),lane_root=str(L),source_sha256=c['source_sha256'],recipe=p['recipe'],
                  solver_binary_sha256=c['solver_sha256'],checker_binary_sha256=c['checker_sha256'])
        return E.inspect(L/it['new_record'],ex,k['record_sha256'])
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as exc:
        return {'state':'INVALID','errors':[repr(exc)]}


def freeze_misses(c,h):
    dest = L/'cycle2'/'ms06-initial-v2-UNKNOWN-misses-ONCE.json'
    assert not dest.exists(), 'miss-set freeze is once, never overwritten'
    rows = []
    for x in c['rows']:
        bi = x['b_index']
        if x['original_record']:
            r,rel = COMMON.read(L/x['original_record']),x['original_record']
        else:
            q = inspect(c,h,bi)
            assert q['state'] not in ('MISSING','INVALID','SAT','HALT_UNKNOWN'), ('initial pass incomplete/veto',bi,q)
            r,rel = q['record'],task(bi)['new_record']
            if r.get('rss_retry_eligible'):
                q2 = inspect(c,h,bi,2)
                assert q2['state'] not in ('MISSING','INVALID','SAT','HALT_UNKNOWN'), ('tier2 incomplete/veto',bi,q2)
                r,rel = q2['record'],task(bi,2)['new_record']
        if r.get('status') != 'UNSAT' or r.get('checked') is not True:
            rows.append({'job':'6:%d' % bi,'b_index':bi,'record':rel,'record_sha256':E.digest(L/rel),
                         'cnf_sha256':r['cnf_sha256'],'cnf_bytes':r['cnf_bytes'],'status':'UNKNOWN',
                         'already_enumerated':bi in (68,73)})
    out = {'schema':'PA19-MS06-UNKNOWN-SET-v1','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'initial_contract_sha256':h,
           'source_sha256':c['source_sha256'],'skeleton_sha256':c['skeleton_sha256'],'jobs':rows,
           'scope':'exact accumulated initial-pass UNKNOWN set; NO helper admission/denominator supplied here',
           'requires_new_source_denominator_growth_review_before_any_helper':True}
    rh = COMMON.publish_json(dest,out,L/'scratch'/'m2k1-publish'/('ms06-misses-'+str(time.time_ns())))
    print(dest,rh,'UNKNOWN',len(rows),flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('contract',nargs='?'); ap.add_argument('sha256',nargs='?')
    ap.add_argument('--freeze',action='store_true'); ap.add_argument('--freeze-misses',action='store_true')
    ap.add_argument('--max-attempts',type=int,default=8)
    args = ap.parse_args()
    R.install_handlers()
    cutoff = datetime.datetime.fromisoformat('2026-10-18T18:31:43-07:00').timestamp()
    deadline = min(time.monotonic()+10800,time.monotonic()+max(0,cutoff-time.time()))
    with R.Capacity(deadline,metadata=True,wait_allowance=60):
        st = os.statvfs(L); assert st.f_bavail*st.f_frsize >= R.BASE_GATE+1024**2
        if args.freeze: freeze(); return
        assert args.contract and args.sha256 and E.digest(args.contract) == args.sha256
        c = COMMON.read(args.contract); verify(c)
        if args.freeze_misses: freeze_misses(c,args.sha256); return
        assert args.max_attempts > 0
        accounting = ACCOUNT.account(L)
        reserve = R.ALL_PLANNED_RETAINED_BOUND
        assert accounting['known'] and accounting['new_data_usage_upper_bytes']+reserve <= R.DATA_CAP
        envelope = {'known':True,'upper_bytes':accounting['new_data_usage_upper_bytes']+reserve,
                    'policy':'fresh census plus common worst-case reservation for M9/M6/LEGACY5 and two halting diagnostics'}
        D = COMMON.read(L/SK); special = [p for p in D['profiles'] if list(p) != COMMON.P0]
    stage = L/'scratch'/'m2k1-publish'/('ms06-'+str(time.time_ns()))
    attempts = 0
    for bi in c['pending_order']:
        for tier in (1,2):
            if attempts >= args.max_attempts or R._CANCEL[0] or time.monotonic()+2550 > deadline: return
            it = task(bi,tier)
            prior = None
            if tier == 2:
                q = inspect(c,args.sha256,bi)
                r = q.get('record') or {}
                if not (r.get('status') == 'UNKNOWN' and r.get('rss_retry_eligible') is True and R.rss_only_retry(r.get('supervisor'),1,r.get('native_result'))): continue
                prior = {'path':task(bi)['new_record'],'sha256':E.digest(L/task(bi)['new_record'])}
            if (L/it['new_record']).exists():
                q = inspect(c,args.sha256,bi,tier)
                if q['state'] in ('INVALID','SAT','HALT_UNKNOWN'): raise RuntimeError('persistent existing direct veto '+repr(q))
                continue
            if not TX.claim(it['claim'],args.sha256,it['id']): continue
            recipe = {'mode':'direct','multiset':6,'b_index':bi,'indices':None,'skeleton_path':SK,
                      'skeleton_sha256':c['skeleton_sha256'],'encoder_sha256':c['source_sha256']['src/encode_skel_b.py']}
            def build():
                verify(c)
                sk = D['skeletons'][bi]
                nv,cl = ENC.build_v2(D['c0'],[tuple(t) for t in sk['types']],sk['empty'],special)
                return ENC.cnf_bytes(nv,cl)
            paths = TX.item_paths(it,stage)
            r = OWNER.execute(build,recipe,args.sha256,c['source_sha256'],paths,deadline,envelope,'cadical',300,tier,prior)
            if not r.get('pre_child_pin_sha256'):
                TX.release_unattempted(it['claim'],'new direct refused before immutable pin/native'); return
            r.update(runner='run_m2_ms06_direct_v2.py',count_for_scientific_coverage=True)
            raw = (json.dumps(r,indent=1)+'\n').encode(); rh = hashlib.sha256(raw).hexdigest()
            COMMON.publish_json(L/it['commit'],{'schema':'PA19-K1-RECEIPT-v2','tier':tier,'production_contract_sha256':args.sha256,
                'b_index':bi,'record_sha256':rh,'pin_sha256':r['pre_child_pin_sha256']},stage)
            COMMON.publish_bytes(L/it['new_record'],raw,stage)
            attempts += 1
            print(json.dumps({'job':'6:%d' % bi,'tier':tier,'record':it['new_record'],'sha256':rh,'status':r['status'],'checked':r['checked']}),flush=True)
            if r['status'] in ('SAT','INVALID') or r.get('halt_production'): return


if __name__ == '__main__':
    main()
