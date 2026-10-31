#!/usr/bin/env python3
"""Search for actual septic boxes without a positive-leading degree-six helper.

Auxiliary question ONLY: q of exact degree6, with q6 normalized to1, strictly
positive real against the whole original septic box. No degree-six claim is
promoted to an original degree-seven counterexample. Uses float grid LP to
scout and requires exact rational nonnegative dual weights/cancellation before
reporting any obstruction. All-member box stability still needs independent
validation; four exact Routh corner checks are supplied.
"""
import argparse
import importlib.util
import json
import time
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

HERE=Path(__file__).resolve().parent

def load(name,file):
    spec=importlib.util.spec_from_file_location(name,HERE/file)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod

base=load('boxes','frontier-20261028-box-search-v1.py')
focus=load('focused','frontier-20261028-focused-search-v1.py')


def row6(a,t):
    if t is None:
        # Coefficient of t^6 in Re[q(iw)a(-iw)] for q of degree<=6.
        return [Q(0)]*5+[Q(-1),a[6]]
    return [x*(1+t) for x in base.row_exact(a,t)[:7]]


def approximate_lp(center,cs,ts):
    tf=np.array([float(x) for x in ts])
    rows=np.vstack([base.row_float(a,tf)[:,:7]*(1+tf[:,None]) for a in cs])
    leading=[]
    for a in cs:
        r=np.zeros(7); r[5]=-1.0; r[6]=float(a[6]); leading.append(r)
    rows=np.vstack([rows,np.array(leading)])
    scale=np.array([float(x) for x in center[:6]])
    lhs=np.column_stack([-rows[:,:6]*scale,np.ones(len(rows))])
    result=linprog(np.array([0.0]*6+[-1.0]),A_ub=lhs,b_ub=rows[:,6],
                   bounds=[(None,None)]*6+[(None,1)],method='highs',
                   options={'time_limit':3.0})
    if not result.success:
        return None
    return {'margin':float(result.x[-1]),'dual':-np.asarray(result.ineqlin.marginals),
            'q':list(result.x[:6]*scale)+[1.0,0.0]}


def exact_dual(cs,ts,weights):
    total=len(cs)*len(ts)
    support=[]
    for k,w in enumerate(weights):
        if w<=1e-9:
            continue
        if k<total:
            support.append((k//len(ts),ts[k%len(ts)]))
        else:
            support.append((k-total,None))
    if not 0<len(support)<=7:
        return None
    rows=[row6(cs[i],t) for i,t in support]
    system=[[row[j] for row in rows] for j in range(6)]
    system.append([Q(1)]*len(rows))
    coeff=focus.exact_solve_unique(system,[Q(0)]*6+[Q(1)])
    if coeff is None or any(x<0 for x in coeff):
        return None
    lead=sum(c*r[6] for c,r in zip(coeff,rows))
    if lead>=0:
        return None
    return {'atoms':[{'corner':i,'t':'infinity' if t is None else str(t),'weight':str(c)}
                     for (i,t),c in zip(support,coeff) if c],
            'normalized_q6_coefficient':str(lead),
            'scope':'no degree-exactly-six numerator with positive leading coefficient can satisfy all finite strict SPR inequalities; endpoint atom uses only necessary nonnegativity'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--seed',type=int,required=True); parser.add_argument('--trials',type=int,default=1500)
    parser.add_argument('--seconds',type=float,default=60); parser.add_argument('--output',required=True)
    args=parser.parse_args()
    if not (1<=args.trials<=10000 and 0<args.seconds<=120):
        parser.error('trials1..10000 and seconds0..120')
    out=Path(args.output).open('x',encoding='utf-8'); rng=np.random.default_rng(args.seed)
    started=time.monotonic(); visited=stable=solved=0; best=None; cert=None
    try:
        for trial in range(args.trials):
            if time.monotonic()-started>=args.seconds:
                break
            visited+=1; box=base.build_box(rng)
            if box is None:
                continue
            stable+=1; center,lo,hi,cs,cols,scale=box; ts=focus.focused_grid(cs)
            result=approximate_lp(center,cs,ts)
            if result is None:
                continue
            solved+=1
            if best is None or result['margin']<best['margin']:
                best={'trial':trial,'margin':result['margin'],'grid_count':len(ts),
                      'lower':[str(x) for x in lo],'upper':[str(x) for x in hi]}
                print('best degree6 trial',trial,'grid margin',result['margin'],flush=True)
            if result['margin']<0:
                exact=exact_dual(cs,ts,result['dual'])
                if exact is not None:
                    cert={'trial':trial,'lower':[str(x) for x in lo],
                          'upper':[str(x) for x in hi],
                          'corners':[[str(x) for x in a] for a in cs],
                          'routh_first_columns':[[str(x) for x in col] for col in cols],
                          'certificate':exact,'numeric_margin':result['margin']}
                    print('EXACT DEGREE6 OBSTRUCTION trial',trial,flush=True)
                    break
        receipt={'schema':1,'seed':args.seed,'visited':visited,'exact_corner_routh_pass':stable,
                 'solved':solved,'elapsed_seconds':time.monotonic()-started,'best_numerical_lead':best,
                 'exact_degree6_obstruction':cert,
                 'scope':'Auxiliary degree6 helper question only; numerical grid not proof. Exact finite witness if present is conditional on independently certifying full box Hurwitz and on the named numerator-degree cut.'}
        json.dump(receipt,out,indent=2,sort_keys=True,allow_nan=False);out.write('\n')
        print('RESULT',json.dumps({'visited':visited,'exact_stable':stable,'solved':solved,
                                   'exact_degree6_obstruction':bool(cert),'elapsed':receipt['elapsed_seconds']}),flush=True)
    finally:
        out.close()


if __name__=='__main__':
    main()
