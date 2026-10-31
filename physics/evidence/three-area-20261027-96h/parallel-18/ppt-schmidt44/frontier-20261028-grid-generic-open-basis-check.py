#!/usr/bin/env python3
"""Exact chart-parameter and modular full-rank check for an open SN2 patch.

No floating arithmetic or scientific source import. The modular nonzero
minor proves real/rational invertibility; continuity is a separate proof.
"""
from fractions import Fraction as F
from pathlib import Path
import ast
import hashlib
import json
import math
import sys

sys.set_int_max_str_digits(0)
HERE=Path(__file__).parent
CERT=HERE/'frontier-20261028-grid-generic-exact-certificate-v1.json'
SOURCE=HERE/'frontier-20261028-grid-rationalized-atoms-run-v1.json'
OUT=HERE/'frontier-20261028-grid-generic-open-basis-v1.json'
Z=(F(0),F(0));O=(F(1),F(0));V=(F(1,4),F(0))

def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def div(a,b):
    d=b[0]*b[0]+b[1]*b[1]
    if not d:raise ZeroDivisionError
    return ((a[0]*b[0]+a[1]*b[1])/d,(a[1]*b[0]-a[0]*b[1])/d)


def safe(node):
    if isinstance(node,ast.Expression):return safe(node.body)
    if isinstance(node,ast.Tuple):return tuple(safe(x) for x in node.elts)
    if isinstance(node,ast.Constant) and isinstance(node.value,(int,str)):return node.value
    if isinstance(node,ast.UnaryOp) and isinstance(node.op,ast.USub):return -safe(node.operand)
    if (isinstance(node,ast.Call) and isinstance(node.func,ast.Name)
            and node.func.id=='Fraction' and len(node.args)==2 and not node.keywords):
        return F(safe(node.args[0]),safe(node.args[1]))
    raise ValueError('unexpected parameter AST')


def chart(alpha,beta,b,f):
    if alpha==Z or f==Z:raise ValueError('chart denominator')
    d=sub(sub(mul(V,f),mul(alpha,b)),beta)
    c=div(sub(add(O,mul(V,f)),mul(beta,b)),alpha)
    e=sub(add(alpha,mul(beta,d)),mul(V,f))
    h=div(mul(V,f),alpha)
    gamma=div(add(mul(V,e),c),h)
    delta=sub(mul(V,e),mul(gamma,b))
    i=sub(add(mul(gamma,c),mul(delta,b)),mul(V,e))
    g=sub(add(gamma,mul(delta,d)),mul(V,e))
    return (O,b,c,d,e,f,g,i,h)


def features(z):
    out=[x*x+y*y for x,y in z]
    for i in range(9):
        for j in range(i+1,9):
            a,b=z[i];c,d=z[j];out.extend((a*c+b*d,b*c-a*d))
    return out


def isprime(n):
    return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))


def pick_mod(columns,p):
    pivots={};selected=[]
    for j,col in enumerate(columns):
        v=[x%p for x in col]
        for k,b in sorted(pivots.items()):
            if v[k]:
                s=v[k];v=[(x-s*y)%p for x,y in zip(v,b)]
        k=next((i for i,x in enumerate(v) if x),None)
        if k is not None:
            s=pow(v[k],-1,p);pivots[k]=[(x*s)%p for x in v];selected.append(j)
            if len(selected)==81:break
    return selected


def det_mod(matrix,p):
    n=len(matrix);a=[[x%p for x in row] for row in matrix];det=1
    for k in range(n):
        j=next((i for i in range(k,n) if a[i][k]),None)
        if j is None:return 0
        if j!=k:a[k],a[j]=a[j],a[k];det=(-det)%p
        pivot=a[k][k];det=det*pivot%p;iv=pow(pivot,-1,p)
        for i in range(k+1,n):
            if a[i][k]:
                s=a[i][k]*iv%p
                for t in range(k,n):a[i][t]=(a[i][t]-s*a[k][t])%p
    return det


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    cert=json.loads(CERT.read_text());data=json.loads(SOURCE.read_text())
    atoms=cert['atoms'];original=data['active_atoms']
    if len(atoms)!=len(original):raise AssertionError('atom count mismatch')
    basis=chart_count=0;columns=[]
    for entry,orig in zip(atoms,original):
        if int(entry['weight_numerator'])<=0:raise AssertionError('nonpositive weight')
        z=[(int(x),int(y)) for x,y in entry['coefficients']]
        params=safe(ast.parse(orig['parameters'],mode='eval'))
        if len(params)==2 and params[0]=='basis':
            j=params[1]
            if z!=[(int(k==j),0) for k in range(9)]:raise AssertionError('basis mismatch')
            basis+=1
        else:
            if len(params)!=4:raise ValueError('unexpected chart parameter count')
            q=chart(*params);scalar=z[0][0]
            if z[0][1] or scalar<=0:raise AssertionError('non-real atom normalization')
            if any((x*scalar,y*scalar)!=(F(a),F(b)) for (x,y),(a,b) in zip(q,z)):
                raise AssertionError('chart/base atom mismatch')
            chart_count+=1
        columns.append(features(z))
    for p in (1000000007,1000000009,2147483647):
        if not isprime(p):raise AssertionError('nonprime modulus')
        chosen=pick_mod(columns,p)
        if len(chosen)==81:break
    if len(chosen)!=81:raise AssertionError('no full-rank modular basis')
    determinant=det_mod([[columns[j][i] for j in chosen] for i in range(81)],p)
    if not determinant:raise AssertionError('zero modular determinant')
    result={'schema_version':1,'kind':'EXACT_OPEN_PATCH_MODULAR_BASIS_CERTIFICATE',
            'input_decomposition_sha256':digest(CERT),'input_chart_parameters_sha256':digest(SOURCE),
            'total_positive_atoms':len(atoms),'constant_low_rank_basis_atoms':basis,
            'validated_nondegenerate_chart_atoms':chart_count,'feature_dimension':81,
            'prime_modulus':p,'determinant_mod_prime':determinant,'selected_indices_zero_based':chosen,
            'limits':'modular determinant proves rational full rank; positivity and exact Gram identity are separately verified in prior certificate'}
    with open(OUT,'x',encoding='utf-8') as f:json.dump(result,f,indent=2)
    print(json.dumps({k:v for k,v in result.items() if k!='selected_indices_zero_based'},indent=2))


if __name__=='__main__':main()
