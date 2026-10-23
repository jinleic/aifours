#!/usr/bin/env python3
"""README B3: inflate a bare H(5,6,4,3) by zero-sum RDTD(3,4,3), then search for NEW resolutions at size18.
No size6 frame/resolution is assumed. Reconstruct the D15 or Z3xD5 KM model exactly and bind its retained SAT
model by the CNF hash; verify the bare540 blocks directly. Inflate each block to27 zero-sum blocks on copies
(p,beta)->3p+beta, yielding14580 blocks. At representatives(0,0),(0,1), independently colour the648 derived
triples: FD into nine PCs per missing-group family, or RD into27 PCs of all72 points outside the group.
Master automorphisms act on master labels with beta fixed; copy negation beta->-beta identifies reps1,2.
The output contains EVERY point's classes and is checked by both definition-first routes without symmetry.
This is a fixed-design search: any UNSAT/UNKNOWN is restricted, not a nonexistence proof.
Usage: inflate_h6_frames.py FD|RD D15|Z3xD5 RETAINED_KMONLY_RUNDIR NEW_OUTDIR NATIVE_SECONDS SEED
"""
import lane_guard  # noqa: F401
import hashlib
import itertools
import json
import os
import subprocess
import sys
import time
from collections import Counter, defaultdict
from lane_guard import fresh_dir, xopen
from lanelib import CNF, kissat, parse_status, model_satisfies
from gdd_seed_search4 import group_D15, group_Z3xD5


