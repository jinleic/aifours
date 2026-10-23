#!/usr/bin/env python3
"""Freeze the HISTORICAL-M2 measured re-solve contract (M2H, A2 ms01..ms08) over the v6_2 transport.
Every item is bound to its immutable historical checked-UNSAT receipt (path+SHA) whose identity is validated with
the EXPLICIT per-revision layout of run_m2h_v6_2.historical_errors (revisions 5, 9, 12, 14, 15; multiset, B index,
exact integer interval, encoder, CNF SHA/positive bytes, native limit, checker verdict). Production regenerates
with the ORIGINAL independent-B encoder and must reproduce the bound bytes before any pin.
Direct cases: one build_v2 item. Split cases: the exact B100 partition of the frozen list whose source/index/
denominator are validated; every interval must have a validated historical checked-UNSAT batch receipt, otherwise
the whole case is excluded (reported, never silently covered). Frozen policy clocks and the whole-plan bound are
taken from run_m2h_v6_2. ms09 belongs to the M9 contract; E0 needs a reviewed encode_q0b worker mode.
Metadata only (JSON reads + hashes); no regeneration, solver or checker here.
"""
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

import m2_ms09_contract_v6_2 as COMMON
import m2_supervised_runtime_v6_2 as R
import run_m2h_v6_2 as H

L = COMMON.LANE


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def limit_of(record):
    m = re.search(r'-t (\d+) CNF',str(record.get('solver')))
    return int(m.group(1)) if m else None


def checked_unsat(r):
    return r.get('status') == 'UNSAT' and r.get('checked') is True and r.get('solver_rc') == 20


def historical(p,r):
    return {'path':str(p.relative_to(L)),'sha256':digest(p),'revision':r.get('stream_check_revision'),
            'recorded_service_seconds':(r.get('solve_seconds') or 0)+(r.get('check_seconds') or 0)}


def main():
    items,excluded,skeletons = [],[],{}
    for mi in range(1,9):
        sk = 'cycle2/skel-b/skeletons-b-ms%02d.json' % mi
        skeletons[mi] = {'path':sk,'sha256':digest(L/sk)}
        n_cases = len(json.loads((L/sk).read_bytes())['skeletons'])
        for bi in range(n_cases):
            case = 'ms%02d_b%05d' % (mi,bi)
            dp = L/'cycle2/m2skel_drat'/(case+'.json')
            split = L/'cycle2/m2part_drat'/case
            if dp.exists():
                r = json.loads(dp.read_bytes())
                if checked_unsat(r):
                    x = {'id':case,'multiset':mi,'b_index':bi,'mode':'direct','indices':None,'historical':historical(dp,r),
                         'expected_cnf_sha256':r.get('cnf_sha256'),'expected_cnf_bytes':r.get('cnf_bytes'),'solver':'cadical','native_seconds':limit_of(r)}
                    errs = H.historical_errors(x,r)
                    if errs: excluded.append({'case':case,'reason':'historical direct receipt identity/layout check failed: '+'; '.join(errs)})
                    else: items.append(x)
                    continue
            if split.is_dir() and (split/'ext.json').exists():
                ed = json.loads((split/'ext.json').read_bytes()); n = ed.get('num_placements')
                lst = {'path':str((split/'ext.json').relative_to(L)),'sha256':digest(split/'ext.json'),'n':n}
                if not (type(n) is int and n > 0):
                    excluded.append({'case':case,'reason':'empty or invalid list: needs separate parent structural check'}); continue
                probe = {'multiset':mi,'b_index':bi,'list':lst}
                lerr = H.list_errors(probe,ed)
                if lerr:
                    excluded.append({'case':case,'reason':'list source/index/denominator check failed: '+'; '.join(lerr)}); continue
                parts,why = [],None
                for lo in range(0,n,100):
                    hi = min(n,lo+100)-1
                    cands = sorted(p for p in split.glob('batch_%05d_%05d*.json' % (lo,hi)) if re.fullmatch(r'batch_%05d_%05d(_exact|_r3)?\.json' % (lo,hi),p.name))
                    good = [(p,json.loads(p.read_bytes())) for p in cands]
                    good = [(p,r) for p,r in good if checked_unsat(r)]
                    if not good: why = 'historical B100 partition incomplete (no checked-UNSAT receipt for every interval)'; break
                    p,r = good[0]
                    x = {'id':'%s:%05d-%05d' % (case,lo,hi),'multiset':mi,'b_index':bi,'mode':'partbatch','indices':[lo,hi],'list':lst,
                         'historical':historical(p,r),'expected_cnf_sha256':r.get('cnf_sha256'),'expected_cnf_bytes':r.get('cnf_bytes'),
                         'solver':'cadical','native_seconds':limit_of(r)}
                    errs = H.historical_errors(x,r)
                    if errs: why = 'historical batch receipt identity/layout check failed at %d-%d: %s' % (lo,hi,'; '.join(errs)); break
                    parts.append(x)
                if why is None: items.extend(parts)
                else: excluded.append({'case':case,'reason':why})
                continue
            excluded.append({'case':case,'reason':'no historical checked-UNSAT direct receipt or complete split'})
    items.sort(key=lambda x:(x['historical']['recorded_service_seconds'],x['multiset'],x['b_index'],x['indices'] or [-1]))
    sources = {rel:digest(L/rel) for rel in tuple(COMMON.SOURCE_FILES)+H.EXTRA_SOURCES}
    out = {'schema':H.SCHEMA,'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'source_sha256':sources,
        'skeletons':{str(k):v for k,v in skeletons.items()},'supervisor':{'path':str(R.SUP_PATH),'sha256':R.SUP_SHA},
        'binary_authority':{k:{'path':p,'sha256':digest(p)} for k,p in [('python',os.path.abspath(sys.executable)),
            ('solver','/opt/homebrew/bin/cadical'),('checker',str(L/'tools/drat-trim/drat-trim'))]},
        'policy_clocks':H.POLICY_CLOCKS,'resource_policy':H.resource_policy(len(items)),'check_seconds':1200,'items':items,
        'order':[x['id'] for x in items],'cases_direct':sum(x['mode'] == 'direct' for x in items),
        'cases_split':len({(x['multiset'],x['b_index']) for x in items if x['mode'] == 'partbatch'}),
        'split_intervals':sum(x['mode'] == 'partbatch' for x in items),'excluded_cases':excluded,
        'recorded_old_transport_service_hours':sum(x['historical']['recorded_service_seconds'] for x in items)/3600,
        'scope':'A2 ms01..ms08 only; ms09 in M9 contract; E0 pending reviewed worker mode; historical receipts remain ORIGINAL-QUALIFIED',
        'automatic_retry_allowed':False,'single_pipeline':True,'deviation':'rev5/rev9 recorded checker 1800s run at reviewed 1200s (stricter)'}
    H.verify(out)
    dest = L/'cycle2'/('m2h-a2-v6_2-contract-%s.json' % time.strftime('%Y%m%dT%H%M%S'))
    stage = L/'scratch/m2h-publish'/('contract-'+str(time.time_ns()))
    h = COMMON.publish_json(dest,out,stage)
    print(dest,h,'items',len(items),'direct',out['cases_direct'],'split_cases',out['cases_split'],'intervals',out['split_intervals'],
          'excluded',len(excluded),'old_service_h %.2f' % out['recorded_old_transport_service_hours'],
          'whole_plan_bound',out['resource_policy']['whole_plan_remaining_bound_bytes'],flush=True)


if __name__ == '__main__':
    R.install_handlers()
    with R.Capacity(time.monotonic()+10800,metadata=True,wait_allowance=600):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+16*1024**2
        main()
