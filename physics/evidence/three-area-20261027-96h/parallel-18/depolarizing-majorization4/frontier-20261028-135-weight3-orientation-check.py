#!/usr/bin/env python3
"""Exact one-instance diagnostic for the 121 weight-three orientation erratum."""
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).parent
sp=importlib.util.spec_from_file_location('exact',ROOT/'frontier-20261028-09-exact-one-uniform-check.py')
e=importlib.util.module_from_spec(sp);sp.loader.exec_module(e)


def main():
    X=e.zero(16)
    X[7][0]=e.z(0,1)
    X[0][7]=e.z(0,-1)
    assert X==e.adjoint(X) and e.trace(X)==e.ZERO
    t=F(1,200);a=(1+t)/2;b=(1-t)/2
    V=e.channel(X,1-t)
    assert V==e.adjoint(V)
    assert V[8][15]==e.z(0,-b*t**3)==e.z(0,F(-199,3200000000))
    assert V[15][8]==e.z(0,b*t**3)
    assert V[7][0]==e.z(0,a*t**3)==e.z(0,F(201,3200000000))
    print(json.dumps({'scope':'one exact physical-noise matrix-unit orientation diagnostic, not a universal proof',
                     't':str(t),'p':str(1-t),'v':'i|0111>',
                     'V_(1000,1111)':str(V[8][15][1]),
                     'V_(1111,1000)':str(V[15][8][1]),
                     'V_(0111,0000)':str(V[7][0][1]),
                     'full_V_hermitian':True},indent=2,sort_keys=True))


if __name__=='__main__':main()
