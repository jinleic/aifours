#!/usr/bin/env python3
"""Alternate whole grade8 small-type actual-parameter certificate replay.

No quotient producer is imported. Uses the frozen literal matrix-unit/string
Lyndon tools; Hadamard tensor Gram (scale2^8); repeated tuple-bracket seeds;
ALL ordered outer tuples; sparse G pushed onto descendants; transpose row
space for ideals; annihilator/lift quotients; all shifted row determinant
points and every actual corner. Explicit complete parameter cover check.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
import math
from collections import Counter,defaultdict
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
LITERAL='frontier-20261029-invariant-actual22-corner-replay.py'
LITERAL_SHA='a1cf8aa7d4b085384bdc48e01978bd56f20beff5c4b8faf9b61eea3621b6d8d6'
OLD='frontier-20261029-level7-canonical-independent-replay.py'
OLD_SHA='07aa8235fbddc50fb0e2683c34c0787bfe47e3398ab35aa6c6cfaf0efd9a396d'
GRADE=8


def load(name,file,sha):
    raw=(ROOT/file).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
    spec=importlib.util.spec_from_file_location(name,ROOT/file)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def move2(terms,delta):
    out=Counter()
    for (i,j),c in terms.items():
        for u in range(i+1):
            v1=c*math.comb(i,u)*(-delta)**(i-u)
            for v in range(j+1):out[u,v]+=v1*math.comb(j,v)*(-delta)**(j-v)
    return {m:c for m,c in out.items() if c}


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser();ap.add_argument('--certificate',required=True);ap.add_argument('--sha256',required=True)
    args=ap.parse_args();L=load('literal_finite_matrix_and_bracket_tools',LITERAL,LITERAL_SHA)
    old=load('literal_lyndon_tools',OLD,OLD_SHA);F=L.flint
    C=json.loads(L.pinned({'file':args.certificate,'sha256':args.sha256}));a,b,n=C['degree'];assert n==GRADE
    S=json.loads(L.pinned(C['free_certificate']));completed=json.loads(L.pinned(C['completed_free_replay']))
    assert S['degree']==[a,b,8] and completed['input_sha256']==C['free_certificate']['sha256']
    assert completed['status']=='PASS_ALTERNATE_ENTIRE_GRADE8_SMALL_MAP_FREE_REGION'
    G,weights=L.literal_module();k=C['entire_free_lowest_dimension']
    assert k==S['entire_lowest_dimension']
    assert tuple(S['source_words'])==old.ind.lyndon_words((a,b,8))
    states={(0,0):['']};characters=[Counter({(0,0):1})]
    for length in range(1,GRADE+1):
        nxt=defaultdict(list)
        for (x,y),prefixes in states.items():
            for j,(dx,dy) in enumerate(weights):
                if x+dx<=a and y+dy<=b:nxt[x+dx,y+dy].extend(w+str(j) for w in prefixes)
        states=nxt
        following=Counter()
        for (x,y),c in characters[-1].items():
            for dx,dy in weights:following[x+dx,y+dy]+=c
        characters.append(following)
    universe=sorted(states[a,b]);assert len(universe)==C['tensor_word_universe']
    def lie(x,y):
        if min(x,y)<0:return 0
        value=characters[8][x,y]
        if x%2==0 and y%2==0:value-=characters[4][x//2,y//2]
        assert value%8==0;return value//8
    expected=lie(a,b)-lie(a-1,b)-lie(a,b-1)+lie(a-2,b-1)+lie(a-1,b-2)-lie(a-2,b-2)
    assert expected==k and lie(a,b)==len(S['source_words'])
    codes=np.array([int(w,8) for w in universe],dtype=np.uint32)
    lookup={w:i for i,w in enumerate(universe)};code_lookup={int(w):i for i,w in enumerate(codes)}
    expansions=[old.ind.ind.standard_bracket(w) for w in S['source_words']]
    V=np.zeros((k,len(universe)),dtype=np.int64);den=[]
    for i,row in enumerate(S['source_coefficients']):
        co={int(j):Q(c) for j,c in row.items()};d=math.lcm(*(c.denominator for c in co.values()));den.append(d)
        vector=Counter()
        for j,c in co.items():
            for word,e in expansions[j].items():assert Q(e).denominator==1;vector[word]+=int(c*d)*int(e)
        assert all(abs(v)<2**63 for v in vector.values())
        for word,c in vector.items():V[i,lookup[word]]=c
    assert den==C['row_denominators']
    W=V.copy();zero=np.zeros(len(codes),dtype=np.int64);three=zero.copy();seven=zero.copy()
    peak=max(abs(int(V.min())),abs(int(V.max())))
    for pos in range(GRADE):
        assert peak*2**(pos+1)<2**63
        shift=3*(GRADE-1-pos);letters=(codes>>shift)&7
        i3=np.flatnonzero(letters==3);i4=np.array([code_lookup[int(codes[i])^(7<<shift)] for i in i3],dtype=np.int64)
        v3=W[:,i3].copy();v4=W[:,i4].copy();W[:,i3]=v3+v4;W[:,i4]=v3-v4
        zero+=(letters==3)|(letters==4);three+=(letters==3);seven+=(letters==7)
    multipliers=np.array([2**(GRADE-int(z))*3**int(t)*4**int(s) for z,t,s in zip(zero,three,seven)],dtype=np.int64)
    assert max(abs(int(W.min())),abs(int(W.max())))*int(multipliers.max())<2**63
    scaled=F.fmpz_mat((W*multipliers).tolist())*F.fmpz_mat(W.tolist()).transpose()
    H=L.matrix(C['source_Gram']);assert F.fmpq_mat(scaled)==H*(2**GRADE)
    assert H.det()
    fields=[F.fmpq_mat(k,k,[F.fmpq(S['matrix'][i][j][h])*den[j]/den[i] for i in range(k) for j in range(k)]) for h in range(3)]
    terms={(e['x_power'],e['y_power']):Q(e['coefficient']) for e in S['polynomial']};b0=C['free_uniform_bound']
    tests=[]
    for bound0 in range(1,b0+1):
        moved=move2(terms,GRADE-bound0)
        good=bool(moved.get((0,0),0)) and all(c>0 for c in moved.values())
        tests.append({'bound':bound0,'nonzero_constant_and_all_positive':good,'terms':len(moved)})
    assert tests==C['free_bound_tests'] and tests[-1]['nonzero_constant_and_all_positive']
    assert all(not t['nonzero_constant_and_all_positive'] for t in tests[:-1])

    def family(node,p):
        target=(a-1,b) if node==1 else (a,b-1);depth=GRADE-p-1
        if min(target)<0 or depth<0:return [],np.zeros((k,0),dtype=np.int64)
        q={(node,):1}
        for _ in range(p):q=L.bracket({(0,):1},q)
        q={w:-c for w,c in q.items()};gens=[];cols=[]
        for outer in itertools.product(range(8),repeat=depth):
            if (sum(weights[x][0] for x in outer),sum(weights[x][1] for x in outer))!=target:continue
            y=q
            for letter in reversed(outer):y=L.bracket({(letter,):1},y)
            gens.append({'node':node,'parameter':p,'outer_letters':list(outer),'whole_word_terms':[[L.code(w),int(c)] for w,c in sorted(y.items(),key=lambda z:L.code(z[0]))]})
            metric_y=Counter()
            for word,c in y.items():
                expanded={():c}
                for letter in word:expanded={pre+(j,):v*G[j][letter] for pre,v in expanded.items() for j in range(8) if G[j][letter]}
                for word,c in expanded.items():metric_y[L.code(word)]+=c
            metric_y={w:c for w,c in metric_y.items() if c}
            ix=np.array([code_lookup[w] for w in metric_y],dtype=np.int64);co=np.array(list(metric_y.values()),dtype=np.int64)
            assert peak*sum(abs(int(c)) for c in co)<2**63
            cols.append(V[:,ix]@co if metric_y else np.zeros(k,dtype=np.int64))
        return gens,(np.array(cols,dtype=np.int64).T if cols else np.zeros((k,0),dtype=np.int64))

    def ideal(cross):
        if cross.shape[1]==0:return F.fmpq_mat(k,0),[],list(range(k))
        rr,rank=F.fmpq_mat(cross.T.tolist()).rref()
        if not rank:return F.fmpq_mat(k,0),[],list(range(k))
        ev=F.fmpq_mat(k,rank,[rr[j,i] for i in range(k) for j in range(rank)])
        reduced,r=H.solve(ev).transpose().rref();assert rank==r
        I=F.fmpq_mat(k,rank,[reduced[j,i] for i in range(k) for j in range(rank)])
        piv=[next(i for i in range(k) if reduced[j,i]) for j in range(rank)]
        return I,piv,[i for i in range(k) if i not in piv]

    def quotient(A,I,piv,free):
        q=len(free);rank=I.ncols();cov=F.fmpq_mat(q,k);lift=F.fmpq_mat(k,q)
        for j,f in enumerate(free):
            cov[j,f]=1;lift[f,j]=1
            for t,p in enumerate(piv):cov[j,p]=-I[f,t]
        if rank:assert cov*I==F.fmpq_mat(q,rank) and cov*A*I==F.fmpq_mat(q,rank)
        return cov*A*lift

    keys=[(r['node'],r['parameter']) for r in C['rows']]
    assert keys==[(node,p) for node in (1,2) for p in range(1,b0)]
    crosses={};extra=set();grid=0;descendants=0
    for record in C['rows']:
        node,p=record['node'],record['parameter']
        assert record['seed_degree']==p+1 and record['outer_tuple_length']==GRADE-p-1 and record['free_lowest_dimension']==k
        gens,cross=family(node,p);descendants+=len(gens)
        assert gens==record['all_generators'] and cross.tolist()==record['cross_inner_products']
        I,piv,free=ideal(cross);crosses[node,p]=cross
        assert I.ncols()==record['projected_ideal_rank'] and len(free)==record['intermediate_quotient_dimension']
        assert L.strings(I)==record['ideal_basis'] and piv==record['pivot_coordinates'] and free==record['complement_coordinates']
        if node==1:A=fields[0]+(p-GRADE)*fields[1]+(b0-GRADE)*fields[2];B=fields[2]
        else:A=fields[0]+(b0-GRADE)*fields[1]+(p-GRADE)*fields[2];B=fields[1]
        QA=quotient(A,I,piv,free);QB=quotient(B,I,piv,free);q=len(free)
        assert [[[str(QA[i,j]),str(QB[i,j])] for j in range(q)] for i in range(q)]==record['quotient_affine_matrix']
        coefficients=[Q(c) for c in record['determinant_coefficients']];assert len(coefficients)==q+1
        for i in range(q+1):
            t=i-2;z=Q(0)
            for c in reversed(coefficients):z=z*t+c
            assert z==(Q(str((QA+t*QB).det())) if q else Q(1));grid+=1
        start=record['certified_from_other_parameter'];assert start>=b0
        moved=[sum((c*math.comb(j,i)*(start-b0)**(j-i) for j,c in enumerate(coefficients) if j>=i),Q(0)) for i in range(q+1)]
        assert moved[0]>0 and all(c>=0 for c in moved)
        for other in range(b0,start):extra.add((p,other) if node==1 else (other,p))
    points=sorted({(r,s) for r in range(1,b0) for s in range(1,b0)}|extra)
    assert [c['parameters'] for c in C['corners']]==[list(point) for point in points]
    dims=[]
    for corner,(r,s) in zip(C['corners'],points):
        parts=[crosses[1,r] if (1,r) in crosses else family(1,r)[1],crosses[2,s] if (2,s) in crosses else family(2,s)[1]]
        I,piv,free=ideal(np.concatenate(parts,axis=1));assert I.ncols()==corner['projected_union_rank'] and len(free)==corner['actual_lowest_dimension']
        M=quotient(fields[0]+(r-GRADE)*fields[1]+(s-GRADE)*fields[2],I,piv,free);det=M.det() if len(free) else F.fmpq(1)
        assert L.strings(M)==corner['quotient_matrix'] and det and str(det)==corner['determinant'];dims.append([r,s,len(free)])
    result={'owner':'MathKacMoody-2','input_file':args.certificate,'input_sha256':args.sha256,'degree':[a,b,8],
        'free_certificate':C['free_certificate'],'completed_free_replay':C['completed_free_replay'],'entire_free_lowest_dimension':k,
        'whole_tensor_source_and_Hadamard_Gram_reconstructed':True,'independent_grade8_Witt_Weyl_count':k,'free_uniform_bound':b0,
        'all_ordered_seed_descendants_reconstructed':descendants,'complete_shifted_row_matrix_determinants':grid,'actual_corner_dimensions':dims,
        'complete_all_positive_parameter_partition_checked':True,'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'literal_helpers':[{'file':LITERAL,'sha256':LITERAL_SHA},{'file':OLD,'sha256':OLD_SHA}],
        'status':'PASS_ALTERNATE_ENTIRE_GRADE8_SMALL_TYPE_ALL_PARAMETER_CERTIFICATE',
        'limits':'Same-owner alternate source/Gram/tuple/ideal/quotient/polynomial algorithms, shared FLINT. Actual-source/seed/PBW/contraction and scientific claims UNREVIEWED; f173 conditional-only. No whole8/B8,parent/formal/kernel/configured-family/human/native-library/status/novelty acceptance.'}
    out=f'frontier-20261029-level8-{a}{b}-small-actual-all-parameters-replay-v1.json'
    with (ROOT/out).open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print('PASS complete new grade8 actual type',(a,b,8),'b0',b0,'descendants',descendants,'grid',grid,'corners',len(dims),out,flush=True)


if __name__=='__main__':main()
