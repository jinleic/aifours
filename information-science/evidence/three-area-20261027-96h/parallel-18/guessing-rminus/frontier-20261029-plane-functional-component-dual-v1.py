#!/usr/bin/env python3
"""Actual-component-cut successor: adds the independently checked 1853-row
projection/parity Farkas inequality, transported to each selected triangle
by explicitly valid vertex permutations. No functional-fiber Delta import.
Version 3 adds ONLY the separately exactly re-derived fifth-order tuple
(5,6,15,15,5,0,0,5,0); its receipt must accompany any checker replay.
Version 2: full joint 13-variable Shannon closure plus the nine already
exactly re-derived DFZ tuples. No imported functional-fiber Delta gates.
Independent successor of direct-dual-v1 (NOT the paused v2 import route).
Adds literal conditional joint Zhang-Yeung rows using the valid 13-to-5-branch
entropy substitution. Full-state gate only; no two-syndrome Delta import.
Direct sparse dual certificate search for mixed-block functional classes.
Usage: python3 script.py OUT.jsonl CLASSES.json INDICES LIMIT_SECONDS CUTS.json CUTS_SHA
Reuses the v2 model's exact row construction, but does NOT optimize the primal
homogeneous cone. Instead solve sum(w_r*row_r)=3*Delta directly, with the
correct signs and an L1 objective (equality weights split positive/negative).
A basic positive-variable solution is proposed, then the old exact flint
identity/sign reconstruction accepts or rejects it. Independent certificate
checking is still mandatory. This is not a code-search or new entropy premise.
"""
from itertools import combinations,permutations
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
V=(1<<10)-1;S=1<<10;FULL=(1<<11)-1
LOOK={tuple(sorted(t)):i for i,t in enumerate(TRI)}
FP=[tuple(LOOK[tuple(sorted(p[v-1] for v in t))] for t in TRI) for p in P]
def mask(vs):return sum(1<<(v-1) for v in vs)
def move(m,p):return sum(1<<(p[i]-1) for i in range(10) if m>>i&1)

def actions(col):
    out=[]
    for p,f in zip(P,FP):
        for perm in permutations(range(3)):
            new=[None]*10
            for t in range(10):new[f[t]]=None if col[t] is None else perm[col[t]]
            if new==list(col):out.append((p,perm))
    return out

