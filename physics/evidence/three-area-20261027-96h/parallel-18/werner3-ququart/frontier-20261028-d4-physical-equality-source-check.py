#!/usr/bin/env python3
"""Audit actual d4 equality metadata against original physical moment factors.

The mathematical stiefel identity is written separately. This checks that each
actual group uses an a replica, or that the two signed same-pair marginals leave
the identical ordered letter word, with whole-replica-compatible local specs;
checks every corrected lambda coordinate against every associated part; and
rejects deliberate metadata faults. No target state is chosen.
"""
import collections
import copy
import hashlib
import importlib.util
import json
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
GLOBAL=ROOT/'frontier-20261028-independent-d4-global-identity-check.py'
EXPECT='b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d'
OUT=ROOT/'frontier-20261028-d4-physical-equality-source-check-results.json'
LETTERS={'31':'aaab','22':'aabb','13':'bbba'}

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load():
    if sha(GLOBAL)!=EXPECT:raise ValueError('global helper hash mismatch')
    sp=importlib.util.spec_from_file_location('global_equality_ref',GLOBAL)
    g=importlib.util.module_from_spec(sp);sp.loader.exec_module(g)
    pkg,corr=g.load_data()
    return g,pkg,corr

def decode_site_label(key):
    f,l,r=key.split('|')[-1].split('_')
    return (int(f[1:]),() if l=='e' else tuple(map(int,l)),() if r=='e' else tuple(map(int,r)))

def local_dim(pkg,spec):
    side,slot,order,kind,mkeys=spec
    total=0
    for mk in mkeys:
        if side=='S':
            _,mat=pkg['diagrams'][(3,())][decode_site_label(mk)]
        elif side=='A':mat=pkg['aux'][mk]
        else:raise ValueError('bad side')
        if not mat or not mat[0] or any(len(row)!=len(mat[0]) for row in mat):raise ValueError('bad compression')
        total+=len(mat[0])**2
    return total

def part_info(pkg,part,stiefel):
    if part['family'] not in LETTERS or part['sign'] not in (-1,1):raise ValueError('bad family/sign')
    local=part['local']
    if len(local)!=4 or [a[0] for a in local]!=['S','S','S','A']:raise ValueError('wrong factors')
    slot=local[0][1];order=tuple(local[0][2])
    if not isinstance(slot,int) or slot not in range(4):raise ValueError('bad slot')
    if sorted(order)!=[i for i in range(4) if i!=slot]:raise ValueError('bad surviving order')
    if any(x[1]!=slot or tuple(x[2])!=order for x in local):raise ValueError('non-whole-replica deletion')
    if any(x[3]!='del' for x in local[:3]):raise ValueError('bad site operation')
    if local[3][3]!=('stiefel_aux' if stiefel else 'del'):raise ValueError('bad auxiliary operation')
    surviving=''.join(LETTERS[part['family']][i] for i in order)
    return {'family':part['family'],'sign':part['sign'],'slot':slot,'order':list(order),
            'deleted_letter':LETTERS[part['family']][slot],'surviving_word':surviving,
            'dimensions':[local_dim(pkg,x) for x in local]}

def validate_group(pkg,name,parts):
    stiefel=name.startswith('stiefel')
    infos=[part_info(pkg,p,stiefel) for p in parts]
    if stiefel:
        if len(infos)!=1 or infos[0]['deleted_letter']!='a' or infos[0]['sign']!=1:
            raise ValueError('Stiefel must act on a replica')
    else:
        if len(infos)!=2 or infos[0]['sign']+infos[1]['sign']!=0:
            raise ValueError('marginal requires opposite signs')
        if infos[0]['surviving_word']!=infos[1]['surviving_word']:
            raise ValueError('different ordered surviving physical factors')
        if infos[0]['dimensions']!=infos[1]['dimensions']:
            raise ValueError('different compressed equality coordinates')
        if any(tuple(a[4])!=tuple(b[4]) for a,b in zip(parts[0]['local'],parts[1]['local'])):
            raise ValueError('different actual compression modules across equal marginals')
    return infos

def coordinate_valid(idx,dims):
    return len(idx)==4 and all(type(i)==int and 0<=i<d for i,d in zip(idx,dims))

def main():
    st=time.monotonic();g,pkg,corr=load()
    groups=pkg['eq_groups'];expected={'stiefel31','stiefel22','stiefel13','aab','abb'}
    if set(groups)!=expected:raise ValueError('unexpected group set')
    info={name:validate_group(pkg,name,group['parts']) for name,group in groups.items()}
    bygroup=collections.Counter();bad=[]
    for item in corr['equality_coefficients']:
        name=item['group'];idx=item['index'];bygroup[name]+=1
        if name not in info or any(not coordinate_valid(idx,part['dimensions']) for part in info[name]):
            bad.append({'group':name,'index':idx})
    # Four intentionally faulty metadata choices; none rewrites source bytes.
    bad_order=copy.deepcopy(groups['abb']['parts']);
    bad_order[1]['local']=[list(spec) for spec in bad_order[1]['local']]
    for spec in bad_order[1]['local']:spec[2]=(0,2,3)
    bad_stiefel=copy.deepcopy(groups['stiefel13']['parts']);
    bad_stiefel[0]['local']=[list(spec) for spec in bad_stiefel[0]['local']]
    for spec in bad_stiefel[0]['local']:spec[1]=0;spec[2]=(1,2,3)
    bad_sign=copy.deepcopy(groups['aab']['parts']);bad_sign[1]['sign']=bad_sign[0]['sign']
    controls={}
    for name,data in [('abb_wrong_order',bad_order),('stiefel_b_replica',bad_stiefel),('same_marginal_sign',bad_sign)]:
        try:validate_group(pkg,'stiefel13' if name=='stiefel_b_replica' else ('abb' if name=='abb_wrong_order' else 'aab'),data)
        except ValueError:controls[name]=True
        else:controls[name]=False
    valid_aab=next(item['index'] for item in corr['equality_coefficients'] if item['group']=='aab')
    bad_index=list(valid_aab);bad_index[0]=info['aab'][0]['dimensions'][0]
    controls['out_of_range_lambda']=not coordinate_valid(bad_index,info['aab'][0]['dimensions'])
    if sha(GLOBAL)!=EXPECT:raise ValueError('global helper changed')
    r={'kind':'all_d4_physical_equality_source_binding',
       'archive_sha256':g.EXPECTED_ARCHIVE,'source_certificate_sha256':g.EXPECTED_CERT,
       'corrected_data_sha256':g.EXPECTED_CORRECTED,'reference_global_helper_sha256':EXPECT,
       'groups':info,'corrected_lambda_count':len(corr['equality_coefficients']),
       'corrected_lambda_counts_by_group':dict(bygroup),'invalid_lambda_coordinates':bad,
       'intentional_metadata_faults_detected':controls,
       'method':'Derive each surviving physical family word from actual family/slot/order; enforce whole-replica source specs and exact signs; check all corrected lambda indices against every part compression shape.',
       'scope':'Complete d4 equality-source metadata and coordinate binding. The Stiefel/marginal physical equalities are written proofs, not inferred from names; local compression values, global identity and PSD are separate.',
       'elapsed_seconds':round(time.monotonic()-st,3),
       'verdict':'PASS' if not bad and all(controls.values()) else 'FAIL'}
    OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print(json.dumps(r,sort_keys=True,indent=2));return 0 if r['verdict']=='PASS' else 1


if __name__=='__main__':raise SystemExit(main())
