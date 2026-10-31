from itertools import product
import z3

def search(n,ms=20000):
 m=z3.Function('mul_all_'+str(n),z3.IntSort(),z3.IntSort(),z3.IntSort())
 a,b,u,v,p,q=z3.Ints(' '.join(s+'_'+str(n) for s in ('a','b','u','v','p','q')))
 z=z3.Solver();z.set(timeout=ms)
 for x in (a,b,u,v,p,q):z.add(x>=0,x<n)
 for x,y in product(range(n),repeat=2):z.add(m(x,y)>=0,m(x,y)<n)
 for x in range(n):z.add(m(x,x)==x)
 for x,y,w in product(range(n),repeat=3):z.add(m(m(x,y),w)==m(x,m(y,w)))
 e,f=0,1
 z.add(m(e,f)==f,m(f,e)==e,m(e,b)==e,m(f,b)==f,m(a,e)==m(a,f))
 z.add(m(m(v,p),q)==e,m(v,q)==f,m(m(u,p),q)==f)
 r=z.check();print('all-band order',n,'verdict',r,'reason',z.reason_unknown() if r==z3.unknown else '')
 if r!=z3.sat:return None
 M=z.model();T=tuple(tuple(M.eval(m(i,j)).as_long() for j in range(n)) for i in range(n));vals=[M.eval(x).as_long() for x in (a,b,u,v,p,q)];A,B,U,V,P,Q=vals
 assert all(T[i][i]==i for i in range(n))
 assert all(T[T[i][j]][k]==T[i][T[j][k]] for i,j,k in product(range(n),repeat=3))
 assert T[0][1]==1 and T[1][0]==0 and T[0][B]==0 and T[1][B]==1 and T[A][0]==T[A][1]
 assert T[T[V][P]][Q]==0 and T[V][Q]==1 and T[T[U][P]][Q]==1
 print('RECHECK table=',T,' a,b,u,v,p,q=',tuple(vals),sep='');return T,vals
for n in (3,4,5,6):
 if search(n) is not None:break
