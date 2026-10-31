# Bounded deterministic exact search for an actual strict negative-atom
# certificate on independently stable anisotropic boxes. Cubic roots are
# isolated with exact rational Sturm sequences, and two frequencies are chosen
# strictly inside every parity inversion band. No floats are used.
from fractions import Fraction as Q
from random import Random
from pathlib import Path
from hashlib import sha256
from math import lcm
import json,z3
R=Random(2026102825);root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def trim(p):
 while len(p)>1 and p[-1]==0:p.pop()
 return p
def mult(A,B):
 C=[Q(0)]*(len(A)+len(B)-1)
 for i,x in enumerate(A):
  for j,y in enumerate(B):C[i+j]+=x*y
 return trim(C)
def ev(p,t):return sum(x*t**j for j,x in enumerate(p))
def rem(p,q):
 p=p[:]
 while len(p)>=len(q) and p!=[0]:
  v=p[-1]/q[-1];shift=len(p)-len(q)
  for j,x in enumerate(q):p[j+shift]-=v*x
  trim(p)
 return p
def sturm(p):
 p=trim(p[:]);d=[Q(j)*p[j] for j in range(1,len(p))];seq=[p,trim(d)]
 while len(seq[-1])>1:
  r=[-x for x in rem(seq[-2],seq[-1])]
  if all(x==0 for x in r):raise ValueError('REPEATED_ROOT')
  seq.append(trim(r))
 return seq
def var(seq,t):
 signs=[1 if z>0 else -1 for z in (ev(p,t) for p in seq) if z!=0]
 return sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))
def isolate(p):
 seq=sturm(p);upper=Q(1)
 while var(seq,Q(0))-var(seq,upper)!=3 or ev(p,upper)==0:
  upper*=2
  if upper>2**60:raise ValueError('ROOT_BOUND')
 todo=[(Q(0),upper,3)];leaves=[]
 while todo:
  a,b,n=todo.pop()
  if n==1:leaves.append((a,b));continue
  m=(a+b)/2
  while ev(p,m)==0:m=(a+m)/2
  n1=var(seq,a)-var(seq,m);n2=n-n1
  if n2:todo.append((m,b,n2))
  if n1:todo.append((a,m,n1))
 leaves.sort();return seq,leaves
def refine(p,seq,interval):
 a,b=interval;m=(a+b)/2
 while ev(p,m)==0:m=(a+m)/2
 return (a,m) if var(seq,a)-var(seq,m)==1 else (m,b)
def parity(a):return [a[0],-a[2],a[4],-a[6]],[a[1],-a[3],a[5],-a[7]]
def corners(lo,hi):
 ret=[]
 for e,o in ((0,0),(0,1),(1,0),(1,1)):
  ret.append([(lo[j] if not(e if j%2==0 else o) else hi[j]) if j%4 in (0,1) else (hi[j] if not(e if j%2==0 else o) else lo[j]) for j in range(7)]+[Q(1)])
 return ret
def routh(a):
 rows=[[a[7],a[5],a[3],a[1]],[a[6],a[4],a[2],a[0]]]
 for _ in range(6):
  x,y=rows[-2:]
  if y[0]<=0:return False
  rows.append([(y[0]*x[j+1]-x[0]*y[j+1])/y[0] for j in range(3)]+[Q(0)])
 return all(r[0]>0 for r in rows)
