# Exact finite symbolic phase-word classification, run in Python Eval only.
# Variables are signs, zeros and phase labels; no frequency or box is sampled.
from itertools import product
from collections import Counter
signs=(-1,0,1)
classes={(-1,-1):(2,6),(-1,1):(1,5),(1,-1):(3,),(1,1):(0,4),
         (0,1):(0,1,4,5),(0,-1):(2,3),(1,0):(3,4),(-1,0):(1,2,5,6)}
def variation(s):
    nonzero=[x for x in s if x]
    return sum(nonzero[i]!=nonzero[i-1] for i in range(1,len(nonzero))), (nonzero[0] if nonzero else None)
words=[]
for even in product(signs,repeat=5):
    changes,start=variation(even)
    if changes<3 or (changes==3 and start!=-1):continue
    for odd in product(signs,repeat=5):
        changes,start=variation(odd)
        if changes<3 or (changes==3 and start!=-1):continue
        if any((even[j],odd[j])==(0,0) for j in range(5)):continue
        for q in product(*(classes[(even[j],odd[j])] for j in range(5))):
            if all(q[i]<=q[j]+1 for i in range(5) for j in range(i+1,5)):
                words.append((even,odd,q))
print('distinct sign profiles:',len({(e,o) for e,o,q in words}))
print('phase assignments by word:',dict(Counter(q for e,o,q in words)))
