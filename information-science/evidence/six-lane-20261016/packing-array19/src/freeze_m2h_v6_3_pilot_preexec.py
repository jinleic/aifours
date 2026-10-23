#!/usr/bin/env python3
"""Creation-only PRE-EXEC for exactly ONE bounded M2H v6_3 pipeline pilot (parent instruction after the v6_3 source GO,
review/pa19-m2h-v6-3-codex-v1.note.md). Binds the review pack, contract, supervisor v6, every contract source, the pilot
prelaunch/closeout checkers, receipts and parent notes; fixes the exact item list (first three contract items, all direct)
and the exact runner argv. Metadata only: no claim, pin, job, record or native work.
"""
import hashlib
import json
import time
from pathlib import Path

L = Path(__file__).resolve().parents[1]
REVIEW = Path('/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review')
PY = '/Users/jinleic/.local/state/research-explorer/venv/bin/python'
CONTRACT = ('cycle2/m2h-a2-v6_3-contract-20261018T110631.json','835ca4b2a9e11313b1663c5c14bba7e1e9c325b06a866abc09838cac6c5a1930')
PACK = ('cycle2/m2h-v6_3-review-pack-20261018T113603.json','07214aa1b0fed523221c3f559717982bc28d30a0b95c0e98e73530c84449c115')
SUP = ('src/supervise_pa19_v6.py','adc5cc0656b73670fa9003a609a90f271255822f24e194c31df7250efb18e075')
PARENT = {str(REVIEW/'pa19-m2h-v6-3-codex-v1.note.md'):'ddcd6aa04e4b4ddc9d6336589d3f86d68ee2ecefad6ad966eda98a7f14682ca3',
          str(REVIEW/'pa19-m1-retry543-end-notice-v1.md'):'7cd962a6591806b86c8df24454c3aa3bc3a4417c3e0ee2ef0511521d8eeef385'}
RECEIPTS = {'cycle2/m2h-v6_3-binding-census-20261018T113533.json':'db6a039bc80272b45150785e94a98e4c4ba8c8b1efd1de465cb0ff820eef4248',
            'cycle2/m2h-v6_3-controls-1792347023007834000/receipt.json':'2600670c6e8c0074156e4bbca4aeb1bfc934ac99c31d7fce70cd376632cd9332',
            'cycle2/supervise-v6-control-20261018T110305/receipt.json':'988237d438f11d799b07ab7ab4af2bc62dcf8e4d72efa688f9b7af461733c6da'}
TOOLS = ('src/m2h_gate_preview_v6_3.py','src/m2h_binding_census_v6_3.py','src/check_m2h_v6_3.py','src/control_supervise_pa19_v6.py',
         'src/m2h_v6_3_pilot_prelaunch.py','src/m2h_v6_3_pilot_closeout.py','src/freeze_m2h_v6_3_pilot_preexec.py')
AMENDMENT = REVIEW/'parent-rule-amendment-long-job-stability-v1.md'
MONITOR = REVIEW/'disk-monitor-v1-20261018T0722-to-1810.jsonl'
LONG_JOB_RULE = {'min_free':13500000000,'window_seconds':300,'min_samples':25,'min_span_seconds':290,'max_age_seconds':30,
                 'drop_floor':300000000,'runway_divisor':12}
