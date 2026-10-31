#!/usr/bin/env python3
"""Compare 48 independently generated original-generator quotient records
with fresh computations in the 8-letter Levi model.  Exact rational ranks only;
this is finite corroboration, not a proof of unbounded parameters.
"""
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('levi',ROOT/'frontier-20261028-levi-lie-engine.py')
levi=importlib.util.module_from_spec(spec);spec.loader.exec_module(levi)


def main():
    out=[]
    for label in ('114','224','324'):
        original=json.loads((ROOT/f'frontier-20261028-lift-{label}-rs1to4.json').read_text(encoding='utf-8'))
        assert len(original['cases'])==16
        for old in original['cases']:
            degree=tuple(old['degree']);r=old['r'];s=old['s']
            new=levi.run(degree,r,s)
            original_source=old['source_dim']-old['ideal_dim']
            assert original_source==new['actual_S_source_dim'],(degree,r,s,'source')
            assert old['delta_mod_target_rank']==new['quotient_delta_rank'],(degree,r,s,'delta')
            assert old['quotient_kernel_dim']==new['actual_simultaneous_quotient_kernel_dim'],(degree,r,s,'kernel')
            out.append({'degree':degree,'r':r,'s':s,'source_dim':original_source,
                        'quotient_delta_rank':old['delta_mod_target_rank'],
                        'quotient_kernel_dim':old['quotient_kernel_dim']})
        print('PASS',label,'16 original/Levi quotient comparisons',flush=True)
    dest=ROOT/'frontier-20261028-original-Levi-48-check-v1.json'
    if dest.exists():raise FileExistsError(dest)
    dest.write_text(json.dumps({'cases':out,'case_count':len(out),'all_match':True,
                                'not_unbounded_proof_or_preliminary_L_identification':True},indent=2)+'\n',encoding='utf-8')
    print('PASS all',len(out),'cases;',dest.name)


if __name__=='__main__':main()
