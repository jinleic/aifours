#!/usr/bin/env python3
"""Full word-level canonical operator on an ENTIRE trace/Dynkin invariant source.

Bound loaded NPY bytes, construct the actual affine F3 operator by rightward
Cartan transport, check EVERY right degree-zero tail, then use ALL8 actual
negative local directions and the finite-Levi trace dual. Every resulting word
vector is checked horizontal. Exact rational coefficients are solved on the
pinned nonzero coefficient minor, and ALL word coordinates are reconstructed
in bounded integer-matrix blocks. No14994-column horizontal nullspace, FFT
spanning assumption, discarded source/target words, floats or numerical rank.
"""
import argparse
import hashlib
import importlib.util
import io
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('literal_local_actions',ROOT/'frontier-20261029-level6-canonical-contraction.py')
local=importlib.util.module_from_spec(spec)
spec.loader.exec_module(local)
flint=local.flint
LIMIT=2**63


def maximum(v):
    return int(np.max(np.abs(v))) if len(v) else 0


class Words:
    def __init__(self,n):
        self.n=n
        self.all=np.arange(8**n,dtype=np.uint32)
        self.a=np.zeros(len(self.all),dtype=np.int16)
        self.b=np.zeros(len(self.all),dtype=np.int16)
        weights=np.array(local.levi.WEIGHTS,dtype=np.int16)
        for i in range(n):
            letters=(self.all>>np.uint32(3*(n-1-i)))&np.uint32(7)
            self.a+=weights[letters,0]
            self.b+=weights[letters,1]
        self.roots={}
        self.actions={}

    def root(self,a,b):
        key=(a,b)
        if key not in self.roots:
            codes=self.all[(self.a==a)&(self.b==b)]
            index=np.full(len(self.all),-1,dtype=np.int32)
            index[codes]=np.arange(len(codes),dtype=np.int32)
            self.roots[key]=(codes,index)
        return self.roots[key]

    def action(self,root,g):
        key=(root,g)
        if key not in self.actions:
            a,b=root
            target=(a-1,b) if g=='f1' else (a,b-1)
            codes,_=self.root(a,b)
            target_codes,target_index=self.root(*target)
            maps=[]
            for position in range(self.n):
                shift=3*(self.n-1-position)
                letters=(codes>>np.uint32(shift))&np.uint32(7)
                for old,row in enumerate(local.ACTION[g]):
                    inputs=np.flatnonzero(letters==old).astype(np.int32)
                    for new,c in row.items():
                        changed=codes[inputs].astype(np.int64)+(new-old)*(1<<shift)
                        assert np.all(changed>=0) and np.all(changed<len(self.all))
                        outputs=target_index[changed]
                        maps.append((inputs,outputs,int(c)))
            self.actions[key]=(target,Transfer(len(codes),len(target_codes),maps))
        return self.actions[key]


class Transfer:
    def __init__(self,inputs,outputs,maps):
        self.inputs=inputs
        self.outputs=outputs
        self.maps=[]
        rows=np.zeros(outputs,dtype=np.int64)
        for source,target,c in maps:
            if not c or not len(source):
                continue
            assert np.all(source>=0) and np.all(source<inputs)
            assert np.all(target>=0) and np.all(target<outputs)
            assert len(np.unique(target))==len(target)
            assert len(source)==len(target)
            self.maps.append((source,target,c))
            rows[target]+=abs(c)
        self.norm=maximum(rows)

    def apply(self,v):
        assert v.dtype==np.dtype('int64') and len(v)==self.inputs
        assert self.norm*maximum(v)<LIMIT, 'int64 transfer bound not established'
        out=np.zeros(self.outputs,dtype=np.int64)
        for source,target,c in self.maps:
            out[target]+=c*v[source]
        return out


