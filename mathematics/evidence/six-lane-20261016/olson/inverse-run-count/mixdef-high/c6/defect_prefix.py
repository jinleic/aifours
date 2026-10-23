#!/usr/bin/env python3
"""[F] Literal controls of the integer defect-prefix lemma in proof-A0.md.
Arbitrary integer lifts x with sum p inside singleton windows; if Phi(Z)>=g+1, construct the first defect prefix.
Check every claimed bound and independent slow_lambda kill. Mutation: target g in place of g+1.
No all-pattern-feasibility or raw group-avoider claims are made.
"""
import random,json,time,resource
GUARD="if __name__ == '__main__':\n    main()"
N={'__name__':'replayLB_lib'}
exec(compile(open('replayLB.py').read().replace(GUARD,''),'replayLB.py','exec'),N)
G=N['G'];Wg=G['Wg'];slow=G['slow_lambda'];rnd=random.Random(192913)
C={'__name__':'seedX2lib'}
exec(compile(open('seedX2.py').read().replace(GUARD,''),'seedX2.py','exec'),C)
def word(p,k,kap,B):
    E=2*p-2*k+2*kap;npr=rnd.randrange(min(B,E)+1);Bp=B-npr
    if Bp==0:ean=0
    else:ean=rnd.randrange(min(E-npr,Bp-1)+1)
    nan=Bp-ean;nal=k-nan-npr;eal=E-npr-ean
    a0=[1]*nal;b0=[1]*nan
    for _ in range(eal):a0[rnd.randrange(nal)]+=1
    for _ in range(ean):b0[rnd.randrange(nan)]+=1
    rs=[(v,0) for v in a0]+[(0,v) for v in b0]+[(1,1)]*npr;rnd.shuffle(rs)
    a,b=map(list,zip(*rs));ls=[1]*k;ls[0]+=2*(p-1-kap)
    W=Wg(p,a,b,ls);assert (W.kappa,W.B,W.E)==(kap,B,E)
    return W

def vector(W,mode):
    lo,hi=W.single_lo,W.single_hi
    if any(a>b for a,b in zip(lo,hi)) or sum(lo)>W.p or sum(hi)<W.p:return None
    x=[rnd.randint(a,b) if mode==0 else (a if mode==1 else min(max(W.d[t]//2,a),b)) for t,(a,b) in enumerate(zip(lo,hi))]
    diff=W.p-sum(x);order=list(range(W.k));rnd.shuffle(order)
    for t in order:
        if diff>0:v=min(diff,hi[t]-x[t]);x[t]+=v;diff-=v
        elif diff<0:v=min(-diff,x[t]-lo[t]);x[t]-=v;diff+=v
    assert diff==0
    return x

def prefix(W,x,target):
    g=W.kB;c=[d-u for d,u in zip(W.d,x)];bh=[2*u-d for d,u in zip(W.d,x)]
    Z=[i for i in range(W.k) if bh[i]<=0]
    phi=lambda Q:sum(c[i] for i in Q)+W.blocks(Q)
    if not Z or phi(set(Z))<target:return None
    rnd.shuffle(Z);P=set()
    for t in Z:
        oldphi=phi(P);oldbh=sum(bh[i] for i in P);oldvalue=sum(x[i] for i in P)+W.blocks(P)
        assert oldvalue==oldphi+oldbh and oldphi<=target-1 and oldbh<=0
        before=W.blocks(P);P.add(t);after=W.blocks(P)
        assert after-before<=1 and x[t]<=W.d[t]//2<=W.E//2
        if phi(P)>=target:
            val=sum(x[i] for i in P)+after
            assert val<=target-1+W.E//2+1
            return P,phi(P),sum(bh[i] for i in P),val
    raise AssertionError('prefix not found')

def main():
    ts=time.time();st={'words':0,'vectors':0,'singleton_infeasible_words':0,'caseA':0,'caseB_skipped':0,'mutation_M_reject':0}
    for p in (5,7,11,13,17,23,31,43):
        cl=C['classes'](p)
        for k,kap,B in rnd.sample(cl,min(48,len(cl))):
            W=word(p,k,kap,B);st['words']+=1
            if any(a>b for a,b in zip(W.single_lo,W.single_hi)) or sum(W.single_lo)>p or sum(W.single_hi)<p:
                st['singleton_infeasible_words']+=1;continue
            for z in range(36):
                x=vector(W,z%3);assert x is not None;st['vectors']+=1
                ans=prefix(W,x,W.kB+1)
                if ans is None:st['caseB_skipped']+=1
                else:
                    P,phi,BH,val=ans
                    assert 0<len(P)<W.k and phi>=W.kB+1 and BH<=0
                    assert val<=W.kB+W.E//2+1<=p-W.B-2<p
                    assert sum(x[i] for i in P)<slow(p,W.d,W.l,W.B,W.kappa,sorted(P))
                    st['caseA']+=1
                bad=prefix(W,x,W.kB)
                if bad is not None and bad[1]<W.kB+1:st['mutation_M_reject']+=1
    # Scalar partition after unconditional Case A: B<=g -> k>=g+3B, else C0W or C+'s class condition.
    st2={'tuples':0,'B_le_g':0,'C0W':0,'Cplus':0}
    for p in range(5,102):
        if not C['isprime'](p):continue
        for k,kap,B in C['classes'](p):
            g=kap-B;E=2*p-2*k+2*kap
            if B<=g:assert k>=g+3*B;st2['B_le_g']+=1
            elif 3*g+1<=p:st2['C0W']+=1
            else:assert 2*g<=p and E<=2*(k-g-2*B)-1;st2['Cplus']+=1
            st2['tuples']+=1
    print(json.dumps({'prefix_controls':st,'partition_controls':st2}),flush=True)
    print(json.dumps({'seconds':round(time.time()-ts,2),'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
if __name__ == '__main__':
    main()
