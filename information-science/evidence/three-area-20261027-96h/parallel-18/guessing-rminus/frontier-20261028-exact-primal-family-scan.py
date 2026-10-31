#!/usr/bin/env python3
"""Try to reconstruct an exact source-core LP point and separate all copy F_n.

The point is a polymatroid/copy relaxation witness, NOT an entropic law. It is
accepted only if every included row, FD, cap, and the objective check exactly.
A full all-block scan is attempted only if a compact exact point is recovered.
"""
from fractions import Fraction
from importlib.util import module_from_spec,spec_from_file_location
from itertools import combinations
from math import lcm
from pathlib import Path
import hashlib
import json
import sys
import time

import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
spec=spec_from_file_location('sparse','frontier-20261028-sparse-certificate-cutting.py')
sparse=module_from_spec(spec);spec.loader.exec_module(sparse)
cert=sparse.cert
OUTPUT=ROOT/'frontier-20261028-exact-primal-family-scan-result.json'
PREV=ROOT/'frontier-20261028-sparse-certificate-cutting-result.json'


def solve(rows):
    keys={tuple(sparse.sets_from_mask(m)) for m in range(1,1024)}
    for terms,_,_,_ in rows:keys.update(terms)
    keys=sorted(keys,key=lambda x:(len(x),x)); col={k:i for i,k in enumerate(keys)}
    starts=[];inds=[];vals=[];lo=[];hi=[]
    for terms,a,b,_ in rows:
        starts.append(len(inds))
        for k,v in terms.items():inds.append(col[k]);vals.append(float(v))
        lo.append(a);hi.append(b)
    n=len(keys);lower=np.zeros(n);upper=np.full(n,highspy.kHighsInf)
    for v in cert.BASE:upper[col[(v,)]]=1
    cost=np.zeros(n);cost[col[tuple(cert.BASE)]]=1
    lp=highspy.HighsLp();lp.num_col_,lp.num_row_=n,len(rows)
    lp.col_cost_,lp.col_lower_,lp.col_upper_=cost,lower,upper
    lp.row_lower_,lp.row_upper_=np.array(lo),np.array(hi)
    lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(inds)],dtype=np.int32)
    lp.a_matrix_.index_=np.array(inds,dtype=np.int32);lp.a_matrix_.value_=np.array(vals)
    lp.sense_=highspy.ObjSense.kMaximize
    h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',25.0);h.passModel(lp)
    h.run();status=h.modelStatusToString(h.getModelStatus())
    if status!='Optimal':return status,keys,col,None
    return status,keys,col,h.getSolution().col_value


def check_rounding(rows,keys,col,vals,maxden):
    x=[Fraction(float(v)).limit_denominator(maxden) for v in vals]
    bad=[]
    for i,value in enumerate(x):
        if value<0:bad.append({'kind':'negative','column':i,'value':str(value)})
    for v in cert.BASE:
        if x[col[(v,)]]>1:bad.append({'kind':'cap','vertex':v,'value':str(x[col[(v,)]])})
    for i,(terms,lo,hi,meta) in enumerate(rows):
        val=sum((x[col[key]]*coefficient for key,coefficient in terms.items()),Fraction())
        if lo!=-highspy.kHighsInf and val<Fraction(int(lo)):
            bad.append({'kind':'lower','index':i,'meta':meta,'value':str(val)})
        if hi!=highspy.kHighsInf and val>Fraction(int(hi)):
            bad.append({'kind':'upper','index':i,'meta':meta,'value':str(val)})
    objective=x[col[tuple(cert.BASE)]]
    if objective!=Fraction(1847,276):bad.append({'kind':'objective','value':str(objective)})
    return x,bad


