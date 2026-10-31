from itertools import product,permutations

def check(n):
 X=0;U=list(range(1,n+1));V=list(range(n+1,2*n+1));B=list(range(2*n+1))
 def m(a,b):
  if b==X:return X
  if a==X:return n+b if b in U else b
  if a in U:return a if b in U else b
  return a if b in U else b
 assert all(m(a,a)==a for a in B)
 assert all(m(m(a,b),c)==m(a,m(b,c)) for a,b,c in product(B,repeat=3))
 assert all(m(m(m(m(a,b),c),d),a)==m(m(m(m(m(m(a,b),c),a),c),d),a) for a,b,c,d in product(B,repeat=4))
 for e in B:
  corner={m(m(e,x),e) for x in B}
  expected={X} if e==X else ({e}|set(V)) if e in U else {e}
  assert corner==expected
  assert all(m(m(m(m(a,b),a),c),a)==m(m(m(a,b),c),a) for a,b,c in product(corner,repeat=3))
 for p in permutations(range(n)):
  def f(a):return X if a==X else 1+p[a-1] if a in U else n+1+p[a-n-1]
  assert all(f(m(a,b))==m(f(a),f(b)) for a,b in product(B,repeat=2))
 if n>=2:
  a,b,c=U[0],X,U[1]
  assert m(m(m(m(a,b),a),c),a)!=m(m(m(a,b),c),a)
 print('n=',n,'band size=',len(B),' SN checks=',len(B)**4,' all symmetric automorphisms=',len(list(permutations(range(n)))),' non-globally-regular=',n>=2,sep='')
for n in (1,2,3,4):check(n)