def grid_for(cs):
 # E- from corner 0, E+ from corner 2; O- from corner 0, O+ from corner 1.
 E0,O0=parity(cs[0]);E1,_=parity(cs[2]);_,O1=parity(cs[1]);P=[E0,E1,O0,O1];iso=[isolate(p) for p in P];grid=set();bands=[]
 for offset in (0,2):
  for i in range(3):
   low=offset+(0 if i%2==0 else 1);high=offset+(1 if i%2==0 else 0)
   seq0,roots0=iso[low];seq1,roots1=iso[high];A=roots0[i];B=roots1[i]
   for _ in range(200):
    if A[1]<B[0]:break
    A=refine(P[low],seq0,A);B=refine(P[high],seq1,B)
   else:raise ValueError('ROOT_SEPARATION')
   t1=(2*A[1]+B[0])/3;t2=(A[1]+2*B[0])/3
   if not A[1]<t1<t2<B[0]:raise ValueError('GRID_BAND')
   grid.update((t1,t2));bands.append({'parity':'even' if offset==0 else 'odd','band':i+1,'root_isolates':[list(map(str,A)),list(map(str,B))],'nodes':[str(t1),str(t2)]})
 base=sorted(grid);grid.update((base[0]/2,base[-1]*2))
 grid.update((a+b)/2 for a,b in zip(base,base[1:]))
 return sorted(grid),bands
def row(a,t):
 E,O=parity(a);ee=ev(E,t);oo=ev(O,t)
 return [(ee*(-t)**(j//2) if j%2==0 else t*oo*(-t)**((j-1)//2))/(1+t)**7 for j in range(8)]
def zz(x):return z3.Q(x.numerator,x.denominator)
def run(case):
 alpha=R.choice([1,2,3,5]);center=[Q(alpha),Q(1)];pairs=[]
 for _ in range(3):
  x=R.choice([1,2,3,5]);y=R.choice([3,7,13,25,50,100]);pairs.append([x,y]);center=mult(center,[Q(x*x+y*y),Q(2*x),Q(1)])
 L=[Q(R.choice([1,2,4,8]),8) for _ in range(7)];U=[Q(R.choice([1,2,4,8,16,32]),8) for _ in range(7)]
 def bounds(r):return [center[j]*(1-r*L[j]) for j in range(7)],[center[j]*(1+r*U[j]) for j in range(7)]
 a=Q(0);b=min(1/x for x in L)
 for _ in range(20):
  m=(a+b)/2;lo,hi=bounds(m)
  if all(routh(c) for c in corners(lo,hi)):a=m
  else:b=m
 scale=a*Q(99999,100000);lo,hi=bounds(scale);cs=corners(lo,hi)
 if not scale>0 or not all(routh(c) for c in cs):raise ValueError('STABILITY')
 grid,bands=grid_for(cs);atoms=[(ci,t,row(c,t)) for ci,c in enumerate(cs) for t in grid]
 weights=[z3.Real('w'+str(case)+'_'+str(i)) for i in range(len(atoms))];solver=z3.Solver();solver.set(timeout=4000)
 solver.add(*(w>=0 for w in weights))
 for j in range(8):solver.add(sum(weights[i]*zz(z[2][j]) for i,z in enumerate(atoms))<=-1)
 status=solver.check();out={'case':case,'center_first_order':alpha,'center_pairs':pairs,'scale':str(scale),'lower':list(map(str,lo)),'upper':list(map(str,hi)),'bands':bands,'atom_count':len(atoms),'status':str(status)}
 if status==z3.sat:
  m=solver.model();vals=[m.eval(w,model_completion=True) for w in weights];w=[Q(x.numerator_as_long(),x.denominator_as_long()) for x in vals]
  sums=[sum(w[i]*atoms[i][2][j] for i in range(len(atoms))) for j in range(8)]
  if not all(x<0 for x in sums):raise ValueError('STRICT_CERTIFICATE')
  out.update({'support':[{'corner':ci,'t':str(t),'weight':str(w[i]),'weight_convention':'compactified_row'} for i,(ci,t,v) in enumerate(atoms) if w[i]>0],'coefficient_sums':list(map(str,sums))})
 return out
for case in range(30):
 result=run(case);out=root/('frontier-20261028-sturm-band-strict-certificate-case-%02d-v1.json'%case);text=json.dumps(result,indent=2,sort_keys=True)+'\n';out.write_text(text)
 print('band-case',case,result['status'],'sha256',sha256(text.encode()).hexdigest())
 if result['status']=='sat':break
