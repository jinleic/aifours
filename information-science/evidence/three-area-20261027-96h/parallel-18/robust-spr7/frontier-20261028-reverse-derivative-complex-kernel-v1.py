# Bounded exact reverse-derivative test around stable complex-root centers.
# Candidate septic pairings are accepted only by full exact Bernstein replay.
from fractions import Fraction as Q
from random import Random
R=Random(20261031);reverse_complex={'proposals':0,'derivative_failures':0,'accepted':[]}
for ws in ((1,2,4),(2,4,8),(4,5,6),(3,7,11)):
 p=[Q(1),Q(1)]
 for w in ws:p=conv_exact(p,[Q(1+w*w),Q(2),Q(1)])
 q=[Q(j+1,7)*p[j+1] for j in range(7)]
 grid={Q(0),Q(1,10),Q(1,2),Q(1),Q(2),Q(5),Q(10),Q(20),Q(50),Q(100)}
 for w in ws:grid.update((Q(w*w,2),Q(w*w),Q(2*w*w)))
 for trial in range(512):
  b=[p[j]*Q(R.randrange(80,121),100) for j in range(7)]+[Q(1)];reverse_complex['proposals']+=1
  dc=[Q(j+1,7)*b[j+1] for j in range(7)];H=pv(q,dc)
  fail=next(((t,ev(H,t)) for t in sorted(grid) if ev(H,t)<=0),None)
  if not fail:continue
  reverse_complex['derivative_failures']+=1;P=pv(p,b);proof=whole_halfline(P,max_depth=40,max_nodes=16000)
  if proof['status']!='STRICT_POSITIVITY' or 'leaves' not in proof:continue
  verify_leaves_by_power(P,proof)
  reverse_complex['accepted'].append({'status':'SEPTIC_SPR_BUT_DERIVATIVE_NOT_SPR','frequencies':ws,'trial':trial+1,
   'p':[str(x) for x in p],'b':[str(x) for x in b],'septic_pairing_polynomial':[str(x) for x in P],
   'septic_proof':proof,'derivative_denominator':[str(x) for x in q],'derivative_numerator':[str(x) for x in dc],
   'derivative_pairing_polynomial':[str(x) for x in H],'failing_t':str(fail[0]),'failing_pairing':str(fail[1])});break
 if reverse_complex['accepted']:break
print('complex reverse-derivative exact stress:',{'proposals':reverse_complex['proposals'],'derivative_failures':reverse_complex['derivative_failures'],
 'result':reverse_complex['accepted'][0] if reverse_complex['accepted'] else None})
