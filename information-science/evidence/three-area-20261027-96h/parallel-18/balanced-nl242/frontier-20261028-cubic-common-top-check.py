#!/opt/homebrew/bin/python3
"""Counterexample-aware degree-3 coset congruence and Z12 even-half control."""
import argparse
import collections
import json
import pathlib


def anf(v,n):
    a=list(v)
    for i in range(n):
        for x in range(1<<n):
            if x&(1<<i):a[x]^=a[x^(1<<i)]
    return [i for i,v in enumerate(a) if v]


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    # H0 is XOR of two six-variable cubic monomials, translated by 7 to contain 0.
    H0=[int(((x^7)&7)==7)^int(((x^7)&25)==25) for x in range(64)]
    assert H0[0] and sum(H0)==12 and max(i.bit_count() for i in anf(H0,6))==3
    H=[1^H0[x>>2] for x in range(256)]
    assert max(i.bit_count() for i in anf(H,8))==3
    qi=[(x&1)+((x>>1)&1)+int(x&3==3) for x in range(256)]
    g=[(qi[x]+2*H[x])%4 for x in range(256)]
    q=[int(x&3!=0) for x in range(256)];assert all(g[x]%2==q[x] for x in range(256))
    Z=g.count(0);assert Z==12 and g[0]==0
    cosets=[[x for x in range(256) if x&3==j] for j in range(4)]
    coset3=[sum(g[x]==3 for x in c) for c in cosets[1:]]
    assert coset3==[52,52,12] and all(v%4==0 for v in coset3)
    Hcount=[sum(H[x] for x in c) for c in cosets]
    assert len({v%4 for v in Hcount})==1
    one=[x for x in range(256) if g[x]==1];three=[x for x in range(256) if g[x]==3]
    four=[x for x in range(256) if g[x]==2];k=[0]*256
    for i,x in enumerate(one):k[x]=2 if i<6 else -6
    for x in three:k[x]=6
    for i,x in enumerate(four):k[x]=4 if i<6 else -4
    assert k[0]==0 and max(map(abs,k))==6 and sum(k)==128 and sum(x*x for x in k)==64*118
    assert sum(abs(v)==2 for v in k)==6 and (6+2*7)%4==0
    out={'scope':'corrected even-half cubic/energy control; NOT a Boolean witness',
         'six_cubic_zero_indicator_weight':Z,'six_cubic_zero_indicator_ANF':anf(H0,6),
         'coset_h_weights':Hcount,'g3_coset_weights':coset3,'g3':len(three),
         'Z':Z,'E2':6,'odd_n3_parity_control':7,'even_first_sum':128,'even_squared_sum':7552,
         'even_k':k,'odd_half_or_Boolean_realization_provided':False}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('Z12 formal even-half control: cubic, G3=116, E2=6, energy m118, first sum128')


if __name__=='__main__':main()
