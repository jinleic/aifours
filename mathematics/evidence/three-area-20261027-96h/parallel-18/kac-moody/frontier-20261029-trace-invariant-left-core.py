#!/usr/bin/env python3
"""Alternate LEFT-transport/seed-regeneration replay of a whole invariant map.

Bound loaded NPY bytes, reconstruct the actual affine F3 operator by LEFTWARD
Cartan transport, check EVERY right degree-zero tail, then use ALL8 actual
negative local directions and the finite-Levi trace dual. Every resulting word
vector is checked horizontal. Exact rational coefficients are solved on the
pinned nonzero coefficient minor, and ALL word coordinates are reconstructed
in bounded integer-matrix blocks. No14994-column horizontal nullspace, FFT
spanning assumption, discarded source/target words, floats or numerical rank.
"""
import argparse
import hashlib
import io
import sys
import itertools
from collections import Counter
from functools import lru_cache
from multiprocessing import Pool
from types import SimpleNamespace
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-fastalgebra'))
import flint


def unit(i,j):
    out=np.zeros((3,3),dtype=np.int64)
    out[i,j]=1
    return out


BASIS=[unit(2,0),-unit(2,1),unit(1,0),unit(0,0)-unit(2,2),
       unit(0,0)-unit(1,1),-unit(0,1),-unit(1,2),-2*unit(0,2)]
OPS={'e1':unit(0,1),'e2':unit(1,2),'e12':unit(0,2),'f1':unit(1,0),'f2':unit(2,1)}
CYCLIC=[(),('e1',),('e2',),('e12',),('e1','e2'),('e12','e1'),('e12','e2'),('e12','e12')]


def bracket(A,B):
    return A@B-B@A


def coordinates2(A):
    co=[2*int(A[2,0]),-2*int(A[2,1]),2*int(A[1,0]),-2*int(A[2,2]),
        -2*int(A[1,1]),-2*int(A[0,1]),-2*int(A[1,2]),-int(A[0,2])]
    reconstructed=sum((c*M for c,M in zip(co,BASIS)),np.zeros((3,3),dtype=np.int64))
    assert np.array_equal(reconstructed,2*A)
    return {i:c for i,c in enumerate(co) if c}


