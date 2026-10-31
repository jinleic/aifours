import json
from itertools import product,permutations,combinations
from pathlib import Path
r=Path(__file__).resolve().parent
J=json.loads((r/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
K=json.loads((r/'frontier-20261028-quotient68-8band-unique-arc-traces-v1.json').read_text())
H=json.loads((r/'frontier-20261028-quotient68-8band-refined-actor-data-v1.json').read_text())
Q=J['source_multiplication'];F=K['fibre_indices'];T=K['fibre_table'];actor=H['actor'];P=H['actor_sandwich_bits']
assert F==[0,8,16,24,36,44,52,60] and len(F)==8
assert all(actor[i]==[0,0,0] and Q[i][i]==i for i in F)
fmap={x:i for i,x in enumerate(F)}
assert all(Q[i][j] in fmap and T[fmap[i]][fmap[j]]==fmap[Q[i][j]] for i,j in product(F,repeat=2))
auts=[p for p in permutations(range(8)) if all(p[T[i][j]]==T[p[i]][p[j]] for i,j in product(range(8),repeat=2))]
assert len(auts)==2 and all(all(p[p[i]]==i for i in range(8)) for p in auts)
assert {tuple(t['automorphism']) for t in K['traces']}==set(auts)
for tr in K['traces']:
 aut=tr['automorphism'];dom=[set(range(8)) for _ in range(68)]
 for k,i in enumerate(F):dom[i]={k}
 empty=None;changes=0
 for ix,group in enumerate(tr['trace']):
  i,j=group['i'],group['j'];k=Q[i][j];w=actor[i][1]^P[actor[i][2]][actor[j][0]];sx=set();sy=set();sz=set()
  for x in dom[i]:
   for y in dom[j]:
    z=T[x][aut[y] if w else y]
    if z in dom[k]:sx.add(x);sy.add(y);sz.add(z)
  supports={'left':(i,sx),'right':(j,sy),'out':(k,sz)};order={'left':0,'right':1,'out':2};last=-1
  for u in group['updates']:
   role=u['role'];assert order[role]>last;last=order[role];var,sup=supports[role]
   assert u['var']==var and sorted(dom[var])==u['old']
   new=dom[var]&sup;assert sorted(new)==u['new'] and new!=dom[var];dom[var]=new;changes+=1
   if not new:empty=var;assert ix==len(tr['trace'])-1 and u==group['updates'][-1]
 if tr['outcome']=='empty':
  assert empty==tr['empty_variable'] and empty is not None
  print('PASS empty action=',aut,'steps=',changes,'empty=',empty,sep='')
 else:
  assert tr['outcome']=='fixed' and empty is None and all(len(d)==1 for d in dom)
  assert [sorted(d) for d in dom]==tr['domains']
  coeff=[next(iter(d)) for d in dom]
  assert coeff==H['coordinates'] and aut==H['band_action']
  for i,j in product(range(68),repeat=2):
   w=actor[i][1]^P[actor[i][2]][actor[j][0]]
   assert coeff[Q[i][j]]==T[coeff[i]][aut[coeff[j]] if w else coeff[j]]
  assert all(coeff[i]!=coeff[j] for i,j in combinations(range(68),2) if actor[i]==actor[j])
  print('PASS unique singleton action=',aut,'steps=',changes,'and all host equations',sep='')
print('RESULT: unique minimum-band8 host over fixed D12 up to fibre relabelling; contingent on pinned source verification')
