#!/usr/bin/env python3
"""Diagnostic LP with explicit cell-width relaxation; NOT a certificate."""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix, vstack
from screen_fourier import data, call_gaps


def probe(amplitude, nbin, half_range, regressions):
    edges=np.linspace(-half_range,half_range,nbin+1)
    x,p,m,xx,weights,f=data({0:1,4:1j*amplitude},edges,order=40)
    n=len(x)
    rows=[]; cols=[]; vals=[]
    for i in range(n):
        for j in range(n):
            for row,value in ((i,1),(n+j,1),(2*n+i,x[j]),(3*n+j,x[i])):
                rows.append(row);cols.append(i*n+j);vals.append(value)
    a=coo_matrix((vals,(rows,cols)),shape=(4*n,n*n)).tocsr()
    # Exact marginal masses; moment coordinates are allowed their full bin errors.
    eq=a[:2*n]; eq_b=np.r_[p,p]
    moment=a[2*n:3*n] if regressions=='IF' else a[2*n:]
    rhs=m if regressions=='IF' else np.r_[m,-m]
    tol=(half_range/nbin+1e-8)*(p if regressions=='IF' else np.r_[p,p])
    result=linprog(np.zeros(n*n),A_eq=eq,b_eq=eq_b,
                   A_ub=vstack((moment,-moment)),b_ub=np.r_[rhs+tol,-rhs+tol],
                   method='highs',options={'time_limit':30,
                       'primal_feasibility_tolerance':1e-9,
                       'dual_feasibility_tolerance':1e-9})
    return {'amplitude':amplitude,'nbin':nbin,'half_range':half_range,
            'regressions':regressions,'status':int(result.status),
            'message':result.message,'sample_call_gap':call_gaps(xx,weights,f)[0],
            'discarded_mass_estimate':float(1-sum(p)),
            'bin_error_allowance':half_range/nbin}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();results=[]
    for amp in (0.03,0.1,0.2,0.35):
        for mode in ('IF','joint'):
            for n in (40,80):
                row=probe(amp,n,5,mode);results.append(row)
                print(json.dumps(row),flush=True)
                args.output.write_text(json.dumps({'status':'EXPLORATORY_ONLY',
                    'rows':results},indent=2)+'\n')
