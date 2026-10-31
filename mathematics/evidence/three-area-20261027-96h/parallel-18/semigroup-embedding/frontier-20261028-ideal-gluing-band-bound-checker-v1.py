from itertools import product

def run(k,m):
 zero=(-1,0)
 A=[[zero]+[(i,j) for j in range(1,m)] for i in range(k)]
 U=sorted(set(x for a in A for x in a));S=[(i,x) for i in range(k) for x in A[i]]
 def meet(x,y):
  if x==zero or y==zero or x[0]!=y[0]:return zero
  return (x[0],min(x[1],y[1]))
 def mult(s,t):return (s[0],meet(s[1],t[1]))
 assert len(U)==1+k*(m-1) and len(S)==k*m
 assert all(mult(mult(x,y),z)==mult(x,mult(y,z)) for x,y,z in product(S,repeat=3))
 assert all(mult(x,x)==x for x in S)
 assert all(mult(mult(mult(mult(x,y),x),z),x)==mult(mult(mult(x,y),z),x) for x,y,z in product(S,repeat=3))
 assert all(meet(meet(x,y),z)==meet(x,meet(y,z)) and meet(x,y)==meet(y,x) for x,y,z in product(U,repeat=3))
 assert all(mult(x,y)[1]==meet(x[1],y[1]) and mult(x,y)[0]==x[0] for x,y in product(S,repeat=2))
 assert all(x==y or x[0]!=y[0] or x[1]!=y[1] for x,y in product(S,repeat=2))
 print('k=',k,' m=',m,' |S|=',len(S),' |union-band|=',len(U),' max actor fibre=',m,sep='')
for k,m in [(2,2),(2,3),(3,3),(4,4)]:run(k,m)
print('PASS exact finite source/host equations; all-actor lower bound is the written argument')
