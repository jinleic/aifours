#!/usr/bin/env python3
"""[F] Constructive controls for Lemmas RZ/RZ2/RZX, not an avoider census.
Usage: python3 -B replayLB.py
(1) Every binary path length <= 11; every RZ and RZ2 request satisfying the written sufficient inequalities: build the configuration.
(2) Explicit all-single-letter words in 3 layouts (one anti block / spread / random), sampled classes from all routes E/S/S2,
including p=7, (11;5,3), and (43;32,8): build the prescribed configuration at every run; independent slow_lambda verifies all four arcs.
(3) 36 explicit excess words of (31;51,24,23), different excess distributions: build RZX configurations for every weight, compare the
actual two-pattern interval with the conservative hull, and check no-wrap/(QS*) or actual empty bounds.
Mutations: RZ omit removing neighbours of anti picks; RZ2 omit a separator between pairs. Structural checks count detections.
"""
import itertools, random, json, time, resource
GUARD="if __name__ == '__main__':\n    main()"
N={"__name__":"seedLB3lib"}
exec(compile(open('seedLB3.py').read().replace(GUARD,''),'seedLB3.py','exec'),N)
S=N['NS']; L=N['NSL']
G={"__name__":"cpluslib"}
exec(compile(open('../c5/cplus_replay.py').read().replace(GUARD,''),'c5/cplus_replay.py','exec'),G)
slow=G['slow_lambda']; Wg=G['Wg']
rnd=random.Random(19017)
def intervals(path, eligible):
    out=[]; block=[]
    for t in path:
        if eligible(t): block.append(t)
        elif block: out.append(block);block=[]
    if block:out.append(block)
    return out
def rz(path,a,b,i,j,mut=0):
    candidates=[t for block in intervals(path,lambda t:a[t]==0 and b[t]>0) for t in block[::2]]
    assert len(candidates)>=i
    anti=set(candidates[:i]); banned=set(anti)
    if mut==0:
        for pos,t in enumerate(path):
            if t in anti:
                if pos:banned.add(path[pos-1])
                if pos+1<len(path):banned.add(path[pos+1])
    available=[t for block in intervals(path,lambda t:b[t]==0 and t not in banned) for t in block[::2]]
    assert len(available)>=j
    return anti|set(available[:j])
