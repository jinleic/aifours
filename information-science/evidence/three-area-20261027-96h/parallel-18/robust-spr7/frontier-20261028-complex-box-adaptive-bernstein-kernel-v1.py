# Exact adaptive Bernstein inner-cone search on a DIFFERENT actual box with
# center (s+1)prod_{v=2,4,8}((s+1)^2+v^2). Eval only. A failed inner template
# never becomes an original no-go unless its active dual rows are physical points.
from fractions import Fraction as Q
from math import lcm

cx_target=complex_results[1]
if cx_target['status']!='NO_STRICT_GRID_CERTIFICATE_OR_GLOBAL_WITNESS':raise ValueError('EXPECTED_TARGET')
cx_center=[Q(x) for x in cx_target['center']];cx_r=Q(cx_target['stable_halfwidth_ratio'])
cx_lo=[Q(x) for x in cx_target['lower']];cx_hi=[Q(x) for x in cx_target['upper']];cx_cs=corners(cx_lo,cx_hi)
if not all(routh_ok(a) and integer_hurwitz(a) for a in cx_cs):raise ValueError('TARGET_STABILITY')
small_template=None;cx_small_factor=None
for divisor in (16,64,256):
    sl,sh=centered_box(cx_center,cx_r/divisor);small_corners=corners(sl,sh)
    small_polys=[pairing_polynomial(a,cx_center) for a in small_corners]
    small_proofs=[whole_halfline(p,max_depth=36,max_nodes=5000) for p in small_polys]
    if all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in small_proofs):
        small_template=[[(Q(l['left']),Q(l['right'])) for l in p['leaves']] for p in small_proofs]
        cx_small_factor=divisor;break
if small_template is None:raise ValueError('NO_INITIAL_TEMPLATE')

cx_basis=[]
for a in cx_cs:
    pp=[]
    for k in range(8):
        unit=[Q(0)]*8;unit[k]=Q(1);pp.append(pairing_polynomial(a,unit))
    cx_basis.append(pp)
cx_seed=[Q(x) for x in cx_target['grid_dual_numerator']]
cx_cone_rounds=[];cx_stop=False
for refinement in range(3):
    vectors=[];meta=[];seen=set()
    for ci in range(4):
        for left,right in small_template[ci]:
            blocks=[bernstein_interval(cx_basis[ci][k],left,right) for k in range(8)]
            for j in range(8):
                vec=tuple(blocks[k][j] for k in range(8))
                if vec not in seen:seen.add(vec);vectors.append(vec);meta.append((ci,left,right,j))
    selected={i for i,v in enumerate(vectors) if sum(v[k]*cx_seed[k] for k in range(8))<=0}
    selected.update(i for i,(_,left,right,j) in enumerate(meta) if (left==0 and j==0) or (right==1 and j==7))
    if not selected:raise ValueError('EMPTY_SELECTION')
    for inner in range(5):
        ids=sorted(selected);common=lcm(*(z.denominator for i in ids for z in vectors[i]));C=[[int(common*vectors[i][k]) for i in ids] for k in range(8)]
        sol=exact_minimax(C,pivot_cap=2200)
        rec={'refinement':refinement,'inner':inner+1,'template_constraints':len(vectors),'selected_constraints':len(ids),
             'solver_status':sol['status'],'pivots':sol['pivots']}
        if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';cx_cone_rounds.append(rec);cx_stop=True;break
        opt=sol['optimum'];rec['selected_margin']=str(opt/common)
        if opt<=0:
            support=[(ids[i],weight) for i,weight in enumerate(sol['lambda']) if weight>0]
            internal=[(idx,w) for idx,w in support if meta[idx][3] not in (0,7)]
            rec['active_support']=[{'metadata':[meta[idx][0],str(meta[idx][1]),str(meta[idx][2]),meta[idx][3]],'weight':str(w)} for idx,w in support]
            if not internal:
                atoms=[]
                for idx,w in support:
                    ci,left,right,j=meta[idx];x=left if j==0 else right;t=x/(1-x) if x<1 else None
                    raw=w*common/(1+t)**7 if t is not None else w*common
                    atoms.append((ci,t,raw))
                scale=lcm(*(a[2].denominator for a in atoms));weights=[int(scale*a[2]) for a in atoms];sums=[]
                for k in range(8):
                    unit=[Q(0)]*8;unit[k]=Q(1)
                    val=sum(weights[i]*(independent_pair_t(cx_cs[a[0]],unit,a[1]) if a[1] is not None else unit[7]) for i,a in enumerate(atoms))
                    if val>0:raise ValueError('PHYSICAL_CERTIFICATE_REPLAY')
                    sums.append(str(val))
                rec.update({'status':'ORIGINAL_NONPOSITIVE_ATOM_CERTIFICATE','atoms':[{'corner':a[0],'t':str(a[1]) if a[1] is not None else 'infinity','weight':weights[i]} for i,a in enumerate(atoms)],'coefficient_sums':sums})
                cx_cone_rounds.append(rec);cx_stop=True;break
            split={(meta[idx][0],meta[idx][1],meta[idx][2]) for idx,w in internal}
            for ci,left,right in split:
                arr=small_template[ci]
                if (left,right) not in arr:raise ValueError('SPLIT_INTERVAL')
                at=arr.index((left,right));mid=(left+right)/2;arr[at:at+1]=[(left,mid),(mid,right)]
            rec['status']='REFINED_INNER_TEMPLATE_NOT_ORIGINAL_FAILURE';rec['split_count']=len(split);cx_cone_rounds.append(rec);break
        dual=sol['dual']
        if dual[7]<=0 or dual[0]<=0:raise ValueError('ENDPOINT')
        b=[v/dual[7] for v in dual];vals=[sum(v[k]*b[k] for k in range(8)) for v in vectors]
        violated=[i for i,v in enumerate(vals) if v<=0];rec['numerator']=[str(x) for x in b];rec['violated_count']=len(violated)
        if not violated:
            if not all(x>0 for x in b):raise ValueError('HURWITZ_COEFFICIENTS')
            ps=[pairing_polynomial(a,b) for a in cx_cs];proofs=[whole_halfline(p,max_depth=40,max_nodes=10000) for p in ps]
            if not all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in proofs):raise ValueError('INDEPENDENT_BERNSTEIN_REPLAY')
            for p,proof in zip(ps,proofs):verify_leaves_by_power(p,proof)
            rec.update({'status':'COMMON_NUMERATOR_PROVED','polynomials':[[str(x) for x in p] for p in ps],
                        'proofs':proofs,'margin':str(min(Q(x['margin']) for x in proofs))});cx_cone_rounds.append(rec);cx_stop=True;break
        add=set(violated)-selected
        if not add:raise ValueError('NO_NEW_ROWS')
        rec['status']='ADDED_TEMPLATE_CONSTRAINTS';rec['added_count']=len(add);cx_cone_rounds.append(rec);selected.update(add)
    else:cx_cone_rounds[-1]['terminal']='FIVE_INNER_LIMIT';cx_stop=True
    if cx_stop:break
else:cx_cone_rounds[-1]['terminal']='THREE_REFINEMENT_LIMIT'
print('complex-box adaptive Bernstein:',{'small_template_divisor':cx_small_factor,'rounds':[{'refinement':r['refinement'],'inner':r['inner'],
 'selected':r['selected_constraints'],'total':r['template_constraints'],'pivots':r['pivots'],'status':r['status'],
 'added':r.get('added_count'),'split':r.get('split_count'),'terminal':r.get('terminal')} for r in cx_cone_rounds]})
