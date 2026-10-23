#!/usr/bin/env python3
"""seedXstar3.py -- exact-integer review revision of the class criterion X* (proof-SEEDGstar-r1.md).
Usage: python3 -B seedXstar3.py MODE PMAX [detail]
MODE0 real QS*; MODE1 QS; MODE2 widen seed ranges by1 (mutation only); MODE3 tighten QS* by1 on both sides (new sensitivity control).
Canonical seed intervals make PIN automatic in real modes0/1/3. MODE2 retains the old pin check solely as a mutation diagnostic.
Every exec'ed source's SHA is printed in the header; optional per-class records report first failing profile/weight/pair/stage.
"""
import sys,time,json,hashlib
SRC_BYTES=open('seedX3.py','rb').read();SRC=SRC_BYTES.decode()
GUARD="if __name__ == '__main__':\n    main()"
if SRC.count(GUARD)!=1:raise RuntimeError('source guard mismatch')
NS={'__name__':'seedX3lib'}
exec(compile(SRC.replace(GUARD,''),'seedX3.py','exec'),NS)
cdiv=NS['cdiv']
def bounds(p,k,kappa,B,d,mode):
    R=2*p-k+2*kappa;E=R-k;D0=2*p-R
    if mode==1:return cdiv(d-D0,2)+1,(d+D0)//2-1
    mn,mx=min(d,0),max(d,0)
    A2=(2*D0+2*E+4,2*D0+E+2-2*mn,D0+E+4,2*D0+E-2*mn,2*D0+2*E-2*d+2,
        D0+E-d-mn+3,D0+E+3-2*d+mx,R-d+2)
    B2=(2*D0+2*E+4,2*D0+E+2*mx,D0+E+4,2*D0+E+2*mx+2,2*D0+2*E+2*d+2,
        D0+E+mx+d+3,D0+E+3+2*d-mn,R+d+2)
    lo,hi=1-(min(A2)+1)//2,(min(B2)+1)//2-1
    return (lo+1,hi-1) if mode==3 else (lo,hi)

def class_report(p,k,kappa,B,mode):
    R=2*p-k+2*kappa;E=R-k;g=kappa-B;A=R-B
    lam=lambda y,m:min(p-m+1,y+m-g,(y+B)//2+1)
    lamc=lambda y,m:min(p-m+1,A-kappa-y+m,(A-y)//2+1)
    profiles=[(p+g,p+g,1,1,False)] if E==0 else NS['profiles'](p,k,kappa,B)
    if not profiles:return {'verdict':'no-profile','stage':'profile-enumeration'}
    widen=1 if mode==2 else 0;cache={};ex=lambda d:abs(d)-1 if d else 1
    for n1,nal,aa,bb,hp in profiles:
        pi=[n1,nal,aa,bb,hp]
        weights=list(range(1,aa+1))+list(range(-bb,0))+([0] if hp else [])
        guaranteed=[aa]+([-bb] if bb else [])+([0] if hp else [])
        live={};gempty=False
        for d in weights:
            key=(n1,nal,d)
            if key not in cache:cache[key]=NS['exact_seed'](p,k,kappa,B,n1,nal,d,('S1','P1','SA','PA'))
            s=cache[key]
            if s is None:
                if d in guaranteed:gempty=True
            else:live[d]=(s[0]-widen,s[1]+widen)
        if gempty:continue
        for d,(a,b) in live.items():
            needlo,needhi=bounds(p,k,kappa,B,d,mode)
            if a<needlo or b>needhi:
                return {'verdict':'fail','stage':'QS' if mode==1 else 'QS*','profile':pi,'weight':d,'seed':[a,b],'required':[needlo,needhi]}
        for d1,(a1,b1) in live.items():
            for d2,(a2,b2) in live.items():
                if ex(d1)+ex(d2)>E:continue
                for m in(1,2):
                    lower=1-lamc(d1+d2,m);upper=p+lam(d1+d2,m)-1
                    if a1+a2<lower or b1+b2>upper:
                        return {'verdict':'fail','stage':'P2','profile':pi,'weights':[d1,d2],'blocks':m,'sum_range':[a1+a2,b1+b2],'required':[lower,upper]}
        if mode==2:
            for d,(a,b) in live.items():
                if b-lam(d,1)>p-1:
                    return {'verdict':'fail','stage':'PIN-mutation-only','profile':pi,'weight':d}
    cplus=E<=4 or (2*g<=p and E<=2*(k-g-2*B)-1)
    return {'verdict':'pass' if cplus else 'pass-noC+','stage':'all-profile-seed-tests','profiles_checked':len(profiles)}

def class_pass(p,k,kappa,B,mode):return class_report(p,k,kappa,B,mode)['verdict']
def main():
    mode=int(sys.argv[1]);PMAX=int(sys.argv[2]);detail=len(sys.argv)>3 and sys.argv[3]=='detail'
    manifest=NS['source_manifest']()
    manifest['seedX3.py']=hashlib.sha256(SRC_BYTES).hexdigest()
    manifest['seedXstar3.py']=hashlib.sha256(open('seedXstar3.py','rb').read()).hexdigest()
    print(json.dumps({'source_sha256':manifest}),flush=True)
    mapsrc=open('map6.py').read()
    if hashlib.sha256(mapsrc.encode()).hexdigest()!=manifest['map6.py']:raise RuntimeError('map source changed before exec')
    M={'__name__':'map6lib'};exec(compile(mapsrc,'map6.py','exec'),M)
    t0=time.time();print('== seedXstar3.py MODE=%d PMAX=%d start %s'%(mode,PMAX,time.strftime('%Y-%m-%dT%H:%M:%S')),flush=True)
    for p in range(11,PMAX+1):
        if not NS['isprime'](p):continue
        counts={};failstages={}
        for k,kappa,B in NS['classes'](p):
            lab=M['classify'](p,k,kappa,B);r=class_report(p,k,kappa,B,mode)
            if detail:print(json.dumps({'class':[p,k,kappa,B],'label':lab,**r}),flush=True)
            key=lab+':'+r['verdict'];counts[key]=counts.get(key,0)+1
            if r['verdict']=='fail':failstages[r['stage']]=failstages.get(r['stage'],0)+1
        print(json.dumps({'p':p,'counts':dict(sorted(counts.items())),'failure_stages':failstages,'t':round(time.time()-t0,1)}),flush=True)
    print('== end %.1f s'%(time.time()-t0),flush=True)
if __name__ == '__main__':
    main()
