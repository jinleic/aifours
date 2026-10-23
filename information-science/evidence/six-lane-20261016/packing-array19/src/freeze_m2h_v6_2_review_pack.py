#!/usr/bin/env python3
"""Creation-only review pack for the parent Codex v2 HOLD (R/pa19-m2h-v6-1-supervisor-codex-v2.note.md):
adapter v5 (diffs vs v3 and v4) + its control receipts, transport v6_1 -> v6_2 (exact and rename-normalized diffs),
the M2H v6_2 sources, frozen contract, complete binding census and private control-suite receipt, and an explicit
finding -> fix map. Metadata only: no solver, checker, helper or native child. Earlier packs/sources are re-verified.
Usage: freeze_m2h_v6_2_review_pack.py CONTRACT V5_CONTROL_RECEIPT M2H_CONTROL_RECEIPT CENSUS_RECEIPT
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

import m2_ms09_contract_v6_2 as COMMON
import m2_supervised_runtime_v6_2 as R
import run_m2h_v6_2 as H

L = COMMON.LANE
V6_PACK = ('cycle2/full-k1-v6-sourcepack-20261018T075617.json','cb9d45ab26a7b39ee960d70f4b28ffe4483d6add3bb6900d6fcc27cdc6a74bc3')
V61_PACK = ('cycle2/m2h-v6_1-review-pack-20261018T092125.json','0f854e75757c8e3a7c9a96efd4a59e856ada16d458f9d070a170ec72349cf713')
ADAPTERS = {'v3':'79c463589c9c5d60fddff7c4397a4e90339bdb0f5a0b2542c865c02a387573b3','v4':'3b5c1808813a1f0627a4ebb721f197294659ddd66fcc7ecc09213b972c4b9f17',
            'v5':'a7540cded7c485491d30e364afd09663b5d02b315232ec38d8f50f3d82a6bbf5'}
FIRST_V5_CONTROL = ('cycle2/supervise-v5-control-20261018T095449/receipt.json','4db47e0235f1591eefba2256920d5d8bf3c5aa48d7c8dd816d5814108a8737e1')
V61_CENSUS = ('cycle2/m2h-v6_1-binding-census-20261018T095744.json','49ac1cd9ea481c455dfe7d43100f26fb5d35f6d9bc62091b561d13e102e049ee')
V61_CONTRACT = ('cycle2/m2h-a2-v6_1-contract-20261018T092051.json','e2dae6f102f1f5a045a6c13ef5ee0adb7fb2ea751cbb8f29a67324ffd4e7bd4e')
FAMILY = ['m2_supervised_runtime','m2_native_staged','m2_item_owner','m2_supervised_evidence','m2_ms09_evidence','m2_ms09_contract',
          'freeze_m2_ms09_k1','run_m2_ms09_k1','final_m2_ms09_inventory','check_m2_ms09_k1','run_m2_ms06_direct']
M2H = ['run_m2h','freeze_m2h','final_m2h_inventory','m2h_binding_census']
FINDINGS = [
 {'finding':'1 MAJOR re-poll window could swallow a stop; final sample predates the window; poll after 5 s',
  'fix':'supervise_pa19_v5.delayed_reap: strict sample + floor + wall + signal checks BEFORE every poll, no poll after the 5 s bound, sleep bounded by '
        'the remaining time; a trip is nonclean and the stop runs only while the leader is unreaped; a flagged signal before the record is nonclean; '
        'observed_signal returned and the v6_2 runtime sets the owner cancel flag',
  'evidence':'v5 control cases A-N (13/13), M2H controls C2'},
 {'finding':'2 BLOCKER historical fallback could qualify unmeasured receipts',
  'fix':'run_m2h_v6_2.inspect accepts ONLY pipeline_schema PA19-SUPERVISED-DRAT-v6_2 and binds contract SHA, pre-child pin SHA+path, runner, coverage '
        'flag, historical reference, interval, list SHA and denominator (direct: no list fields), pin supervisor SHA (v5), group supervisor SHA, and '
        'every admitted gate before the frozen cutoff; then the measured evidence reader',
  'evidence':'M2H controls R0-R14'},
 {'finding':'3 BLOCKER 17:20 admission / 17:57 native end not enforced; fixed 2400 s wall',
  'fix':'contract policy_clocks (17:20 cutoff, 17:57 native end, 120 s cleanup) verified against the runner constants; runner refuses at/after the '
        'cutoff and uses deadline = native end - cleanup; v6_2 full_gate refuses every phase at/after the lease cutoff (missing cutoff refuses) and '
        'records at_epoch; Capacity.supervise refuses a group whose 2400 s budget does not fit before the deadline; STOP-K1 still refuses',
  'evidence':'M2H controls G1-G3, C1, T8, T10'},
 {'finding':'4 MAJOR historical split identity insufficiently checked',
  'fix':'explicit per-revision layouts (5, 9, 12, 14, 15; direct/partbatch) for solver string+limit, checker verdict, replay, multiset, B index, exact '
        'integer interval, encoder, CNF SHA/positive bytes; list source realpath/index/positive denominator; ID/case uniqueness, direct/split '
        'disjointness, declared counts and included+excluded = all A2 ms01..ms08 cases, all in verify() and the freeze',
  'evidence':'contract freeze + verify (5,580 items), binding census'},
 {'finding':'5 MAJOR pre-pin binding mismatch persisted an INTEGRITY veto',
  'fix':'owner v6_2 BindingRefusal: unattempted before pin, no pin/job/group, chunk ends, no veto; any other constructor failure stays a persistent '
        'INTEGRITY veto; the runner records a binding-refusal receipt and releases only its claim',
  'evidence':'M2H controls O1, O2, T3 (real owner)'},
 {'finding':'6 MAJOR M6/M9 namespace is not continuity',
  'fix':'unchanged: M6/M9 stay PARKED; no v6_1/v6_2 M6/M9 contract exists; a version-independent attempt map is required before any resumption',
  'evidence':'none needed (no change)'}]


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def udiff(a,b,fa,fb):
    return ''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile=fa,tofile=fb))


def changed(d):
    return sum(1 for line in d.splitlines() if line[:1] in '+-' and not line.startswith(('+++','---')))


def write_x(path,text):
    with path.open('x') as f: f.write(text)
    return {'path':str(path.relative_to(L)),'sha256':digest(path),'bytes':path.stat().st_size}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('contract'); ap.add_argument('v5_control'); ap.add_argument('m2h_control'); ap.add_argument('census')
    args = ap.parse_args(); stamp = time.strftime('%Y%m%dT%H%M%S')
    for rel,h in (V6_PACK,V61_PACK,FIRST_V5_CONTROL,V61_CENSUS,V61_CONTRACT): assert digest(L/rel) == h, rel
    v6 = json.loads((L/V6_PACK[0]).read_bytes())
    for rel,item in v6['source_files'].items(): assert digest(L/rel) == item['sha256'], ('production v6 source changed',rel)
    v61 = json.loads((L/V61_PACK[0]).read_bytes())
    for item in v61['transport_v6_1']['family']: assert digest(L/item['new']) == item['new_sha256'], ('v6_1 source changed',item['new'])
    for k,h in ADAPTERS.items(): assert digest(L/('src/supervise_pa19_%s.py' % k)) == h
    assert R.SUP_SHA == ADAPTERS['v5'] and R.SUP_PATH == L/'src/supervise_pa19_v5.py'
    txt = {k:(L/('src/supervise_pa19_%s.py' % k)).read_text() for k in ADAPTERS}
    ad35 = write_x(L/'cycle2'/('supervise-pa19-v3-to-v5-%s.diff' % stamp),udiff(txt['v3'],txt['v5'],'src/supervise_pa19_v3.py','src/supervise_pa19_v5.py'))
    ad45 = write_x(L/'cycle2'/('supervise-pa19-v4-to-v5-%s.diff' % stamp),udiff(txt['v4'],txt['v5'],'src/supervise_pa19_v4.py','src/supervise_pa19_v5.py'))
    v5r = json.loads(Path(args.v5_control).read_bytes())
    assert v5r['all_expected'] is True and v5r['pins']['v5']['sha256'] == ADAPTERS['v5'] and v5r['control_source_sha256'] == digest(L/'src/control_supervise_pa19_v5.py')
    exact,normal,family = [],[],[]
    for b in FAMILY:
        a,n = (L/('src/%s_v6_1.py' % b)).read_text(),(L/('src/%s_v6_2.py' % b)).read_text()
        exact.append(udiff(a,n,'src/%s_v6_1.py' % b,'src/%s_v6_2.py' % b))
        nd = udiff(a,re.sub(r'(?<![0-9A-Za-z])([vV])6_2(?![0-9])',lambda m: m.group(1)+'6_1',n),'src/%s_v6_1.py' % b,'src/%s_v6_2.py [v6_2->v6_1 normalized]' % b)
        normal.append(nd)
        family.append({'base':'src/%s_v6_1.py' % b,'base_sha256':digest(L/('src/%s_v6_1.py' % b)),'new':'src/%s_v6_2.py' % b,
                       'new_sha256':digest(L/('src/%s_v6_2.py' % b)),'normalized_changed_lines':changed(nd),'content':n})
    allowed = {'m2_supervised_runtime','m2_item_owner','m2_ms09_contract','check_m2_ms09_k1'}
    assert all(f['normalized_changed_lines'] == 0 for f in family if Path(f['new']).stem[:-5] not in allowed), 'unexpected non-rename transport change'
    tx_exact = write_x(L/'cycle2'/('full-k1-v6_1-to-v6_2-exact-delta-%s.diff' % stamp),''.join(exact))
    tx_norm = write_x(L/'cycle2'/('full-k1-v6_1-to-v6_2-rename-normalized-delta-%s.diff' % stamp),''.join(normal))
    m2h_new,m2h_vs = [],[]
    for b in M2H:
        new = L/('src/%s_v6_2.py' % b); old = L/('src/%s_v6_1.py' % b)
        m2h_new.append(udiff('',new.read_text(),'/dev/null','src/%s_v6_2.py' % b))
        m2h_vs.append(udiff(old.read_text(),new.read_text(),'src/%s_v6_1.py' % b,'src/%s_v6_2.py' % b))
    m2h_full = write_x(L/'cycle2'/('m2h-v6_2-new-files-%s.diff' % stamp),''.join(m2h_new))
    m2h_delta = write_x(L/'cycle2'/('m2h-v6_1-to-v6_2-delta-%s.diff' % stamp),''.join(m2h_vs))
    c = json.loads(Path(args.contract).read_bytes()); csha = digest(args.contract); H.verify(c)
    c1 = json.loads((L/V61_CONTRACT[0]).read_bytes())
    key = lambda x: (x['id'],x['expected_cnf_sha256'],x['expected_cnf_bytes'],x['historical']['path'],x['historical']['sha256'],x['native_seconds'])
    same_items = [key(x) for x in c['items']] == [key(x) for x in c1['items']]
    cen = json.loads(Path(args.census).read_bytes())
    assert cen['contract_sha256'] == csha and cen['status'] == 'COMPLETE' and cen['checked'] == len(c['items']) == cen['matches'] and not cen['mismatches']
    ctl = json.loads(Path(args.m2h_control).read_bytes())
    assert ctl['all_expected'] is True and ctl['contract_sha256'] == csha and ctl['control_source_sha256'] == digest(L/'src/check_m2h_v6_2.py')
    assert ctl['sources'] == c['source_sha256']
    first_split = next(i for i,x in enumerate(c['items']) if x['mode'] == 'partbatch')
    pack = {'schema':'PA19-M2H-V6_2-REVIEW-PACK-v1','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'status':'FROZEN FOR PARENT RE-REVIEW; native production HOLD until GO; parent M1 retries have priority',
        'responds_to':'review/pa19-m2h-v6-1-supervisor-codex-v2.note.md (HOLD)','finding_fix_map':FINDINGS,
        'adapter_v5':{'path':'src/supervise_pa19_v5.py','sha256':ADAPTERS['v5'],'content':txt['v5'],'diff_v3_to_v5':ad35,'diff_v4_to_v5':ad45,
            'control':{'source':{'path':'src/control_supervise_pa19_v5.py','sha256':digest(L/'src/control_supervise_pa19_v5.py'),
                                 'content':(L/'src/control_supervise_pa19_v5.py').read_text()},
                       'receipt':{'path':str(Path(args.v5_control).resolve().relative_to(L)),'sha256':digest(args.v5_control),
                                  'cases':[{k:r.get(k) for k in ('case','module','completed_cleanly','leader_returncode','trip_reason','stop_ran','observed_signal','poll_calls','poll_span_s','expected_ok')} for r in v5r['cases']]},
                       'earlier_run':{'path':FIRST_V5_CONTROL[0],'sha256':FIRST_V5_CONTROL[1],'all_expected':False,
                                      'why':'my case-B expectation copied the v4 sleep-then-poll timing (real poll >= 10 ms later); v5 checks then polls '
                                            'immediately, so the real poll came 0.3 ms later; behaviour correct, expectation corrected, all 13 cases re-run'}}},
        'transport_v6_2':{'family':family,'exact_diff_vs_v6_1':tx_exact,'rename_normalized_diff_vs_v6_1':tx_norm,
            'normalized_changed_lines':{Path(f['new']).stem:f['normalized_changed_lines'] for f in family},
            'harness_note':'check_m2_ms09_k1_v6_2 is the v6_1 harness renamed; its gates would now refuse without a policy cutoff; it is NOT run and not used by M2H'},
        'm2h_v6_2':{'sources':{'src/%s_v6_2.py' % b:{'sha256':digest(L/('src/%s_v6_2.py' % b)),'content':(L/('src/%s_v6_2.py' % b)).read_text()} for b in M2H},
            'control_source':{'path':'src/check_m2h_v6_2.py','sha256':digest(L/'src/check_m2h_v6_2.py'),'content':(L/'src/check_m2h_v6_2.py').read_text()},
            'new_files_diff':m2h_full,'delta_vs_v6_1':m2h_delta,
            'contract':{'path':str(Path(args.contract).resolve().relative_to(L)),'sha256':csha,'items':len(c['items']),'cases_direct':c['cases_direct'],
                        'cases_split':c['cases_split'],'split_intervals':c['split_intervals'],'excluded_cases':len(c['excluded_cases']),
                        'excluded_by_reason':dict(collections.Counter(x['reason'] for x in c['excluded_cases'])),'policy_clocks':c['policy_clocks'],
                        'whole_plan_remaining_bound_bytes':c['resource_policy']['whole_plan_remaining_bound_bytes'],
                        'items_identical_to_v6_1_census_contract':same_items,'first_split_position':first_split},
            'binding_census':{'path':str(Path(args.census).resolve().relative_to(L)),'sha256':digest(args.census),'checked':cen['checked'],
                              'matches':cen['matches'],'mismatches':len(cen['mismatches']),'seconds':cen['seconds']},
            'earlier_complete_census_same_items':{'path':V61_CENSUS[0],'sha256':V61_CENSUS[1],'contract':V61_CONTRACT[0]},
            'control_receipt':{'path':str(Path(args.m2h_control).resolve().relative_to(L)),'sha256':digest(args.m2h_control),
                               'cases':{fam:[{'name':r['name'],'ok':r['ok']} for r in rows] for fam,rows in ctl['families'].items()},
                               'native_children_started':ctl['native_children_started']}},
        'production_plan_after_GO':['ONE M2H pipeline (singleton lock); the second token stays reserved for the parent M1 re-attempts; no native work while a parent retry is alive',
                                    'first tranche bounded (--max-attempts) to show a direct item through publisher -> exact reader -> inventory; the first split '
                                    'interval is at frozen position %d and will be reported the same way' % first_split,
                                    'admission closes 17:20 by the frozen clock (and STOP-K1 at 17:20); owned groups quiescent by 17:57'],
        'open_items':['M6/M9 PARKED pending a version-independent attempt map','E0 (486) needs a reviewed encode_q0b worker mode; ms09 stays in the parked M9 contract',
                      'no PA19 or M2 completeness theorem follows from these controls'],
        'generator_sha256':digest(__file__)}
    dest = L/'cycle2'/('m2h-v6_2-review-pack-%s.json' % stamp)
    with dest.open('x') as f: json.dump(pack,f,indent=1); f.write('\n')
    print(dest,digest(dest),flush=True)
    print(json.dumps({'adapter':{'v3_to_v5':ad35,'v4_to_v5':ad45},'transport':{'exact':tx_exact,'normalized':tx_norm,
                      'normalized_changed_lines':pack['transport_v6_2']['normalized_changed_lines']},
                      'm2h':{'new_files':m2h_full,'delta':m2h_delta},'contract':pack['m2h_v6_2']['contract'],'census':pack['m2h_v6_2']['binding_census']},indent=1),flush=True)


if __name__ == '__main__':
    R.install_handlers()
    with R.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+16*1024**2
        main()
