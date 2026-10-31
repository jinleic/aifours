"""Exploratory: for random SN bands Y (found by Z3 with random side constraints), compute the least
congruences lam (quotient LEFTSN: e x e y e x e = e x e y e) and rho (quotient RIGHTSN:
e x e y e x e = e y e x e) by generating all instances, and test whether lam ∩ rho is trivial.
A failure exhibits an SN band that is NOT a subdirect product of a LEFTSN and a RIGHTSN band."""
import random,json,sys,time
from itertools import product
import z3
def least(T,inst):
 n=len(T);par=list(range(n))
 def root(x):
  while par[x]!=x:par[x]=par[par[x]];x=par[x]
  return x
 todo=list(inst)
 while todo:
  a,b=todo.pop();ra,rb=root(a),root(b)
  if ra==rb:continue
  par[rb]=ra
  for z in range(n):todo.append((T[a][z],T[b][z]));todo.append((T[z][a],T[z][b]))
 return [root(x) for x in range(n)]
def m(T,*xs):
 r=xs[0]
 for x in xs[1:]:r=T[r][x]
 return r
def decompose(T):
 n=len(T);R=range(n)
 lam=least(T,[(m(T,e,x,e,y,e,x,e),m(T,e,x,e,y,e)) for e,x,y in product(R,repeat=3)])
 rho=least(T,[(m(T,e,x,e,y,e,x,e),m(T,e,y,e,x,e)) for e,x,y in product(R,repeat=3)])
 bad=[(a,b) for a in R for b in R if a<b and lam[a]==lam[b] and rho[a]==rho[b]]
 return len(set(lam)),len(set(rho)),bad
def random_SN_band_uf(n,seed,extra=6):
 Bs,el=z3.EnumSort(f'Y{n}_{seed}',[f'y{k}_{seed}' for k in range(n)])
 f=z3.Function(f'f_{seed}',Bs,Bs,Bs);so=z3.Solver();so.set('random_seed',seed);so.set('timeout',90000)
 for x in el:so.add(f(x,x)==x)
 for x,y,z in product(el,repeat=3):so.add(f(f(x,y),z)==f(x,f(y,z)))
 for a,b,c,d in product(el,repeat=4):so.add(f(f(f(f(a,b),c),d),a)==f(f(f(f(f(f(a,b),c),a),c),d),a))
 rnd=random.Random(seed)
 # random side constraints to diversify, plus: not LEFTSN and not RIGHTSN witnesses
 e,x,y=el[0],el[1],el[2]
 so.add(f(f(f(f(f(f(e,x),e),y),e),x),e)!=f(f(f(f(e,x),e),y),e))
 e2,x2,y2=el[rnd.randrange(n)],el[rnd.randrange(n)],el[rnd.randrange(n)]
 so.add(f(f(f(f(f(f(e2,x2),e2),y2),e2),x2),e2)!=f(f(f(f(e2,y2),e2),x2),e2))
 for _ in range(extra):
  a,b,c=(el[rnd.randrange(n)] for _ in range(3))
  so.add(f(a,b)==c if rnd.random()<0.5 else f(a,b)!=c)
 if so.check()!=z3.sat:return None
 md=so.model();ix={str(v):k for k,v in enumerate(el)}
 return [[ix[str(md.eval(f(a,b),model_completion=True))] for b in el] for a in el]
if __name__=='__main__':
 budget=float(sys.argv[1]);t0=time.time();found=[];tested=0;seed=0
 while time.time()-t0<budget:
  seed+=1;n=random.Random(seed).choice([5,6,7,8])
  T=random_SN_band_uf(n,seed)
  if T is None:continue
  tested+=1;l,r,bad=decompose(T)
  if bad:
   found.append({'n':n,'seed':seed,'table':T,'lam_classes':l,'rho_classes':r,'collapsed_pairs':bad[:5]})
   print(json.dumps(found[-1]));sys.stdout.flush()
   if len(found)>=3:break
 print(json.dumps({'tested':tested,'found':len(found),'seconds':round(time.time()-t0,1)}))
