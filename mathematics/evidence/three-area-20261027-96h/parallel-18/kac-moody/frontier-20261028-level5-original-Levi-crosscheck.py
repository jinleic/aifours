#!/usr/bin/env python3
"""Compare entire original three-generator quotient with Levi model.

One finite case per invocation. All six original Serre seeds are generated
and the full three-lowering target is retained. Finite corroboration only;
not an unbounded proof or a substitute for the full source theorem.
"""
import argparse
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('levi',ROOT/'frontier-20261028-levi-lie-engine.py')
levi=importlib.util.module_from_spec(spec);spec.loader.exec_module(levi)


def main():
    ap=argparse.ArgumentParser()
    for n in ('a','b','r','s'):ap.add_argument('--'+n,type=int,required=True)
    args=ap.parse_args();a,b,r,s=args.a,args.b,args.r,args.s;degree=(a,b,5)
    out=ROOT/f'frontier-20261028-level5-original-Levi-{a}{b}-r{r}-s{s}-v1.json'
    if out.exists():raise FileExistsError(out)
    original=levi.lift.run_case(degree,r,s)
    print('original generated',degree,'r,s',r,s,'source',original['source_dim'],'ideal',original['ideal_dim'],flush=True)
    model=levi.run(degree,r,s)
    assert original['source_dim']-original['ideal_dim']==model['actual_S_source_dim']
    assert original['delta_mod_target_rank']==model['quotient_delta_rank']
    assert original['quotient_kernel_dim']==model['actual_simultaneous_quotient_kernel_dim']
    result={'degree':degree,'r':r,'s':s,'actual_S_source_dim':model['actual_S_source_dim'],
            'full_three_lowering_quotient_rank':model['quotient_delta_rank'],
            'full_simultaneous_quotient_kernel_dim':model['actual_simultaneous_quotient_kernel_dim'],
            'original_all_six_seed_ideal_target_descent':True,'cross_representation_comparison':'PASS',
            'scope':'one exact case only; no unbounded proof or preliminary reached-image identification'}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',degree,'r,s',r,s,out.name,flush=True)

if __name__=='__main__':main()
