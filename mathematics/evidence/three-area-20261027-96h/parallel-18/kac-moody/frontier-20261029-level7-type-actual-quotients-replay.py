#!/usr/bin/env python3
"""Alternate replay of one whole actual-parameter level7 type certificate.

Imports NO producer. Source tensor expansion uses the separate older literal
Lyndon implementation; Gram uses the Hadamard-diagonal tensor formula; seeds
use repeated tuple brackets; sparse G is pushed onto descendants; ideals use
transpose evaluation RREF; quotients use explicit annihilators and lifts;
free-bound tests use stdlib binomial integer translation.
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


def load(name,file,sha):
    raw=(ROOT/file).read_bytes()
    if sha is not None:assert hashlib.sha256(raw).hexdigest()==sha,file
    spec=importlib.util.spec_from_file_location(name,ROOT/file)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module,hashlib.sha256(raw).hexdigest()


def translate2(terms,delta,degree):
    out=Counter()
    for (i,j),c in terms.items():
        for u in range(i+1):
            cu=c*math.comb(i,u)*(-delta)**(i-u)
            for v in range(j+1):out[u,v]+=cu*math.comb(j,v)*(-delta)**(j-v)
    return {m:c for m,c in out.items() if c}


def translate1(coefficients,delta):
    return [sum((c*math.comb(j,i)*delta**(j-i) for j,c in enumerate(coefficients) if j>=i),Q(0)) for i in range(len(coefficients))]


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True)
    ap.add_argument('--sha256',required=True);ap.add_argument('--old-replay-sha256',required=True)
    args=ap.parse_args();a,b=args.a,args.b;label=f'{a}{b}'
    L,_=load('literal_tools',LITERAL,LITERAL_SHA);F=L.flint
    old,old_sha=load('older_literal_lyndon',OLD,args.old_replay_sha256)
    name=f'frontier-20261029-level7-{label}-actual-all-parameters-v1.json'
    C=json.loads(L.pinned({'file':name,'sha256':args.sha256}))
    assert C['degree']==[a,b,7]
    S=json.loads(L.pinned(C['inputs']['source']));P=json.loads(L.pinned(C['inputs']['pencil']))
    D=json.loads(L.pinned(C['inputs']['polynomial']))
    assert P['source_pencil_sha256']==C['inputs']['source']['sha256'] and D['pencil_sha256']==C['inputs']['pencil']['sha256']
    k=P['entire_primitive_dimension'];assert k==C['entire_free_primitive_dimension']==S['joint_horizontal_kernel_dim']
    assert tuple(S['source_words'])==old.ind.lyndon_words((a,b,7))
    assert old.seventh_dimensions(a,b)==(len(S['source_words']),k)
    G,degrees=L.literal_module()
    states={(0,0):['']}
    for _ in range(7):
        nxt=defaultdict(list)
        for (x,y),prefixes in states.items():
            for j,(dx,dy) in enumerate(degrees):
                if x+dx<=a and y+dy<=b:nxt[x+dx,y+dy].extend(p+str(j) for p in prefixes)
        states=nxt
    universe=sorted(states[a,b]);assert len(universe)==C['word_universe']
    codes=np.array([L.code(tuple(map(int,w))) for w in universe],dtype=np.uint32)
    lookup={w:i for i,w in enumerate(universe)};code_lookup={int(c):i for i,c in enumerate(codes)}
    expansions=[old.ind.ind.standard_bracket(w) for w in S['source_words']]
    V=np.zeros((k,len(universe)),dtype=np.int64);den=[]
    for i,row in enumerate(S['horizontal_kernel_coefficients']):
        parsed={int(j):Q(c) for j,c in row.items()}
        d=math.lcm(*(c.denominator for c in parsed.values()));den.append(d)
        vec=Counter()
        for j,c in parsed.items():
            m=int(c*d)
            for w,x in expansions[j].items():
                assert Q(x).denominator==1;vec[w]+=m*int(x)
        assert all(abs(int(c))<2**63 for c in vec.values())
        for w,c in vec.items():V[i,lookup[w]]=c
    assert den==C['row_denominators']
    W=V.copy();zero=np.zeros(len(codes),dtype=np.int64);three=zero.copy();seven=zero.copy()
    peak=max(abs(int(W.min())),abs(int(W.max())))
    for pos in range(7):
        assert peak*2**(pos+1)<2**63
        shift=3*(6-pos);letters=(codes>>shift)&7
        c3=np.flatnonzero(letters==3);c4=np.array([code_lookup[int(codes[i])^(7<<shift)] for i in c3],dtype=np.int64)
        x=W[:,c3].copy();y=W[:,c4].copy();W[:,c3]=x+y;W[:,c4]=x-y
        zero+=(letters==3)|(letters==4);three+=(letters==3);seven+=(letters==7)
    weights=np.array([2**(7-int(z))*3**int(t)*4**int(s) for z,t,s in zip(zero,three,seven)],dtype=np.int64)
    assert max(abs(int(W.min())),abs(int(W.max())))*int(weights.max())<2**63
    scaled=F.fmpz_mat((W*weights).tolist())*F.fmpz_mat(W.tolist()).transpose()
    H=L.matrix(C['source_gram'])
    assert F.fmpq_mat(scaled)==128*H and H.det()
    fields=[F.fmpq_mat(k,k,[F.fmpq(P['matrix'][i][j][h])*den[j]/den[i] for i in range(k) for j in range(k)]) for h in range(3)]
    terms={(e['x_power'],e['y_power']):Q(e['coefficient']) for e in D['coefficients']}
    tests=[]
    for bound in range(1,8):
        moved=translate2(terms,7-bound,k)
        tests.append({'bound':bound,'all_positive_nonzero_constant':bool(moved.get((0,0),0)) and all(c>0 for c in moved.values()),'terms':len(moved)})
    assert tests==C['free_bound_tests']
    b0=C['free_uniform_positive_bound'];assert b0==min(t['bound'] for t in tests if t['all_positive_nonzero_constant'])

    def family(node,p):
        target=(a-1,b) if node==1 else (a,b-1)
        if min(target)<0 or p>6:return [],np.zeros((k,0),dtype=np.int64)
        q={(node,):1}
        for _ in range(p):q=L.bracket({(0,):1},q)
        q={w:-c for w,c in q.items()};gens=[];cols=[]
        vpeak=max(abs(int(V.min())),abs(int(V.max())))
        for outer in itertools.product(range(8),repeat=6-p):
            if (sum(degrees[x][0] for x in outer),sum(degrees[x][1] for x in outer))!=target:continue
            y=q
            for x in reversed(outer):y=L.bracket({(x,):1},y)
            gens.append({'node':node,'parameter':p,'outer_letters':list(outer),
                         'whole_word_terms':[[L.code(w),int(c)] for w,c in sorted(y.items(),key=lambda z:L.code(z[0]))]})
            gy=Counter()
            for word,c in y.items():
                expansion={():c}
                for letter in word:
                    expansion={pre+(j,):val*G[j][letter] for pre,val in expansion.items() for j in range(8) if G[j][letter]}
                for w,val in expansion.items():gy[L.code(w)]+=val
            gy={w:c for w,c in gy.items() if c}
            if not gy:cols.append(np.zeros(k,dtype=np.int64));continue
            ix=np.array([code_lookup[w] for w in gy],dtype=np.int64);co=np.array(list(gy.values()),dtype=np.int64)
            assert vpeak*sum(abs(int(c)) for c in co)<2**63
            cols.append(V[:,ix]@co)
        return gens,(np.array(cols,dtype=np.int64).T if cols else np.zeros((k,0),dtype=np.int64))

    def ideal(cross):
        if cross.shape[1]==0:return F.fmpq_mat(k,0),[],list(range(k))
        rr,rank=F.fmpq_mat(cross.T.tolist()).rref()
        if rank==0:return F.fmpq_mat(k,0),[],list(range(k))
        basis_eval=F.fmpq_mat(k,rank,[rr[j,i] for i in range(k) for j in range(rank)])
        proj=H.solve(basis_eval);red,r=proj.transpose().rref();assert r==rank
        I=F.fmpq_mat(k,rank,[red[j,i] for i in range(k) for j in range(rank)])
        piv=[next(i for i in range(k) if red[j,i]) for j in range(rank)]
        return I,piv,[i for i in range(k) if i not in piv]

    def quotient(A,I,piv,free):
        q=len(free);d=I.ncols()
        cov=F.fmpq_mat(q,k);lift=F.fmpq_mat(k,q)
        for j,f in enumerate(free):
            cov[j,f]=1;lift[f,j]=1
            for t,p in enumerate(piv):cov[j,p]=-I[f,t]
        if d:assert cov*I==F.fmpq_mat(q,d) and cov*A*I==F.fmpq_mat(q,d)
        return cov*A*lift

    crosses={};grid=0;descendants=0
    assert len(C['rows'])==2*(b0-1)
    for record,(node,p) in zip(C['rows'],[(n,p) for n in (1,2) for p in range(1,b0)]):
        assert (record['node'],record['parameter'])==(node,p)
        gens,cross=family(node,p);descendants+=len(gens)
        assert gens==record['all_generators'] and cross.tolist()==record['all_cross_inner_products']
        I,piv,free=ideal(cross)
        assert I.ncols()==record['whole_projected_ideal_rank'] and L.strings(I)==record['ideal_basis']
        assert piv==record['ideal_pivot_coordinates'] and free==record['complement_coordinates']
        crosses[node,p]=cross
        if node==1:A=fields[0]+(p-7)*fields[1]+(b0-7)*fields[2];B=fields[2]
        else:A=fields[0]+(b0-7)*fields[1]+(p-7)*fields[2];B=fields[1]
        QA=quotient(A,I,piv,free);QB=quotient(B,I,piv,free);q=len(free)
        assert [[[str(QA[i,j]),str(QB[i,j])] for j in range(q)] for i in range(q)]==record['quotient_affine_matrix']
        coeffs=[Q(c) for c in record['determinant_coefficients']];assert len(coeffs)==q+1
        for i in range(q+1):
            t=i-2;val=Q(0)
            for c in reversed(coeffs):val=val*t+c
            assert val==(Q(str((QA+t*QB).det())) if q else Q(1));grid+=1
        base=record['certified_from_other_parameter']-b0;assert base>=0
        moved=translate1(coeffs,base);assert moved[0]>0 and all(c>=0 for c in moved)
        assert base==0 or not(translate1(coeffs,base-1)[0]>0 and all(c>=0 for c in translate1(coeffs,base-1)))
    extra=set()
    for record in C['rows']:
        base=record['certified_from_other_parameter']-b0
        for t in range(base):extra.add((record['parameter'],b0+t) if record['node']==1 else (b0+t,record['parameter']))
    points=sorted({(r,s) for r in range(1,b0) for s in range(1,b0)}|extra)
    assert [c['parameters'] for c in C['corners']]==[list(p) for p in points]
    dims=[]
    for corner,(r,s) in zip(C['corners'],points):
        parts=[crosses[1,r] if r<b0 else family(1,r)[1],crosses[2,s] if s<b0 else family(2,s)[1]]
        I,piv,free=ideal(np.concatenate(parts,axis=1))
        assert I.ncols()==corner['whole_ideal_rank'] and len(free)==corner['actual_primitive_dimension']
        Qbar=quotient(fields[0]+(r-7)*fields[1]+(s-7)*fields[2],I,piv,free)
        assert L.strings(Qbar)==corner['entire_quotient_contraction_matrix']
        det=Qbar.det() if Qbar.nrows() else F.fmpq(1)
        assert det and str(det)==corner['determinant'];dims.append([r,s,len(free)])
    result={'owner':'MathKacMoody-2','input_file':name,'input_sha256':args.sha256,'degree':[a,b,7],
            'inputs':C['inputs'],'literal_helper':{'file':LITERAL,'sha256':LITERAL_SHA},'older_literal_lyndon':{'file':OLD,'sha256':old_sha},
            'entire_free_primitive_dimension':k,'source_tensor_vectors_and_Gram_reconstructed':True,
            'free_uniform_positive_bound':b0,'all_seven_free_bound_tests_stdlib':True,
            'all_seed_descendants_reconstructed':descendants,'row_shifted_matrix_determinants':grid,
            'actual_corner_dimensions':dims,'all_corner_determinants_nonzero':True,
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'numpy_version':np.__version__,'flint_version':F.__version__,
            'status':'PASS_ALTERNATE_WHOLE_ACTUAL_ALL_PARAMETER_TYPE',
            'limits':'Same owner, shared NumPy/FLINT; alternate algorithms only. Named actual-source/projection/single-seed/descent WRITTEN inputs require scientific review. No B7, parent, formal/kernel, configured-family/human, native-library or novelty acceptance.'}
    out=ROOT/f'frontier-20261029-level7-{label}-actual-all-parameters-replay-v1.json'
    with out.open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print('PASS alternate whole actual type',label,'b0',b0,'descendants',descendants,'grid',grid,'corners',len(dims),out.name,flush=True)


if __name__=='__main__':main()
