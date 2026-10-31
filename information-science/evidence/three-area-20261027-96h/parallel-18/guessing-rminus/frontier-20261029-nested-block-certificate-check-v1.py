#!/usr/bin/env python3
"""Independent exact checker for nested-block certificates.
Usage: python3 script.py OUT.json CERT.json CERT_SHA VERIFY.json VERIFY_SHA [...]
Legacy rows use the pinned v5 checker. No generator/producer import. All nested
block rows are reconstructed from the declared original source, original over-
set, block sizes and count vectors. The kernel lemma, not this arithmetic
check, supplies the validity of within-block exchangeability.
"""
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
BASE='frontier-20261029-dfz-certificate-check-v5.py';BASE_SHA='26bd124a5bbdfe39088778fbd9e97bc707ee8ec938bf574197a3417273f61f49'
if sha256((ROOT/BASE).read_bytes()).hexdigest()!=BASE_SHA:raise ValueError('BASE_HASH')
s=spec_from_file_location('legacy',ROOT/BASE);legacy=module_from_spec(s);s.loader.exec_module(legacy)

def compile_specs(cert):
    result={}
    for i,branch in enumerate(cert['nested_copy_blocks']):
        blocks=[]
        if not branch['blocks']:raise ValueError('NB_EMPTY')
        for bl in branch['blocks']:
            v,k,over=bl['vertex'],bl['copies'],bl['over']
            if isinstance(v,bool) or not isinstance(v,int) or not 1<=v<=10:raise ValueError('NB_VERTEX')
            if isinstance(k,bool) or not isinstance(k,int) or k<1:raise ValueError('NB_COPIES')
            if len(set(over))!=len(over) or v in over or any(isinstance(x,bool) or not isinstance(x,int) or not 1<=x<=10 for x in over):raise ValueError('NB_OVER')
            blocks.append((1<<(v-1),sum(1<<(x-1) for x in over),k))
        result[f'n{i}']=blocks
    return result

def terms(row,specs):
    kind=row[0]
    if not kind.startswith('nb'):return legacy.row_terms(row)
    tag=row[1]
    if tag not in specs:raise ValueError('NB_TAG')
    blocks=specs[tag];ks=tuple(bl[2] for bl in blocks);d=len(ks);zero=(0,)*d
    def K(m,q):
        q=tuple(q)
        if not isinstance(m,int) or not 0<=m<=1023 or len(q)!=d or any(isinstance(x,bool) or not isinstance(x,int) or not 0<=x<=ks[a] for a,x in enumerate(q)):raise ValueError('NB_KEY')
        if m==0 and q==zero:return None
        return ('o',m) if q==zero else (tag,m,*q)
    def out(ts,t='eq'):return [(K(m,q),c) for m,q,c in ts],t
    def bump(q,a):
        r=list(q);r[a]+=1;return tuple(r)
    if kind=='nbmono':
        typ,i=row[2:]
        if typ=='o':
            if not 0<=i<10:raise ValueError('NB_MONO_ORIGINAL')
            return out([(1023,ks,1),(1023^(1<<i),ks,-1)],'ge')
        if typ=='c':
            if not 0<=i<d:raise ValueError('NB_MONO_COPY')
            q=list(ks);q[i]-=1;return out([(1023,ks,1),(1023,q,-1)],'ge')
        raise ValueError('NB_MONO_TYPE')
    if kind=='nbcmi':
        typ,i,j,z,q=row[2:];q=tuple(q);K(z,q)
        if typ=='oo':
            if not 0<=i<j<10 or z&((1<<i)|(1<<j)):raise ValueError('NB_CMI_OO')
            return out([(z|1<<i,q,1),(z|1<<j,q,1),(z|1<<i|1<<j,q,-1),(z,q,-1)],'ge')
        if typ=='oc':
            if not 0<=i<10 or not 0<=j<d or z&(1<<i) or q[j]>=ks[j]:raise ValueError('NB_CMI_OC')
            qj=bump(q,j);return out([(z|1<<i,q,1),(z,qj,1),(z|1<<i,qj,-1),(z,q,-1)],'ge')
        if typ=='cc':
            if not 0<=i<j<d or q[i]>=ks[i] or q[j]>=ks[j]:raise ValueError('NB_CMI_CC')
            qi=bump(q,i);qj=bump(q,j);qij=bump(qi,j)
            return out([(z,qi,1),(z,qj,1),(z,qij,-1),(z,q,-1)],'ge')
        if typ=='same':
            if not 0<=i<d or j!=i or q[i]>ks[i]-2:raise ValueError('NB_CMI_SAME')
            qi=bump(q,i);qii=bump(qi,i);return out([(z,qi,2),(z,qii,-1),(z,q,-1)],'ge')
        raise ValueError('NB_CMI_TYPE')
    if kind=='nbcopy':
        a,u,q=row[2:];q=tuple(q)
        if not 0<=a<d:raise ValueError('NB_COPY_BLOCK')
        old,Y,k=blocks[a];K(u,q)
        if u&~Y or q[a]>=k or any(q[t] for t in range(a+1,d)):raise ValueError('NB_COPY_SUBSET')
        return out([(u,bump(q,a),1),(u|old,q,-1)])
    if kind=='nbind':
        a,r=row[2:]
        if not 0<=a<d or not 0<=r<ks[a]:raise ValueError('NB_IND_INDEX')
        Y=blocks[a][1];q=ks[:a]+(r,)+(0,)*(d-a-1);qn=bump(q,a)
        return out([(1023,qn,1),(Y,q,1),(1023,q,-1),(Y,qn,-1)])
    raise ValueError('NB_ROW_KIND')

