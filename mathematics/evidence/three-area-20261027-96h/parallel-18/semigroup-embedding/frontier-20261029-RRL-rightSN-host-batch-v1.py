"""Bounded exploration (NOT proof): random right-regular-local (RRL) original sources inside
P(B5^1,D8) whose coordinate hull is NOT seminormal and which have lambda_S-related pairs; Z3 searches
for a faithful RIGHTSN physical host over the GIVEN D8 actor, band sizes 2..NMAX.  SAT results are
exactly rechecked.  UNSAT/unknown only bound this actor and these sizes."""
import sys,json,random,time,importlib.util
from itertools import product
from pathlib import Path
import z3
root=Path(__file__).resolve().parent
def load(name,fn):
 sp=importlib.util.spec_from_file_location(name,root/fn);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
sn2=load('sn2','frontier-20261029-SN-pattern-counterexample-search-v2.py')
def find_rightSN_host(S,mul,actor,n,P,timeout_ms):
 Bs,el=z3.EnumSort(f'R{n}_{random.random()}',[f'r{k}_{random.random()}' for k in range(n)])
 m=z3.Function(f'm{random.random()}',Bs,Bs,Bs);sg=z3.Function(f'sg{random.random()}',Bs,Bs)
 beta={s:z3.Const(f'b{s}_{random.random()}',Bs) for s in S}
 so=z3.Solver();so.set('timeout',timeout_ms)
 for x in el:so.add(m(x,x)==x,sg(sg(x))==x)
 for x,y in product(el,repeat=2):so.add(sg(m(x,y))==m(sg(x),sg(y)))
 for x,y,z in product(el,repeat=3):
  so.add(m(m(x,y),z)==m(x,m(y,z)))
  so.add(m(m(m(m(m(m(x,y),x),z),x),y),x)==m(m(m(m(x,z),x),y),x))   # e x e y e x e = e y e x e with (e,x,y)=(x,y,z)
 for s,t in product(S,repeat=2):
  i,g,l=actor[s];j,h,u=actor[t];wt=g^P[l][j]
  so.add(beta[mul[(s,t)]]==m(beta[s],sg(beta[t]) if wt else beta[t]))
 for s,t in product(S,repeat=2):
  if s<t and actor[s]==actor[t]:so.add(beta[s]!=beta[t])
 r=so.check()
 if r!=z3.sat:return str(r),None
 md=so.model();idx={str(e):k for k,e in enumerate(el)}
 ev=lambda t:idx[str(md.eval(t,model_completion=True))]
 return 'sat',([[ev(m(x,y)) for y in el] for x in el],[ev(sg(x)) for x in el],{s:ev(beta[s]) for s in S})
def recheck(S,mul,actor,P,Mv,sv,bv):
 n=len(Mv);R=range(n);mm=lambda *xs:__import__('functools').reduce(lambda a,b:Mv[a][b],xs)
 assert all(Mv[x][x]==x for x in R)
 assert all(Mv[Mv[x][y]][z]==Mv[x][Mv[y][z]] for x,y,z in product(R,repeat=3))
 assert all(mm(e,x,e,y,e,x,e)==mm(e,y,e,x,e) for e,x,y in product(R,repeat=3))
 assert all(sv[sv[x]]==x and sv[Mv[x][y]]==Mv[sv[x]][sv[y]] for x,y in product(R,repeat=2))
 for s,t in product(S,repeat=2):
  i,g,l=actor[s];j,h,u=actor[t];wt=g^P[l][j]
  assert bv[mul[(s,t)]]==Mv[bv[s]][sv[bv[t]] if wt else bv[t]]
 assert len({(bv[s],actor[s]) for s in S})==len(S)
if __name__=='__main__':
 seed=int(sys.argv[1]);count=int(sys.argv[2]);NMAX=int(sys.argv[3]);tmo=int(sys.argv[4])
 random.seed(seed);P=[[0,0],[0,1]];out=[];tried=0
 configs=[(d,a) for d in (False,True) for a in ('trivial','swap')];tables={c:sn2.make(*c) for c in configs}
 while len(out)<count:
  tried+=1;c=random.choice(configs);H,T=tables[c]
  gens=random.sample(range(48),random.randint(2,5));S=sn2.closure(T,gens)
  if len(S)>40 or sn2.analyse(H,T,S) is None:continue
  pos={s:k for k,s in enumerate(S)};M=[[pos[T[a][b]] for b in S] for a in S];E=[x for x in range(len(S)) if M[x][x]==x]
  corners=[[x for x in E if M[M[g][x]][g]==x] for g in E]
  if not all(M[M[x][y]][x]==M[y][x] for C in corners for x in C for y in C):continue   # RRL
  locR=sum(1 for C in corners for x in C for y in C if x<y and M[x][y]==y and M[y][x]==x)
  if locR==0:continue
  mul={(s,t):T[s][t] for s in S for t in S};actor={s:H[s][1] for s in S}
  rec={'config':str(c),'size':len(S),'local_R_pairs':locR,'gens':[str(H[g]) for g in gens],'runs':[]}
  for n in range(2,NMAX+1):
   t0=time.time();r,sol=find_rightSN_host(S,mul,actor,n,P,tmo)
   rec['runs'].append((n,r,round(time.time()-t0,1)))
   if r=='sat':recheck(S,mul,actor,P,*sol);rec['rightSN_host_band_size']=n;break
  out.append(rec);print(json.dumps(rec));sys.stdout.flush()
 print(json.dumps({'seed':seed,'sources':len(out),'generated':tried}))
