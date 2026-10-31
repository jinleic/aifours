#!/usr/bin/env python3
"""Independent bounded tests of zero-tail packing and outside-head tradeoff."""
from itertools import combinations
import json


def atom(i,j):return b'a'*i+b'b'+b'a'*j


def UD(code):
    todo={v[len(u):] for u in code for v in code if u!=v and v.startswith(u)}
    done=set()
    while todo:
        if b'' in todo or todo&code:return False
        fresh=todo-done
        if not fresh:return True
        done|=fresh;new=set()
        for r in fresh:
            for w in code:
                if r.startswith(w):new.add(r[len(w):])
                if w.startswith(r):new.add(w[len(r):])
        todo=new
    return True


def scan(n):
    cells=[(i,j) for i in range(n) for j in range(n) if (i,j)!=(0,0)]
    candidates=valid=subset_tests=0
    for rest in combinations(cells,n-1):
        W={(0,0),*rest};candidates+=1
        if not UD({atom(i,j) for i,j in W}|{b'a'*n}):continue
        valid+=1;I={i for i,j in W if j==0};k=len(I)
        for i in range(n):
            J={j for h,j in W if h==i}
            sums=[(j+h)%n for j in J for h in I]
            if len(sums)!=len(set(sums)) or len(sums)>n:
                raise AssertionError(('zero-column packing failed',n,W,i))
        I=sorted(I)
        for z in range(1,len(I)+1):
            for A in combinations(I,z):
                outside=sum(i not in A for i,j in W)
                if outside<n-z*(n//k):raise AssertionError('outside-head inequality failed')
                subset_tests+=1
    return {'n':n,'layers':candidates,'UD_full_size':valid,'anchor_subset_checks':subset_tests}


def control():
    # Deliberately non-UD: (ba)(b)=(b)(ab).
    W={(0,0),(1,0),(2,0),(0,1)};n=4;I={0,1,2};A={0,1}
    if UD({atom(i,j) for i,j in W}|{b'a'*n}):raise AssertionError('bad control accepted as UD')
    outside=sum(i not in A for i,j in W)
    if not outside<n-len(A)*(n//len(I)):
        raise AssertionError('control did not violate target inequality')
    return 'non-UD control correctly violates packing bound'


if __name__=='__main__':
    print(json.dumps({'domains':[scan(4),scan(5)],'negative_control':control(),
                      'scope':'synthetic complete-bayonet layers only, not Shor completions'},indent=2))
