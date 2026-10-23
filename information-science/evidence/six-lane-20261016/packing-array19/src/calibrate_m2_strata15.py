#!/usr/bin/env python3
"""NEW parent-fixed five-stratum CALIBRATION ONLY; no launch before source-review PASS.
Unchanged B build_partbatch/cnf_bytes and complete original B100 intervals; kissat600/check1200/guard15/caps/COUNT<=2.
Exactly b70[0..24],b13[0..99],b20[0..99],b31[0..99],b55[0..99], one staged call each. A started/completed selection
is a recorded conflict, not substituted or duplicated. Outputs are creation-only outside coverage trees/count=false.
One3h chunk with90s receipt reserve and conservative2400s next-stage allowance, checked before/after token and
BigLock waits by the runner-local budget overlay; immutable guard15 proof/ownership logic is unchanged.
Usage: calibrate_m2_strata15.py CONTRACT_JSON EXPECTED_CONTRACT_SHA256
"""
import datetime
import hashlib
import json
import sys
import time
from pathlib import Path

import aggregate16 as AG
import encode_skel_b as ENC
import stream_check15 as S
from calibration_chunk_budget import ChunkBudget

LANE = Path(__file__).resolve().parent.parent
P0 = [4,3,3,3,3,3]
SELECTED = [(70,[0,24]),(13,[0,99]),(20,[0,99]),(31,[0,99]),(55,[0,99])]


class SelectionConflict(Exception):
    pass


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def write_x(p,value):
    with Path(p).open('x') as f:
        json.dump(value,f,indent=1)


def main():
    cp = Path(sys.argv[1]).resolve()
    assert sha(cp) == sys.argv[2]
    contract = json.loads(cp.read_text())
    jobs = contract['jobs']
    assert [(r['b_index'],r['indices']) for r in jobs] == SELECTED
    assert (contract['native_seconds'],contract['check_seconds'],contract['chunk_seconds'],contract['allowance_seconds']) == (600,1200,10800,2400)
    S.install_sigterm_handler()
    S.set_stop_files([str(LANE/'cycle2'/'STOP-m2r12')])
    run_cutoff = datetime.datetime.fromisoformat('2026-10-18T18:31:43-07:00').timestamp()
    budget = ChunkBudget(S,run_cutoff)
    outdir = LANE/'cycle2'/contract['output_directory_name']
    assert outdir.parent == LANE/'cycle2' and outdir.name.startswith('m2-kissat-strata-calibration-')
    outdir.mkdir(exist_ok=False)
    summaries,stop_reason = [],None
    for job in jobs:
        bi = job['b_index']
        lo,hi = job['indices']
        label = 'calibration_ms09_b%05d_%05d_%05d' % (bi,lo,hi)
        hold = {}
        why = stop_reason or budget.reason()
        if why:
            r = {'status':'DEFERRED/UNKNOWN','checked':False,'reason':why,'no_staged_call':True}
        else:
            def build():
                assert sha(cp) == sys.argv[2], 'contract changed after token wait'
                for rel,expected in contract['source_and_input_sha256'].items():
                    assert sha(LANE/rel) == expected, 'source/input changed: '+rel
                assert sha(S.KISSAT) == contract['kissat_binary_sha256'] and sha(S.DT) == contract['drat_trim_binary_sha256']
                original = LANE/'cycle2'/'m2part_drat'/('ms09_b%05d' % bi)/('batch_%05d_%05d.json' % (lo,hi))
                claim = LANE/'cycle2'/'claims'/('m2pbd9_ms09_b%05d.claim' % bi)
                if original.exists() or claim.exists():
                    raise SelectionConflict('selected original batch/case already started/completed; no duplicate or substitute')
                ep = LANE/job['list_path']
                raw = ep.read_bytes()
                assert hashlib.sha256(raw).hexdigest() == job['list_sha256']
                E = json.loads(raw)
                assert E['num_placements'] == len(E['placements']) == job['complete_placement_denominator']
                assert E['raw_class_assignments'] == job['raw_class_assignments'] and E['automorphisms'] == job['automorphisms']
                D = json.loads((LANE/contract['skeleton_path']).read_text())
                sk = D['skeletons'][bi]
                special = [p for p in D['profiles'] if list(p) != P0]
                nv,cl = ENC.build_partbatch(D['c0'],[tuple(t) for t in sk['types']],sk['empty'],special,
                                           [E['placements'][i] for i in range(lo,hi+1)])
                cnf = ENC.cnf_bytes(nv,cl)
                digest = hashlib.sha256(cnf).hexdigest()
                hold.update(cnf_sha256=digest,cnf_bytes=len(cnf))
                why = budget.reason()
                if why:
                    raise S.AdmissionDenied(why)
                write_x(outdir/(label+'.cnf-pin.json'),{'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
                    'purpose':'CALIBRATION ONLY, pinned before solver child','b_index':bi,'indices':[lo,hi],
                    'cnf_sha256':digest,'cnf_bytes':len(cnf),'list_sha256':job['list_sha256'],
                    'complete_placement_denominator':E['num_placements'],'contract_sha256':sys.argv[2],
                    'cnf_retained':False,'proof_retained':False})
                return cnf
            try:
                with budget:
                    r = S.kissat_staged(build,str(LANE/'scratch'/'fifo'/label),600,1200)
            except SelectionConflict as exc:
                r = {'status':'CONFLICT/UNKNOWN','checked':False,'reason':str(exc),'selection_conflict':True,
                     'no_native_child_for_conflict':True}
            except (Exception,SystemExit) as exc:
                stop_reason = repr(exc)
                r = {'status':'UNKNOWN','checked':False,'reason':stop_reason}
        r.update(multiset=9,b_index=bi,indices=[lo,hi],placements=hi-lo+1,purpose='CALIBRATION ONLY',
                 runner='calibrate_m2_strata15.py',encoder='encode_skel_b.build_partbatch',
                 count_for_scientific_coverage=False,proof_retained=False,contract_sha256=sys.argv[2],
                 calibration_scope_bound=bool(hold and r.get('cnf_sha256') == hold['cnf_sha256']),
                 chunk_alarm_fired=budget.alarm_fired)
        if r.get('status') == 'SAT':
            candidate = outdir/(label+'.candidate-solver.txt')
            with candidate.open('x') as f:
                f.write(r.get('solver_out',''))
            r.update(candidate_solver_path=str(candidate.relative_to(LANE)),candidate_solver_sha256=sha(candidate),candidate_verified=False)
        r['solver_out'] = ''
        r['calibration_valid_unsat'] = bool(r['calibration_scope_bound'] and AG.certified(r))
        r['service_seconds_per_placement'] = (r.get('solve_seconds',0)+r.get('check_seconds',0))/(hi-lo+1) if 'solve_seconds' in r else None
        write_x(outdir/(label+'.json'),r)
        summaries.append({k:r.get(k) for k in ('b_index','indices','status','checked','calibration_valid_unsat',
            'solve_seconds','check_seconds','service_seconds_per_placement','cnf_sha256','reason','selection_conflict')})
        print(json.dumps(summaries[-1]),flush=True)
        if r.get('status') == 'SAT' or S.ABORT[0] or r.get('admission_denied'):
            stop_reason = 'SAT candidate/abort/admission refusal: remaining fixed selections deferred, no substitution'
    write_x(outdir/'summary.json',{'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'purpose':'CALIBRATION ONLY',
        'count_for_scientific_coverage':False,'records':summaries,'full_route_go':False,
        'scope':'fixed size strata; samples never certify unsolved sibling placements/cases'})
    print(outdir,flush=True)


if __name__ == '__main__':
    main()