def build(col):
    acts=actions(col)
    def tr(a,b,p,cp):return (move(a,p),2+cp[b-2] if b>=2 else b)
    def canon(a,b):return min(tr(a,b,p,cp) for p,cp in acts)
    keys=sorted({canon(a,b) for a in range(V+1) for b in range(5) if a or b});index={k:i for i,k in enumerate(keys)};n=len(keys)
    rows=[];cols=[];data=[];lo=[];hi=[];names=[];seen=set();inf=highspy.kHighsInf
    def row(terms,l,h,name):
        clean={}
        for a,b,c in terms:
            if a or b:x=index[canon(a,b)];clean[x]=clean.get(x,0)+c
        key=(tuple(sorted((i,c) for i,c in clean.items() if c)),l,h)
        if not key[0] or key in seen:return
        seen.add(key);r=len(lo)
        for k,c in key[0]:rows.append(r);cols.append(k);data.append(c)
        lo.append(l);hi.append(h);names.append(name)
    def H(m,b):return (m&V,b if m&S else 0)
    for br in range(1,5):
        for i in range(11):row([(*H(FULL,br),1),(*H(FULL^(1<<i),br),-1)],0,inf,('mono',br,i))
        for i,j in combinations(range(11),2):
            a,b=1<<i,1<<j;rest=FULL^a^b;k=rest
            while True:
                row([(*H(k|a,br),1),(*H(k|b,br),1),(*H(k|a|b,br),-1),(*H(k,br),-1)],0,inf,('cmi',br,i,j,k))
                if not k:break
                k=(k-1)&rest
        row([(V,br,1),(V,0,-1)],0,0,('aux-determined',br))
        if br==1:row([(V,0,3),(0,br,17)]+[(1<<i,br,-2) for i in range(10)],-inf,0,('gate',br))
    for v in range(1,11):
        nm=mask(N[v]);row([(nm|1<<(v-1),0,1),(nm,0,-1)],0,0,('graph-fd',v))
        types={col[t] for t,T in enumerate(TRI) if v in T and col[t] is not None}
        for c in types:row([(nm,2+c,1),(nm,0,-1)],0,0,('functional-neighborhood',v,c))
        if len(types)>=2:row([(nm,1,1),(nm,0,-1)],0,0,('state-neighborhood',v))
        L=mask({u for t,T in enumerate(TRI) if col[t] is not None and v in T for u in T if u!=v})
        row([(L|1<<(v-1),1,1),(L,1,-1)],0,0,('mixed-local-fd',v))
    for t,T in enumerate(TRI):
        if col[t] is not None:m=mask(T);row([(m,2+col[t],1),(m,0,-1)],0,0,('functional-triangle',t+1))
    for a in range(V+1):
        for j in (2,3,4):
            row([(a,j,1),(a,1,-1)],-inf,0,('data-processing',a,j))
        for j,k in combinations((2,3,4),2):row([(a,1,1),(a,j,-1),(a,k,-1),(a,0,1)],-inf,0,('pair-determines-state',a,j,k))
    # Full 13-variable Shannon closure, mapped through the rank-two auxiliary circuit.
    for i in range(13):row(joint_shannon_terms(('joint-mono',i)),0,inf,('joint-mono',i))
    for i,j in combinations(range(13),2):
        rest=8191^(1<<i)^(1<<j);z=rest
        while True:
            row(joint_shannon_terms(('joint-cmi',i,j,z)),0,inf,('joint-cmi',i,j,z))
            if not z:break
            z=(z-1)&rest
    for cut in JOINT_CUTS:
        coef=cut['coefficients'];A,B,C,D,Z=[cut[k] for k in ('A','B','C','D','Z')]
        row(joint_dfz_terms(coef,A,B,C,D,Z),0,inf,('joint-dfz',list(coef),A,B,C,D,Z))
    for permutation,factor in COMPONENT_INSTANCES:
        if col[factor-1] is not None:row(component_terms(permutation,factor,col),0,inf,('component-cut',list(permutation),factor))
    rr=[[] for _ in names]
    for r,c,value in zip(rows,cols,data):rr[r].append((c,value))
    target=np.zeros(n);target[index[canon(V,0)]]=3
    for i in range(10):target[index[canon(1<<i,0)]]-=2
    return keys,acts,names,rr,lo,hi,target

from importlib.util import spec_from_file_location,module_from_spec
from hashlib import sha256
spec=spec_from_file_location('oldbatch',ROOT/'frontier-20261028-plane-functional-batch.py');oldbatch=module_from_spec(spec);spec.loader.exec_module(oldbatch)

JOINT_CUTS=[]
COMPONENT_CERT_SHA='bc22cd7ce064c262c2a2a5848853b75d54b6ab6a54c89fb0252504487555284d'
COMPONENT_RECEIPT='frontier-20261029-component-cut-factor2-case493-check-v1.json'
COMPONENT_RECEIPT_SHA='a6378ddecae934f63ad58e96e90c874223558b8449d211b5e9bdf1b4e40cdd9f'
_component_raw=(ROOT/COMPONENT_RECEIPT).read_bytes()
if sha256(_component_raw).hexdigest()!=COMPONENT_RECEIPT_SHA:raise ValueError('COMPONENT_RECEIPT_HASH')
_component_doc=json.loads(_component_raw)
if not _component_doc['all_checked'] or _component_doc['certificate_sha256']!=COMPONENT_CERT_SHA:raise ValueError('COMPONENT_ADMISSION')
COMPONENT_SCHEMA=_component_doc['primitive_schema_coefficients']
SOURCE_TRIANGLE=tuple(_component_doc['vertices'])

def component_instances():
    from itertools import permutations as ordered
    source_other=[v for v in range(1,11) if v not in SOURCE_TRIANGLE];out=[];seen=set()
    for t,T in enumerate(TRI):
        rest=sorted(set(range(1,11))-set(T))
        for orientation in ordered(T):
            mapping=dict(zip(SOURCE_TRIANGLE,orientation));mapping.update(zip(source_other,rest));p=tuple(mapping[v] for v in range(1,11));key=(p,t+1)
            if key not in seen:seen.add(key);out.append(key)
    for p in P:
        t=LOOK[tuple(sorted(p[v-1] for v in SOURCE_TRIANGLE))]+1;key=(tuple(p),t)
        if key not in seen:seen.add(key);out.append(key)
    return out
COMPONENT_INSTANCES=component_instances()

