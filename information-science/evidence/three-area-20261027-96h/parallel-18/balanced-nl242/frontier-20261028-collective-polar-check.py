#!/opt/homebrew/bin/python3
"""Controls for collective quadratic Walsh bounds and the rank-four parity obstruction."""
import argparse
import functools
import itertools
import json
import pathlib


def fw(a):
    a=list(a);step=1
    while step<len(a):
        for i in range(0,len(a),2*step):
            for j in range(i,i+step):x,y=a[j],a[j+step];a[j]=x+y;a[j+step]=x-y
        step*=2
    return a


def flats(n,k):
    for piv in itertools.combinations(range(n),k):
        free=[i for i in range(n) if i not in piv];slots=[(r,c) for c in free for r in range(k) if c>piv[r]]
        for assignment in range(1<<len(slots)):
            basis=[1<<p for p in piv]
            for j,(r,c) in enumerate(slots):
                if assignment&(1<<j):basis[r]|=1<<c
            span=[0]
            for b in basis:span += [v^b for v in span]
            for z in range(1<<len(free)):
                origin=sum(1<<free[i] for i in range(len(free)) if z&(1<<i))
                yield basis,origin,{origin^v for v in span}


def rank(rows):
    b={}
    for v in rows:
        while v:
            i=v.bit_length()-1
            if i in b:v^=b[i]
            else:b[i]=v;break
    return len(b)


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    # Formal rank-two/z=64, m=108, D=0; correct inverse on Q's support only.
    q=[int(bool(x&1) or bool(x&2)) for x in range(256)]
    zero={x for x in range(256) if not q[x] and ((x>>2)&7)==0}
    one=[x for x in range(256) if q[x]];six=set(one[:164])
    even=[0 if x in zero else (4 if not q[x] else (6 if x in six else 2)) for x in range(256)]
    h=[int((x&4)==0) for x in range(256)]
    odd=[(-1 if q[x] else 1)*(12*h[x]-7) for x in range(256)]
    k=even+odd;QW=fw([(-1 if v else 1) for v in q]);OW=fw(odd)
    support=[i for i,v in enumerate(QW) if v]
    assert q.count(0)==64 and len(zero)==8 and k[0]==0 and max(map(abs,k))==7
    assert sum(v*v for v in k)==16384 and sum(v*v for v in even)==64*108
    assert len(support)==4 and all(abs(QW[y])==128 and OW[y]==-QW[y] for y in support)
    assert all((even[x]//2)%2==int(odd[x]%4==3) for x in range(256))
    assert sum(abs(v) in (1,3) for v in odd)==0 and any(abs(v)>128 for v in OW)
    formal={'scope':'formal labelled NON-WITNESS, m=108 collective lower bound sharp',
            'spectrum_k':k,'q_zero_count':64,'Walsh_zeros':8,'D':0,'m':108,
            'Q_support':support,'Q_Walsh':[QW[y] for y in support],
            'odd_inverse_on_Q_support':[OW[y] for y in support],
            'odd_inverse_exceeds_128_count':sum(abs(v)>128 for v in OW),'max_odd_inverse':max(map(abs,OW))}
    # For every four-variable nondegenerate quadratic phase and every affine 2-/3-flat,
    # verify dual bentness, the isotropic dimension bound and half-integer quotient sums.
    F2=list(flats(4,2));F3=list(flats(4,3));assert len(F2)==140 and len(F3)==30
    phases=iso=three=half=0
    for linear in range(16):
        for const in (0,1):
            sig=[-1 if (((x&1)*((x>>1)&1))^(((x>>2)&1)*((x>>3)&1))^((linear&x).bit_count()%2)^const) else 1 for x in range(16)]
            FS=fw(sig);assert all(abs(v)==4 for v in FS);phases+=1
            for basis,origin,S in F3:
                affine=all(sig[origin]*sig[origin^u]*sig[origin^v]*sig[origin^u^v]==1 for u,v in itertools.combinations(basis,2))
                assert not affine;three+=1
            count=0
            for basis,origin,S in F2:
                u,v=basis;affine=sig[origin]*sig[origin^u]*sig[origin^v]*sig[origin^u^v]==1
                if not affine:continue
                Fpart=fw([sig[x] if x in S else 0 for x in range(16)])
                assert sum(t!=0 for t in Fpart)==4 and all(abs(t)==4 for t in Fpart if t)
                quotient=[2*FS[i]-6*Fpart[i] for i in range(16)]
                assert sum(x%16!=0 for x in quotient)>=12
                count+=1;iso+=1;half+=1
            assert count==60
    assert phases==32 and iso==1920 and three==960 and half==1920
    # Actual balanced rank-four/z=128 high-peak control, independently computed twice.
    flips=[486,412,214,428,499,173,429,421];f=[x&1 for x in range(512)]
    for x in flips:f[x]^=1
    T=functools.reduce(int.__xor__,(i for i,v in enumerate(f) if v),0)
    sign=[1-2*v for v in f];W=fw(sign)
    assert W==[sum(sign[x]*(-1 if ((x&y).bit_count()%2) else 1) for x in range(512)) for y in range(512)]
    pivot=T.bit_length()-1;basis=[(1<<i)^((1<<pivot) if T&(1<<i) else 0) for i in range(9) if i!=pivot]
    qvals=[]
    for x in range(256):
        y=functools.reduce(int.__xor__,(basis[i] for i in range(8) if x&(1<<i)),0)
        assert W[y]%8==0;qvals.append((W[y]//8)%2)
    anf=qvals[:]
    for i in range(8):
        for x in range(256):
            if x&(1<<i):anf[x]^=anf[x^(1<<i)]
    assert all(not anf[x] or x.bit_count()<=2 for x in range(256))
    rows=[0]*8
    for x,v in enumerate(anf):
        if v and x.bit_count()==2:
            i,j=[t for t in range(8) if x&(1<<t)];rows[i]|=1<<j;rows[j]|=1<<i
    m=sum(f[x]==f[x^T] for x in range(512))//2
    assert sum(f)==256 and T==86 and rank(rows)==4 and qvals.count(0)==128 and m==250 and max(map(abs,W))==496
    actual={'scope':'actual balanced rank4 high-peak NON-TARGET','flips':flips,'truth_bits':''.join(map(str,f)),
            'T':T,'rank':4,'q_zero_count':128,'m':m,'peak':max(map(abs,W)),'direct_and_fwht_agree':True}
    out={'formal_rank2':formal,'dual_phase_count':phases,'affine_threeflat_checks':three,
         'isotropic_twoflat_checks':iso,'half_integer_checks':half,'actual_rank4':actual}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('rank2 m108 formal near-miss; 1920 rank4 half-integer checks; real rank4 peak496')


if __name__=='__main__':main()
