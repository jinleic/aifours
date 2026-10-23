#!/usr/bin/env python3
"""Read-only closeout of the ONE M2H v6_4 split-path pilot frozen in a PRE-EXEC: publisher -> exact reader -> inventory.
Binds the PRE-EXEC, the runner chunk (summary.json incl. its selection plan), the runner log and the inventory receipt;
re-reads every planned interval through the exact reader (run_m2h_v6_4.inspect); checks that published records, commits
and pins match the summary, that only the attempted planned intervals created v6_4 artifacts and that no v6_3 artifact
exists for them, and that the full-contract inventory counts the case covered iff all four intervals are QUALIFIED and
lists exactly their persistent vetoes. Writes one creation-only receipt. Pilot evidence only; no completeness claim.
Usage: m2h_v6_4_pilot_closeout.py PRE_EXEC PRE_EXEC_SHA256 CHUNK_DIR RUN_LOG INVENTORY
"""
import glob
import hashlib
import json
import sys
import time
from pathlib import Path

L = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(L/'src'))
import m2_supervised_runtime_v6_3 as R  # noqa: E402
import run_m2h_v6_4 as H  # noqa: E402


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    pre_path,pre_sha,chunk,run_log,inv_path = sys.argv[1:6]
    assert digest(pre_path) == pre_sha, 'PRE-EXEC hash differs'
    pre = json.loads(Path(pre_path).read_bytes()); chunk = Path(chunk)
    csha = pre['contract']['sha256']; cpath = L/pre['contract']['path']
    with R.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        assert digest(cpath) == csha
        c = json.loads(cpath.read_bytes()); H.verify(c)
        bad = {p:h for p,h in pre['bindings'].items() if digest(Path(p) if p.startswith('/') else L/p) != h}
        assert not bad, ('bound file changed during the pilot',bad)
        summary = json.loads((chunk/'summary.json').read_bytes())
        assert summary['contract_sha256'] == csha and summary['automatic_retry_allowed'] is False
        sp = summary['selection_plan']
        assert sp['sha256'] == pre['plan']['sha256'] and sp['selected_ids'] == pre['pilot']['items'], sp
        planned = pre['pilot']['items']; ids = [r['id'] for r in summary['records']]
        assert ids == planned[:len(ids)] and summary['attempts'] == len(ids) <= pre['pilot']['max_attempts'], (ids,summary['attempts'])
        by_id = {x['id']:x for x in c['items']}
        rows,expected = [],set()
        for ident in planned:
            x = by_id[ident]; it = H.task(x); q = H.inspect(c,csha,x); old = H.task(x,'h6_3')
            assert not any((L/old[k]).exists() for k in ('new_record','pin','commit','claim')), ('v6_3 artifact for a planned item',ident)
            row = {'id':ident,'contract_position':c['items'].index(x),'state':q['state'],'errors':[str(e)[:300] for e in q.get('errors') or []][:4]}
            if ident in ids:
                s = summary['records'][ids.index(ident)]
                row.update(record=it['new_record'],record_sha256=digest(L/it['new_record']),summary_sha_matches=digest(L/it['new_record']) == s['sha256'],
                           commit_sha256=digest(L/it['commit']),pin_sha256=digest(L/it['pin']),status=s['status'],checked=s['checked'],
                           integrity_status=s['integrity_status'])
                base = str(L/it['new_record'])[:-len('.json')]
                expected |= set(glob.glob(base+'*')) | {str(L/it['claim'])}
            else:
                assert q['state'] == 'MISSING', ('unattempted planned item has a record',ident)
            rows.append(row)
        found = set(glob.glob(str(L/'cycle2/m2skel_drat/*_h6_4*'))) | set(glob.glob(str(L/'cycle2/m2part_drat/*/*_h6_4*'))) | set(glob.glob(str(L/'cycle2/claims/m2h6_4_*')))
        assert found == expected, ('v6_4 artifacts outside the attempted planned items',sorted(found ^ expected)[:10])
        inv = json.loads(Path(inv_path).read_bytes())
        assert inv['schema'] == 'PA19-M2H-INVENTORY-v6_4' and inv['contract_sha256'] == csha and inv['formula_verification_mode'] is True
        qualified = sum(r['state'] == 'QUALIFIED' for r in rows)
        covered = 1 if qualified == len(planned) else 0
        vetoed = {r['id'] for r in rows if r['state'] in ('INTEGRITY_VETO','SAT_VETO','HALT_UNKNOWN')}
        assert inv['cases'] == c['cases_direct']+c['cases_split'] and inv['covered_cases'] == covered and inv['open_cases'] == inv['cases']-covered, \
            (inv['covered_cases'],covered)
        assert {i['id'] for i in inv['issues'] if i['state'] != 'FORMULA_MISMATCH'} == vetoed and not any(i['state'] == 'FORMULA_MISMATCH' for i in inv['issues'])
    out = {'schema':'PA19-M2H-V6_4-PILOT-CLOSEOUT-v1','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
           'pre_exec':{'path':str(Path(pre_path).resolve().relative_to(L)),'sha256':pre_sha},
           'chunk':{'path':str(chunk.resolve().relative_to(L)),'summary_sha256':digest(chunk/'summary.json'),'stop_reason':summary['stop_reason'],
                    'attempts':summary['attempts'],'selection_plan':sp},
           'run_log':{'path':str(Path(run_log).resolve().relative_to(L)),'sha256':digest(run_log)},
           'inventory':{'path':str(Path(inv_path).resolve().relative_to(L)),'sha256':digest(inv_path),'cases':inv['cases'],
                        'covered_cases':inv['covered_cases'],'open_cases':inv['open_cases'],'issues':len(inv['issues']),
                        'final_component_ready':inv['final_component_ready']},
           'items':rows,'qualified_planned_intervals':qualified,'case_covered':bool(covered),'v6_4_artifacts':len(found),
           'publisher_reader_inventory_consistent':True,
           'scope':'split-path pilot evidence for one case only; no PA19 or M2 completeness; v6_3 records stay v6_3-only; M6/M9/E0 parked',
           'source_sha256':digest(__file__)}
    dest = L/'cycle2'/('m2h-v6_4-pilot-closeout-%s.json' % time.strftime('%Y%m%dT%H%M%S'))
    with dest.open('x') as f:
        json.dump(out,f,indent=1); f.write('\n')
    print(dest,digest(dest),json.dumps({'states':[(r['id'],r['state']) for r in rows],'covered':inv['covered_cases']}),flush=True)


if __name__ == '__main__':
    R.install_handlers()
    main()
