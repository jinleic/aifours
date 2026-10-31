#!/usr/bin/env python3
"""Reconstruct coefficient incidence for the compact syndrome entropy bound."""
from pathlib import Path
import json

TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
V1=(2,5,9,10);V2=(6,7);T=(1,2,6,8)
OUT=Path(__file__).resolve().parent/'frontier-20261028-syndrome-coordinate-incidence-check-result.json'

def coefficients(tri):
    out=[]
    for i,t in enumerate(tri,1):
        out.append(sum((1 if v in V1 else 2 if v in V2 else 0) for v in t)+3*int(i in T))
    return out

def main():
    expected=[4,4,4,2,4,4,2,4,4,4];actual=coefficients(TRI)
    if actual!=expected or sum(actual)!=36:raise ValueError('INCIDENCE')
    changed=list(TRI);changed[0]=(1,2,6)
    try:
        if coefficients(changed)!=expected:raise ValueError('INCIDENCE')
    except ValueError as e:control=str(e)
    else:raise ValueError('CONTROL_ACCEPTED')
    out={'all_checked':True,'three_times_marginal_weights':actual,'sum':sum(actual),'negative_control':control,
         'limits':'Exact finite incidence arithmetic only. Validity of the source entropy inequality and substitution is a separate written argument.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
