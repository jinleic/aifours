import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
import collections, json, math, time
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, vstack
from solve import ROOT, load, propagate


def feature_matrix(projections, iw, ib):
    keys=sorted({(k,int(code)) for color,ids in enumerate((iw,ib)) for k in range(projections[color].shape[1]) for code in projections[color][ids,k]})
    lookup={key:j for j,key in enumerate(keys)}
    rows=[];cols=[]
    for color,ids in enumerate((iw,ib)):
        off=0 if color==0 else len(iw)
        for i,ix in enumerate(ids):
            for k,code in enumerate(projections[color][ix]):
                rows.append(off+i);cols.append(lookup[k,int(code)])
    phi=csr_matrix((np.ones(len(rows),dtype=np.int64),(rows,cols)),shape=(len(iw)+len(ib),len(keys)))
    return keys,phi


def separate(projections,iw,ib,fs,m):
    keys,phi=feature_matrix(projections,iw,ib)
    sign=np.r_[-np.ones(len(iw)),np.ones(len(ib))]
    A=phi.multiply(sign[:,None]).tocsr()
    res=linprog(np.zeros(len(keys)),A_ub=A,b_ub=np.r_[-np.ones(len(iw)),np.zeros(len(ib))],bounds=(None,None),method='highs',options={'threads':1})
    if res.status==2: return None
    if not res.success: raise RuntimeError(res.message)
    for scale in [1,10,100,1000,1000000,1000000000]:
        coef=np.rint(res.x*scale).astype(np.int64)
        vals=phi@coef
        wmin=int(vals[:len(iw)].min());bmax=int(vals[len(iw):].max())
        if wmin>bmax:
            divisor=math.gcd(*(int(v) for v in coef),bmax)
            divisor=max(divisor,1)
            coef//=divisor;bmax//=divisor
            # Independent Python integer reconstruction, not float or int64 evidence.
            table={key:int(v) for key,v in zip(keys,coef) if v}
            scores=[]
            for color,ids in enumerate((iw,ib)):
                scores.append([sum(table.get((k,int(p)),0) for k,p in enumerate(projections[color][ix]))-bmax for ix in ids])
            assert min(scores[0])>=1 and max(scores[1])<=0
            return {'constant':-bmax,'terms':[{'forbidden':fs[k],'projection':[(code>>(5*i))&31 for i in range(m)],'coefficient':v} for (k,code),v in sorted(table.items())], 'white_min':min(scores[0]),'black_max':max(scores[1]),'verified_white':len(iw),'verified_black':len(ib),'arithmetic':'Python exact integers'}
    raise RuntimeError('Floating separator has no verified integral reconstruction')


def feasible_distribution(projections,iw,ib,arrays,qs,fs):
    _,phi=feature_matrix(projections,iw,ib)
    signs=np.r_[np.ones(len(iw)),-np.ones(len(ib))]
    A=vstack([phi.T.multiply(signs),csr_matrix(np.r_[np.ones(len(iw)),np.zeros(len(ib))][None,:]),csr_matrix(np.r_[np.zeros(len(iw)),np.ones(len(ib))][None,:])],format='csr')
    res=linprog(np.zeros(len(iw)+len(ib)),A_eq=A,b_eq=np.r_[np.zeros(phi.shape[1]),1,1],bounds=(0,None),method='highs',options={'threads':1})
    if not res.success:raise RuntimeError('Neither an exact separator nor a positive witness was obtained: '+res.message)
    masses=[Fraction(float(v)).limit_denominator(10000000) for v in res.x]
    colors=[]
    for color,ids in enumerate((iw,ib)):
        off=0 if color==0 else len(iw)
        colors.append([(tuple(map(int,arrays[color][ix])),masses[off+j]) for j,ix in enumerate(ids) if masses[off+j]>0])
    assert all(sum(p for _,p in color)==1 for color in colors)
    for f in fs:
        projected=[]
        for color in colors:
            counts=collections.Counter()
            for orbit,p in color:counts[tuple(sorted(c&f for c in orbit))]+=p
            projected.append(counts)
        assert projected[0]==projected[1]
    for q in qs:
        assert min(sum(bool(c&q) for c in a) for a,_ in colors[1])>max(sum(bool(c&q) for c in a) for a,_ in colors[0])
    return {name:[{'orbit':list(a),'probability':str(p)} for a,p in color] for name,color in zip(('white','black'),colors)}


def decide(case,m):
    started=time.monotonic(); qs,fs,arrays,weights,projections=load(case,m)
    iw=np.load(ROOT/f'case{case}_m{m}_white_ids.npy');ib=np.load(ROOT/f'case{case}_m{m}_black_ids.npy')
    nodes=[];memo={};found=[]
    def visit(iw,ib,thresholds):
        key=(tuple(map(int,iw)),tuple(map(int,ib)))
        if key in memo: return memo[key]
        node={'id':len(nodes),'thresholds':thresholds,'before':[len(iw),len(ib)],'arc_trace':[]}
        nid=len(nodes);nodes.append(node);memo[key]=nid
        iw,ib=propagate(weights,projections,iw,ib,node['arc_trace'])
        node['after']=[len(iw),len(ib)]
        if not len(iw) or not len(ib):
            node['kind']='empty';return nid
        cert=separate(projections,iw,ib,fs,m)
        if cert is not None:
            node['kind']='separating_functional';node['certificate']=cert;return nid
        conflicts=np.max(weights[0][iw],axis=0)>=np.min(weights[1][ib],axis=0)
        if not np.any(conflicts):
            node['kind']='feasible_distribution'
            node['witness']=feasible_distribution(projections,iw,ib,arrays,qs,fs)
            found.append(nid)
            return nid
        choices=[]
        for k in np.flatnonzero(conflicts):
            children=[];seen=set()
            for t in range(1,m+1):
                w=iw[weights[0][iw,k]<t];b=ib[weights[1][ib,k]>=t]
                if not len(w) or not len(b):continue
                ck=(tuple(map(int,w)),tuple(map(int,b)))
                if ck in seen:continue
                seen.add(ck);children.append((t,w,b))
            score=sum(len(w)*len(b) for _,w,b in children)
            choices.append((score,len(children),int(k),children))
        _,_,k,children=min(choices,key=lambda a:a[:3])
        node['kind']='threshold_split';node['qualified']=qs[k]
        node['threshold_cases']=[{'threshold':t,'candidate_counts':[int(np.sum(weights[0][iw,k]<t)),int(np.sum(weights[1][ib,k]>=t))]} for t in range(1,m+1)]
        node['children']=[]
        for t,w,b in children:
            node['children'].append({'threshold':t,'node':visit(w,b,thresholds+[[qs[k],t]])})
            if found:break
        return nid
    root=visit(iw,ib,[])
    out={'case':case,'m':m,'verdict':'YES' if found else 'NO','root':root,'nodes':nodes,'node_count':len(nodes),'branch_nodes':sum(n['kind']=='threshold_split' for n in nodes),'leaf_count':sum(n['kind']!='threshold_split' for n in nodes),'separator_terms':sum(len(n.get('certificate',{}).get('terms',[])) for n in nodes),'seconds':time.monotonic()-started}
    (ROOT/f'case{case}_m{m}_decision.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='nodes'}),flush=True)
    return out

if __name__=='__main__':
    for case,m in [(1,5),(2,6),(3,5),(4,6),(5,6),(5,7)]:decide(case,m)
