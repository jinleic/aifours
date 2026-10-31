#!/opt/homebrew/bin/python3
"""Verify a formal rank-eight ten-point H2 model, not a Boolean target."""
import argparse
import importlib.util
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    path=pathlib.Path(__file__).with_name('frontier-20261028-eightzero-sextic-check.py')
    spec=importlib.util.spec_from_file_location('base',path);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    S={0,1,2,7,11,31,47,63};Z={0,64,128}|{192+x for x in S if x};assert len(Z)==10
    def q(x):return (sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(4))+(x&51).bit_count())%2
    assert all(q(x)==0 for x in Z)
    a=[int(x in Z) for x in range(256)]
    for i in range(8):
        for x in range(256):
            if x>>i&1:a[x]^=a[x^(1<<i)]
    sextic=[x for x,v in enumerate(a) if v and x.bit_count()==6]
    assert sextic==[63,207,243,252] and max(x.bit_count() for x,v in enumerate(a) if v)==6
    checks=0
    for basis,L,free in base.subspaces(8,6):
        gram=[sum(base.B(x,y,4)<<j for j,y in enumerate(basis)) for x in basis]
        expected=int(base.rank(gram)==6)
        for c in range(4):
            origin=sum(1<<free[j] for j in range(2) if c>>j&1)
            assert sum((origin^x) in Z for x in L)%2==expected;checks+=1
    assert checks==43180
    result={'rank':8,'formal_zero_set':sorted(Z),'size':10,'contains_origin':True,'qzero_subset':True,
            'anf_degree':6,'sextic_terms':sextic,'all_43180_affine6flat_H2_checks':True,
            'scope':'abstract quadratic/zero parity control; not an actual Boolean f or Walsh spectrum'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('formal rank8 |Z|=10 H2=43180',flush=True)


if __name__=='__main__':main()
