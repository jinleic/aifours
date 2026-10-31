#!/usr/bin/env python3
"""Exercise actual owner Gram/objective/equality aggregation under modular data.

Intercept all 17 Gram, one objective and every equality-part full-word tensor
from the pinned unmodified owner main with in-memory rational residues mod p.
Compare Gram to prior per-type references, objective to independent cycle
formula and equality to independent literal-index per-lambda contractions.
Stop before the original result write. This is not full coefficient identity.
"""
import collections
import hashlib
import importlib.util
import json
import math
import sys
import time
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
G=ROOT/'frontier-20261028-independent-d4-global-identity-check.py'
D=ROOT/'frontier-20261028-d4-grouped-versus-per-type-contraction-check.py'
R=ROOT/'frontier-20261028-d4-grouped-versus-per-type-contraction-check-results.json'
E=ROOT/'frontier-20261028-d4-owner-literal-equality-map-check.py'
O=ROOT/'frontier-20261028-d4-owner-objective-cycle-check.py'
PINS={G:'b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d',
      D:'68e226dd6888b26d33364b0f6ce56e38a4a04b34da3f828c830ffec4a8efb6bc',
      R:'0c93b7316404981a4395bdc43f8925052d23d616e8b2d26624a3480b103a877a',
      E:'f3b5cbe975cf0844bc4206191143682ee0ae2d7d5247a4f2616d9cf2b45e8421',
      O:'e84a463dce2e313cbfd8daaa2bbe42f278ca96b02299efbb6f7978c0b9133f6c'}
OUT=ROOT/'frontier-20261028-d4-actual-owner-full-aggregation-check-results.json'
P=65521;DEN=2**31

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def rat(num,den):
    d=int(den)%P
    if not d:raise ValueError('denominator divides modulus')
    return (int(num)%P)*pow(d,-1,P)%P

class FinishedAll(Exception):pass


def independent_eq(pkg,part,items,eq,diag):
    values=[]
    for which in range(2):
        vectors=[]
        for axis,spec in enumerate(part['local']):
            w=diag.weights(which,axis,P);column=[]
            for mk in spec[4]:
                rows=eq.rows_for(pkg,spec,mk)
                for i in range(len(rows[0])):
                    column.append(sum(int(w[j])*rows[j][i] for j in range(24))%P)
            vectors.append(column)
        total=0
        for item in items:
            value=rat(item['numerator'],item['denominator'])
            if len(item['index'])!=4:raise ValueError('wrong equality index length')
            for axis,index in enumerate(item['index']):value=value*vectors[axis][index]%P
            total=(total+value)%P
        values.append(total)
    return values


def independent_objective(obj,diag):
    perms=obj.PERMS;tau=obj.TAU
    site=[2*4**obj.cycles(p)-4**obj.cycles(tuple(tau[p[j]] for j in range(4))) for p in perms]
    aux=[2**obj.cycles(tuple(tau[p[j]] for j in range(4))) for p in perms]
    out=[]
    for which in range(2):
        z=1
        for axis in range(4):
            w=diag.weights(which,axis,P);seq=aux if axis==3 else site
            z=z*sum(int(w[j])*seq[j] for j in range(24))%P
        out.append(z*pow(DEN,-1,P)%P)
    return out


