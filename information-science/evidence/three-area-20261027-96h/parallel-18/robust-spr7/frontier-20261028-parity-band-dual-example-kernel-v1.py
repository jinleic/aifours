# Exact dual example for the parity-band no-inversion obstruction.
# All four corners at one rational frequency inside each disjoint parity band.
from fractions import Fraction as Q
lo1=[Q(x) for x in five_frozen['boundary_lower']];hi1=[Q(x) for x in five_frozen['boundary_upper']]
center=[(lo1[j]+hi1[j])/2 for j in range(7)]+[Q(1)];rho=Q(1,2)
lo=[center[j]-rho*(hi1[j]-lo1[j])/2 for j in range(7)];hi=[center[j]+rho*(hi1[j]-lo1[j])/2 for j in range(7)];cs=corners(lo,hi)
if not all(routh_ok(a) and integer_hurwitz(a) for a in cs):raise ValueError('STABILITY')
Er=[Q(1,2),Q(5,2),Q(7)];Or=[Q(3,2),Q(4),Q(9)]
def cubic(roots):
    v=[Q(1)]
    for r in roots:
        w=[Q(0)]*(len(v)+1)
        for i,x in enumerate(v):w[i]+=r*x;w[i+1]+=x
        v=w
    return v
E=cubic(Er);O=cubic(Or);b=[Q(0)]*8
for i,x in enumerate(E):b[2*i]=x
for i,x in enumerate(O):b[2*i+1]=x
if not all(x>0 for x in b):raise ValueError('NUMERATOR')
grid=sorted(set(Er+Or));vals=[]
for ci,a in enumerate(cs):
    for t in grid:
        value=independent_pair_t(a,b,t)/(1+t)**7
        if value<=0:raise ValueError('DUAL_SIGN')
        vals.append(value)
    v0=independent_pair_t(a,b,Q(0))
    if v0<=0:raise ValueError('ZERO_SIGN')
    vals.append(v0)
vals.append(b[7])
print('parity-band dual example:',{'lower':[str(v) for v in lo],'upper':[str(v) for v in hi],
 'numerator':[str(v) for v in b],'positive_finite_grid_atoms':len(vals)-1,'infinity_positive':b[7]>0,
 'min_normalized_pairing':str(min(vals))})
