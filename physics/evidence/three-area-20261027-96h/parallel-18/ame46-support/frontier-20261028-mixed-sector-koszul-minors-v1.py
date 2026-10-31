#!/usr/bin/env python3
"""Search exact no-common-root certificates for mixed-sector Koszul pencils.

For two free parties and one H/one K restricted party, contract the H factor
against (lambda,mu), obtaining a 6x6x4 tensor. Its wedge-1 Koszul flattening
is 60x36. We find 31x31 homogeneous minors with no common projective zero by
checking coprime dehomogenized polynomials over F_257 plus the point at infinity.
All relevant source coefficients are integers +/-1, so nonzero modular
resultants imply nonzero integer resultants. This is a rank LOWER certificate.
"""
import argparse
import collections
import importlib.util
import itertools
import json
from math import isqrt
from pathlib import Path
import sys

P=257
D=31
WEDGES=tuple(itertools.combinations(range(6),2))
WEDGE_INDEX={w:i for i,w in enumerate(WEDGES)}


def prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))


def make_pencil(tensor,free,hparty,kparty):
    aa,bb=free
    a0=[[0]*36 for _ in range(60)];a1=[[0]*36 for _ in range(60)]
    terms=0
    for coord,(r,s) in tensor.items():
        if coord[hparty] not in (1,2) or coord[kparty] not in (0,3,4,5):continue
        if s or r not in (-1,1):raise ValueError('mixed sector is not integer signed-unit')
        terms+=1; av,bv=coord[aa],coord[bb];dv=(0,3,4,5).index(coord[kparty])
        dest=a0 if coord[hparty]==1 else a1
        for t in range(6):
            if t==av:continue
            wedge=(min(av,t),max(av,t));sign=1 if av<t else -1
            row=WEDGE_INDEX[wedge]*4+dv;col=t*6+bv
            dest[row][col]=(dest[row][col]+sign*r)%P
    if terms!=16:raise ValueError(f'expected 16 sector entries, got {terms}')
    return a0,a1


def mat_at(a,b,t):
    if t is None:return [row[:] for row in b]
    return [[(x+t*y)%P for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]


def choose_minor(matrix):
    m=[row[:] for row in matrix];ids=list(range(len(m)));r=0;selected=[];cols=[]
    for c in range(len(m[0])):
        pivot=next((j for j in range(r,len(m)) if m[j][c]%P),None)
        if pivot is None:continue
        m[r],m[pivot]=m[pivot],m[r];ids[r],ids[pivot]=ids[pivot],ids[r]
        inverse=pow(m[r][c],-1,P)
        for i in range(r+1,len(m)):
            factor=m[i][c]*inverse%P
            if factor:
                for j in range(c,len(m[0])):m[i][j]=(m[i][j]-factor*m[r][j])%P
        selected.append(ids[r]);cols.append(c);r+=1
        if r==D:return tuple(selected),tuple(cols)
    return None


def determinant(matrix,rows,cols):
    a=[[matrix[i][j] for j in cols] for i in rows];det=1
    for c in range(len(cols)):
        pivot=next((j for j in range(c,len(rows)) if a[j][c]%P),None)
        if pivot is None:return 0
        if pivot!=c:a[c],a[pivot]=a[pivot],a[c];det=-det
        v=a[c][c]%P;det=det*v%P;inverse=pow(v,-1,P)
        for i in range(c+1,len(rows)):
            factor=a[i][c]*inverse%P
            if factor:
                for j in range(c+1,len(cols)):a[i][j]=(a[i][j]-factor*a[c][j])%P
    return det%P


def trim(f):
    while f and f[-1]%P==0:f.pop()
    return f


def poly_add(a,b):
    out=[0]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]=(out[i]+x)%P
    for i,x in enumerate(b):out[i]=(out[i]+x)%P
    return trim(out)


def poly_mul_linear(a,constant):
    out=[0]*(len(a)+1)
    for i,v in enumerate(a):out[i]=(out[i]-constant*v)%P;out[i+1]=(out[i+1]+v)%P
    return trim(out)


