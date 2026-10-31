#!/usr/bin/env python3
"""Exact bivariate determinant of a complete affine pencil, faster v2.

Per prime p: if the slope N of the charpoly variable is invertible mod p,
    det(A+zN+wO)=det(N)*charpoly(-(N^-1A+w N^-1O))(z),
so each node needs ONE characteristic polynomial. Otherwise per-node
det(M)*charpoly(M^-1N) is used. Prime product exceeds twice the smaller of the
row- and column-Hadamard coefficient bounds, so CRT is exact. Every residue
above total degree m must vanish.
Mode --verify: recompute residue tables for DISJOINT primes in the opposite
orientation and require that a pinned exact integer table reduces to them.
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
    dB=int(MB.det());nodes=[];values=[]
    if dB:
        Bi=MB.inv();X=Bi*MA;Y=Bi*MC
        for node in range(m+1):
            K=X+Y*node if node else X
            e=[int(c) for c in (K*(p-1)).charpoly().coeffs()]
            e+=[0]*(m+1-len(e));assert e[m]==1
            values.append([dB*e[i]%p for i in range(m+1)]);nodes.append(node)
        method='slope-inverse'
    else:
        node=0
        while len(nodes)<m+1:
            M=MA+MC*node if node else MA
            d=int(M.det())
            if d:
                K=M.inv()*MB
                e=[int(c) for c in K.charpoly().coeffs()];e+=[0]*(m+1-len(e));assert e[m]==1
                values.append([(d*(-1)**i*e[m-i])%p for i in range(m+1)]);nodes.append(node)
            node+=1;assert node<4*m+40
        method='node-inverse'
    W=flint.nmod_mat(m+1,m+1,[pow(t,j,p) for t in nodes for j in range(m+1)],p)
    T=W.inv()*flint.nmod_mat(m+1,m+1,[v for row in values for v in row],p)
    out=[]
    for j in range(m+1):
        for i in range(m+1):
            c=int(T[j,i])
            if i+j>m:assert c==0,'total degree violation'
            else:out.append(c)
    return p,method,out


def integer_pencil(P):
    A=[];B=[];C=[];scales=[]
    for row in P['matrix']:
        entries=[[Q(v) for v in e] for e in row]
        L=math.lcm(*(v.denominator for e in entries for v in e));scales.append(L)
        A.append([int(e[0]*L) for e in entries]);B.append([int(e[1]*L) for e in entries]);C.append([int(e[2]*L) for e in entries])
    return A,B,C,scales


def hadamard(A,B,C):
    m=len(A);col=1;row=1
    for j in range(m):col*=sum(math.isqrt(sum(M[i][j]**2 for i in range(m)))+1 for M in (A,B,C))
    for i in range(m):row*=sum(math.isqrt(sum(v*v for v in M[i]))+1 for M in (A,B,C))
    return min(col,row)


def prime_list(offset,need=None,count=None):
    out=[];product=1;skipped=0;c=(1<<62)-1
    while (need is not None and product<=need) or (count is not None and len(out)<count):
        if is_prime(c):
            if skipped<offset:skipped+=1
            else:out.append(c);product*=c
        c-=2
    return out


def monomials(m,orientation):
    out=[]
    for j in range(m+1):
        for i in range(m+1-j):out.append((i,j) if orientation=='x' else (j,i))
    return out


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser()
    ap.add_argument('--pencil',required=True);ap.add_argument('--pencil-sha256',required=True)
    ap.add_argument('--orientation',choices=['x','y'],default='x')
    ap.add_argument('--prime-offset',type=int,default=0)
    ap.add_argument('--workers',type=int,default=8);ap.add_argument('--tag',default='v2')
    ap.add_argument('--verify');ap.add_argument('--verify-sha256');ap.add_argument('--verify-primes',type=int,default=12)
    ap.add_argument('--shear',action='store_true',help='compute Q(z,w)=det(A+z(B+C)+wC) and return P(x,y)=Q(x,y-x)')
    args=ap.parse_args()
    assert Path(args.pencil).name==args.pencil
    raw=(ROOT/args.pencil).read_bytes();assert hashlib.sha256(raw).hexdigest()==args.pencil_sha256
    P=json.loads(raw);m=P['entire_primitive_dimension'];a,b,n=P['degree']
    assert len(P['matrix'])==m and all(len(row)==m for row in P['matrix'])
    A,B,C,scales=integer_pencil(P)
    if args.shear:
        assert not args.verify and args.orientation=='x'
        B=[[u+v for u,v in zip(rb,rc)] for rb,rc in zip(B,C)]
    bound=hadamard(A,B,C)
    if args.verify:
        vraw=(ROOT/args.verify).read_bytes();assert hashlib.sha256(vraw).hexdigest()==args.verify_sha256
        R=json.loads(vraw);assert R['pencil']=={'file':args.pencil,'sha256':args.pencil_sha256}
        assert R['orientation']!=args.orientation and R['row_scales']==[str(s) for s in scales]
        craw=(ROOT/R['coefficient_file']['file']).read_bytes();assert hashlib.sha256(craw).hexdigest()==R['coefficient_file']['sha256']
        table={(i,j):int(c) for i,j,c in json.loads(gzip.decompress(craw))}
        plist=prime_list(args.prime_offset,count=args.verify_primes)
        assert not set(map(str,plist))&set(R['primes'])
    else:
        plist=prime_list(args.prime_offset,need=2*bound+1)
    print('PENCIL',P['degree'],'dimension',m,'bound bits',bound.bit_length(),'primes',len(plist),'verify' if args.verify else 'exact',flush=True)
    with Pool(args.workers,initializer=init,initargs=((A,B,C,args.orientation),)) as pool:
        results=sorted(pool.map(residues,plist,chunksize=1),key=lambda z:plist.index(z[0]))
    mono=monomials(m,args.orientation)
    stem=f'frontier-20261029-level{n}-{a}{b}-multimodular-determinant-{args.orientation}-{args.tag}'
    if args.shear:stem+='-shear'
    if args.verify:
        out=ROOT/f'{stem}-verification.json'
        if out.exists():raise FileExistsError(out)
        for p,_,res in results:
            for mn,x in zip(mono,res):assert table.get(mn,0)%p==x,('independent residue mismatch',p,mn)
        record={'owner':'MathKacMoody-2','degree':P['degree'],'pencil':R['pencil'],'verified_table':{'file':args.verify,'sha256':args.verify_sha256},
                'orientation':args.orientation,'disjoint_primes':[str(p) for p in plist],'methods':sorted({r[1] for r in results}),
                'entire_residue_tables_matched':len(plist),'monomials_per_table':len(mono),
                'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'flint_version':flint.__version__,
                'status':'PASS_DISJOINT_PRIME_OPPOSITE_ORIENTATION_RESIDUE_REPLAY',
                'limits':'Replays the exact table modulo independent primes with the opposite charpoly variable; the exact proof is the bounded CRT computation. Shared FLINT. No parent/formal/novelty acceptance.'}
        with out.open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
        print('PASS residue replay',out.name,flush=True);return
    out=ROOT/f'{stem}.json';coef_out=ROOT/f'{stem}-coefficients.json.gz'
    if out.exists() or coef_out.exists():raise FileExistsError(out)
    X=list(results[0][2]);M=results[0][0]
    for p,_,res in results[1:]:
        inv=pow(M%p,-1,p);X=[x+((r-x)*inv%p)*M for x,r in zip(X,res)];M*=p
    half=M//2;X=[x-M if x>half else x for x in X]
    assert all(abs(x)<=bound for x in X)
    coefficients={mn:x for mn,x in zip(mono,X) if x}
    if args.shear:
        S=[flint.fmpz_poly([0]) for _ in range(m+1)];rows={}
        for (i,j),c in coefficients.items():rows.setdefault(j,{})[i]=c
        for j,r in rows.items():S[j]=flint.fmpz_poly([r.get(i,0) for i in range(max(r)+1)])
        xpoly=flint.fmpz_poly([0,1]);sheared={}
        for l in range(m+1):
            acc=flint.fmpz_poly([0])
            for d in range(m-l,-1,-1):
                acc=acc*xpoly+S[l+d]*(math.comb(l+d,l)*(-1)**d)
            for i,c in enumerate(acc.coeffs()):
                if c:sheared[i,l]=int(c)
        p0=results[0][0];check=flint.nmod_mat(m,m,[0]*(m*m),p0)
        for (xv,yv) in ((3,5),(11,2)):
            M0=flint.nmod_mat(m,m,[(A[i][j]+xv*(B[i][j]-C[i][j])+yv*C[i][j])%p0 for i in range(m) for j in range(m)],p0)
            z=sum(c*pow(xv,i,p0)*pow(yv,j,p0) for (i,j),c in sheared.items())%p0
            assert z==int(M0.det()),'shear transform spot check failed'
        coefficients=sheared
    serial=json.dumps([[i,j,str(c)] for (i,j),c in sorted(coefficients.items())],separators=(',',':')).encode()
    with coef_out.open('xb') as raw_stream:
        with gzip.GzipFile(fileobj=raw_stream,mode='wb',compresslevel=6,mtime=0) as stream:stream.write(serial)
    record={'owner':'MathKacMoody-2','degree':P['degree'],'pencil':{'file':args.pencil,'sha256':args.pencil_sha256},
            'variables':P['variable_meaning'],'dimension':m,'orientation':args.orientation,
            'shear':('Q(z,w)=prod(row_scales)*det(A+z(B+C)+wC) computed by bounded CRT (bound for Q), then exact fmpz_poly transform P(x,y)=Q(x,y-x); two exact modular spot evaluations of P' if args.shear else None),
            'row_scales':[str(s) for s in scales],'row_scale_product_bits':math.prod(scales).bit_length(),
            'integer_polynomial_meaning':'Z(x,y)=prod(row_scales)*det(A+xB+yC); listed integer coefficients are Z',
            'hadamard_bound_bits':bound.bit_length(),'prime_count':len(plist),'prime_offset':args.prime_offset,
            'primes':[str(p) for p in plist],'methods':sorted({r[1] for r in results}),
            'nonzero_coefficients':len(coefficients),'positive':sum(c>0 for c in coefficients.values()),
            'negative':sum(c<0 for c in coefficients.values()),'constant':str(coefficients.get((0,0),0)),
            'coefficient_file':{'file':coef_out.name,'sha256':hashlib.sha256(coef_out.read_bytes()).hexdigest(),
                                'uncompressed_serialization_sha256':hashlib.sha256(serial).hexdigest()},
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'flint_version':flint.__version__,
            'status':'EXACT_MULTIMODULAR_PENCIL_DETERMINANT',
            'limits':'Shared FLINT modular arithmetic; exact by proven Hadamard bound and CRT. Pencil correctness, D3-kernel containment and actual quotient transport are separate obligations. No parent/formal/configured-family/human/novelty acceptance.'}
    with out.open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
    print('WROTE',out.name,'terms',len(coefficients),'positive',record['positive'],'negative',record['negative'],flush=True)


if __name__=='__main__':main()
