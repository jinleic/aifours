#!/usr/bin/env python3
"""Independent bounded parent aid for B0S and MXG; finite evidence only, not a universal proof.
No worker code is imported. Exact ordered-product bit DP, independently cross-checked by combinations;
H0's B=0 interval against direct counts; generated words with genuine empty gaps in the stated families.
"""
import hashlib,itertools,json,os,random,time
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
ROOT=Path(__file__).resolve().parent
SEED=202610180508

def cyclic_shift(mask,v,p):
    v%=p
    return ((mask<<v)|(mask>>(p-v)))&((1<<p)-1)

def raw_dp(w,p,target=None):
    target=2*p if target is None else target
    plus=[0]*(target+1);minus=[0]*(target+1);plus[0]=1
    for pos,(v,e) in enumerate(w):
        for n in range(min(target-1,pos),-1,-1):
            a=cyclic_shift(plus[n],v,p);b=cyclic_shift(minus[n],-v,p)
            if e==1:plus[n+1]|=a;minus[n+1]|=b
            else:minus[n+1]|=a;plus[n+1]|=b
    return bool(plus[target]&1)

def direct(w,p,m):
    for ids in itertools.combinations(range(len(w)),m):
        v,e=0,1
        for i in ids:
            a,b=w[i];v=(v+e*a)%p;e*=b
        if v==0 and e==1:return True
    return False