def component_terms(permutation,factor,col):
    color=col[factor-1]
    if color is None:raise ValueError('UNSELECTED_COMPONENT_FACTOR')
    result=[]
    for term in COMPONENT_SCHEMA:
        slot=term['auxiliary_slot'];br=0 if slot=='none' else (1 if slot=='state' else 2+color)
        result.append((move(term['original_mask'],permutation),br,term['coefficient']))
    return result


ADMITTED_DFZ={(5, 6, 15, 15, 5, 0, 0, 5, 0), (3, 9, 2, 2, 3, 0, 0, 3, 0), (2, 4, 2, 1, 2, 0, 0, 2, 3), (3, 7, 2, 2, 3, 0, 0, 3, 2), (3, 5, 6, 2, 3, 0, 0, 3, 0), (1, 2, 1, 1, 1, 0, 0, 1, 0), (8, 17, 9, 5, 8, 0, 0, 8, 0), (5, 20, 15, 1, 5, 0, 0, 5, 0), (2, 5, 2, 1, 2, 0, 0, 2, 0), (5, 10, 3, 6, 5, 0, 0, 5, 2)}

def joint_shannon_terms(name):
    def H(m):
        a=m&1023;u=m>>10;b=0 if not u else (1+u.bit_length() if u.bit_count()==1 else 1)
        return a,b
    if name[0]=='joint-mono':ts=[(8191,1),(8191^(1<<name[1]),-1)]
    else:
        _,i,j,z=name;ts=[(z|1<<i,1),(z|1<<j,1),(z|1<<i|1<<j,-1),(z,-1)]
    return [(*H(mask),w) for mask,w in ts]

def joint_dfz_terms(coef,A,B,C,D,Z):
    def H(m):
        a=m&1023;u=m>>10
        b=0 if not u else (1+u.bit_length() if u.bit_count()==1 else 1)
        return a,b
    def I(a,b,z):return [(a|z,1),(b|z,1),(a|b|z,-1),(z,-1)]
    a,b,c,d,e,f,g,h,i=coef;out=[]
    for weight,ts in [(-a,I(A,B,Z)),(b,I(A,B,C|Z)),(c,I(A,C,B|Z)),(d,I(B,C,A|Z)),(e,I(A,B,D|Z)),(f,I(A,D,B|Z)),(g,I(B,D,A|Z)),(h,I(C,D,Z)),(i,I(C,D,A|Z))]:
        for m,x in ts:
            if weight*x:out.append((*H(m),weight*x))
    return out

fl=oldbatch.fl;flint=oldbatch.flint
def terms(name,col):
    if name[0]=='component-cut':return component_terms(name[1],name[2],col)
    if name[0]=='joint-dfz':return joint_dfz_terms(name[1],*name[2:])
    if name[0] in ('joint-cmi','joint-mono'):return joint_shannon_terms(name)
    return oldbatch.terms(name,col)

def exact(r):
    col=r['colors'];acts=[(tuple(p),tuple(cp)) for p,cp in r['actions']]
    def tr(a,b,p,cp):return (fl.move(a,p),2+cp[b-2] if b>=2 else b)
    def canon(a,b):return min(tr(a,b,p,cp) for p,cp in acts)
    keys=[tuple(k) for k in r['keys']];ix={k:i for i,k in enumerate(keys)};n=len(keys);dd=r['dual_support'];k=len(dd)
    M=[[0]*k for _ in range(n)]
    for j,z in enumerate(dd):
        for a,b,w in terms(z['name'],col):
            if a or b:M[ix[canon(a,b)]][j]+=w
    t=[0]*n;t[ix[canon(V,0)]]+=3
    for i in range(10):t[ix[canon(1<<i,0)]]-=2
    Mf=flint.fmpz_mat(M)
    if Mf.rank()!=k:return None,'RANK_DEFICIENT'
    Mt=Mf.transpose();y=(Mt*Mf).solve(Mt*flint.fmpz_mat([[x] for x in t]))
    res=flint.fmpq_mat(Mf)*y
    if any(res[i,0]!=t[i] for i in range(n)):return None,'INCONSISTENT'
    mult=[]
    for j,z in enumerate(dd):
        q=y[j,0];kind=z['name'][0]
        if q==0:continue
        if kind in ('cmi','mono','joint-dfz','joint-cmi','joint-mono','component-cut') and not q<0:return None,'SIGN'
        if kind in ('gate','data-processing','pair-determines-state') and not q>0:return None,'SIGN'
        mult.append({'row':z['name'],'multiplier':str(q)})
    return {'colors':col,'actions':r['actions'],'multipliers':mult,'target':'3*Delta'},'ok'

