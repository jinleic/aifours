# Exact QF_LRA minimization for a smaller monic numerator on the already
# proven boundary Bernstein leaves. Tangent and every leaf are hard constraints.
from fractions import Fraction as Q
import z3
if jround[-1]['status']!='ALL_MARKER_REGION_COMMON_NUMERATOR':raise ValueError('NO_SEED')
parts=[[(Q(x['left']),Q(x['right'])) for x in pr['leaves']] for pr in jround[-1]['boundary_checks']]+[[(Q(x['left']),Q(x['right'])) for x in jround[-1]['center_proof']['leaves']]]
constraints=[]
for ci in range(5):
 for left,right in parts[ci]:
  vals=[beta(matrices[ci][k],left,right) for k in range(8)]
  for j in range(len(vals[0])):constraints.append([vals[k][j] for k in range(8)])
BV=[z3.Real('jointcompact_b%d'%j) for j in range(8)];M=z3.Optimize();M.set(timeout=15000)
eps=Q(1,10**8)
M.add(BV[7]==1)
for v in BV:M.add(v>=zval(eps))
M.add(sum(zval(tangent[k])*BV[k] for k in range(8))==0)
for row in constraints:M.add(sum(zval(row[k])*BV[k] for k in range(8))>=zval(eps))
M.minimize(sum(BV));status=M.check();compact={'solver_status':str(status),'constraints':len(constraints),'epsilon':str(eps)}
if status==z3.sat:
 model=M.model();b=[frac(model.eval(v,model_completion=True)) for v in BV]
 if b[-1]!=1 or not all(v>0 for v in b) or sum(tangent[k]*b[k] for k in range(8))!=0:raise ValueError('MODEL')
 if not all(sum(row[k]*b[k] for k in range(8))>=eps for row in constraints):raise ValueError('LEAF_MODEL')
 ps=[];res=[];proofs=[]
 for ci,a in enumerate(outercs):
  p=pairing_polynomial(a,b);rr=p
  if ci==2:rr=quotient_by_root(quotient_by_root(rr,contact),contact)
  ps.append(p);res.append(rr);proofs.append(exact_nonnegative_halfline(rr,maxdepth=46,maxnodes=24000))
 cp=pairing_polynomial(bn,b);cproof=whole_halfline(cp,max_depth=46,max_nodes=24000)
 if not all(v['status']=='NONNEGATIVE_PROVED' for v in proofs) or cproof['status']!='STRICT_POSITIVITY':raise ValueError('REPLAY')
 verify_leaves_by_power(cp,cproof)
 compact.update({'status':'ALL_MARKER_REGION_COMMON_NUMERATOR','numerator':[str(v) for v in b],
  'boundary_polynomials':[[str(x) for x in p] for p in ps],'boundary_residuals':[[str(x) for x in p] for p in res],
  'boundary_checks':proofs,'center_polynomial':[str(x) for x in cp],'center_proof':cproof,'center_margin':str(Q(cproof['margin']))})
else:compact['status']='INCONCLUSIVE_'+str(status)
print('compact joint marker-region numerator:',{'status':compact['status'],'constraints':compact['constraints'],'numerator':compact.get('numerator'),
 'boundary_leaves':[len(v['leaves']) for v in compact.get('boundary_checks',[])],'center_margin':compact.get('center_margin')})
