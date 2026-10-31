#!/usr/bin/env python3
"""Exact Laurent-coefficient audit of the recovered one-phase family."""
import importlib.util
from itertools import combinations
from pathlib import Path
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('near',P/'frontier-20261028-near-hadamard-pair-exact-v1.py')
near=importlib.util.module_from_spec(sp);sp.loader.exec_module(near)
E=near.E;phi=[1,-1,1,-1,1]
def red(p):
    p=p[:]
    for i in range(len(p)-1,3,-1):
        v=p[i]
        for j in range(5):p[i-4+j]-=v*phi[j]
    return tuple((p+[0]*4)[:4])
def root(k):return red([0]*(k%10)+[1])
def mul(v,c):return tuple(c*x for x in v)
Z=(0,0,0,0);R0=mul(root(0),5);R1=mul(root(1),-5);R9=mul(root(9),-5)
B0a={(0,2),(7,8)};B0b={(1,5),(3,4),(6,9)}
B1a={(0,1),(5,8)};B1b={(2,4),(3,9),(6,7)}
for shift in (0,1):
    for c,d in combinations(range(10),2):
        groups={k:[0]*10 for k in (-1,0,1)}
        for t in range(10):
            a=E[t][d]//2-E[t][c]//2+shift*t*(d-c)
            k=E[t][d]%2-E[t][c]%2
            groups[k][a%10]+=1
        g={k:red(v) for k,v in groups.items()}
        expected={-1:Z,0:Z,1:Z}
        if shift==0 and (c,d) in B0a:expected.update({0:R0,1:R9})
        if shift==0 and (c,d) in B0b:expected.update({-1:R1,0:R0})
        if shift==1 and (c,d) in B1a:expected.update({0:R0,1:mul(R0,-1)})
        if shift==1 and (c,d) in B1b:expected.update({-1:mul(R0,-1),0:R0})
        assert g==expected,(shift,c,d,g,expected)
print('PASS all90 unordered pairs, all Laurent coefficients exactly in Q(zeta10)')
print('H defects five pairs proportional to 5*(1-z/zeta10) or its inverse-power equivalent')
print('HF defects five pairs proportional to 5*(1-z) or its inverse-power equivalent')
print('For |z|=1: exact loss=5/2*(|1-z/zeta10|^2+|1-z|^2)')
print('Minimum ONLY IN THIS ONE-PHASE FAMILY: 10*(1-cos(pi/10)) at z=exp(i*pi/10)')
