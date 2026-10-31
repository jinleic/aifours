#!/opt/homebrew/bin/python3
"""Deterministic rank2 D12 common-cubic placement; explicit NON-WITNESS."""
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


def anf(v):
    a=list(v)
    for i in range(8):
        for x in range(256):
            if x&(1<<i):a[x]^=a[x^(1<<i)]
    return [i for i,v in enumerate(a) if v]


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    def aff(mask,r):return ((mask&63&r).bit_count()%2)^((mask>>6)&1)
    A,B,C=28,62,52
    H=[1^int((x>>2)&7==0)^(int(bool(x&1))*aff(A,x>>2))^
       (int(bool(x&2))*aff(B,x>>2))^(int(x&3==3)*aff(C,x>>2)) for x in range(256)]
    qi=[(x&1)+((x>>1)&1)+int(x&3==3) for x in range(256)]
    g=[(qi[x]+2*H[x])%4 for x in range(256)];assert max(i.bit_count() for i in anf(H))==3
    even=[0]*256
    for i,x in enumerate([x for x in range(256) if g[x]==1]):even[x]=2 if i<8 else -6
    for x in range(256):
        if g[x]==3:even[x]=6
    for i,x in enumerate([x for x in range(256) if g[x]==2]):even[x]=4 if i<20 else -4
    assert even[0]==0 and sum(even)==0 and sum(v*v for v in even)==64*118
    assert collections.Counter(map(abs,even))=={0:8,2:8,4:56,6:184}
    slices=[int(s,16) for s in ('6110296b49c768d5','40fdcbbac27fdfae','4c0e0b7a3e7cef9e','fb757f3d2352ce73')]
    h=[(slices[x&3]>>(x>>2))&1 for x in range(256)]
    assert max(i.bit_count() for i in anf(h))==3 and [v.bit_count() for v in slices]==[28,40,36,40]
    q0=[int(x&3==3) for x in range(256)];g0=[-1 if v else 1 for v in q0];delta=[0]*256
    for i,(N,U) in enumerate(zip((2,4,2,4),(0,0,2,0))):
        for x in [x for x in range(256) if x&3==i and h[x]][:N-U]:delta[x]=g0[x]
        for x in [x for x in range(256) if x&3==i and not h[x]][:U]:delta[x]=-g0[x]
    odd=[-g0[x]*(12*h[x]-7)+8*delta[x] for x in range(256)]
    assert collections.Counter(map(abs,odd))=={1:2,3:10,5:134,7:110} and sum(odd)==128
    Q=[int(v%4==3) for v in odd];q=[(v//2)%2 for v in even]
    assert sum(Q)==192 and [i for i in anf(Q) if i.bit_count()==2]==[i for i in anf(q) if i.bit_count()==2]==[3]
    assert max(i.bit_count() for i in anf([int(abs(v) in(3,5)) for v in odd]))==3
    k=even+odd;assert sum(k)==128 and sum(v*v for v in k)==16384 and max(map(abs,k))==7
    assert (sum(abs(v)==2 for v in even)+2*sum(abs(v)==3 for v in odd))%4==0
    GH=fw([-1 if x else 1 for x in Q]);Y=[y for y,v in enumerate(GH) if v]
    OH=fw(odd);assert len(Y)==4 and all(OH[y]==128 for y in Y)
    inv=fw(k);corr=[sum(k[x]*k[x^s] for x in range(512)) for s in range(1,512)]
    assert sum(v not in(-128,128) for v in inv)==483 and sum(v!=0 for v in corr)==506
    out={'scope':'common cubic/even+odd polar placement; formal NON-WITNESS',
         'spectrum_k':k,'T':256,'D':12,'m_from_even_energy':118,'Z':8,'Q_weight':192,
         'even_first_sum':0,'odd_first_sum':128,'full_energy':16384,
         'even_q_zero_count':64,'common_polar_rank':2,'odd_h_degree':3,'even_h_degree':3,
         'even_correction_masks':[A,B,C],'odd_slice_hex':[format(v,'016x') for v in slices],
         'odd_abs_counts':{'1':2,'3':10,'5':134,'7':110},'parent_mod4_congruence_passes':True,
         'Q_support':Y,'odd_Q_support_inverse':[OH[y] for y in Y],
         'full_inverse_not_sign_count':483,'nonzero_correlation_failures':506,
         'max_abs_nonzero_correlation':max(map(abs,corr))}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('D12 common cubic formal: Q192, four Q-support inverses pass; 483 inverse failures')


if __name__=='__main__':main()
