#!/usr/bin/env python3
"""Bounded numerical falsification screen, NOT a mathematical certificate.

Fourier-invariant Hermite superpositions have mu=nu and GD=-IF. We screen
both one-sided call inequalities, then a binned joint-regression LP. A failed
LP is only a lead: discretization can create false infeasibility.
"""
import argparse
import json
import math
from pathlib import Path
import time
import numpy as np
from scipy.special import eval_hermite
from scipy.optimize import linprog
from scipy.sparse import coo_matrix, vstack
from numpy.polynomial.legendre import leggauss


def hermite(n, x):
    return (np.pi ** -0.25 * np.exp(-x*x/2) * eval_hermite(n, x)
            / np.sqrt(float(2**n * math.factorial(n))))


def data(coeff, edges, order=20):
    z, w = leggauss(order)
    centers = (edges[:-1] + edges[1:])/2
    half = np.diff(edges)/2
    x = centers[:, None] + half[:, None]*z[None, :]
    weight = half[:, None]*w[None, :]
    q = np.zeros_like(x, dtype=complex)
    dq = np.zeros_like(x, dtype=complex)
    for n, c in coeff.items():
        hn = hermite(n, x)
        q += c*hn
        dq += c*((np.sqrt(2*n)*hermite(n-1, x) if n else 0)-x*hn)
    energy = sum(abs(c)**2 for c in coeff.values())
    rho = abs(q)**2/energy
    current = np.imag(np.conj(q)*dq)/energy
    f = np.divide(current, rho, out=np.zeros_like(current), where=rho>1e-300)
    mass = np.sum(weight*rho, axis=1)
    moment = np.sum(weight*current, axis=1)
    return centers, mass, moment, x.ravel(), (weight*rho).ravel(), f.ravel()


def call_gaps(x, mass, f):
    # Both laws symmetric for the selected even Hermite families.
    grid = np.linspace(0, max(5, np.max(abs(f))), 401)
    gaps = np.array([np.sum(np.maximum(x-k, 0)*mass)
                     -np.sum(np.maximum(f-k, 0)*mass) for k in grid])
    idx = np.argmin(gaps)
    return float(gaps[idx]), float(grid[idx]), float(np.max(abs(f)))


def joint_lp(x, mass, moments):
    n = len(x)
    rows, cols, values = [], [], []
    for i in range(n):
        for j in range(n):
            col = i*n+j
            for row, value in ((i,1),(n+j,1),(2*n+i,x[j]),(3*n+j,x[i])):
                rows.append(row); cols.append(col); values.append(value)
    a = coo_matrix((values, (rows, cols)), shape=(4*n,n*n)).tocsr()
    b = np.concatenate((mass,mass,moments,-moments))
    tolerance = np.concatenate((np.full(2*n,1e-10), np.full(2*n,1e-8)))
    result = linprog(np.zeros(n*n), A_ub=vstack((a,-a)),
                     b_ub=np.concatenate((b+tolerance,-b+tolerance)),
                     bounds=(0,None),method='highs',options={'time_limit':20})
    return {'status':int(result.status),'message':result.message}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    started=time.monotonic()
    rows=[]
    edges=np.linspace(-7,7,81)
    for n in (4,8,12):
        for amplitude in (0.03,0.1,0.2,0.35,0.5,0.7,1,1.5,2,3,5,10):
            coeff={0:1, n:1j*amplitude}
            x,p,m,xx,weights,f=data(coeff,edges)
            gap,k,mx=call_gaps(xx,weights,f)
            row={'n':n,'imaginary_amplitude':amplitude,
                 'sample_min_call_gap':gap,'min_call_strike':k,
                 'sample_max_abs_IF':mx,'truncated_mass':float(sum(p)),
                 'binned_cross_moment':float(x@m)}
            if gap>=-1e-7:
                row['joint_lp']=joint_lp(x,p,m)
            rows.append(row)
            args.output.write_text(json.dumps({'status':'EXPLORATORY_ONLY',
                'seconds':time.monotonic()-started,'rows':rows},indent=2)+'\n')
            print(json.dumps(row),flush=True)


if __name__=='__main__':
    main()
