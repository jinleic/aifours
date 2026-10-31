#!/usr/bin/env python3
"""Genuinely new grade8 complete primitive maps on the free region r,s>=8.

Producer: whole f1/f2 kernel in the full Lyndon root space, canonical affine
endomorphism, complete bivariate determinant interpolation. Replay: separate
literal string-Lyndon/tree-Jacobi source/actions/contraction, every affine
matrix and the entire determinant on a DIFFERENT unisolvent triangle.
No actual-parameter claim below8, no whole-level8 or B8 result.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def pin(name,sha):
    assert Path(name).name==name
    raw=(ROOT/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
    return json.loads(raw)


def publish(name,record):
    with (ROOT/name).open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
    return hashlib.sha256((ROOT/name).read_bytes()).hexdigest()


def mobius(d):
    count=0;p=2
    while p*p<=d:
        if d%p==0:
            d//=p;count+=1
            if d%p==0:return 0
        p+=1
    return (-1)**(count+int(d>1))


def dimensions(weights,a,b):
    chars=[Counter({(0,0):1})]
    for n in range(1,9):
        following=Counter()
        for (u,v),c in chars[-1].items():
            for x,y in weights:following[u+x,v+y]+=c
        chars.append(following)
    def lie(x,y):
        if x<0 or y<0:return 0
        value=sum(mobius(d)*chars[8//d][x//d,y//d] for d in (1,2,4,8) if x%d==0 and y%d==0)
        assert value%8==0
        return value//8
    multiplicity=lie(a,b)-lie(a-1,b)-lie(a,b-1)+lie(a-2,b-1)+lie(a-1,b-2)-lie(a-2,b-2)
    return lie(a,b),multiplicity


def signed_stirling(m):
    rows=[[1]]
    for n in range(1,m+1):
        row=[0]*(n+1)
        for j,c in enumerate(rows[-1]):row[j]-=(n-1)*c;row[j+1]+=c
        rows.append(row)
    return rows


def polynomial(matrices,F):
    k=len(matrices[0]);triples=[[[matrices[0][i][j],matrices[1][i][j]-matrices[0][i][j],matrices[2][i][j]-matrices[0][i][j]] for j in range(k)] for i in range(k)]
    scales=[math.lcm(*(c.denominator for e in row for c in e)) for row in triples]
    data=[[[int(c*s) for c in e] for e in row] for row,s in zip(triples,scales)]
    values={(i,j):int(F.fmpz_mat([[a+i*b+j*c for a,b,c in row] for row in data]).det()) for i in range(k+1) for j in range(k+1-i)}
    dx={};dxy={}
    for j in range(k+1):
        work=[values[i,j] for i in range(k+1-j)]
        for i in range(k+1-j):dx[i,j]=work[0];work=[b-a for a,b in zip(work,work[1:])]
    for i in range(k+1):
        work=[dx[i,j] for j in range(k+1-i)]
        for j in range(k+1-i):dxy[i,j]=work[0];work=[b-a for a,b in zip(work,work[1:])]
    st=signed_stirling(k);fac=[math.factorial(i) for i in range(k+1)]
    coefficients=Counter()
    for (i,j),d in dxy.items():
        if not d:continue
        multiplier=Q(d,fac[i]*fac[j]*math.prod(scales))
        for u,c in enumerate(st[i]):
            if c:
                for v,e in enumerate(st[j]):
                    if e:coefficients[u,v]+=multiplier*c*e
    coefficients={m:c for m,c in coefficients.items() if c}
    for (i,j),value in values.items():
        assert sum((c*i**u*j**v for (u,v),c in coefficients.items()),Q(0))*math.prod(scales)==value
    return triples,coefficients,len(values)


def produce(a,b):
    A=load('grade8_exact_canonical_tools','frontier-20261029-level6-canonical-contraction.py')
    dimension,k=dimensions(A.levi.WEIGHTS,a,b)
    assert 0<k<=60 and dimension<=150,'bounded eight-type free-region slice'
    basis=A.levi.lie_basis((a,b,8));assert len(basis)==dimension
    columns=[]
    for _,vector in basis:
        col={}
        for gidx,g in enumerate(('f1','f2')):col.update({(gidx,w):c for w,c in A.levi.levi_action(vector,g,8,8).items()})
        columns.append(col)
    coefficients=A.lift.kernel_with_coefficients(columns);assert len(coefficients)==k
    detectors=[max(co) for co in coefficients]
    assert len(set(detectors))==k
    assert all(co.get(j,0)==int(i==q) for i,co in enumerate(coefficients) for q,j in enumerate(detectors))
    primitive=A.qmatrix([[co.get(j,0) for co in coefficients] for j in range(dimension)])
    matrices=[]
    for r,s in ((8,8),(9,8),(8,9)):
        all_images=[];selected=[]
        for co in coefficients:
            den=math.lcm(*(Q(c).denominator for c in co.values()));vector={}
            for j,c in co.items():A.plus(vector,A.standard(basis[j][0]),int(c*den))
            assert vector and not A.action2(vector,'f1') and not A.action2(vector,'f2')
            output=A.canonical_96(A.suffix_d3_2(vector,r,s))
            assert not A.action2(output,'f1') and not A.action2(output,'f2')
            image=A.decompose_integer(output);normalization=den*192
            all_images.append({w:Q(c,normalization) for w,c in image.items()})
            selected.append([Q(image.get(basis[j][0],0),normalization) for j in detectors])
        M=[list(row) for row in zip(*selected)]
        assert primitive*A.qmatrix(M)==A.qmatrix([[co.get(w,Q(0)) for co in all_images] for w,_ in basis])
        matrices.append(M)
    triples,terms,points=polynomial(matrices,A.flint)
    name=f'frontier-20261029-level8-{a}{b}-small-primitive-candidate-v1.json'
    result={'owner':'MathKacMoody-2','degree':[a,b,8],'variables':'x=r-8,y=s-8',
            'source_words':[''.join(map(str,w)) for w,_ in basis],
            'source_coefficients':[{str(j):str(c) for j,c in sorted(co.items())} for co in coefficients],
            'complete_free_weight_dimension':dimension,'entire_lowest_dimension':k,'detector_Lyndon_indices':detectors,
            'matrix':[[[str(c) for c in e] for e in row] for row in triples],
            'polynomial':[{'x_power':u,'y_power':v,'coefficient':str(c)} for (u,v),c in sorted(terms.items())],
            'full_triangular_grid_points':points,'positive_coefficients':sum(c>0 for c in terms.values()),
            'negative_coefficients':sum(c<0 for c in terms.values()),'positive_constant':terms.get((0,0),Q(0))>0,
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'canonical_helper':{'file':'frontier-20261029-level6-canonical-contraction.py','sha256':hashlib.sha256((ROOT/'frontier-20261029-level6-canonical-contraction.py').read_bytes()).hexdigest()},
            'status':'PRODUCER_ENTIRE_GRADE8_FREE_REGION_SMALL_MAP_CANDIDATE',
            'limits':'Exact candidate source/pencil/polynomial only; alternate reconstruction and actual-source/classical/contraction review required. Claimed parameter region r,s>=8 only if all coefficients positive with positive constant. No small rows, whole grade8/B8, f173 actual-source transfer, parent/formal/kernel/configured-family/human/native-library/novelty acceptance.'}
    sha=publish(name,result)
    print('WROTE new grade8',(a,b,8),'free',dimension,'lowest',k,'positive',result['positive_coefficients'],'negative',result['negative_coefficients'],'constant',result['positive_constant'],name,sha,flush=True)


def replay(a,b,sha):
    A=load('grade8_literal_old_replay','frontier-20261029-level7-canonical-independent-replay.py')
    name=f'frontier-20261029-level8-{a}{b}-small-primitive-candidate-v1.json';C=pin(name,sha)
    words=C['source_words'];assert tuple(words)==A.ind.lyndon_words((a,b,8))
    dim,k=dimensions(A.ind.WEIGHTS,a,b);assert (dim,k)==(len(words),C['entire_lowest_dimension'])
    coefs=[{int(j):Q(c) for j,c in row.items()} for row in C['source_coefficients']]
    free=C['detector_Lyndon_indices'];assert len(coefs)==len(free)==k
    assert all(co.get(j,0)==int(i==q) for i,co in enumerate(coefs) for q,j in enumerate(free))
    for co in coefs:
        vector=A.ind.combine([A.ind.ind.standard_bracket(w) for w in words],co)
        assert not A.ind.act(vector,'f1',8,8) and not A.ind.act(vector,'f2',8,8)
    primitive=A.qmatrix([[co.get(j,Q(0)) for co in coefs] for j in range(dim)])
    G=[[sum(A.ind.BASIS[i][u][v]*A.ind.BASIS[j][u][v] for u in range(3) for v in range(3)) for j in range(8)] for i in range(8)]
    inverse=A.qmatrix(G).inv();GI=[[Q(str(inverse[i,j])) for j in range(8)] for i in range(8)]
    matrices=[]
    for r,s in ((8,8),(9,8),(8,9)):
        all_images=[];selected=[]
        for co in coefs:
            d=A.full_tree_d3(co,words,r,s);out,den=A.independent_contraction(d,GI)
            assert set(out)<=set(words)
            all_images.append({w:Q(c,den) for w,c in out.items()})
            selected.append([Q(out.get(words[j],0),den) for j in free])
        M=[list(row) for row in zip(*selected)]
        assert primitive*A.qmatrix(M)==A.qmatrix([[co.get(w,Q(0)) for co in all_images] for w in words]);matrices.append(M)
    triples=[[[matrices[0][i][j],matrices[1][i][j]-matrices[0][i][j],matrices[2][i][j]-matrices[0][i][j]] for j in range(k)] for i in range(k)]
    assert [[[str(c) for c in e] for e in row] for row in triples]==C['matrix']
    terms={(t['x_power'],t['y_power']):Q(t['coefficient']) for t in C['polynomial']}
    assert len(terms)==len(C['polynomial']) and all(u+v<=k and min(u,v)>=0 for u,v in terms)
    assert terms.get((0,0),Q(0))>0 and all(c>0 for c in terms.values())
    checked=0
    for i in range(k+1):
        x=i-2
        for j in range(k+1-i):
            y=j+3;M=A.qmatrix([[c+x*r+y*s for c,r,s in row] for row in triples])
            assert Q(str(M.det()))==sum((c*x**u*y**v for (u,v),c in terms.items()),Q(0));checked+=1
    output=f'frontier-20261029-level8-{a}{b}-small-primitive-replay-v1.json'
    result={'owner':'MathKacMoody-2','input_file':name,'input_sha256':sha,'degree':[a,b,8],
            'complete_free_weight_dimension':dim,'entire_lowest_dimension':k,
            'whole_source_membership_independence_and_Witt_Weyl_completeness':True,
            'all3_entire_source_matrix_identities':True,'positive_polynomial_terms':len(terms),
            'shifted_full_matrix_determinants':checked,'grid':'x=i-2,y=j+3;i,j>=0;i+j<=lowest dimension',
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'literal_algebra':{'file':'frontier-20261029-level7-canonical-independent-replay.py','sha256':hashlib.sha256((ROOT/'frontier-20261029-level7-canonical-independent-replay.py').read_bytes()).hexdigest()},
            'status':'PASS_ALTERNATE_ENTIRE_GRADE8_SMALL_MAP_FREE_REGION',
            'limits':'Separate literal actions/tree-Jacobi/cyclic-negative replay, same owner and FLINT; shared scalar Witt character method. Actual-source/PBW/classical/contraction inputs UNREVIEWED, f173 conditional only. Region r,s>=8 only; no small parameters, whole grade8/B8, parent/formal/kernel/configured-family/human/native-library/status/novelty acceptance.'}
    print('PASS new grade8 replay',(a,b,8),'lowest',k,'grid',checked,output,publish(output,result),flush=True)


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True)
    ap.add_argument('--replay-sha256');args=ap.parse_args()
    if args.replay_sha256:replay(args.a,args.b,args.replay_sha256)
    else:produce(args.a,args.b)


if __name__=='__main__':main()
