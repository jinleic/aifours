#!/usr/bin/env python3
"""Creation-only PRE-EXEC for exactly ONE bounded M2H v6_4 split-path pilot: the frozen plan's four B100 intervals of
ms01_b00957 (contract positions 617, 4801, 5151, 5161). Binds the v6_4 review pack, contract, plan, supervisor v6, every
contract source, the pilot prelaunch/closeout checkers, receipts and the parent source-review authority given on the
command line; fixes the exact runner argv. Metadata only: no claim, pin, job, record or native work.
Usage: freeze_m2h_v6_4_pilot_preexec.py AUTHORITY_PATH AUTHORITY_SHA256 [AUTHORITY_PATH AUTHORITY_SHA256 ...]
"""
import hashlib
import json
import sys
import time
from pathlib import Path

L = Path(__file__).resolve().parents[1]
REVIEW = Path('/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review')
PY = '/Users/jinleic/.local/state/research-explorer/venv/bin/python'
CONTRACT = ('cycle2/m2h-a2-v6_4-contract-20261018T121918.json','41983dedd232232804b955df350de750c9e3feda7b45500293212932808edd5d')
PLAN = ('cycle2/m2h-v6_4-subset-plan-20261018T121940.json','73738d7689746908e7d8d08a0fe27ab9e272664916c0930e03fa09f0c14df6c2')
PACK = ('cycle2/m2h-v6_4-review-pack-20261018T124847.json','db01b47791e1512ee02c6d901da44e39ccd9817d68e6e68ee3e3804deb547e74')
SUP = ('src/supervise_pa19_v6.py','adc5cc0656b73670fa9003a609a90f271255822f24e194c31df7250efb18e075')
RECEIPTS = {'cycle2/m2h-v6_4-binding-census-20261018T124819.json':'192dec76a25e732f07878c66e9faf74a490fa07fd57655d14bc28c9e6e9a9e31',
            'cycle2/m2h-v6_4-controls-1792351189630705000/receipt.json':'3434f6d4dc197a9fd2e6f6895e93b4abea1cea96fdf898c70df514ba591783fb',
            'cycle2/supervise-v6-control-20261018T110305/receipt.json':'988237d438f11d799b07ab7ab4af2bc62dcf8e4d72efa688f9b7af461733c6da'}
TOOLS = ('src/m2h_gate_preview_v6_4.py','src/m2h_binding_census_v6_4.py','src/check_m2h_v6_4.py','src/freeze_m2h_v6_4_plan.py',
         'src/freeze_m2h_v6_4_review_pack.py','src/control_supervise_pa19_v6.py','src/m2h_v6_4_pilot_prelaunch.py',
         'src/m2h_v6_4_pilot_closeout.py','src/freeze_m2h_v6_4_pilot_preexec.py')
AMENDMENT = REVIEW/'parent-rule-amendment-long-job-stability-v1.md'
MONITOR = REVIEW/'disk-monitor-v1-20261018T0722-to-1810.jsonl'
LONG_JOB_RULE = {'min_free':13500000000,'window_seconds':300,'min_samples':25,'min_span_seconds':290,'max_age_seconds':30,
                 'drop_floor':300000000,'runway_divisor':12}
