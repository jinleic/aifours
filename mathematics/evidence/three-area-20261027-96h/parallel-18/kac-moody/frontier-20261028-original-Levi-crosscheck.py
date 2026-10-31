#!/usr/bin/env python3
"""Compare original three-generator and eight-letter Levi quotient engines.

The two representations generate the actual same Serre quotient under the
candidate source theorem.  They need not have the same *preliminary* reached
obstruction.  This check compares only the Serre-quotient source, full
simultaneous lowering rank and quotient kernel at four bounded cases.
"""
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


original=load('original','frontier-20261028-lift-exact.py')
levi=load('levi','frontier-20261028-levi-lie-engine.py')


def main():
    cases=[((1,1,4),1,2),((2,2,4),2,2),((3,2,4),1,3),((3,3,3),2,3)]
    output=[]
    for degree,r,s in cases:
        a=original.run_case(degree,r,s)
        b=levi.run(degree,r,s)
        actual_dimension=a['source_dim']-a['ideal_dim']
        assert actual_dimension==b['actual_S_source_dim'],(degree,r,s,'source')
        assert a['delta_mod_target_rank']==b['quotient_delta_rank'],(degree,r,s,'rank')
        assert a['quotient_kernel_dim']==b['actual_simultaneous_quotient_kernel_dim'],(degree,r,s,'kernel')
        output.append({'degree':degree,'r':r,'s':s,'quotient_source_dim':actual_dimension,
                       'quotient_delta_rank':a['delta_mod_target_rank'],
                       'quotient_kernel_dim':a['quotient_kernel_dim']})
        print('PASS',degree,'r',r,'s',s,'dim/rank/kernel',actual_dimension,a['delta_mod_target_rank'],a['quotient_kernel_dim'],flush=True)
    path=ROOT/'frontier-20261028-original-Levi-crosscheck-v1.json'
    if path.exists():raise FileExistsError(path)
    path.write_text(json.dumps({'cases':output,'scope':'finite exact Q cross-representation comparison; NOT a proof of all parameters or equality of preliminary/compressed L',
                               'not_independent_formal_or_external_review':True},indent=2)+'\n',encoding='utf-8')
    print('WROTE',path.name)


if __name__=='__main__':main()
