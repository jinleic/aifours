#!/usr/bin/env python3
"""Independent exact row reconstruction for exchangeable-copy certificates.

Usage: python3 script.py OUT.json CERT.json CERT_SHA VERIFY.json VERIFY_SHA [...]
No import from the LP generator/producer. Legacy row types use the byte-pinned
v5 checker; exchangeable row types are independently reconstructed below from
ordinary-base masks and copy counts. This verifies arithmetic and row syntax;
the written conditional-kernel lemma supplies exchangeability's validity.
"""
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
BASE='frontier-20261029-dfz-certificate-check-v5.py'
BASE_SHA='26bd124a5bbdfe39088778fbd9e97bc707ee8ec938bf574197a3417273f61f49'
if sha256((ROOT/BASE).read_bytes()).hexdigest()!=BASE_SHA:raise ValueError('BASE_CHECKER_HASH')
s=spec_from_file_location('legacy',ROOT/BASE);legacy=module_from_spec(s);s.loader.exec_module(legacy)
T2=sum(1<<(x-1) for x in (1,4,5,6,7,8,9,10));T4=sum(1<<(x-1) for x in (1,2,5,6,7,8,10))

def compile_specs(cert):
    out={}
    for i,sp in enumerate(cert['exchangeable_copies']):
        k=sp['copies'];tail=sp.get('tail',False)
        if isinstance(k,bool) or not isinstance(k,int) or k<1 or not isinstance(tail,bool):raise ValueError('EC_SPEC')
        out[f'e{i}']=(k,tail,12 if tail else 11)
    return out

def terms(row,specs):
    kind=row[0]
    if not kind.startswith('ec'):return legacy.row_terms(row)
    tag=row[1]
    if tag not in specs:raise ValueError('EC_TAG')
    k,tail,b=specs[tag];full=(1<<b)-1;c0=1<<10;d=1<<11;E=1023|c0;Y=T4|c0;Yt=T2|c0
    def K(m,r):
        if not isinstance(m,int) or not isinstance(r,int) or m<0 or m>full or not 0<=r<=k:raise ValueError('EC_KEY')
        if m==0 and r==0:return None
        return ('o',m) if r==0 and m<1024 else (tag,m,r)
    def out(ts,t='eq'):return [(K(m,r),a) for m,r,a in ts],t
    if kind=='ecmono':
        i=row[2]
        if i==-1:return out([(full,k,1),(full,k-1,-1)],'ge')
        if not 0<=i<b:raise ValueError('EC_MONO')
        return out([(full,k,1),(full^(1<<i),k,-1)],'ge')
    if kind=='eccmi':
        typ,i,j,z,r=row[2:]
        if typ=='bb':
            if not 0<=i<j<b or z<0 or z>full or z&((1<<i)|(1<<j)) or not 0<=r<=k:raise ValueError('EC_CMI_BB')
            return out([(z|1<<i,r,1),(z|1<<j,r,1),(z|1<<i|1<<j,r,-1),(z,r,-1)],'ge')
        if typ=='bc':
            if not 0<=i<b or j!=-1 or z<0 or z>full or z&(1<<i) or not 0<=r<k:raise ValueError('EC_CMI_BC')
            return out([(z|1<<i,r,1),(z,r+1,1),(z|1<<i,r+1,-1),(z,r,-1)],'ge')
        if typ=='cc':
            if i!=-1 or j!=-2 or z<0 or z>full or not 0<=r<=k-2:raise ValueError('EC_CMI_CC')
            return out([(z,r+1,2),(z,r+2,-1),(z,r,-1)],'ge')
        raise ValueError('EC_CMI_TYPE')
    if kind=='ecfirstcopy':
        u=row[2]
        if u<0 or u&~T2:raise ValueError('EC_FIRST_SUBSET')
        return out([(u|c0,0,1),(u|2,0,-1)])
    if kind=='ecfirstind':return out([(E,0,1),(T2,0,1),(1023,0,-1),(T2|c0,0,-1)])
    if kind=='ecblockcopy':
        u,r=row[2:]
        if u<0 or u&~Y or not 0<=r<k:raise ValueError('EC_BLOCK_SUBSET')
        return out([(u,r+1,1),(u|8,r,-1)])
    if kind=='ecblockind':
        r=row[2]
        if not 0<=r<k:raise ValueError('EC_BLOCK_INDEX')
        return out([(E,r+1,1),(Y,r,1),(E,r,-1),(Y,r+1,-1)])
    if kind=='ectailcopy':
        if not tail:raise ValueError('EC_NO_TAIL')
        u,r=row[2:]
        if u<0 or u&~Yt or not 0<=r<=k:raise ValueError('EC_TAIL_SUBSET')
        return out([(u|d,r,1),(u|2,r,-1)])
    if kind=='ectailind':
        if not tail:raise ValueError('EC_NO_TAIL')
        return out([(full,k,1),(Yt,k,1),(E,k,-1),(Yt|d,k,-1)])
    raise ValueError(('EC_ROW',kind))

