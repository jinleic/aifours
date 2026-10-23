#!/usr/bin/env python3
"""[F] Literal construction smoke for the E2-layer constant certificate and the two generic extreme constructions.
All D=4..8, p>=31; independent c5 slow_lambda arcs. This is not a model-independent/parent checker and not a word-avoider census.
"""
import random,json,time,resource
GUARD="if __name__ == '__main__':\n    main()"
P={'__name__':'seedE2pairtip_lib'}
exec(compile(open('seedE2pairtip.py').read().replace(GUARD,''),'seedE2pairtip.py','exec'),P)
R={'__name__':'seedE2tip_lib'}
exec(compile(open('seedE2tip.py').read().replace(GUARD,''),'seedE2tip.py','exec'),R)
N=P['N'];makeword=P['D']['word'];pairbuild=P['config'];rzbuild=R['ordinary_rz'];rnd=random.Random(201103)
cert=json.loads(open('const-e2/315-table.json').read())
BT={(r['delta'],r['h'],r['d']):r for r in cert['balanced']}
GT={(r['delta'],r['g'],r['rho'],r['d']):r for r in cert['small_g']}
def prime(p):return p>1 and all(p%q for q in range(2,int(p**.5)+1))
def main():
    tt=time.time();st={};jobs=[]
    for D in range(4,9):
        for typ in ('B','G','R','P'):
            pool=[]
            for p in range(31,102):
                if not prime(p):continue
                for g in range(1,p-D-1):
                    B=p-D-1-g;h=g-B
                    if typ=='G' and g in(1,2):pool.append((p,D,g,B,typ))
                    if g<3:continue
                    if typ=='R' and h<=D-6:pool.append((p,D,g,B,typ))
                    elif typ=='P' and h>=18-D:pool.append((p,D,g,B,typ))
                    elif typ=='B' and D-4<=h<=16-D and B>=7:pool.append((p,D,g,B,typ))
            jobs+=rnd.sample(pool,min(4,len(pool)))
    for p,D,g,B,typ in jobs:
        kk=2*p-D-2;kap=p-D-1
        for _ in range(2):
            W=makeword(p,kk,kap,B)
            st[typ+'_words']=st.get(typ+'_words',0)+1
            for target,d in enumerate(W.d):
                bounds=[]
                if typ=='G':
                    row=GT[(D,g,p%4,d)]
                    for w in row['witnesses']:
                        m=(p-3)//2+w['t'];y=w['y'];i=(m-y)//2;j=(m+y)//2
                        Q=rzbuild(W,target,i,j);a,b=N['check_word_type'](W,target,Q,y,m)
                        if (a,b)!=(w['lo'],w['hi']):raise RuntimeError('small-g actual interval mismatch')
                        bounds.append((max(W.single_lo[target],a),min(W.single_hi[target],b)))
                elif typ=='B':
                    row=BT[(D,g-B,d)]
                    for w in row['witnesses']:
                        m=g+w['t'];y=g+w['u']
                        if w['kind']=='S':j1,j2=m,0
                        else:j1,j2=g+2*w['t']-w['u'],w['u']-w['t']
                        Q=pairbuild(W,target,j1,j2);a,b=N['check_word_type'](W,target,Q,y,m)
                        if (a,b)!=(w['lo'],w['hi']):raise RuntimeError('balanced actual interval mismatch')
                        bounds.append((max(W.single_lo[target],a),min(W.single_hi[target],b)))
                else:
                    m=(p-3)//2
                    if typ=='R':
                        r=m-g;c=2 if r%2==0 else 3;y=g+c;i=(m-y)//2;j=(m+y)//2
                        Q=rzbuild(W,target,i,j)
                    else:
                        y=g+2;j1=B+D-4;j2=(g-B-D+6)//2
                        Q=pairbuild(W,target,j1,j2)
                    a,b=N['check_word_type'](W,target,Q,y,m)
                    la,lc=N['arcs'](W,Q);lt,lct=N['arcs'](W,Q|{target})
                    if (la,lc,lt,lct)!=((y+B)//2+1,(W.A-y)//2+1,(y+d+B)//2+1,(W.A-y-d)//2+1):raise RuntimeError('extreme genericity')
                    bounds.append((max(W.single_lo[target],a),min(W.single_hi[target],b)))
                lo=max(a for a,b in bounds);hi=min(b for a,b in bounds)
                if lo>hi:st[typ+'_empty']=st.get(typ+'_empty',0)+1
                elif typ=='B':
                    C=D//2
                    if not -C<=lo<=hi<=C:raise RuntimeError('balanced seed box')
                elif not (2*lo>=d-D+2 and 2*hi<=d+D-2):raise RuntimeError('quality interval')
                st[typ+'_targets']=st.get(typ+'_targets',0)+1
                st[typ+'_configs']=st.get(typ+'_configs',0)+len(bounds)
    print(json.dumps({'jobs':len(jobs),'outcomes':st}),flush=True)
    print(json.dumps({'seconds':round(time.time()-tt,2),'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
if __name__ == '__main__':
    main()
