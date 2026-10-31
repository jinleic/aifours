#!/usr/bin/env python3
"""Check forced canonical tilers and single-saturated-row ambiguity certificates."""
import json
import sys

A=(0,3,8,11)


def atom(i,j):return 'a'*i+'b'+'a'*j


def check(n):
    if n<32 or n%16:raise ValueError('require n multiple16 and at least32')
    m=n//16
    standard={16*k+y for k in range(m) for y in (0,2,4,6)}
    tiles=[{(j+a)%n for a in A} for j in range(n)]
    known={0,2,4,6};forced=0
    for k in range(m-1):
        for offset in (16,18,20,22):
            target=16*k+offset
            covered=set().union(*(tiles[j] for j in known))
            if target in covered:raise AssertionError('target already covered by known tiles')
            candidates=[(target-a)%n for a in A if not (tiles[(target-a)%n]&covered)]
            if candidates!=[target]:raise AssertionError((n,target,candidates))
            known.add(target);forced+=1
    if known!=standard or len(set().union(*(tiles[j] for j in known)))!=n:
        raise AssertionError('forcing did not yield full canonical tiling')
    diffs={(p-q)%n:(p,q) for p in standard for q in standard if p!=q}
    sums={(j+v)%n:(j,v) for j in standard for v in A}
    if len(sums)!=n:raise AssertionError('canonical tiler not bijective')
    checks={}
    for u in (3,8):
        heads=[r for r in range(n) if r!=u and (r-u)%n in diffs]
        if u==3 and any(r%2!=1 or r%16==11 for r in heads):
            raise AssertionError('wrong row3 head set')
        if u==8 and any(r%2!=0 or r%16==0 for r in heads):
            raise AssertionError('wrong row8 head set')
        total=0
        for r in heads:
            p,q=diffs[(r-u)%n]
            for s in range(n):
                j,v=sums[s]
                lg=(p+u,j+v);rg=(q+r,s);target=tuple(max(x,y) for x,y in zip(lg,rg))
                if any((x-y)%n for x,y in zip(lg,rg)):raise AssertionError('bad seam')
                left=[atom(u,p)]+['a'*n]*((target[0]-lg[0])//n)+[atom(u,j)]
                left+=['a'*n]*((target[1]-lg[1])//n)+[atom(v,0)]
                right=[atom(u,q)]+['a'*n]*((target[0]-rg[0])//n)+[atom(r,s)]
                right+=['a'*n]*((target[1]-rg[1])//n)+[atom(0,0)]
                if left==right or ''.join(left)!=''.join(right):raise AssertionError('bad witness')
                total+=1
        checks[str(u)]={'excluded_head_residues':len(heads),'raw_witnesses':total}
    return {'n':n,'forced_new_tails':forced,'canonical_size':len(known),'single_row_checks':checks}


if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('usage: saturated-row-forcing-check.py MAX_N')
    cap=int(sys.argv[1])
    if not 32<=cap<=256:raise SystemExit('require32<=MAX_N<=256')
    print(json.dumps([check(n) for n in range(32,cap+1,16)],indent=2))