def main():
    st=time.monotonic();sys.set_int_max_str_digits(0)
    if any(sha(k)!=v for k,v in PINS.items()):raise ValueError('pinned helper mismatch')
    if any(P%d==0 for d in range(2,math.isqrt(P)+1)):raise ValueError('nonprime modulus')
    direct=json.loads(R.read_text())
    if direct['verdict']!='PASS' or direct['prime']!=P or direct['row_pattern_groups']!=17:raise ValueError('bad Gram reference')
    diag=load('weight_and_projection',D);eq=load('literal_equality_reference',E);obj=load('cycle_objective_reference',O)
    g=load('actual_owner_code',G);pkg,corr=g.load_data()
    groups={}
    for ti,t in enumerate(pkg['types']):
        for r,a in enumerate(t['rows']):
            for s,b in enumerate(t['rows']):
                f,kp,lp=g.literal_rule(a,b);cut=t['modules'][0].split('|')[1]
                groups.setdefault((f,kp,lp,cut),[]).append((ti,r,s))
    ordered=sorted(groups.items(),key=lambda z:str(z[0]))
    if len(ordered)!=17 or len(direct['groups'])!=17:raise ValueError('unexpected Gram groups')
    for ((key,items),v) in zip(ordered,direct['groups']):
        if key[0]!=v['family'] or len(items)!=v['type_row_pairs'] or not v['match']:raise ValueError('Gram reference order mismatch')
    lam_bygroup=collections.defaultdict(list)
    for item in corr['equality_coefficients']:lam_bygroup[item['group']].append(item)
    eq_expected=[]
    for name,group in pkg['eq_groups'].items():
        for part in group['parts']:
            eq_expected.append({'group':name,'family':part['family'],'sign':-int(part['sign']),
                                'lambda_count':len(lam_bygroup[name]),
                                'direct':independent_eq(pkg,part,lam_bygroup[name],eq,diag)})
    objective=independent_objective(obj,diag)
    if len(eq_expected)!=7:raise ValueError('unexpected equality part count')
    for matrix in corr['matrices']:
        for pair in matrix['values']:pair[0]=str(rat(pair[0],pair[1]));pair[1]='1'
    for item in corr['equality_coefficients']:
        item['numerator']=str(rat(item['numerator'],item['denominator']));item['denominator']='1'
    g.load_data=lambda:(pkg,corr)
    g.OUT=ROOT/'frontier-20261028-unused-full-stop-before-output.json'
    reports=[];family_ids={};ids_family={};fault=False;dinv=pow(DEN,-1,P)
    def capture(acc,oid,arr,sign):
        nonlocal fault
        j=len(reports)
        if j<17:
            kind='gram';family=ordered[j][0][0];expected_sign=-1;reference=direct['groups'][j]['direct'];name='gram-'+str(j+1)
        elif j==17:
            kind='objective';family='31';expected_sign=1;reference=objective;name='objective'
        else:
            q=j-18
            if q>=len(eq_expected):raise ValueError('unexpected extra callback')
            e=eq_expected[q];kind='equality';family=e['family'];expected_sign=e['sign'];reference=e['direct'];name=e['group']
        if sign!=expected_sign or arr.shape!=(24,24,24,24):raise ValueError('callback sign/shape mismatch')
        ident=id(acc)
        if family in family_ids and family_ids[family]!=ident:raise ValueError('family accumulator switched')
        if ident in ids_family and ids_family[ident]!=family:raise ValueError('family accumulator collision')
        family_ids[family]=ident;ids_family[ident]=family
        vals=np.fromiter((int(v)%P for v in arr.ravel()),dtype=np.int64,count=24**4).reshape((24,)*4)
        actual=[]
        for which in range(2):
            vectors=[diag.weights(which,axis,P) for axis in range(4)]
            val=diag.projection(vals,vectors,P)*dinv%P;actual.append(val)
            if kind=='equality' and not fault:
                bad=vals.copy();bad[(0,0,0,0)]=(int(bad[(0,0,0,0)])+1)%P
                fault=(diag.projection(bad,vectors,P)*dinv%P)!=val
        reports.append({'kind':kind,'name':name,'family':family,'sign':sign,'actual_owner':actual,'independent_reference':reference,'match':actual==reference})
        print('owner callback',j+1,kind,name,'match',actual==reference,'elapsed',round(time.monotonic()-st,2),flush=True)
        if len(reports)==18+len(eq_expected):raise FinishedAll()
    g.add_orbits=capture
    try:g.main()
    except FinishedAll:pass
    else:raise ValueError('owner did not stop at final expected callback')
    if any(sha(k)!=v for k,v in PINS.items()):raise ValueError('pinned helper changed during check')
    counts=collections.Counter(x['kind'] for x in reports)
    ok=counts=={'gram':17,'objective':1,'equality':7} and all(x['match'] for x in reports) and fault
    out={'kind':'actual_pinned_owner_full_aggregation_weighted_projection_audit',
         'owner_checker_sha256':PINS[G],'per_type_reference_sha256':PINS[R],
         'independent_equality_script_sha256':PINS[E],'independent_objective_script_sha256':PINS[O],
         'archive_sha256':g.EXPECTED_ARCHIVE,'corrected_data_sha256':g.EXPECTED_CORRECTED,
         'prime':P,'prime_trial_division':'PASS','source_denominator':DEN,
         'callbacks':dict(counts),'equality_parts':eq_expected,'results':reports,
         'equality_tensor_entry_fault_detected':fault,'elapsed_seconds':round(time.monotonic()-st,3),
         'method':'Run pinned actual owner main with in-memory Z/lambda reduced modulo p, intercept all full-word group tensors before orbit accumulation, and compare two source-word projections to independently arranged per-type Gram, literal equality and cycle objective contractions.',
         'scope':'Two finite modular projections of actual Gram/objective/equality aggregation code, not full rational identity, corrected PSD, a physical target-state sample, formal-kernel or independent-model-family review.',
         'verdict':'PASS' if ok else 'FAIL'}
    OUT.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps(out,sort_keys=True,indent=2));return 0 if ok else 1


if __name__=='__main__':raise SystemExit(main())
