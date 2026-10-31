#!/usr/bin/env python3
"""Replay the ENTIRE actual level7 invariant two-seed corner.

No producer is imported. Fresh matrix-unit Gram; Hadamard-diagonal tensor
Gram rather than applying G to full vectors; tuple bracket trees rather than
packed-word adjoints; sparse G on ideal vectors rather than G on source.
Shares NumPy/FLINT and the pinned already-replayed free source/pencil.
"""
import argparse
import hashlib
import io
import itertools
import json
import math
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-fastalgebra'))
import flint


def pinned(pin):
    name=pin['file']
    assert isinstance(name,str) and Path(name).name==name
    raw=(ROOT/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==pin['sha256'],'pinned byte mismatch'
    return raw


def array(pin):
    stream=io.BytesIO(pinned(pin))
    result=np.load(stream,allow_pickle=False)
    assert stream.tell()==len(stream.getvalue()),'trailing array bytes'
    return result


def literal_module():
    def E(i,j):
        m=np.zeros((3,3),dtype=np.int64);m[i,j]=1
        return m
    B=[E(2,0),-E(2,1),E(1,0),E(0,0)-E(2,2),
       E(0,0)-E(1,1),-E(0,1),-E(1,2),-2*E(0,2)]
    G=[[int(np.trace(a@b.T)) for b in B] for a in B]
    assert G==[[int(i==j) if i not in (3,4,7) else
                (2 if i==j else 1 if j in (3,4) else 0) if i in (3,4) else
                (4 if j==7 else 0) for j in range(8)] for i in range(8)]
    H=[E(0,0)-E(1,1),E(1,1)-E(2,2)]
    degrees=[]
    for b in B:
        weights=[]
        for h in H:
            candidates=[w for w in range(-2,3) if np.array_equal(h@b-b@h,w*b)]
            assert len(candidates)==1
            weights.append(candidates[0])
        a=2*weights[0]+weights[1]+3
        c=weights[0]+2*weights[1]+3
        assert a%3==c%3==0
        degrees.append((a//3,c//3))
    return G,degrees


def bracket(a,b):
    out=Counter()
    for u,x in a.items():
        for v,y in b.items():
            out[u+v]+=x*y
            out[v+u]-=x*y
    return {w:c for w,c in out.items() if c}


def code(word):
    out=0
    for a in word:out=8*out+a
    return out


def matrix(rows):
    return flint.fmpq_mat([[flint.fmpq(str(v)) for v in row] for row in rows])


def strings(M):
    return [[str(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser()
    ap.add_argument('--certificate',required=True)
    ap.add_argument('--sha256',required=True)
    args=ap.parse_args()
    raw=pinned({'file':args.certificate,'sha256':args.sha256})
    C=json.loads(raw)
    assert C['parameters']==[2,2] and C['degree']==[7,7,7]
    S=json.loads(pinned(C['source']))
    R=json.loads(pinned(C['source_replay']))
    P=json.loads(pinned(C['canonical_pencil']))
    assert R['status']=='PASS_LITERAL_ENTIRE_INVARIANT_SOURCE_AND_BYTE_SEED_REPLAY'
    assert R['input_sha256']==C['source']['sha256']
    assert P['source_pencil_sha256']==C['source']['sha256']
    words,V=[array(p) for p in S['files']]
    assert words.dtype==np.dtype('uint32') and V.dtype==np.dtype('int64')
    assert V.shape==(100,104960) and words.shape==(104960,)
    assert np.all(words[1:]>words[:-1])
    maximum=max(abs(int(V.min())),abs(int(V.max())))
    assert maximum<=6048
    lookup={int(w):i for i,w in enumerate(words)}
    G,degrees=literal_module()

    # Independent orthogonal sum/difference factorization:
    # [[2,1],[1,2]]=H diag(3,1) H^T/2, H=[[1,1],[1,-1]].
    W=V.copy()
    zero=np.zeros(len(words),dtype=np.int64)
    three=np.zeros(len(words),dtype=np.int64)
    seven=np.zeros(len(words),dtype=np.int64)
    for pos in range(7):
        shift=3*(6-pos);letters=(words>>shift)&7
        c3=np.flatnonzero(letters==3)
        c4=np.array([lookup[int(words[i])^(7<<shift)] for i in c3],dtype=np.int64)
        a=W[:,c3].copy();b=W[:,c4].copy()
        assert maximum*2**(pos+1)<2**63
        W[:,c3]=a+b;W[:,c4]=a-b
        zero+=(letters==3)|(letters==4)
        three+=(letters==3);seven+=(letters==7)
    weights=np.array([2**(7-int(z))*3**int(t)*4**int(s) for z,t,s in zip(zero,three,seven)],dtype=np.int64)
    scaled_gram=flint.fmpz_mat(100,100)
    unweighted_bounds=[]
    for weight in np.unique(weights):
        ix=np.flatnonzero(weights==weight)
        block=W[:,ix]
        peak=max(abs(int(block.min())),abs(int(block.max())))
        bound=peak*peak*len(ix)
        assert bound<2**63
        unweighted_bounds.append(bound)
        scaled_gram+=flint.fmpz_mat((block@block.T).tolist())*int(weight)
    saved_gram=flint.fmpz_mat(C['source_gram'])
    assert scaled_gram==saved_gram*128,'entire tensor Gram mismatch'
    print('PASS independent Hadamard entire100x100 Gram',flush=True)

    regenerated=[];columns=[]
    for seed_letter in (1,2):
        for outer in itertools.product(range(8),repeat=4):
            da=sum(degrees[a][0] for a in outer)+degrees[seed_letter][0]
            db=sum(degrees[a][1] for a in outer)+degrees[seed_letter][1]
            if (da,db)!=(7,7):continue
            q=bracket({(0,):1},bracket({(0,):1},{(seed_letter,):1}))
            y={w:-v for w,v in q.items()}
            for a in reversed(outer):y=bracket({(a,):1},y)
            terms=sorted((code(w),int(c)) for w,c in y.items())
            regenerated.append({'seed_letter':seed_letter,'outer_letters':list(outer),
                                'whole_word_terms':[[w,c] for w,c in terms]})
            # Push G onto each sparse ideal vector, the opposite direction
            # from the producer's full-source metric application.
            gy=Counter()
            for w,c in y.items():
                expansion={():c}
                for letter in w:
                    expansion={u+(j,):value*G[j][letter]
                               for u,value in expansion.items() for j in range(8) if G[j][letter]}
                for u,value in expansion.items():gy[code(u)]+=value
            gy={w:c for w,c in gy.items() if c}
            ix=np.array([lookup[w] for w in gy],dtype=np.int64)
            coefficients=np.array(list(gy.values()),dtype=np.int64)
            assert maximum*sum(abs(int(c)) for c in coefficients)<2**63
            columns.append(V[:,ix]@coefficients)
    assert len(regenerated)==80 and regenerated==C['generators']
    cross=np.array(columns,dtype=np.int64).T
    assert cross.tolist()==C['cross_inner_products'],'whole ideal cross Gram mismatch'
    print('PASS all80 tuple-tree seed descendants and opposite-direction cross pairings',flush=True)

    coordinates=flint.fmpq_mat(saved_gram).solve(flint.fmpq_mat(cross.tolist()))
    assert strings(coordinates)==C['projected_ideal_coordinates']
    rr,rank=coordinates.transpose().rref()
    assert rank==C['whole_ideal_rank']==26
    single=[]
    for start in (0,40):
        single.append(matrix([[coordinates[i,j] for j in range(start,start+40)] for i in range(100)]).rank())
    assert single==C['single_seed_ranks']==[15,15]
    assert sum(single)-rank==C['overlap_dimension']==4
    I=matrix([[rr[j,i] for j in range(rank)] for i in range(100)])
    assert strings(I)==C['ideal_basis']
    pivots=[next(i for i in range(100) if rr[j,i]) for j in range(rank)]
    free=[i for i in range(100) if i not in pivots]
    assert pivots==C['ideal_pivot_coordinates'] and free==C['complement_coordinates']
    A=matrix([[flint.fmpq(e[0])-5*flint.fmpq(e[1])-5*flint.fmpq(e[2]) for e in row] for row in P['matrix']])
    AI=A*I
    T=matrix([[AI[i,j] for j in range(rank)] for i in pivots])
    assert AI==I*T,'whole ideal not contraction-stable'
    Q=matrix([[A[i,j]-sum(I[i,k]*A[p,j] for k,p in enumerate(pivots)) for j in free] for i in free])
    assert len(free)==C['actual_invariant_dimension']==74
    assert strings(Q)==C['induced_contraction_matrix']
    determinant=Q.det()
    assert determinant and str(determinant)==C['induced_contraction_determinant']
    assert 100-A.rank()==C['free_contraction_nullity']==2
    result={'owner':'MathKacMoody-2','input_file':args.certificate,'input_sha256':args.sha256,
            'source':C['source'],'source_replay':C['source_replay'],'canonical_pencil':C['canonical_pencil'],
            'entire_free_invariant_dimension':100,'all_seed_descendants_replayed':80,
            'entire_source_gram_entries_reconstructed':10000,
            'cross_pairings_reconstructed':8000,'single_seed_invariant_ranks':single,
            'whole_two_seed_ideal_rank':rank,'seed_overlap_dimension':4,
            'entire_actual_invariant_dimension':len(free),'free_contraction_nullity':2,
            'whole_ideal_contraction_stability_checked':True,
            'entire_actual_quotient_contraction_dimension':len(free),
            'nonzero_quotient_determinant':str(determinant),
            'max_unweighted_Hadamard_dot_int64_bound':max(unweighted_bounds),
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'numpy_version':np.__version__,'flint_version':flint.__version__,
            'status':'PASS_ENTIRE_ACTUAL74_INVARIANT_TWO_SEED_CORNER',
            'limits':'Different whole Gram/seed-expansion/projection algorithms, same owner and NumPy/FLINT libraries. Actual-source, complete ideal-projection and canonical-kernel written proofs remain explicit inputs. No target-adjoint dimension at parameter2, human/configured-family/formal/kernel, parent/scientific or novelty acceptance.'}
    output=args.certificate.removesuffix('-v1.json')+'-replay-v1.json'
    with (ROOT/output).open('x') as stream:
        json.dump(result,stream,indent=2);stream.write('\n')
    print('PASS ENTIRE actual74-source invariant corner',output,flush=True)


if __name__=='__main__':main()