MONITORS = [{'pid':60597,'marker':'rss_watchdog4'},{'pid':60600,'marker':'checkpoint_clock'},{'pid':60602,'marker':'stop_k1_timer'}]
GROWTH = 4905886720  # GO condition: the gate-preview usage limit (DATA_CAP - whole-plan bound - other-writer margin) as projected growth
EXPECTED_WALL_SECONDS = 600  # expectation: v6_3 pilot 26-31 s per item; four intervals; worst case bounded by 4 x 2400 s supervisor walls


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    auth = sys.argv[1:]
    assert auth and len(auth) % 2 == 0, 'authority PATH SHA pairs required'
    authority = {auth[i]:auth[i+1] for i in range(0,len(auth),2)}
    for p,h in authority.items(): assert digest(p) == h, ('authority hash differs',p)
    host_iso = time.strftime('%Y-%m-%dT%H:%M:%S%z'); host_iso = host_iso[:-2]+':'+host_iso[-2:]
    for p,h in [CONTRACT,PLAN,PACK,SUP]+list(RECEIPTS.items()): assert digest(L/p) == h, p
    c = json.loads((L/CONTRACT[0]).read_bytes()); plan = json.loads((L/PLAN[0]).read_bytes())
    assert c['source_sha256'][SUP[0]] == SUP[1] and plan['contract_sha256'] == CONTRACT[1]
    items = [c['items'][s['contract_position']] for s in plan['items']]
    assert [x['id'] for x in items] == [s['id'] for s in plan['items']] and all(x['mode'] == 'partbatch' for x in items)
    bindings = {CONTRACT[0]:CONTRACT[1],PLAN[0]:PLAN[1],PACK[0]:PACK[1]}
    bindings.update(c['source_sha256']); bindings.update(RECEIPTS); bindings.update(authority)
    bindings.update({t:digest(L/t) for t in TOOLS}); bindings[str(AMENDMENT)] = digest(AMENDMENT)
    for ref in c['skeletons'].values(): bindings[ref['path']] = ref['sha256']
    for x in items:
        bindings[x['historical']['path']] = x['historical']['sha256']; bindings[x['list']['path']] = x['list']['sha256']
    argv = ['/usr/bin/env','-u','PYTHONOPTIMIZE','PYTHONDONTWRITEBYTECODE=1',PY,'-B',str(L/'src/run_m2h_v6_4.py'),str(L/CONTRACT[0]),CONTRACT[1],
            '--max-attempts',str(len(items)),'--plan',str(L/PLAN[0]),'--plan-sha256',PLAN[1]]
    assert not any(a.startswith('-O') for a in argv), 'assertions must stay enabled'
    pre = {'schema':'PA19-M2H-V6_4-PILOT-PRE-EXEC-v1','host_clock_iso':host_iso,
        'status':'FROZEN; launch only after an explicit parent GO bound to this file SHA-256; one pipeline, no retry, no relaunch',
        'authority':{p:h for p,h in authority.items()},
        'review_pack':{'path':PACK[0],'sha256':PACK[1]},
        'contract':{'path':CONTRACT[0],'sha256':CONTRACT[1],'items':len(c['items']),'source_sha256':c['source_sha256'],
                    'identical_to_contract':c['identical_to_contract']},
        'plan':{'path':PLAN[0],'sha256':PLAN[1]},
        'supervisor':{'path':SUP[0],'sha256':SUP[1]},
        'pilot':{'runner':'src/run_m2h_v6_4.py','max_attempts':len(items),'items':[x['id'] for x in items],
                 'item_bindings':[{'contract_position':s['contract_position'],'id':x['id'],'mode':x['mode'],'multiset':x['multiset'],'b_index':x['b_index'],
                                   'indices':x['indices'],'list':x['list'],'expected_cnf_sha256':x['expected_cnf_sha256'],'expected_cnf_bytes':x['expected_cnf_bytes'],
                                   'native_seconds':x['native_seconds'],'solver':x['solver'],'historical':x['historical'],'item_sha256':s['item_sha256']}
                                  for s,x in zip(plan['items'],items)],
                 'why_exact':'the runner validates the bound plan with plan_items and iterates ONLY its items; the prelaunch gate proves a fresh '
                             'v6_4 namespace; each item is claimed and attempted at most once; any stop path ends the pilot earlier',
                 'case':'ms01_b00957 (complete B100 partition n=310: 00000-00099, 00100-00199, 00200-00299, 00300-00309)'},
        'argv':argv,'cwd':str(L),'log':'cycle2/m2h-v6_4-pilot-run-<host stamp>.log (created with noclobber)',
        'policy_clocks':c['policy_clocks'],'min_launch_headroom_seconds':2850,
        'interpreter':{'assertions_enabled':True,'rule':'no -O flag in argv; PYTHONOPTIMIZE removed by env -u; prelaunch also checks its own flags'},
        'disk_gate':{'base_gate_bytes':12200000000,'projected_growth_bytes':GROWTH,
                     'note':'GO condition: projected growth = the gate-preview usage limit 4,905,886,720 B (no smaller projection claimed); the '
                            'in-flight floor 12e9 B and every per-phase gate remain enforced by the reviewed runtime'},
        'expected_wall_seconds':EXPECTED_WALL_SECONDS,
        'long_job_rule':{'amendment':{'path':str(AMENDMENT),'sha256':digest(AMENDMENT)},'monitor':str(MONITOR),'rule':LONG_JOB_RULE,
                         'gating':EXPECTED_WALL_SECONDS >= 3600,
                         'applied':'GO condition: the 300 s monitor rule gates only an expected wall time >= 60 min. Expected here: minutes (v6_3 '
                                   'pilot 26-31 s per item, four intervals); worst case bounded by the runner deadline and 4 x 2400 s supervisor '
                                   'walls. The rule is still evaluated and recorded at prelaunch as admission evidence.'},
        'lane_caps':{'busy_processes':4,'lane_rss_bytes':8*1024**3,'group_rss_bytes':c['resource_policy']['normal_group_rss_bytes'],
                     'tokens':'COUNT<=2 (cycle2/tokens/t0,t1); the runner holds at most one at a time','pipelines':1,
                     'singletons':['cycle2/m2h-v6_3-singleton.lock','cycle2/m2h-v6_4-singleton.lock']},
        'monitors':MONITORS,
        'steps':['1 fresh gate preview: src/m2h_gate_preview_v6_4.py CONTRACT SHA (metadata only), created after this PRE-EXEC and <= 600 s before launch',
                 '2 prelaunch: src/m2h_v6_4_pilot_prelaunch.py PRE_EXEC SHA GATE_PREVIEW must exit 0 (receipt written either way)',
                 '3 launch exactly argv once, in cwd, with a lane-local TMPDIR, stdout+stderr to the noclobber log; never retried or relaunched',
                 '4 after the runner exits: src/final_m2h_inventory_v6_4.py CONTRACT SHA --verify-formulas',
                 '5 src/m2h_v6_4_pilot_closeout.py PRE_EXEC SHA CHUNK_DIR RUN_LOG INVENTORY',
                 '6 report receipts and SHA-256s to the parent; README/checkpoint amendment'],
        'stop_rules':['any prelaunch failure: no launch; report','any runner stop path ends the pilot; no automatic retry; no relaunch without a new GO',
                      'parent stop request: SIGTERM only to this pilot runner process (no SIGKILL)','UNKNOWN is never UNSAT; persistent vetoes are never cleared',
                      'admission closes at the frozen 17:20 policy clock; native end 17:57 with 120 s cleanup'],
        'expected_outcomes':'each attempted interval ends QUALIFIED (measured UNSAT with checked DRAT, all five admissions, every binding incl. list '
                            'SHA, denominator and enumerator) or UNKNOWN/veto under the frozen semantics; the case counts as covered only if all '
                            'four intervals are QUALIFIED; every outcome is pilot evidence only',
        'scope':'split-path pilot evidence for one case; no PA19 or M2 completeness; no production expansion; M6/M9/E0 stay parked',
        'bindings':bindings}
    dest = L/'cycle2'/('m2h-v6_4-pilot-pre-exec-%s.json' % time.strftime('%Y%m%dT%H%M%S'))
    with dest.open('x') as f:
        json.dump(pre,f,indent=1); f.write('\n')
    print(dest,digest(dest),'items',pre['pilot']['items'],'bindings',len(bindings),flush=True)


if __name__ == '__main__':
    main()