def affine_f3(source,target,n):
    codes,_=source.root(n,n)
    out_codes,out_index=target.root(n,n)
    letters=[((codes>>np.uint32(3*(n-1-i)))&np.uint32(7)) for i in range(n)]
    maps=[[],[],[]]
    tails={g:[[],[],[]] for g in ('h3','e1','e2','e12')}
    tail_roots={'h3':(n,n),'e1':(n-1,n),'e2':(n,n-1),'e12':(n-1,n-1)}
    local_brackets=[('h3',(-1,0,0)),('e1',(-n,-1,0)),('e2',(-n,0,-1)),('e12',(-2*n,-1,-1)),('e12',(-n,0,-1))]
    for k in range(n):
        shift=3*(n-1-k)
        shortened=((codes>>(shift+3))<<shift)|(codes&np.uint32((1<<shift)-1))
        for j,(g,co) in enumerate(local_brackets):
            inputs=np.flatnonzero(letters[k]==j).astype(np.int32)
            _,tail_index=target.root(*tail_roots[g])
            outputs=tail_index[shortened[inputs]]
            for piece,c in enumerate(co):
                tails[g][piece].append((inputs,outputs,c))
            for ell in range(k+1,n):
                # When removing an EARLIER letter, the old suffix bit shift
                # is unchanged in the shortened packed word.
                action_shift=3*(n-1-ell)
                for old in range(8):
                    selected=np.flatnonzero((letters[k]==j)&(letters[ell]==old)).astype(np.int32)
                    if not len(selected):
                        continue
                    if g=='h3':
                        a,b=local.levi.WEIGHTS[old]
                        choices={old:(-4+2*n*(a+b),2*a,2*b)}
                    else:
                        choices={new:tuple(c*act for c in co) for new,act in local.ACTION[g][old].items()}
                    for new,values in choices.items():
                        changed=shortened[selected].astype(np.int64)+(new-old)*(1<<action_shift)
                        assert np.all(changed>=0) and np.all(changed<len(target.all))
                        outputs=out_index[changed]
                        for piece,c in enumerate(values):
                            maps[piece].append((selected,outputs,int(c)))
    f3=[Transfer(len(codes),len(out_codes),part) for part in maps]
    tail_checks=[]
    for g,parts in tails.items():
        tail_codes,_=target.root(*tail_roots[g])
        tail_checks.extend(Transfer(len(codes),len(tail_codes),part) for part in parts)
    return f3,tail_checks


def difference(a,b):
    assert a.shape==b.shape and maximum(a)+maximum(b)<LIMIT
    return a-b


def canonical_96(d,word_space,source_space,n,outer_cache):
    root=(n,n)
    r1,F1=word_space.action(root,'f1')
    r2,F2=word_space.action(root,'f2')
    f1=F1.apply(d)
    f2=F2.apply(d)
    rr,F2_after1=word_space.action(r1,'f2')
    rr2,F1_after2=word_space.action(r2,'f1')
    assert rr==rr2
    f21=F2_after1.apply(f1)
    f12=F1_after2.apply(f2)
    h=difference(f21,f12)
    r5,H1=word_space.action(rr,'f1')
    r6,H2=word_space.action(rr,'f2')
    h1=H1.apply(h)
    h2=H2.apply(h)
    r7,H12=word_space.action(r6,'f1')
    h12=H12.apply(h2)
    negative=[(root,d,1,1),(r1,f1,2,-1),(r2,f2,2,-1),(rr,h,4,-1),
              (rr,f12,4,1),(r5,h1,8,1),(r6,h2,8,1),(r7,h12,8,-1)]
    source_codes,source_index=source_space.root(n,n)
    terms=[]
    bound=0
    for j,(degree,v,den,sign) in enumerate(negative):
        for i in range(8):
            factor=96*local.GINV[i][j]*sign/den
            assert factor.denominator==1
            factor=int(factor)
            if not factor:
                continue
            key=(i,degree)
            if key not in outer_cache:
                codes,_=word_space.root(*degree)
                left=source_index[(np.uint32(i)<<np.uint32(3*(n-1)))|codes]
                right=source_index[(codes<<np.uint32(3))|np.uint32(i)]
                assert np.all(left>=0) and np.all(right>=0)
                assert len(np.unique(left))==len(left) and len(np.unique(right))==len(right)
                outer_cache[key]=(left,right)
            terms.append((v,*outer_cache[key],factor))
            bound+=2*abs(factor)*maximum(v)
    assert bound<LIMIT, 'int64 complete outer-bracket bound not established'
    out=np.zeros(len(source_codes),dtype=np.int64)
    for v,left,right,factor in terms:
        out[left]+=factor*v
        out[right]-=factor*v
    return out


def qmatrix(rows):
    return flint.fmpq_mat([[flint.fmpq(Q(c).numerator,Q(c).denominator) for c in row] for row in rows])