def windows_hit(runs,ys,p,kappa):
    # General half-window with all constant blocks odd, hence beta=0.
    k=len(runs);A=sum(a for a,b in runs);B=sum(b for a,b in runs)
    theta=[(ys[i-1]-ys[i])%p for i in range(k)]
    lo=-min(p,A-kappa-1,A//2);hi=min(p,B-kappa-1,B//2)
    def hit(u,l,h):return l<=h and l+(u-l)%p<=h
    if hit(0,lo,hi):return 0
    full=(1<<k)-1
    for mask in range(1,full):
        m=sum(bool(mask&(1<<i)) and not bool(mask&(1<<((i-1)%k))) for i in range(k))
        DP=sum(a-b for i,(a,b) in enumerate(runs) if mask>>i&1)
        E=DP+B;R=A+B
        up=min(p-m,E-kappa+m-1,E//2)
        low=-min(p-m,R-E-kappa+m-1,(R-E)//2)
        u=sum(theta[i] for i in range(k) if mask>>i&1)*((p+1)//2)%p
        if hit(u,low,up):return mask
    return None

def composition(n,k,rng,positive=False):
    z=[1 if positive else 0]*k;remaining=n-sum(z)
    assert remaining>=0 and k>0
    for _ in range(remaining):z[rng.randrange(k)]+=1
    return z

def generated(p,kind,rng):
    while True:
        k=rng.randint(3,p);kap=rng.randint(1,p-1)
        if kind=='B0S':
            if k<2*kap+1:continue
            B=0
        else:
            if kap<2:continue
            B=rng.randint(1,kap-1)
        R=2*p-k+2*kap;A=R-B
        if A>2*p-1 or A<B or R<1:continue
        H=p-1-kap
        halves=composition(H,k,rng);lengths=[2*t+1 for t in halves]
        # One specified empty gap is always present; all nonempty runs are pure.
        order=list(range(k));rng.shuffle(order)
        if B:
            np=rng.randint(1,min(A,k-2));nn=rng.randint(1,min(B,k-np-1))
            positive=order[:np];negative=order[np:np+nn]
            ap=composition(A,np,rng,True);bn=composition(B,nn,rng,True)
            runs=[(0,0)]*k
            for i,n in zip(positive,ap):runs[i]=(n,0)
            for i,n in zip(negative,bn):runs[i]=(0,n)
        else:
            np=rng.randint(1,min(A,k-1));runs=[(0,0)]*k
            for i,n in zip(order[:np],composition(A,np,rng,True)):runs[i]=(n,0)
        ys=[rng.randrange(p) for _ in range(k)]
        if any(a+b==0 and ys[i-1]==ys[i] for i,(a,b) in enumerate(runs)):continue
        return k,kap,runs,lengths,ys

def word(runs,lengths,ys,p):
    out=[]
    for (a,b),l,y in zip(runs,lengths,ys):out.extend([(1,1)]*a+[(p-1,1)]*b+[(y,-1)]*l)
    return out

def main():
    start=time.monotonic();rng=random.Random(SEED);fail=[]
    result={'at':datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),'seed':SEED,'scope':'bounded independent aids only; not universal proof','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    control=0
    for p in (5,7,11):
        for _ in range(120):
            w=[(rng.randrange(p),rng.choice((-1,1))) for _ in range(9)];t=rng.randrange(10)
            assert raw_dp(w,p,t)==direct(w,p,t);control+=1
        # Sharp boundary: two blocks, length4p-2, kappa0, outside B0S/MXG hypotheses.
        w=[(1,1)]*(2*p-1)+[(0,-1)]*(2*p-1)
        assert not raw_dp(w,p)
        assert raw_dp(w+[(0,-1)],p);control+=2
    result['raw_dp_controls']=control
    algebra=0
    for p in (5,7,11,13,17,19,23,29,31):
        for kap in range(1,(p-1)//2+1):
            for k in range(2*kap+1,p+1):
                R=2*p-k+2*kap
                for m in range(1,k//2+1):
                    for E in range(R+1):
                        attainable=set()
                        for n in range(max(0,2*kap+2-2*m),min(R,2*p-2*m)+1,2):
                            for a in range(max(0,n-(R-E)),min(n,E)+1):attainable.add(a-n//2)
                        low=-min(p-m,R-E+m-kap-1,(R-E)//2)
                        high=min(p-m,E+m-kap-1,E//2)
                        assert attainable==set(range(low,high+1)),(p,kap,k,m,E)
                        algebra+=1
    result['B0S_direct_count_window_equalities']=algebra
    rows=[]
    for kind in ('B0S','MXG'):
        for p,samples in ((5,1000),(7,1400),(11,1400)):
            ct=0;multi=0;gmax=0
            for _ in range(samples):
                k,kap,runs,lens,ys=generated(p,kind,rng);w=word(runs,lens,ys,p)
                assert len(w)==4*p-2
                solved=raw_dp(w,p);pattern=windows_hit(runs,ys,p,kap)
                if not solved or pattern is None:
                    fail.append({'kind':kind,'p':p,'runs':runs,'lengths':lens,'values':ys,'raw_solved':solved,'pattern':pattern});break
                ct+=1;gmax=max(gmax,sum(a+b==0 for a,b in runs))
                if pattern:
                    m=sum(bool(pattern&(1<<i)) and not bool(pattern&(1<<((i-1)%k))) for i in range(k))
                    multi+=m>=2
            rows.append({'kind':kind,'p':p,'generated_words':ct,'all_solvable':ct==samples,'max_genuine_empty_gaps':gmax,'first_witness_multi_interval':multi})
    result['word_checks']=rows
    # Explicit CaseII arithmetic fixture; no claimed avoidance of its other windows.
    p=7;kap=3;r=[0,0,1,1,1,1,9];x=[-1,-1,1,1,1,1,5];ys=[];prev=0
    for xt in x:prev=(prev-2*xt)%p;ys.append(prev)
    assert prev==0
    Z={0,1};W={3};P=Z|W;m=2;rho=sum(r[i] for i in P);delta=sum(r[i]-2*x[i] for i in P);R=sum(r)
    conds=[rho+2*m-delta<=2*p,rho+2*m+delta>=2*kap+2,delta>=0,delta+2*m-rho<=2*p,delta+rho-2*m<=2*R-2*kap-2,delta<=R-((R-rho)%2)]
    assert all(conds) and raw_dp(word([(a,0) for a in r],[7,1,1,1,1,1,1],ys,p),p)
    result['CaseII_fixture']={'p':p,'kappa':kap,'r':r,'x':x,'Z':sorted(Z),'W':sorted(W),'six_inequalities':conds,'raw_DP_solvable':True}
    result.update(status='PASS' if not fail else 'FAIL',failures=fail,seconds=round(time.monotonic()-start,3))
    with (ROOT/'RESULT.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result))
if __name__=='__main__':main()
