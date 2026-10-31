# Exact bounded test of the converse derivative implication for one stable p.
# Search b/p SPR but (b'/7)/(p'/7) non-SPR at a rational frequency.
from fractions import Fraction as Q
from math import comb
p=[Q(comb(7,j)) for j in range(8)];q=[Q(comb(6,j)) for j in range(7)]
grid=[Q(0),Q(1,100),Q(1,20),Q(1,10),Q(1,4),Q(1,2),Q(1),Q(2),Q(3),Q(4),Q(5),Q(10),Q(20),Q(50),Q(100)]
reverse_stress=[];attempts=0
for k in range(1,7):
 for dv in (Q(-20),Q(-10),Q(-5),Q(-2),Q(-1),Q(-1,2),Q(1,2),Q(1),Q(2),Q(5),Q(10),Q(20),Q(50)):
  b=p[:];b[k]+=dv;attempts+=1
  if not all(v>0 for v in b):continue
  P=pv(p,b);proof=whole_halfline(P,max_depth=40,max_nodes=16000)
  if proof['status']!='STRICT_POSITIVITY' or 'leaves' not in proof:continue
  verify_leaves_by_power(P,proof)
  dc=[Q(j+1,7)*b[j+1] for j in range(7)];H=pv(q,dc)
  fail=next(((t,ev(H,t)) for t in grid if ev(H,t)<=0),None)
  if fail:
   reverse_stress.append({'status':'SEPTIC_SPR_BUT_DERIVATIVE_NOT_SPR','power':k,'delta':str(dv),'p':[str(x) for x in p],
    'b':[str(x) for x in b],'septic_pairing_polynomial':[str(x) for x in P],'septic_proof':proof,
    'derivative_numerator':[str(x) for x in dc],'derivative_pairing_polynomial':[str(x) for x in H],
    'failing_t':str(fail[0]),'failing_pairing':str(fail[1])});break
 else:continue
 break
print('reverse derivative bounded stress:',{'attempts':attempts,'status':reverse_stress[0]['status'] if reverse_stress else 'NO_REVERSE_OBSTRUCTION_FOUND',
 'power':reverse_stress[0]['power'] if reverse_stress else None,'delta':reverse_stress[0]['delta'] if reverse_stress else None,
 't':reverse_stress[0]['failing_t'] if reverse_stress else None,'pairing':reverse_stress[0]['failing_pairing'] if reverse_stress else None})
