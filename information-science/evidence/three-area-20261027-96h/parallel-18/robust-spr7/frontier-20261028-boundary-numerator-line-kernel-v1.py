# Exact one-parameter numerator-line decision on the pinned boundary box.
# Eval-only rational arithmetic; four cuts maximum, no native program.
if not boundary_rounds or 'numerator' not in boundary_rounds[-1]:raise ValueError('NO_GRID_NUMERATOR')
line_a=boundary_old
line_b=[Q(x) for x in boundary_rounds[-1]['numerator']]
if line_a[7]!=1 or line_b[7]!=1:raise ValueError('NORMALIZATION')
line_nodes=sorted(set(boundary_tgrid+[Q(0)]))
line_rounds=[]
for iteration in range(4):
    low=Q(0);high=Q(1);low_source=None;high_source=None;impossible=None
    for ci,a in enumerate(boundary_cs):
        for t in line_nodes:
            A=independent_pair_t(a,line_a,t);D=independent_pair_t(a,line_b,t)-A
            if D>0:
                bound=-A/D
                if bound>low:low=bound;low_source={'corner':ci,'t':str(t),'A':str(A),'D':str(D),'bound':str(bound)}
            elif D<0:
                bound=-A/D
                if bound<high:high=bound;high_source={'corner':ci,'t':str(t),'A':str(A),'D':str(D),'bound':str(bound)}
            elif A<=0:
                impossible={'corner':ci,'t':str(t),'A':str(A),'D':'0'};break
        if impossible is not None:break
    rec={'iteration':iteration+1,'nodes':[str(x) for x in line_nodes],'lower':str(low),'upper':str(high),
         'lower_source':low_source,'upper_source':high_source,'constant_obstruction':impossible}
    if impossible is not None or low>=high:
        rec['status']='ENTIRE_LINE_EXCLUDED_BY_EXACT_FINITE_CONSTRAINTS';line_rounds.append(rec);break
    eta=(low+high)/2;candidate=[(1-eta)*x+eta*y for x,y in zip(line_a,line_b)]
    if candidate[7]!=1 or not all(x>0 for x in candidate):raise ValueError('LINE_NUMERATOR')
    if any(independent_pair_t(a,candidate,t)<=0 for a in boundary_cs for t in line_nodes):raise ValueError('LINE_INTERVAL')
    rec['eta']=str(eta);rec['numerator']=[str(x) for x in candidate];proofs=[];failure=None
    for ci,a in enumerate(boundary_cs):
        p=pairing_polynomial(a,candidate);cert=whole_halfline(p,max_depth=32,max_nodes=4000)
        if cert['status']=='SUBDIVISION_CAP':cert=locate_strict_failure(p,max_depth=64,max_nodes=10000)
        proofs.append({'corner':ci,'polynomial':[str(x) for x in p],'certificate':cert})
        if cert['status']=='NONPOSITIVE_EXACT' and failure is None:failure=Q(cert['t'])
    rec['proofs']=proofs
    if all(x['certificate']['status']=='STRICT_POSITIVITY' and 'leaves' in x['certificate'] for x in proofs):
        for x in proofs:verify_leaves_by_power([Q(a) for a in x['polynomial']],x['certificate'])
        rec['status']='COMMON_NUMERATOR_PROVED';line_rounds.append(rec);break
    if failure is None:rec['status']='BERNSTEIN_CAP_UNRESOLVED';line_rounds.append(rec);break
    if failure in line_nodes:raise ValueError('REPEATED_EXACT_FAILURE')
    rec['status']='EXACT_UNSEEN_FREQUENCY_REFINEMENT';rec['new_t']=str(failure)
    line_rounds.append(rec);line_nodes=sorted(line_nodes+[failure])
else:line_rounds[-1]['terminal']='FOUR_LINE_CUT_LIMIT'
print('exact boundary numerator line:',[{'iteration':r['iteration'],'status':r['status'],'lower':r['lower'],'upper':r['upper'],
 'eta':r.get('eta'),'new_t':r.get('new_t'),'terminal':r.get('terminal')} for r in line_rounds])
