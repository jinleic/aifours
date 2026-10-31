import json
from pathlib import Path
from itertools import product
r=Path(__file__).resolve().parent
S=json.loads((r/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
A=json.loads((r/'frontier-20261028-quotient68-8band-refined-actor-data-v1.json').read_text())
P=json.loads((r/'frontier-20261028-quotient68-universal-group-trace-v1.json').read_text())
T=S['source_multiplication'];actor=A['actor']
def inv(w):return tuple(-x for x in w[::-1])
def free(w):
 stack=[]
 for x in w:
  if stack and stack[-1]==-x:stack.pop()
  else:stack.append(x)
 return tuple(stack)
def cyc(w):
 v=free(w)
 while len(v)>1 and v[0]==-v[-1]:v=v[1:-1]
 if not v:return ()
 return min(u[k:]+u[:k] for u in (v,inv(v)) for k in range(len(u)))
def substitute(w,g,repl):
 return free([a for x in w for a in (repl if x==g else inv(repl) if x==-g else (x,))])
def pm(c,row):return () if c==0 or row==0 else (68+c,)
rels={cyc((-(T[i][j]+1),i+1)+pm(actor[i][2],actor[j][0])+(j+1,)) for i,j in product(range(68),repeat=2)};rels.discard(())
active=set(range(1,71));count=0
for step in P['steps']:
 g=step['generator'];w=tuple(step['relation']);v=tuple(step['replacement'])
 assert g in active and g!=3 and w in rels and sum(abs(x)==g for x in w)==1
 assert g not in map(abs,v) and set(map(abs,v))<=active and free(substitute(w,g,v))==()
 active.remove(g);rels={cyc(substitute(w0,g,v)) for w0 in rels};rels.discard(());count+=1
 assert all(set(map(abs,w0))<=active for w0 in rels)
assert count==69 and active=={3} and rels=={(-3,-3),(-3,-3,-3,-3)}
assert sorted(map(list,rels))==P['final_relators']
assert all(actor[T[i][j]][1]==actor[i][1]^A['actor_sandwich_bits'][actor[i][2]][actor[j][0]]^actor[j][1] for i,j in product(range(68),repeat=2))
assert actor[2][1]==1
print('PASS all 4624 universal group relators and 69 exact generator-elimination steps')
print('PASS final <t | t^2=1,t^4=1>; second relator redundant and nontrivial C2 map checked')
print('RESULT universal CS group C2, conditional on the written universal presentation theorem')
