#!/usr/bin/env python3
"""Direct raw-word checks of the canonical Shor row displacement lemma."""
import json
import sys

A=(0,3,8,11)
OLD={(0,j) for j in (0,1,7,13,14)} | {(i,j) for i in (3,8) for j in (0,2,4,6)} | {(11,j) for j in (0,1,2)}


def atom(i,j):return 'a'*i+'b'+'a'*j


def witness(n, standard, r, s, t, p, q, u, extra=()):
    j,v=next((j,v) for j in standard for v in A if (j+v)%n==s)
    leftg=(p+u,j+v);rightg=(q+r,s)
    if any((x-y)%n for x,y in zip(leftg,rightg)):
        raise AssertionError('wrong seam condition')
    common=tuple(max(x,y) for x,y in zip(leftg,rightg))
    left=[atom(t,p)]+['a'*n]*((common[0]-leftg[0])//n)+[atom(u,j)]
    left+=['a'*n]*((common[1]-leftg[1])//n)+[atom(v,0)]
    right=[atom(t,q)]+['a'*n]*((common[0]-rightg[0])//n)+[atom(r,s)]
    right+=['a'*n]*((common[1]-rightg[1])//n)+[atom(0,0)]
    allowed={atom(i,j) for i,j in OLD}|{atom(i,j) for i in (3,8) for j in standard}
    allowed|={atom(i,j) for i,j in extra}|{'a'*n,atom(r,s)}
    if left==right or ''.join(left)!=''.join(right) or not set(left+right)<=allowed:
        raise AssertionError(('invalid raw witness',n,r,s))


def check(n):
    if n<32 or n%16:raise ValueError('n must be a multiple of16, >=32')
    m=n//16
    standard={16*k+y for k in range(m) for y in (0,2,4,6)}
    if len({(j+a)%n for j in standard for a in A})!=n:
        raise AssertionError('standard row is not a tiling')
    diff={}
    for p in standard:
        for q in standard:
            if p!=q:diff[(p-q)%n]=(p,q)
    exceptional={16*h for h in range(1,m)} | {11+16*h for h in range(1,m)}
    witnesses=0
    for r in range(n):
        if r in A or r in exceptional:continue
        u=8 if r%2==0 else 3
        p,q=diff[(r-u)%n]
        for s in range(n):witness(n,standard,r,s,3,p,q,u)
        witnesses+=n
    for k in range(m-1):
        anchor=14+16*k
        r1=16*(k+1)
        r2=11+16*(m-1-k)
        for s in range(n):
            witness(n,standard,r1,s,0,anchor,1,3,((0,anchor),))
            witness(n,standard,r2,s,0,1,anchor,8,((0,anchor),))
        witnesses+=2*n
    return {'n':n,'standard_row_size':len(standard),
            'exceptional_new_head_residues':len(exceptional),
            'optional_row0_anchors':max(0,m-2),'direct_equal_word_witnesses':witnesses}


if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('usage: canonical-row-displacement-check.py MAX_N')
    cap=int(sys.argv[1])
    if not 32<=cap<=256:raise SystemExit('require 32<=MAX_N<=256')
    print(json.dumps([check(n) for n in range(32,cap+1,16)],indent=2))
