# Bounded exact search for b/p SPR but b'/p' not SPR at some rational t.
# Deterministic integer random multipliers; exact Bernstein acceptance only.
from fractions import Fraction as Q
from math import comb
from random import Random
rr=Random(20261030);p=[Q(comb(7,j)) for j in range(8)];q=[Q(comb(6,j)) for j in range(7)]
grid=[Q(0),Q(1,100),Q(1,20),Q(1,10),Q(1,4),Q(1,2),Q(1),Q(2),Q(3),Q(4),Q(5),Q(10),Q(20),Q(50),Q(100)]
rev_random={'proposals':0,'derivative_failures':0,'accepted':[]}
for trial in range(512):
 b=[p[j]*Q(rr.randrange(2,31),10) for j in range(7)]+[Q(1)];rev_random['proposals']+=1
 dc=[Q(j+1,7)*b[j+1] for j in range(7)];H=pv(q,dc)
 fail=next(((t,ev(H,t)) for t in grid if ev(H,t)<=0),None)
 if not fail:continue
 rev_random['derivative_failures']+=1;P=pv(p,b);proof=whole_halfline(P,max_depth=36,max_nodes=10000)
 if proof['status']!='STRICT_POSITIVITY' or 'leaves' not in proof:continue
 verify_leaves_by_power(P,proof)
 rev_random['accepted'].append({'status':'SEPTIC_SPR_BUT_DERIVATIVE_NOT_SPR','trial':trial+1,'b':[str(v) for v in b],
  'septic_pairing_polynomial':[str(v) for v in P],'septic_proof':proof,'derivative_numerator':[str(v) for v in dc],
  'derivative_pairing_polynomial':[str(v) for v in H],'failing_t':str(fail[0]),'failing_pairing':str(fail[1])});break
print('asymmetric reverse-derivative stress:',{'proposals':rev_random['proposals'],'derivative_failures':rev_random['derivative_failures'],
 'accepted':rev_random['accepted'][0] if rev_random['accepted'] else None})
