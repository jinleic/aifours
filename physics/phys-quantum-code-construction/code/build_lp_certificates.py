#!/usr/bin/env python3
"""Propose tiny quantum-LP witnesses, then accept them only over Fraction.

Normalized enumerators: a_i=A_i/K^2, b_i=B_i/K; n=7, d=3.
The independent verifier does not import this module or use SciPy.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json
import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
from scipy.optimize import linprog

ROOT = Path(__file__).resolve().parents[1]
N, D = 7, 3


def kraw(j, i):
    return sum((-1)**t * 3**(j-t) * comb(i, t) * comb(N-i, j-t)
               for t in range(max(0, j-N+i), min(j, i)+1))


def constraints(K):
    identity = [[int(i == j) for i in range(N+1)] for j in range(N+1)]
    mac = [[K*kraw(j, i) - 2**N*int(i == j) for i in range(N+1)]
           for j in range(N+1)]
    shadow = [[(-1)**i*kraw(j, i) for i in range(N+1)] for j in range(N+1)]
    # G*a >= 0, H*a = h. All matrix entries are integers.
    G = identity + mac[D:] + shadow
    H = [identity[0]] + mac[:D]
    h = [1] + [0]*D
    glabels = [f'a_{i}' for i in range(N+1)] + [f'KB_{i}-A_{i}' for i in range(D,N+1)] + [f'shadow_{i}' for i in range(N+1)]
    hlabels = ['a_0=1'] + [f'KB_{i}-A_{i}=0' for i in range(D)]
    return G, H, h, glabels, hlabels


def dot(a, b):
    return sum(x*y for x,y in zip(a,b))


def rational(values):
    return [F(float(x)).limit_denominator(10**6) for x in values]


def build():
    G,H,h,_,_ = constraints(3)
    p = linprog(np.zeros(N+1), A_ub=-np.array(G), b_ub=np.zeros(len(G)),
                A_eq=H, b_eq=h, bounds=[(None,None)]*(N+1), method='highs')
    assert p.success, p.message
    a = rational(p.x)
    assert all(dot(row,a) >= 0 for row in G)
    assert all(dot(row,a) == rhs for row,rhs in zip(H,h))
    (ROOT/'results/lp-feasible-7-3-3.json').write_text(json.dumps({
        'n':N,'K':3,'d':D,'normalization':'a_i=A_i/K^2',
        'a':[str(x) for x in a],
        'claim':'feasible enhanced quantum LP, NOT a quantum code'
    },indent=2)+'\n')

    G,H,h,glabels,hlabels = constraints(4)
    ng,nh=len(G),len(H)
    # Farkas proof: y>=0, yG+zH=0, z*h=1 gives 0=yGa+1>=1.
    eq = np.block([[np.array(G).T, np.array(H).T],
                   [np.zeros((1,ng)), np.array([h])]])
    rhs = np.array([0]*(N+1)+[1])
    d = linprog(np.array([1]*ng+[0]*nh), A_eq=eq,b_eq=rhs,
                bounds=[(0,None)]*ng+[(None,None)]*nh,method='highs')
    assert d.success, d.message
    y,z = rational(d.x[:ng]),rational(d.x[ng:])
    assert min(y)>=0 and dot(z,h)==1
    assert all(sum(y[r]*G[r][i] for r in range(ng))+sum(z[r]*H[r][i] for r in range(nh))==0
               for i in range(N+1))
    sparse_y={label:str(v) for label,v in zip(glabels,y) if v}
    sparse_z={label:str(v) for label,v in zip(hlabels,z) if v}
    (ROOT/'results/lp-infeasible-7-4-3.json').write_text(json.dumps({
        'n':N,'K':4,'d':D,'nonnegative_multipliers':sparse_y,
        'equality_multipliers':sparse_z,
        'identity':'yG+zH=0; z*h=1; hence feasible a would imply 0>=1'
    },indent=2)+'\n')
    print('K=3 exact enhanced-LP feasible a =', [str(x) for x in a])
    print('K=4 exact Farkas certificate:', json.dumps({'y':sparse_y,'z':sparse_z},sort_keys=True))


if __name__ == '__main__':
    build()