def check(cert,verified):
    specs=compile_specs(cert);legacy.set_extra(cert.get('extra_single_copies'));legacy.set_programs(cert.get('programs'))
    acc={};bound=Fraction();used=set()
    for item in cert['multipliers']:
        row=item['row'];w=Fraction(item['multiplier'])
        if row[0] in ('dfz','dfzb'):
            t=tuple(row[1] if row[0]=='dfz' else row[2])
            if t not in verified:raise ValueError('UNVERIFIED_DFZ')
            used.add(t)
        ts,kind=terms(row,specs)
        if kind=='ge' and w>0:raise ValueError('SIGN')
        if kind=='cap':
            if w<0:raise ValueError('CAP_SIGN')
            bound+=w
        for key,c in ts:
            if key is not None:acc[key]=acc.get(key,Fraction())+w*c
    if {key:w for key,w in acc.items() if w}!={('o',1023):Fraction(1)}:raise ValueError('IDENTITY')
    if bound!=Fraction(cert['bound']):raise ValueError('BOUND_CLAIM')
    return bound,used

def main():
    raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('CERT_HASH')
    cert=json.loads(raw);verified=set();deps=[]
    for p,h in zip(sys.argv[4::2],sys.argv[5::2]):
        vr=(ROOT/p).read_bytes()
        if sha256(vr).hexdigest()!=h:raise ValueError('VERIFY_HASH')
        verified.update(tuple(r['coefficients']) for r in json.loads(vr)['results'] if r['valid_exact']);deps.append({'path':p,'sha256':h})
    bound,used=check(cert,verified);controls={}
    def reject(name,c,v=verified):
        try:check(c,v)
        except (ValueError,KeyError,IndexError) as e:controls[name]=str(e)
        else:raise ValueError(('CONTROL_NOT_REJECTED',name))
    ei=next(i for i,m in enumerate(cert['multipliers']) if m['row'][0]=='eccmi')
    c=deepcopy(cert);c['multipliers'][ei]['multiplier']=str(-Fraction(c['multipliers'][ei]['multiplier']));reject('flipped_compressed_cmi_sign',c)
    c=deepcopy(cert);c['multipliers'][ei]['row'][-1]=-1;reject('negative_copy_count',c)
    c=deepcopy(cert);c['multipliers'][ei]['multiplier']=str(2*Fraction(c['multipliers'][ei]['multiplier']));reject('changed_compressed_cmi_weight',c)
    c=deepcopy(cert);ci=next(i for i,m in enumerate(c['multipliers']) if m['row'][0]=='cap');c['multipliers'][ci]['multiplier']=str(2*Fraction(c['multipliers'][ci]['multiplier']));reject('changed_cap_weight',c)
    c=deepcopy(cert);c['bound']=str(bound+1);reject('changed_reported_bound',c)
    if used:reject('dropped_dfz_receipt',cert,verified-{next(iter(used))})
    rep={'certificate_sha256':sys.argv[3],'legacy_checker_sha256':BASE_SHA,'dfz_dependencies':deps,'all_checked':True,'bound':str(bound),'bound_float':float(bound),
         'rows':len(cert['multipliers']),'row_kinds':{k:sum(m['row'][0]==k for m in cert['multipliers']) for k in sorted({m['row'][0] for m in cert['multipliers']})},
         'dfz_tuples_used':[list(t) for t in sorted(used)],'negative_controls':controls,
         'limits':'Exact Fraction coefficient identity, row syntax, signs and bound. Validity of auxiliary exchangeability requires the written conditional-kernel proof; no formal, cross-model or novelty review.'}
    with open(ROOT/sys.argv[1],'x') as f:json.dump(rep,f,indent=1);f.write('\n')
    print(json.dumps(rep,indent=1))
if __name__=='__main__':main()
