#!/usr/bin/env python3
"""Exact sample checks of the written CRT formulas for 2p Weyl triples."""
from itertools import product
from math import gcd
for p in (3,5,7,11,13):
 n=2*p;r=(p+1)//2
 pts=list(product(range(2),range(p)))
 t=lambda a,b:(p*a+2*r*b)%n
 assert len({t(a,b) for a,b in pts})==n
 for (a,b),(c,d) in product(pts,repeat=2):
  assert (2*t(a,b)*t(c,d)-2*p*a*c-8*r*r*b*d)%(4*p)==0
 for a,b in pts:
  assert (t(a,b)**2-p*p*a-4*r*r*b*b)%(4*p)==0
 for m,c in product(range(n),repeat=2):
  if (m,c)==(0,0):continue
  if m%2 or c%2:assert ((p*m)%n,(p*c)%n) in {(p,0),(0,p),(p,p)}
  else:assert ((m//2)%p,(c//2)%p)!=(0,0)
 print('p',p,'PASS',n*n,'Fourier,',n,'chirp and',n*n-1,'Weyl labels')
print('Finite sample checks only; general proof is written separately.')
