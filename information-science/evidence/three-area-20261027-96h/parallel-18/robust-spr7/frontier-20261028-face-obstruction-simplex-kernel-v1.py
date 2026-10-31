# Probe a target coordinate over lambda>=0,sum(lambda)=1,F=C*lambda<=0.
# A synthetic zero column starts a feasible exact simplex. Only a replayed
# negative coordinate is reported as an obstruction; no dual is claimed.
from fractions import Fraction as Q

def face_probe(C,target,pivot_cap=2500):
    d=len(C);n=len(C[0])
    if d!=8 or any(len(row)!=n for row in C):raise ValueError('MATRIX')
    C=[[0]+row for row in C];n+=1
    nonbasic=list(range(1,n));slack=lambda k:n+k
    rows={0:(Q(1),{i:Q(-1) for i in range(1,n)})}
    for k in range(d):rows[slack(k)]=(Q(0),{i:Q(-C[k][i]) for i in range(1,n) if C[k][i]})
    objective_const=Q(0);objective={i:Q(-C[target][i]) for i in range(1,n) if C[target][i]};pivots=0
    while True:
        candidates=[j for j in nonbasic if objective.get(j,0)>0]
        if not candidates:break
        if pivots>=pivot_cap:return {'status':'PIVOT_CAP','pivots':pivots}
        enter=min(candidates);leavers=[(v/(-co.get(enter,0)),key) for key,(v,co) in rows.items() if co.get(enter,0)<0]
        if not leavers:raise ValueError('UNBOUNDED')
        _,leave=min(leavers);val,co=rows.pop(leave);a=co[enter];nv=-val/a;nc={leave:Q(1)/a}
        for j,v in co.items():
            if j!=enter and v:nc[j]=-v/a
        for base in list(rows):
            v,bc=rows[base];bc=dict(bc);factor=bc.pop(enter,Q(0));v+=factor*nv
            if factor:
                for j,w in nc.items():bc[j]=bc.get(j,Q(0))+factor*w
            rows[base]=(v,{j:w for j,w in bc.items() if w})
        factor=objective.pop(enter,Q(0));objective_const+=factor*nv
        if factor:
            for j,w in nc.items():objective[j]=objective.get(j,Q(0))+factor*w
        objective={j:w for j,w in objective.items() if w};rows[enter]=(nv,{j:w for j,w in nc.items() if w})
        nonbasic.remove(enter);nonbasic.append(leave)
        if any(v<0 for v,co in rows.values()):raise ValueError('FEASIBILITY')
        pivots+=1
    weights=[rows.get(i,(Q(0),{}))[0] for i in range(n)]
    F=[sum(Q(C[k][i])*weights[i] for i in range(n)) for k in range(d)]
    if sum(weights)!=1 or any(v<0 for v in weights) or any(v>0 for v in F) or objective_const!=-F[target]:raise ValueError('REPLAY')
    return {'status':'NEGATIVE_FACE_WITNESS' if F[target]<0 else 'NO_NEGATIVE_WITNESS_FOUND',
            'pivots':pivots,'weights':weights[1:],'synthetic_zero_weight':weights[0],'vector':F}

face7=face_probe(C,7,pivot_cap=3000)
print('exact near-four face probe:',{'status':face7['status'],'pivots':face7['pivots'],
 'vector_signs':[0 if x==0 else -1 if x<0 else 1 for x in face7.get('vector',[])],
 'synthetic_zero_weight':str(face7.get('synthetic_zero_weight'))})
