#!/usr/bin/env python3
"""Independent block-by-block rank-saturation certificate, all 15^4 choices.

One local two-level sector per party, arbitrary invertible 2x2 blocks and
monomial action on the remaining levels. The only nontrivial imported lemma
is the written rank-3 classification for three nonadjacent binary 3-tuples.
"""
import argparse
import collections
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys

P=17
R2=6
LEVEL_PAIRS=tuple(itertools.combinations(range(6),2))


class CertificateError(ValueError):pass


def load_table(path):
    raw=path.read_bytes();tensor={};cells=[]
    for line in raw.decode('utf-8').splitlines():
        if not line or line.startswith('#'):continue
        f=line.split()
        if len(f)<3 or not all(re.fullmatch('[0-5]',x) for x in f[:2]):raise CertificateError('bad cell')
        a,b=map(int,f[:2]);cells.append((a,b))
        for token in f[2:]:
            if not re.fullmatch(r'[+\-s][0-5][0-5]',token):raise CertificateError('bad term')
            key=(a,b,int(token[1]),int(token[2]))
            if key in tensor:raise CertificateError('duplicate term')
            tensor[key]=(0,1) if token[0]=='s' else (1 if token[0]=='+' else -1,0)
    if cells!=list(itertools.product(range(6),repeat=2)) or len(tensor)!=60:
        raise CertificateError('wrong table coverage')
    return tensor,hashlib.sha256(raw).hexdigest()


def check_no_hamming_one(tensor):
    for axis in range(4):
        fibers=[tuple(x[j] for j in range(4) if j!=axis) for x in tensor]
        if len(set(fibers))!=len(fibers):raise CertificateError('Hamming-one support collision')


def rank_mod(mat):
    m=[row[:] for row in mat];r=0
    for c in range(len(m[0])):
        pivot=next((i for i in range(r,len(m)) if m[i][c]%P),None)
        if pivot is None:continue
        m[r],m[pivot]=m[pivot],m[r]
        inv=pow(m[r][c],-1,P)
        for i in range(r+1,len(m)):
            scale=m[i][c]*inv%P
            if scale:
                for j in range(c,len(m[0])):m[i][j]=(m[i][j]-scale*m[r][j])%P
        r+=1
        if r==len(m):break
    return r


def flatten_rank(points,coeffs,axes):
    other=tuple(a for a in range(4) if a not in axes)
    matrix=[[0]*4 for _ in range(4)]
    for point,(a,b) in zip(points,coeffs):
        row=point[axes[0]]*2+point[axes[1]]
        col=point[other[0]]*2+point[other[1]]
        matrix[row][col]=(matrix[row][col]+a+R2*b)%P
    return rank_mod(matrix)


def prove_block(points,coeffs,active):
    n=len(points)
    if n==1:return 'singleton'
    if n==2:
        if sum(a!=b for a,b in zip(points[0],points[1]))<2:
            raise CertificateError('two-term rank-two condition failed')
        return 'two-term-separated'
    if n==3:
        varying=[j for j in range(4) if len({x[j] for x in points})>1]
        if len(varying)==3:
            reduced=[tuple(x[j] for j in varying) for x in points]
            if len({sum(x)%2 for x in reduced})!=1:
                raise CertificateError('three-term W parity failed')
            if any(sum(a!=b for a,b in zip(x,y))<2 for x,y in itertools.combinations(reduced,2)):
                raise CertificateError('three-term W separation failed')
            return 'three-term-W'
        if len(varying)!=4:raise CertificateError('unexpected 3-term varying count')
        if max(flatten_rank(points,coeffs,(0,j)) for j in (1,2,3))<3:
            raise CertificateError('three-term rank-three minor absent')
        return 'three-term-minor'
    if n==4:
        if max(flatten_rank(points,coeffs,(0,j)) for j in (1,2,3))<4:
            raise CertificateError('four-term rank-four minor absent')
        return 'four-term-minor'
    raise CertificateError(f'block size {n} not certified')


def main():
    p=argparse.ArgumentParser();p.add_argument('table',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
    tensor,sha=load_table(a.table);check_no_hamming_one(tensor)
    if R2*R2%P!=2:raise CertificateError('invalid modular root')
    mutated=dict(tensor);key=next(iter(tensor));replacement=((key[0]+1)%6,)+key[1:]
    if replacement in mutated:raise CertificateError('control mutation coordinate unexpectedly occupied')
    mutated[replacement]=(1,0)
    try:check_no_hamming_one(mutated)
    except CertificateError as exc:
        if str(exc)!='Hamming-one support collision':raise
        negative=str(exc)
    else:raise CertificateError('Hamming-one control accepted')
    counts=collections.Counter(); blocks_checked=0;choices=0
    for pairs in itertools.product(LEVEL_PAIRS,repeat=4):
        blocks=collections.defaultdict(list)
        for coord,coeff in tensor.items():
            key=tuple(None if coord[j] in pairs[j] else coord[j] for j in range(4))
            point=tuple(pairs[j].index(coord[j]) if key[j] is None else 0 for j in range(4))
            blocks[key].append((point,coeff))
        subtotal=0
        for key,entries in blocks.items():
            points=[x for x,_ in entries];coeffs=[x for _,x in entries]
            active=tuple(j for j,x in enumerate(key) if x is None)
            kind=prove_block(points,coeffs,active)
            counts[(len(active),len(entries),kind)]+=1
            subtotal+=len(entries);blocks_checked+=1
        if subtotal!=60:raise CertificateError('block partition does not cover 60 terms')
        choices+=1
    if choices!=15**4:raise CertificateError('incomplete pair choices')
    result={'table_sha256':sha,'prime':P,'sqrt2_image':R2,'pair_choices_verified':choices,
            'invariant_blocks_verified':blocks_checked,'every_block_rank_equals_original_support':True,
            'block_certificate_histogram':[{'active':k[0],'terms':k[1],'certificate':k[2],'count':v} for k,v in sorted(counts.items())],
            'added_Hamming_one_control':negative,
            'scope':'Exact finite certificate + written W-rank lemma; arbitrary 2x2 GL per party, not arbitrary U(6)^4 or other AME states.'}
    with a.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    json.dump(result,sys.stdout,indent=2);print()


if __name__=='__main__':main()
