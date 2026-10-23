#!/usr/bin/env python3
"""Creation-only review pack for the parent Codex re-review of v6_2 (R/pa19-m2h-v6-2-codex-v1.note.md, HOLD): the exact
deltas v5->v6 (adapter), v6_2->v6_3 (transport, exact + rename-normalized) and M2H v6_2->v6_3, the new v6 adapter and
M2H v6_3 control receipts, the frozen v6_3 contract with its complete binding census and fresh gate preview, and a
finding -> fix map. Everything not listed is unchanged from the v6_2 pack, whose pins are re-verified. Metadata only.
Usage: freeze_m2h_v6_3_review_pack.py CONTRACT V6_CONTROL M2H_CONTROL CENSUS GATE_PREVIEW
"""
import argparse
import difflib
import hashlib
import json
import os
import re
import time
from pathlib import Path

import m2_ms09_contract_v6_3 as COMMON
import m2_supervised_runtime_v6_3 as R
import run_m2h_v6_3 as H

L = COMMON.LANE
V62_PACK = ('cycle2/m2h-v6_2-review-pack-20261018T104505.json','549062c06de10702fb82c1ae04b2d409059a3cc7239899a4850a1a4e7c8257e7')
ADAPTERS = {'v3':'79c463589c9c5d60fddff7c4397a4e90339bdb0f5a0b2542c865c02a387573b3','v5':'a7540cded7c485491d30e364afd09663b5d02b315232ec38d8f50f3d82a6bbf5',
            'v6':'adc5cc0656b73670fa9003a609a90f271255822f24e194c31df7250efb18e075'}
FAMILY = ['m2_supervised_runtime','m2_native_staged','m2_item_owner','m2_supervised_evidence','m2_ms09_evidence','m2_ms09_contract',
          'freeze_m2_ms09_k1','run_m2_ms09_k1','final_m2_ms09_inventory','check_m2_ms09_k1','run_m2_ms06_direct']
