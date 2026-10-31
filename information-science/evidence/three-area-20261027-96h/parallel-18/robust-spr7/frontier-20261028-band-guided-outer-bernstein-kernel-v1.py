# Exact inner-cone search for the asymmetrically weighted outer box.
# Failed templates are refined; only actual endpoint support is a no-go.
from fractions import Fraction as Q
from math import lcm
box=asym_results[0];gl=[Q(x) for x in box['lower']];gh=[Q(x) for x in box['upper']];gcs=local_corners(gl,gh)
nom=center_from_factors(box['real_root'],box['pairs']);template=None
for divider in (16,64,256):
 sl=[nom[j]+(gl[j]-nom[j])/divider for j in range(7)];sh=[nom[j]+(gh[j]-nom[j])/divider for j in range(7)]
 cps=[pairing_polynomial(a,nom) for a in local_corners(sl,sh)];pr=[whole_halfline(p,max_depth=36,max_nodes=5000) for p in cps]
 if all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in pr):
  template=[[(Q(z['left']),Q(z['right'])) for z in p['leaves']] for p in pr];base_divider=divider;break
if template is None:raise ValueError('NO_TEMPLATE')
basis=[]
for a in gcs:
 arr=[]
 for k in range(8):
  unit=[Q(0)]*8;unit[k]=Q(1);arr.append(pairing_polynomial(a,unit))
 basis.append(arr)
seed=[Q(v) for v in guided[-1]['dual_monic']];gcone=[];stop=False
for refinement in range(4):
 vectors=[];meta=[];seen=set()
 for ci in range(4):
  for left,right in template[ci]:
   blocks=[bernstein_interval(basis[ci][k],left,right) for k in range(8)]
   for j in range(8):
    v=tuple(blocks[k][j] for k in range(8))
    if v not in seen:seen.add(v);vectors.append(v);meta.append((ci,left,right,j))
 selected={i for i,v in enumerate(vectors) if sum(v[k]*seed[k] for k in range(8))<=0}
 selected.update(i for i,(ci,l,r,j) in enumerate(meta) if (l==0 and j==0) or (r==1 and j==7))
 if not selected:raise ValueError('EMPTY')
 for inner in range(5):
  ids=sorted(selected);scale=lcm(*(z.denominator for i in ids for z in vectors[i]));C=[[int(scale*vectors[i][k]) for i in ids] for k in range(8)]
  sol=exact_minimax(C,pivot_cap=2500);rec={'refinement':refinement,'inner':inner+1,'selected':len(ids),'total':len(vectors),'pivots':sol['pivots'],'solver_status':sol['status']}
  if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';gcone.append(rec);stop=True;break
  opt=sol['optimum']/scale;rec['margin']=str(opt)
  if opt<=0:
   support=[(ids[i],w) for i,w in enumerate(sol['lambda']) if w>0];internal=[(idx,w) for idx,w in support if meta[idx][3] not in (0,7)]
   if not internal:
    atoms=[]
    for idx,w in support:
     ci,left,right,j=meta[idx];x=left if j==0 else right;t=x/(1-x) if x<1 else None
     atoms.append((ci,t,w*scale/(1+t)**7 if t is not None else w*scale))
    den=lcm(*(w.denominator for ci,t,w in atoms));weights=[int(den*w) for ci,t,w in atoms];sums=[]
    for k in range(8):
     unit=[Q(0)]*8;unit[k]=Q(1);sums.append(sum(weights[i]*(independent_pair_t(gcs[ci],unit,t) if t is not None else unit[7]) for i,(ci,t,w) in enumerate(atoms)))
    if any(v>0 for v in sums):raise ValueError('PHYSICAL_CERT')
    rec.update({'status':'ACTUAL_NONPOSITIVE_ATOM_CERTIFICATE','support':[{'corner':ci,'t':str(t) if t is not None else 'infinity','weight':weights[i]} for i,(ci,t,w) in enumerate(atoms)],'coefficient_sums':[str(v) for v in sums]});gcone.append(rec);stop=True;break
   split={(meta[idx][0],meta[idx][1],meta[idx][2]) for idx,w in internal}
   for ci,l,r in split:
    arr=template[ci];j=arr.index((l,r));mid=(l+r)/2;arr[j:j+1]=[(l,mid),(mid,r)]
   rec.update({'status':'REFINED_INNER_TEMPLATE','split_count':len(split)});gcone.append(rec);break
  dual=sol['dual']
  if dual[0]<=0 or dual[7]<=0:raise ValueError('DUAL_ENDPOINT')
  b=[v/dual[7] for v in dual];bad=[i for i,v in enumerate(vectors) if sum(v[k]*b[k] for k in range(8))<=0]
  if not bad:
   ps=[pairing_polynomial(a,b) for a in gcs];proofs=[whole_halfline(p,max_depth=42,max_nodes=16000) for p in ps]
   if not all(v['status']=='STRICT_POSITIVITY' and 'leaves' in v for v in proofs):raise ValueError('PAIR_REPLAY')
   for p,pr in zip(ps,proofs):verify_leaves_by_power(p,pr)
   rec.update({'status':'COMMON_NUMERATOR_PROVED','numerator':[str(v) for v in b],'pairing_polynomials':[[str(v) for v in p] for p in ps],
       'proofs':proofs,'pairing_margin':str(min(Q(v['margin']) for v in proofs))});gcone.append(rec);stop=True;break
  new=set(bad)-selected
  if not new:raise ValueError('NO_NEW')
  rec.update({'status':'ADDED_CONSTRAINTS','added':len(new)});gcone.append(rec);selected.update(new)
 else:gcone[-1]['terminal']='FIVE_INNER_LIMIT';stop=True
 if stop:break
else:gcone[-1]['terminal']='FOUR_REFINEMENT_LIMIT'
print('band-guided outer-box Bernstein:',{'template_divider':base_divider,'rounds':[{'refinement':r['refinement'],'inner':r['inner'],
 'selected':r['selected'],'total':r['total'],'pivots':r['pivots'],'status':r['status'],'added':r.get('added'),
 'split':r.get('split_count'),'terminal':r.get('terminal')} for r in gcone]})
