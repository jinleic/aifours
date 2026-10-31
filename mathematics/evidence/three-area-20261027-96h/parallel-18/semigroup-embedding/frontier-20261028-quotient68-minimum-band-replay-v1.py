import json
from itertools import product,permutations,combinations
from collections import Counter
from pathlib import Path
root=Path(__file__).resolve().parent
J=json.loads((root/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
K=json.loads((root/'frontier-20261028-quotient68-no9-arc-traces-v1.json').read_text())
L=json.loads((root/'frontier-20261028-quotient68-10band-host-data-v1.json').read_text())
Q=J['source_multiplication'];actor=J['actual_actor'];F=K['fibre_indices'];T=K['fibre_table']
assert len(Q)==len(actor)==68 and F==[1,9,17,25,32,37,45,53,61] and len(F)==9
assert all(actor[i]==[0,0,1] and Q[i][i]==i for i in F)
fmap={x:i for i,x in enumerate(F)}
assert all(Q[i][j] in fmap and T[fmap[i]][fmap[j]]==fmap[Q[i][j]] for i,j in product(F,repeat=2))
auts=[p for p in permutations(range(9)) if all(p[T[i][j]]==T[p[i]][p[j]] for i,j in product(range(9),repeat=2))]
assert len(auts)==2 and all(all(p[p[i]]==i for i in range(9)) for p in auts)
assert {tuple(t['automorphism']) for t in K['traces']}==set(auts)
for tr in K['traces']:
 aut=tr['automorphism'];dom=[set(range(9)) for _ in range(68)]
 for k,i in enumerate(F):dom[i]={k}
 empty=None;changes=0
 for ix,group in enumerate(tr['trace']):
  i,j=group['i'],group['j'];k=Q[i][j];w=actor[i][1]^(actor[i][2]&actor[j][0]);sx=set();sy=set();sz=set()
  for x in dom[i]:
   for y in dom[j]:
    z=T[x][aut[y] if w else y]
    if z in dom[k]:sx.add(x);sy.add(y);sz.add(z)
  supports={'left':(i,sx),'right':(j,sy),'out':(k,sz)}
  order={'left':0,'right':1,'out':2};last=-1
  for u in group['updates']:
   role=u['role'];assert order[role]>last;last=order[role]
   var,support=supports[role];assert u['var']==var and sorted(dom[var])==u['old']
   new=dom[var]&support;assert sorted(new)==u['new'] and new!=dom[var]
   dom[var]=new;changes+=1
   if not new:empty=var;assert ix==len(tr['trace'])-1 and u==group['updates'][-1]
 assert empty==tr['empty_variable'] and empty is not None
 print('PASS 9-band arc trace action=',aut,'steps=',changes,'empty variable=',empty,sep='')
B=L['band_table'];action=L['band_action'];coords=L['coordinates'];n=10
assert len(B)==len(action)==n and len(coords)==68
assert all(len(row)==n and all(0<=v<n for v in row) for row in B)
assert all(B[i][i]==i and action[action[i]]==i for i in range(n))
assert all(B[B[i][j]][k]==B[i][B[j][k]] for i,j,k in product(range(n),repeat=3))
assert all(B[B[B[B[a][b]][c]][d]][a]==B[B[B[B[B[B[a][b]][c]][a]][c]][d]][a] for a,b,c,d in product(range(n),repeat=4))
assert all(action[B[i][j]]==B[action[i]][action[j]] for i,j in product(range(n),repeat=2))
for i,j in product(range(68),repeat=2):
 w=actor[i][1]^(actor[i][2]&actor[j][0])
 assert coords[Q[i][j]]==B[coords[i]][action[coords[j]] if w else coords[j]]
pairs=[(i,j) for i,j in combinations(range(68),2) if actor[i]==actor[j]]
assert len(pairs)==256 and all(coords[i]!=coords[j] for i,j in pairs)
assert len(set(coords))==10 and max(Counter(map(tuple,actor)).values())==9
print('PASS exhaustive 9! automorphisms: exactly two C2 actions, both arc-inconsistent')
print('PASS 10-band: 1000 associativity, 10000 SN identities, all 4624 source products, 256 injectivity pairs')
print('RESULT: exact minimum actual-q band size=10, contingent on pinned source/actor verification')