M2H = ['run_m2h','freeze_m2h','final_m2h_inventory','m2h_binding_census','m2h_gate_preview','check_m2h']
FINDINGS = [
 {'finding':'1 MAJOR late signal after the final check could persist/return completed_cleanly=True with observed_signal; owner composition and '
            'evidence reader accepted observed_signal/owner cancellation',
  'fix':'supervise_pa19_v6: the finalization window (final signal check, record build/write, handler restoration) runs with SIGTERM/SIGINT blocked; a '
        'signal in it reaches only the restored outer handler; written == returned record, no post-write mutation. Owner v6_3: observed_signal or owner '
        'cancellation at any point up to outcome composition -> UNKNOWN + owner_cancelled + persistent HALT. Evidence v6_3 proof_errors rejects '
        'observed_signal and owner_cancelled. Runner v6_3: signal-blocked publication window with a final cancellation check (-> UNKNOWN + HALT '
        'before publication); a signal inside the window is delivered after publication and stops the runner. The M2H reader rejects any UNSAT '
        'carrying a signal/cancellation. No PGID is signalled after reaping (unchanged v5 rule).',
  'evidence':'v6 adapter control P5 (v5 defect reproduced) and P6 (v6 consistent) plus all 13 v5 cases on v6; M2H controls O3/O4 (settlement window, '
             'real owner), T12 (publication window), T13 (cancellation before publication), R18'},
 {'finding':'2 MAJOR reader omitted native_result.worker_preconstruction_gate from the cutoff checks',
  'fix':'run_m2h_v6_3.admission_errors: ONE shared predicate over all five admissions (owner construct, owner worker spawn, worker construct, worker '
        'solver, worker checker): every present record carries its phase and the frozen cutoff, every admitted one is timestamped strictly before the '
        'cutoff, and a qualifying UNSAT requires all five admitted',
  'evidence':'M2H controls R15 (missing), R16 (wrong cutoff), R17 (post-cutoff), R19 (all five valid: predicate passes), R10 (owner gate after cutoff)'},
 {'finding':'3 MINOR exclusion census used cardinality only',
  'fix':'verify(): covered and excluded case names must be unique, disjoint, and their union must EQUAL the A2 ms01..ms08 skeleton universe',
  'evidence':'M2H controls V1 (out-of-domain name), V2 (duplicate), V3 (overlap); contract freeze verify'}]


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
    ap = argparse.ArgumentParser()
    for a in ('contract','v6_control','m2h_control','census','gate_preview'): ap.add_argument(a)
    args = ap.parse_args(); stamp = time.strftime('%Y%m%dT%H%M%S')
    assert digest(L/V62_PACK[0]) == V62_PACK[1]
    v62 = json.loads((L/V62_PACK[0]).read_bytes())
    for item in v62['transport_v6_2']['family']: assert digest(L/item['new']) == item['new_sha256'], ('v6_2 source changed',item['new'])
    for rel,item in v62['m2h_v6_2']['sources'].items(): assert digest(L/rel) == item['sha256'], ('M2H v6_2 source changed',rel)
    for k,h in ADAPTERS.items(): assert digest(L/('src/supervise_pa19_%s.py' % k)) == h
    assert R.SUP_SHA == ADAPTERS['v6'] and R.SUP_PATH == L/'src/supervise_pa19_v6.py'
    v5t,v6t,v3t = [(L/('src/supervise_pa19_%s.py' % k)).read_text() for k in ('v5','v6','v3')]
    ad56 = write_x(L/'cycle2'/('supervise-pa19-v5-to-v6-%s.diff' % stamp),udiff(v5t,v6t,'src/supervise_pa19_v5.py','src/supervise_pa19_v6.py'))
    ad36 = write_x(L/'cycle2'/('supervise-pa19-v3-to-v6-%s.diff' % stamp),udiff(v3t,v6t,'src/supervise_pa19_v3.py','src/supervise_pa19_v6.py'))
    v6r = json.loads(Path(args.v6_control).read_bytes())
    assert v6r['all_expected'] is True and v6r['pins']['v6']['sha256'] == ADAPTERS['v6'] and v6r['control_source_sha256'] == digest(L/'src/control_supervise_pa19_v6.py')
    exact,normal,family = [],[],[]
    for b in FAMILY:
        a,n = (L/('src/%s_v6_2.py' % b)).read_text(),(L/('src/%s_v6_3.py' % b)).read_text()
        exact.append(udiff(a,n,'src/%s_v6_2.py' % b,'src/%s_v6_3.py' % b))
        nd = udiff(a,re.sub(r'(?<![0-9A-Za-z])([vV])6_3(?![0-9])',lambda m: m.group(1)+'6_2',n),'src/%s_v6_2.py' % b,'src/%s_v6_3.py [v6_3->v6_2 normalized]' % b)
        normal.append(nd)
        family.append({'base':'src/%s_v6_2.py' % b,'base_sha256':digest(L/('src/%s_v6_2.py' % b)),'new':'src/%s_v6_3.py' % b,
                       'new_sha256':digest(L/('src/%s_v6_3.py' % b)),'normalized_changed_lines':changed(nd),'content':n})
    allowed = {'m2_supervised_runtime','m2_item_owner','m2_supervised_evidence','m2_ms09_contract','check_m2_ms09_k1'}
    assert all(f['normalized_changed_lines'] == 0 for f in family if Path(f['new']).stem[:-5] not in allowed), 'unexpected non-rename transport change'
    tx_exact = write_x(L/'cycle2'/('full-k1-v6_2-to-v6_3-exact-delta-%s.diff' % stamp),''.join(exact))
    tx_norm = write_x(L/'cycle2'/('full-k1-v6_2-to-v6_3-rename-normalized-delta-%s.diff' % stamp),''.join(normal))
    norm = lambda s: re.sub(r'(?<![0-9A-Za-z])([vV])6_3(?![0-9])',lambda m: m.group(1)+'6_2',s).replace('_h6_3','_h6_2').replace('m2h6_3','m2h6_2')
    m2h_exact,m2h_norm = [],[]
    for b in M2H:
        a,n = (L/('src/%s_v6_2.py' % b)).read_text(),(L/('src/%s_v6_3.py' % b)).read_text()
        m2h_exact.append(udiff(a,n,'src/%s_v6_2.py' % b,'src/%s_v6_3.py' % b))
        m2h_norm.append(udiff(a,norm(n),'src/%s_v6_2.py' % b,'src/%s_v6_3.py [normalized]' % b))
    m2h_d = write_x(L/'cycle2'/('m2h-v6_2-to-v6_3-exact-delta-%s.diff' % stamp),''.join(m2h_exact))
    m2h_n = write_x(L/'cycle2'/('m2h-v6_2-to-v6_3-rename-normalized-delta-%s.diff' % stamp),''.join(m2h_norm))
    c = json.loads(Path(args.contract).read_bytes()); csha = digest(args.contract); H.verify(c)
    c62 = json.loads((L/v62['m2h_v6_2']['contract']['path']).read_bytes())
    key = lambda x: (x['id'],x['expected_cnf_sha256'],x['expected_cnf_bytes'],x['historical']['path'],x['historical']['sha256'],x['native_seconds'])
    cen = json.loads(Path(args.census).read_bytes())
    assert cen['contract_sha256'] == csha and cen['status'] == 'COMPLETE' and cen['checked'] == len(c['items']) == cen['matches'] and not cen['mismatches']
    ctl = json.loads(Path(args.m2h_control).read_bytes())
    assert ctl['all_expected'] is True and ctl['contract_sha256'] == csha and ctl['control_source_sha256'] == digest(L/'src/check_m2h_v6_3.py') and ctl['sources'] == c['source_sha256']
    gp = json.loads(Path(args.gate_preview).read_bytes())
    assert gp['contract_sha256'] == csha and gp['usage_within_reservation'] and gp['budget_2400_fits'] and all(g['admitted'] for g in gp['gates'].values())
    rel = lambda p: str(Path(p).resolve().relative_to(L))
    pack = {'schema':'PA19-M2H-V6_3-REVIEW-PACK-v1','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'status':'FROZEN FOR PARENT RE-REVIEW; native production HOLD until GO','responds_to':'review/pa19-m2h-v6-2-codex-v1.note.md',
        'previous_pack':{'path':V62_PACK[0],'sha256':V62_PACK[1],'unchanged_pins_reverified':True},'finding_fix_map':FINDINGS,
        'adapter_v6':{'path':'src/supervise_pa19_v6.py','sha256':ADAPTERS['v6'],'content':v6t,'diff_v5_to_v6':ad56,'diff_v3_to_v6':ad36,
            'control':{'source':{'path':'src/control_supervise_pa19_v6.py','sha256':digest(L/'src/control_supervise_pa19_v6.py'),'content':(L/'src/control_supervise_pa19_v6.py').read_text()},
                       'receipt':{'path':rel(args.v6_control),'sha256':digest(args.v6_control),
                                  'cases':[{k:r.get(k) for k in ('case','module','completed_cleanly','trip_reason','observed_signal','written_equals_returned','outer_handler_calls','expected_ok')} for r in v6r['cases']]}}},
        'transport_v6_3':{'family':family,'exact_diff_vs_v6_2':tx_exact,'rename_normalized_diff_vs_v6_2':tx_norm,
                          'normalized_changed_lines':{Path(f['new']).stem:f['normalized_changed_lines'] for f in family}},
        'm2h_v6_3':{'sources':{'src/%s_v6_3.py' % b:{'sha256':digest(L/('src/%s_v6_3.py' % b)),'content':(L/('src/%s_v6_3.py' % b)).read_text()} for b in M2H},
            'exact_delta_vs_v6_2':m2h_d,'rename_normalized_delta_vs_v6_2':m2h_n,
            'contract':{'path':rel(args.contract),'sha256':csha,'items':len(c['items']),'cases_direct':c['cases_direct'],'cases_split':c['cases_split'],
                        'split_intervals':c['split_intervals'],'excluded_cases':len(c['excluded_cases']),'policy_clocks':c['policy_clocks'],
                        'whole_plan_remaining_bound_bytes':c['resource_policy']['whole_plan_remaining_bound_bytes'],
                        'items_identical_to_v6_2_contract':[key(x) for x in c['items']] == [key(x) for x in c62['items']]},
            'binding_census':{'path':rel(args.census),'sha256':digest(args.census),'checked':cen['checked'],'matches':cen['matches'],'mismatches':len(cen['mismatches'])},
            'control_receipt':{'path':rel(args.m2h_control),'sha256':digest(args.m2h_control),
                               'cases':{fam:[{'name':r['name'],'ok':r['ok']} for r in rows] for fam,rows in ctl['families'].items()},
                               'native_children_started':ctl['native_children_started']},
            'gate_preview':{'path':rel(args.gate_preview),'sha256':digest(args.gate_preview),'census_bytes':gp['census']['current_data_upper_bytes'],
                            'usage_limit_bytes':gp['usage_limit_bytes'],'gates':{k:(g['admitted'],g['errors']) for k,g in gp['gates'].items()}}},
        'unchanged':['M6/M9 PARKED (version-independent attempt map required)','E0 outside M2H','one pipeline, singleton lock, frozen 17:20/17:57 clocks',
                     'no PA19 or M2 completeness theorem follows from controls'],
        'generator_sha256':digest(__file__)}
    dest = L/'cycle2'/('m2h-v6_3-review-pack-%s.json' % stamp)
    with dest.open('x') as f: json.dump(pack,f,indent=1); f.write('\n')
    print(dest,digest(dest),flush=True)
    print(json.dumps({'adapter':{'v5_to_v6':ad56,'v3_to_v6':ad36},'transport':{'exact':tx_exact,'normalized':tx_norm,
                      'normalized_changed_lines':pack['transport_v6_3']['normalized_changed_lines']},'m2h':{'exact':m2h_d,'normalized':m2h_n},
                      'contract':pack['m2h_v6_3']['contract'],'census':pack['m2h_v6_3']['binding_census'],'gate_preview':pack['m2h_v6_3']['gate_preview']},indent=1),flush=True)


if __name__ == '__main__':
    R.install_handlers()
    with R.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+16*1024**2
        main()
