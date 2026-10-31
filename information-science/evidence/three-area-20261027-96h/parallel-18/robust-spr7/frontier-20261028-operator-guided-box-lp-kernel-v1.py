# Exact linear box search using a mixed-operator primal support. The box is
# constrained by five disjoint parity-root markers and checked independently.
from fractions import Fraction as Q
import z3
support=[]
for i,w in enumerate(sol['lambda']):
 if w>0:
  k,h,ci,t,_=atoms[i]
  if t>0:support.append((k,h,ci,t,w/(1+t)**(7-k)))
if len(support)<3:raise ValueError('SUPPORT')
seedlo=ahlo[:];seedhi=ahhi[:]
def symbolic_corner(lo,hi,ci):
 out=[];es=ci//2;oside=ci%2
 for j in range(7):
  side=es if j%2==0 else oside
  out.append(lo[j] if ((j//2)%2==0)==(side==0) else hi[j])
 return out+[zval(1)]
def symbolic_op_vector(a,k,h,t):
 q=[zval(Q(ff(j,k),ff(7,k)))*a[j] for j in range(k,8)]
 for j in range(k+1,8):q[j-k-1]+=zval(h*Q(ff(j,k+1),ff(7,k)))*a[j]
 E=sum(q[j]*zval((-t)**(j//2)) for j in range(0,len(q),2));O=sum(q[j]*zval((-t)**((j-1)//2)) for j in range(1,len(q),2));out=[]
 def term(power):return zval((-t)**(power//2))*E if power%2==0 else zval(t*(-t)**((power-1)//2))*O
 for j in range(8):
  if j<k:out.append(zval(0));continue
  v=zval(Q(ff(j,k),ff(7,k)))*term(j-k)
  if j>k:v+=zval(h*Q(ff(j,k+1),ff(7,k)))*term(j-k-1)
  out.append(v)
 return out
L=[z3.Real('og_l%d'%j) for j in range(7)];U=[z3.Real('og_u%d'%j) for j in range(7)];B=z3.Real('og_bound');S=z3.Optimize();S.set(timeout=15000)
for j in range(7):S.add(L[j]>=zval(seedlo[j]/10),U[j]-L[j]>=zval(Q(1,10**8)),U[j]<=zval(seedhi[j]*2))
for t,req in zip(ahmarks,ahreq):
 for idx,sgn in req:S.add(sgn*oe(L,U,zval(t))[idx]>=zval(Q(1,10**12)))
for j in range(8):S.add(sum(zval(w)*symbolic_op_vector(symbolic_corner(L,U,ci),k,h,t)[j] for k,h,ci,t,w in support)<=B)
S.minimize(B);status=S.check();op_box_result={'solver_status':str(status),'support':[{'order':k,'h':str(h),'corner':ci,'t':str(t),'weight':str(w)} for k,h,ci,t,w in support]}
if status==z3.sat:
 model=S.model();lo=[frac(model.eval(x,model_completion=True)) for x in L];hi=[frac(model.eval(x,model_completion=True)) for x in U]
 if not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('BOX')
 if not all(sgn*oe(lo,hi,t)[idx]>0 for t,req in zip(ahmarks,ahreq) for idx,sgn in req):raise ValueError('MARKERS')
 if not all(routh_ok(a) and integer_hurwitz(a) for a in local_corners(lo,hi)):raise ValueError('STABILITY')
 cs=local_corners(lo,hi);F=[sum(w*op_vector(cs[ci],k,h,t)[j] for k,h,ci,t,w in support) for j in range(8)]
 op_box_result.update({'status':'OPERATOR_CERTIFICATE' if max(F)<=0 else 'NO_CERTIFICATE_FIXED_WEIGHTS','lower':[str(x) for x in lo],
  'upper':[str(x) for x in hi],'coefficient_sums':[str(v) for v in F],'bound':str(max(F))})
else:op_box_result['status']='INCONCLUSIVE_'+str(status)
print('operator-guided exact box optimization:',{'status':op_box_result['status'],'solver_status':str(status),'support_size':len(support),'bound':op_box_result.get('bound')})