def direct_certificate(col,limit):
    keys,acts,names,rr,lo,hi,target=build(col);n=len(keys);starts=[];ids=[];values=[];which=[];inf=highspy.kHighsInf
    for r,items in enumerate(rr):
        signs=(-1,) if lo[r]==0 and hi[r]==inf else ((1,) if lo[r]==-inf and hi[r]==0 else (1,-1))
        for sign in signs:
            starts.append(len(ids));which.append((r,sign))
            for c,a in items:ids.append(c);values.append(sign*a)
    nv=len(which);lp=highspy.HighsLp();lp.num_col_=nv;lp.num_row_=n
    lp.col_cost_=np.ones(nv);lp.col_lower_=np.zeros(nv);lp.col_upper_=np.full(nv,inf)
    lp.row_lower_=target;lp.row_upper_=target;lp.a_matrix_.format_=highspy.MatrixFormat.kColwise
    lp.a_matrix_.start_=np.array(starts+[len(ids)],dtype=np.int32);lp.a_matrix_.index_=np.array(ids,dtype=np.int32);lp.a_matrix_.value_=np.array(values,dtype=float)
    h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',limit)
    h.setOptionValue('solver','ipm');h.setOptionValue('run_crossover','on');h.setOptionValue('primal_feasibility_tolerance',1e-9);h.setOptionValue('dual_feasibility_tolerance',1e-9)
    h.passModel(lp);t=monotonic();h.run();status=h.modelStatusToString(h.getModelStatus())
    report={'status_float':status,'dual_variables':nv,'coefficient_equations':n,'solve_s':monotonic()-t,'certificate':None}
    if status!='Optimal':return report
    weights={}
    for (r,sign),v in zip(which,h.getSolution().col_value):
        if v!=0:weights[r]=weights.get(r,0.)+sign*float(v)
    proposal={'colors':list(col),'actions':[[list(p),list(cp)] for p,cp in acts],'keys':keys,
      'dual_support':[{'name':names[r],'float':v} for r,v in weights.items() if v!=0]}
    cert,exact_status=exact(proposal)
    if cert is not None:cert['component_proof_sha256']=COMPONENT_CERT_SHA;cert['component_proof_receipt_sha256']=COMPONENT_RECEIPT_SHA
    report.update({'exact_status':exact_status,'certificate':cert,'proposed_support_rows':len(proposal['dual_support']),'floating_L1_objective':h.getInfo().objective_function_value})
    return report

def main():
    out=ROOT/sys.argv[1];raw=(ROOT/sys.argv[2]).read_bytes();classes=json.loads(raw)['colorings'];indices=[int(i) for i in sys.argv[3].split(',')];limit=float(sys.argv[4])
    global JOINT_CUTS
    cutraw=(ROOT/sys.argv[5]).read_bytes()
    if sha256(cutraw).hexdigest()!=sys.argv[6]:raise ValueError('CUT_FILE_HASH')
    JOINT_CUTS=json.loads(cutraw)['cuts']
    for cut in JOINT_CUTS:
        if tuple(cut['coefficients']) not in ADMITTED_DFZ:raise ValueError('UNADMITTED_DFZ_TUPLE')
        masks=[cut[k] for k in ('A','B','C','D','Z')]
        if not all(masks[:4]) or any(not 0<=m<8192 for m in masks) or any(masks[i]&masks[j] for i in range(5) for j in range(i+1,5)):raise ValueError('JOINT_ROLE_MASKS')
    with out.open('x') as f:
        for i in indices:
            text=classes[i];col=tuple(None if ch=='-' else int(ch) for ch in text);r=direct_certificate(col,limit)
            r.update({'joint_cuts_sha256':sys.argv[6],'index':i,'colors':text,'class_file_sha256':sha256(raw).hexdigest(),'status':('ok' if r.get('exact_status')=='ok' else r.get('exact_status',r['status_float']))})
            f.write(json.dumps(r)+'\n');f.flush();print(i,text,r['status'],r.get('proposed_support_rows'),r['solve_s'],flush=True)
if __name__=='__main__':main()
