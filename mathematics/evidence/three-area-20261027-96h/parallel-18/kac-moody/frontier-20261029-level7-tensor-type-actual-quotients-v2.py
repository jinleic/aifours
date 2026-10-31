#!/usr/bin/env python3
"""Whole actual-parameter certificate for a level7 type with a TENSOR source.

Same mathematics as the Lyndon-source producer: least uniform free positive
bound b0; EVERY fixed-seed descendant below b0; whole one-seed quotient row
pencils; all remaining two-seed corners. Large matrices are recorded by
SHA-256 of canonical exact serializations; full row polynomials and corner
determinants are recorded explicitly.
"""
import argparse
import gzip
import hashlib
import io
import itertools
import json
import math
import sys
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-fastalgebra'))
import flint

WEIGHTS=((0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2))


def pinned_raw(name,sha):
    assert isinstance(name,str) and Path(name).name==name
    raw=(ROOT/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha,name
    return raw


def pinned_array(pin):
    raw=pinned_raw(pin['file'],pin['sha256']);stream=io.BytesIO(raw)
    a=np.load(stream,allow_pickle=False);assert stream.tell()==len(raw)
    return a


def digest(M):
    rows=[[str(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
    return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()


def select(M,rows,cols):
    rows=tuple(rows);cols=tuple(cols)
    return flint.fmpq_mat(len(rows),len(cols),[M[i,j] for i in rows for j in cols])


def taylor2(terms,d):
    xs=flint.fmpz_poly([-d,1]);rows={}
    for (i,j),c in terms.items():rows.setdefault(j,{})[i]=c
    mid={}
    for j,r in rows.items():
        for i,c in enumerate(flint.fmpz_poly([r.get(i,0) for i in range(max(r)+1)])(xs).coeffs()):
            if c:mid[i,j]=int(c)
    cols={};out={}
    for (i,j),c in mid.items():cols.setdefault(i,{})[j]=c
    for i,col in cols.items():
        for j,c in enumerate(flint.fmpz_poly([col.get(j,0) for j in range(max(col)+1)])(xs).coeffs()):
            if c:out[i,j]=int(c)
    return out


def ideal_basis(H,cross,k):
    if cross.shape[1]==0:return flint.fmpq_mat(k,0),[],list(range(k))
    rr,_,rank=flint.fmpz_mat(cross.tolist()).rref()
    if rank==0:return flint.fmpq_mat(k,0),[],list(range(k))
    columns=[next(j for j in range(cross.shape[1]) if rr[i,j]) for i in range(rank)]
    coordinates=H.solve(flint.fmpq_mat(cross[:,columns].tolist()))
    reduced,r=coordinates.transpose().rref();assert r==rank
    I=flint.fmpq_mat(k,rank,[reduced[j,i] for i in range(k) for j in range(rank)])
    pivots=[next(i for i in range(k) if reduced[j,i]) for j in range(rank)]
    return I,pivots,[i for i in range(k) if i not in pivots]


def induced(A,I,pivots,free):
    d=I.ncols()
    if d:
        AI=A*I;T=select(AI,pivots,range(d))
        assert AI==I*T,'whole ideal not contraction-stable'
        return select(A,free,free)-select(I,free,range(d))*select(A,pivots,free)
    return select(A,free,free)


def rowpoly(QA,QB):
    q=QA.nrows()
    if q==0:return [Q(1)]
    t0=0
    while True:
        M0=QA+QB*t0 if t0 else QA
        d0=M0.det()
        if d0:break
        t0+=1;assert t0<=q+2
    K=M0.inv()*QB
    e=[Q(str(c)) for c in K.charpoly().coeffs()];e+=[Q(0)]*(q+1-len(e));assert e[q]==1
    shifted=[Q(str(d0))*(-1)**i*e[q-i] for i in range(q+1)]  # polynomial in (t-t0)
    out=[sum((c*math.comb(j,i)*(-t0)**(j-i) for j,c in enumerate(shifted) if j>=i),Q(0)) for i in range(q+1)]
    for t in (t0,t0+1):
        z=Q(0)
        for c in reversed(out):z=z*t+c
        assert z==Q(str((QA+QB*t).det()))
    return out


def translate1(coefficients,delta):
    return [sum((c*math.comb(j,i)*delta**(j-i) for j,c in enumerate(coefficients) if j>=i),Q(0)) for i in range(len(coefficients))]


def positive(c):return c[0]>0 and all(x>=0 for x in c)


RADIX=1<<30


def digits(M):
    out=[];rest=M.copy();half=RADIX//2
    while np.any(rest):
        lo=((rest+half)%RADIX)-half;out.append(lo);rest=(rest-lo)//RADIX
    return out or [np.zeros_like(M)]


def xdigest(cross):
    rows=[[str(int(x)) for x in row] for row in cross]
    return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()


def seed_family(node,parameter,a,b,lookup,mdig):
    k=mdig[0].shape[0]
    target=(a-1,b) if node==1 else (a,b-1)
    if min(target)<0 or parameter>6:return [],np.zeros((k,0),dtype=object)
    gens=[];cols=[]
    for outer in itertools.product(range(8),repeat=6-parameter):
        if (sum(WEIGHTS[x][0] for x in outer),sum(WEIGHTS[x][1] for x in outer))!=target:continue
        poly={node<<(3*i):(-1)**(i+1)*math.comb(parameter,i) for i in range(parameter+1)};length=parameter+1
        for x in reversed(outer):
            out=Counter()
            for w,c in poly.items():out[(x<<(3*length))|w]+=c;out[(w<<3)|x]-=c
            poly={w:c for w,c in out.items() if c};length+=1
        gens.append(list(outer))
        col=np.zeros(k,dtype=object)
        if poly:
            ix=np.array([lookup[w] for w in poly],dtype=np.int64);co=np.array(list(poly.values()),dtype=np.int64)
            assert (RADIX//2)*sum(abs(int(c)) for c in co)<2**63
            for t,M in enumerate(mdig):col=col+(M[:,ix]@co).astype(object)*(RADIX**t)
        cols.append(col)
    return gens,(np.array(cols,dtype=object).T if cols else np.zeros((k,0),dtype=object))


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser()
    for name in ('source','pencil','polynomial'):
        ap.add_argument(f'--{name}',required=True);ap.add_argument(f'--{name}-sha256',required=True)
    ap.add_argument('--tag',default='v1')
    args=ap.parse_args()
    S=json.loads(pinned_raw(args.source,args.source_sha256));P=json.loads(pinned_raw(args.pencil,args.pencil_sha256))
    D=json.loads(pinned_raw(args.polynomial,args.polynomial_sha256))
    a,b,n=S['degree'];assert n==7 and P['degree']==D['degree']==[a,b,7]
    assert P['source_pencil_sha256']==args.source_sha256 and D['pencil_sha256']==args.pencil_sha256
    label=f'{a}{b}';output=ROOT/f'frontier-20261029-level7-{label}-actual-all-parameters-{args.tag}.json'
    print('PRODUCER v2 exact base-2^30 digit cross arithmetic',flush=True)
    if output.exists():raise FileExistsError(output)
    codes=pinned_array(S['files'][0]);V=pinned_array(S['files'][1]);k=S['entire_lowest_dimension']
    assert V.shape==(k,len(codes)) and k==P['entire_primitive_dimension']==D['size']
    lookup={int(w):i for i,w in enumerate(codes)}
    peak=max(abs(int(V.min())),abs(int(V.max())));metric=V.copy()
    for pos in range(7):
        assert peak*4**(pos+1)<2**63
        shift=3*(6-pos);letters=(codes>>shift)&7
        c3=np.flatnonzero(letters==3);c4=np.array([lookup[int(codes[i])^(7<<shift)] for i in c3],dtype=np.int64)
        x=metric[:,c3].copy();y=metric[:,c4].copy()
        metric[:,c3]=2*x+y;metric[:,c4]=x+2*y;metric[:,np.flatnonzero(letters==7)]*=4
    mdig=digits(metric)
    gram=flint.fmpz_mat(k,k)
    for start in range(0,len(codes),2048):
        end=min(start+2048,len(codes))
        gram+=flint.fmpz_mat(metric[:,start:end].tolist())*flint.fmpz_mat(V[:,start:end].T.tolist())
    assert gram==gram.transpose() and gram.det()
    H=flint.fmpq_mat(gram)
    fields=[flint.fmpq_mat(k,k,[flint.fmpq(P['matrix'][i][j][h]) for i in range(k) for j in range(k)]) for h in range(3)]
    rational={(e['x_power'],e['y_power']):Q(e['coefficient']) for e in D['coefficients']}
    common=math.lcm(*(c.denominator for c in rational.values()))
    terms={m:int(c*common) for m,c in rational.items()}
    b0=None;tests=[]
    for bound in range(1,8):
        moved=taylor2(terms,7-bound)
        ok=bool(moved.get((0,0),0)) and all(c>0 for c in moved.values())
        tests.append({'bound':bound,'all_positive_nonzero_constant':ok,'terms':len(moved)})
        print('FREE bound',label,bound,ok,flush=True)
        if ok:b0=bound;break
    assert b0 is not None,'no uniform free polynomial positivity bound <=7'
    families={};rows=[];extra=[]
    for node in (1,2):
        for p in range(1,b0):
            gens,cross=seed_family(node,p,a,b,lookup,mdig)
            I,pivots,free=ideal_basis(H,cross,k);families[node,p]=(gens,cross,I,pivots,free)
            if node==1:A=fields[0]+fields[1]*(p-7)+fields[2]*(b0-7);B=fields[2]
            else:A=fields[0]+fields[1]*(b0-7)+fields[2]*(p-7);B=fields[1]
            QA=induced(A,I,pivots,free);QB=induced(B,I,pivots,free)
            poly=rowpoly(QA,QB);base=0
            while not positive(translate1(poly,base)):
                base+=1;assert base<=40,'row certificate base too large'
            extra.extend(((p,b0+t) if node==1 else (b0+t,p)) for t in range(base))
            rows.append({'node':node,'parameter':p,'variable':f't=other_parameter-{b0}','generator_outer_letters':gens,
                         'cross_sha256':xdigest(cross),'cross_shape':list(cross.shape),
                         'whole_projected_ideal_rank':I.ncols(),'ideal_basis_sha256':digest(I),
                         'ideal_pivot_coordinates':pivots,'complement_coordinates':free,
                         'quotient_A_sha256':digest(QA),'quotient_B_sha256':digest(QB),
                         'determinant_coefficients':[str(c) for c in poly],'certified_from_other_parameter':b0+base})
            print('ROW',label,node,p,'ideal',I.ncols(),'quotient',len(free),'certified other>=',b0+base,flush=True)
    corners=[];points=sorted({(r,s) for r in range(1,b0) for s in range(1,b0)}|set(extra))
    for r,s in points:
        parts=[families[1,r][1] if r<b0 else seed_family(1,r,a,b,lookup,mdig)[1],
               families[2,s][1] if s<b0 else seed_family(2,s,a,b,lookup,mdig)[1]]
        I,pivots,free=ideal_basis(H,np.concatenate(parts,axis=1),k)
        Qbar=induced(fields[0]+fields[1]*(r-7)+fields[2]*(s-7),I,pivots,free)
        det=Qbar.det() if Qbar.nrows() else flint.fmpq(1)
        assert det,('ACTUAL quotient contraction singular',label,r,s)
        corners.append({'parameters':[r,s],'whole_ideal_rank':I.ncols(),'actual_primitive_dimension':len(free),
                        'quotient_sha256':digest(Qbar),'determinant':str(det)})
        print('CORNER',label,r,s,'actual',len(free),flush=True)
    result={'owner':'MathKacMoody-2','degree':[a,b,7],'entire_free_primitive_dimension':k,
            'inputs':{'source':{'file':args.source,'sha256':args.source_sha256},'pencil':{'file':args.pencil,'sha256':args.pencil_sha256},
                      'polynomial':{'file':args.polynomial,'sha256':args.polynomial_sha256}},
            'word_universe':len(codes),'source_gram_sha256':digest(H),'free_uniform_positive_bound':b0,'free_bound_tests':tests,
            'rows':rows,'corners':corners,'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'numpy_version':np.__version__,'flint_version':flint.__version__,
            'status':'PRODUCER_COMPLETE_ACTUAL_ALL_PARAMETER_TYPE_CERTIFICATE',
            'limits':'Same-owner producer pending alternate replay and scientific review. Large exact matrices recorded by canonical SHA-256. Named actual-source, lowest-projection, single-seed and quotient-descent WRITTEN inputs remain substantive. No B7, parent, formal/kernel, configured-family/human, native-library or novelty acceptance.'}
    with output.open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print('WROTE',output.name,'b0',b0,'rows',len(rows),'corners',len(corners),flush=True)


if __name__=='__main__':main()