def reconstruct_master(name, source, out):
    els, idx, mul, K = {'D15':group_D15,'Z3xD5':group_Z3xD5}[name]()
    cosets, assigned = [], set()
    for a in els:
        if idx[a] not in assigned:
            C=sorted(idx[mul(a,k)] for k in K)
            cosets.append(C);assigned.update(C)
    order=[p for C in cosets for p in C]
    lab={p:i for i,p in enumerate(order)}
    G=sorted({tuple(lab[idx[mul(a,els[order[q]])]] for q in range(30)) for a in els})
    assert len(G)==30 and len({e[0] for e in G})==30
    image=lambda e,T:tuple(sorted(e[p] for p in T))
    canon=lambda T:min(image(e,T) for e in G)
    trans=lambda T:len({p//6 for p in T})==len(T)
    tc={T:canon(T) for T in itertools.combinations(range(30),3) if trans(T)}
    ts=Counter(tc.values());cols=sorted(ts);ci={T:i for i,T in enumerate(cols)}
    qs=Counter(canon(Q) for Q in itertools.combinations(range(30),4) if trans(Q))
    rows=[]
    for Q in sorted(qs):
        counts=Counter(ci[tc[T]] for T in itertools.combinations(Q,3))
        if all(qs[Q]*n==ts[cols[c]] for c,n in counts.items()):rows.append((Q,sorted(counts)))
    cnf=CNF();yv=[cnf.var() for _ in rows];bycol=defaultdict(list)
    for j,(_,cs) in enumerate(rows):
        for c in cs:bycol[c].append(yv[j])
    for c in range(len(cols)):cnf.exactly_one(bycol[c])
    sha=cnf.write(os.path.join(out,'master-replay.cnf'))
    old=json.load(open(os.path.join(source,'summary.json')))
    assert old['km_only']==1 and old['group']==name and sha==old['cnf_sha256'], 'master model does not replay'
    logpath=os.path.join(source,'model.cnf.log')
    status, model=parse_status(open(logpath).read())
    assert status=='SAT' and model_satisfies(os.path.join(out,'master-replay.cnf'),model)
    blocks=sorted({image(e,Q) for j,(Q,_) in enumerate(rows) if yv[j] in model for e in G})
    expected={T for T in itertools.combinations(range(30),3) if trans(T)}
    covered=Counter(T for B in blocks for T in itertools.combinations(B,3))
    assert len(blocks)==540 and set(covered)==expected and set(covered.values())=={1}
    with xopen(os.path.join(out,'master-h6.json')) as fh:
        json.dump({'group':name,'groups':[list(range(6*i,6*i+6)) for i in range(5)],'blocks':blocks,'permutations':G,
                   'source_run':source,'source_cnf_sha256':sha,
                   'source_model_sha256':hashlib.sha256(open(logpath,'rb').read()).hexdigest()},fh,indent=1)
    return blocks,G


def fixed_frame_model(blocks,x,kind):
    derived=sorted(tuple(p for p in B if p!=x) for B in blocks if x in B)
    assert len(derived)==len(set(derived))==648
    gx=x//18
    miss={T:(set(range(5))-{gx}-{p//18 for p in T}).pop() for T in derived}
    if kind=='FD':
        families=[(y,[p for p in range(90) if p//18 not in (gx,y)]) for y in range(5) if y!=gx]
        nclass=9
        imbalance=[]
        for y,points in families:
            for p in points:
                degree=sum(p in T for T in derived if miss[T]==y)
                if degree!=9:imbalance.append((y,p,degree))
        if imbalance:return None,{'family_degree_imbalance':imbalance[:12]}
    else:
        families=[(0,[p for p in range(90) if p//18!=gx])];nclass=27
    cnf=CNF();z={(T,j):cnf.var() for T in derived for j in range(nclass)}
    pv=defaultdict(list)
    for T in derived:
        cnf.exactly_one([z[(T,j)] for j in range(nclass)])
        family=miss[T] if kind=='FD' else 0
        for j in range(nclass):
            for p in T:pv[(family,j,p)].append(z[(T,j)])
    for family,points in families:
        for j in range(nclass):
            for p in points:cnf.exactly_one(pv[(family,j,p)])
        anchor=min(points)
        Ts=sorted(T for T in derived if anchor in T and (kind=='RD' or miss[T]==family))
        before=[None]*nclass
        for T in Ts:
            for j in range(1,nclass):
                cnf.add([-z[(T,j)],before[j-1]] if before[j-1] is not None else [-z[(T,j)]])
            after=[]
            for j in range(nclass):
                v=cnf.var();zi=z[(T,j)]
                if before[j] is None:cnf.add([-v,zi]);cnf.add([v,-zi])
                else:
                    cnf.add([-before[j],v]);cnf.add([-zi,v]);cnf.add([-v,before[j],zi])
                after.append(v)
            before=after
    return (cnf,z,derived,miss,families,nclass),None


def main():
    kind,name,source,out,tl,sd=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],int(sys.argv[5]),int(sys.argv[6])
    assert kind in ('FD','RD')
    fresh_dir(out);started=time.perf_counter()
    master,G=reconstruct_master(name,source,out)
    inflated=set()
    for B in master:
        for a,b,c in itertools.product(range(3),repeat=3):
            d=(-a-b-c)%3
            inflated.add(tuple(sorted((3*B[0]+a,3*B[1]+b,3*B[2]+c,3*B[3]+d))))
    blocks=sorted(inflated)
    assert len(blocks)==14580
    rec={'kind':kind,'master_group':name,'master_blocks':540,'inflated_blocks':len(blocks),'colourings':[]}
    solutions={}
    for alpha in (0,1):
        package,why=fixed_frame_model(blocks,alpha,kind)
        if package is None:
            rec['colourings'].append({'copy':alpha,'status':'DEGREE-OBSTRUCTION-FIXED-DESIGN',**why});break
        cnf,z,derived,miss,families,nclass=package
        path=os.path.join(out,f'colour-copy{alpha}.cnf');sha=cnf.write(path)
        cr={'copy':alpha,'triples':len(derived),'vars':cnf.nv,'clauses':len(cnf.clauses),'cnf_sha256':sha}
        print(json.dumps({'stage':'colour-model',**cr}),flush=True)
        st,model,seconds=kissat(path,tl,seed=sd,log=path+'.log')
        cr.update({'status':st,'seconds':seconds});rec['colourings'].append(cr)
        print(json.dumps(cr),flush=True)
        if st!='SAT':break
        classes=[]
        for family,_ in families:
            for j in range(nclass):
                classes.append((family if kind=='FD' else j,
                                sorted(T for T in derived if (kind=='RD' or miss[T]==family) and z[(T,j)] in model)))
        assert sorted(T for _,C in classes for T in C)==derived
        solutions[alpha]=classes
    if len(solutions)==2:
        sections={}
        for e in G:
            for alpha in range(3):
                base=0 if alpha==0 else 1
                def image_point(p):
                    q,beta=divmod(p,3)
                    return 3*e[q]+((-beta)%3 if alpha==2 else beta)
                xp=3*e[0]+alpha
                sections[xp]=[((e[6*y]//6) if kind=='FD' else y,
                               sorted(tuple(sorted(image_point(p) for p in T)) for T in C))
                              for y,C in solutions[base]]
        assert sorted(sections)==list(range(90))
        L=[f'GDD34 {kind}GDD 5 18','GROUPS']+[' '.join(str(p) for p in range(18*i,18*i+18)) for i in range(5)]+['BLOCKS']
        L+=[' '.join(map(str,B)) for B in blocks]
        for x in range(90):
            L.append(f'POINT {x}')
            for y,C in sections[x]:
                L.append(f"{'FRAME' if kind=='FD' else 'PC'} {y}")
                L+=[' '.join(map(str,T)) for T in C]
        text='\n'.join(L)+'\n';cert=os.path.join(out,f'{kind.lower()}gdd_5_18_inflated_{name}.txt')
        with xopen(cert) as fh:fh.write(text)
        rec.update({'certificate':cert,'sha256':hashlib.sha256(text.encode()).hexdigest()})
        run=subprocess.run([sys.executable,os.path.join(os.path.dirname(__file__),'check_gdd34.py'),cert],capture_output=True,text=True)
        rec['route1']=json.loads(run.stdout)
        run=subprocess.run([os.path.join(os.path.dirname(__file__),'bin','check_gdd34_c'),cert],capture_output=True,text=True)
        rec['route2']=run.stdout.strip()
    rec['total_seconds']=time.perf_counter()-started
    with xopen(os.path.join(out,'summary.json')) as fh:json.dump(rec,fh,indent=1)
    print(json.dumps(rec),flush=True)


if __name__=='__main__':main()
