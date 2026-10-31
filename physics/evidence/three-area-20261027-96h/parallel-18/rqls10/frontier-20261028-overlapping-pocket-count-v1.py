#!/usr/bin/env python3
"""Integer checks of the written OA(3) intersection double counts, not exhaustive enumeration."""
n=10;k=3
for t in range(k+1):
    a_only=4*k*n-16*k*k+t*(7*k-n)
    neither=n*n-8*k*n+18*k*k+t*(n-6*k)
    assert a_only<0 or neither<0
    print('disjoint shared-axis size',t,'A-only',a_only,'neither',neither)
X=n*n-2*k*k+1
A=4*k*(n-k)-4*(k-1)
cross=12*k*k-(24*k-12)
same=4*(n-2*k+1)
I=cross+same
union=2*A-I
print('one-common-cell X,A,B,cross,same,I,union,neither',X,A,A,cross,same,I,union,X-union)
assert (X,A,cross,same,I,union,X-union)==(83,76,48,20,68,84,-1)
