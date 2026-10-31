#!/usr/bin/env python3
"""Cutting-plane LP: R-minus Shannon bound plus conditional DFZ instances.

Usage: python3 script.py OUT.json MAX_ROUNDS BRANCHES [PRELOAD_RESULT.json SHA]
Variables are the 1,023 original joint entropies (plus, if BRANCHES=gurpinar,
the publisher's three copy branches). Rows: every elemental Shannon inequality
(of each variable set), caps h(v)<=1, the ten graph FD equalities, copy
equalities, and an iteratively grown set of instances of the published
Dougherty-Freiling-Zeger inequalities (independently re-derived separately)
with A,B,C,D,Z disjoint unions of original variables. Each round solves the
LP (floating, HiGHS), scans all 6^10 role assignments for all listed DFZ
inequalities at the current original profile, and adds the most violated
instances. Floating output is a proposal; an exact dual certificate must be
reconstructed and checked separately before any bound is claimed.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json,re,sys,time
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
TEX='frontier-20261029-dfz-source/src/nonShannon.tex'
TEX_SHA='ab01cd4113f334715d6e80b538bfcca657d659380504be916de2bd43857e732c'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),
   6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
INF=highspy.kHighsInf

def coefficients():
    raw=(ROOT/TEX).read_bytes()
    if sha256(raw).hexdigest()!=TEX_SHA:raise ValueError('TEX_HASH')
    lines=raw.decode('utf-8').split('\n')
    s=next(i for i,l in enumerate(lines) if 'label{FourCopies}' in l);e=next(i for i,l in enumerate(lines) if 'label{infinite}' in l)
    out={}
    for l in lines[s:e]:
        m=re.match(r'\s*\\item\s+((?:\d+\s+){9})(.*)',l)
        if m:out.setdefault(tuple(int(x) for x in m.group(1).split()),m.group(2).strip())
    out.setdefault((1,2,1,1,1,0,0,1,0),'r c ab.')
    return out

class Model:
    """Sparse row store with coordinates indexed by (branch-local) masks mapped to global columns."""
    def __init__(self):
        self.col={};self.rows=[];self.lo=[];self.hi=[];self.meta=[]
    def c(self,key):
        if key not in self.col:self.col[key]=len(self.col)
        return self.col[key]
    def add(self,terms,lo,hi,meta):
        t={}
        for key,x in terms:
            if key is None:continue
            j=self.c(key);t[j]=t.get(j,0)+x
        t={j:x for j,x in t.items() if x}
        if not t:return
        self.rows.append(t);self.lo.append(lo);self.hi.append(hi);self.meta.append(meta)

def base_key(m):return None if m==0 else ('o',m)

def add_shannon(M,names,keyf):
    n=len(names);full=(1<<n)-1
    for i in range(n):M.add([(keyf(full),1),(keyf(full^(1<<i)),-1)],0,INF,('mono',names,i))
    for i,j in combinations(range(n),2):
        rest=full^(1<<i)^(1<<j);z=rest
        while True:
            M.add([(keyf(z|1<<i),1),(keyf(z|1<<j),1),(keyf(z|1<<i|1<<j),-1),(keyf(z),-1)],0,INF,('cmi',names,i,j,z))
            if not z:break
            z=(z-1)&rest

def gurpinar_branches(M):
    L='abcdefghij'
    def branch(tag,aux):
        names=list(L)+aux;pos={x:k for k,x in enumerate(names)}
        def keyf(m):
            if m==0:return None
            if m<1024:return ('o',m)
            return (tag,m)
        return names,pos,keyf
    def mk(pos,s):return sum(1<<pos[x] for x in s)
    def copy(names,pos,keyf,new,old,over,existing):
        Y=mk(pos,over)
        for q in range(1,1<<len(new)):
            nm=sum(1<<pos[new[k]] for k in range(len(new)) if q>>k&1);om=sum(1<<pos[old[k]] for k in range(len(new)) if q>>k&1)
            U=Y
            while True:
                M.add([(keyf(U|nm),1),(keyf(U|om),-1)],0,0,('copy',tuple(new),q,U))
                if not U:break
                U=(U-1)&Y
        E=mk(pos,existing);Nn=mk(pos,new)
        M.add([(keyf(E|Nn),1),(keyf(Y),1),(keyf(E),-1),(keyf(Y|Nn),-1)],0,0,('independence',tuple(new)))
    # branch 1: b'0 copies b over a,d,e,f,g,h,i,j
    names,pos,keyf=branch('b1',["b'0"]);add_shannon(M,names,keyf)
    copy(names,pos,keyf,["b'0"],['b'],list('adefghij'),list(L))
    names,pos,keyf=branch('b2',["d'1","e'1","g'2"]);add_shannon(M,names,keyf)
    copy(names,pos,keyf,["d'1","e'1"],['d','e'],list('abcfghi'),list(L))
    copy(names,pos,keyf,["g'2"],['g'],['a','b','c','d',"e'1",'f','h','i'],list(L)+["d'1","e'1"])
    names,pos,keyf=branch('b3',["f'3","g'3","h'4"]);add_shannon(M,names,keyf)
    copy(names,pos,keyf,["f'3","g'3"],['f','g'],list('abcdehij'),list(L))
    copy(names,pos,keyf,["h'4"],['h'],['a','b','c','d','e','f',"f'3",'i','j'],list(L)+["f'3","g'3"])

def build(branches):
    M=Model()
    for m in range(1,1024):M.c(('o',m))
    add_shannon(M,list('abcdefghij'),base_key)
    for v in range(1,11):
        n=sum(1<<(u-1) for u in N[v]);M.add([(('o',n|1<<(v-1)),1),(('o',n),-1)],0,0,('fd',v))
        M.add([(('o',1<<(v-1)),1)],-INF,1,('cap',v))
    if branches in ('gurpinar','gurpinar-sym'):gurpinar_branches(M)
    if branches in ('sym','gurpinar-sym'):
        # automorphism symmetrization of the original profile (valid: the closure of the entropic cone is convex
        # and every listed row type is invariant, so the max is attained at a symmetrized almost-entropic vector)
        GEN=((7,9,6,5,8,2,3,0,1,4),(0,4,5,6,1,2,3,7,8,9))
        for gi,g in enumerate(GEN):
            for m in range(1,1024):
                gm=sum(1<<g[i] for i in range(10) if m>>i&1)
                if gm!=m:M.add([(('o',m),1),(('o',gm),-1)],0,0,('sym',gi,m))
    return M

def dfz_terms(k,A,B,C,D,Z):
    a,b,c,d,e,f,g,h,i=k
    def I(x,y,z):return [(x|z,1),(y|z,1),(x|y|z,-1),(z,-1)]
    out={}
    for w,t in [(-a,I(A,B,Z)),(b,I(A,B,C|Z)),(c,I(A,C,B|Z)),(d,I(B,C,A|Z)),(e,I(A,B,D|Z)),(f,I(A,D,B|Z)),(g,I(B,D,A|Z)),(h,I(C,D,Z)),(i,I(C,D,A|Z))]:
        if not w:continue
        for m,x in t:
            if m:out[m]=out.get(m,0)+w*x
    return {m:x for m,x in out.items() if x}

class Scanner:
    def __init__(self,keys):
        self.keys=keys;self.W=np.array([[-k[0]]+list(k[1:]) for k in keys],dtype=np.float64).T
        n=8;idx=np.arange(6**n,dtype=np.int64);digs=np.stack([(idx//6**k)%6 for k in range(n)],axis=1)
        self.tail=[sum(((digs[:,k]==r).astype(np.int64)<<(k+2)) for k in range(n)) for r in range(6)]
    def scan(self,H,per=3):
        cands=[]
        for d0 in range(6):
            for d1 in range(6):
                m=[self.tail[r]+((1 if d0==r else 0)<<0)+((1 if d1==r else 0)<<1) for r in range(6)]
                A,B,C,D,Z=m[1],m[2],m[3],m[4],m[5];ok=(A>0)&(B>0)&(C>0)&(D>0);A,B,C,D,Z=A[ok],B[ok],C[ok],D[ok],Z[ok]
                h=lambda x:H[x]
                hZ=h(Z);hAZ=h(A|Z);hBZ=h(B|Z);hCZ=h(C|Z);hDZ=h(D|Z);hABZ=h(A|B|Z);hACZ=h(A|C|Z);hBCZ=h(B|C|Z)
                hADZ=h(A|D|Z);hBDZ=h(B|D|Z);hCDZ=h(C|D|Z);hABCZ=h(A|B|C|Z);hABDZ=h(A|B|D|Z);hACDZ=h(A|C|D|Z)
                MF=np.stack([hAZ+hBZ-hABZ-hZ,hACZ+hBCZ-hABCZ-hCZ,hABZ+hBCZ-hABCZ-hBZ,hABZ+hACZ-hABCZ-hAZ,
                             hADZ+hBDZ-hABDZ-hDZ,hABZ+hBDZ-hABDZ-hBZ,hABZ+hADZ-hABDZ-hAZ,hCZ+hDZ-hCDZ-hZ,hACZ+hADZ-hACDZ-hAZ],axis=1)
                for s in range(0,len(MF),500000):
                    V=MF[s:s+500000]@self.W
                    p=np.argpartition(V,per,axis=0)[:per]
                    for kk in range(V.shape[1]):
                        for r in p[:,kk]:
                            val=V[r,kk]
                            if val<-1e-9:cands.append((float(val),kk,int(A[s+r]),int(B[s+r]),int(C[s+r]),int(D[s+r]),int(Z[s+r])))
        return cands

def solve(M,h=None,added_from=0):
    if h is None:
        h=highspy.Highs();h.silent();h.setOptionValue('threads',1)
        lp=highspy.HighsLp();n=len(M.col);lp.num_col_=n;cost=np.zeros(n);cost[M.col[('o',1023)]]=-1.0
        lp.col_cost_=cost;lp.col_lower_=np.full(n,-INF);lp.col_upper_=np.full(n,INF)
        starts=[];ids=[];vals=[]
        for t in M.rows:
            starts.append(len(ids))
            for j,x in t.items():ids.append(j);vals.append(float(x))
        lp.num_row_=len(M.rows);lp.row_lower_=np.array(M.lo,dtype=float);lp.row_upper_=np.array(M.hi,dtype=float)
        lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise;lp.a_matrix_.start_=np.array(starts+[len(ids)],dtype=np.int32)
        lp.a_matrix_.index_=np.array(ids,dtype=np.int32);lp.a_matrix_.value_=np.array(vals,dtype=float)
        if len(M.rows)>100000:h.setOptionValue('solver','ipm');h.setOptionValue('run_crossover','on')
        h.passModel(lp)
    else:
        h.setOptionValue('solver','simplex')
        rows=M.rows[added_from:]
        if rows:
            starts=[];ids=[];vals=[]
            for t in rows:
                starts.append(len(ids))
                for j,x in t.items():ids.append(j);vals.append(float(x))
            h.addRows(len(rows),np.array(M.lo[added_from:],dtype=float),np.array(M.hi[added_from:],dtype=float),len(ids),
                      np.array(starts,dtype=np.int32),np.array(ids,dtype=np.int32),np.array(vals,dtype=float))
    t=time.monotonic();h.run();status=h.modelStatusToString(h.getModelStatus())
    x=np.array(h.getSolution().col_value);obj=-h.getInfo().objective_function_value
    return h,status,obj,x,time.monotonic()-t

def main():
    out=ROOT/sys.argv[1];rounds=int(sys.argv[2]);branches=sys.argv[3] if len(sys.argv)>3 else 'none'
    t0=time.monotonic();coeff=coefficients();keys=sorted(coeff);M=build(branches);S=Scanner(keys)
    seen=set();cuts=[]
    if len(sys.argv)>5:
        raw=(ROOT/sys.argv[4]).read_bytes()
        if sha256(raw).hexdigest()!=sys.argv[5]:raise ValueError('PRELOAD_HASH')
        for c in json.loads(raw)['cuts']:
            kk=keys.index(tuple(c['coefficients']));key=(kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
            if key in seen:continue
            seen.add(key);t=dfz_terms(keys[kk],c['A'],c['B'],c['C'],c['D'],c['Z'])
            M.add([(('o',m),x2) for m,x2 in t.items()],0,INF,('dfz',list(keys[kk]),c['A'],c['B'],c['C'],c['D'],c['Z']))
            cuts.append({'coefficients':list(keys[kk]),'A':c['A'],'B':c['B'],'C':c['C'],'D':c['D'],'Z':c['Z'],'violation_at_add':'preloaded'})
    print('columns',len(M.col),'rows',len(M.rows),'preloaded cuts',len(cuts),flush=True)
    h,status,obj,x,dt=solve(M);log=[{'round':0,'status':status,'objective':obj,'rows':len(M.rows),'solve_s':dt}]
    print(log[-1],flush=True)
    for rnd in range(1,rounds+1):
        H=np.zeros(1024);H[1:]=x[[M.col[('o',m)] for m in range(1,1024)]]
        cands=S.scan(H);cands.sort();chosen=[];per={}
        for val,kk,A,B,C,D,Z in cands:
            key=(kk,A,B,C,D,Z)
            if key in seen or per.get(kk,0)>=40:continue
            seen.add(key);per[kk]=per.get(kk,0)+1;chosen.append((val,)+key)
            if len(chosen)>=400:break
        if not chosen:log.append({'round':rnd,'violations':0});print('no violations',flush=True);break
        start=len(M.rows)
        for val,kk,A,B,C,D,Z in chosen:
            t=dfz_terms(keys[kk],A,B,C,D,Z);M.add([(('o',m),x2) for m,x2 in t.items()],0,INF,('dfz',list(keys[kk]),A,B,C,D,Z))
            cuts.append({'coefficients':list(keys[kk]),'A':A,'B':B,'C':C,'D':D,'Z':Z,'violation_at_add':val})
        h,status,obj,x,dt=solve(M,h,start)
        log.append({'round':rnd,'added':len(chosen),'most_violated':chosen[0][0],'status':status,'objective':obj,'rows':len(M.rows),'solve_s':round(dt,2),'elapsed_s':round(time.monotonic()-t0,1)})
        print(log[-1],flush=True)
    H=x[[M.col[('o',m)] for m in range(1,1024)]]
    res={'branches':branches,'tex_sha256':TEX_SHA,'inequalities':len(keys),'log':log,'final_objective_float':obj,'cuts':cuts,
         'final_original_profile_float':[float(v) for v in H],
         'limits':'Floating cutting-plane proposal only. A bound is claimed only after an exact rational dual certificate is reconstructed and independently checked.'}
    with open(out,'x',encoding='utf-8') as f:json.dump(res,f);f.write('\n')

if __name__=='__main__':main()
