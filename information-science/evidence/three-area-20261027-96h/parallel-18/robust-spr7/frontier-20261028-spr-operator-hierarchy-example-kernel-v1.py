# Exact finite example for SPR preservation under D^k(I+hD).
from fractions import Fraction as Q
from math import comb
def ff(n,k):
 v=1
 for j in range(k):v*=n-j
 return v
def transform(a,k,h):
 out=[Q(ff(j,k),ff(7,k))*a[j] for j in range(k,8)]
 for j in range(k+1,8):out[j-k-1]+=h*Q(ff(j,k+1),ff(7,k))*a[j]
 return out
a=[Q(comb(7,j)) for j in range(8)];b=a[:];b[1]+=1
operator_levels=[]
for k in range(7):
 for h in (Q(0),Q(1,10),Q(1),Q(10)):
  aa=transform(a,k,h);bb=transform(b,k,h);P=pv(aa,bb);proof=exact_nonnegative_halfline(P,maxdepth=40,maxnodes=16000)
  if proof['status']!='NONNEGATIVE_PROVED' or not all(Q(v)>0 for leaf in proof['leaves'] for v in leaf['coefficients']):raise ValueError('PAIR')
  operator_levels.append({'order':k,'h':str(h),'denominator':[str(x) for x in aa],'numerator':[str(x) for x in bb],
    'pairing_polynomial':[str(x) for x in P],'proof':proof,'margin':str(min(Q(v) for leaf in proof['leaves'] for v in leaf['coefficients']))})
print('exact SPR operator hierarchy:',{'levels':len(operator_levels),'min_margin':str(min(Q(v['margin']) for v in operator_levels)),
 'max_leaves':max(len(v['proof']['leaves']) for v in operator_levels)})
