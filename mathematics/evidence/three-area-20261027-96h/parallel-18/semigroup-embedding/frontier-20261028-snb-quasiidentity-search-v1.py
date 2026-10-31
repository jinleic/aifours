from itertools import product
import z3

def search(n,ms=15000):
 m=z3.Function('mul_snb_'+str(n),z3.IntSort(),z3.IntSort(),z3.IntSort())
 a,b=z3.Ints('a_snb_%d b_snb_%d'%(n,n));z=z3.Solver();z.set(timeout=ms)
 z.add(a>=0,a<n,b>=0,b<n)
 for i,j in product(range(n),repeat=2):z.add(m(i,j)>=0,m(i,j)<n)
 for i in range(n):z.add(m(i,i)==i)
 for i,j,k in product(range(n),repeat=3):z.add(m(m(i,j),k)==m(i,m(j,k)))
 for x,y,c,d in product(range(n),repeat=4):
  z.add(m(m(m(m(x,y),c),d),x)==m(m(m(m(m(m(x,y),c),x),c),d),x))
 z.add(m(0,1)==1,m(1,0)==0,m(0,b)==0,m(1,b)==1,m(a,0)==m(a,1))
 r=z.check();print('order',n,'verdict',r,'reason',z.reason_unknown() if r==z3.unknown else '')
 if r!=z3.sat:return None
 model=z.model();T=tuple(tuple(model.eval(m(i,j)).as_long() for j in range(n)) for i in range(n));A=model.eval(a).as_long();B=model.eval(b).as_long()
 assert all(T[i][i]==i for i in range(n))
 assert all(T[T[i][j]][k]==T[i][T[j][k]] for i,j,k in product(range(n),repeat=3))
 assert all(T[T[T[T[x][y]][c]][d]][x]==T[T[T[T[T[T[x][y]][c]][x]][c]][d]][x] for x,y,c,d in product(range(n),repeat=4))
 assert T[0][1]==1 and T[1][0]==0 and T[0][B]==0 and T[1][B]==1 and T[A][0]==T[A][1]
 print('RECHECK table=',T,' a=',A,' b=',B,sep='');return T,A,B

for n in (3,4,5,6):
 if search(n) is not None:break
