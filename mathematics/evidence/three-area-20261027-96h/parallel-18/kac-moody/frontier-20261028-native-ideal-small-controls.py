#!/usr/bin/env python3
"""Full-space controls for multi-step native ideal generation at seed levels2,3.

Compare every weight space through level4, in BOTH subspace directions, with
the earlier exact tensor-word Levi-closure engine. These are new implementation
controls, not evidence of new scientific injectivity by themselves.
"""
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('native_control',ROOT/'frontier-20261028-lyndon-native-ideals.py')
n=importlib.util.module_from_spec(sp)
sp.loader.exec_module(n)


def main():
    out=ROOT/'frontier-20261028-native-ideal-small-controls-v1.json'
    if out.exists():
        raise FileExistsError(out)
    records=[]
    for r,s in ((1,6),(2,6),(6,1),(6,2)):
        old=n.levi.ideal_bases((4,4,4),r,s)
        new=n.ideal_bases((4,4,4),r,s)
        assert set(old)==set(new)
        total=0
        for degree in sorted(old):
            assert len(old[degree])==len(new[degree])
            for row in old[degree].rows.values():
                assert not new[degree].reduce(row)
            for row in new[degree].rows.values():
                assert not old[degree].reduce(row)
            total+=len(old[degree])
        records.append({'parameters':[r,s],'bound':[4,4,4],'weight_spaces':len(old),'total_ideal_dimension':total,
                        'all_subspaces_equal_in_both_directions':True})
        print('PASS native multi-step ideal control',r,s,'spaces',len(old),'dimension',total,flush=True)
    with out.open('x') as stream:
        json.dump({'helper_sha256':hashlib.sha256((ROOT/'frontier-20261028-lyndon-native-ideals.py').read_bytes()).hexdigest(),
                   'records':records,'status':'PASS_ALL_FOUR_FULL_SPACE_MULTI_STEP_CONTROLS',
                   'scope':'exact representation/algorithm controls only, not a new original-map theorem'},stream,indent=2)
        stream.write('\n')
    print('WROTE',out.name)


if __name__=='__main__':
    main()
