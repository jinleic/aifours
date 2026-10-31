# Simplify the two-radius boundary witness while preserving its exact tangent.
from fractions import Fraction as Q
if bcone[-1]['status']!='ALL_MARKER_REGION_COMMON_NUMERATOR':raise ValueError('NO_SOURCE')
raw=[Q(x) for x in bcone[-1]['numerator']];base=[v/raw[-1] for v in raw]
if not tangent[1]:raise ValueError('SINGULAR')
jround=[]
for den in (1,10,100,1000,10000,100000,1000000,10000000):
 b=[Q(0)]*8;b[0]=base[0];b[7]=Q(1)
 for j in (2,3,4,5,6):b[j]=nearest(base[j],den)
 b[1]=-sum(tangent[k]*b[k] for k in range(8) if k!=1)/tangent[1]
 rec={'denominator':den,'numerator':[str(x) for x in b]}
 if not all(v>0 for v in b):rec['status']='NONPOSITIVE';jround.append(rec);continue
 if sum(tangent[k]*b[k] for k in range(8))!=0:raise ValueError('TANGENCY')
 checks=[];polys=[];residuals=[]
 for ci,a in enumerate(outercs):
  p=pairing_polynomial(a,b);polys.append(p);res=p
  if ci==2:res=quotient_by_root(quotient_by_root(res,contact),contact)
  residuals.append(res);checks.append(exact_nonnegative_halfline(res,maxdepth=46,maxnodes=24000))
 rec['boundary_checks']=checks
 if not all(v['status']=='NONNEGATIVE_PROVED' for v in checks):rec['status']='BOUNDARY_NOT_CERTIFIED';jround.append(rec);continue
 cp=pairing_polynomial(bn,b);proof=whole_halfline(cp,max_depth=46,max_nodes=24000)
 if proof['status']!='STRICT_POSITIVITY' or 'leaves' not in proof:rec['status']='CENTER_NOT_CERTIFIED';jround.append(rec);continue
 verify_leaves_by_power(cp,proof)
 rec.update({'status':'ALL_MARKER_REGION_COMMON_NUMERATOR','boundary_polynomials':[[str(v) for v in p] for p in polys],
   'boundary_residuals':[[str(v) for v in p] for p in residuals],'center_polynomial':[str(v) for v in cp],
   'center_proof':proof,'center_margin':str(Q(proof['margin']))});jround.append(rec);break
print('joint marker-region numerator rounding:',[{'denominator':r['denominator'],'status':r['status'],'numerator':r['numerator'],
 'boundary_status':[v['status'] for v in r.get('boundary_checks',[])],'center_margin':r.get('center_margin')} for r in jround])
