#!/usr/bin/env python3
"""[F] Controls for proof-Ewide.md: uniform mixed-single seed family with excess.
E even>=2, B>=g+2E+3, Delta0=p-g-B-E/2>=E+5. No finite word/counterexample census.
All arithmetic tuples p<=101, all target weights d and y in the excess-coupled RZX hull: availability, four generic arcs, QS, no wrap.
Literal configurations in sampled classes/words are verified with independent c5 slow_lambda.
"""
import random,json,time,resource
GUARD="if __name__ == '__main__':\n    main()"
D={'__name__':'defect_prefix_lib'}
exec(compile(open('defect_prefix.py').read().replace(GUARD,''),'defect_prefix.py','exec'),D)
N=D['N'];Wg=D['Wg'];rnd=random.Random(193355)
def prime(p):return p>1 and all(p%q for q in range(2,int(p**.5)+1))
def tuples(P):
    for p in range(7,P+1):
        if not prime(p):continue
        for E in range(2,p-3,2):
            for g in range(1,p):
                low=g+2*E+3;high=p-g-E//2-(E+5)
                for B in range(low,high+1):yield p,E,g,B

def recipe(E,g,B):
    kap=g+B;m=(kap+1)//2;c=2 if (m-g-E)%2==0 else 3;y0=g+E+c
    return m,c,y0,(m-y0)//2,(m+y0)//2

def main():
    t=time.time();st={'classes':0,'target_types':0,'generic_arcs':0};pool=[]
    for p,E,g,B in tuples(101):
        kap=g+B;delta=p-g-E//2;Delta0=p-kap-E//2;k=p+kap-E//2
        m,c,y0,i,j=recipe(E,g,B)
        assert i>=0 and j>=0 and (m-y0)%2==0
        assert 2*i<=B-E-3 and 2*m<=k-B-3 and 2*m+2<k
        X=y0+2*m;Z=y0-2*m
        assert 2*g+B+E+2<=X<=2*p-B-E-3
        assert E+3-delta<=Z<=delta-2*B-2
        A=p+g+E//2
        lam=lambda y,b:min(p-b+1,y+b-g,(y+B)//2+1)
        lc=lambda y,b:min(p-b+1,A-kap-y+b,(A-y)//2+1)
        U=lambda y,b:p-lc(y,b)
        gen=lambda y,b:lam(y,b)==(y+B)//2+1 and lc(y,b)==(A-y)//2+1
        assert 2*g<=p and E<=2*(k-g-2*B)-1
        for d in range(-min(B,E+1),E+2):
            et=abs(d)-1 if d else 1;er=E-et
            for y in range(y0-er,y0+er+1):
                assert gen(y,m) and gen(y+d,m+1)
                sl=lam(y+d,m+1)-U(y,m);sh=U(y+d,m+1)-lam(y,m)
                assert 2*sl>=d-Delta0+2 and 2*sh<=d+Delta0-2
                assert lam(d,1)-sh>-p and U(d,1)-sl<p
                st['target_types']+=1;st['generic_arcs']+=4
        st['classes']+=1
        pool.append((p,E,g,B))
    print(json.dumps({'arithmetic':st}),flush=True)
    chosen=rnd.sample(pool,min(36,len(pool)))+[(p,2,1,p-9) for p in (17,29,41,61,97)]
    cs={'classes':len(chosen),'words':0,'configurations':0,'actual_empty':0}
    for p,E,g,B in chosen:
        kap=g+B;k=p+kap-E//2;m,c,y0,i,j=recipe(E,g,B)
        for z in range(3):
            W=D['word'](p,k,kap,B);assert W.E==E
            cs['words']+=1
            for t0,d in enumerate(W.d):
                path=[(t0+2+s)%k for s in range(k-3)]
                Q=N['rz'](path,W.a,W.b,i,j);y=sum(W.d[q] for q in Q)
                et=abs(d)-1 if d else 1
                assert y0-(E-et)<=y<=y0+(E-et)
                l,lc=N['arcs'](W,Q);lt,lct=N['arcs'](W,Q|{t0})
                assert l==(y+B)//2+1 and lc==(W.A-y)//2+1
                assert lt==(y+d+B)//2+1 and lct==(W.A-y-d)//2+1
                sl,sh=N['check_word_type'](W,t0,Q,y,m)
                if max(W.single_lo[t0],sl)>min(W.single_hi[t0],sh):cs['actual_empty']+=1
                cs['configurations']+=1
    print(json.dumps({'constructive':cs}),flush=True)
    # Boundary control: weakening Delta0>=E+5 by one is not claimed sound; find arithmetic type failures at Delta0=E+4.
    ctrl={'boundary_classes':0,'nongeneric_classes':0}
    for p in range(7,102):
        if not prime(p):continue
        for E in range(2,p-3,2):
            for g in range(1,p):
                B=p-g-E//2-E-4
                if B<g+2*E+3:continue
                m,c,y0,i,j=recipe(E,g,B);A=p+g+E//2;kap=g+B
                gen=lambda y,b:min(p-b+1,y+b-g,(y+B)//2+1)==(y+B)//2+1 and min(p-b+1,A-kap-y+b,(A-y)//2+1)==(A-y)//2+1
                bad=False
                for d in range(-min(B,E+1),E+2):
                    et=abs(d)-1 if d else 1;er=E-et
                    for y in range(y0-er,y0+er+1):
                        if not (gen(y,m) and gen(y+d,m+1)):bad=True
                ctrl['boundary_classes']+=1
                if bad:ctrl['nongeneric_classes']+=1
    print(json.dumps({'boundary_control':ctrl}),flush=True)
    print(json.dumps({'seconds':round(time.time()-t,2),'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
if __name__ == '__main__':
    main()
