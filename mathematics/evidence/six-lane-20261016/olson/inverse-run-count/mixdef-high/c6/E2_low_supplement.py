#!/usr/bin/env python3
"""[F] Eight finite low-prime E2 classes not accepted by the base X* test. Verify actual ordinary mixed-single recipes directly;
NO application of a p>=31 theorem at a smaller prime. This is not a raw ordered-product or avoider search.
"""
import json,hashlib,random,subprocess,time,resource
SOURCE=('E2_low_supplement.py','seedE2tip.py','defect_prefix.py','replayLB.py','seedLB3.py','seedLB.py','seedXstar2.py','seedX2.py','../c5/cplus_replay.py')
print(json.dumps({'host_time':subprocess.check_output(['date','+%Y-%m-%dT%H:%M:%S%z'],text=True).strip(),
 'source_sha256':{f:hashlib.sha256(open(f,'rb').read()).hexdigest() for f in SOURCE},
 'low_receipt_sha256':hashlib.sha256(open('out/E2_small_primes.txt','rb').read()).hexdigest()}),flush=True)
G={'__name__':'seedE2tip_lib'};guard="if __name__ == '__main__':\n    main()"
exec(compile(open('seedE2tip.py').read().replace(guard,''),'seedE2tip.py','exec'),G)
N=G['N'];makeword=G['D']['word'];build=G['ordinary_rz'];rnd=random.Random(204944)
D3={(1, 1): {-3: {'lo': -1, 'hi': -2, 'witnesses': [(0, 3, -1, -1), (-1, 4, -2, -2)]}, -2: {'lo': -1, 'hi': -1, 'witnesses': [(0, 1, -1, 0), (0, 3, -1, -1)]}, -1: {'lo': -1, 'hi': -1, 'witnesses': [(-1, 2, -1, 0), (-1, 4, -1, -1)]}, 0: {'lo': 0, 'hi': 0, 'witnesses': [(-1, 2, 0, 1), (-1, 4, 0, 0)]}, 1: {'lo': 1, 'hi': 0, 'witnesses': [(-1, 0, 0, 2), (-1, 4, 0, 0)]}, 2: {'lo': 2, 'hi': 1, 'witnesses': [(-1, 0, 1, 3), (-1, 4, 1, 1)]}, 3: {'lo': 3, 'hi': 2, 'witnesses': [(-2, 1, 2, 4), (-1, 2, 1, 2)]}}, (1, 3): {-3: {'lo': -2, 'hi': -2, 'witnesses': [(0, 2, -2, -1), (0, 4, -2, -2)]}, -2: {'lo': -1, 'hi': -1, 'witnesses': [(0, 2, -1, -1), (0, 2, -1, -1)]}, -1: {'lo': 0, 'hi': 0, 'witnesses': [(-1, 3, 0, 0), (-1, 3, 0, 0)]}, 0: {'lo': 0, 'hi': 0, 'witnesses': [(-1, 1, 0, 1), (-1, 3, 0, 0)]}, 1: {'lo': 1, 'hi': 1, 'witnesses': [(-1, 1, 1, 2), (-1, 3, 1, 1)]}, 2: {'lo': 2, 'hi': 1, 'witnesses': [(-1, 1, 1, 2), (-1, 3, 1, 1)]}, 3: {'lo': 3, 'hi': 2, 'witnesses': [(-1, 1, 2, 3), (-1, 3, 2, 2)]}}, (2, 1): {-3: {'lo': -2, 'hi': -2, 'witnesses': [(0, 3, -2, -1), (0, 5, -2, -2)]}, -2: {'lo': -1, 'hi': -1, 'witnesses': [(0, 3, -1, -1), (0, 3, -1, -1)]}, -1: {'lo': 0, 'hi': 0, 'witnesses': [(-1, 4, 0, 0), (-1, 4, 0, 0)]}, 0: {'lo': 0, 'hi': 0, 'witnesses': [(0, 1, 0, 1), (0, 3, 0, 0)]}, 1: {'lo': 1, 'hi': 1, 'witnesses': [(-1, 2, 1, 2), (-1, 4, 1, 1)]}, 2: {'lo': 1, 'hi': 1, 'witnesses': [(-1, 0, 1, 3), (-1, 4, 1, 1)]}, 3: {'lo': 2, 'hi': 1, 'witnesses': [(-1, 0, 2, 4), (0, 3, 1, 1)]}}, (2, 3): {-3: {'lo': -1, 'hi': -2, 'witnesses': [(0, 4, -1, -1), (-1, 5, -2, -2)]}, -2: {'lo': -1, 'hi': -1, 'witnesses': [(0, 2, -1, 0), (0, 4, -1, -1)]}, -1: {'lo': -1, 'hi': -1, 'witnesses': [(-1, 3, -1, 0), (-1, 5, -1, -1)]}, 0: {'lo': 0, 'hi': 0, 'witnesses': [(0, 0, 0, 2), (0, 2, 0, 0)]}, 1: {'lo': 0, 'hi': 0, 'witnesses': [(-1, 1, 0, 2), (-1, 5, 0, 0)]}, 2: {'lo': 1, 'hi': 1, 'witnesses': [(-1, 1, 1, 3), (-1, 5, 1, 1)]}, 3: {'lo': 2, 'hi': 2, 'witnesses': [(0, 0, 2, 3), (0, 2, 2, 2)]}}}
raw=open('const-e2/315-table.json','rb').read()
if hashlib.sha256(raw).hexdigest()!='cba0206dd7db29b7b840eca3aa35b77720e6591bf5ab75ca558292bb67f22b86':raise RuntimeError('constant certificate hash mismatch')
SC={(r['delta'],r['g'],r['rho'],r['d']):r for r in json.loads(raw)['small_g']}
rows=[json.loads(s) for s in open('out/E2_small_primes.txt') if s.startswith('{')]
base=rows[-1];failures=base['nonpassing'];passed=sum(c.get('pass',0) for c in base['counts'].values())
if passed!=706 or len(failures)!=8:raise RuntimeError('low-prime base receipt shape changed')
FD={-3:4,-2:2,-1:0,0:1,1:0,2:0,3:1};stats={'base_pass':passed,'supplemented_classes':0,'words':0,'configurations':0,'empty_intersections':0,'ordinary_filter_mutation_mass_reject':0}
t=time.time()
for p,k,kap,B,old in failures:
    D=p-kap-1;g=kap-B
    if D not in(3,4) or 2*p-2*k+2*kap!=2:raise RuntimeError('unexpected finite supplement class')
    lam=lambda v,b:min(p-b+1,v+b-g,(v+B)//2+1)
    lc=lambda v,b:min(p-b+1,p-B+1-v+b,(p+g+1-v)//2+1)
    U=lambda v,b:p-lc(v,b)
    chosen={}
    for d in range(-3,4):
        if g>=3:
            m=(p-3)//2;r=m-g;c=2 if r%2==0 else 3;y=g+c
            specs=[(m,y)]
        elif D==3:specs=[((p-3)//2+w[0],w[1]) for w in D3[(g,p%4)][d]['witnesses']]
        else:specs=[((p-3)//2+w['t'],w['y']) for w in SC[(D,g,p%4,d)]['witnesses']]
        rawboxes=[];configs=[]
        for m,y in specs:
            if (m-y)%2 or y>m or m-y>B-7 or 2*m>p+g-6+FD[d] or m<1 or 2*m+2>k:raise RuntimeError('finite ordinary availability')
            sl=lam(y+d,m+1)-U(y,m);sh=U(y+d,m+1)-lam(y,m)
            if not(lam(d,1)-sh>-p and U(d,1)-sl<p):raise RuntimeError('finite no-wrap')
            rawboxes.append((max(lam(d,1),sl),min(U(d,1),sh)));configs.append((m,y,sl,sh))
        lo=max(a for a,b in rawboxes);hi=min(b for a,b in rawboxes)
        if not(lo>hi or (2*lo>=d-D+2 and 2*hi<=d+D-2)):raise RuntimeError(('finite quality fails',p,k,kap,B,d,lo,hi))
        chosen[d]=configs
    print(json.dumps({'class':[p,k,kap,B],'recipe_verified_for_weights':list(range(-3,4))}),flush=True)
    for _ in range(4):
        W=makeword(p,k,kap,B);stats['words']+=1
        for target,d in enumerate(W.d):
            boxes=[]
            for m,y,sl,sh in chosen[d]:
                i=(m-y)//2;j=(m+y)//2;Q=build(W,target,i,j)
                a,b=N['check_word_type'](W,target,Q,y,m)
                if(a,b)!=(sl,sh):raise RuntimeError('finite actual interval mismatch')
                boxes.append((max(W.single_lo[target],a),min(W.single_hi[target],b)));stats['configurations']+=1
                bad=build(W,target,i,j,True)
                if sum(W.d[q] for q in bad)!=y:stats['ordinary_filter_mutation_mass_reject']+=1
            lo=max(a for a,b in boxes);hi=min(b for a,b in boxes)
            if lo>hi:stats['empty_intersections']+=1
    stats['supplemented_classes']+=1
print(json.dumps({'result':stats,'seconds':round(time.time()-t,2),'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
