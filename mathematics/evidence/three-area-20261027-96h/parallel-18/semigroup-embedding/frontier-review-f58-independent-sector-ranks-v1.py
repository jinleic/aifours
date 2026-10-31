#!/usr/bin/env python3
"""Exact P/E sector ranks for the published 60-term tensor.

Uses the reviewer-owned strict table parser, not any author implementation or
receipt.  P is divided by its common sqrt(2) for rank only; E coefficients are
integers.  Fraction row reduction is exact and deterministic.
"""
import importlib.util
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
PARSER=HERE/'frontier-review-f35-independent-sector-check-v1.py'
PIN='aa7105b8e868ba9a53507ba77f4fa93853423f1454634960db9ce8061fda6066'
if sha256(PARSER.read_bytes()).hexdigest()!=PIN:
    raise ValueError('reviewer parser pin mismatch')
spec=importlib.util.spec_from_file_location('reviewer_sector_parser',PARSER)
parser=importlib.util.module_from_spec(spec)
spec.loader.exec_module(parser)
H={1,2};K={0,3,4,5}


def require(ok,why):
    if not ok:raise ValueError(why)


def rank(matrix):
    a=[[Fraction(x) for x in row] for row in matrix]
    nr,nc=len(a),len(a[0]);pivot=0
    for col in range(nc):
        row=next((j for j in range(pivot,nr) if a[j][col]),None)
        if row is None:continue
        a[pivot],a[row]=a[row],a[pivot]
        scale=a[pivot][col]
        a[pivot]=[v/scale for v in a[pivot]]
        for j in range(pivot+1,nr):
            scale=a[j][col]
            if scale:
                a[j]=[u-scale*v for u,v in zip(a[j],a[pivot])]
        pivot+=1
        if pivot==nr:break
    return pivot


def flatten(entries,left,coefficient):
    right=tuple(i for i in range(4) if i not in left)
    mat=[[0]*36 for _ in range(36)]
    for pos,value in entries.items():
        row=6*pos[left[0]]+pos[left[1]]
        col=6*pos[right[0]]+pos[right[1]]
        mat[row][col]=coefficient(value)
    return mat


def check(T):
    ps={};es={pair:{} for pair in combinations(range(4),2)}
    for pos,value in T.items():
        active=tuple(i for i,x in enumerate(pos) if x in H)
        if not active:
            require(value==(0,1,0,0),'P coefficient')
            ps[pos]=value
        else:
            require(len(active)==2 and value in ((1,0,0,0),(-1,0,0,0)),'E sector/coefficients')
            es[active][pos]=value
    require(len(ps)==12,'P count')
    for left in combinations(range(4),2):
        right=tuple(i for i in range(4) if i not in left)
        rows=[tuple(p[i] for i in left) for p in ps]
        cols=[tuple(p[i] for i in right) for p in ps]
        require(len(set(rows))==12 and len(set(cols))==12,'P matching')
        require(rank(flatten(ps,left,lambda v:v[1]))==12,'P rank')
    block_count=0
    for active,entries in es.items():
        spectators=tuple(i for i in range(4) if i not in active)
        blocks={}
        for pos,value in entries.items():
            key=tuple(pos[i] for i in spectators)
            block=blocks.setdefault(key,[0,0,0,0])
            j=2*(pos[active[0]]-1)+(pos[active[1]]-1)
            require(block[j]==0,'duplicate E cell')
            block[j]=value[0]
        require(len(blocks)==4,'E spectator count')
        require({key[0] for key in blocks}==K and {key[1] for key in blocks}==K,'E spectator matching')
        for block in blocks.values():
            require(block[0]*block[3]-block[1]*block[2]!=0,'E block determinant')
            require(sum(x!=0 for x in block)==2,'E block source support')
            block_count+=1
        require(len(entries)==8,'E sector count')
        for k in spectators:
            left=(active[0],k)
            require(rank(flatten(entries,left,lambda v:v[0]))==8,'E cross rank')
    require(block_count==24,'total block count')
    return ps,es


def main(path):
    raw,T=parser.parse(path)
    require(sha256(raw).hexdigest()=='cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38','source pin')
    ps,es=check(T)
    altered=dict(T)
    victim=next(iter(next(iter(es.values()))))
    del altered[victim]
    try:
        check(altered)
    except ValueError as error:
        require(str(error)=='E block determinant','mutation wrong reason')
    else:
        raise ValueError('mutation accepted')
    print('table_sha256=',sha256(raw).hexdigest(),sep='')
    print('P_terms=12 E_sectors=6 E_terms_each=8 active_blocks=24')
    print('PASS all six P 2|2 flattenings rank12 and distinct row/column matchings')
    print('PASS all twelve E cross-flattenings rank8 and each 4-spectator matching/block determinant')
    print('CONTROL deletion of one E coefficient rejected: E block determinant')
    print('LIMIT: source ranks only; arbitrary GL and disjoint-sector bound is a written proof')


if __name__=='__main__':
    require(len(sys.argv)==2,'usage: checker TABLE')
    main(sys.argv[1])
