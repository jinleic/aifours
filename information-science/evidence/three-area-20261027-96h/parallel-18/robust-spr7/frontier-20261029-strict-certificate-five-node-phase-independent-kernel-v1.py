# Exhaust all actual septic phase-class sign sequences after the written
# oriented-moment lemma; no selected box or floating arithmetic.
from itertools import product,combinations
signs=((1,1),(-1,1),(-1,-1),(1,-1),(1,1),(-1,1),(-1,-1))
roots=('E1','O1','E2','O2','E3','O3')
def oriented(v):return any(tuple(v[i] for i in ix)==(-1,1,-1,1) for ix in combinations(range(len(v)),4))
def survivors(m,ordered=True):
 ans=[]
 for qs in product(range(7),repeat=m):
  if ordered and any(qs[i]>qs[j]+1 for i in range(m) for j in range(i+1,m)):continue
  if not oriented([signs[q][0] for q in qs]) or not oriented([signs[q][1] for q in qs]):continue
  back=tuple((i+1,roots[qs[i+1]]) for i in range(m-1) if qs[i+1]==qs[i]-1)
  ans.append((qs,back))
 return ans
four=survivors(4);five=survivors(5)
assert four==[]
assert five==[((2,1,3,2,4),((1,'O1'),(3,'E2'))),((2,1,3,5,4),((1,'O1'),(4,'E3'))),((2,4,3,5,4),((2,'O2'),(4,'E3')))]
free4=len(survivors(4,False));free5=len(survivors(5,False));assert free4>0 and free5>len(five)
print({'four_node_survivors':0,'five_node_survivors':len(five),'without_phase_order_4':free4,'without_phase_order_5':free5,'five_node_cases':five})
