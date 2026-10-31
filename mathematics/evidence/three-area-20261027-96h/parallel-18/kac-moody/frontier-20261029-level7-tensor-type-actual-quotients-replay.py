#!/usr/bin/env python3
"""Alternate replay of a tensor-source actual all-parameter type certificate.

Imports NO producer. Hadamard-diagonal Gram; repeated tuple-bracket seeds with
sparse G on descendants; transpose evaluation RREF; annihilator quotients;
row determinant polynomials re-derived by bounded multimodular interpolation;
every corner determinant recomputed exactly; free-bound tests recomputed with
a different exact translation algorithm (mpoly composition).
"""
import argparse
import hashlib
import importlib.util
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
LITERAL='frontier-20261029-invariant-actual22-corner-replay.py'
LITERAL_SHA='a1cf8aa7d4b085384bdc48e01978bd56f20beff5c4b8faf9b61eea3621b6d8d6'


def load():
    raw=(ROOT/LITERAL).read_bytes();assert hashlib.sha256(raw).hexdigest()==LITERAL_SHA
    spec=importlib.util.spec_from_file_location('literal_tools',ROOT/LITERAL)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


L=load();F=L.flint


def digest(M):
    rows=[[str(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
    return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()


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


def rowpoly_multimodular(QA,QB,claimed):
    q=QA.nrows()
    if q==0:return claimed==[Q(1)]
    scales=[];A=[];B=[]
    for i in range(q):
        s=math.lcm(*(int(M[i,j].denominator) for M in (QA,QB) for j in range(q)));scales.append(s)
        A.append([int(QA[i,j]*s) for j in range(q)]);B.append([int(QB[i,j]*s) for j in range(q)])
    bound=1
    for i in range(q):bound*=math.isqrt(sum(v*v for v in A[i]))+math.isqrt(sum(v*v for v in B[i]))+2
    scale=math.prod(scales)
    target=[c*scale for c in claimed];assert all(c.denominator==1 for c in target)
    target=[int(c) for c in target];need=2*max(bound,max(abs(c) for c in target))+1
    product=1;c=(1<<62)-1-2*5000;checked=0
    while product<=need:
        while not is_prime(c):c-=2
        p=c;c-=2;product*=p
        MA=F.nmod_mat(q,q,[v%p for row in A for v in row],p);MB=F.nmod_mat(q,q,[v%p for row in B for v in row],p)
        for t in range(q+1):
            val=int((MA+MB*t).det()) if t else int(MA.det())
            z=0
            for cc in reversed(target):z=(z*t+cc)%p
            assert z==val,('row polynomial residue mismatch',p,t)
        checked+=1
    return checked


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser();ap.add_argument('--certificate',required=True);ap.add_argument('--sha256',required=True)
    args=ap.parse_args()
    C=json.loads(L.pinned({'file':args.certificate,'sha256':args.sha256}))
    a,b,_=C['degree'];k=C['entire_free_primitive_dimension']
    S=json.loads(L.pinned(C['inputs']['source']));P=json.loads(L.pinned(C['inputs']['pencil']));D=json.loads(L.pinned(C['inputs']['polynomial']))
    assert P['source_pencil_sha256']==C['inputs']['source']['sha256'] and D['pencil_sha256']==C['inputs']['pencil']['sha256']
    codes,V=[L.array(pin) for pin in S['files']];assert V.shape==(k,len(codes))
    G,degrees=L.literal_module();lookup={int(c):i for i,c in enumerate(codes)}
    W=V.copy();zero=np.zeros(len(codes),dtype=np.int64);three=zero.copy();seven=zero.copy()
    peak=max(abs(int(W.min())),abs(int(W.max())))
    for pos in range(7):
        assert peak*2**(pos+1)<2**63
        shift=3*(6-pos);letters=(codes>>shift)&7
        c3=np.flatnonzero(letters==3);c4=np.array([lookup[int(codes[i])^(7<<shift)] for i in c3],dtype=np.int64)
        x=W[:,c3].copy();y=W[:,c4].copy();W[:,c3]=x+y;W[:,c4]=x-y
        zero+=(letters==3)|(letters==4);three+=(letters==3);seven+=(letters==7)
    weights=np.array([2**(7-int(z))*3**int(t)*4**int(s) for z,t,s in zip(zero,three,seven)],dtype=np.int64)
    assert max(abs(int(W.min())),abs(int(W.max())))*int(weights.max())<2**63
    gram=F.fmpz_mat(k,k)
    for start in range(0,len(codes),2048):
        end=min(start+2048,len(codes))
        gram+=F.fmpz_mat((W[:,start:end]*weights[start:end]).tolist())*F.fmpz_mat(W[:,start:end].T.tolist())
    H=F.fmpq_mat(gram)*F.fmpq(1,128)
    assert digest(H)==C['source_gram_sha256'],'Hadamard Gram mismatch'
    fields=[F.fmpq_mat(k,k,[F.fmpq(P['matrix'][i][j][h]) for i in range(k) for j in range(k)]) for h in range(3)]
    rational={(e['x_power'],e['y_power']):Q(e['coefficient']) for e in D['coefficients']}
    common=math.lcm(*(c.denominator for c in rational.values()))
    ctx=F.fmpz_mpoly_ctx.get(('x','y'),'lex');X,Y=ctx.gens()
    poly=ctx.from_dict({m:int(c*common) for m,c in rational.items()})
    tests=[]
    for t in C['free_bound_tests']:
        moved=poly.compose(X-(7-t['bound']),Y-(7-t['bound'])).to_dict()
        ok=bool(moved.get((0,0),0)) and all(int(c)>0 for c in moved.values())
        tests.append({'bound':t['bound'],'all_positive_nonzero_constant':ok,'terms':len(moved)})
    assert tests==C['free_bound_tests'];b0=C['free_uniform_positive_bound']
    assert tests[-1]['bound']==b0 and tests[-1]['all_positive_nonzero_constant'] and all(not t['all_positive_nonzero_constant'] for t in tests[:-1])
    vpeak=max(abs(int(V.min())),abs(int(V.max())))

    def family(node,p):
        target=(a-1,b) if node==1 else (a,b-1)
        if min(target)<0 or p>6:return [],np.zeros((k,0),dtype=np.int64)
        q={(node,):1}
        for _ in range(p):q=L.bracket({(0,):1},q)
        q={w:-c for w,c in q.items()};gens=[];cols=[]
        for outer in itertools.product(range(8),repeat=6-p):
            if (sum(degrees[x][0] for x in outer),sum(degrees[x][1] for x in outer))!=target:continue
            y=q
            for x in reversed(outer):y=L.bracket({(x,):1},y)
            gens.append(list(outer));gy=Counter()
            for word,c in y.items():
                expansion={():c}
                for letter in word:
                    expansion={pre+(j,):val*G[j][letter] for pre,val in expansion.items() for j in range(8) if G[j][letter]}
                for w,val in expansion.items():gy[L.code(w)]+=val
            gy={w:c for w,c in gy.items() if c}
            if not gy:cols.append(np.zeros(k,dtype=np.int64));continue
            ix=np.array([lookup[w] for w in gy],dtype=np.int64);co=np.array(list(gy.values()),dtype=np.int64)
            assert vpeak*sum(abs(int(c)) for c in co)<2**63
            cols.append(V[:,ix]@co)
        return gens,(np.array(cols,dtype=np.int64).T if cols else np.zeros((k,0),dtype=np.int64))

    def ideal(cross):
        if cross.shape[1]==0:return F.fmpq_mat(k,0),[],list(range(k))
        rr,_,rank=F.fmpz_mat(cross.T.tolist()).rref()
        if rank==0:return F.fmpq_mat(k,0),[],list(range(k))
        ev=F.fmpq_mat(k,rank,[rr[j,i] for i in range(k) for j in range(rank)])
        red,r=H.solve(ev).transpose().rref();assert r==rank
        I=F.fmpq_mat(k,rank,[red[j,i] for i in range(k) for j in range(rank)])
        piv=[next(i for i in range(k) if red[j,i]) for j in range(rank)]
        return I,piv,[i for i in range(k) if i not in piv]

    def quotient(A,I,piv,free):
        q=len(free);d=I.ncols();cov=F.fmpq_mat(q,k);lift=F.fmpq_mat(k,q)
        for j,f in enumerate(free):
            cov[j,f]=1;lift[f,j]=1
            for t,p in enumerate(piv):cov[j,p]=-I[f,t]
        if d:assert cov*I==F.fmpq_mat(q,d) and cov*A*I==F.fmpq_mat(q,d)
        return cov*A*lift

    crosses={};row_primes=[];descendants=0
    for record in C['rows']:
        node,p=record['node'],record['parameter']
        gens,cross=family(node,p);descendants+=len(gens)
        assert gens==record['generator_outer_letters'] and hashlib.sha256(cross.tobytes()).hexdigest()==record['cross_sha256']
        I,piv,free=ideal(cross)
        assert I.ncols()==record['whole_projected_ideal_rank'] and digest(I)==record['ideal_basis_sha256']
        assert piv==record['ideal_pivot_coordinates'] and free==record['complement_coordinates']
        crosses[node,p]=cross
        if node==1:A=fields[0]+fields[1]*(p-7)+fields[2]*(b0-7);B=fields[2]
        else:A=fields[0]+fields[1]*(b0-7)+fields[2]*(p-7);B=fields[1]
        QA=quotient(A,I,piv,free);QB=quotient(B,I,piv,free)
        assert digest(QA)==record['quotient_A_sha256'] and digest(QB)==record['quotient_B_sha256']
        claimed=[Q(c) for c in record['determinant_coefficients']]
        row_primes.append(rowpoly_multimodular(QA,QB,claimed))
        base=record['certified_from_other_parameter']-b0
        moved=[sum((c*math.comb(j,i)*base**(j-i) for j,c in enumerate(claimed) if j>=i),Q(0)) for i in range(len(claimed))]
        assert moved[0]>0 and all(c>=0 for c in moved)
        print('PASS row',node,p,'quotient',len(free),flush=True)
    for corner in C['corners']:
        r,s=corner['parameters']
        parts=[crosses[1,r] if (1,r) in crosses else family(1,r)[1],crosses[2,s] if (2,s) in crosses else family(2,s)[1]]
        I,piv,free=ideal(np.concatenate(parts,axis=1))
        assert I.ncols()==corner['whole_ideal_rank'] and len(free)==corner['actual_primitive_dimension']
        Qbar=quotient(fields[0]+fields[1]*(r-7)+fields[2]*(s-7),I,piv,free)
        assert digest(Qbar)==corner['quotient_sha256']
        det=Qbar.det() if Qbar.nrows() else F.fmpq(1)
        assert det and str(det)==corner['determinant']
        print('PASS corner',r,s,'actual',len(free),flush=True)
    result={'owner':'MathKacMoody-2','input_file':args.certificate,'input_sha256':args.sha256,'degree':[a,b,7],
            'inputs':C['inputs'],'literal_helper':{'file':LITERAL,'sha256':LITERAL_SHA},
            'Hadamard_Gram_digest_matched':True,'free_bound_tests_mpoly_recomputed':True,'free_uniform_positive_bound':b0,
            'all_seed_descendants_reconstructed':descendants,'row_polynomial_primes':row_primes,
            'all_corner_determinants_recomputed':len(C['corners']),
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'numpy_version':np.__version__,'flint_version':F.__version__,
            'status':'PASS_ALTERNATE_WHOLE_ACTUAL_ALL_PARAMETER_TENSOR_TYPE',
            'limits':'Same owner and shared NumPy/FLINT; alternate algorithms. Written actual-source/projection/descent inputs pending review. No B7, parent, formal/kernel, configured-family/human, native-library or novelty acceptance.'}
    out=ROOT/args.certificate.replace('-v1.json','-replay-v1.json')
    with out.open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print('PASS tensor actual type replay',out.name,flush=True)


if __name__=='__main__':main()
