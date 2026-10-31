# Adaptive exact Bernstein inner-cone search for the same actual boundary box.
# A negative inner dual is NOT an original obstruction unless every active
# Bernstein coefficient is an actual interval endpoint (physical frequency).
# Eval-only; no optimizer or author checker imports.
from fractions import Fraction as Q
from math import lcm

template_intervals=[[(Q(l['left']),Q(l['right'])) for l in hard_best['proofs'][ci]['leaves']] for ci in range(4)]
template_seed=[Q(x) for x in unperturbed_rounds[-1]['numerator']]
adaptive_bern=[]
stop=False
for refinement in range(3):
    vectors=[];meta=[];seen=set()
    for ci in range(4):
        for left,right in template_intervals[ci]:
            blocks=[bernstein_interval(basis_polys[ci][k],left,right) for k in range(8)]
            for j in range(8):
                vec=tuple(blocks[k][j] for k in range(8))
                if vec not in seen:
                    seen.add(vec);vectors.append(vec);meta.append((ci,left,right,j))
    selected={i for i,v in enumerate(vectors) if sum(v[k]*template_seed[k] for k in range(8))<=0}
    selected.update(i for i,(_,left,right,j) in enumerate(meta) if (left==0 and j==0) or (right==1 and j==7))
    if not selected:raise ValueError('EMPTY_SELECTED')
    for inner in range(5):
        ids=sorted(selected);common=lcm(*(z.denominator for i in ids for z in vectors[i]))
        C=[[int(common*vectors[i][k]) for i in ids] for k in range(8)]
        result=exact_minimax(C,pivot_cap=2200)
        rec={'refinement':refinement,'inner':inner+1,'total_template_constraints':len(vectors),
             'selected_constraints':len(ids),'solver_status':result['status'],'pivots':result['pivots']}
        if result['status']!='CERTIFIED_OPTIMUM':
            rec['status']='PIVOT_CAP';adaptive_bern.append(rec);stop=True;break
        opt=result['optimum'];rec['selected_margin']=str(opt/common)
        if opt<=0:
            support=[(ids[i],weight) for i,weight in enumerate(result['lambda']) if weight>0]
            internal=[(idx,weight) for idx,weight in support if meta[idx][3] not in (0,7)]
            rec['active_support']=[{'metadata':[meta[idx][0],str(meta[idx][1]),str(meta[idx][2]),meta[idx][3]],'weight':str(w)} for idx,w in support]
            if not internal:
                raw_atoms=[]
                for idx,w in support:
                    ci,left,right,j=meta[idx];x=left if j==0 else right
                    t=x/(1-x) if x<1 else None
                    raw=w*common/(1+t)**7 if t is not None else w*common
                    raw_atoms.append((ci,t,raw))
                scale=lcm(*(v.denominator for _,_,v in raw_atoms))
                ints=[int(scale*v) for _,_,v in raw_atoms];sums=[]
                for k in range(8):
                    unit=[Q(0)]*8;unit[k]=Q(1)
                    v=sum(ints[i]*(independent_pair_t(boundary_cs[a[0]],unit,a[1]) if a[1] is not None else unit[7]) for i,a in enumerate(raw_atoms))
                    if v>0:raise ValueError('PHYSICAL_CERTIFICATE_REPLAY')
                    sums.append(str(v))
                rec.update({'status':'ORIGINAL_NONPOSITIVE_ATOM_CERTIFICATE','atoms':[{'corner':a[0],'t':str(a[1]) if a[1] is not None else 'infinity','weight':ints[i]} for i,a in enumerate(raw_atoms)],'coefficient_sums':sums})
                adaptive_bern.append(rec);stop=True;break
            split={(meta[idx][0],meta[idx][1],meta[idx][2]) for idx,w in internal}
            for ci,left,right in split:
                arr=template_intervals[ci]
                if (left,right) not in arr:raise ValueError('SPLIT_INTERVAL')
                at=arr.index((left,right));mid=(left+right)/2
                arr[at:at+1]=[(left,mid),(mid,right)]
            rec['status']='REFINED_INNER_TEMPLATE_NOT_ORIGINAL_FAILURE';rec['split_count']=len(split)
            adaptive_bern.append(rec);break
        dual=result['dual']
        if dual[7]<=0 or dual[0]<=0:raise ValueError('ENDPOINT')
        b=[v/dual[7] for v in dual]
        values=[sum(v[k]*b[k] for k in range(8)) for v in vectors]
        violated=[i for i,v in enumerate(values) if v<=0]
        rec['numerator']=[str(x) for x in b];rec['violated_count']=len(violated)
        if not violated:
            if not all(x>0 for x in b):raise ValueError('HURWITZ_COEFFICIENTS')
            polys=[pairing_polynomial(a,b) for a in boundary_cs]
            proofs=[whole_halfline(p,max_depth=40,max_nodes=10000) for p in polys]
            if not all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in proofs):raise ValueError('INDEPENDENT_BERNSTEIN_REPLAY')
            for p,proof in zip(polys,proofs):verify_leaves_by_power(p,proof)
            rec.update({'status':'COMMON_NUMERATOR_PROVED','polynomials':[[str(x) for x in p] for p in polys],
                        'proofs':proofs,'margin':str(min(Q(x['margin']) for x in proofs))})
            adaptive_bern.append(rec);stop=True;break
        new=set(violated)-selected
        if not new:raise ValueError('NO_NEW_ROWS')
        rec['status']='ADDED_TEMPLATE_CONSTRAINTS';rec['added_count']=len(new)
        adaptive_bern.append(rec);selected.update(new)
    else:
        adaptive_bern[-1]['terminal']='FIVE_INNER_LIMIT';stop=True
    if stop:break
else:
    adaptive_bern[-1]['terminal']='THREE_REFINEMENT_LIMIT'
print('adaptive exact Bernstein:',[{'refinement':r['refinement'],'inner':r['inner'],'selected':r['selected_constraints'],
 'total':r['total_template_constraints'],'pivots':r['pivots'],'status':r['status'],
 'added':r.get('added_count'),'split':r.get('split_count'),'terminal':r.get('terminal')} for r in adaptive_bern])
