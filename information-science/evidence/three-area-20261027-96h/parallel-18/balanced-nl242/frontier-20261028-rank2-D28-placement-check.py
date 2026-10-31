#!/opt/homebrew/bin/python3
"""Deterministic labelled D28 formal placement; exact first failures, no Boolean witness."""
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
    for i in range(8):
        for x in range(256):
            if x&(1<<i):a[x]^=a[x^(1<<i)]
    return [x for x,v in enumerate(a) if v]


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    original={6:1,16:-1,27:1,33:-1,45:1,53:-1,61:1,68:1,71:-1,74:-1,76:1,77:1,78:-1,81:1,83:-1,107:1,137:1,148:1,158:-1,166:-1,194:1,214:1,217:1,225:-1,236:-1,237:-1,244:1,254:1}
    delta=[-original.get(x,0) for x in range(256)];assert sum(v!=0 for v in delta)==28
    u,w,ell,const=92,127,5,0
    def bit(a,x):return (a&x).bit_count()%2
    q=[bit(u,x)*bit(w,x)^bit(u,x)^bit(w,x) for x in range(256)]
    Q=[bit(u,x)*bit(w,x)^bit(ell,x)^const for x in range(256)]
    assert [t for t in anf(q) if t.bit_count()==2]==[t for t in anf(Q) if t.bit_count()==2]
    R=[x for x in range(256) if q[x]==0];assert len(R)==64
    zero={0,3,12,15,20,23,24,27};assert zero<=set(R)
    inside=[x for x in R if x not in zero];outside=[x for x in range(256) if q[x]]
    even=[0]*256
    for i,x in enumerate(inside):even[x]=-4 if i<22 else 4
    for i,x in enumerate(outside):even[x]=-6 if i<100 else 6
    H=int('f839846f42d6308bfd3fae448bf3c3c722ade9a8ae070796b5a59e5409f0cde9',16)
    h=[(H>>x)&1 for x in range(256)];g=[-1 if Q[x] else 1 for x in range(256)]
    odd=[g[x]*(12*h[x]-7)-8*delta[x] for x in range(256)];k=even+odd
    assert k[0]==0 and max(map(abs,k))==7 and sum(k)==128 and sum(even)==0 and sum(odd)==128
    assert sum(t*t for t in k)==16384 and sum(t*t for t in even)==64*122
    assert {x for x,v in enumerate(k) if not v}==zero
    assert all((even[x]//2)%2==q[x] and int(odd[x]%4==3)==Q[x] for x in range(256))
    assert collections.Counter(map(abs,odd))=={1:11,3:17,5:115,7:113}
    GH=fw(g);Y=[y for y,v in enumerate(GH) if v];assert len(Y)==4 and all(abs(GH[y])==128 for y in Y)
    OH=fw(odd);assert all(OH[y]==-GH[y] for y in Y)
    DD=fw(delta);assert sum(v%3!=0 for v in DD)==130 and all(DD[y]%3==0 for y in Y)
    terms=anf(h);degree=max(x.bit_count() for x in terms);assert degree==7
    inv=fw(k);corr=[sum(k[x]*k[x^s] for x in range(512)) for s in range(1,512)]
    invbad=sum(v not in (-128,128) for v in inv);cbad=sum(v!=0 for v in corr)
    assert invbad==497 and cbad==511 and corr[0]==8032
    out={'scope':'saturated D28 labelled formal NON-WITNESS; cubic/Boolean inverse fail',
         'spectrum_k':k,'T':256,'q_zero_count':64,'zero_positions':sorted(zero),
         'zero_plane_basis':[3,12,20],'m_from_even_energy':122,'D':28,'odd_abs_counts':{1:11,3:17,5:115,7:113},
         'full_energy':16384,'full_first_sum':128,'even_first_sum':0,'odd_first_sum':128,
         'Q_support':Y,'odd_inverse_on_Q_support':[OH[y] for y in Y],
         'Dhat_nonzero_mod3':130,'odd_h_degree':degree,'h_anf_high_terms':[x for x in terms if x.bit_count()>3],
         'odd_inverse_not_ternary_count':sum(v not in(-128,0,128) for v in OH),
         'full_inverse_not_sign_count':invbad,'nonzero_correlation_failures':cbad,'correlation_at_1':corr[0]}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('D28 formal: all 4 Q-support inverses pass; h degree7, 497 inverse/511 correlation failures')


if __name__=='__main__':main()
