#!/usr/bin/env python3
"""Creation-only ONE review pack (parent decision after the 08:45 HALT): (1) supervisor adapter v3->v4 exact diff plus
the deterministic control receipt; (2) transport v6->v6_1 exact and rename-normalized diffs (normalized: only the
supervisor pin; the harness is the reviewed v8 harness renamed); (3) the M2H v6_1 sources and frozen contract.
Metadata only: no solver, checker, helper or native child. Production v6 sources are re-verified unchanged.
Usage: freeze_m2h_v6_1_review_pack.py M2H_CONTRACT CONTROL_RECEIPT
"""
import argparse
import collections
import difflib
import hashlib
import json
import os
import re
import time
from pathlib import Path

import m2_ms09_contract_v6_1 as COMMON
import m2_supervised_runtime_v6_1 as R
import run_m2h_v6_1 as H

L = COMMON.LANE
V6_PACK = ('cycle2/full-k1-v6-sourcepack-20261018T075617.json','cb9d45ab26a7b39ee960d70f4b28ffe4483d6add3bb6900d6fcc27cdc6a74bc3')
ADAPTER = {'v3':('src/supervise_pa19_v3.py','79c463589c9c5d60fddff7c4397a4e90339bdb0f5a0b2542c865c02a387573b3'),
           'v4':('src/supervise_pa19_v4.py','3b5c1808813a1f0627a4ebb721f197294659ddd66fcc7ecc09213b972c4b9f17')}
FAMILY = ['m2_supervised_runtime','m2_native_staged','m2_item_owner','m2_supervised_evidence','m2_ms09_evidence','m2_ms09_contract',
          'freeze_m2_ms09_k1','run_m2_ms09_k1','final_m2_ms09_inventory','check_m2_ms09_k1','run_m2_ms06_direct']
NORMALIZED_CHANGES_ALLOWED = {'m2_supervised_runtime':4,'m2_ms09_contract':1,'check_m2_ms09_k1':4}
RETIRED = 'archive/superseded-m2h-v6-drafts-20261018'


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def normalize(t):
    return re.sub(r'(?<![0-9A-Za-z])([vV])6_1(?![0-9])',lambda m: m.group(1)+'6',t)


def udiff(a,b,fa,fb):
    return ''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile=fa,tofile=fb))


def changed_lines(d):
    return sum(1 for line in d.splitlines() if line[:1] in '+-' and not line.startswith(('+++','---')))