def rz2(path,a,b,j1,j2,mut=0):
    segs=intervals(path,lambda t:b[t]==0); paircounts=[]; need=j2
    for seg in segs:
        num=min(need,(len(seg)+1)//3); paircounts.append(num);need-=num
    assert need==0
    Q=set()
    for seg,np in zip(segs,paircounts):
        for z in range(np):
            pos=(3 if mut==0 else 2)*z
            Q.update(seg[pos:pos+2])
        # Under mutation the omitted separator is local to the pairs; singles keep their original positions.
    need=j1
    for seg,np in zip(segs,paircounts):
        for pos in range(3*np,len(seg),2):
            if need==0:break
            Q.add(seg[pos]);need-=1
    assert need==0
    return Q
def line_blocks(path,Q):
    return sum(t in Q and (z==0 or path[z-1] not in Q) for z,t in enumerate(path))
def cycle_blocks(k,Q):return sum(t in Q and (t-1)%k not in Q for t in range(k))
def class_arcs(p,kB,B):
    A=p+kB;kap=kB+B
    lam=lambda y,m:min(p-m+1,y+m-kB,(y+B)//2+1)
    lamc=lambda y,m:min(p-m+1,A-kap-y+m,(A-y)//2+1)
    return lam,lamc,lambda y,m:p-lamc(y,m)
def word_from(p,kB,B,layout):
    k=p+kB+B
    anti=set(range(B)) if layout==0 else (set((i*k)//B for i in range(B)) if layout==1 else set(rnd.sample(range(k),B)))
    a=[int(t not in anti) for t in range(k)];b=[int(t in anti) for t in range(k)]
    ref=[1]*k;ref[rnd.randrange(k)]+=2*(p-1-kB-B)
    return Wg(p,a,b,ref)
def arcs(W,Q):
    return slow(W.p,W.d,W.l,W.B,W.kappa,sorted(Q)),slow(W.p,W.d,W.l,W.B,W.kappa,[t for t in range(W.k) if t not in Q])
def check_word_type(W,t,Q,y,m):
    assert t not in Q and all((q-t)%W.k not in (1,W.k-1) for q in Q)
    assert cycle_blocks(W.k,Q)==m and cycle_blocks(W.k,Q|{t})==m+1
    assert sum(W.d[q] for q in Q)==y
    l,lc=arcs(W,Q);lt,lct=arcs(W,Q|{t})
    fast=lambda yy,mm:min(W.p-mm+1,yy+mm-W.kB,(yy+W.B)//2+1)
    fastc=lambda yy,mm:min(W.p-mm+1,W.A-W.kappa-yy+mm,(W.A-yy)//2+1)
    d=W.d[t]
    assert (l,lc,lt,lct)==(fast(y,m),fastc(y,m),fast(y+d,m+1),fastc(y+d,m+1))
    return lt-W.p+lc,W.p-lct-l

def exhaustive_paths():
    stats={"paths":0,"RZ":0,"RZ2":0,"M1_structural_reject":0,"M2_structural_reject":0}
    for n in range(1,12):
        path=list(range(n))
        for mask in range(1<<n):
            a=[int((mask>>t)&1) for t in path];b=[1-aa for aa in a];alpha=sum(a);beta=n-alpha
            r=len(intervals(path,lambda t:b[t]==0));stats['paths']+=1
            for i in range(beta//2+1):
                for j in range(max(alpha//2-i,0)+1):
                    if 2*(i+j)>alpha:continue
                    Q=rz(path,a,b,i,j);stats['RZ']+=1
                    assert len(Q)==i+j and line_blocks(path,Q)==i+j and sum(b[t] for t in Q)==i
                    Qm=rz(path,a,b,i,j,1)
                    if line_blocks(path,Qm)!=i+j:stats['M1_structural_reject']+=1
            cap=alpha-r
            for j2 in range(max(cap,0)//3+1):
                for j1 in range(max(cap-3*j2,0)//2+1):
                    if 3*j2+2*j1>cap:continue
                    Q=rz2(path,a,b,j1,j2);stats['RZ2']+=1
                    assert len(Q)==j1+2*j2 and line_blocks(path,Q)==j1+j2
                    Qm=rz2(path,a,b,j1,j2,1)
                    if len(Qm)!=j1+2*j2 or line_blocks(path,Qm)!=j1+j2:stats['M2_structural_reject']+=1
    return stats

def literal_singles():
    pool={'E':[],'S':[],'S2':[]}
    for p in (7,11,23,31,43,61):
        for kb in range(1,p):
            for B in range(2,p):
                if kb+B>p-3 or 2*B+kb<p-1:continue
                z=L['route_SE'](p,kb,B,0)
                if z[0] in ('E','S'):pool[z[0]].append((p,kb,B,z))
                else:
                    zz=N['route_S2'](p,kb,B)
                    if zz[0]=='S2':pool['S2'].append((p,kb,B,zz))
    pick=[]
    for route,vals in pool.items():pick+=rnd.sample(vals,min(8,len(vals)))
    for p,kb,B in ((7,2,2),(7,1,3),(11,5,3),(43,32,8)):
        z=L['route_SE'](p,kb,B,0)
        if z[0] not in ('E','S'):z=N['route_S2'](p,kb,B)
        pick.append((p,kb,B,z))
    counts={"classes":len(pick),"words":0,"configurations":0,"empty_bounds":0,"seed_bounds":0}
    for p,kb,B,z in pick:
        lam,lamc,U=class_arcs(p,kb,B)
        for layout in range(3):
            W=word_from(p,kb,B,layout);counts['words']+=1
            for t,d in enumerate(W.d):
                if z[0]=='E':
                    if d!=z[1]:continue
                    y,m=z[2];i=(m-y)//2;j=m-i
                    assert (m-y)%2==0
                    path=[(t+2+s)%W.k for s in range(W.k-3)]
                    Q=rz(path,W.a,W.b,i,j)
                elif z[0]=='S':
                    y,m=z[1][d];i=(m-y)//2;j=m-i
                    assert (m-y)%2==0
                    path=[(t+2+s)%W.k for s in range(W.k-3)]
                    Q=rz(path,W.a,W.b,i,j)
                else:
                    y,m,j2,j1=z[1][d];path=[(t+2+s)%W.k for s in range(W.k-3)]
                    Q=rz2(path,W.a,W.b,j1,j2)
                slo,shi=check_word_type(W,t,Q,y,m)
                assert (slo,shi)==(lam(y+d,m+1)-U(y,m),U(y+d,m+1)-lam(y,m))
                L1,U1=lam(d,1),U(d,1)
                assert L1-shi>-p and U1-slo<p
                a,b=max(L1,slo),min(U1,shi)
                if a>b:counts['empty_bounds']+=1
                else:
                    alo,bhi=S['bounds'](p,W.k,W.kappa,B,d,0)
                    assert a>=alo and b<=bhi
                    counts['seed_bounds']+=1
                counts['configurations']+=1
    return counts

def excess_words():
    stats={"words":0,"configurations":0,"empty_bounds":0,"seed_bounds":0}
    for ix in range(36):
        p,k,kap,B,E=31,51,24,23,8
        npr=rnd.randrange(9);ean=rnd.randrange(E-npr+1);nan=B-npr-ean;nal=k-nan-npr
        a0=[1]*nal;b0=[1]*nan
        for _ in range(E-npr-ean):a0[rnd.randrange(nal)]+=1
        for _ in range(ean):b0[rnd.randrange(nan)]+=1
        runs=[(x,0) for x in a0]+[(0,x) for x in b0]+[(1,1)]*npr
        rnd.shuffle(runs);a,b=map(list,zip(*runs));ref=[1]*k;ref[0]+=2*(p-1-kap)
        W=Wg(p,a,b,ref);assert (W.kappa,W.E,W.B)==(kap,E,B)
        astar=max(a0);nlo=B-E+astar-1;assert nan>=nlo
        data={}
        for d in set(W.d):
            et=abs(d)-1 if d else 1;er=E-et;L1=slow(p,W.d,W.l,B,kap,[W.d.index(d)]);U1=p-slow(p,W.d,W.l,B,kap,[q for q in range(k) if q!=W.d.index(d)])
            alo,bhi=S['bounds'](p,k,kap,B,d,0)
            fast=lambda y,m:min(p-m+1,y+m-W.kB,(y+B)//2+1)
            fc=lambda y,m:min(p-m+1,W.A-kap-y+m,(W.A-y)//2+1)
            best=None
            for m in range(1,(nal-3)//2+1):
                for i in range(min(m,max((nlo-3)//2,0))+1):
                    j=m-i;rl=[];rh=[];ok=True
                    for y in range(j-i-er,j-i+er+1):
                        sl=fast(y+d,m+1)-p+fc(y,m);sh=p-fc(y+d,m+1)-fast(y,m)
                        if not (L1-sh>-p and U1-sl<p):ok=False;break
                        rl.append(sl);rh.append(sh)
                    if not ok:continue
                    aa,bb=max(L1,min(rl)),min(U1,max(rh))
                    if aa>bb or (aa>=alo and bb<=bhi):best=(i,j,min(rl),max(rh));break
                if best:break
            assert best is not None,(d,nal,nan,astar)
            data[d]=best
        for t,d in enumerate(W.d):
            i,j,hl,hh=data[d];m=i+j
            path=[(t+2+s)%k for s in range(k-3)];Q=rz(path,W.a,W.b,i,j);y=sum(W.d[q] for q in Q)
            et=abs(d)-1 if d else 1
            assert j-i-(E-et)<=y<=j-i+(E-et)
            slo,shi=check_word_type(W,t,Q,y,m);assert hl<=slo and shi<=hh
            aa,bb=max(W.single_lo[t],hl),min(W.single_hi[t],hh)
            if aa>bb:stats['empty_bounds']+=1
            else:stats['seed_bounds']+=1
            stats['configurations']+=1
        stats['words']+=1
    return stats

def main():
    start=time.time()
    print(json.dumps({'part':'exhaustive-paths','result':exhaustive_paths()}),flush=True)
    print(json.dumps({'part':'literal-singletons','result':literal_singles()}),flush=True)
    print(json.dumps({'part':'literal-excess','result':excess_words()}),flush=True)
    print(json.dumps({'elapsed':round(time.time()-start,2),'child_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
if __name__ == '__main__':
    main()
