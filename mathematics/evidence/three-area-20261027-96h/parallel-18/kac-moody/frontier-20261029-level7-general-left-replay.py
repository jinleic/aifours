#!/usr/bin/env python3
"""Alternate WHOLE source and canonical-pencil replay for any level7 root.

Imports only the pinned literal LEFT core (matrix-unit actions, cyclic theta
negatives, prefix-moved local F3) and generalizes its two transports from
root(n,n) to root(a,b). Source checks: exhaustive recursive word universe,
literal f1/f2 lowest condition, Dynkin-Specht-Wever Lie membership
theta(v)=7v for EVERY vector, independence by a nonzero detector minor, and
independent Witt/Weyl completeness. Every canonical matrix entry of the pinned
RIGHT-transport pencil must be reproduced exactly.
"""
import argparse
import hashlib
import importlib.util
import io
import json
import math
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
CORE='frontier-20261029-trace-invariant-left-core.py'
CORE_SHA='79e80f81715e04f930f9cca29015a32870c495d8448055a2273b95a34d7ab352'
N=7


def load_core():
    raw=(ROOT/CORE).read_bytes();assert hashlib.sha256(raw).hexdigest()==CORE_SHA
    spec=importlib.util.spec_from_file_location('literal_left_core',ROOT/CORE)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m


core=load_core();flint=core.flint


def affine_f3_left(source,target,a,b):
    n=N
    codes,_=source.root(a,b);out_codes,out_index=target.root(a,b)
    letters=[((codes>>np.uint32(3*(n-1-i)))&np.uint32(7)) for i in range(n)]
    maps=[[],[],[]];tails={g:[[],[],[]] for g in ('h3','e1','e2','e12')}
    shifts={'h3':(0,0),'e1':(1,0),'e2':(0,1),'e12':(1,1)}
    table=core.independent_local_f3(n)
    for k in range(n):
        shift=3*(n-1-k)
        shortened=((codes>>(shift+3))<<shift)|(codes&np.uint32((1<<shift)-1))
        for j,terms in enumerate(table):
            for g,co in terms:
                inputs=np.flatnonzero(letters[k]==j).astype(np.int32)
                a0,b0=shifts[g]
                _,tail_index=target.root(a-a0,b-b0)
                outputs=tail_index[shortened[inputs]]
                for piece,c in enumerate(co):tails[g][piece].append((inputs,outputs,c))
                for ell in range(k):
                    action_shift=3*(n-2-ell)
                    for old in range(8):
                        selected=np.flatnonzero((letters[k]==j)&(letters[ell]==old)).astype(np.int32)
                        if not len(selected):continue
                        if g=='h3':
                            assert co[1]==co[2]==0
                            x,y=core.WEIGHTS[old]
                            choices={old:tuple(-co[0]*z for z in (4-2*n*(x+y),-2*x,-2*y))}
                        else:
                            choices={new:tuple(-c*act for c in co) for new,act in core.ACTION[g][old].items()}
                        for new,values in choices.items():
                            changed=shortened[selected].astype(np.int64)+(new-old)*(1<<action_shift)
                            assert np.all(changed>=0) and np.all(changed<len(target.all))
                            outputs=out_index[changed]
                            for piece,c in enumerate(values):maps[piece].append((selected,outputs,int(c)))
    f3=[core.Transfer(len(codes),len(out_codes),part) for part in maps]
    tail_checks=[]
    for g,parts in tails.items():
        x,y=shifts[g];tail_codes,_=target.root(a-x,b-y)
        tail_checks.extend(core.Transfer(len(codes),len(tail_codes),part) for part in parts)
    return f3,tail_checks


