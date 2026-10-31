#!/usr/bin/env python3
"""Actual-component successor: recursively rechecks the literal inner Farkas
proof, validates each component instance and then checks the outer 3*Delta
identity. No producing code is imported and no functional-fiber Delta gate is
accepted. This is same-harness arithmetic, not an independent human review.
Version 2 independently reconstructs full joint 13-variable Shannon rows
in addition to conditional joint DFZ rows. The old full-state-only gate is
retained; no functional-fiber Delta gate or paused source is accepted.
Independent successor of OLD plane-functional-check (not paused v2).
Adds conditional joint DFZ rows only with exact derivation receipts; the literal
13-to-5-branch substitution is reconstructed independently below.
Independent checker for plane-functional certificates (exact Fractions).

Usage: python3 script.py OUT.json CERTS.json SHA COMPONENT_CERT.json COMPONENT_SHA VERIFY.json VERIFY_SHA [...]
Each certificate: colors (list over {None,0,1,2} per factor), actions (list of
[vertex permutation, functional permutation]) and multipliers of named rows,
normalized so the identity target is 3*Delta. Rows are rebuilt from graph and
coloring data; every (vertex, functional) action is re-verified to preserve
the coloring up to the given functional permutation; signs and the averaged
identity on all 5,119 branch coordinates are checked exactly.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json,sys
from copy import deepcopy
from importlib.util import spec_from_file_location,module_from_spec

ROOT=Path(__file__).resolve().parent
VERIFIED_DFZ=set()
COMPONENT_SCHEMA=None
COMPONENT_SOURCE_TRIANGLE=None
COMPONENT_PROOF_SHA=None
ADMITTED_COMPONENT_PROOF='bc22cd7ce064c262c2a2a5848853b75d54b6ab6a54c89fb0252504487555284d'
ADMITTED_COMPONENT_RECEIPT='a6378ddecae934f63ad58e96e90c874223558b8449d211b5e9bdf1b4e40cdd9f'
INNER_CHECKER='frontier-20261029-component-cut-independent-check-v1.py'
INNER_CHECKER_SHA='13d19361a84fc1347e81ea49217b46de9a720577d9649762191d59638f0600a2'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
V=(1<<10)-1;S=1<<10;FULL=(1<<11)-1
LOOK={tuple(sorted(t)):i for i,t in enumerate(TRI)}
def vm(vs):return sum(1<<(v-1) for v in vs)

def rows(name,col):
    k=name[0]
    def H(m,b):return (m&V,b if m&S else 0)
    if k=='component-cut':
        if COMPONENT_SCHEMA is None or COMPONENT_SOURCE_TRIANGLE is None:raise ValueError('UNLOADED_COMPONENT_PROOF')
        permutation,factor=name[1:];permutation=tuple(permutation)
        if len(permutation)!=10 or sorted(permutation)!=list(range(1,11)) or not 1<=factor<=10:raise ValueError('COMPONENT_INSTANCE')
        if tuple(sorted(permutation[v-1] for v in COMPONENT_SOURCE_TRIANGLE))!=tuple(sorted(TRI[factor-1])):raise ValueError('COMPONENT_INSTANCE_GEOMETRY')
        if col[factor-1] is None:raise ValueError('COMPONENT_FACTOR_NOT_SELECTED')
        color=col[factor-1];out=[]
        for term in COMPONENT_SCHEMA:
            a=term['original_mask'];moved=sum(1<<(permutation[i]-1) for i in range(10) if a>>i&1)
            slot=term['auxiliary_slot'];br=0 if slot=='none' else (1 if slot=='state' else 2+color)
            out.append((moved,br,term['coefficient']))
        return out,'ge'
    if k in ('joint-cmi','joint-mono'):
        def mapped(mask):
            base=mask&1023;u=mask>>10
            return base,(0 if not u else ({1:2,2:3,4:4}[u] if u in (1,2,4) else 1))
        if k=='joint-mono':
            i=name[1]
            if not 0<=i<13:raise ValueError('JOINT_MONO')
            raw=[(8191,1),(8191^(1<<i),-1)]
        else:
            i,j,z=name[1:]
            if not 0<=i<j<13 or not 0<=z<8192 or z&((1<<i)|(1<<j)):raise ValueError('JOINT_CMI')
            raw=[(z|1<<i,1),(z|1<<j,1),(z|1<<i|1<<j,-1),(z,-1)]
        return [(*mapped(m),w) for m,w in raw],'ge'
    if k=='joint-dfz':
        coef=tuple(name[1]);masks=name[2:]
        if coef not in VERIFIED_DFZ:raise ValueError('UNVERIFIED_DFZ')
        if len(masks)!=5 or not all(masks[:4]) or any(isinstance(m,bool) or not isinstance(m,int) or not 0<=m<8192 for m in masks):raise ValueError('JOINT_DFZ_ROLES')
        if any(masks[i]&masks[j] for i in range(5) for j in range(i+1,5)):raise ValueError('JOINT_DFZ_OVERLAP')
        P,Q,R,T,Z=masks
        def HH(mask):
            original=mask&1023;aux=mask>>10
            if aux==0:return original,0
            if aux in (1,2,4):return original,{1:2,2:3,4:4}[aux]
            return original,1
        def MI(x,y,z):return [(x|z,1),(y|z,1),(x|y|z,-1),(z,-1)]
        a,b,c,d,e,f,g,h,i=coef;out=[]
        pieces=[(-a,MI(P,Q,Z)),(b,MI(P,Q,R|Z)),(c,MI(P,R,Q|Z)),(d,MI(Q,R,P|Z)),(e,MI(P,Q,T|Z)),(f,MI(P,T,Q|Z)),(g,MI(Q,T,P|Z)),(h,MI(R,T,Z)),(i,MI(R,T,P|Z))]
        for scale,ts in pieces:
            for mask,sign in ts:
                if scale*sign:out.append((*HH(mask),scale*sign))
        return out,'ge'
    if k=='mono':
        _,br,i=name
        if br not in range(1,5) or not 0<=i<11:raise ValueError('MONO')
        return [(*H(FULL,br),1),(*H(FULL^(1<<i),br),-1)],'ge'
    if k=='cmi':
        _,br,i,j,K=name
        if br not in range(1,5) or not 0<=i<j<11 or not 0<=K<=FULL or K&((1<<i)|(1<<j)):raise ValueError('CMI')
        a,b=1<<i,1<<j;return [(*H(K|a,br),1),(*H(K|b,br),1),(*H(K|a|b,br),-1),(*H(K,br),-1)],'ge'
    if k=='aux-determined':
        br=name[1];return [(V,br,1),(V,0,-1)],'eq'
    if k=='gate':
        if name[1]!=1:raise ValueError('ONLY_STATE_GATE_ALLOWED')
        return [(V,0,3),(0,1,17)]+[(1<<i,1,-2) for i in range(10)],'le'
    if k=='graph-fd':
        v=name[1];n=vm(N[v]);return [(n|1<<(v-1),0,1),(n,0,-1)],'eq'
    if k=='functional-neighborhood':
        _,v,c=name
        if c not in {col[t] for t,T in enumerate(TRI) if v in T and col[t] is not None}:raise ValueError('FUNCTIONAL_VISIBILITY')
        for t,T in enumerate(TRI):
            if v in T and col[t]==c and any(u!=v and u not in N[v] for u in T):raise ValueError('TRIANGLE_EDGE')
        n=vm(N[v]);return [(n,2+c,1),(n,0,-1)],'eq'
    if k=='state-neighborhood':
        v=name[1]
        if len({col[t] for t,T in enumerate(TRI) if v in T and col[t] is not None})<2:raise ValueError('STATE_VISIBILITY')
        n=vm(N[v]);return [(n,1,1),(n,0,-1)],'eq'
    if k=='mixed-local-fd':
        v=name[1];L={u for t,T in enumerate(TRI) if col[t] is not None and v in T for u in T if u!=v}
        if not L:raise ValueError('UNCOVERED')
        L=vm(L);return [(L|1<<(v-1),1,1),(L,1,-1)],'eq'
    if k=='functional-triangle':
        t=name[1]
        if col[t-1] is None:raise ValueError('FIXED_TRIANGLE')
        m=vm(TRI[t-1]);return [(m,2+col[t-1],1),(m,0,-1)],'eq'
    if k=='data-processing':
        _,a,j=name
        if not 0<=a<=V or j not in (2,3,4):raise ValueError('DP')
        return [(a,j,1),(a,1,-1)],'le'
    if k=='pair-determines-state':
        _,a,j,l=name
        if not 0<=a<=V or not (j in (2,3,4) and l in (2,3,4) and j<l):raise ValueError('PAIR')
        return [(a,1,1),(a,j,-1),(a,l,-1),(a,0,1)],'le'
    raise ValueError(('ROW',name))

def check(c,change=False):
    if any(row['row'][0]=='component-cut' for row in c['multipliers']):
        if c.get('component_proof_sha256')!=COMPONENT_PROOF_SHA or c.get('component_proof_receipt_sha256')!=ADMITTED_COMPONENT_RECEIPT:raise ValueError('COMPONENT_PROOF_BINDING')
    col=[None if x is None else int(x) for x in c['colors']]
    if len(col)!=10 or all(x is None for x in col):raise ValueError('COLORS')
    J={t for t in range(10) if col[t] is not None}
    if set().union(*(set(TRI[t]) for t in J))!=set(N):raise ValueError('COVER')
    E={tuple(sorted((u,v))) for u in N for v in N[u]};acts=[]
    for p,cp in c['actions']:
        p=tuple(p);cp=tuple(cp)
        if set(p)!=set(N) or {tuple(sorted((p[a-1],p[b-1]))) for a,b in E}!=E or sorted(cp)!=[0,1,2]:raise ValueError('ACTION')
        moved=[tuple(sorted(p[v-1] for v in t)) for t in TRI]
        if set(moved)!=set(LOOK):raise ValueError('FACTORS')
        f=[LOOK[m] for m in moved];new=[None]*10
        for t in range(10):new[f[t]]=None if col[t] is None else cp[col[t]]
        if new!=col:raise ValueError('COLOR_ACTION')
        acts.append((p,cp))
    if (tuple(range(1,11)),(0,1,2)) not in acts:raise ValueError('IDENTITY_ACTION')
    acc={};g=len(acts)
    for item in c['multipliers']:
        q=Fraction(item['multiplier']);ts,kind=rows(item['row'],col)
        if not q:raise ValueError('ZERO')
        if kind=='ge' and q>=0:raise ValueError('SIGN_GE')
        if kind=='le' and q<=0:raise ValueError('SIGN_LE')
        for p,cp in acts:
            for a,b,w in ts:
                a2=sum(1<<(p[i]-1) for i in range(10) if a>>i&1);b2=2+cp[b-2] if b>=2 else b
                if a2 or b2:acc[(a2,b2)]=acc.get((a2,b2),0)+q*w/g
    tgt={(V,0):Fraction(3)}
    for i in range(10):tgt[(1<<i,0)]=Fraction(-2)
    if change:tgt[(V,0)]+=1
    keys=set(acc)|set(tgt)
    if any(acc.get(k,0)!=tgt.get(k,0) for k in keys):raise ValueError('IDENTITY')
    return Counter(x['row'][0] for x in c['multipliers'])

def main():
    out=ROOT/sys.argv[1];raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('HASH')
    global COMPONENT_SCHEMA,COMPONENT_SOURCE_TRIANGLE,COMPONENT_PROOF_SHA
    compraw=(ROOT/sys.argv[4]).read_bytes()
    if sha256(compraw).hexdigest()!=sys.argv[5] or sys.argv[5]!=ADMITTED_COMPONENT_PROOF:raise ValueError('COMPONENT_CERTIFICATE_HASH')
    receipt=(ROOT/'frontier-20261029-component-cut-factor2-case493-check-v1.json').read_bytes()
    if sha256(receipt).hexdigest()!=ADMITTED_COMPONENT_RECEIPT:raise ValueError('COMPONENT_RECEIPT_HASH')
    if sha256((ROOT/INNER_CHECKER).read_bytes()).hexdigest()!=INNER_CHECKER_SHA:raise ValueError('INNER_CHECKER_HASH')
    spec=spec_from_file_location('inner',ROOT/INNER_CHECKER);inner=module_from_spec(spec);spec.loader.exec_module(inner)
    compcert=json.loads(compraw);ccounts,cvalue,primitive,cscale=inner.check(compcert)
    COMPONENT_SCHEMA=primitive;COMPONENT_SOURCE_TRIANGLE=tuple(compcert['vertices']);COMPONENT_PROOF_SHA=sys.argv[5]
    component_dependency={'certificate_sha256':sys.argv[5],'checker_sha256':INNER_CHECKER_SHA,'receipt_sha256':ADMITTED_COMPONENT_RECEIPT,'proof_rows_rechecked':sum(ccounts.values()),'primitive_terms':len(primitive),'primitive_scale':str(cscale)}
    VERIFIED_DFZ.clear();dependencies=[]
    for path,expected in zip(sys.argv[6::2],sys.argv[7::2]):
        vr=(ROOT/path).read_bytes()
        if sha256(vr).hexdigest()!=expected:raise ValueError('DFZ_RECEIPT_HASH')
        VERIFIED_DFZ.update(tuple(r['coefficients']) for r in json.loads(vr)['results'] if r['valid_exact']);dependencies.append({'path':path,'sha256':expected})
    certs=json.loads(raw)['certificates'];summary=[]
    for c in certs:
        cnt=check(c);summary.append({'colors':c['colors'],'rows':sum(cnt.values()),'kinds':dict(cnt)})
    try:check(certs[0],change=True)
    except ValueError as e:control=str(e)
    else:raise ValueError('CONTROL')
    dfz_control={}
    if any(m['row'][0]=='joint-dfz' for c in certs for m in c['multipliers']):
        c=next(c for c in certs if any(m['row'][0]=='joint-dfz' for m in c['multipliers']))
        i=next(i for i,m in enumerate(c['multipliers']) if m['row'][0]=='joint-dfz')
        mutant=deepcopy(c);mutant['multipliers'][i]['multiplier']=str(-Fraction(mutant['multipliers'][i]['multiplier']))
        try:check(mutant)
        except ValueError as e:dfz_control['flipped_joint_dfz_sign']=str(e)
        else:raise ValueError('DFZ_CONTROL')
        mutant=deepcopy(c);mutant['multipliers'][i]['row'][2]=0
        try:check(mutant)
        except ValueError as e:dfz_control['empty_joint_role']=str(e)
        else:raise ValueError('DFZ_CONTROL')
        used=tuple(c['multipliers'][i]['row'][1]);VERIFIED_DFZ.remove(used)
        try:check(c)
        except ValueError as e:dfz_control['dropped_exact_derivation']=str(e)
        else:raise ValueError('DFZ_CONTROL')
        VERIFIED_DFZ.add(used)
    component_controls={}
    if any(row['row'][0]=='component-cut' for c in certs for row in c['multipliers']):
        c=next(c for c in certs if any(row['row'][0]=='component-cut' for row in c['multipliers']))
        i=next(i for i,row in enumerate(c['multipliers']) if row['row'][0]=='component-cut')
        mutant=deepcopy(c);mutant['component_proof_sha256']='0'*64
        try:check(mutant)
        except ValueError as e:component_controls['changed_inner_proof_binding']=str(e)
        else:raise ValueError('COMPONENT_CONTROL')
        mutant=deepcopy(c);mutant['multipliers'][i]['multiplier']=str(-Fraction(mutant['multipliers'][i]['multiplier']))
        try:check(mutant)
        except ValueError as e:component_controls['flipped_component_cut_sign']=str(e)
        else:raise ValueError('COMPONENT_CONTROL')
        mutant=deepcopy(c);factor=mutant['multipliers'][i]['row'][2];mutant['multipliers'][i]['row'][2]=1 if factor!=1 else 2
        try:check(mutant)
        except ValueError as e:component_controls['changed_instance_factor']=str(e)
        else:raise ValueError('COMPONENT_CONTROL')
    rep={'component_dependency':component_dependency,'component_negative_controls':component_controls,'checker_source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'dfz_dependencies':dependencies,'dfz_negative_controls':dfz_control,'certificates_sha256':sys.argv[3],'all_checked':True,'count':len(certs),'cases':summary,'negative_control':control,
         'limits':'Exact identities, signs, coloring-action and premise checks. Only the full-state gate, admitted conditional DFZ inequalities and the recursively checked actual-component inequality are used. No two-syndrome entropy theorem or paused functional-gate route is imported. Written mixed-block lifting and the joint-variable substitution require mathematical review.'}
    with out.open('x',encoding='utf-8') as f:json.dump(rep,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in rep.items() if k!='cases'},indent=2))


if __name__=='__main__':main()
