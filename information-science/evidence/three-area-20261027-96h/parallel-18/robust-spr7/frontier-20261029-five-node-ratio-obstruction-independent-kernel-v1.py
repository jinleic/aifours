# Exhaust the choices of three zeroed frequencies in the three previously
# classified five-node phase cases. 'large/small' is the required sign of
# gamma relative to t*|O|/|E|; same-sign incompatible nodes are discarded.
from itertools import combinations
phase=((1,1),(-1,1),(-1,-1),(1,-1),(1,1),(-1,1),(-1,-1))
cases=((2,1,3,2,4),(2,1,3,5,4),(2,4,3,5,4))
out=[]
for qs in cases:
 candidates=[]
 for zero in combinations(range(5),3):
  keep=[i for i in range(5) if i not in zero];need=[]
  for i in keep:
   f=(-1)**sum(j<i for j in zero);e,o=phase[qs[i]]
   if e==o:kind='auto' if e==f else 'impossible'
   else:kind='large' if e==f else 'small'
   need.append((i+1,kind))
  if all(v!='impossible' for _,v in need):candidates.append((tuple(i+1 for i in zero),tuple(need)))
 out.append(candidates)
assert out==[
 [((1,4,5),((2,'large'),(3,'small')))],
 [((1,2,5),((3,'large'),(4,'small'))),((1,3,5),((2,'large'),(4,'small'))),((1,4,5),((2,'large'),(3,'small')))],
 [((1,2,5),((3,'large'),(4,'small')))]
]
print({'phase_cases':3,'zero_triples_each':10,'feasible_sign_patterns':[len(x) for x in out],'quantitative_requirements':['r2>r3','r2>r3>r4','r3>r4']})
