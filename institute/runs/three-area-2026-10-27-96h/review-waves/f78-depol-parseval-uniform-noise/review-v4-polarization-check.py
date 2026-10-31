#!/usr/bin/env python3
"""Check the polarization-argument qualification, without author imports."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
B=[x for x in range(16) if x.bit_count()>=2]
def defect(v):
    x,y=v.get(3,(F(0),F(0)))
    return 2*x*y  # Im(c_3**2)
checks=0
for i in B:
    assert defect({i:(F(1),F(0))})==0;checks+=1
for i,j in combinations(B,2):
    for imag in (False,True):
        v={i:(F(1),F(0)),j:(F(0),F(1)) if imag else (F(1),F(0))}
        assert defect(v)==0;checks+=1
witness=defect({3:(F(1),F(1))})
assert checks==121 and witness==2
print(json.dumps({'normal_basis':B,'vanishing_basis_and_pairs':checks,'quadratic':'Im(c_3^2)','value_at_c_3_1_plus_i':witness,
 'interpretation':'quadratic homogeneity alone does not imply sesquilinear polarization; actual channel charge covariance supplies the missing property'},indent=2))
