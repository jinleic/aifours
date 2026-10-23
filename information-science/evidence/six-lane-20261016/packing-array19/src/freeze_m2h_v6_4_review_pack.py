#!/usr/bin/env python3
"""Creation-only source-review pack for the M2H v6_4 explicit-subset selector (parent instruction after the v6_3 pilot):
exact and rename-normalized deltas v6_3 -> v6_4 for every M2H file, the new plan freezer, the frozen v6_4 contract with
its identical-items proof against the v6_3 contract, the complete binding census, the control receipt, a fresh gate
preview, the frozen four-interval plan and a requirement -> implementation map. Transport v6_3 and supervisor v6 are
unchanged (pins re-verified). Metadata only.
Usage: freeze_m2h_v6_4_review_pack.py CONTRACT PLAN CONTROLS CENSUS GATE_PREVIEW
"""
import argparse
import difflib
import hashlib
import json
import os
import time
from pathlib import Path

import m2_ms09_contract_v6_3 as COMMON
import m2_supervised_runtime_v6_3 as R
import run_m2h_v6_4 as H

L = COMMON.LANE
V63_CONTRACT = ('cycle2/m2h-a2-v6_3-contract-20261018T110631.json','835ca4b2a9e11313b1663c5c14bba7e1e9c325b06a866abc09838cac6c5a1930')
V63_PACK = ('cycle2/m2h-v6_3-review-pack-20261018T113603.json','07214aa1b0fed523221c3f559717982bc28d30a0b95c0e98e73530c84449c115')
FILES = ['run_m2h','freeze_m2h','final_m2h_inventory','m2h_binding_census','m2h_gate_preview','check_m2h']
PAIRS = [('run_m2h_v6_3','run_m2h_v6_4'),('freeze_m2h_v6_3','freeze_m2h_v6_4'),('final_m2h_inventory_v6_3','final_m2h_inventory_v6_4'),
         ('m2h_binding_census_v6_3','m2h_binding_census_v6_4'),('m2h_gate_preview_v6_3','m2h_gate_preview_v6_4'),('check_m2h_v6_3','check_m2h_v6_4'),
         ('m2h-a2-v6_3-contract','m2h-a2-v6_4-contract'),('m2h-v6_3-','m2h-v6_4-'),('PA19-M2H-A2-v6_3','PA19-M2H-A2-v6_4'),
         ('PA19-M2H-INVENTORY-v6_3','PA19-M2H-INVENTORY-v6_4'),('PA19-M2H-V6_3-','PA19-M2H-V6_4-'),('M2H v6_3','M2H v6_4'),
         ('measured-v6_3','measured-v6_4'),('_h6_3','_h6_4'),('m2h6_3','m2h6_4')]
REQUIREMENTS = [
 ('keep the full 5,580-item contract identities and denominators; no item mutation or renumbering',
  'freeze_m2h_v6_4 derives items exactly as v6_3 and asserts items, order, exclusions, skeletons, binaries, clocks, resource policy, '
  'case/interval counts, retry and single-pipeline flags EQUAL the frozen v6_3 contract; the contract records identical_to_contract; '
  'plans reference items by id + position + canonical item SHA-256 and never copy them'),
 ('exact unique IDs, membership checked',
  'run_m2h_v6_4.plan_items: schema, contract SHA, non-empty, exact entry fields, well-formed ids, unique ids, not an excluded case, '
  'member at the stated position, identical canonical item, contract order, complete split cases (controls S0-S14, S19)'),
 ('existing v6_3 attempts remain distinct',
  'v6_4 uses its own namespace (_h6_4 records/pins/commits, m2h6_4_ claims, m2h6_4-chunks); plan_items refuses any selected item with a '
  'v6_3 record, pin, commit or claim (control S15 on the live pilot record ms01_b00045); v6_3 records are read by the v6_3 reader only'),
 ('no bypass of admission/pins/leases/stop/reader',
  'only the loop iterable changes (for x in selected); owner execute, gates, pins, claims, capacity leases, stop/cancel/HALT checks, '
  'publication window, exact reader and inventory are the v6_3 code unchanged (rename-normalized delta); all v6_3 control families re-run'),
 ('deterministic controls: unknown/duplicate/out-of-contract IDs rejected; only selected items attempted',
  'S1-S15 unit rejections, S16 runner claims/attempts exactly the four selected intervals in contract order, S17-S19 no plan / wrong '
  'plan hash / invalid plan refuse before any claim, S20 a held v6_3 singleton refuses v6_4, I2 inventory counts one complete case of 5,424'),
 ('one pipeline', 'v6_4 holds BOTH the v6_3 and the v6_4 singleton locks'),
 ('17:20 admission / 17:57 end unchanged', 'POLICY_CLOCKS unchanged and bound in the identical contract fields')]


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def udiff(a,b,fa,fb):
    return ''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile=fa,tofile=fb))


