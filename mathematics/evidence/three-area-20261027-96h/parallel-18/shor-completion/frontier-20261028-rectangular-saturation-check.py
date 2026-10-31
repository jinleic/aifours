#!/usr/bin/env python3
"""Exact checks of anchor-hole certificates and synthetic rectangle products."""
import json
import sys

A=(0,3,8,11)
Y=(0,1,7,13,14)


def forced_holes(n):
    row=[]
    for a in A:
        j=(6-a)%n
        witness=next(((y,u,v) for y in Y for u in A for v in A
                      if j!=y and (j+u-y-v)%n==0),None)
        if witness is None:raise AssertionError(('row hole not certified',n,j))
        row.append((j,witness))
    col=[]
    for y in Y:
        i=(2-y)%n
        witness=next(((a,u,v) for a in A for u in Y for v in Y
                      if i!=a and (i+u-a-v)%n==0),None)
        if witness is None:raise AssertionError(('column hole not certified',n,i))
        col.append((i,witness))
    return row,col


def compose(P,Q,g,n):
    out=set()
    for i,j in P:
        for k,l in Q:
            if (j+k)%n==g:
                if (i,l) in out:raise AssertionError(('non-unique path',n,g,i,l))
                out.add((i,l))
    return out


def rectangle(n,heads,tails):
    W={(i,j) for i in heads for j in tails}
    if len(W)!=n:raise AssertionError('wrong rectangle size')
    checked=0
    for g in range(n):
        P=compose(W,W,g,n)
        if P!=W:raise AssertionError('rectangle did not remain stable')
        checked+=len(P)
    return {'n':n,'pairs':len(W),'seams':n,'direct_path_endpoints_checked':checked,
            'scope':'synthetic complete-bayonet positive control; NOT Shor S'}


def main(limit):
    if not 26<=limit<=10000:raise ValueError('require26<=MAX_N<=10000')
    for n in range(26,limit+1):forced_holes(n)
    row,col=forced_holes(limit)
    return {'anchor_holes_checked_for_n':[26,limit],
            'row_target6_candidate_conflicts':row,
            'column_target2_candidate_conflicts':col,
            'positive_controls':[rectangle(32,A,tuple(16*k+y for k in range(2) for y in (0,2,4,6))),
                                 rectangle(20,(0,5,10,15),(0,1,2,3,4))]}


if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('usage: rectangular-saturation-check.py MAX_N')
    print(json.dumps(main(int(sys.argv[1])),indent=2))