def load_array(pin):
    raw=(ROOT/pin['file']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==pin['sha256']
    array=np.load(io.BytesIO(raw),allow_pickle=False)
    return array


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--grade',type=int,choices=[5,7],required=True)
    ap.add_argument('--source-sha256',required=True)
    ap.add_argument('--block-size',type=int,default=512)
    args=ap.parse_args()
    n=args.grade
    assert 1<=args.block_size<=4096
    name=f'frontier-20261029-level{n}-trace-dynkin-invariants-v1.json'
    raw=(ROOT/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==args.source_sha256
    C=json.loads(raw)
    assert C['grade']==n and C['root_degree']==[n,n,n]
    assert C['status']=='COMPLETE_EXACT_TRACE_DYNKIN_INVARIANT_SOURCE_CANDIDATE'
    words=load_array(C['files'][0])
    vectors=load_array(C['files'][1])
    k=C['entire_primitive_invariant_dimension']
    assert k==({5:6,7:100}[n]) and vectors.shape==(k,len(words))
    assert vectors.dtype==np.dtype('int64') and words.dtype==np.dtype('uint32')
    source=Words(n)
    target=Words(n-1)
    expected,_=source.root(n,n)
    assert np.array_equal(words,expected), 'word universe mismatch or omitted words'
    detectors=C['coefficient_detector_indices']
    assert len(detectors)==k==len(set(detectors)) and all(0<=j<len(words) for j in detectors)
    coefficient_minor=qmatrix(vectors[:,detectors].T.tolist())
    assert coefficient_minor.det()
    inverse=coefficient_minor.inv()
    path=ROOT/f'frontier-20261029-level{n}-trace-dynkin-canonical-pencil-v1.json'
    if path.exists():
        raise FileExistsError(path)
    F3,tails=affine_f3(source,target,n)
    _,source_f1=source.action((n,n),'f1')
    _,source_f2=source.action((n,n),'f2')
    images=[np.empty_like(vectors) for _ in range(3)]
    outer_cache={}
    for i,v in enumerate(vectors):
        assert not np.any(source_f1.apply(v)) and not np.any(source_f2.apply(v))
        for tail in tails:
            assert not np.any(tail.apply(v)), 'actual right degree-zero Cartan/Levi tail did not cancel'
        for piece,operator in enumerate(F3):
            d=operator.apply(v)
            out=canonical_96(d,target,source,n,outer_cache)
            assert not np.any(source_f1.apply(out)) and not np.any(source_f2.apply(out))
            images[piece][i]=out
        if (i+1)%10==0 or i+1==k:
            print('ENTIRE WORD invariant canonical',n,i+1,'of',k,'words',len(words),flush=True)
    matrices=[]
    check_blocks=[]
    for piece,image in enumerate(images):
        M=inverse*qmatrix(image[:,detectors].T.tolist())
        denominator=math.lcm(*(int(M[i,j].denominator) for i in range(k) for j in range(k)))
        integer_coefficients=flint.fmpz_mat([[int(M[i,j]*denominator) for j in range(k)] for i in range(k)])
        blocks=0
        for start in range(0,len(words),args.block_size):
            end=min(start+args.block_size,len(words))
            A=flint.fmpz_mat(vectors[:,start:end].T.tolist())
            B=flint.fmpz_mat([[int(image[j,w])*denominator for j in range(k)] for w in range(start,end)])
            assert A*integer_coefficients==B, 'full canonical word-coordinate reconstruction failed'
            blocks+=1
        matrices.append([[Q(int(M[i,j].numerator),int(M[i,j].denominator))/192 for j in range(k)] for i in range(k)])
        check_blocks.append(blocks)
        print('PASS EVERY invariant word coordinate',n,'piece',piece,'blocks',blocks,flush=True)
    entries=[[[matrices[piece][i][j] for piece in range(3)] for j in range(k)] for i in range(k)]
    record={'owner':'MathKacMoody-2','degree':[n,n,n],'variable_meaning':f'x=r-{n},y=s-{n}',
            'source_pencil':name,'source_pencil_sha256':args.source_sha256,'source_files':C['files'],
            'source_basis_representation':'ENTIRE literal tensor-word invariant basis, NOT a Lyndon-coordinate nullspace',
            'entire_primitive_dimension':k,'whole_tensor_weight_word_count':len(words),
            'matrix':[[[str(c) for c in e] for e in row] for row in entries],
            'coefficient_detector_indices':detectors,'all_source_and_output_full_f1_f2_checks':True,
            'all_affine_right_degree_zero_tails_cancelled':True,'all3_entire_word_coordinate_reconstructions':True,
            'word_coordinate_block_size':args.block_size,'blocks_per_affine_piece':check_blocks,
            'canonical_normalization':'F3 operators produce2*F3; canonical outer sum produces96*Omega, hence divide192',
            'f3_affine_integer_operator_norms':[operator.norm for operator in F3],
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'integer_local_helper_sha256':hashlib.sha256((ROOT/'frontier-20261029-level6-canonical-contraction.py').read_bytes()).hexdigest(),
            'numpy_version':np.__version__,'flint_version':flint.__version__,
            'status':'COMPLETE_EXACT_WORD_LEVEL_INVARIANT_CANONICAL_PENCIL_CANDIDATE',
            'limits':'Entire source/target word arithmetic checked with explicit int64 bounds and arbitrary-integer full matrix identities; input source membership/completeness and D3-kernel containment require the named written proofs. No determinant sign, D3 injectivity, scientific review, parent, formal/kernel, independent-library or novelty acceptance inferred.'}
    with path.open('x') as stream:
        json.dump(record,stream,indent=2)
        stream.write('\n')
    print('WROTE',path.name,'ENTIRE invariant dimension',k,'word rows',len(words),flush=True)


if __name__=='__main__':
    main()
