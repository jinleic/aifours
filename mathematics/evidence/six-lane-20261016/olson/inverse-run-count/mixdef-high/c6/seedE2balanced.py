#!/usr/bin/env python3
"""[F] Controls for proof-E2balanced.md. Constant-offset table is a written algebraic certificate valid for every B>=7.
The arithmetic loops are controls, not a finite-prime extrapolation. Literal-word constructions use ordinary aligned runs only.
"""
import random,json,time,resource
from math import ceil
GUARD="if __name__ == '__main__':\n    main()"
D={'__name__':'seedE2pairtip_lib'}
exec(compile(open('seedE2pairtip.py').read().replace(GUARD,''),'seedE2pairtip.py','exec'),D)
N=D['N'];makeword=D['D']['word'];build=D['config'];rnd=random.Random(195619)
TABLE={-1: {-3: {'lo': -1, 'hi': -2, 'witnesses': [('P', 1, 2, -1, -1), ('P', 0, 3, -2, -2)]}, -2: {'lo': -1, 'hi': -1, 'witnesses': [('S', 1, 1, -1, -1), ('S', 1, 1, -1, -1)]}, -1: {'lo': 0, 'hi': -1, 'witnesses': [('S', 2, 2, 0, 0), ('S', 1, 1, -1, -1)]}, 0: {'lo': 0, 'hi': 0, 'witnesses': [('S', 0, 0, 0, 1), ('S', 1, 1, 0, 0)]}, 1: {'lo': 1, 'hi': 0, 'witnesses': [('S', 0, 0, 1, 2), ('S', 1, 1, 0, 0)]}, 2: {'lo': 1, 'hi': 1, 'witnesses': [('S', 0, 0, 1, 2), ('S', 1, 1, 1, 1)]}, 3: {'lo': 2, 'hi': 1, 'witnesses': [('S', 0, 0, 2, 3), ('S', 1, 1, 1, 1)]}}, 1: {-3: {'lo': -1, 'hi': -2, 'witnesses': [('P', 0, 2, -1, -1), ('P', 0, 3, -2, -2)]}, -2: {'lo': -1, 'hi': 0, 'witnesses': [('S', 0, 0, -1, 0), ('S', 0, 0, -1, 0)]}, -1: {'lo': 0, 'hi': 0, 'witnesses': [('S', 0, 0, 0, 0), ('S', 0, 0, 0, 0)]}, 0: {'lo': 0, 'hi': 0, 'witnesses': [('S', 0, 0, 0, 0), ('S', 0, 0, 0, 0)]}, 1: {'lo': 1, 'hi': 0, 'witnesses': [('S', 0, 0, 1, 1), ('S', 1, 1, 0, 0)]}, 2: {'lo': 1, 'hi': 1, 'witnesses': [('S', 0, 0, 1, 1), ('S', 0, 0, 1, 1)]}, 3: {'lo': 2, 'hi': 1, 'witnesses': [('S', 0, 0, 2, 2), ('S', 1, 1, 1, 1)]}}, 3: {-3: {'lo': -1, 'hi': -2, 'witnesses': [('S', 0, 0, -1, 1), ('P', -1, 3, -2, -2)]}, -2: {'lo': -1, 'hi': 0, 'witnesses': [('S', 0, 0, -1, 1), ('P', -1, 0, -1, 0)]}, -1: {'lo': 0, 'hi': 1, 'witnesses': [('S', 0, 0, 0, 1), ('S', 0, 0, 0, 1)]}, 0: {'lo': 0, 'hi': 1, 'witnesses': [('S', 0, 0, 0, 1), ('S', 0, 0, 0, 1)]}, 1: {'lo': 1, 'hi': 1, 'witnesses': [('S', 0, 0, 1, 1), ('S', 0, 0, 1, 1)]}, 2: {'lo': 1, 'hi': 1, 'witnesses': [('S', 0, 0, 1, 1), ('S', 0, 0, 1, 1)]}, 3: {'lo': 2, 'hi': 1, 'witnesses': [('S', 0, 0, 2, 2), ('S', 1, 1, 0, 1)]}}, 5: {-3: {'lo': -1, 'hi': -2, 'witnesses': [('P', -1, 0, -1, 1), ('P', -2, 3, -2, -2)]}, -2: {'lo': -1, 'hi': -1, 'witnesses': [('P', -1, 0, -1, 1), ('P', -2, 1, -1, -1)]}, -1: {'lo': -1, 'hi': 1, 'witnesses': [('S', 0, 0, -1, 2), ('S', -1, -1, -1, 1)]}, 0: {'lo': 0, 'hi': 1, 'witnesses': [('S', -1, -1, 0, 1), ('S', -1, -1, 0, 1)]}, 1: {'lo': 1, 'hi': 1, 'witnesses': [('S', -2, -2, 1, 2), ('S', -1, -1, 0, 1)]}, 2: {'lo': 1, 'hi': 1, 'witnesses': [('S', -1, -1, 1, 1), ('S', -1, -1, 1, 1)]}, 3: {'lo': 2, 'hi': 1, 'witnesses': [('P', -3, 0, 2, 3), ('S', -1, -1, 1, 1)]}}, 7: {-3: {'lo': -1, 'hi': -2, 'witnesses': [('P', -2, 0, -1, 1), ('P', -3, 3, -2, -2)]}, -2: {'lo': -1, 'hi': -1, 'witnesses': [('P', -2, 0, -1, 1), ('P', -3, 1, -1, -1)]}, -1: {'lo': -1, 'hi': 1, 'witnesses': [('S', -2, -2, -1, 2), ('P', -4, -1, -2, 1)]}, 0: {'lo': 0, 'hi': 0, 'witnesses': [('P', -3, 0, 0, 0), ('P', -3, 0, 0, 0)]}, 1: {'lo': 1, 'hi': 2, 'witnesses': [('P', -3, -2, 1, 2), ('S', -1, -1, -1, 2)]}, 2: {'lo': 1, 'hi': 2, 'witnesses': [('P', -3, -2, 1, 2), ('S', -1, -1, 0, 2)]}, 3: {'lo': 2, 'hi': 1, 'witnesses': [('P', -3, 0, 2, 2), ('P', -2, -1, 1, 1)]}}, 9: {-3: {'lo': -1, 'hi': -2, 'witnesses': [('P', -3, 0, -1, 1), ('P', -4, 3, -2, -2)]}, -2: {'lo': -1, 'hi': -1, 'witnesses': [('P', -3, 0, -1, 1), ('P', -4, 1, -1, -1)]}, -1: {'lo': -1, 'hi': 1, 'witnesses': [('P', -5, 0, -1, 1), ('P', -5, 0, -1, 1)]}, 0: {'lo': 0, 'hi': 0, 'witnesses': [('P', -3, 0, 0, 1), ('P', -4, 0, 0, 0)]}, 1: {'lo': 1, 'hi': 1, 'witnesses': [('P', -5, 0, 1, 2), ('P', -4, -1, 0, 1)]}, 2: {'lo': 1, 'hi': 2, 'witnesses': [('P', -5, 0, 1, 2), ('P', -5, 0, 1, 2)]}, 3: {'lo': 2, 'hi': 1, 'witnesses': [('P', -3, 0, 2, 2), ('P', -3, -1, 1, 1)]}}, 11: {-3: {'lo': -1, 'hi': -2, 'witnesses': [('P', -4, 0, -1, 1), ('P', -5, 3, -2, -2)]}, -2: {'lo': -1, 'hi': -1, 'witnesses': [('P', -4, 0, -1, 1), ('P', -5, 1, -1, -1)]}, -1: {'lo': 0, 'hi': 0, 'witnesses': [('P', -5, 0, 0, 0), ('P', -5, 0, 0, 0)]}, 0: {'lo': 0, 'hi': 0, 'witnesses': [('P', -4, 0, 0, 1), ('P', -5, 0, 0, 0)]}, 1: {'lo': 1, 'hi': 1, 'witnesses': [('P', -5, 0, 1, 1), ('P', -5, 0, 1, 1)]}, 2: {'lo': 1, 'hi': 1, 'witnesses': [('P', -5, 0, 1, 1), ('P', -5, 0, 1, 1)]}, 3: {'lo': 2, 'hi': 1, 'witnesses': [('P', -4, 0, 2, 2), ('P', -4, -1, 1, 1)]}}, 13: {-3: {'lo': -1, 'hi': -2, 'witnesses': [('P', -5, 0, -1, 1), ('P', -6, 3, -2, -2)]}, -2: {'lo': -1, 'hi': -1, 'witnesses': [('P', -5, 0, -1, 1), ('P', -6, 1, -1, -1)]}, -1: {'lo': 0, 'hi': -1, 'witnesses': [('P', -5, 0, 0, 1), ('P', -6, 1, -1, -1)]}, 0: {'lo': 0, 'hi': 0, 'witnesses': [('P', -5, 0, 0, 1), ('P', -6, 0, 0, 0)]}, 1: {'lo': 1, 'hi': 0, 'witnesses': [('P', -5, 0, 1, 1), ('P', -6, 1, 0, 0)]}, 2: {'lo': 1, 'hi': 1, 'witnesses': [('P', -5, 0, 1, 1), ('P', -5, 0, 1, 1)]}, 3: {'lo': 2, 'hi': 1, 'witnesses': [('P', -5, 0, 2, 2), ('P', -4, 1, 0, 1)]}}}
FD={-3:4,-2:2,-1:0,0:1,1:0,2:0,3:1}
def bounds(h,d,t,u):
    L=min(-h+5-t,u+t,(u-h)//2+1)
    U=max(t-1,u-h-t-1,ceil((u-h+3)/2)-1)
    LP=min(-h+4-t,u+d+t+1,(u+d-h)//2+1)
    UP=max(t,u+d-h-t-2,ceil((u+d-h+3)/2)-1)
    return LP-U,UP-L

def main():
    start=time.time();st={'constant_rows':0,'discarding_lower_configuration_reject':0,'conditional_availability_rows':0,'classes':0,'target_types':0};pool=[]
    for h,row in TABLE.items():
        for d,v in row.items():
            raw=[]
            for kind,t,u,sl,sh in v['witnesses']:
                assert bounds(h,d,t,u)==(sl,sh) and -8<=sl<=sh<=8
                assert 7+h+t>=1 and t<=7
                if kind=='S':assert u==t and 2*t<=5+FD[d]
                else:
                    assert u>=t and 7+h+2*t-u>=0 and t+u<=-5+2*FD[d]
                    if t+u>-5:st['conditional_availability_rows']+=1
                raw.append((sl,sh))
            assert (max(a for a,b in raw),min(b for a,b in raw))==(v['lo'],v['hi'])
            assert v['lo']>v['hi'] or (-1<=v['lo']<=v['hi']<=2)
            a,b=raw[1]
            if not (a>b or -1<=a<=b<=2):st['discarding_lower_configuration_reject']+=1
            st['constant_rows']+=1
    for B in range(7,121):
        for h,row in TABLE.items():
            g=B+h;p=g+B+4;kap=p-4;k=2*p-5
            if not D['prime'](p):continue
            lam=lambda y,m:min(p-m+1,y+m-g,(y+B)//2+1)
            lc=lambda y,m:min(p-m+1,p-B+1-y+m,(p+g+1-y)//2+1)
            U=lambda y,m:p-lc(y,m)
            for d,v in row.items():
                for kind,t,u,sl,sh in v['witnesses']:
                    m=g+t;y=g+u
                    assert lam(y+d,m+1)-U(y,m)==sl and U(y+d,m+1)-lam(y,m)==sh
                    assert lam(d,1)-sh>-p and U(d,1)-sl<p
                st['target_types']+=1
            # P2/PIN controls with the deliberately wider common nonempty box [-1,2].
            for d1 in range(-3,4):
                for d2 in range(-3,4):
                    for m in (1,2):assert -2>=1-lc(d1+d2,m) and 4<=p+lam(d1+d2,m)-1
            assert all(2-lam(d,1)<=p-1 for d in range(-3,4))
            st['classes']+=1;pool.append((p,g,B,h))
    print(json.dumps({'arithmetic':st}),flush=True)
    chosen=rnd.sample(pool,min(48,len(pool)))
    cs={'classes':len(chosen),'words':0,'target_configurations':0,'target_intersections':0,'actual_empty_intersection':0}
    for p,g,B,h in chosen:
        kap=p-4;k=2*p-5
        for _ in range(3):
            W=makeword(p,k,kap,B);cs['words']+=1
            n1=sum(a==1 and b==0 for a,b in zip(W.a,W.b))
            for target,d in enumerate(W.d):
                assert n1>=p+g-3+FD[d]
                v=TABLE[h][d];raw=[]
                for kind,t,u,sl,sh in v['witnesses']:
                    m=g+t;y=g+u
                    j1=m if kind=='S' else g+2*t-u;j2=0 if kind=='S' else u-t
                    Q=build(W,target,j1,j2)
                    a,b=N['check_word_type'](W,target,Q,y,m)
                    assert (a,b)==(sl,sh);raw.append((max(W.single_lo[target],a),min(W.single_hi[target],b)))
                    cs['target_configurations']+=1
                lo=max(a for a,b in raw);hi=min(b for a,b in raw)
                assert lo>hi or -1<=lo<=hi<=2
                if lo>hi:cs['actual_empty_intersection']+=1
                cs['target_intersections']+=1
    print(json.dumps({'constructive':cs}),flush=True)
    print(json.dumps({'seconds':round(time.time()-start,2),'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
if __name__ == '__main__':
    main()
