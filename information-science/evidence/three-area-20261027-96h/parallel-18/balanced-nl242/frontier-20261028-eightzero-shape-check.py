#!/opt/homebrew/bin/python3
"""Check a rank-six formal eight-point H2 solution with one radical period."""
import argparse
import importlib.util
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    path=pathlib.Path(__file__).with_name('frontier-20261028-eightzero-sextic-check.py')
    spec=importlib.util.spec_from_file_location('base',path);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    Z={0,128,65,68,69,193,196,197};assert len(Z)==8 and 0 in Z
    assert all((x^128) in Z for x in Z) and any((a^b) not in Z for a in Z for b in Z)
    def q(x):return sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))%2
    assert all(q(x)==0 for x in Z)
    a=[int(x in Z) for x in range(256)]
    for i in range(8):
        for x in range(256):
            if x>>i&1:a[x]^=a[x^(1<<i)]
    assert max(x.bit_count() for x,v in enumerate(a) if v)==6
    assert [x for x,v in enumerate(a) if v and x.bit_count()==6]==[63]
    checked=0
    for basis,L,free in base.subspaces(8,6):
        gram=[sum(base.B(x,y,3)<<j for j,y in enumerate(basis)) for x in basis]
        expected=int(base.rank(gram)==6)
        for c in range(4):
            origin=sum(1<<free[j] for j in range(2) if c>>j&1)
            assert sum((origin^x) in Z for x in L)%2==expected;checked+=1
    assert checked==43180
    result={'formal_zero_set':sorted(Z),'size':8,'contains_origin':True,'qzero_subset':True,
            'radical_period':128,'not_linear_3plane':True,'anf_degree':6,'sextic_terms':[63],
            'all_43180_affine6flat_H2_checks':True,
            'scope':'abstract q/Z parity control, no Boolean f or Walsh spectrum'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('formal rank6 Z8=8 period=128 nonplane H2=43180',flush=True)


if __name__=='__main__':main()