def exhaustive_all_n(h):
    """All disjoint A,B,C,D,Z partitions of ten variables, A<B; exact ints."""
    low_size=6**7
    codes=np.arange(low_size,dtype=np.int64)
    roles=[np.zeros(low_size,dtype=np.int64) for _ in range(5)]
    temp=codes.copy()
    for i in range(7):
        digit=temp%6;temp//=6
        for r in range(5):roles[r] |= np.where(digit==r+1,1<<i,0)
    count=0; min_slack=None; min_example=None
    started=time.monotonic()
    def I(a,b,z):return h[a|z]+h[b|z]-h[a|b|z]-h[z]
    for high_code in range(6**3):
        t=high_code; high=[0]*5
        for i in range(7,10):
            digit=t%6;t//=6
            if digit:high[digit-1]|=1<<i
        arrays=[roles[i]|high[i] for i in range(5)]
        mask=(arrays[0]>0)&(arrays[1]>0)&(arrays[2]>0)&(arrays[3]>0)&(arrays[0]<arrays[1])
        A,B,C,D,Z=(x[mask] for x in arrays)
        count+=len(A)
        if len(A)==0:continue
        a=I(A,B,C|Z)
        c=a+I(A,B,D|Z)+I(C,D,Z)-I(A,B,Z)
        d=I(A,C,B|Z)+I(B,C,A|Z)
        if np.any(a<0) or np.any(d<0):
            raise ValueError('negative Shannon term on exact alleged feasible point')
        if np.any((d==0)&(c<0)):
            k=int(np.flatnonzero((d==0)&(c<0))[0])
            return {'status':'VIOLATION_AT_LARGE_N','assignment_masks':[int(x[k]) for x in (A,B,C,D,Z)],
                    'a_scaled':int(a[k]),'c_scaled':int(c[k]),'d_scaled':int(d[k]),
                    'checked_before_stop':count,'elapsed_s':time.monotonic()-started}
        nz=d>0
        n=np.ones(len(A),dtype=np.int64)
        n[nz]=np.maximum(1,-np.floor_divide(c[nz],d[nz])-1)
        # Guard against overflow in exact signed-64-bit arithmetic.
        bound=int(max(np.max(np.abs(a)),np.max(np.abs(c)),np.max(np.abs(d)),1))
        nmax=int(n.max())
        if 2*bound*(nmax+1)**2 >= 2**62:
            return {'status':'INTEGER_RANGE_BLOCKER','checked_before_stop':count,'nmax':nmax,
                    'scaled_coefficient_bound':bound,'elapsed_s':time.monotonic()-started}
        twice=2*a+2*n*c+n*(n+1)*d
        k=int(np.argmin(twice)); val=int(twice[k])
        if min_slack is None or val<min_slack:
            min_slack=val;min_example={'assignment_masks':[int(x[k]) for x in (A,B,C,D,Z)],'n':int(n[k])}
        if val<0:
            return {'status':'EXACT_VIOLATION','twice_slack_scaled':val,'example':min_example,
                    'checked_before_stop':count,'elapsed_s':time.monotonic()-started}
    return {'status':'ALL_DISJOINT_BLOCK_SUBSTITUTIONS_AND_ALL_POSITIVE_N_PASS',
            'substitution_count_mod_AB_swap':count,'min_twice_slack_scaled':min_slack,
            'minimum_example':min_example,'elapsed_s':time.monotonic()-started}


def main():
    started=time.monotonic()
    data={key:(ROOT/info[0]).read_bytes() for key,info in cert.FILES.items()}
    for key,(_,expected) in cert.FILES.items():cert.pin(key,data[key],expected)
    source=cert.parse_input(data['layout'],data['text'])
    previous_raw=PREV.read_bytes();previous=json.loads(previous_raw)
    extras=previous['added_cuts']; rows=sparse.build_constraints(source,extras)
    status,keys,col,vals=solve(rows)
    result={'source_hashes':{k:v[1] for k,v in cert.FILES.items()},
            'prior_cut_result_sha256':hashlib.sha256(previous_raw).hexdigest(),
            'source_rows':len(source),'added_prior_cuts':len(extras),
            'solver_status':status,'rounding_attempts':[],
            'limits':'LP primal need not be entropic. Any all-family obstruction is only to this explicitly defined relaxation, not to an original R-minus upper bound.'}
    if vals is not None:
        chosen=None
        for maxden in (100,1000,10000,100000,1000000):
            x,bad=check_rounding(rows,keys,col,vals,maxden)
            result['rounding_attempts'].append({'max_denominator':maxden,'bad_count':len(bad),'first_bad':bad[:3]})
            if not bad:chosen=x;break
        if chosen is not None:
            result['exact_all_rows_and_objective']=True
            result['primal_values']=[{'entropy_variables':k,'value':str(chosen[i])} for i,k in enumerate(keys)]
            base_h=[Fraction(0)]+[chosen[col[tuple(sparse.sets_from_mask(m))]] for m in range(1,1024)]
            scale=lcm(*(x.denominator for x in base_h))
            result['base_integer_scale']=scale
            base_int=[int(x*scale) for x in base_h]
            if max(map(abs,base_int))<10**8:
                result['all_n_scan']=exhaustive_all_n(np.array(base_int,dtype=np.int64))
            else:
                result['all_n_scan']={'status':'INTEGER_RANGE_BLOCKER','largest_scaled_entropy':max(map(abs,base_int))}
    result['total_elapsed_s']=time.monotonic()-started
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='primal_values'},indent=2))


if __name__=='__main__':main()
