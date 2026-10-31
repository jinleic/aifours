#!/opt/homebrew/bin/python3
"""Exact counterexample to the invalid six-variable cubic weight-divisibility claim."""
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
    # Six-variable cubic, translated so the zero-frequency point lies in its support.
    def p6(x):return int(x&7==7)^int(x&56==56)^int(x&11==11)
    H=[p6(x^7) for x in range(64)];terms=anf(H,6)
    assert sum(H)==14 and H[0]==1 and max(t.bit_count() for t in terms)==3
    # Embed as the even mod8 zero-indicator on an anisotropic rank-two quadratic's radical.
    qint=[(x&1)+((x>>1)&1)+int(x&3==3) for x in range(256)]
    h=[1^H[x>>2] for x in range(256)];g=[(qint[x]+2*h[x])%4 for x in range(256)]
    q=[int(x&3!=0) for x in range(256)]
    assert max(t.bit_count() for t in anf(h,8))==3 and all(g[x]%2==q[x] for x in range(256))
    assert collections.Counter(g)=={0:14,1:78,2:50,3:114}
    zeros=[x for x in range(256) if g[x]==0];four=[x for x in range(256) if g[x]==2]
    one=[x for x in range(256) if g[x]==1];three=[x for x in range(256) if g[x]==3]
    k=[0]*256
    for i,x in enumerate(four):k[x]=4 if i<11 else -4
    for i,x in enumerate(one):k[x]=2 if i<4 else -6
    for i,x in enumerate(three):k[x]=-2 if i<1 else 6
    assert k[0]==0 and max(map(abs,k))==6 and sum(k)==128 and sum(x*x for x in k)==64*118
    assert sum(abs(x)==2 for x in k)==5 and len(zeros)==14 and len(three)==114
    out={'scope':'even-half formal NON-WITNESS refuting unconditional cubic divisor-8 claims',
         'six_variable_indicator_weight':14,'six_variable_indicator_ANF':terms,'contains_origin':True,
         'cubic_correction_ANF':anf(h,8),'q_zero_count':64,'q_polar_rank':2,
         'Z':14,'g3_count':114,'g3_mod8':2,'even_k':k,'even_sum':128,
         'even_squared_sum':7552,'m_from_even_energy':118,'even_magnitude_2_count':5,
         'odd_half_or_Boolean_realization_provided':False}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('cubic weight14: Z=14 and G3=114; formal even energy m118 and first sum128')


if __name__=='__main__':main()
