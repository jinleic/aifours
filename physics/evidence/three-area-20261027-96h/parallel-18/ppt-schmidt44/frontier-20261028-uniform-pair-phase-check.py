#!/usr/bin/env python3
"""Exact Gaussian-rational checks for a frustrated 2-block-positive example."""
from fractions import Fraction as F
import json
# W0=(1/2)I+3 sum[ii]-[omega] is 2-block positive by two trace bounds.
# Add P, supported on correlated basis, with diagonal 1/5 and P01=(2-20i)/101.
pdiag=F(1,5);p01r=F(2,101);p01i=F(-20,101)
det=pdiag*pdiag-p01r*p01r-p01i*p01i
assert pdiag>0 and det>0
# New correlated diagonal t=27/10, offdiagonal magnitudes all 1, q=1/2.
t=F(27,10);q=F(1,2);k01r=F(-99,101);k01i=F(-20,101)
assert k01r*k01r+k01i*k01i==1
# The triangle 01,12,20 has product K01*(-1)*(-1)=K01, non-real.
assert k01i!=0
womega=4*t+2*(5*F(-1)+k01r)
wpt=2*(q-F(1))
assert womega==F(-586,505) and wpt==-1
print(json.dumps({'P_positive_diagonal':str(pdiag),'P_01_block_determinant':str(det),
 'correlated_offdiagonal_modulus_squared':1,'frustrated_triangle_imaginary_part':str(k01i),
 'W_omega_test':str(womega),'W_partial_transpose_test':str(wpt),
 'SR2_validity':'written: W0 is 2-block positive by trace bounds and P is PSD'},indent=2))