MONITORS = [{'pid':60597,'marker':'rss_watchdog4'},{'pid':60600,'marker':'checkpoint_clock'},{'pid':60602,'marker':'stop_k1_timer'}]
MAX_ATTEMPTS = 3


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    host_iso = time.strftime('%Y-%m-%dT%H:%M:%S%z'); host_iso = host_iso[:-2]+':'+host_iso[-2:]
    for p,h in [CONTRACT,PACK,SUP]: assert digest(L/p) == h, p
    for p,h in list(PARENT.items())+[(L/k,v) for k,v in RECEIPTS.items()]: assert digest(p) == h, p
    c = json.loads((L/CONTRACT[0]).read_bytes())
    assert c['source_sha256'][SUP[0]] == SUP[1]
    items = c['items'][:MAX_ATTEMPTS]
    assert all(x['mode'] == 'direct' for x in items)
    bindings = {CONTRACT[0]:CONTRACT[1],PACK[0]:PACK[1]}
    bindings.update(c['source_sha256']); bindings.update(RECEIPTS); bindings.update(PARENT)
    bindings.update({t:digest(L/t) for t in TOOLS}); bindings[str(AMENDMENT)] = digest(AMENDMENT)
    for ref in c['skeletons'].values(): bindings[ref['path']] = ref['sha256']
    for x in items: bindings[x['historical']['path']] = x['historical']['sha256']
    argv = ['/usr/bin/env','PYTHONDONTWRITEBYTECODE=1',PY,'-B',str(L/'src/run_m2h_v6_3.py'),str(L/CONTRACT[0]),CONTRACT[1],'--max-attempts',str(MAX_ATTEMPTS)]
    pre = {'schema':'PA19-M2H-V6_3-PILOT-PRE-EXEC-v1','host_clock_iso':host_iso,
        'status':'FROZEN; launch only after an explicit parent GO bound to this file SHA-256; one pipeline, no retry, no relaunch',
        'authority':{'source_go':'review/pa19-m2h-v6-3-codex-v1.note.md (GO source acceptance; pilot admission held only on the M1 retry-543 end notice)',
                     'operational_release':'review/pa19-m1-retry543-end-notice-v1.md','instruction':'Main message after the v6_3 re-review: freeze a PRE-EXEC for exactly ONE bounded M2H pipeline pilot'},
        'review_pack':{'path':PACK[0],'sha256':PACK[1]},
        'contract':{'path':CONTRACT[0],'sha256':CONTRACT[1],'items':len(c['items']),'source_sha256':c['source_sha256']},
        'supervisor':{'path':SUP[0],'sha256':SUP[1]},
        'pilot':{'runner':'src/run_m2h_v6_3.py','max_attempts':MAX_ATTEMPTS,'items':[x['id'] for x in items],
                 'item_bindings':[{'contract_position':i,'id':x['id'],'mode':x['mode'],'multiset':x['multiset'],'b_index':x['b_index'],
                                   'expected_cnf_sha256':x['expected_cnf_sha256'],'expected_cnf_bytes':x['expected_cnf_bytes'],
                                   'native_seconds':x['native_seconds'],'solver':x['solver'],'historical':x['historical']} for i,x in enumerate(items)],
                 'why_exact':'the prelaunch gate proves a fresh v6_3 namespace (no item artifact, claim or chunk); the runner walks the contract in '
                             'order, claims and attempts each item at most once and stops after --max-attempts 3 or on any stop path, so it can only '
                             'claim/attempt contract positions 0..2; a skipped item is impossible without an existing record/claim',
                 'split_path':'not exercised: the first B100 interval is at contract position 617; split-path runtime evidence remains required '
                              'before any expansion'},
        'argv':argv,'cwd':str(L),'log':'cycle2/m2h-v6_3-pilot-run-<host stamp>.log (created with noclobber)',
        'policy_clocks':c['policy_clocks'],'min_launch_headroom_seconds':2850,
        'disk_gate':{'base_gate_bytes':12200000000,'projected_growth_bytes':c['resource_policy']['whole_plan_remaining_bound_bytes'],
                     'note':'projected growth = the frozen whole-plan retained bound (the runtime per-item bound is 64 MiB + 384 KiB); the '
                            'in-flight floor 12e9 B and every per-phase gate remain enforced by the reviewed runtime'},
        'long_job_rule':{'amendment':{'path':str(AMENDMENT),'sha256':digest(AMENDMENT)},'monitor':str(MONITOR),'rule':LONG_JOB_RULE,
                         'applied':'fail-closed at prelaunch although the expected duration is minutes (recorded historical service 0.25 s per '
                                   'item); worst case is bounded by the runner deadline and the 2400 s supervisor wall per item'},
        'lane_caps':{'busy_processes':4,'lane_rss_bytes':8*1024**3,'group_rss_bytes':c['resource_policy']['normal_group_rss_bytes'],
                     'tokens':'COUNT<=2 (cycle2/tokens/t0,t1); the runner holds at most one at a time','pipelines':1,
                     'singleton':'cycle2/m2h-v6_3-singleton.lock'},
        'monitors':MONITORS,
        'steps':['1 fresh gate preview: src/m2h_gate_preview_v6_3.py CONTRACT SHA (metadata only), created after this PRE-EXEC and <= 600 s before launch',
                 '2 prelaunch: src/m2h_v6_3_pilot_prelaunch.py PRE_EXEC SHA GATE_PREVIEW must exit 0 (receipt written either way)',
                 '3 launch exactly argv once, in cwd, stdout+stderr to the noclobber log; never retried or relaunched under this PRE-EXEC',
                 '4 after the runner exits: src/final_m2h_inventory_v6_3.py CONTRACT SHA --verify-formulas',
                 '5 src/m2h_v6_3_pilot_closeout.py PRE_EXEC SHA CHUNK_DIR RUN_LOG INVENTORY',
                 '6 report receipts and SHA-256s to the parent; README/checkpoint amendment'],
        'stop_rules':['any prelaunch failure: no launch; report','any runner stop path ends the pilot; no automatic retry; no relaunch without a new GO',
                      'parent stop request: SIGTERM only to this pilot runner process (no SIGKILL); the runner and owner turn it into UNKNOWN + HALT where applicable',
                      'UNKNOWN is never UNSAT; persistent vetoes are never cleared',
                      'admission closes at the frozen 17:20 policy clock; native end 17:57 with 120 s cleanup'],
        'expected_outcomes':'each attempted item ends QUALIFIED (measured UNSAT with checked DRAT, all five admissions and every binding) or '
                            'UNKNOWN/veto under the frozen semantics; every outcome is pilot evidence only',
        'scope':'pilot evidence only; no PA19 or M2 completeness; split-path runtime evidence still required; M6/M9/E0 stay parked',
        'bindings':bindings}
    dest = L/'cycle2'/('m2h-v6_3-pilot-pre-exec-%s.json' % time.strftime('%Y%m%dT%H%M%S'))
    with dest.open('x') as f:
        json.dump(pre,f,indent=1); f.write('\n')
    print(dest,digest(dest),'items',pre['pilot']['items'],'bindings',len(bindings),flush=True)


if __name__ == '__main__':
    main()
