# Exact full-width stable septic box whose sextic tail contains an unstable
# polynomial. This demonstrates a limitation of the small-constant lift.
from fractions import Fraction as Q
def tail_corner7(lower,upper):
    out=[]
    for es in (0,1):
        for oside in (0,1):
            a=[Q(0)]*8;a[7]=Q(1)
            for j in (0,2,4,6):a[j]=lower[j] if ((j//2)%2==0)==(es==0) else upper[j]
            for j in (1,3,5):a[j]=lower[j] if ((j//2)%2==0)==(oside==0) else upper[j]
            out.append(a)
    return out
p=[Q(1),Q(1)]
for w in (4,5,6):p=conv_exact(p,[Q(1+w*w),Q(2),Q(1)])
if p!=[Q(v) for v in (16354,20420,6419,2681,420,98,7,1)]:raise ValueError('CENTER')
q=p[1:];qmin= minors(q)
if qmin[4]!=-1933582924:raise ValueError('TAIL_DELTA5')
rev=q[::-1];M=[[int(rev[2*j-i]) if 0<=2*j-i<len(rev) else 0 for j in range(1,6)] for i in range(1,6)]
if bareiss_det(M)!=qmin[4]:raise ValueError('TAIL_BAREISS')
base=pairing_polynomial(p,p);proof=whole_halfline(base,max_depth=40,max_nodes=18000)
if proof['status']!='STRICT_POSITIVITY':raise ValueError('BASE_PAIR')
verify_leaves_by_power(base,proof)
r=Q(1,10**9);B=sum(abs(x) for x in p);delta0=Q(proof['margin']);delta=delta0-7*r*B
if delta<=0:raise ValueError('PERTURBATION')
lo=[p[j]-r for j in range(7)];hi=[p[j]+r for j in range(7)];cs=tail_corner7(lo,hi)
if not all(0<lo[j]<hi[j] for j in range(7)) or not all(routh_ok(a) and integer_hurwitz(a) for a in cs):raise ValueError('STABILITY')
ps=[pairing_polynomial(a,p) for a in cs];proofs=[whole_halfline(v,max_depth=40,max_nodes=18000) for v in ps]
if not all(v['status']=='STRICT_POSITIVITY' for v in proofs):raise ValueError('EXPANDED_PAIR')
for v,pr in zip(ps,proofs):verify_leaves_by_power(v,pr)
S=1+sum(hi)
print('stable septic with unstable sextic tail:',{'center':[str(v) for v in p],'tail':[str(v) for v in q],'tail_delta5':str(qmin[4]),
 'radius':str(r),'base_margin':str(delta0),'B':str(B),'box_margin':str(delta),'ratio':str(delta/S**2),
 'base_leaves':len(proof['leaves']),'box_leaf_counts':[len(v['leaves']) for v in proofs]})
