#!/opt/homebrew/bin/python3
"""Exact 3x512 phase checks for rank-eight extremal sign syndromes."""
import argparse
import collections
import json
import pathlib


def fw(v):
    a=list(v);step=1
    while step<len(a):
        for i in range(0,len(a),2*step):
            for j in range(i,i+step):
                x,y=a[j],a[j+step];a[j]=x+y;a[j+step]=x-y
        step*=2
    return a


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
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
    results={}
    for name,(sl,center) in reps.items():
        h=[int((x&63) in sl[x>>6]) for x in range(256)];assert sum(h)==46
        amplitudes=collections.Counter();positive=None
        for linear in range(256):
            for constant in (0,1):
                Q=[q6(x&63)^(((x>>6)&1)*((x>>7)&1))^((linear&x).bit_count()%2)^constant for x in range(256)]
                r=[(1+6*Q[x]+4*h[x])%8 for x in range(256)]
                k0=[v-8*int(v in (1,3)) for v in r];F=fw(k0)
                assert all(x%8==0 for x in F)
                residue=(F[0]//8)%16;assert residue in (5,11)
                amplitude=5 if residue==5 else -5
                assert all(((F[y]//8)-amplitude*(-1 if ((center&y).bit_count()%2) else 1))%16==0 for y in range(256))
                amplitudes[amplitude]+=1
                if positive is None:
                    kcopy=k0[:];kcopy[center]-=8*amplitude;iv=fw(kcopy)
                    assert all(v%128==0 for v in iv) and abs(kcopy[center])>7
                    wrong=k0[:];wrong[center^1]-=8*amplitude
                    assert any(v%128 for v in fw(wrong))
                    positive={'linear_phase':linear,'constant_phase':constant,'amplitude':amplitude,
                              'changed_frequency':center,'changed_value':kcopy[center],
                              'peak_bound_deliberately_broken':True,'all_inverse_sums_divisible_128':True,
                              'wrong_frequency_mutation_rejected':True}
        assert amplitudes=={-5:256,5:256}
        results[name]={'center':center,'phase_count':512,'amplitudes':dict(amplitudes),'near_miss':positive}
    out={'scope':'finite phase table and deliberately nonphysical near misses; not Boolean witnesses',
         'representatives':results,'all_1536_phases_and_393216_inverse_positions_checked':True}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('1536 phases: inverse syndrome = ±5 times the stated center character')


if __name__=='__main__':main()
