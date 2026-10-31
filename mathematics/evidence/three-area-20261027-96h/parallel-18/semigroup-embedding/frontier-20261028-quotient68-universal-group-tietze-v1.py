import json
from pathlib import Path
from collections import Counter
from itertools import product
r=Path(__file__).resolve().parent
J=json.loads((r/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
K=json.loads((r/'frontier-20261028-quotient68-8band-refined-actor-data-v1.json').read_text())
Q=J['source_multiplication'];actor=K['actor'];n=68
# x_s = s+1; p_(column1,row1)=69; p_(column2,row1)=70.
def pgen(col,row):return () if col==0 or row==0 else (68+col,)
def reduce(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(x)
 return tuple(out)
def inverse(w):return tuple(-x for x in w[::-1])
def canonical(w):
 w=reduce(w)
 while len(w)>1 and w[0]==-w[-1]:w=w[1:-1]
 if not w:return ()
 choices=[]
 for v in (w,inverse(w)):choices.extend(v[i:]+v[:i] for i in range(len(v)))
 return min(choices)
def subword(w,g,repl):
 out=[]
 for x in w:out.extend(repl if x==g else inverse(repl) if x==-g else (x,))
 return reduce(out)
rels={canonical((-(Q[s][t]+1),s+1)+pgen(actor[s][2],actor[t][0])+(t+1,)) for s,t in product(range(n),repeat=2)}
rels.discard(());t=3;elims=[]
while True:
 choices=[]
 for w in rels:
  counts=Counter(map(abs,w))
  for g,c in counts.items():
   if g!=t and c==1:choices.append((len(w),g,w))
 if not choices:break
 _,g,w=min(choices);pos=next(i for i,x in enumerate(w) if abs(x)==g);A=w[:pos];B=w[pos+1:]
 repl=reduce(inverse(A)+inverse(B)) if w[pos]>0 else reduce(B+A)
 assert g not in map(abs,repl) and reduce(subword(w,g,repl))==()
 elims.append({'generator':g,'relation':list(w),'replacement':list(repl)})
 rels={canonical(subword(v,g,repl)) for v in rels};rels.discard(())
print('Tietze eliminations=',len(elims),' remaining relation count=',len(rels),' remaining generators=',sorted({abs(x) for w in rels for x in w}),sep='')
print('remaining relations=',sorted(rels))
assert len(elims)==69 and rels=={(-3,-3),(-3,-3,-3,-3)}
# The length-four relator is the square of the length-two relator and is redundant.
# The exact target C2 assignment satisfies all original source relations and sends x_2 nontrivially.
assert actor[2][1]==1
assert all(actor[Q[s][t]][1]==actor[s][1]^K['actor_sandwich_bits'][actor[s][2]][actor[t][0]]^actor[t][1] for s,t in product(range(n),repeat=2))
print('PASS presented group exactly C2: one generator t, relation t^2=1, nontrivial C2 quotient')
