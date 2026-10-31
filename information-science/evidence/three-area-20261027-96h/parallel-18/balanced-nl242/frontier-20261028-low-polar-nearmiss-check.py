#!/opt/homebrew/bin/python3
"""Controls for rank-zero/rank-two-plus exclusions; none is a target witness."""
import argparse
import functools
import json
import pathlib


def fw(a):
    a=list(a);s=1
    while s<len(a):
        for i in range(0,len(a),2*s):
            for j in range(i,i+s):x,y=a[j],a[j+s];a[j]=x+y;a[j+s]=x-y
        s*=2
    return a


def rank(rows):
    basis={}
    for v in rows:
        while v:
            i=v.bit_length()-1
            if i in basis:v^=basis[i]
            else:basis[i]=v;break
    return len(basis)


def actual(flips):
    f=[x&1 for x in range(512)]
    for x in flips:f[x]^=1
    T=functools.reduce(int.__xor__,(i for i,v in enumerate(f) if v),0)
    assert len(flips) in (2,4) and sum(f)==256 and T
    sig=[1-2*v for v in f];W=fw(sig)
    direct=[sum(sig[x]*(-1 if ((x&a).bit_count()%2) else 1) for x in range(512)) for a in range(512)]
    assert W==direct and W[0]==0
    m=sum(f[x]==f[x^T] for x in range(512))//2
    pivot=T.bit_length()-1;basis=[(1<<i)^((1<<pivot) if T&(1<<i) else 0) for i in range(9) if i!=pivot]
    q=[]
    for x in range(256):
        a=functools.reduce(int.__xor__,(basis[i] for i in range(8) if x&(1<<i)),0)
        assert W[a]%8==0;q.append((W[a]//8)%2)
    zeros=q.count(0);anf=q[:]
    for i in range(8):
        for x in range(256):
            if x&(1<<i):anf[x]^=anf[x^(1<<i)]
    assert all(not anf[x] or x.bit_count()<=2 for x in range(256))
    rows=[0]*8
    for x,v in enumerate(anf):
        if v and x.bit_count()==2:
            i,j=[u for u in range(8) if x&(1<<u)];rows[i]|=1<<j;rows[j]|=1<<i
    return {'flips':flips,'truth_bits':''.join(str(v) for v in f),'T':T,'m':m,'rank':rank(rows),
            'q_zero_count':zeros,'peak':max(map(abs,W)),'direct_and_fwht_agree':True,'target_met':False}


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    q=[int((x&1)!=0 and (x&2)!=0) for x in range(256)];h=[int((x&3)==0) for x in range(256)]
    even=[4 if not q[x] else 6 for x in range(256)]
    odd=[5 if h[x] else (7 if q[x] else -7) for x in range(256)]
    k=even+odd;F=fw(odd)
    assert q.count(0)==192 and k[0]==4 and all(v!=0 for v in k)
    assert max(map(abs,k))==7 and sum(v*v for v in k)==16384 and sum(v*v for v in even)==64*84
    assert F[0]==-128 and F[3]==1664 and sum(h)==64
    assert all((even[x]//2)%2==q[x] and int(odd[x]%4==3)==q[x] for x in range(256))
    assert sum(abs(v)==1 for v in odd)==sum(abs(v)==3 for v in odd)==0
    # The lower m bound is attained, but the balance-origin condition is deliberately violated.
    assert 84==56+7*128//32
    mutated=k[:];mutated[0]=0;assert sum(v*v for v in mutated)==16368
    c0=actual([0,1]);c2=actual([336,202,71,313])
    assert (c0['rank'],c0['q_zero_count'],c0['T'],c0['peak'])==(0,256,1,508)
    assert (c2['rank'],c2['q_zero_count'],c2['T'],c2['peak'])==(2,192,228,504)
    out={'scope':'formal origin-relaxed object and two actual high-peak NON-TARGETS',
         'formal_origin_relaxed':{'rank':2,'q_zero_count':192,'k0':4,'Walsh_zero_count':0,
            'max_abs_k':7,'energy':16384,'m_from_even_energy':84,'odd_h':64,
            'odd_inverse_at_0':F[0],'odd_inverse_at_3':F[3],
            'forcing_origin_zero_breaks_energy':True,'boolean_witness':False},
         'actual_rank0_control':c0,'actual_rank2_control':c2}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('origin-relaxed rank2 model reaches m=84; real rank0/rank2 controls have peaks 508/504')


if __name__=='__main__':main()
