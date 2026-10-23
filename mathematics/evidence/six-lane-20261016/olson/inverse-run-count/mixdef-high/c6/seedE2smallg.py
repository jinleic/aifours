#!/usr/bin/env python3
"""[F] Controls of proof-E2smallg.md: E2,Delta3,g in{1,2},p>=31, arbitrary run structure.
A constant table in (g,p mod4,d) chooses two ordinary mixed-single configurations; no finite-prime extrapolation.
"""
import random,json,time,resource
from math import ceil
GUARD="if __name__ == '__main__':\n    main()"
D={'__name__':'seedE2tip_lib'}
exec(compile(open('seedE2tip.py').read().replace(GUARD,''),'seedE2tip.py','exec'),D)
N=D['N'];makeword=D['D']['word'];build=D['ordinary_rz'];rnd=random.Random(200050)
TABLE={(1, 1): {-3: {'lo': -1, 'hi': -2, 'witnesses': [(0, 3, -1, -1), (-1, 4, -2, -2)]}, -2: {'lo': -1, 'hi': -1, 'witnesses': [(0, 1, -1, 0), (0, 3, -1, -1)]}, -1: {'lo': -1, 'hi': -1, 'witnesses': [(-1, 2, -1, 0), (-1, 4, -1, -1)]}, 0: {'lo': 0, 'hi': 0, 'witnesses': [(-1, 2, 0, 1), (-1, 4, 0, 0)]}, 1: {'lo': 1, 'hi': 0, 'witnesses': [(-1, 0, 0, 2), (-1, 4, 0, 0)]}, 2: {'lo': 2, 'hi': 1, 'witnesses': [(-1, 0, 1, 3), (-1, 4, 1, 1)]}, 3: {'lo': 3, 'hi': 2, 'witnesses': [(-2, 1, 2, 4), (-1, 2, 1, 2)]}}, (1, 3): {-3: {'lo': -2, 'hi': -2, 'witnesses': [(0, 2, -2, -1), (0, 4, -2, -2)]}, -2: {'lo': -1, 'hi': -1, 'witnesses': [(0, 2, -1, -1), (0, 2, -1, -1)]}, -1: {'lo': 0, 'hi': 0, 'witnesses': [(-1, 3, 0, 0), (-1, 3, 0, 0)]}, 0: {'lo': 0, 'hi': 0, 'witnesses': [(-1, 1, 0, 1), (-1, 3, 0, 0)]}, 1: {'lo': 1, 'hi': 1, 'witnesses': [(-1, 1, 1, 2), (-1, 3, 1, 1)]}, 2: {'lo': 2, 'hi': 1, 'witnesses': [(-1, 1, 1, 2), (-1, 3, 1, 1)]}, 3: {'lo': 3, 'hi': 2, 'witnesses': [(-1, 1, 2, 3), (-1, 3, 2, 2)]}}, (2, 1): {-3: {'lo': -2, 'hi': -2, 'witnesses': [(0, 3, -2, -1), (0, 5, -2, -2)]}, -2: {'lo': -1, 'hi': -1, 'witnesses': [(0, 3, -1, -1), (0, 3, -1, -1)]}, -1: {'lo': 0, 'hi': 0, 'witnesses': [(-1, 4, 0, 0), (-1, 4, 0, 0)]}, 0: {'lo': 0, 'hi': 0, 'witnesses': [(0, 1, 0, 1), (0, 3, 0, 0)]}, 1: {'lo': 1, 'hi': 1, 'witnesses': [(-1, 2, 1, 2), (-1, 4, 1, 1)]}, 2: {'lo': 1, 'hi': 1, 'witnesses': [(-1, 0, 1, 3), (-1, 4, 1, 1)]}, 3: {'lo': 2, 'hi': 1, 'witnesses': [(-1, 0, 2, 4), (0, 3, 1, 1)]}}, (2, 3): {-3: {'lo': -1, 'hi': -2, 'witnesses': [(0, 4, -1, -1), (-1, 5, -2, -2)]}, -2: {'lo': -1, 'hi': -1, 'witnesses': [(0, 2, -1, 0), (0, 4, -1, -1)]}, -1: {'lo': -1, 'hi': -1, 'witnesses': [(-1, 3, -1, 0), (-1, 5, -1, -1)]}, 0: {'lo': 0, 'hi': 0, 'witnesses': [(0, 0, 0, 2), (0, 2, 0, 0)]}, 1: {'lo': 0, 'hi': 0, 'witnesses': [(-1, 1, 0, 2), (-1, 5, 0, 0)]}, 2: {'lo': 1, 'hi': 1, 'witnesses': [(-1, 1, 1, 3), (-1, 5, 1, 1)]}, 3: {'lo': 2, 'hi': 2, 'witnesses': [(0, 0, 2, 3), (0, 2, 2, 2)]}}}
FD={-3:4,-2:2,-1:0,0:1,1:0,2:0,3:1}
def bounds(g,rho,d,t,y):
    a=(rho-3)//2
    L=min(rho-a-t+1,a+t+y-g,(y+rho-4-g)//2+1)
    U=max(a+t-1,y+rho-5-g-a-t,ceil((rho-g-1+y)/2)-1)
    LP=min(rho-a-t,a+t+y+d+1-g,(y+d+rho-4-g)//2+1)
    UP=max(a+t,y+d+rho-6-g-a-t,ceil((rho-g-1+y+d)/2)-1)
    return LP-U,UP-L

def main():
    tt=time.time();st={'constant_rows':0,'lower_only_certificate_reject':0,'classes':0,'target_types':0};pool=[]
    for (g,rho),row in TABLE.items():
        a=(rho-3)//2
        for d,v in row.items():
            raw=[]
            for t,y,sl,sh in v['witnesses']:
                assert bounds(g,rho,d,t,y)==(sl,sh)
                assert -2<=t<=0 and 0<=y<=5 and (a+t-y)%2==0
                assert 2*t<=g-3+FD[d]
                assert sl>=max(-8,d-g-5) and sh<=8 and sl<=sh
                raw.append((sl,sh))
            lo=max(d+1-g,max(vv[0] for vv in raw));hi=min(vv[1] for vv in raw)
            assert (lo,hi)==(v['lo'],v['hi'])
            assert lo>hi or (2*lo>=d-1 and 2*hi<=d+1)
            aa=max(d+1-g,raw[0][0]);bb=raw[0][1]
            if not (aa>bb or (2*aa>=d-1 and 2*bb<=d+1)):st['lower_only_certificate_reject']+=1
            st['constant_rows']+=1
    for p in range(31,402):
        if not D['prime'](p):continue
        for g in (1,2):
            rho=p%4;B=p-4-g;kap=p-4;A=p+g+1;k=2*p-5
            lam=lambda v,b:min(p-b+1,v+b-g,(v+B)//2+1)
            lc=lambda v,b:min(p-b+1,p-B+1-v+b,(A-v)//2+1)
            U=lambda v,b:p-lc(v,b)
            for d,v in TABLE[(g,rho)].items():
                for t,y,sl,sh in v['witnesses']:
                    m=(p-3)//2+t;i=(m-y)//2;j=(m+y)//2
                    assert i>=0 and j>=0 and 2*i<=B-7 and 2*m<=p+g-6+FD[d]
                    assert lam(y+d,m+1)-U(y,m)==sl and U(y+d,m+1)-lam(y,m)==sh
                    assert lam(d,1)-sh>-p and U(d,1)-sl<p
                st['target_types']+=1
            st['classes']+=1
            if p<=101:pool.append((p,g,B))
    print(json.dumps({'arithmetic':st}),flush=True)
    chosen=rnd.sample(pool,min(32,len(pool)))+[(31,1,26),(31,2,25),(37,1,32),(37,2,31)]
    cs={'classes':len(chosen),'words':0,'target_configurations':0,'target_intersections':0,'actual_empty':0}
    for p,g,B in chosen:
        k=2*p-5;kap=p-4;row=TABLE[(g,p%4)]
        for _ in range(3):
            W=makeword(p,k,kap,B);cs['words']+=1
            for target,d in enumerate(W.d):
                raw=[]
                for t,y,sl,sh in row[d]['witnesses']:
                    m=(p-3)//2+t;i=(m-y)//2;j=(m+y)//2
                    Q=build(W,target,i,j);a,b=N['check_word_type'](W,target,Q,y,m)
                    assert (a,b)==(sl,sh)
                    raw.append((max(W.single_lo[target],a),min(W.single_hi[target],b)));cs['target_configurations']+=1
                lo=max(a for a,b in raw);hi=min(b for a,b in raw)
                assert lo>hi or (2*lo>=d-1 and 2*hi<=d+1)
                if lo>hi:cs['actual_empty']+=1
                cs['target_intersections']+=1
    print(json.dumps({'constructive':cs}),flush=True)
    print(json.dumps({'seconds':round(time.time()-tt,2),'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
if __name__ == '__main__':
    main()