def check(cert,verified):
    specs=compile_specs(cert);legacy.set_extra(cert.get('extra_single_copies'));legacy.set_programs(cert.get('programs'))
    acc={};bound=Fraction();used=set()
    for item in cert['multipliers']:
        row=item['row'];w=Fraction(item['multiplier'])
        if row[0] in ('dfz','dfzb'):
            t=tuple(row[1] if row[0]=='dfz' else row[2])
            if t not in verified:raise ValueError('UNVERIFIED_DFZ')
            used.add(t)
        ts,typ=terms(row,specs)
        if typ=='ge' and w>0:raise ValueError('SIGN')
        if typ=='cap':
            if w<0:raise ValueError('CAP_SIGN')
            bound+=w
        for key,c in ts:
            if key is not None:acc[key]=acc.get(key,Fraction())+w*c
    if {key:v for key,v in acc.items() if v}!={('o',1023):Fraction(1)}:raise ValueError('IDENTITY')
    if bound!=Fraction(cert['bound']):raise ValueError('BOUND_CLAIM')
    return bound,used

def main():
    raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('CERT_HASH')
    cert=json.loads(raw);verified=set();deps=[]
    for p,h in zip(sys.argv[4::2],sys.argv[5::2]):
        data=(ROOT/p).read_bytes()
        if sha256(data).hexdigest()!=h:raise ValueError('VERIFY_HASH')
        verified.update(tuple(r['coefficients']) for r in json.loads(data)['results'] if r['valid_exact']);deps.append({'path':p,'sha256':h})
    bound,used=check(cert,verified);controls={}
    def reject(name,c,v=verified):
        try:check(c,v)
        except (ValueError,KeyError,IndexError) as e:controls[name]=str(e)
        else:raise ValueError(('CONTROL_NOT_REJECTED',name))
    ni=next(i for i,m in enumerate(cert['multipliers']) if m['row'][0]=='nbcmi')
    c=deepcopy(cert);c['multipliers'][ni]['multiplier']=str(-Fraction(c['multipliers'][ni]['multiplier']));reject('flipped_nested_cmi_sign',c)
    c=deepcopy(cert);c['multipliers'][ni]['row'][-1][0]=-1;reject('negative_copy_count',c)
    c=deepcopy(cert);c['multipliers'][ni]['multiplier']=str(2*Fraction(c['multipliers'][ni]['multiplier']));reject('changed_nested_cmi_weight',c)
    c=deepcopy(cert);ci=next(i for i,m in enumerate(c['multipliers']) if m['row'][0]=='cap');c['multipliers'][ci]['multiplier']=str(2*Fraction(c['multipliers'][ci]['multiplier']));reject('changed_cap_weight',c)
    c=deepcopy(cert);c['bound']=str(bound+1);reject('changed_reported_bound',c)
    if used:reject('dropped_dfz_receipt',cert,verified-{next(iter(used))})
    doc={'certificate_sha256':sys.argv[3],'legacy_checker_sha256':BASE_SHA,'dfz_dependencies':deps,'all_checked':True,'bound':str(bound),'bound_float':float(bound),
         'rows':len(cert['multipliers']),'row_kinds':{k:sum(m['row'][0]==k for m in cert['multipliers']) for k in sorted({m['row'][0] for m in cert['multipliers']})},
         'dfz_tuples_used':[list(t) for t in sorted(used)],'negative_controls':controls,
         'limits':'Exact Fraction identity, signs, row syntax and bound; nested conditional-kernel proof is a separate written premise. No formalization, independent scientific review or novelty clearance.'}
    with open(ROOT/sys.argv[1],'x') as f:json.dump(doc,f,indent=1);f.write('\n')
    print(json.dumps(doc,indent=1))
if __name__=='__main__':main()
