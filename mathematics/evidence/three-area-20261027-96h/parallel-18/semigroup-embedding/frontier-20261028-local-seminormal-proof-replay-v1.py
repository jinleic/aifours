#!/usr/bin/env python3
"""Replay a two-local-identity proof using square and band-content reductions."""
from itertools import product

def local(e,a,b,c):
 x=e+a+e;y=e+b+e;z=e+c+e
 return x+y+x+z+x,x+y+z+x

def sig(w):
 if not w:return ()
 C=set(w)
 if len(C)==1:return ('one',w[0])
 v=set()
 for i,x in enumerate(w):
  v.add(x)
  if v==C:last=x;pre=w[:i];break
 v=set()
 for i in range(len(w)-1,-1,-1):
  x=w[i];v.add(x)
  if v==C:first=x;suf=w[i+1:];break
 return(last,sig(pre),first,sig(suf))

def step(a,b):
 n=len(a)
 for i in range(n):
  for k in range(1,(n-i)//2+1):
   if a[i:i+k]==a[i+k:i+2*k] and a[:i]+a[i:i+k]+a[i+2*k:]==b:return ('square',a[i:i+k])
 for i in range(n):
  for j in range(i+1,n):
   C=set(a[i:j])
   for k in range(j+1,n):
    if not set(a[j:k])<=C:break
    for l in range(k+1,n+1):
     Z=set(a[k:l])
     if not Z<=C:break
     if Z==C and a[:j]+a[k:]==b:return ('content',a[i:j],a[j:k],a[k:l])
 return None
I_L=('abcaccbccaccdaccacda','abcacbccaccdaccacda','abcacbccacdaccacda','abcacbccacda','abcacbcacda','abcacda')
I_R=('abcaccbccdaccacda','abcacbccdaccacda','abcacbcdaccacda','abcacbcdacacda','abcacbcdacda','abcacbcda')
II_L=('abcabcbcacbcbcabcbcdbcbcabcda','abcabcbcacbcabcbcdbcbcabcda','abcabcbcabcbcdbcbcabcda','abcabcbcabcdbcbcabcda','abcabcbcabcda','abcabcda','abcda')
II_R=('abcabcbcacbcbcdbcbcabcda','abcbcacbcbcdbcbcabcda','abcacbcbcdbcbcabcda','abcacbcdbcbcabcda','abcacbcdbcabcda','abcacbcdcabcda','abcacbcdabcda','abcacbcda')
a,b=local('c','a','b','da');assert 'ab'+a+'da'==I_L[0] and 'ab'+b+'da'==I_R[0]
a,b=local('bc','a','ac','d');assert 'a'+a+'da'==II_L[0] and 'a'+b+'da'==II_R[0]
counts={'square':0,'content':0}
for trace in (I_L,I_R,II_L,II_R):
 for x,y in zip(trace,trace[1:]):
  r=step(x,y);assert r is not None and sig(x)==sig(y);counts[r[0]]+=1
assert I_L[-1]=='abcacda' and I_R[-1]=='abcacbcda'
assert II_L[-1]=='abcda' and II_R[-1]=='abcacbcda'
assert sig('abcda')!=sig('abcacda') # local regularity is essential, not a band identity
# Controls: removing a required symbol is not a valid free-band equality/rewrite.
assert sig('abcda')!=sig('abcaa') and step('abcda','abcaa') is None
print('PASS two local-regular identity instances with exact contexts, four band-rewrite traces')
print('square contractions=',counts['square'],' content absorptions=',counts['content'],sep='')
print('CONCLUSION conditional on named Green-Rees/content lemma: local regular implies seminormal')
print('CONTROL target words are distinct in the unrestricted free band; bad rewrite rejected')
print('LIMIT same-author replay; independent written review still required')
