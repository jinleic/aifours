#!/opt/homebrew/bin/python3
"""Check the center-sign overlay for the 1,536 extremal quadratic phases."""
import argparse
import collections
import importlib.util
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    path=pathlib.Path(__file__).with_name('frontier-20261028-extremal-sign-syndrome-check.py')
    spec=importlib.util.spec_from_file_location('phase',path);phase=importlib.util.module_from_spec(spec);spec.loader.exec_module(phase)
    def q6(x):return sum(((x>>i)&1)*((x>>(i+1))&1) for i in (0,2,4))%2
    S={0,1,2,7,11,31,47,63};H0=set(range(16))
    D7={x for x in range(64) if q6(x)^((12&x).bit_count()%2)^1}
    D3={x for x in range(64) if q6(x)^((60&x).bit_count()%2)}
    V={0,3,7,11,12,13,14,16,32,48}
    H1={0,3,13,14,16,19,29,30,32,35,45,46,48,51,61,62}
    H2={0,7,11,12,16,23,27,28,32,39,43,44,48,55,59,60}
    reps={'8-8-8-22':([S,S,S,S^D7],255),
          '8-8-14-16':([S,S,S^H0,S^(H0^D3)],143),
          '10-12-12-12':([V,V^H0,V^H1,V^H2],0)}
    result={}
    for name,(slices,center) in reps.items():
        h=[int((x&63) in slices[x>>6]) for x in range(256)];assert h[center]==1
        pairs=collections.Counter()
        for linear in range(256):
            for constant in (0,1):
                Q=[q6(x&63)^(((x>>6)&1)*((x>>7)&1))^((linear&x).bit_count()%2)^constant for x in range(256)]
                r=[(1+6*Q[x]+4*h[x])%8 for x in range(256)]
                b0=[int(v in (1,3)) for v in r];F=phase.fw([r[x]-8*b0[x] for x in range(256)])
                assert F[0]%8==0 and (F[0]//8)%16 in (5,11)
                A=5 if (F[0]//8)%16==5 else -5;alpha=1 if A==5 else -1
                assert (A,r[center]) in ((5,3),(-5,5))
                assert all(((F[y]//8)-A*(-1 if ((center&y).bit_count()%2) else 1))%16==0 for y in range(256))
                assert b0[center]+alpha not in (0,1)
                pairs[(A,r[center])]+=1
        assert pairs=={(5,3):256,(-5,5):256}
        result[name]={'center':center,'amplitude_and_residue_counts':{f'{A},{r}':n for (A,r),n in pairs.items()}}
    for t in range(-251,252):
        if t%16==5:assert t*t>=55-6*t
    out={'scope':'finite center-sign controls; not a target witness',
         'representatives':result,'all_1536_phases_checked':True,
         'center_same_sign_bit_flip_is_invalid':True,'quadratic_inequality_checked_on_sample':True}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('all 1536 phases: center permits only the sign opposite its inverse syndrome')


if __name__=='__main__':main()
