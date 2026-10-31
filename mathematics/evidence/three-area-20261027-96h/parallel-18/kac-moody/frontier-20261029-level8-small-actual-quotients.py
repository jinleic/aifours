#!/usr/bin/env python3
"""Whole positive-parameter quotient certificate for one small grade8 type.

Reuses the frozen grade7 scalar/Gram/finite-linear-algebra helpers; grade8
word length, polynomial origin and seed tuple length are explicit here.
Consumes an already replayed complete grade8 free-source/pencil/polynomial.
No f173 transfer: actual-source/seed/contraction consequences remain inputs.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
LIB='frontier-20261029-level7-type-actual-quotients.py'
LIB_SHA='19ce1de5ce8585f5b54b17a05e523cc89e94fbf1eb2837a1e087f3189ca0e6b8'
GRADE=8


def helper():
    raw=(ROOT/LIB).read_bytes();assert hashlib.sha256(raw).hexdigest()==LIB_SHA
    spec=importlib.util.spec_from_file_location('frozen_finite_quotient_helpers',ROOT/LIB)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def matching_tuples(weights,length,a,b):
    if min(a,b)<0:return
    def visit(prefix,left,x,y):
        if min(x,y)<0 or max(x,y)>2*left:return
        if left==0:
            if x==y==0:yield prefix
            return
        for j,(dx,dy) in enumerate(weights):yield from visit(prefix+(j,),left-1,x-dx,y-dy)
    yield from visit((),length,a,b)


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser();ap.add_argument('--free-certificate',required=True);ap.add_argument('--sha256',required=True)
    args=ap.parse_args();T=helper();F=T.flint
    assert Path(args.free_certificate).name==args.free_certificate
    raw=(ROOT/args.free_certificate).read_bytes();assert hashlib.sha256(raw).hexdigest()==args.sha256
    C=json.loads(raw);a,b,n=C['degree'];assert n==GRADE
    replay_name=f'frontier-20261029-level8-{a}{b}-small-primitive-replay-v1.json'
    rraw=(ROOT/replay_name).read_bytes();R=json.loads(rraw)
    assert R['input_sha256']==args.sha256 and R['status']=='PASS_ALTERNATE_ENTIRE_GRADE8_SMALL_MAP_FREE_REGION'
    k=C['entire_lowest_dimension']
    words=[]
    for w in matching_tuples(T.WEIGHTS,GRADE,a,b):words.append(T.code(w))
    assert words==sorted(set(words))
    codes=np.array(words,dtype=np.uint32);lookup={int(w):i for i,w in enumerate(codes)}
    basis=[tuple(map(int,w)) for w in C['source_words']]
    BM=np.zeros((len(basis),len(codes)),dtype=np.int64)
    for i,w in enumerate(basis):
        for u,c in T.expansion(w).items():BM[i,lookup[T.code(u)]]=c
    rows=[];den=[]
    for row in C['source_coefficients']:
        co={int(j):Q(c) for j,c in row.items()};d=math.lcm(*(c.denominator for c in co.values()));den.append(d)
        rows.append({j:int(c*d) for j,c in co.items()})
    bound=max(sum(abs(c) for c in co.values()) for co in rows)*max(abs(int(BM.min())),abs(int(BM.max())))
    assert bound<2**63
    coefficients=np.zeros((k,len(basis)),dtype=np.int64)
    for i,co in enumerate(rows):
        for j,c in co.items():coefficients[i,j]=c
    V=coefficients@BM;peak=max(abs(int(V.min())),abs(int(V.max())))
    assert peak<=bound
    metric=V.copy()
    for pos in range(GRADE):
        assert peak*4**(pos+1)<2**63
        shift=3*(GRADE-1-pos);letters=(codes>>shift)&7
        i3=np.flatnonzero(letters==3);i4=np.array([lookup[int(codes[i])^(7<<shift)] for i in i3],dtype=np.int64)
        v3=metric[:,i3].copy();v4=metric[:,i4].copy();metric[:,i3]=2*v3+v4;metric[:,i4]=v3+2*v4
        metric[:,np.flatnonzero(letters==7)]*=4
    HG=F.fmpz_mat(metric.tolist())*F.fmpz_mat(V.tolist()).transpose()
    assert HG==HG.transpose() and HG.det();H=F.fmpq_mat(HG)
    fields=[F.fmpq_mat(k,k,[F.fmpq(C['matrix'][i][j][t])*den[j]/den[i] for i in range(k) for j in range(k)]) for t in range(3)]
    terms={(e['x_power'],e['y_power']):Q(e['coefficient']) for e in C['polynomial']}
    common=math.lcm(*(c.denominator for c in terms.values()))
    ctx=F.fmpz_mpoly_ctx.get(('x','y'),'lex');X,Y=ctx.gens();poly=ctx.from_dict({m:int(c*common) for m,c in terms.items()})
    free_tests=[];b0=None
    for bound0 in range(1,GRADE+1):
        moved=poly.compose(X-(GRADE-bound0),Y-(GRADE-bound0)).to_dict()
        good=bool(moved.get((0,0),0)) and all(int(c)>0 for c in moved.values())
        free_tests.append({'bound':bound0,'nonzero_constant_and_all_positive':good,'terms':len(moved)})
        if good:b0=bound0;break
    assert b0 is not None

    def family(node,p):
        target=(a-1,b) if node==1 else (a,b-1)
        generators=[];columns=[];depth=GRADE-p-1
        if depth<0 or min(target)<0:return [],np.zeros((k,0),dtype=np.int64)
        for outer in matching_tuples(T.WEIGHTS,depth,*target):
            q={node<<(3*i):(-1)**(i+1)*math.comb(p,i) for i in range(p+1)};length=p+1
            for letter in reversed(outer):
                nxt=Counter()
                for w,c in q.items():nxt[(letter<<(3*length))|w]+=c;nxt[(w<<3)|letter]-=c
                q={w:c for w,c in nxt.items() if c};length+=1
            assert length==GRADE
            ix=np.array([lookup[w] for w in q],dtype=np.int64);co=np.array(list(q.values()),dtype=np.int64)
            assert max(abs(int(metric.min())),abs(int(metric.max())))*sum(abs(int(c)) for c in co)<2**63
            columns.append(metric[:,ix]@co if q else np.zeros(k,dtype=np.int64))
            generators.append({'node':node,'parameter':p,'outer_letters':list(outer),'whole_word_terms':[[int(w),int(c)] for w,c in sorted(q.items())]})
        return generators,(np.array(columns,dtype=np.int64).T if columns else np.zeros((k,0),dtype=np.int64))

    families={};row_results=[];extra=set()
    for node in (1,2):
        for p in range(1,b0):
            gens,cross=family(node,p);I,piv,free=T.ideal_basis(H,cross,k);families[node,p]=(gens,cross)
            if node==1:A=fields[0]+(p-GRADE)*fields[1]+(b0-GRADE)*fields[2];B=fields[2]
            else:A=fields[0]+(b0-GRADE)*fields[1]+(p-GRADE)*fields[2];B=fields[1]
            QA=T.induced(A,I,piv,free);QB=T.induced(B,I,piv,free)
            coeffs=T.univariate(QA,QB);delta=0
            while not T.positive(T.translate1(coeffs,delta)):
                delta+=1;assert delta<=40,'row polynomial did not yield sufficient positivity'
            for other in range(b0,b0+delta):extra.add((p,other) if node==1 else (other,p))
            row_results.append({'node':node,'parameter':p,'seed_degree':p+1,'outer_tuple_length':GRADE-p-1,
                'free_lowest_dimension':k,'projected_ideal_rank':I.ncols(),'intermediate_quotient_dimension':len(free),
                'all_generators':gens,'cross_inner_products':cross.tolist(),'ideal_basis':T.strings(I),'pivot_coordinates':piv,'complement_coordinates':free,
                'quotient_affine_matrix':[[[str(QA[i,j]),str(QB[i,j])] for j in range(len(free))] for i in range(len(free))],
                'variable':f't=other_parameter-{b0}','determinant_coefficients':[str(c) for c in coeffs],'certified_from_other_parameter':b0+delta})
            print('NEW grade8 row',(a,b),node,p,'ideal',I.ncols(),'intermediate',len(free),'other>=',b0+delta,flush=True)
    corners=[]
    for r,s in sorted({(r,s) for r in range(1,b0) for s in range(1,b0)}|extra):
        parts=[families[1,r][1] if (1,r) in families else family(1,r)[1],families[2,s][1] if (2,s) in families else family(2,s)[1]]
        I,piv,free=T.ideal_basis(H,np.concatenate(parts,axis=1),k)
        M=T.induced(fields[0]+(r-GRADE)*fields[1]+(s-GRADE)*fields[2],I,piv,free)
        det=M.det() if len(free) else F.fmpq(1)
        assert det,('actual quotient contraction singular',a,b,r,s)
        corners.append({'parameters':[r,s],'projected_union_rank':I.ncols(),'actual_lowest_dimension':len(free),'quotient_matrix':T.strings(M),'determinant':str(det)})
    name=f'frontier-20261029-level8-{a}{b}-small-actual-all-parameters-v1.json'
    result={'owner':'MathKacMoody-2','degree':[a,b,8],'free_certificate':{'file':args.free_certificate,'sha256':args.sha256},
        'completed_free_replay':{'file':replay_name,'sha256':hashlib.sha256(rraw).hexdigest()},'entire_free_lowest_dimension':k,
        'tensor_word_universe':len(codes),'row_denominators':den,'source_Gram':T.strings(H),'free_uniform_bound':b0,'free_bound_tests':free_tests,
        'rows':row_results,'corners':corners,'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'finite_helpers':{'file':LIB,'sha256':LIB_SHA},'status':'PRODUCER_ENTIRE_GRADE8_SMALL_TYPE_ALL_PARAMETER_CANDIDATE',
        'limits':'Whole source/seed ideals/quotient contractions represented exactly but alternate replay and scientific review pending. Projection f173 is CONDITIONAL ONLY, no actual-source/seed/PBW/rank/D3 transfer. Intermediate row dimensions not automatically actual when opposite seed present. No whole8/B8, parent/formal/kernel/configured-family/human/native-library/novelty acceptance.'}
    with (ROOT/name).open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print('WROTE new grade8 ALL-PARAMETER producer',(a,b,8),'b0',b0,'rows',len(row_results),'corners',len(corners),name,flush=True)


if __name__=='__main__':main()
