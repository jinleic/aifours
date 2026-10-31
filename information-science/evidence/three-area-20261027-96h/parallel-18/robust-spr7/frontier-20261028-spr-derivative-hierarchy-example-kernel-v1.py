# Exact all-level example for the derivative-preservation theorem.
from fractions import Fraction as Q
from math import comb
a=[Q(comb(7,j)) for j in range(8)];b=a[:];b[1]+=1
levels=[]
for k in range(7):
 p=pv(a,b);proof=exact_nonnegative_halfline(p,maxdepth=40,maxnodes=16000)
 if proof['status']!='NONNEGATIVE_PROVED' or not all(Q(v)>0 for leaf in proof['leaves'] for v in leaf['coefficients']):raise ValueError('LEVEL')
 levels.append({'derivative_order':k,'denominator':[str(v) for v in a],'numerator':[str(v) for v in b],
  'pairing_polynomial':[str(v) for v in p],'proof':proof,'margin':str(min(Q(v) for leaf in proof['leaves'] for v in leaf['coefficients']))})
 n=7-k
 if n>1:a=[Q(j+1,n)*a[j+1] for j in range(n)];b=[Q(j+1,n)*b[j+1] for j in range(n)]
print('exact SPR derivative hierarchy:',[{'order':v['derivative_order'],'degree':len(v['denominator'])-1,
 'leaves':len(v['proof']['leaves']),'margin':v['margin']} for v in levels])
