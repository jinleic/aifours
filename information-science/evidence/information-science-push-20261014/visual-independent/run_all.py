"""Regenerate and exactly check the six independent finite decisions and controls."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
import hashlib,json,math,platform,resource,subprocess,sys,time
from pathlib import Path
import numpy,scipy
import decide,expected_control,solve,verify,witness_search

ROOT=Path(__file__).resolve().parent
TARGETS=[(1,5),(2,6),(3,5),(4,6),(5,6),(5,7)]


def main():
    started=time.monotonic()
    subprocess.run(['clang++','-O3','-std=c++17',str(ROOT/'enumerate.cpp'),'-o',str(ROOT/'enumerate')],cwd=ROOT,check=True)
    controls=[witness_search.find_basis(c,m) for c,m in [(1,6),(5,8)]]
    assert all('white' in w and 'black' in w for w in controls)
    (ROOT/'basis_controls.json').write_text(json.dumps(controls,indent=2)+'\n')
    cases=[]
    for case,m in TARGETS:
        subprocess.run([str(ROOT/'enumerate'),str(case),str(m)],cwd=ROOT,check=True)
        enumeration=json.loads((ROOT/f'case{case}_m{m}_enumeration.json').read_text())
        assert enumeration['black_enumerated']==math.comb(m+31,m)
        assert enumeration['white_with_zero']==math.comb(m+30,m-1)
        arc=solve.run(case,m)
        decision=decide.decide(case,m)
        certificates=[{'node':n['id'],'thresholds':n['thresholds'],**n['certificate']} for n in decision['nodes'] if 'certificate' in n]
        cases.append({'case':case,'minimal_qualified_sets':witness_search.CASES[case-1],'m':m,'verdict':decision['verdict'],'method':'complete orbit enumeration; proved zero/coverage/projection filters; exact full-projection contrast-compatible support pruning; exhaustive integer thresholds; integer projection-event separators','candidate_counts':{'all_orbits':enumeration['black_enumerated'],'white_zero_column':enumeration['white_with_zero'],'black_coverage_obligations':enumeration['black_obligations'],'black_after_coverage':enumeration['black_surviving'],'white_after_projection_filter':enumeration['white_projection_filtered'],'root_arc_rounds':arc['arc_trace'],'after_root_arc':arc['surviving'],'proof_nodes':[{'node':n['id'],'before':n['before'],'after':n['after'],'kind':n['kind'],'thresholds':n['thresholds']} for n in decision['nodes']]},'branch_counts':{'decision_nodes':decision['node_count'],'split_nodes':decision['branch_nodes'],'leaves':decision['leaf_count'],'materialized_edges':sum(len(n.get('children',[])) for n in decision['nodes']),'integer_thresholds_tested':sum(len(n.get('threshold_cases',[])) for n in decision['nodes'])},'certificate_term_count':decision['separator_terms'],'certificates':certificates,'run_time_seconds':{'enumeration':enumeration['seconds'],'root_pruning':arc['seconds'],'decision':decision['seconds'],'total':enumeration['seconds']+arc['seconds']+decision['seconds']},'decision_file':f'case{case}_m{m}_decision.json'})
    relaxed=expected_control.run()
    checked=verify.run()
    canonical=['enumerate.cpp','solve.py','decide.py','witness_search.py','expected_control.py','verify.py','run_all.py','proofs.md','basis_controls.json','expected_count_control.json','verification.json']
    for case,m in TARGETS:
        canonical.extend(f'case{case}_m{m}_{suffix}' for suffix in ['enumeration.json','white.bin','black.bin','arc.json','white_ids.npy','black_ids.npy','decision.json'])
    hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in canonical}
    unit=1 if sys.platform=='darwin' else 1024
    peak_self=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*unit
    peak_children=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss*unit
    assert peak_self+peak_children<12*1024**3
    result={'scope':'six exactly specified n=5 expansion existence questions, arbitrary real secret distributions, full projected-multiset security and all-support OR contrast','independence':'derived from supplied model; no files under ai4s/visual-cryptography-optimality/ or ai4s/evidence/ were read','cases':cases,'disagreement_with_six_claims':any(x['verdict']!='NO' for x in cases),'positive_controls':controls,'expected_count_control':relaxed,'verification':checked,'reproduce_command':f'{sys.executable} {ROOT / "run_all.py"}','environment':{'python':sys.version,'numpy':numpy.__version__,'scipy':scipy.__version__,'platform':platform.platform(),'blas_threads':1,'highs_threads':1,'execution':'serial','peak_self_bytes':peak_self,'peak_children_bytes':peak_children,'peak_sum_upper_bound_bytes':peak_self+peak_children},'total_wall_seconds':time.monotonic()-started,'sha256':hashes,'trust_boundary':'finite certificates checked with exact integer/Fraction arithmetic; not Lean/kernel verification'}
    (ROOT/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'results':str(ROOT/'results.json'),'verdicts':[(c['case'],c['m'],c['verdict']) for c in cases],'expected_count_verdict':relaxed['verdict'],'total_wall_seconds':result['total_wall_seconds'],'peak_sum_upper_bound_bytes':result['environment']['peak_sum_upper_bound_bytes']}),flush=True)

if __name__=='__main__':main()
