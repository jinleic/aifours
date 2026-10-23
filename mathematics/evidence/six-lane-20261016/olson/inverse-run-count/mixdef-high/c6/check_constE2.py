#!/usr/bin/env python3
"""Strict standalone checker of the finite E2 constant certificate; authored by the producing worker, NOT an independent checker.
CLI: python3 [-O] -B check_constE2.py EXPECTED_SHA256 FILE
No worker modules imported; bytes read once, hashed, strict exact schema and full expected index universes.
Universal monotonic-extension lemmas are written in proof-E2layer.md; this checker verifies their finite arithmetic obligations.
"""
import hashlib,json,sys,math
class CertificateError(Exception):
    def __init__(self,reason,detail):self.reason=reason;self.detail=detail

def need(condition,reason,detail):
    if not condition:raise CertificateError(reason,detail)
def obj(pairs):
    out={}
    for k,v in pairs:
        need(k not in out,'SCHEMA','duplicate object key '+str(k));out[k]=v
    return out
def shape(v,keys):need(type(v) is dict and set(v)==set(keys),'SCHEMA','unexpected object fields')
def ints(v,keys):
    for k in keys:need(type(v[k]) is int,'SCHEMA','non-integer '+k)
def cdiv(a,b):return -((-a)//b)
FD={-3:4,-2:2,-1:0,0:1,1:0,2:0,3:1}
def arcs(p,g,B,D,y,m):
    A=p+g+1
    l=min(p-m+1,y+m-g,(y+B)//2+1)
    lc=min(p-m+1,p-B+1-y+m,(A-y)//2+1)
    return l,p-lc

def balanced_raw(D,h,d,t,u):
    L=min(-h+D+2-t,u+t,(u-h)//2+1)
    U=max(t-1,u-h-t-1,cdiv(u-h+D,2)-1)
    LT=min(-h+D+1-t,u+d+t+1,(u+d-h)//2+1)
    UT=max(t,u+d-h-t-2,cdiv(u+d-h+D,2)-1)
    return LT-U,UT-L

def sg_raw(D,g,rho,d,t,y):
    a=(rho-3)//2
    L=min(rho-a-t+1,a+t+y-g,(y+rho-D-1-g)//2+1)
    U=max(a+t-1,y+rho-D-2-g-a-t,cdiv(rho-g-1+y,2)-1)
    LT=min(rho-a-t,a+t+y+d+1-g,(y+d+rho-D-1-g)//2+1)
    UT=max(a+t,y+d+rho-D-3-g-a-t,cdiv(rho-g-1+y+d,2)-1)
    return LT-U,UT-L

def check(expected,path):
    raw=open(path,'rb').read();digest=hashlib.sha256(raw).hexdigest()
    need(len(expected)==64 and digest==expected,'HASH','unexpected certificate bytes')
    try:data=json.loads(raw,object_pairs_hook=obj)
    except CertificateError:raise
    except (ValueError,UnicodeError) as e:raise CertificateError('SCHEMA','invalid JSON') from e
    shape(data,('schema','scope','balanced','small_g'))
    need(type(data['schema']) is int and data['schema']==1,'SCHEMA','wrong schema version')
    shape(data['scope'],('E','p_min','delta_min','delta_max'));ints(data['scope'],data['scope'])
    need(data['scope']==dict(E=2,p_min=31,delta_min=4,delta_max=8),'SCHEMA','wrong scope')
    need(type(data['balanced']) is list and type(data['small_g']) is list,'SCHEMA','non-array rows')
    targetB={(D,h,d) for D in range(4,9) for h in range(D-4,17-D,2) for d in range(-3,4)}
    targetG={(D,g,rho,d) for D in range(4,9) for g in (1,2) for rho in (1,3) for d in range(-3,4)}
    seenB=set();seenG=set()
    # Full coverage is checked before arithmetic, so dropping a row has a precise intended failure.
    for r in data['balanced']:
        shape(r,('delta','h','d','witnesses','lo','hi'));ints(r,('delta','h','d','lo','hi'))
        key=(r['delta'],r['h'],r['d']);need(key not in seenB,'COVERAGE','duplicate balanced index');seenB.add(key)
    for r in data['small_g']:
        shape(r,('delta','g','rho','d','witnesses','lo','hi'));ints(r,('delta','g','rho','d','lo','hi'))
        key=(r['delta'],r['g'],r['rho'],r['d']);need(key not in seenG,'COVERAGE','duplicate small-g index');seenG.add(key)
    need(seenB==targetB,'COVERAGE','balanced index universe mismatch')
    need(seenG==targetG,'COVERAGE','small-g index universe mismatch')
    witnesses=0
    for r in data['balanced']:
        D,h,d=r['delta'],r['h'],r['d'];B=7;g=B+h;p=g+B+D+1;k=2*p-D-2
        need(type(r['witnesses']) is list and len(r['witnesses'])==2,'SCHEMA','balanced witness count')
        ends=[]
        for w in r['witnesses']:
            shape(w,('kind','t','u','lo','hi'));ints(w,('t','u','lo','hi'));kind=w['kind'];t,u=w['t'],w['u']
            need(kind in ('S','P'),'SCHEMA','unknown configuration kind')
            m,y=g+t,g+u
            need(m>=1 and 2*m+2<=k,'AVAILABILITY','balanced properness')
            if kind=='S':need(u==t and 2*m<=p+g-6+FD[d],'AVAILABILITY','balanced ordinary singles')
            else:
                need(u>=t and g+2*t-u>=0 and t+u<=D-8+2*FD[d],'AVAILABILITY','balanced ordinary packing')
            need(balanced_raw(D,h,d,t,u)==(w['lo'],w['hi']),'ALGEBRA','balanced endpoint identity')
            l,U=arcs(p,g,B,D,y,m);lt,Ut=arcs(p,g,B,D,y+d,m+1)
            need((lt-U,Ut-l)==(w['lo'],w['hi']),'ALGEBRA','balanced direct-arc identity')
            need(-8<=w['lo']<=w['hi']<=8,'RANGE','balanced raw interval')
            L1,U1=arcs(p,g,B,D,d,1)
            need(L1-w['hi']>-p and U1-w['lo']<p,'NO_WRAP','balanced boundary wrap')
            ends.append((w['lo'],w['hi']));witnesses+=1
        lo=max(a for a,b in ends);hi=min(b for a,b in ends)
        need((lo,hi)==(r['lo'],r['hi']),'ALGEBRA','balanced intersection identity')
        C=D//2
        need(lo>hi or -C<=lo<=hi<=C,'SEED','balanced final common box')
        # [-C,C] implies QS*: the weakest ceil target across all d is ceil((D+2)/2).
        need(C+1<=cdiv(D+2,2),'SEED','balanced weak seed target')
        for d1 in range(-3,4):
            for d2 in range(-3,4):
                for mm in (1,2):
                    lam,Um=arcs(p,g,B,D,d1+d2,mm);lc=p-Um
                    need(-2*C>=1-lc and 2*C<=p+lam-1,'PAIR','balanced P2 boundary')
        for dd in range(-3,4):
            ll,uu=arcs(p,g,B,D,dd,1)
            need(C-ll<=p-1,'PIN','balanced pin boundary')
    for r in data['small_g']:
        D,g,rho,d=r['delta'],r['g'],r['rho'],r['d'];p=33 if rho==1 else 31;B=p-D-1-g;k=2*p-D-2
        need(type(r['witnesses']) is list and len(r['witnesses'])==2,'SCHEMA','small-g witness count')
        ends=[]
        for w in r['witnesses']:
            shape(w,('t','y','lo','hi'));ints(w,('t','y','lo','hi'));t,y=w['t'],w['y'];m=(p-3)//2+t
            need((m-y)%2==0 and 0<=y<=m and m>=1 and 2*m+2<=k,'AVAILABILITY','small-g type parity/properness')
            need(m-y<=B-7 and 2*m<=p+g-6+FD[d],'AVAILABILITY','small-g ordinary counts')
            need(sg_raw(D,g,rho,d,t,y)==(w['lo'],w['hi']),'ALGEBRA','small-g endpoint identity')
            l,U=arcs(p,g,B,D,y,m);lt,Ut=arcs(p,g,B,D,y+d,m+1)
            need((lt-U,Ut-l)==(w['lo'],w['hi']),'ALGEBRA','small-g direct-arc identity')
            need(max(-12,d-D-g-2)<=w['lo']<=w['hi']<=12,'RANGE','small-g raw interval')
            L1,U1=arcs(p,g,B,D,d,1)
            need(L1-w['hi']>-p and U1-w['lo']<p,'NO_WRAP','small-g boundary wrap')
            ends.append((w['lo'],w['hi']));witnesses+=1
        lo=max(d+1-g,max(a for a,b in ends));hi=min(b for a,b in ends)
        need((lo,hi)==(r['lo'],r['hi']),'ALGEBRA','small-g intersection identity')
        need(lo>hi or (2*lo>=d-D+2 and 2*hi<=d+D-2),'SEED','small-g quality seed')
    return {'RESULT':'VALID','sha256':digest,'balanced_rows':len(seenB),'small_g_rows':len(seenG),'witnesses':witnesses}

def main():
    if len(sys.argv)!=3:
        print(json.dumps({'RESULT':'INVALID','error':'USAGE'}));return 2
    try:result=check(sys.argv[1],sys.argv[2])
    except CertificateError as e:
        print(json.dumps({'RESULT':'INVALID','error':e.reason,'detail':e.detail}));return 2
    print(json.dumps(result,sort_keys=True));return 0
if __name__=='__main__':
    sys.exit(main())
