#!/usr/bin/env python3
"""Exhaustive small-order test of saturated-row/column rectangle closure.

Independent synthetic CBCs; this is not a Shor completion or an all-order proof.
"""
from itertools import combinations
import json
import sys


def word(i,j):return b'a'*i+b'b'+b'a'*j


def ud(code):
    residual={v[len(u):] for u in code for v in code if u!=v and v.startswith(u)}
    seen=set()
    while residual:
        if b'' in residual or residual & code:return False
        fresh=residual-seen
        if not fresh:return True
        seen.update(fresh);nxt=set()
        for r in fresh:
            for w in code:
                if r.startswith(w):nxt.add(r[len(w):])
                if w.startswith(r):nxt.add(w[len(r):])
        residual=nxt
    return True


def compose(P,Q,g,n):
    out=set()
    for i,j in P:
        for k,l in Q:
            if (j+k)%n==g:
                if (i,l) in out:raise AssertionError('duplicate composed path')
                out.add((i,l))
    if len(out)!=n:raise AssertionError('wrong conserved path count')
    return out


def tiling(X,Y,n):
    sums=[(x+y)%n for x in X for y in Y]
    return len(sums)==n and len(set(sums))==n


def check(W,n):
    A={i for i,j in W if j==0};Y={j for i,j in W if i==0}
    rows=cols=0
    for u in range(n):
        J={j for i,j in W if i==u}
        if not J or len(A)*len(J)!=n:continue
        Q=compose(W,W,u,n)
        if Q!={(a,j) for a in A for j in J}:raise AssertionError('row Q wrong')
        t=min(J);P=compose(Q,W,t,n);T={j for i,j in P}
        if P!={(a,j) for a in A for j in T} or not Y<=T or not tiling(A,T,n):
            raise AssertionError('row closure wrong')
        for g in range(n):compose(P,P,g,n)
        rows+=1
    for j in range(n):
        I={i for i,t in W if t==j}
        if not I or len(I)*len(Y)!=n:continue
        Q=compose(W,W,j,n)
        if Q!={(i,y) for i in I for y in Y}:raise AssertionError('column Q wrong')
        h=min(I);P=compose(W,Q,h,n);U={i for i,j in P}
        if P!={(i,y) for i in U for y in Y} or not A<=U or not tiling(U,Y,n):
            raise AssertionError('column closure wrong')
        for g in range(n):compose(P,P,g,n)
        cols+=1
    return rows,cols


def run(n):
    cells=[(i,j) for i in range(n) for j in range(n) if (i,j)!=(0,0)]
    scanned=valid=rows=cols=0
    for rest in combinations(cells,n-1):
        W={(0,0),*rest};scanned+=1
        code={word(i,j) for i,j in W}|{b'a'*n}
        if not ud(code):continue
        valid+=1;r,c=check(W,n);rows+=r;cols+=c
    return {'n':n,'b_containing_layers_scanned':scanned,'UD_full_size_layers':valid,
            'saturated_row_closures_verified':rows,'saturated_column_closures_verified':cols}


if __name__=='__main__':
    if len(sys.argv)!=1:raise SystemExit('takes no arguments')
    print(json.dumps([run(4),run(5)],indent=2))
