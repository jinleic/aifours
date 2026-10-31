# Exact Bernstein inner cone with the rational boundary tangent imposed.
# Fractional rational x leaves; failure of a template is NOT an original no-go.
from fractions import Fraction as Q
from math import lcm

def divide_no_remainder(poly,r):
 out=[Q(0)]*(len(poly)-1);out[-1]=poly[-1]
 for j in range(len(out)-2,-1,-1):out[j]=poly[j+1]+r*out[j+1]
 return out
endpoints=[Q(0)]+[Q(1)-Q(1,2**i) for i in range(1,8)]+[Q(1)]
parts=[[(endpoints[j],endpoints[j+1]) for j in range(len(endpoints)-1)] for _ in range(5)]
matrices=[]
for ci,a in enumerate(outercs+[bn]):
 arr=[]
 for k in range(8):
  unit=[Q(0)]*8;unit[k]=Q(1);p=pairing_polynomial(a,unit)
  if ci==2:p=divide_no_remainder(divide_no_remainder(p,contact),contact)
  arr.append(p)
 matrices.append(arr)
seed=[Q(v) for v in joint_cone[-1]['numerator']];bcone=[];done=False
for ref in range(4):
 vectors=[];meta=[];seen=set()
 for ci in range(5):
  for left,right in parts[ci]:
   blocks=[beta(matrices[ci][k],left,right) for k in range(8)]
   for j in range(len(blocks[0])):
    vec=tuple(blocks[k][j] for k in range(8))
    if vec not in seen:seen.add(vec);vectors.append(vec);meta.append((ci,left,right,j,len(blocks[0])-1))
 selected={i for i,v in enumerate(vectors) if sum(v[k]*seed[k] for k in range(8))<=0}
 selected.update(i for i,(ci,l,r,j,n) in enumerate(meta) if (l==0 and j==0) or (r==1 and j==n))
 for inner in range(5):
  ids=sorted(selected);eps=Q(1,10**14)
  rows=[[v-eps for v in vectors[i]] for i in ids]
  rows += [[Q(int(k==j))-eps for k in range(8)] for j in range(8)]
  rows += [[sign*v for v in tangent] for sign in (-1,1)]
  scale=lcm(*(v.denominator for row in rows for v in row));C=[[int(scale*row[k]) for row in rows] for k in range(8)]
  sol=exact_minimax(C,pivot_cap=2800);rec={'refinement':ref,'inner':inner+1,'selected':len(ids),'total':len(vectors),'pivots':sol['pivots'],'solver_status':sol['status']}
  if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';bcone.append(rec);done=True;break
  opt=sol['optimum']/scale;rec['margin']=str(opt)
  if opt<0:
   support=[ids[i] for i in range(len(ids)) if sol['lambda'][i]>0]
   split={(meta[i][0],meta[i][1],meta[i][2]) for i in support if meta[i][3] not in (0,meta[i][4])}
   if not split:rec['status']='INFEASIBLE_MARGIN_TEMPLATE';bcone.append(rec);done=True;break
   for ci,l,r in split:
    arr=parts[ci];j=arr.index((l,r));mid=(l+r)/2;arr[j:j+1]=[(l,mid),(mid,r)]
   rec.update({'status':'REFINED_TEMPLATE','split_count':len(split)});bcone.append(rec);break
  if opt!=0:raise ValueError('TANGENT_PAIR')
  dual=sol['dual']
  if any(v<eps for v in dual) or sum(tangent[k]*dual[k] for k in range(8))!=0:raise ValueError('DUAL')
  bad=[i for i,v in enumerate(vectors) if sum(v[k]*dual[k] for k in range(8))<eps]
  if not bad:
   polys=[];checks=[]
   for ci,a in enumerate(outercs):
    p=pairing_polynomial(a,dual);polys.append(p);r=p
    if ci==2:r=quotient_by_root(quotient_by_root(r,contact),contact)
    test=exact_nonnegative_halfline(r,maxdepth=46,maxnodes=24000);checks.append(test)
   cp=pairing_polynomial(bn,dual);cproof=whole_halfline(cp,max_depth=46,max_nodes=24000)
   if not all(v['status']=='NONNEGATIVE_PROVED' for v in checks) or cproof['status']!='STRICT_POSITIVITY':raise ValueError('REPLAY')
   verify_leaves_by_power(cp,cproof)
   rec.update({'status':'ALL_MARKER_REGION_COMMON_NUMERATOR','numerator':[str(v) for v in dual],
    'boundary_polynomials':[[str(x) for x in p] for p in polys],'boundary_checks':checks,'center_proof':cproof});bcone.append(rec);done=True;break
  add=set(bad)-selected
  if not add:raise ValueError('NO_NEW')
  rec.update({'status':'ADDED_COEFFICIENTS','added':len(add)});bcone.append(rec);selected.update(add)
 else:bcone[-1]['terminal']='FIVE_INNER_LIMIT';done=True
 if done:break
else:bcone[-1]['terminal']='FOUR_REFINEMENT_LIMIT'
print('joint boundary Bernstein cone:',[{'refinement':r['refinement'],'inner':r['inner'],'selected':r['selected'],'total':r['total'],
 'pivots':r['pivots'],'status':r['status'],'added':r.get('added'),'split':r.get('split_count'),'terminal':r.get('terminal')} for r in bcone])
