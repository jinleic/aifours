#!/usr/bin/env python3
# Extra equality, endpoint and projective-boundary controls using the independent verifier.
from pathlib import Path
import hashlib, json
p=Path(__file__).with_name('independent-exact-check-v1.py')
source=p.read_text().split('r45=[',1)[0]
ns={}
exec(compile(source,str(p),'exec'),ns)
Q,F=ns['Q'],ns['F']; exact45=ns['exact45']; grid=ns['grid45']
psd,pt,state,rank2,vec=ns['psd'],ns['pt'],ns['state'],ns['rank2'],ns['vec']
w=(1,1,1,1,2,2,1,1,1)
overlap=exact45('own equality overlap',w,0,Q(F(1,2),F(1,2)),1,1,F(1,2))
assert overlap['cost1']=='1' and overlap['cost2']=='1'
assert overlap['gram1_psd'] and overlap['gram2_psd'] and overlap['mixed_psd']
Ucritical=exact45('own U=K2/phi',w,Q(F(1,2),F(1,2)),Q(1,1),1,1,1)
assert Ucritical['U']=='1/2' and Ucritical['gram1_psd'] and Ucritical['mixed_psd']
endpoint0=exact45('own p=0 endpoint',w,Q(F(1,2),F(1,2)),Q(1,1),1,1,0)
assert endpoint0['mixed_psd']==endpoint0['gram2_psd']
endpoint1=exact45('own p=1 endpoint',w,Q(F(1,2),F(1,2)),Q(1,1),1,1,1)
assert endpoint1['mixed_psd']==endpoint1['gram1_psd']

def project_boundary(g,kind):
    terms=[]
    for a,b,c in g:
        if kind=='complex':
            maps={0:[(0,Q(-1,-1))],1:[(1,Q(1))],2:[(0,Q(1))],3:[(2,Q(1))],4:[(3,Q(1))]}
        else: maps={0:[],1:[(0,Q(1))],2:[(1,Q(1))],3:[(2,Q(1))],4:[(3,Q(1))]}
        for j,x in maps[b]:terms.append((4*a+j,c*x))
    return vec(16,terms)
proj=[]
for kind,kernel in [('complex','|0>+(1+i)|2>'),('coordinate','|0>')]:
    vs=[project_boundary(g,kind) for g in grid]
    assert all(rank2(v,4,4) for v in vs)
    rho=state(vs,ns['W1']); result=psd(pt(rho,4,4)); assert result[0]
    proj.append({'kernel':kernel,'all_nine_generator_ranks_at_most_two':True,'output_pt':True,'pt_pivots':[str(x) for x in result[1]]})
receipt={'equality_weight_profile':w,'assumptions':'K2(1/epsilon+alpha/(phi*iota))=1, phi*eta=K2*epsilon, beta*delta=alpha^2',
         'overlap':overlap,'U_threshold':Ucritical,'p0':endpoint0,'p1':endpoint1,'projective_boundaries':proj}
output=Path(__file__).with_name('independent-boundary-receipt-v1.json')
with output.open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps({'path':str(output),'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'overlap_costs':[overlap['cost1'],overlap['cost2']],'overlap_gram_pivots':[overlap['gram1_pivots'],overlap['gram2_pivots']], 'U_threshold_cost':Ucritical['cost1'],'p0':endpoint0['mixed_psd'],'p1':endpoint1['mixed_psd'],'projective_boundaries':proj},indent=2))
