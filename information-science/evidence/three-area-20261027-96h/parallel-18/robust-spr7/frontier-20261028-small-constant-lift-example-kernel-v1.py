# Exact 6->7 lifting example; full width in all seven uncertain coefficients.
from fractions import Fraction as Q
qbase=[Q(1),Q(6),Q(15),Q(20),Q(15),Q(6)];r=Q(1,1000)
lo=[Q(1,2000)]+[v-r for v in qbase];hi=[Q(1,1000)]+[v+r for v in qbase]
b=[Q(1,100),Q(1),Q(6),Q(15),Q(20),Q(15),Q(6),Q(1)]
if not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('WIDTH')
qmargin=Q(1)-Q(64)*6*r;MO=Q(32003,1000);MG=Q(32);epsilon=Q(1,100);A=Q(1,1000);kappa=qmargin-epsilon*MO-A*MG
if qmargin!=Q(77,125) or kappa!=Q(26397,100000) or kappa<=0:raise ValueError('LIFT_BOUND')
cs=corners(lo,hi)
if not all(routh_ok(a) and integer_hurwitz(a) for a in cs):raise ValueError('STABILITY')
polys=[pairing_polynomial(a,b) for a in cs];proofs=[whole_halfline(p,max_depth=40,max_nodes=16000) for p in polys]
if not all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in proofs):raise ValueError('PAIRING')
for p,proof in zip(polys,proofs):verify_leaves_by_power(p,proof)
small=epsilon*lo[0]/2**7;delta=min(kappa/2,small);S=1+sum(hi)
print('small-constant lift exact example:',{'lower':[str(v) for v in lo],'upper':[str(v) for v in hi],'numerator':[str(v) for v in b],
 'q_margin':str(qmargin),'MO':str(MO),'MG':str(MG),'kappa':str(kappa),'lift_delta':str(delta),'S':str(S),'ratio_margin':str(delta/S**2),
 'direct_leaf_counts':[len(p['leaves']) for p in proofs],'direct_margin':str(min(Q(p['margin']) for p in proofs))})
