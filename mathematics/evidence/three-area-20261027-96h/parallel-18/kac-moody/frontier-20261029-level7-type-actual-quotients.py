#!/usr/bin/env python3
"""Whole actual-parameter certificate for one complete level7 lowest type.

Inputs are the pinned complete free source, canonical pencil and free
determinant polynomial. Finds the least uniform bound b0<=7 where the free
polynomial has a nonzero constant and only positive coefficients. Then forms
EVERY fixed-seed descendant below b0, one-seed quotient row pencils and all
remaining actual two-seed corners. Nothing is selected or deleted.
"""
import argparse
import hashlib
import itertools
import json
import math
import sys
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-fastalgebra'))
import flint

WEIGHTS=((0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2))
G=[[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,2,1,0,0,0],
   [0,0,0,1,2,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,4]]


def pinned(name,sha):
    assert isinstance(name,str) and Path(name).name==name
    raw=(ROOT/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
    return json.loads(raw)


def code(word):
    value=0
    for a in word:value=8*value+int(a)
    return value


def bracket(a,b):
    out=Counter()
    for u,x in a.items():
        for v,y in b.items():out[u+v]+=x*y;out[v+u]-=x*y
    return {w:c for w,c in out.items() if c}


def lyndon(word):return all(word<word[i:] for i in range(1,len(word)))


@lru_cache(None)
def expansion(word):
    assert lyndon(word)
    if len(word)==1:return {word:1}
    cut=next(i for i in range(1,len(word)) if lyndon(word[i:]))
    out=bracket(expansion(word[:cut]),expansion(word[cut:]))
    assert min(out)==word and out[word]==1
    return out


def universe(a,b):
    out=[]
    def visit(prefix,left,x,y):
        if min(x,y)<0 or max(x,y)>2*left:return
        if left==0:
            if x==y==0:out.append(code(prefix))
            return
        for j,(dx,dy) in enumerate(WEIGHTS):visit(prefix+(j,),left-1,x-dx,y-dy)
    visit((),7,a,b)
    assert out==sorted(set(out))
    return np.array(out,dtype=np.uint32)


def select(M,rows,cols):
    rows=tuple(rows);cols=tuple(cols)
    return flint.fmpq_mat(len(rows),len(cols),[M[i,j] for i in rows for j in cols])


def strings(M):return [[str(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]


def ideal_basis(H,cross,k):
    if cross.shape[1]==0:
        return flint.fmpq_mat(k,0),[],list(range(k))
    rr,rank=flint.fmpq_mat(cross.tolist()).rref()
    columns=[next(j for j in range(cross.shape[1]) if rr[i,j]) for i in range(rank)]
    if rank==0:return flint.fmpq_mat(k,0),[],list(range(k))
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


def univariate(QA,QB):
    q=QA.nrows()
    if q==0:return [Q(1)]
    values=[Q(str((QA+t*QB).det())) for t in range(q+1)]
    work=values[:];differences=[]
    while work:differences.append(work[0]);work=[y-x for x,y in zip(work,work[1:])]
    out=[Q(0)]*(q+1);falling=[Q(1)]
    for order,d in enumerate(differences):
        for i,c in enumerate(falling):out[i]+=d*c/math.factorial(order)
        nxt=[Q(0)]*(len(falling)+1)
        for i,c in enumerate(falling):nxt[i]-=order*c;nxt[i+1]+=c
        falling=nxt
    for t,v in enumerate(values):
        z=Q(0)
        for c in reversed(out):z=z*t+c
        assert z==v
    return out


def translate1(coefficients,delta):
    return [sum((c*math.comb(j,i)*delta**(j-i) for j,c in enumerate(coefficients) if j>=i),Q(0)) for i in range(len(coefficients))]


def positive(coefficients):
    return coefficients[0]>0 and all(c>=0 for c in coefficients)


def seed_family(node,parameter,a,b,codes,lookup,metric):
    target=(a-1,b) if node==1 else (a,b-1)
    if min(target)<0 or parameter>6:return [],np.zeros((metric.shape[0],0),dtype=np.int64)
    depth=6-parameter;generators=[];columns=[]
    peak=max(abs(int(metric.min())),abs(int(metric.max())))
    for outer in itertools.product(range(8),repeat=depth):
        if (sum(WEIGHTS[x][0] for x in outer),sum(WEIGHTS[x][1] for x in outer))!=target:continue
        poly={node<<(3*i):(-1)**(i+1)*math.comb(parameter,i) for i in range(parameter+1)}
        length=parameter+1
        for x in reversed(outer):
            out=Counter()
            for w,c in poly.items():out[(x<<(3*length))|w]+=c;out[(w<<3)|x]-=c
            poly={w:c for w,c in out.items() if c};length+=1
        if not poly:
            generators.append({'node':node,'parameter':parameter,'outer_letters':list(outer),'whole_word_terms':[]})
            columns.append(np.zeros(metric.shape[0],dtype=np.int64));continue
        ix=np.array([lookup[w] for w in poly],dtype=np.int64)
        coefs=np.array(list(poly.values()),dtype=np.int64)
        assert peak*sum(abs(int(c)) for c in coefs)<2**63
        columns.append(metric[:,ix]@coefs)
        generators.append({'node':node,'parameter':parameter,'outer_letters':list(outer),
                           'whole_word_terms':[[int(w),int(c)] for w,c in sorted(poly.items())]})
    cross=np.array(columns,dtype=np.int64).T if columns else np.zeros((metric.shape[0],0),dtype=np.int64)
    return generators,cross


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser()
    for name in ('source','pencil','polynomial'):ap.add_argument(f'--{name}-sha256',required=True)
    ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True)
    args=ap.parse_args();a,b=args.a,args.b;label=f'{a}{b}'
    output=ROOT/f'frontier-20261029-level7-{label}-actual-all-parameters-v1.json'
    if output.exists():raise FileExistsError(output)
    names={'source':f'frontier-20261029-level7-{label}-complete-primitive-source-v1.json',
           'pencil':f'frontier-20261029-level7-{label}-canonical-contraction-pencil-v1.json',
           'polynomial':f'frontier-20261029-level7-{label}-canonical-determinant-v1.json'}
    S=pinned(names['source'],args.source_sha256);P=pinned(names['pencil'],args.pencil_sha256)
    D=pinned(names['polynomial'],args.polynomial_sha256)
    assert S['degree']==P['degree']==D['degree']==[a,b,7]
    assert P['source_pencil_sha256']==args.source_sha256 and D['pencil_sha256']==args.pencil_sha256
    k=P['entire_primitive_dimension'];assert k==S['joint_horizontal_kernel_dim']==D['size']
    basis=[tuple(map(int,w)) for w in S['source_words']]
    codes=universe(a,b);lookup={int(w):i for i,w in enumerate(codes)}
    Bm=np.zeros((len(basis),len(codes)),dtype=np.int64)
    for i,w in enumerate(basis):
        for v,c in expansion(w).items():Bm[i,lookup[code(v)]]=c
    rows=[];den=[]
    for row in S['horizontal_kernel_coefficients']:
        parsed={int(j):Q(c) for j,c in row.items()}
        d=math.lcm(*(c.denominator for c in parsed.values()));den.append(d)
        rows.append({j:int(c*d) for j,c in parsed.items()})
    bound=max(sum(abs(c) for c in row.values()) for row in rows)*max(abs(int(Bm.min())),abs(int(Bm.max())))
    assert bound<2**63
    C=np.zeros((k,len(basis)),dtype=np.int64)
    for i,row in enumerate(rows):
        for j,c in row.items():C[i,j]=c
    V=C@Bm;peak=max(abs(int(V.min())),abs(int(V.max())))
    metric=V.copy()
    for pos in range(7):
        assert peak*4**(pos+1)<2**63
        shift=3*(6-pos);letters=(codes>>shift)&7
        c3=np.flatnonzero(letters==3);c4=np.array([lookup[int(codes[i])^(7<<shift)] for i in c3],dtype=np.int64)
        x=metric[:,c3].copy();y=metric[:,c4].copy()
        metric[:,c3]=2*x+y;metric[:,c4]=x+2*y;metric[:,np.flatnonzero(letters==7)]*=4
    gram=flint.fmpz_mat(metric.tolist())*flint.fmpz_mat(V.tolist()).transpose()
    assert gram==gram.transpose() and gram.det()
    H=flint.fmpq_mat(gram)
    fields=[flint.fmpq_mat(k,k,[flint.fmpq(P['matrix'][i][j][h])*den[j]/den[i] for i in range(k) for j in range(k)]) for h in range(3)]
    ctx=flint.fmpz_mpoly_ctx.get(('x','y'),'lex')
    coeffs={(e['x_power'],e['y_power']):Q(e['coefficient']) for e in D['coefficients']}
    common=math.lcm(*(c.denominator for c in coeffs.values()))
    poly=ctx.from_dict({m:int(c*common) for m,c in coeffs.items()})
    X,Y=ctx.gens();b0=None;free_test=[]
    for bound_candidate in range(1,8):
        moved=poly.compose(X-(7-bound_candidate),Y-(7-bound_candidate)).to_dict()
        ok=bool(moved.get((0,0),0)) and all(int(c)>0 for c in moved.values())
        free_test.append({'bound':bound_candidate,'all_positive_nonzero_constant':ok,'terms':len(moved)})
        if ok and b0 is None:b0=bound_candidate
    assert b0 is not None,'no uniform free polynomial positivity bound <=7'
    families={};row_records=[];extra=[]
    for node in (1,2):
        for p in range(1,b0):
            generators,cross=seed_family(node,p,a,b,codes,lookup,metric)
            I,pivots,free=ideal_basis(H,cross,k)
            families[node,p]=(generators,cross,I,pivots,free)
            if node==1:A=fields[0]+(p-7)*fields[1]+(b0-7)*fields[2];B=fields[2]
            else:A=fields[0]+(b0-7)*fields[1]+(p-7)*fields[2];B=fields[1]
            QA=induced(A,I,pivots,free);QB=induced(B,I,pivots,free)
            poly1=univariate(QA,QB);base=0
            while not positive(translate1(poly1,base)):
                base+=1;assert base<=40,'row certificate base too large'
            extra.extend(((p,b0+t) if node==1 else (b0+t,p)) for t in range(base))
            row_records.append({'node':node,'parameter':p,'variable':f't=other_parameter-{b0}','all_generators':generators,
                                'all_cross_inner_products':cross.tolist(),'whole_projected_ideal_rank':I.ncols(),
                                'ideal_basis':strings(I),'ideal_pivot_coordinates':pivots,'complement_coordinates':free,
                                'quotient_affine_matrix':[[[str(QA[i,j]),str(QB[i,j])] for j in range(len(free))] for i in range(len(free))],
                                'determinant_coefficients':[str(c) for c in poly1],'certified_from_other_parameter':b0+base})
            print('ROW',label,node,p,'ideal',I.ncols(),'quotient',len(free),'certified other>=',b0+base,flush=True)
    corners=[];points=sorted({(r,s) for r in range(1,b0) for s in range(1,b0)}|set(extra))
    for r,s in points:
        parts=[]
        for node,p in ((1,r),(2,s)):
            if p<b0:parts.append(families[node,p][1])
            else:parts.append(seed_family(node,p,a,b,codes,lookup,metric)[1])
        cross=np.concatenate(parts,axis=1)
        I,pivots,free=ideal_basis(H,cross,k)
        Qbar=induced(fields[0]+(r-7)*fields[1]+(s-7)*fields[2],I,pivots,free)
        determinant=Qbar.det() if Qbar.nrows() else flint.fmpq(1)
        assert determinant,('ACTUAL quotient contraction singular',label,r,s)
        corners.append({'parameters':[r,s],'whole_ideal_rank':I.ncols(),'actual_primitive_dimension':len(free),
                        'entire_quotient_contraction_matrix':strings(Qbar),'determinant':str(determinant)})
        print('CORNER',label,r,s,'actual',len(free),flush=True)
    result={'owner':'MathKacMoody-2','degree':[a,b,7],'entire_free_primitive_dimension':k,
            'inputs':{key:{'file':names[key],'sha256':getattr(args,f'{key}_sha256')} for key in names},
            'word_universe':len(codes),'row_denominators':den,'source_gram':strings(H),
            'free_uniform_positive_bound':b0,'free_bound_tests':free_test,'rows':row_records,'corners':corners,
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'numpy_version':np.__version__,'flint_version':flint.__version__,
            'status':'PRODUCER_COMPLETE_ACTUAL_ALL_PARAMETER_TYPE_CERTIFICATE',
            'limits':'Same-owner producer pending alternate replay and scientific review. Named actual-source, lowest-projection, single-seed ideal and quotient-descent WRITTEN inputs remain substantive. No B7, parent, formal/kernel, configured-family/human, native-library or novelty acceptance.'}
    with output.open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print('WROTE',output.name,'b0',b0,'rows',len(row_records),'corners',len(corners),flush=True)


if __name__=='__main__':main()