def canonical_left(d,word_space,source_space,a,b,outer_cache):
    n=N;negative=[]
    for word in core.CYCLIC:
        vector=d;root=(a,b);denominator=1
        for g in reversed(word):
            if g=='e12':
                r1,F1=word_space.action(root,'f1');r2,F2=word_space.action(root,'f2')
                rr,F2after=word_space.action(r1,'f2');rr2,F1after=word_space.action(r2,'f1');assert rr==rr2
                vector=core.difference(F2after.apply(F1.apply(vector)),F1after.apply(F2.apply(vector)))
                root=rr;denominator*=4
            else:
                root,operator=word_space.action(root,'f1' if g=='e1' else 'f2')
                vector=operator.apply(vector);denominator*=2
        negative.append((root,vector,denominator,(-1)**len(word)))
    common=math.lcm(*(Q(core.GINV[i][j]*sign,den).denominator for j,(root,v,den,sign) in enumerate(negative) for i in range(8)))
    source_codes,source_index=source_space.root(a,b)
    terms=[];bound=0
    for j,(degree,v,den,sign) in enumerate(negative):
        for i in range(8):
            factor=common*core.GINV[i][j]*sign/den;assert factor.denominator==1;factor=int(factor)
            if not factor:continue
            key=(i,degree)
            if key not in outer_cache:
                codes,_=word_space.root(*degree)
                left=source_index[(np.uint32(i)<<np.uint32(3*(n-1)))|codes]
                right=source_index[(codes<<np.uint32(3))|np.uint32(i)]
                assert np.all(left>=0) and np.all(right>=0)
                outer_cache[key]=(left,right)
            terms.append((v,*outer_cache[key],factor));bound+=2*abs(factor)*core.maximum(v)
    assert bound<core.LIMIT
    out=np.zeros(len(source_codes),dtype=np.int64)
    for v,left,right,factor in terms:out[left]+=factor*v;out[right]-=factor*v
    return out,common


def dynkin_maps(codes,lookup):
    letters=np.stack([((codes>>np.uint32(3*(N-1-i)))&np.uint32(7)).astype(np.int64) for i in range(N)])
    maps=[]
    for mask in range(1<<(N-1)):
        left=[i for i in range(1,N) if mask>>(i-1)&1];right=[i for i in range(1,N) if not mask>>(i-1)&1]
        order=list(reversed(left))+[0]+right
        new=np.zeros(len(codes),dtype=np.int64)
        for p in order:new=new*8+letters[p]
        idx=np.array([lookup[int(c)] for c in new],dtype=np.int64)
        assert len(np.unique(idx))==len(idx)
        maps.append(((-1)**len(left),idx))
    return maps


