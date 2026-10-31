#!/opt/homebrew/bin/python3
"""Independent direct inverse, FWHT correlation and algebra audit of D12 non-witness."""
import argparse
import collections
import json
import pathlib


def fw(a):
    a=list(a);s=1
    while s<len(a):
        for i in range(0,len(a),2*s):
            for j in range(i,i+s):x,y=a[j],a[j+s];a[j]=x+y;a[j+s]=x-y
        s*=2
    return a


def anf(a):
    a=list(a)
    for j in range(8):
        for x in range(256):
            if x&(1<<j):a[x]^=a[x^(1<<j)]
    return [x for x,v in enumerate(a) if v]


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    r=json.loads(a.input.read_text());k=r['spectrum_k'];assert len(k)==512 and k[0]==0
    direct=[sum(k[x]*(-1 if ((x&y).bit_count()%2) else 1) for x in range(512)) for y in range(512)]
    assert direct==fw(k);num=fw([x*x for x in direct]);assert all(x%512==0 for x in num)
    corr=[x//512 for x in num];assert corr[0]==16384
    invbad=sum(v not in(-128,128) for v in direct);cbad=sum(v!=0 for v in corr[1:])
    assert (invbad,cbad)==(483,506) and max(map(abs,corr[1:]))==5760
    q=[(v//2)%2 for v in k[:256]];Q=[int(v%4==3) for v in k[256:]]
    def polar(v):return [[v[0]^v[1<<i]^v[1<<j]^v[(1<<i)^(1<<j)] for j in range(8)] for i in range(8)]
    P=polar(q);assert P==polar(Q)
    for v in(q,Q):
        for x in range(256):
            for i in range(8):
                for j in range(8):assert v[x]^v[x^(1<<i)]^v[x^(1<<j)]^v[x^(1<<i)^(1<<j)]==P[i][j]
    rows=[sum(P[i][j]<<j for j in range(8)) for i in range(8)];assert rows==[2,1,0,0,0,0,0,0]
    h=[int(abs(v) in(3,5)) for v in k[256:]];assert max(x.bit_count() for x in anf(h))==3
    # Independently recover even mod8 lift and its cubic ANF.
    qi=[(x&1)+((x>>1)&1)+int(x&3==3) for x in range(256)]
    g=[(v//2)%4 for v in k[:256]];assert all((g[x]-qi[x])%2==0 for x in range(256))
    t=[((g[x]-qi[x])%4)//2 for x in range(256)];assert max(x.bit_count() for x in anf(t))==3
    assert collections.Counter(map(abs,k[256:]))=={1:2,3:10,5:134,7:110}
    assert sum(k)==128 and sum(v*v for v in k)==16384 and sum(Q)==192
    out={'scope':'independent direct/FWHT and common-polar audit of a formal NON-WITNESS',
         'direct_inverse_agrees':True,'autocorrelation_crosschecked':True,'q_Q_all_second_derivatives_checked':True,
         'common_polar_rank':2,'even_mod8_cubic_degree':3,'odd_h_degree':3,
         'inverse_failures':invbad,'nonzero_correlation_failures':cbad,'max_abs_correlation':5760}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('D12 independent direct/FWHT audit: common rank2 cubic, 483 inverse/506 correlation failures')


if __name__=='__main__':main()
