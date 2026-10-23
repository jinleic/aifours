#!/usr/bin/env python3
"""Freeze the HISTORICAL-M2 measured re-solve contract (M2H, A2 ms01..ms08) over UNCHANGED v6 transport.
Every item is bound to its immutable historical checked-UNSAT receipt (path+SHA) and that receipt's CNF SHA/bytes;
production regenerates with the ORIGINAL independent-B encoder and must reproduce the bound bytes before any pin.
Direct cases: one build_v2 item. Split cases: the exact B100 partition of the frozen list; every interval must have a
historical checked-UNSAT batch receipt, otherwise the case is excluded (reported, not silently covered).
Limits: original CaDiCaL -t (300/600) and drat-trim 1200 as supported by the reviewed worker; rev5/rev9 recorded
checker 1800 becomes 1200 (stricter: only more UNKNOWN). ms09 belongs to the M9 contract; E0 needs a reviewed
encode_q0b worker mode and is NOT in this contract. Historical receipts stay ORIGINAL-QUALIFIED only.
Metadata only (JSON reads + hashes); no regeneration, solver or checker here.
"""
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

import m2_ms09_contract_v6 as COMMON
import m2_supervised_runtime_v6 as R

L = COMMON.LANE
SCHEMA = 'PA19-M2H-A2-v6'
EXTRA_SOURCES = ('src/freeze_m2h_v6.py','src/run_m2h_v6.py','src/final_m2h_inventory_v6.py')


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def limit_of(record):
    m = re.search(r'-t (\d+) CNF',str(record.get('solver')))
    n = int(m.group(1)) if m else None
    assert n in (300,600), ('historical solver limit unsupported by reviewed worker',n)
    return n


def checked_unsat(r):
    return r.get('status') == 'UNSAT' and r.get('checked') is True and r.get('solver_rc') == 20


def main():
    items,excluded,skeletons = [],[],{}
    for mi in range(1,9):
        sk = 'cycle2/skel-b/skeletons-b-ms%02d.json' % mi
        skeletons[mi] = {'path':sk,'sha256':digest(L/sk)}
        D = json.loads((L/sk).read_bytes()); n_cases = len(D['skeletons'])
        for bi in range(n_cases):
            dp = L/'cycle2/m2skel_drat'/('ms%02d_b%05d.json' % (mi,bi))
            split = L/'cycle2/m2part_drat'/('ms%02d_b%05d' % (mi,bi))
            if dp.exists():
                r = json.loads(dp.read_bytes())
                if checked_unsat(r):
                    assert r.get('encoder') == 'encode_skel_b.build_v2' and r.get('multiset') == mi and r.get('b_index') == bi
                    items.append({'id':'ms%02d_b%05d' % (mi,bi),'multiset':mi,'b_index':bi,'mode':'direct','indices':None,
                        'historical':{'path':str(dp.relative_to(L)),'sha256':digest(dp),'revision':r.get('stream_check_revision'),
                            'recorded_service_seconds':(r.get('solve_seconds') or 0)+(r.get('check_seconds') or 0)},
                        'expected_cnf_sha256':r['cnf_sha256'],'expected_cnf_bytes':r['cnf_bytes'],'solver':'cadical','native_seconds':limit_of(r)})
                    continue
            if split.is_dir() and (split/'ext.json').exists():
                ed = json.loads((split/'ext.json').read_bytes()); n = ed['num_placements']
                assert n == len(ed['placements'])
                if n == 0:
                    excluded.append({'case':'ms%02d_b%05d' % (mi,bi),'reason':'empty list: needs separate parent structural check'}); continue
                parts,ok = [],True
                for lo in range(0,n,100):
                    hi = min(n,lo+100)-1
                    cands = sorted(split.glob('batch_%05d_%05d*.json' % (lo,hi)))
                    good = [p for p in cands if re.fullmatch(r'batch_%05d_%05d(_exact|_r3)?\.json' % (lo,hi),p.name) and checked_unsat(json.loads(p.read_bytes()))]
                    if not good: ok = False; break
                    p = good[0]; r = json.loads(p.read_bytes())
                    assert r.get('encoder') == 'encode_skel_b.build_partbatch'
                    parts.append({'id':'ms%02d_b%05d:%05d-%05d' % (mi,bi,lo,hi),'multiset':mi,'b_index':bi,'mode':'partbatch','indices':[lo,hi],
                        'list':{'path':str((split/'ext.json').relative_to(L)),'sha256':digest(split/'ext.json'),'n':n},
                        'historical':{'path':str(p.relative_to(L)),'sha256':digest(p),'revision':r.get('stream_check_revision'),
                            'recorded_service_seconds':(r.get('solve_seconds') or 0)+(r.get('check_seconds') or 0)},
                        'expected_cnf_sha256':r['cnf_sha256'],'expected_cnf_bytes':r['cnf_bytes'],'solver':'cadical','native_seconds':limit_of(r)})
                if ok: items.extend(parts)
                else: excluded.append({'case':'ms%02d_b%05d' % (mi,bi),'reason':'historical B100 partition incomplete (no checked-UNSAT receipt for every interval)'})
                continue
            excluded.append({'case':'ms%02d_b%05d' % (mi,bi),'reason':'no historical checked-UNSAT direct receipt or complete split'})
    items.sort(key=lambda x:(x['historical']['recorded_service_seconds'],x['multiset'],x['b_index'],x['indices'] or [-1]))
    sources = {rel:digest(L/rel) for rel in tuple(COMMON.SOURCE_FILES)+EXTRA_SOURCES}
    out = {'schema':SCHEMA,'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'source_sha256':sources,
        'skeletons':{str(k):v for k,v in skeletons.items()},'supervisor':{'path':str(R.SUP_PATH),'sha256':R.SUP_SHA},
        'binary_authority':{k:{'path':p,'sha256':digest(p)} for k,p in [('python',os.path.abspath(sys.executable)),
            ('solver','/opt/homebrew/bin/cadical'),('checker',str(L/'tools/drat-trim/drat-trim'))]},
        'resource_policy':COMMON.resource_policy(),'check_seconds':1200,'items':items,'order':[x['id'] for x in items],
        'cases_direct':sum(x['mode'] == 'direct' for x in items),'cases_split':len({(x['multiset'],x['b_index']) for x in items if x['mode'] == 'partbatch'}),
        'split_intervals':sum(x['mode'] == 'partbatch' for x in items),'excluded_cases':excluded,
        'recorded_old_transport_service_hours':sum(x['historical']['recorded_service_seconds'] for x in items)/3600,
        'scope':'A2 ms01..ms08 only; ms09 in M9 contract; E0 pending reviewed worker mode; historical receipts remain ORIGINAL-QUALIFIED',
        'automatic_retry_allowed':False,'deviation':'rev5/rev9 recorded checker 1800s run at reviewed 1200s (stricter)'}
    dest = L/'cycle2'/('m2h-a2-v6-contract-%s.json' % time.strftime('%Y%m%dT%H%M%S'))
    stage = L/'scratch/m2h-publish'/('contract-'+str(time.time_ns()))
    h = COMMON.publish_json(dest,out,stage)
    print(dest,h,'items',len(items),'direct',out['cases_direct'],'split_cases',out['cases_split'],'intervals',out['split_intervals'],
          'excluded',len(excluded),'old_service_h %.2f' % out['recorded_old_transport_service_hours'],flush=True)


if __name__ == '__main__':
    R.install_handlers()
    with R.Capacity(time.monotonic()+10800,metadata=True,wait_allowance=600):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+16*1024**2
        main()
