from itertools import product

def partitions(n):
 out=[]
 def go(v):
  if len(v)==n:out.append(tuple(v));return
  for x in range(max(v)+2):go(v+[x])
 go([0]);return out

def check(k,m,part):
 blocks=max(part)+1;r=max(part.count(a) for a in range(blocks));label=[];used={}
 for i,a in enumerate(part):label.append(used.setdefault(a,0));used[a]+=1
 zero=(-1,0)
 S=[(i,z) for i in range(k) for z in range(m)]
 B=[('z',j) for j in range(r)]+[('n',i,z) for i in range(k) for z in range(1,m)]
 def sm(x,y):
  i,a=x;j,b=y
  return (i,min(a,b) if i==j else 0)
 def coeff(x):return ('z',label[x[0]]) if x[1]==0 else ('n',)+x
 def bm(x,y):
  if x[0]=='z':return x
  _,i,a=x
  if y[0]=='n' and i==y[1]:return ('n',i,min(a,y[2]))
  return ('z',label[i])
 assert len(B)==k*(m-1)+r
 assert all(bm(b,b)==b for b in B)
 assert all(bm(bm(a,b),c)==bm(a,bm(b,c)) for a,b,c in product(B,repeat=3))
 assert all(bm(bm(bm(a,b),c),d)==bm(bm(bm(a,c),b),d) for a,b,c,d in product(B,repeat=4))
 assert all(coeff(sm(x,y))==bm(coeff(x),coeff(y)) and part[sm(x,y)[0]]==part[x[0]] for x,y in product(S,repeat=2))
 assert all(x==y or part[x[0]]!=part[y[0]] or coeff(x)!=coeff(y) for x,y in product(S,repeat=2))
 return blocks,len(B)
for k,m in ((2,2),(3,2),(4,3),(5,2)):
 values=[check(k,m,p) for p in partitions(k)]
 observed={a:min(b for aa,b in values if aa==a) for a in range(1,k+1)}
 expected={a:k*(m-1)+(k+a-1)//a for a in range(1,k+1)}
 assert observed==expected
 print('k=',k,' m=',m,' all partitions=',len(values),' actor→min band=',observed,sep='')
print('PASS exact constructions for every indicated row partition; lower bound is written proof')
