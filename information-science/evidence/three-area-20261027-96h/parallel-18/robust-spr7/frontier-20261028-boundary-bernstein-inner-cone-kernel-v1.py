# Exact LP over a FIXED Bernstein inner cone for the actual boundary box.
# Eval-only. A positive solution proves all-frequency positivity; failure of
# this inner template is NOT an original no-numerator certificate.
# Requires earlier exact simplex, pairing and Bernstein functions; imports no
# optimizer, author checker, native scientific process or floating arithmetic.
from fractions import Fraction as Q
from math import lcm

basis_polys=[]
for a in boundary_cs:
    pp=[]
    for k in range(8):
        unit=[Q(0)]*8;unit[k]=Q(1)
        pp.append(pairing_polynomial(a,unit))
    basis_polys.append(pp)
# Each leaf interval comes from a previous valid partition only; no earlier
# numerical positivity is assumed for this new box or numerator.
bern_rows=[];bern_metadata=[];seen_vectors=set()
for ci in range(4):
    for li,leaf in enumerate(hard_best['proofs'][ci]['leaves']):
        left,right=Q(leaf['left']),Q(leaf['right'])
        by_basis=[bernstein_interval(basis_polys[ci][k],left,right) for k in range(8)]
        for j in range(8):
            vec=tuple(by_basis[k][j] for k in range(8))
            if vec not in seen_vectors:
                seen_vectors.add(vec);bern_rows.append(vec)
                bern_metadata.append({'corner':ci,'left':str(left),'right':str(right),'bernstein_index':j})
seed_b=[Q(x) for x in unperturbed_rounds[-1]['numerator']]
selected={i for i,row in enumerate(bern_rows) if sum(row[k]*seed_b[k] for k in range(8))<=0}
selected.update(i for i,m in enumerate(bern_metadata) if (m['left']=='0' and m['bernstein_index']==0) or (m['right']=='1' and m['bernstein_index']==7))
if not selected:raise ValueError('EXPECTED_NONEMPTY_CUT_SET')
bern_inner_rounds=[]
for iteration in range(8):
    ids=sorted(selected)
    common=lcm(*(v.denominator for i in ids for v in bern_rows[i]))
    C=[[int(common*bern_rows[i][k]) for i in ids] for k in range(8)]
    sol=exact_minimax(C,pivot_cap=1800)
    rec={'iteration':iteration+1,'total_template_constraints':len(bern_rows),'selected_constraints':len(ids),
         'solver_status':sol['status'],'pivots':sol['pivots'],'common_scale':str(common)}
    if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';bern_inner_rounds.append(rec);break
    opt=sol['optimum'];rec['selected_margin']=str(opt/common)
    if opt<=0:
        rec['status']='FIXED_BERNSTEIN_TEMPLATE_NOT_STRICTLY_FEASIBLE_ON_SELECTED_ROWS'
        bern_inner_rounds.append(rec);break
    dual=sol['dual']
    if dual[7]<=0 or dual[0]<=0:raise ValueError('ENDPOINT_MARGIN')
    b=[x/dual[7] for x in dual]
    if any(x<0 for x in b):raise ValueError('NUMERATOR')
    vals=[sum(row[k]*b[k] for k in range(8)) for row in bern_rows]
    violated=[i for i,v in enumerate(vals) if v<=0]
    rec['numerator']=[str(x) for x in b];rec['violated_count']=len(violated)
    if not violated:
        if not all(x>0 for x in b):raise ValueError('HURWITZ_COEFFICIENT_CONTRADICTION')
        polys=[pairing_polynomial(a,b) for a in boundary_cs]
        proofs=[whole_halfline(p,max_depth=40,max_nodes=10000) for p in polys]
        if not all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in proofs):raise ValueError('INDEPENDENT_BERNSTEIN_REPLAY')
        for p,proof in zip(polys,proofs):verify_leaves_by_power(p,proof)
        rec.update({'status':'COMMON_NUMERATOR_PROVED','polynomials':[[str(x) for x in p] for p in polys],
                    'proofs':proofs,'margin':str(min(Q(x['margin']) for x in proofs))})
        bern_inner_rounds.append(rec);break
    new=set(violated)-selected
    if not new:raise ValueError('NO_NEW_TEMPLATE_CONSTRAINT')
    rec['status']='ADDED_ACTUAL_TEMPLATE_CONSTRAINTS';rec['added_count']=len(new)
    bern_inner_rounds.append(rec);selected.update(new)
else:bern_inner_rounds[-1]['terminal']='EIGHT_ROUND_LIMIT'
print('exact fixed Bernstein inner cone:',[{'iteration':r['iteration'],'selected':r['selected_constraints'],
 'total':r['total_template_constraints'],'pivots':r['pivots'],'status':r['status'],
 'violated':r.get('violated_count'),'added':r.get('added_count'),'terminal':r.get('terminal')} for r in bern_inner_rounds])
