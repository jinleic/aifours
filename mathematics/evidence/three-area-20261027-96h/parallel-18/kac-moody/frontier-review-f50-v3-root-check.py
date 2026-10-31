#!/usr/bin/env python3
"""Independently check only the cited earlier v3 root interval/comparison."""
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('helpers',ROOT/'frontier-review-f18-ph7-independent-check.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
S,R=a.S,a.R
z=a.z

def main():
    g=6000000000000000000*z**3+1102901000000000000*z**2-5748481270830000000*z+660610321325765899
    low=R(820409,1000000); high=R(82041,100000)
    left,right=S.cancel(g.subs(z,low)),S.cancel(g.subs(z,high))
    assert left<0<right
    deriv=a.bernstein(S.diff(g,z),z,low,high)
    assert all(x>0 for x in deriv)
    v4low=R(820420341,10**9)
    assert high<v4low
    p=ROOT/'frontier-review-f50-v3-root-check-v1.json'
    if p.exists():raise FileExistsError(p)
    p.write_text(json.dumps({'left_value':str(left),'right_value':str(right),
                              'derivative_bernstein':[str(x) for x in deriv],
                              'v3_upper_less_than_v4_lower':True,
                              'scope':'only old cubic root interval and v4 endpoint comparison; not whole v3 PH proof'},indent=2)+'\n',encoding='utf-8')
    print('PASS: old v3 cubic has unique root in cited interval; v3 upper < v4 lower;',p.name)

if __name__=='__main__':main()
