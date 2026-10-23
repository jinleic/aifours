#!/usr/bin/env python3
"""Parent-GO calibration ONLY: unchanged M2 B encoder/CNF/cover, Kissat staged DRAT instead of CaDiCaL.
Exactly B9[0..99] unstarted and B4[100..199] already-written strict-checked re-solve;600/1200, same guard15/full
predicate/caps/COUNT<=2. No helper/enumeration. All outputs have calibration* names outside scientific result trees;
NEITHER record is automatically counted for coverage. B4 is never counted a second time. New contract/source/input
SHAs are checked under the token in the constructor. Exact CNF SHA is pinned before any solver child starts;
B4 must byte-hash-identically match its original CNF. Original files are never changed/overwritten.
Usage: calibrate_m2_kissat15.py CONTRACT_JSON EXPECTED_CONTRACT_SHA256
"""
import hashlib
import json
import os
import sys
import time
from pathlib import Path

import aggregate16 as AG
import encode_skel_b as ENC
import stream_check15 as S

LANE = Path(__file__).resolve().parent.parent
P0 = [4,3,3,3,3,3]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def write_x(p, value):
    with Path(p).open('x') as f:
        json.dump(value,f,indent=1)


def main():
    contract_path = Path(sys.argv[1]).resolve()
    assert sha(contract_path) == sys.argv[2], 'contract SHA differs from parent freeze'
    contract = json.loads(contract_path.read_text())
    jobs = contract['jobs']
    assert [(r['b_index'],r['indices']) for r in jobs] == [(9,[0,99]),(4,[100,199])]
    assert contract['native_seconds'] == 600 and contract['check_seconds'] == 1200
    S.install_sigterm_handler()
    S.set_stop_files([str(LANE/'cycle2'/'STOP-m2r12')])
    outdir = LANE/'cycle2'/contract['output_directory_name']
    assert outdir.parent == LANE/'cycle2' and outdir.name.startswith('m2-kissat-calibration-')
    outdir.mkdir(exist_ok=False)
    summaries = []
    for job in jobs:
        bi = job['b_index']
        lo,hi = job['indices']
        label = 'calibration_ms09_b%05d_%05d_%05d' % (bi,lo,hi)
        hold = {}

        def build():
            assert sha(contract_path) == sys.argv[2], 'contract changed after token wait'
            for rel,expected in contract['source_and_input_sha256'].items():
                assert sha(LANE/rel) == expected, 'source/input changed: '+rel
            assert sha(S.KISSAT) == contract['kissat_binary_sha256']
            assert sha(S.DT) == contract['drat_trim_binary_sha256']
            if bi == 9:
                original = LANE/'cycle2'/'m2part_drat'/'ms09_b00009'/'batch_00000_00099.json'
                claim = LANE/'cycle2'/'claims'/'m2pbd9_ms09_b00009.claim'
                assert not original.exists() and not claim.exists(), 'B9 production batch is no longer unstarted'
            else:
                original = LANE/job['original_record']
                assert sha(original) == job['original_record_sha256']
                assert AG.certified(json.loads(original.read_text())), 'B4 original is not strict-checked'
            extpath = LANE/job['list_path']
            raw = extpath.read_bytes()
            assert hashlib.sha256(raw).hexdigest() == job['list_sha256']
            E = json.loads(raw)
            assert E['num_placements'] == len(E['placements']) == job['complete_placement_denominator']
            D = json.loads((LANE/contract['skeleton_path']).read_text())
            sk = D['skeletons'][bi]
            special = [p for p in D['profiles'] if list(p) != P0]
            # EXACT same constructor/arguments as run_m2_15.run_split, not M1 code.
            nv,cl = ENC.build_partbatch(D['c0'],[tuple(t) for t in sk['types']],sk['empty'],special,
                                       [E['placements'][i] for i in range(lo,hi+1)])
            cnf = ENC.cnf_bytes(nv,cl)
            digest = hashlib.sha256(cnf).hexdigest()
            if bi == 4:
                assert digest == job['original_cnf_sha256'], 'not byte-identical to B4 original CNF'
            hold.update(cnf_sha256=digest,cnf_bytes=len(cnf))
            write_x(outdir/(label+'.cnf-pin.json'),{'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
                'purpose':'CALIBRATION ONLY, pinned before solver child','b_index':bi,'indices':[lo,hi],
                'cnf_sha256':digest,'cnf_bytes':len(cnf),'list_sha256':job['list_sha256'],
                'complete_placement_denominator':E['num_placements'],'contract_sha256':sys.argv[2],
                'cnf_retained':False,'proof_retained':False})
            return cnf

        try:
            r = S.kissat_staged(build,str(LANE/'scratch'/'fifo'/label),600,1200)
        except (Exception,SystemExit) as exc:
            r = {'status':'UNKNOWN','checked':False,'reason':repr(exc),'scope':'calibration admission/construction failed'}
        r.update(multiset=9,b_index=bi,indices=[lo,hi],placements=hi-lo+1,purpose='CALIBRATION ONLY',
                 runner='calibrate_m2_kissat15.py',encoder='encode_skel_b.build_partbatch',
                 count_for_scientific_coverage=False,proof_retained=False,contract_sha256=sys.argv[2],
                 calibration_scope_bound=bool(hold and r.get('cnf_sha256') == hold['cnf_sha256']))
        if r.get('status') == 'SAT':
            candidate = outdir/(label+'.candidate-solver.txt')
            with candidate.open('x') as f:
                f.write(r.get('solver_out',''))
            r.update(candidate_solver_path=str(candidate.relative_to(LANE)),candidate_solver_sha256=sha(candidate),
                     candidate_verified=False)
        r['solver_out'] = ''
        r['calibration_valid_unsat'] = bool(r['calibration_scope_bound'] and AG.certified(r))
        r['service_seconds_per_placement'] = (r.get('solve_seconds',0)+r.get('check_seconds',0))/(hi-lo+1)
        write_x(outdir/(label+'.json'),r)
        summaries.append({k:r.get(k) for k in ('b_index','indices','status','checked','calibration_valid_unsat',
            'solve_seconds','check_seconds','service_seconds_per_placement','cnf_sha256','candidate_solver_sha256')})
        print(json.dumps(summaries[-1]),flush=True)
        if r.get('status') == 'SAT' or S.ABORT[0] or r.get('admission_denied') or r.get('reason'):
            break
    write_x(outdir/'summary.json',{'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'purpose':'CALIBRATION ONLY',
        'count_for_scientific_coverage':False,'records':summaries,'full_route_go':False,
        'threshold':'propose full route only if B4 valid strict UNSAT and service <=0.2 seconds/placement; parent decision required'})
    print(outdir,flush=True)


if __name__ == '__main__':
    main()