def normalize(t):
    for a,b in PAIRS: t = t.replace(b,a)
    return t


def write_x(path,text):
    with path.open('x') as f: f.write(text)
    return {'path':str(path.relative_to(L)),'sha256':digest(path),'bytes':path.stat().st_size}


def main():
    ap = argparse.ArgumentParser()
    for a in ('contract','plan','controls','census','gate_preview'): ap.add_argument(a)
    args = ap.parse_args(); stamp = time.strftime('%Y%m%dT%H%M%S')
    assert digest(L/V63_PACK[0]) == V63_PACK[1] and digest(L/V63_CONTRACT[0]) == V63_CONTRACT[1]
    c = json.loads(Path(args.contract).read_bytes()); csha = digest(args.contract); H.verify(c)
    c63 = json.loads((L/V63_CONTRACT[0]).read_bytes())
    same = c['identical_to_contract']['fields']
    assert c['identical_to_contract']['sha256'] == V63_CONTRACT[1] and all(c[k] == c63[k] for k in same)
    transport = {p:h for p,h in c['source_sha256'].items() if p not in H.EXTRA_SOURCES}
    assert transport == {p:h for p,h in c63['source_sha256'].items() if p not in ('src/freeze_m2h_v6_3.py','src/run_m2h_v6_3.py','src/final_m2h_inventory_v6_3.py')}, \
        'transport/supervisor sources differ from the v6_3 contract'
    exact,normal,files = [],[],{}
    for b in FILES:
        a,n = (L/('src/%s_v6_3.py' % b)).read_text(),(L/('src/%s_v6_4.py' % b)).read_text()
        exact.append(udiff(a,n,'src/%s_v6_3.py' % b,'src/%s_v6_4.py' % b))
        nd = udiff(a,normalize(n),'src/%s_v6_3.py' % b,'src/%s_v6_4.py [M2H renames normalized]' % b)
        normal.append(nd)
        files['src/%s_v6_4.py' % b] = {'sha256':digest(L/('src/%s_v6_4.py' % b)),'base':'src/%s_v6_3.py' % b,'base_sha256':digest(L/('src/%s_v6_3.py' % b)),
            'normalized_changed_lines':sum(1 for s in nd.splitlines() if s[:1] in '+-' and not s.startswith(('+++','---'))),'content':n}
    for extra in ('src/freeze_m2h_v6_4_plan.py','src/freeze_m2h_v6_4_review_pack.py'):
        files[extra] = {'sha256':digest(L/extra),'base':None,'content':(L/extra).read_text()}
    d_exact = write_x(L/'cycle2'/('m2h-v6_3-to-v6_4-exact-delta-%s.diff' % stamp),''.join(exact))
    d_norm = write_x(L/'cycle2'/('m2h-v6_3-to-v6_4-rename-normalized-delta-%s.diff' % stamp),''.join(normal))
    plan = json.loads(Path(args.plan).read_bytes()); psha = digest(args.plan)
    chosen = [x['id'] for x in H.plan_items(c,csha,plan)]
    ctl = json.loads(Path(args.controls).read_bytes())
    assert ctl['all_expected'] is True and ctl['contract_sha256'] == csha and ctl['control_source_sha256'] == digest(L/'src/check_m2h_v6_4.py') and ctl['sources'] == c['source_sha256']
    cen = json.loads(Path(args.census).read_bytes())
    assert cen['contract_sha256'] == csha and cen['status'] == 'COMPLETE' and cen['checked'] == len(c['items']) == cen['matches'] and not cen['mismatches']
    gp = json.loads(Path(args.gate_preview).read_bytes())
    assert gp['contract_sha256'] == csha and gp['usage_within_reservation'] and gp['budget_2400_fits'] and all(g['admitted'] for g in gp['gates'].values())
    rel = lambda p: str(Path(p).resolve().relative_to(L))
    pack = {'schema':'PA19-M2H-V6_4-SELECTOR-REVIEW-PACK-v1','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'status':'FROZEN FOR PARENT SOURCE REVIEW; no native launch until a separate parent GO',
        'requirements_map':[{'requirement':a,'implementation':b} for a,b in REQUIREMENTS],
        'unchanged':{'transport_and_supervisor_sources':transport,'previous_pack':{'path':V63_PACK[0],'sha256':V63_PACK[1]},
                     'v6_3_contract':{'path':V63_CONTRACT[0],'sha256':V63_CONTRACT[1]}},
        'm2h_v6_4':{'files':files,'exact_delta_vs_v6_3':d_exact,'rename_normalized_delta_vs_v6_3':d_norm,
            'normalized_changed_lines':{k:v.get('normalized_changed_lines') for k,v in files.items()}},
        'contract':{'path':rel(args.contract),'sha256':csha,'items':len(c['items']),'identical_to_contract':c['identical_to_contract'],
                    'cases_direct':c['cases_direct'],'cases_split':c['cases_split'],'split_intervals':c['split_intervals'],
                    'excluded_cases':len(c['excluded_cases']),'policy_clocks':c['policy_clocks']},
        'plan':{'path':rel(args.plan),'sha256':psha,'items':plan['items'],'validated_selection':chosen},
        'binding_census':{'path':rel(args.census),'sha256':digest(args.census),'checked':cen['checked'],'matches':cen['matches'],'mismatches':len(cen['mismatches'])},
        'controls':{'path':rel(args.controls),'sha256':digest(args.controls),'native_children_started':ctl['native_children_started'],
                    'cases':{fam:[{'name':r['name'],'ok':r['ok']} for r in rows] for fam,rows in ctl['families'].items()}},
        'gate_preview':{'path':rel(args.gate_preview),'sha256':digest(args.gate_preview),'census_bytes':gp['census']['current_data_upper_bytes'],
                        'usage_limit_bytes':gp['usage_limit_bytes'],'gates':{k:(g['admitted'],g['errors']) for k,g in gp['gates'].items()}},
        'scope':'source review only; a split-path run would be pilot evidence for one case (4 intervals); no PA19 or M2 completeness; '
                'v6_3 pilot records remain v6_3-only; M6/M9/E0 parked',
        'generator_sha256':digest(__file__)}
    dest = L/'cycle2'/('m2h-v6_4-review-pack-%s.json' % stamp)
    with dest.open('x') as f: json.dump(pack,f,indent=1); f.write('\n')
    print(dest,digest(dest),flush=True)
    print(json.dumps({'exact':d_exact,'normalized':d_norm,'normalized_changed_lines':pack['m2h_v6_4']['normalized_changed_lines'],
                      'contract':{k:pack['contract'][k] for k in ('path','sha256','items')},'plan':{k:pack['plan'][k] for k in ('path','sha256','validated_selection')},
                      'census':pack['binding_census'],'gate_preview':{k:pack['gate_preview'][k] for k in ('path','sha256','census_bytes','gates')}},indent=1),flush=True)


if __name__ == '__main__':
    R.install_handlers()
    with R.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+16*1024**2
        main()
