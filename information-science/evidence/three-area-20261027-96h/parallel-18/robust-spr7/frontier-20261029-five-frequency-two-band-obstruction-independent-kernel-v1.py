# Finite exact phase-class classification for five distinct positive nodes
# with both endpoints. No selected denominators or numerical approximation.
from itertools import product
phase_signs=((1,1),(-1,1),(-1,-1),(1,-1),(1,1),(-1,1),(-1,-1))
base=(1,-1,1,-1,1)
root_names=('E1','O1','E2','O2','E3','O3')
result=[]
for k in range(6):
 for l in range(6):
  signs=[(base[i]*(-1 if i<k else 1),base[i]*(-1 if i<l else 1)) for i in range(5)]
  classes=[[q for q in range(7) if phase_signs[q]==sgn] for sgn in signs]
  for qs in product(*classes):
   if all(qs[i]<=qs[j]+1 for i in range(5) for j in range(i+1,5)):
    backwards=[(i+1,root_names[qs[i+1]]) for i in range(4) if qs[i+1]==qs[i]-1]
    result.append((k,l,qs,tuple(backwards)))
expected=[
 (1,3,(2,1,3,2,4),((1,'O1'),(3,'E2'))),
 (1,4,(2,1,3,5,4),((1,'O1'),(4,'E3'))),
 (2,4,(2,4,3,5,4),((2,'O2'),(4,'E3'))),
]
assert result==expected,(result,expected)
assert all(1<=k<l<=4 and k+1<l for k,l,_,_ in result)
assert all(back[0][1][0]=='O' and back[1][1][0]=='E' for _,_,_,back in result)
# Removing phase order must produce extra cases, so the ordering assertion is active.
without_order=0
for k in range(6):
 for l in range(6):
  signs=[(base[i]*(-1 if i<k else 1),base[i]*(-1 if i<l else 1)) for i in range(5)]
  counts=[sum(sgn==p for p in phase_signs) for sgn in signs]
  n=1
  for c in counts:n*=c
  without_order+=n
assert without_order>len(result)
print('exact threshold pairs:',36,'surviving class patterns:',len(result),'unrestricted patterns:',without_order)
for k,l,qs,back in result:print('switches',k,l,'classes',qs,'backward bands',back)
