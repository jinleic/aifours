from itertools import product
import z3

def run(n,ms=15000):
 m=z3.Function('smallnr_'+str(n),z3.IntSort(),z3.IntSort(),z3.IntSort());s=z3.Solver();s.set(timeout=ms)
 for a,b in product(range(n),repeat=2):s.add(m(a,b)>=0,m(a,b)<n)
 for a in range(n):s.add(m(a,a)==a)
 for a,b,c in product(range(n),repeat=3):s.add(m(m(a,b),c)==m(a,m(b,c)))
 for a,b,c,d in product(range(n),repeat=4):s.add(m(m(m(m(a,b),c),d),a)==m(m(m(m(m(m(a,b),c),a),c),d),a))
 x,y,z=z3.Ints(f'x{n} y{n} z{n}');s.add(x>=0,x<n,y>=0,y<n,z>=0,z<n)
 s.add(m(m(m(m(x,y),x),z),x)!=m(m(m(x,y),z),x))
 r=s.check();print('order',n,'nonregular SN',r,'reason',s.reason_unknown() if r==z3.unknown else '')
 if r!=z3.sat:return None
 M=s.model();T=tuple(tuple(M.eval(m(i,j)).as_long() for j in range(n)) for i in range(n));w=tuple(M.eval(a).as_long() for a in (x,y,z))
 assert all(T[i][i]==i for i in range(n))
 assert all(T[T[i][j]][k]==T[i][T[j][k]] for i,j,k in product(range(n),repeat=3))
 assert all(T[T[T[T[a][b]][c]][d]][a]==T[T[T[T[T[T[a][b]][c]][a]][c]][d]][a] for a,b,c,d in product(range(n),repeat=4))
 a,b,c=w;assert T[T[T[T[a][b]][a]][c]][a]!=T[T[T[a][b]][c]][a]
 print('RECHECK table=',T,' witness=',w,sep='');return T,w
for n in (2,3,4,5):
 if run(n) is not None:break
