#!/usr/bin/env python3
"""Add valid original-variable copy-family cuts to the 1920-row source core.

Sparse relaxation includes every original Shannon inequality and graph/symmetry
constraint, plus exactly the source certificate's 1920 checked rows. Results
are floating-point proposals; exact rational proof must be generated separately.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import hashlib
import json
import sys
import time
import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy


def load(name, filename):
    spec=spec_from_file_location(name,ROOT/filename)
    module=module_from_spec(spec); spec.loader.exec_module(module)
    return module

cert = load('strict_cert','frontier-20261028-gurpinar-certificate-independent.py')
cut = load('cut_search','frontier-20261028-copy-family-cutting-plane.py')
base = cut.base
OUTPUT=ROOT/'frontier-20261028-sparse-certificate-cutting-result.json'
MAX_ROUNDS=6
TIME_LIMIT=25.0
MAX_CUTS=1000


def sets_from_mask(mask):
    return tuple(cert.BASE[i] for i in range(10) if (mask>>i)&1)


def fn_row(meta):
    n=meta['n']; a=meta['A_mask']; b=meta['B_mask']; c=meta['C_mask']; d=meta['D_mask']; z=meta['condition_mask']
    f=n*(n+1)//2
    terms=(base.cmi(a,b,c|z,n+1)+base.cmi(a,b,d|z,n)+base.cmi(c,d,z,n)
           +base.cmi(a,b,z,-n)+base.cmi(a,c,b|z,f)+base.cmi(b,c,a|z,f))
    return cert.vector([(set(sets_from_mask(mask)),coef) for mask,coef in terms])


def build_constraints(source_rows, extras):
    inf=highspy.kHighsInf
    rows=[]
    def add(terms,lo,hi,meta):
        if terms:
            rows.append((terms,lo,hi,meta))
    for index,row in enumerate(source_rows,1):
        lo,hi=({'=':(0.0,0.0),'>=':(0.0,inf),'<=':(-inf,1.0)})[row['relation']]
        add(row['terms'],lo,hi,{'kind':'source','index':index,'name':row['name']})
    full=(1<<10)-1
    for i in range(10):
        add(cert.vector([(set(cert.BASE),1),(set(sets_from_mask(full^(1<<i))),-1)]),0,inf,
            {'kind':'Hconditional','i':i+1})
    for i,j in combinations(range(10),2):
        rest=full^(1<<i)^(1<<j); z=rest
        while True:
            a,b=1<<i,1<<j
            terms=cert.vector([(set(sets_from_mask(mask)),coef) for mask,coef in base.cmi(a,b,z)])
            add(terms,0,inf,{'kind':'CMI','i':i+1,'j':j+1,'condition_mask':z})
            if z==0:break
            z=(z-1)&rest
    for v,ns in base.NEIGHBOURS.items():
        N=set(cert.BASE[u-1] for u in ns)
        add(cert.vector([(N|{cert.BASE[v-1]},1),(N,-1)]),0,0,{'kind':'FD','vertex':v})
    for perm in base.GENERATORS:
        for mask in range(1,full+1):
            mapped=base.permute_mask(mask,perm)
            if mapped!=mask:
                add(cert.vector([(set(sets_from_mask(mask)),1),(set(sets_from_mask(mapped)),-1)]),0,0,
                    {'kind':'symmetry','mask':mask,'mapped':mapped})
    for meta in extras:
        add(fn_row(meta),0,inf,meta)
    return rows


from itertools import combinations


def solve(source_rows,extras):
    rows=build_constraints(source_rows,extras)
    keys={tuple(sets_from_mask(mask)) for mask in range(1,1024)}
    for terms,_,_,_ in rows: keys.update(terms)
    keys=sorted(keys,key=lambda x:(len(x),x)); cols={key:i for i,key in enumerate(keys)}
    starts=[]; inds=[]; vals=[]; lo=[]; hi=[]
    for terms,l,u,_ in rows:
        starts.append(len(inds))
        for key,value in terms.items():
            inds.append(cols[key]); vals.append(float(value))
        lo.append(l); hi.append(u)
    n=len(keys); lower=np.zeros(n); upper=np.full(n,highspy.kHighsInf)
    for v in cert.BASE:upper[cols[(v,)]]=1.0
    cost=np.zeros(n); cost[cols[tuple(cert.BASE)]]=1
    lp=highspy.HighsLp(); lp.num_col_=n; lp.num_row_=len(rows)
    lp.col_cost_,lp.col_lower_,lp.col_upper_=cost,lower,upper
    lp.row_lower_,lp.row_upper_=np.array(lo),np.array(hi)
    lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(inds)],dtype=np.int32)
    lp.a_matrix_.index_=np.array(inds,dtype=np.int32)
    lp.a_matrix_.value_=np.array(vals,dtype=float)
    lp.sense_=highspy.ObjSense.kMaximize
    solver=highspy.Highs(); solver.silent(); solver.setOptionValue('threads',1)
    solver.setOptionValue('time_limit',TIME_LIMIT); solver.passModel(lp)
    t=time.monotonic(); solver.run(); elapsed=time.monotonic()-t
    status=solver.modelStatusToString(solver.getModelStatus()); sol=solver.getSolution()
    result={'status':status,'objective_float_unverified':float(solver.getInfo().objective_function_value),
            'rows':len(rows),'columns':n,'nnz':len(inds),'solve_elapsed_s':elapsed}
    if status!='Optimal': return result,None
    result['nonzero_source_duals_float']=[{'row':meta['index'],'name':meta['name'],'dual':float(value)}
        for (_,_,_,meta),value in zip(rows,sol.row_dual) if meta['kind']=='source' and abs(float(value))>1e-9]
    result['nonzero_extra_duals_float']=[{'metadata':meta,'dual':float(value)}
        for (_,_,_,meta),value in zip(rows,sol.row_dual) if meta['kind']=='copy-family' and abs(float(value))>1e-9]
    base_h=[0.0]+[sol.col_value[cols[tuple(sets_from_mask(mask))]] for mask in range(1,1024)]
    return result,base_h


def main():
    t0=time.monotonic()
    data={key:(ROOT/info[0]).read_bytes() for key,info in cert.FILES.items()}
    for key,(_,expected) in cert.FILES.items():cert.pin(key,data[key],expected)
    source=cert.parse_input(data['layout'],data['text'])
    group=base.automorphism_group(); orbit,reps=base.canonical_orbits(group)
    candidate=json.loads(base.INPUT.read_bytes())
    sample=base.sample_sym_entropy(group,orbit,reps,candidate)
    extras=[]; known=set(); rounds=[]
    for i in range(MAX_ROUNDS):
        r,h=solve(source,extras); r['round']=i
        if h is None:
            r['stop']='LP not optimal'; rounds.append(r); break
        primal=[h[mask] for mask in reps]
        t=time.monotonic(); count,violations=cut.scan(primal,orbit,known)
        selected=sorted(violations.items(),key=lambda x:x[1][0])[:MAX_CUTS]
        r.update({'expanded_substitutions_checked':count,'unique_violated_rows':len(violations),
                  'most_negative_slack_float':min((x[0] for x in violations.values()),default=0.0),
                  'scan_elapsed_s':time.monotonic()-t,'cuts_added':len(selected)})
        for key,(slack,meta) in selected:
            assert sum(coef*sample[col] for col,coef in key)>-1e-8
            known.add(key); extras.append(meta)
        rounds.append(r)
        if not selected:break
    out={'pinned_source_hashes':{k:v[1] for k,v in cert.FILES.items()},
         'base_module_sha256':hashlib.sha256((ROOT/'frontier-20261028-copy-family-upper-lp.py').read_bytes()).hexdigest(),
         'source_certificate_rows':len(source),'group_size':len(group),
         'max_rounds':MAX_ROUNDS,'solver_time_limit_s':TIME_LIMIT,'solver_threads':1,
         'added_cuts':extras,'rounds':rounds,'total_elapsed_s':time.monotonic()-t0,
         'limits':'Floating LP search only. Even an improved objective needs a valid exact dual identity and separate review; no conclusion from a timeout or solver status alone.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:
        json.dump(out,stream,indent=2); stream.write('\n')
    print(json.dumps([{k:v for k,v in r.items() if not k.startswith('nonzero_')} for r in rounds],indent=2))
    print('source_rows',len(source),'total_elapsed_s',out['total_elapsed_s'])


if __name__=='__main__':main()