def interpolate(values):
    diffs=values[:];basis=[1];result=[]
    for k in range(len(values)):
        result=poly_add(result,[(diffs[0]*v)%P for v in basis])
        diffs=[(diffs[i+1]-diffs[i])%P for i in range(len(diffs)-1)]
        basis=poly_mul_linear(basis,k)
        inverse=pow(k+1,-1,P)
        basis=[v*inverse%P for v in basis]
    return result


def poly_remainder(a,b):
    a=trim(a[:]);b=trim(b[:])
    if not b:raise ValueError('division by zero polynomial')
    inv=pow(b[-1],-1,P)
    while len(a)>=len(b):
        scale=a[-1]*inv%P;shift=len(a)-len(b)
        for j,x in enumerate(b):a[j+shift]=(a[j+shift]-scale*x)%P
        trim(a)
    return a


def gcd(a,b):
    a,b=trim(a[:]),trim(b[:])
    while b:a,b=b,poly_remainder(a,b)
    if not a:return []
    inv=pow(a[-1],-1,P)
    return [(x*inv)%P for x in a]


def minor_poly(a,b,minor):
    rows,cols=minor
    values=[determinant(mat_at(a,b,t),rows,cols) for t in range(D+1)]
    f=interpolate(values)
    infinity=determinant(b,rows,cols)
    if (f[D] if len(f)>D else 0)!=infinity:
        raise ValueError('homogeneous leading coefficient mismatch')
    value37=sum(coeff*pow(37,j,P) for j,coeff in enumerate(f))%P
    if value37!=determinant(mat_at(a,b,37),rows,cols):
        raise ValueError('interpolation control mismatch')
    return f,infinity


def solve(a,b):
    candidates=[];seen=set()
    for t in (0,None,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15):
        minor=choose_minor(mat_at(a,b,t))
        if minor is None or minor in seen:continue
        seen.add(minor);f,inf=minor_poly(a,b,minor)
        for old in candidates:
            if gcd(old['polynomial'],f)==[1] and (old['infinity'] or inf):
                return {'status':'CERTIFIED','minors':[old,{'rows':minor[0],'cols':minor[1],
                        'polynomial':f,'infinity':inf,'selected_at':t}], 'gcd_mod_p':[1]}
        candidates.append({'rows':minor[0],'cols':minor[1], 'polynomial':f,'infinity':inf,'selected_at':t})
    return {'status':'NO_CERTIFICATE_IN_BOUNDED_MINOR_SEARCH','number_minors':len(candidates)}


def main():
    p=argparse.ArgumentParser();p.add_argument('table',type=Path);p.add_argument('verifier',type=Path);p.add_argument('out',type=Path);args=p.parse_args()
    if not prime(P) or P<=D:raise ValueError('invalid interpolation field')
    spec=importlib.util.spec_from_file_location('dense',args.verifier);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    tensor,sha=m.load_table(args.table);results=[]
    for free in itertools.combinations(range(4),2):
        rest=tuple(j for j in range(4) if j not in free)
        for h,k in (rest,rest[::-1]):
            a,b=make_pencil(tensor,free,h,k)
            result=solve(a,b)
            results.append({'free_parties':free,'H_party':h,'K_party':k,**result})
    out={'table_sha256':sha,'prime':P,'minor_size':D,
         'scope':'all complex nonzero H contractions of each mixed sector; zero-minor search result is NOT a no-go',
         'certified_count':sum(x['status']=='CERTIFIED' for x in results),'total':len(results),'cases':results}
    with args.out.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    json.dump({'table_sha256':sha,'prime':P,'minor_size':D,'certified_count':out['certified_count'],
               'total':out['total'],'cases':[{'free':x['free_parties'],'H':x['H_party'],'K':x['K_party'],'status':x['status']} for x in results]},sys.stdout,indent=2);print()


if __name__=='__main__':main()
