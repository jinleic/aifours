#!/usr/bin/env python3
"""Find exact countervectors to a SPECIFIC naive Euclidean PSD shortcut.

Uses the entire 235-row free target pencil; does NOT claim any kernel of D3,
a non-Serre witness, or impossibility of another inner product/certificate.
"""
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('al6',ROOT/'frontier-20261028-level6-alternate-type-minor-search.py')
al6=importlib.util.module_from_spec(spec);spec.loader.exec_module(al6)


def solve(M,b):
    n=len(b);A=[M[i][:]+[b[i]] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if A[i][j]),None);assert pivot is not None
        A[j],A[pivot]=A[pivot],A[j];q=A[j][j];A[j]=[v/q for v in A[j]]
        for i in range(n):
            if i!=j and A[i][j]:
                q=A[i][j];A[i]=[u-q*v for u,v in zip(A[i],A[j])]
    return [A[i][-1] for i in range(n)]


def main():
    P=json.loads((ROOT/'frontier-20261028-level6-free-22-pencil-v1.json').read_text());rows=al6.full_rows(P)
    n=P['joint_horizontal_kernel_dim'];assert n==34 and len(rows)==235
    results=[]
    for z,label in ((1,'r_slope'),(2,'s_slope')):
        H=[[sum((Q(v[i][0])*Q(v[j][z])+Q(v[i][z])*Q(v[j][0]) for v in rows.values()),Q(0))
            for j in range(n)] for i in range(n)]
        m=20;u=solve([row[:m] for row in H[:m]],[-H[i][m] for i in range(m)])
        vector=u+[Q(1)]+[Q(0)]*(n-m-1)
        val=sum((vector[i]*H[i][j]*vector[j] for i in range(n) for j in range(n)),Q(0))
        assert val<0
        results.append({'slope':label,'vector':[str(q) for q in vector],
                        'quadratic_value':str(val),'strictly_negative':True})
    out=ROOT/'frontier-20261028-level6-226-naive-accretivity-obstruction-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'degree':P['degree'],'full_target_word_rows':len(rows),
                               'matrix':'D=A+xB+yC; Hx=A^T B+B^T A; Hy=A^T C+C^T A',
                               'witnesses':results,'status':'BOTH_SPECIFIC_EUCLIDEAN_SLOPE_FORMS_INDEFINITE',
                               'scope':'disproves only this Euclidean accretivity shortcut; no D3-kernel or no-other-inner-product claim'},indent=2)+'\n')
    print('PASS exact negative vector for EACH Euclidean slope form; no map-kernel claim;',out.name,flush=True)

if __name__=='__main__':main()
