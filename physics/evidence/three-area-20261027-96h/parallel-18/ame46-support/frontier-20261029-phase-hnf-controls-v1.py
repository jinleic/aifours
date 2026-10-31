#!/usr/bin/env python3
"""Exact controls for integer row reduction used by the zero-excess phase solver.
No quantum claim; tests unimodularity and kernel parity on elementary systems.
"""
import argparse
from fractions import Fraction
import importlib.util
import itertools
import json
from pathlib import Path


def load(path):
    spec=importlib.util.spec_from_file_location('phase_solver',path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod


def determinant(A):
    A=[[Fraction(x) for x in r] for r in A];d=Fraction(1);n=len(A)
    for c in range(n):
        j=next((j for j in range(c,n) if A[j][c]),None)
        if j is None:return 0
        if j!=c:A[j],A[c]=A[c],A[j];d=-d
        x=A[c][c];d*=x
        for j in range(c+1,n):
            f=A[j][c]/x
            A[j]=[a-f*b for a,b in zip(A[j],A[c])]
    if d.denominator!=1:raise ValueError('integer determinant became fractional')
    return int(d)


def verify(mod,M):
    H,U,piv=mod.hnf_with_transform(M);m=len(M);n=len(M[0])
    if abs(determinant(U))!=1:raise ValueError('transform not unimodular')
    if any(sum(U[i][k]*M[k][j] for k in range(m))!=H[i][j] for i in range(m) for j in range(n)):
        raise ValueError('UM != H')
    r=len(piv)
    if any(any(H[i]) for i in range(r,m)):raise ValueError('nonzero kernel row')
    if any(H[i][c]==0 or any(H[j][c] for j in range(i+1,m)) for i,c in enumerate(piv)):
        raise ValueError('not an echelon reduction')
    return all(sum(y)%2==0 for y in U[r:]),r


def main():
    p=argparse.ArgumentParser();p.add_argument('solver',type=Path);p.add_argument('out',type=Path);a=p.parse_args();mod=load(a.solver)
    examples=[('one_half',[[1]],True),('integer_obstruction',[[0]],False),
      ('duplicate',[[1],[1]],True),('opposite',[[1],[-1]],True),
      ('odd_kernel',[[1],[1],[2]],False),
      ('complex_only_triangle',[[1,1,0],[0,1,1],[1,0,1]],True)]
    reports=[]
    for name,M,want in examples:
        ok,r=verify(mod,M)
        if ok!=want:raise ValueError(f'wrong kernel-parity answer for {name}')
        reports.append({'name':name,'rank':r,'complex_solvable':ok})
    # The complex-only triangle has phases (1/4,1/4,1/4); F2 signs are impossible.
    tri=examples[-1][1];psi=[Fraction(1,4)]*3
    if any(sum(x*y for x,y in zip(row,psi))!=Fraction(1,2) for row in tri):raise ValueError('triangle rational solution')
    if any(all(sum(row[i]*bit[i] for i in range(3))%2==1 for row in tri) for bit in itertools.product((0,1),repeat=3)):
        raise ValueError('triangle incorrectly real-solvable')
    # Mutation removes the third constraint; real solutions then exist.
    if not any(all(sum(row[i]*bit[i] for i in range(3))%2==1 for row in tri[:2]) for bit in itertools.product((0,1),repeat=3)):
        raise ValueError('triangle constraint-removal control')
    seed=20261029;tested=0
    for m in range(1,7):
      for n in range(1,7):
       for rep in range(30):
        M=[]
        for i in range(m):
            row=[]
            for j in range(n):seed=(1664525*seed+1013904223)%(1<<32);row.append(seed%7-3)
            M.append(row)
        verify(mod,M);tested+=1
    result={'elementary_cases':reports,'complex_only_triangle_exact_phases':['1/4']*3,
      'triangle_real_sign_infeasible':True,'triangle_removed_constraint_real_feasible':True,
      'random_integer_UM_and_unimodularity_checks':tested,
      'scope':'Exact arithmetic controls; no acceptance of a quantum witness or SAT UNSAT status.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