def write_x(path,text):
    with path.open('x') as f: f.write(text)
    return {'path':str(path.relative_to(L)),'sha256':digest(path),'bytes':path.stat().st_size}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('contract'); ap.add_argument('control_receipt'); args = ap.parse_args()
    stamp = time.strftime('%Y%m%dT%H%M%S')
    assert digest(L/V6_PACK[0]) == V6_PACK[1]
    v6pack = json.loads((L/V6_PACK[0]).read_bytes())
    for rel,item in v6pack['source_files'].items(): assert digest(L/rel) == item['sha256'], ('production v6 source changed',rel)
    for rel,h in ADAPTER.values(): assert digest(L/rel) == h
    assert R.SUP_PATH == L/ADAPTER['v4'][0] and R.SUP_SHA == ADAPTER['v4'][1]
    v3t,v4t = (L/ADAPTER['v3'][0]).read_text(),(L/ADAPTER['v4'][0]).read_text()
    adapter_diff = write_x(L/'cycle2'/('supervise-pa19-v3-to-v4-%s.diff' % stamp),udiff(v3t,v4t,ADAPTER['v3'][0],ADAPTER['v4'][0]))
    receipt_path = Path(args.control_receipt).resolve(); receipt = json.loads(receipt_path.read_bytes())
    assert receipt['all_expected'] is True and receipt['pins']['v4']['sha256'] == ADAPTER['v4'][1] and receipt['pins']['v3']['sha256'] == ADAPTER['v3'][1]
    control_src = L/'src/control_supervise_pa19_v4.py'; assert receipt['control_source_sha256'] == digest(control_src)
    exact,normal,family,norm_counts = [],[],[],{}
    for b in FAMILY:
        base = 'src/check_m2_ms09_k1_v8.py' if b == 'check_m2_ms09_k1' else 'src/%s_v6.py' % b
        new = 'src/%s_v6_1.py' % b
        bt,nt = (L/base).read_text(),(L/new).read_text()
        exact.append(udiff(bt,nt,base,new))
        nd = udiff(bt,normalize(nt),base,new+' [v6_1->v6 normalized]'); normal.append(nd)
        norm_counts[b] = changed_lines(nd)
        assert norm_counts[b] <= 2*NORMALIZED_CHANGES_ALLOWED.get(b,0), ('unexpected non-rename change',b,norm_counts[b])
        family.append({'base':base,'base_sha256':digest(L/base),'new':new,'new_sha256':digest(L/new),'normalized_changed_lines':norm_counts[b],
                       'content':nt})
    exact_diff = write_x(L/'cycle2'/('full-k1-v6-to-v6_1-exact-delta-%s.diff' % stamp),''.join(exact))
    normal_diff = write_x(L/'cycle2'/('full-k1-v6-to-v6_1-rename-normalized-delta-%s.diff' % stamp),''.join(normal))
    c = json.loads(Path(args.contract).read_bytes()); csha = digest(args.contract); H.verify(c)
    new_m2h = list(H.EXTRA_SOURCES)
    m2h_diff = write_x(L/'cycle2'/('m2h-v6_1-new-files-%s.diff' % stamp),''.join(udiff('',(L/rel).read_text(),'/dev/null',rel) for rel in new_m2h))
    info = write_x(L/'cycle2'/('m2h-v6_1-runner-vs-m6-adapter-%s.diff' % stamp),
                   udiff((L/'src/run_m2_ms06_direct_v6_1.py').read_text(),(L/'src/run_m2h_v6_1.py').read_text(),'src/run_m2_ms06_direct_v6_1.py','src/run_m2h_v6_1.py'))
    fam_files = {'src/%s_v6_1.py' % b for b in FAMILY} | {ADAPTER['v4'][0]}
    unchanged = {rel:h for rel,h in c['source_sha256'].items() if rel not in fam_files and rel not in new_m2h}
    v6_hashes = {rel:item['sha256'] for rel,item in v6pack['source_files'].items()}
    assert all(v6_hashes.get(rel) == h for rel,h in unchanged.items()), 'a shared dependency differs from the v6 pack'
    retired = sorted(str(p.relative_to(L)) for p in (L/RETIRED).rglob('*') if p.is_file())
    pack = {'schema':'PA19-M2H-V6_1-REVIEW-PACK-v1','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'status':'FROZEN FOR ONE PARENT REVIEW; native production HOLD until GO',
        'adapter':{'v3':{'path':ADAPTER['v3'][0],'sha256':ADAPTER['v3'][1]},'v4':{'path':ADAPTER['v4'][0],'sha256':ADAPTER['v4'][1],'content':v4t},
                   'exact_diff':adapter_diff,
                   'control':{'source':{'path':str(control_src.relative_to(L)),'sha256':digest(control_src),'content':control_src.read_text()},
                              'receipt':{'path':str(receipt_path.relative_to(L)),'sha256':digest(receipt_path),'all_expected':receipt['all_expected'],
                                         'cases':[{k:r[k] for k in ('case','module','inject','completed_cleanly','leader_returncode','trip_reason',
                                                  'poll_calls','poll_span_s','expected_ok')} for r in receipt['cases']]}}},
        'transport_v6_1':{'family':family,'exact_diff':exact_diff,'rename_normalized_diff':normal_diff,'normalized_changed_lines':norm_counts,
                          'non_rename_changes':['m2_supervised_runtime: SUP_PATH/SUP_SHA pin supervise_pa19_v4.py; docstring names v4 and states the one change',
                                                'm2_ms09_contract: SOURCE_FILES lists src/supervise_pa19_v4.py instead of v3',
                                                'check_m2_ms09_k1_v6_1 = reviewed v8 harness (not the v6 harness), rename only plus its two receipt labels; not used by M2H'],
                          'shared_dependencies_unchanged_vs_v6_pack':unchanged},
        'm2h':{'sources':{rel:{'sha256':digest(L/rel),'content':(L/rel).read_text()} for rel in new_m2h},'new_files_diff':m2h_diff,
               'runner_vs_reviewed_m6_adapter_informative_diff':info,
               'contract':{'path':str(Path(args.contract).resolve().relative_to(L)),'sha256':csha,'items':len(c['items']),'cases_direct':c['cases_direct'],
                           'cases_split':c['cases_split'],'split_intervals':c['split_intervals'],'excluded_cases':len(c['excluded_cases']),
                           'excluded_by_reason':dict(collections.Counter(x['reason'] for x in c['excluded_cases'])),
                           'native_limits':dict(collections.Counter(x['native_seconds'] for x in c['items'])),
                           'historical_revisions':dict(collections.Counter(str(x['historical']['revision']) for x in c['items'])),
                           'recorded_old_transport_service_hours':c['recorded_old_transport_service_hours'],
                           'whole_plan_remaining_bound_bytes':c['resource_policy']['whole_plan_remaining_bound_bytes']},
               'semantic_points':['identity binding: regenerated ORIGINAL encode_skel_b CNF must equal the historical receipt CNF SHA/bytes before pin',
                                  'per-item constructor re-verifies contract SHA, all source SHAs, supervisor pin, skeleton and historical receipt',
                                  'one attempt per item; claims shared by both pipelines; existing records are never retried',
                                  'whole-plan retained bound = runtime plan bound + every M2H item at the ordinary per-item bound',
                                  'acceptance: only measured-v6_1 QUALIFIED records count; historical receipts stay ORIGINAL-QUALIFIED']},
        'superseded_unreviewed_drafts':{'archive_dir':RETIRED,'files':retired},
        'halt_retirement_receipt':'cycle2/m2k3-halt-retirement-receipt-20261018T085458.json',
        'open_items':['no v6_1 M6/M9 contract exists, so those runners cannot start; before any M6/M9 resumption under v6_1 the continuity with '
                      'existing v6 records (ms06 b74/b151/b182/b201/b295, ms09 b5 0-299) must be reviewed so nothing is retried',
                      'E0 (486) still needs a reviewed encode_q0b worker mode; ms09 stays in the parked M9 contract'],
        'generator_sha256':digest(__file__)}
    dest = L/'cycle2'/('m2h-v6_1-review-pack-%s.json' % stamp)
    with dest.open('x') as f: json.dump(pack,f,indent=1); f.write('\n')
    print(dest,digest(dest),flush=True)
    print(json.dumps({'adapter_diff':adapter_diff,'exact_diff':exact_diff,'normalized_diff':normal_diff,'normalized_changed_lines':norm_counts,
                      'm2h_diff':m2h_diff,'informative':info,'contract':pack['m2h']['contract']},indent=1),flush=True)


if __name__ == '__main__':
    R.install_handlers()
    with R.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+16*1024**2
        main()