ACTION={g:[coordinates2(bracket(op,M)) for M in BASIS] for g,op in OPS.items()}
WEIGHTS=[]
for M in BASIS:
    mu=[]
    for H in (unit(0,0)-unit(1,1),unit(1,1)-unit(2,2)):
        A=bracket(H,M)
        i,j=next((i,j) for i in range(3) for j in range(3) if M[i,j])
        eigen=Q(int(A[i,j]),int(M[i,j]))
        assert eigen.denominator==1 and np.array_equal(A,int(eigen)*M)
        mu.append(int(eigen))
    a,b=2*mu[0]+mu[1]+3,mu[0]+2*mu[1]+3
    assert a%3==b%3==0
    WEIGHTS.append((a//3,b//3))
for i,word in enumerate(CYCLIC):
    M=BASIS[0]
    for g in reversed(word):
        M=bracket(OPS[g],M)
    assert np.array_equal(M,BASIS[i])
Gram=[[Q(int(np.trace(A@B.T))) for B in BASIS] for A in BASIS]
aug=[row+[Q(int(i==j)) for j in range(8)] for i,row in enumerate(Gram)]
for j in range(8):
    pivot=next(i for i in range(j,8) if aug[i][j])
    aug[pivot],aug[j]=aug[j],aug[pivot]
    divisor=aug[j][j]
    aug[j]=[c/divisor for c in aug[j]]
    for i in range(8):
        if i!=j and aug[i][j]:
            c=aug[i][j]
            aug[i]=[a-c*b for a,b in zip(aug[i],aug[j])]
GINV=[row[8:] for row in aug]
local=SimpleNamespace(ACTION=ACTION,GINV=GINV,levi=SimpleNamespace(WEIGHTS=tuple(WEIGHTS)))


@lru_cache(None)
def recursive_words(length,a,b):
    if length==0:
        return (0,) if a==b==0 else ()
    if min(a,b)<0 or max(a,b)>2*length:
        return ()
    result=[]
    for j,(u,v) in enumerate(WEIGHTS):
        prefix=j<<(3*(length-1))
        result.extend(prefix|w for w in recursive_words(length-1,a-u,b-v))
    return tuple(result)


LIMIT=2**63


def maximum(v):
    return max(abs(int(v.min())),abs(int(v.max()))) if len(v) else 0


class Words:
    def __init__(self,n):
        self.n=n
        self.all=range(8**n)
        self.roots={}
        self.actions={}

    def root(self,a,b):
        key=(a,b)
        if key not in self.roots:
            codes=np.array(recursive_words(self.n,a,b),dtype=np.uint32)
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


def independent_local_f3(n):
    table=[]
    roots={'e1':(n,1,0),'e2':(n,0,1),'e12':(2*n,1,1)}
    for word in CYCLIC:
        h=-1
        matrices=[np.zeros((3,3),dtype=np.int64) for _ in range(3)]
        for g in reversed(word):
            matrices=[bracket(OPS[g],M)+h*c*OPS[g] for M,c in zip(matrices,roots[g])]
            h=0
        terms=[]
        if h:
            terms.append(('h3',(h,0,0)))
        accounted=[np.zeros((3,3),dtype=np.int64) for _ in range(3)]
        for g,(i,j) in (('e1',(0,1)),('e2',(1,2)),('e12',(0,2))):
            co=tuple(int(M[i,j]) for M in matrices)
            if any(co):
                terms.append((g,co))
            for piece,c in enumerate(co):
                accounted[piece]+=c*OPS[g]
        assert all(np.array_equal(a,b) for a,b in zip(accounted,matrices))
        table.append(terms)
    return table


def affine_f3(source,target,n):
    # DIFFERENT representation: move EVERY degree-zero local bracket LEFT.
    # u*g = g*u - [g,u], so only PREFIX actions occur and each has a MINUS.
    codes,_=source.root(n,n)
    out_codes,out_index=target.root(n,n)
    letters=[((codes>>np.uint32(3*(n-1-i)))&np.uint32(7)) for i in range(n)]
    maps=[[],[],[]]
    tails={g:[[],[],[]] for g in ('h3','e1','e2','e12')}
    shifts={'h3':(0,0),'e1':(1,0),'e2':(0,1),'e12':(1,1)}
    table=independent_local_f3(n)
    for k in range(n):
        shift=3*(n-1-k)
        shortened=((codes>>(shift+3))<<shift)|(codes&np.uint32((1<<shift)-1))
        for j,terms in enumerate(table):
            for g,co in terms:
                inputs=np.flatnonzero(letters[k]==j).astype(np.int32)
                a0,b0=shifts[g]
                _,tail_index=target.root(n-a0,n-b0)
                outputs=tail_index[shortened[inputs]]
                for piece,c in enumerate(co):
                    tails[g][piece].append((inputs,outputs,c))
                for ell in range(k):
                    action_shift=3*(n-2-ell)
                    for old in range(8):
                        selected=np.flatnonzero((letters[k]==j)&(letters[ell]==old)).astype(np.int32)
                        if not len(selected):
                            continue
                        if g=='h3':
                            assert co[1]==co[2]==0
                            a,b=WEIGHTS[old]
                            choices={old:tuple(-co[0]*z for z in (4-2*n*(a+b),-2*a,-2*b))}
                        else:
                            choices={new:tuple(-c*act for c in co) for new,act in ACTION[g][old].items()}
                        for new,values in choices.items():
                            changed=shortened[selected].astype(np.int64)+(new-old)*(1<<action_shift)
                            assert np.all(changed>=0) and np.all(changed<len(target.all))
                            outputs=out_index[changed]
                            for piece,c in enumerate(values):
                                maps[piece].append((selected,outputs,int(c)))
    f3=[Transfer(len(codes),len(out_codes),part) for part in maps]
    tail_checks=[]
    for g,parts in tails.items():
        a,b=shifts[g]
        tail_codes,_=target.root(n-a,n-b)
        tail_checks.extend(Transfer(len(codes),len(tail_codes),part) for part in parts)
    return f3,tail_checks


def difference(a,b):
    assert a.shape==b.shape and maximum(a)+maximum(b)<LIMIT
    return a-b


def canonical_96(d,word_space,source_space,n,outer_cache):
    negative=[]
    for word in CYCLIC:
        vector=d
        root=(n,n)
        denominator=1
        for g in reversed(word):
            if g=='e12':
                r1,F1=word_space.action(root,'f1')
                r2,F2=word_space.action(root,'f2')
                rr,F2after=word_space.action(r1,'f2')
                rr2,F1after=word_space.action(r2,'f1')
                assert rr==rr2
                vector=difference(F2after.apply(F1.apply(vector)),F1after.apply(F2.apply(vector)))
                root=rr
                denominator*=4
            else:
                root,operator=word_space.action(root,'f1' if g=='e1' else 'f2')
                vector=operator.apply(vector)
                denominator*=2
        # w_j=-theta(u_j); theta flips EVERY positive cyclic operator.
        negative.append((root,vector,denominator,(-1)**len(word)))
    common=math.lcm(*(Q(GINV[i][j]*sign,den).denominator for j,(root,v,den,sign) in enumerate(negative) for i in range(8)))
    source_codes,source_index=source_space.root(n,n)
    terms=[]
    bound=0
    for j,(degree,v,den,sign) in enumerate(negative):
        for i in range(8):
            factor=common*GINV[i][j]*sign/den
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
    assert bound<LIMIT
    out=np.zeros(len(source_codes),dtype=np.int64)
    for v,left,right,factor in terms:
        out[left]+=factor*v
        out[right]-=factor*v
    return out,common


def qmatrix(rows):
    return flint.fmpq_mat([[flint.fmpq(Q(c).numerator,Q(c).denominator) for c in row] for row in rows])


def load_array(pin):
    raw=(ROOT/pin['file']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==pin['sha256']
    stream=io.BytesIO(raw)
    array=np.load(stream,allow_pickle=False)
    assert stream.tell()==len(raw), 'unparsed trailing NPY bytes'
    return array


