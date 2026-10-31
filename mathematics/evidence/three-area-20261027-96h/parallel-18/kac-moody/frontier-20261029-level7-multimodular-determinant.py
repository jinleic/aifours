#!/usr/bin/env python3
"""Exact bivariate determinant of a complete affine canonical pencil.

For each prime p and each interpolation node in one variable, the other
variable is recovered from a characteristic polynomial:
    det(M+zN)=det(M)*sum_i (-1)^i e_(m-i) z^i,  e=charpoly(M^-1 N).
A Vandermonde inverse then gives every coefficient modulo p. A proven
column-Hadamard bound fixes the CRT prime product before any reconstruction.
No floating arithmetic. The total-degree vanishing of every residue table
entry above degree m is checked.
"""
import argparse
import gzip
import hashlib
import json
import math
import sys
from fractions import Fraction as Q
from multiprocessing import Pool
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-fastalgebra'))
import flint

DATA=None


def is_prime(n):
    if n<2:return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%p==0:return n==p
    d=n-1;s=0
    while d%2==0:d//=2;s+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x=pow(a,d,n)
        if x in (1,n-1):continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1:break
        else:return False
    return True


def init(data):
    global DATA
    DATA=data


def residues(p):
    A,B,C,orientation=DATA
    m=len(A)
    def reduce(rows):return flint.nmod_mat(m,m,[v%p for row in rows for v in row],p)
    MA,MB,MC=reduce(A),reduce(B),reduce(C)
    if orientation=='y':MB,MC=MC,MB
    nodes=[];values=[];node=0
    while len(nodes)<m+1:
        M=MA+MC*node if node else MA
        d=int(M.det())
        if d:
            K=M.inv()*MB
            e=[int(c) for c in K.charpoly().coeffs()]
            e+= [0]*(m+1-len(e));assert e[m]==1
            values.append([(d*(-1)**i*e[m-i])%p for i in range(m+1)])
            nodes.append(node)
        node+=1
        assert node<4*m+40,'too many singular nodes'
    W=flint.nmod_mat(m+1,m+1,[pow(t,j,p) for t in nodes for j in range(m+1)],p)
    T=W.inv()*flint.nmod_mat(m+1,m+1,[v for row in values for v in row],p)
    out=[]
    for j in range(m+1):
        for i in range(m+1):
            c=int(T[j,i])
            if i+j>m:assert c==0,'total degree violation'
            else:out.append(c)
    return p,nodes[-1],out


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser()
    ap.add_argument('--pencil',required=True);ap.add_argument('--pencil-sha256',required=True)
    ap.add_argument('--orientation',choices=['x','y'],default='x')
    ap.add_argument('--prime-offset',type=int,default=0)
    ap.add_argument('--workers',type=int,default=8);ap.add_argument('--tag',default='v1')
    args=ap.parse_args()
    assert Path(args.pencil).name==args.pencil
    raw=(ROOT/args.pencil).read_bytes();assert hashlib.sha256(raw).hexdigest()==args.pencil_sha256
    P=json.loads(raw);m=P['entire_primitive_dimension'];a,b,n=P['degree']
    stem=f'frontier-20261029-level{n}-{a}{b}-multimodular-determinant-{args.orientation}-{args.tag}'
    out=ROOT/f'{stem}.json';coef_out=ROOT/f'{stem}-coefficients.json.gz'
    if out.exists() or coef_out.exists():raise FileExistsError(out)
    assert len(P['matrix'])==m and all(len(row)==m for row in P['matrix'])
    A=[];B=[];C=[];scales=[]
    for row in P['matrix']:
        entries=[[Q(v) for v in e] for e in row]
        L=math.lcm(*(v.denominator for e in entries for v in e));scales.append(L)
        A.append([int(e[0]*L) for e in entries]);B.append([int(e[1]*L) for e in entries]);C.append([int(e[2]*L) for e in entries])
    bound=1
    for j in range(m):
        norms=sum(math.isqrt(sum(M[i][j]**2 for i in range(m)))+1 for M in (A,B,C))
        bound*=norms
    need=2*bound+1
    plist=[];product=1;skipped=0;candidate=(1<<62)-1
    while product<=need:
        if is_prime(candidate):
            if skipped<args.prime_offset:skipped+=1
            else:plist.append(candidate);product*=candidate
        candidate-=2
    print('PENCIL',P['degree'],'dimension',m,'bound bits',bound.bit_length(),'primes',len(plist),flush=True)
    with Pool(args.workers,initializer=init,initargs=((A,B,C,args.orientation),)) as pool:
        results=pool.map(residues,plist,chunksize=1)
    results.sort(key=lambda z:plist.index(z[0]))
    count=(m+1)*(m+2)//2
    assert all(len(r[2])==count for r in results)
    X=list(results[0][2]);M=results[0][0]
    for p,_,res in results[1:]:
        inv=pow(M%p,-1,p)
        X=[x+((r-x)*inv%p)*M for x,r in zip(X,res)];M*=p
    half=M//2
    X=[x-M if x>half else x for x in X]
    assert all(abs(x)<=bound for x in X)
    mono=[]
    for j in range(m+1):
        for i in range(m+1-j):mono.append((i,j) if args.orientation=='x' else (j,i))
    coefficients={mn:x for mn,x in zip(mono,X) if x}
    scale=math.prod(scales)
    serial=json.dumps([[i,j,str(c)] for (i,j),c in sorted(coefficients.items())],separators=(',',':')).encode()
    with coef_out.open('xb') as raw_stream:
        with gzip.GzipFile(fileobj=raw_stream,mode='wb',compresslevel=6,mtime=0) as stream:stream.write(serial)
    record={'owner':'MathKacMoody-2','degree':P['degree'],'pencil':{'file':args.pencil,'sha256':args.pencil_sha256},
            'variables':P['variable_meaning'],'dimension':m,'orientation':args.orientation,
            'row_scale_product_bits':scale.bit_length(),'row_scales':[str(s) for s in scales],
            'integer_polynomial_meaning':'Z(x,y)=prod(row_scales)*det(A+xB+yC); listed integer coefficients are Z',
            'column_hadamard_bound_bits':bound.bit_length(),'prime_count':len(plist),'prime_offset':args.prime_offset,
            'primes':[str(p) for p in plist],'max_node_used':max(r[1] for r in results),
            'nonzero_coefficients':len(coefficients),'positive':sum(c>0 for c in coefficients.values()),
            'negative':sum(c<0 for c in coefficients.values()),'constant':str(coefficients.get((0,0),0)),
            'coefficient_file':{'file':coef_out.name,'sha256':hashlib.sha256(coef_out.read_bytes()).hexdigest(),
                                'uncompressed_serialization_sha256':hashlib.sha256(serial).hexdigest()},
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'flint_version':flint.__version__,
            'status':'EXACT_MULTIMODULAR_PENCIL_DETERMINANT',
            'limits':'Shared FLINT modular arithmetic. Exact by the proven column bound and CRT, not a sampled polynomial. Pencil correctness, D3-kernel containment and actual quotient transport are separate obligations. No parent/formal/configured-family/human/novelty acceptance.'}
    with out.open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
    print('WROTE',out.name,'terms',len(coefficients),'positive',record['positive'],'negative',record['negative'],flush=True)


if __name__=='__main__':main()
