#!/opt/homebrew/bin/python3
"""Finite arithmetic and formal sharpness controls for singular cubic zero bounds."""
import argparse
import json
import pathlib


def anf(v):
    a=list(v)
    for i in range(8):
        for x in range(256):
            if x&(1<<i):a[x]^=a[x^(1<<i)]
    return [i for i,x in enumerate(a) if x]


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    cases=[(0,256,8,32),(0,128,7,16),(2,64,6,8),(2,128,6,8),(2,192,7,16),
           (4,96,5,4),(4,128,5,4),(4,160,6,8),(6,112,4,2),(6,128,4,2),
           (6,144,5,4),(8,120,3,1),(8,136,4,2)]
    rows=[]
    for rank,z,s,Z in cases:
        m=2*((9216-20*z-16*Z)//128);lower=max(0,(64*(256-m)-6400+23)//24)
        assert Z==1<<max(0,s-3)
        rows.append({'rank':rank,'q_zero_count':z,'singular_dimension':s,'zero_lower':Z,
                     'agreeing_pair_upper':m,'peak_lower':lower})
    h=[int((x&7)==0) for x in range(256)];assert sum(h)==32
    assert max(t.bit_count() for t in anf(h))==3 and h[0]==1
    k0=[0 if h[x] else 4 for x in range(256)]+[7]*256
    assert k0[0]==0 and sum(v==0 for v in k0)==32 and max(map(abs,k0))==7
    energy0=sum(v*v for v in k0);assert energy0==16128<16384
    # q=x7, restricted cubic support is exactly a 4-flat in its 7-dimensional kernel.
    ka=[2*(((x>>7)&1)+2*(1-h[x]))%8 for x in range(256)]+[7]*256
    assert ka[0]==0 and sum(v==0 for v in ka)==16
    assert all(((ka[x]//2)%2)==((x>>7)&1) for x in range(256))
    out={'scope':'formal cubic controls and finite integer table; neither is a Boolean witness',
         'rank_and_qzero_table':rows,'constant_q_formal_zero_count':32,'constant_q_formal_energy':energy0,
         'affine_q_formal_zero_count':16,'affine_q_formal_energy':sum(v*v for v in ka),
         'formal_max_abs_k':7,'mutation_at_origin_would_break_balance':k0[0]+4!=0}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('13 rank cases; formal q=0 has 32 zeros and maximum energy 16128<16384')


if __name__=='__main__':main()
