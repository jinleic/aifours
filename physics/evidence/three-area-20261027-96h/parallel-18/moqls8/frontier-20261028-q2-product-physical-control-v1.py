#!/usr/bin/env python3
"""Exercise cross-cell product singleton constraints on a real four-family."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
M=[('net','frontier-20261028-anchor-sparse-net-obstructions-v1.py','6e46c39749b322809758b16d64171c89d429a4d6bfcdc848bed86508f9f1c8e3'),
   ('phys','frontier-20261028-q1-support-physical-control-v1.py','ca8f42999f128a8f42a98c480c81eca747abeb60497af9513202f881d0234a8c')]
mods={}
for name,file,pin in M:
 if hashlib.sha256((H/file).read_bytes()).hexdigest()!=pin:raise ValueError('module pin')
 s=importlib.util.spec_from_file_location(name,H/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);mods[name]=m
V=range(8)
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 b=(H/'frontier-20261028-q1-support-physical-control-receipt-v1.json').read_bytes();pin='48d467c1493904d5b4c3108e12ac545875c72e438277a5597d697efb3bf80ef3'
 if hashlib.sha256(b).hexdigest()!=pin:raise ValueError('control pin')
 Q=json.loads(b)['positive_Q_classical_symbols'];nets=sum((mods['net'].read_catalogue(*z) for z in mods['net'].P),[])
 T=mods['net'].orient(nets[38],0,1,0);R=[T[0][i][j] for i in V for j in V];C=[T[1],T[2]]
 full=mods['phys'].physical(Q,T)
 if any(full.values()):raise ValueError('positive physical')
 facts={x:(x//8,x%8,*(L[x//8][x%8] for L in C)) for x in range(64)}
 A={x:set(V)-set(facts[x][1:]) for x in range(8,64)}
 pairs=[(x,y) for x,y in itertools.combinations(range(8,64),2) if not any(a==b for a,b in zip(facts[x],facts[y]))]
 def test(U,W):
  violations=0;clauses=0
  for x,y in pairs:
   common=A[x]&A[y]
   B0={t:(U[x]==t and U[y]==t) for t in common};B1={t:(W[x]==t and W[y]==t) for t in common}
   for t in common:
    for u in common:
     clauses+=1
     if not ((not B0[t]) or any(B0[v] for v in common if v!=t) or (not B1[u]) or any(B1[w] for w in common if w!=u)):violations+=1
  return violations,clauses
 good,count=test(Q,R)
 if good:raise ValueError('actual family violates product clause')
 found=None
 for x,y in pairs:
  if Q[x] in A[y] and R[x] in A[y] and Q[x]!=R[x]:found=(x,y);break
 if found is None:raise ValueError('no valid negative mutation')
 x,y=found;badQ=Q.copy();badR=R.copy();badQ[y]=badQ[x];badR[y]=badR[x]
 bad,_=test(badQ,badR)
 if not bad:raise ValueError('product collision not detected')
 out={'result':'PASS_PHYSICAL_CROSS_PRODUCT_POSITIVE_AND_NEGATIVE',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'positive_full_physical_gram_errors':full,'nonadjacent_pairs':len(pairs),'cross_product_clauses_evaluated':count,
      'positive_clause_violations':good,'negative_mutation_cells':[x,y],'negative_clause_violations':bad,
      'elapsed_seconds':time.monotonic()-start,'limits':'Physical four-classical control on a different 4-net; no q2 witness.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
