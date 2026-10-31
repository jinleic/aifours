# Exact finite example for reciprocal-derivative SPR-preserving operators.
from fractions import Fraction as Q
from math import comb
def complement(a):
 n=len(a)-1;return [Q(n-j)*a[j] for j in range(n)]
def reversed_operator(a,h):
 n=len(a)-1;out=a[:];q=complement(a)
 for j in range(n):out[j+1]+=h*q[j]
 return out
a=[Q(comb(7,j)) for j in range(8)];b=a[:];b[1]+=1
recip_levels=[]
for label,h in [('complement',None)]+[('reciprocal_T',x) for x in (Q(0),Q(1,10),Q(1),Q(10))]:
 aa=complement(a) if h is None else reversed_operator(a,h);bb=complement(b) if h is None else reversed_operator(b,h)
 P=pv(aa,bb);proof=exact_nonnegative_halfline(P,maxdepth=40,maxnodes=16000)
 if proof['status']!='NONNEGATIVE_PROVED' or not all(Q(v)>0 for leaf in proof['leaves'] for v in leaf['coefficients']):raise ValueError('PAIR')
 recip_levels.append({'operator':label,'h':str(h) if h is not None else None,'denominator':[str(v) for v in aa],
   'numerator':[str(v) for v in bb],'pairing_polynomial':[str(v) for v in P],'proof':proof,
   'margin':str(min(Q(v) for leaf in proof['leaves'] for v in leaf['coefficients']))})
print('exact reciprocal-operator example:',[{'operator':r['operator'],'h':r['h'],'degree':len(r['denominator'])-1,
 'leaves':len(r['proof']['leaves']),'margin':r['margin']} for r in recip_levels])