def witt_lowest(a,b):
    ch=Counter({(0,0):1})
    for _ in range(N):
        nxt=Counter()
        for (u,v),c in ch.items():
            for x,y in core.WEIGHTS:nxt[u+x,v+y]+=c
        ch=nxt
    def lie(x,y):
        if x<0 or y<0:return 0
        extra=sum(1 for w in core.WEIGHTS if x%N==0 and y%N==0 and w==(x//N,y//N))
        assert (ch[x,y]-extra)%N==0
        return (ch[x,y]-extra)//N
    return lie(a,b)-lie(a-1,b)-lie(a,b-1)+lie(a-2,b-1)+lie(a-1,b-2)-lie(a-2,b-2)


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser()
    ap.add_argument('--pencil',required=True);ap.add_argument('--pencil-sha256',required=True)
    ap.add_argument('--block-size',type=int,default=512)
    args=ap.parse_args();assert Path(args.pencil).name==args.pencil
    raw=(ROOT/args.pencil).read_bytes();assert hashlib.sha256(raw).hexdigest()==args.pencil_sha256
    P=json.loads(raw);a,b,n=P['degree'];assert n==N
    sraw=(ROOT/P['source_pencil']).read_bytes();assert hashlib.sha256(sraw).hexdigest()==P['source_pencil_sha256']
    S=json.loads(sraw);assert S['files']==P['source_files']
    arrays=[]
    for pin in S['files']:
        data=(ROOT/pin['file']).read_bytes();assert hashlib.sha256(data).hexdigest()==pin['sha256']
        stream=io.BytesIO(data);arrays.append(np.load(stream,allow_pickle=False));assert stream.tell()==len(data)
    words,vectors=arrays;k=P['entire_primitive_dimension']
    assert vectors.shape==(k,len(words)) and k==S['entire_lowest_dimension']==witt_lowest(a,b)
    source=core.Words(N);target=core.Words(N-1)
    exhaustive,_=source.root(a,b);assert np.array_equal(exhaustive,words)
    lookup={int(c):i for i,c in enumerate(words)}
    maps=dynkin_maps(words,lookup)
    assert 64*core.maximum(vectors.ravel())<core.LIMIT
    for v in vectors:
        theta=np.zeros_like(v)
        for sign,idx in maps:theta[idx]+=sign*v
        assert np.array_equal(theta,7*v),'Dynkin-Specht-Wever Lie membership failed'
    detectors=S['coefficient_detector_indices'];assert detectors==P['coefficient_detector_indices']
    minor=flint.fmpz_mat(vectors[:,detectors].T.tolist());assert minor.det()
    inverse=flint.fmpq_mat(minor).inv()
    F3,tails=affine_f3_left(source,target,a,b)
    _,F1=source.action((a,b),'f1');_,F2=source.action((a,b),'f2')
    images=[np.empty_like(vectors) for _ in range(3)];cache={};normalization=None
    for j,v in enumerate(vectors):
        assert not np.any(F1.apply(v)) and not np.any(F2.apply(v)),'literal lowest condition failed'
        for tail in tails:assert not np.any(tail.apply(v)),'left tail did not cancel'
        for piece,op in enumerate(F3):
            image,common=canonical_left(op.apply(v),target,source,a,b,cache)
            if normalization is None:normalization=2*common
            assert normalization==2*common
            assert not np.any(F1.apply(image)) and not np.any(F2.apply(image))
            images[piece][j]=image
        if (j+1)%100==0 or j+1==k:print('LEFT images',(a,b,7),j+1,'of',k,flush=True)
    blocks=[]
    for piece,image in enumerate(images):
        M=inverse*flint.fmpq_mat(image[:,detectors].T.tolist())
        den=math.lcm(*(int(M[i,j].denominator) for i in range(k) for j in range(k)))
        integer=flint.fmpz_mat(k,k,[int(M[i,j]*den) for i in range(k) for j in range(k)])
        checked=0
        for start in range(0,len(words),args.block_size):
            end=min(start+args.block_size,len(words))
            A=flint.fmpz_mat(vectors[:,start:end].T.tolist())
            B=flint.fmpz_mat((image[:,start:end].T.astype(object)*den).tolist())
            assert A*integer==B,'LEFT full word reconstruction mismatch';checked+=1
        for i in range(k):
            for j in range(k):
                assert Q(int(M[i,j].numerator),int(M[i,j].denominator))/normalization==Q(P['matrix'][i][j][piece]),('LEFT/RIGHT mismatch',piece,i,j)
        blocks.append(checked);print('PASS LEFT piece',piece,'blocks',checked,flush=True)
    result={'owner':'MathKacMoody-2','degree':[a,b,7],'pencil':{'file':args.pencil,'sha256':args.pencil_sha256},
            'source':{'file':P['source_pencil'],'sha256':P['source_pencil_sha256']},'entire_lowest_dimension':k,
            'whole_word_universe':len(words),'all_vectors_Dynkin_Lie_membership':True,'all_vectors_literal_lowest':True,
            'independent_Witt_Weyl_completeness':k,'detector_minor_nonzero':True,
            'computed_LEFT_normalization':normalization,'all3_entire_word_reconstructions':blocks,
            'every_canonical_matrix_entry_reproduced':k*k*3,
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'literal_core':{'file':CORE,'sha256':CORE_SHA},
            'numpy_version':np.__version__,'flint_version':flint.__version__,
            'status':'PASS_ALTERNATE_WHOLE_SOURCE_AND_LEFT_CANONICAL_PENCIL',
            'limits':'Same owner; shared word-index framing and NumPy/FLINT; mathematically different LEFT transport, literal matrix-unit actions and cyclic negatives. D3-kernel containment and actual quotient transport remain WRITTEN inputs. No parent/formal/configured-family/human/novelty acceptance.'}
    out=ROOT/f'frontier-20261029-level7-{a}{b}-general-left-replay-v1.json'
    with out.open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print('PASS alternate whole source and LEFT pencil',(a,b,7),out.name,flush=True)


if __name__=='__main__':main()
