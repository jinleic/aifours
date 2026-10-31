# Bounded exact exchange on the same r=679/640 actual Hurwitz box, replacing
# the perturbed dual by the EXACT finite-grid max-margin dual. All failed corner
# frequencies are added in a batch. Eval only; no native solver or floats.
search_nodes=sorted(set(line_nodes+[Q(0),Q(451,61),Q(53,203)]))
unperturbed_rounds=[]
for iteration in range(3):
    atoms=[]
    for ci,a in enumerate(boundary_cs):
        for t in search_nodes:
            direct,local=pair_vector_t(a,t);atoms.append((ci,t,[Q(v,local)/(1+t)**7 for v in direct]))
    atoms.append((None,None,[Q(0)]*7+[Q(1)]))
    common=lcm(*(v.denominator for atom in atoms for v in atom[2]))
    C=[[int(common*atom[2][k]) for atom in atoms] for k in range(8)]
    sol=exact_minimax(C,pivot_cap=1400)
    rec={'iteration':iteration+1,'nodes':[str(t) for t in search_nodes]+['infinity'],
         'atom_count':len(atoms),'common_scale':str(common),'solver_status':sol['status'],'pivots':sol['pivots']}
    if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';unperturbed_rounds.append(rec);break
    opt=sol['optimum'];rec['normalized_grid_margin']=str(opt/common)
    if opt<0:
        raw=[sol['lambda'][i]*Q(common)/(1+atom[1])**7 if atom[1] is not None else sol['lambda'][i]*common for i,atom in enumerate(atoms)]
        factor=lcm(*(v.denominator for v in raw));weights=[int(factor*v) for v in raw];sums=[]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1)
            val=sum(weights[i]*(independent_pair_t(boundary_cs[a[0]],unit,a[1]) if a[1] is not None else unit[7]) for i,a in enumerate(atoms))
            if val>=0:raise ValueError('STRICT_CERTIFICATE_REPLAY')
            sums.append(str(val))
        rec.update({'status':'STRICT_ACTUAL_BOX_CERTIFICATE','raw_weights':weights,'strict_sums':sums});unperturbed_rounds.append(rec);break
    if opt==0:rec['status']='ZERO_GRID_MARGIN_UNRESOLVED';unperturbed_rounds.append(rec);break
    dual=sol['dual']
    if dual[7]<=0 or dual[0]<=0:raise ValueError('ENDPOINT_POSITIVITY')
    candidate=[v/dual[7] for v in dual]
    if any(x<0 for x in candidate):raise ValueError('DUAL_COEFFICIENT_SIGN')
    for i,(ci,t,v) in enumerate(atoms):
        actual=independent_pair_t(boundary_cs[ci],candidate,t)/(1+t)**7 if t is not None else candidate[7]
        if actual<=0 or sum(candidate[k]*C[k][i] for k in range(8))!=common*actual:raise ValueError('GRID_DUAL_REPLAY')
    rec['numerator']=[str(x) for x in candidate];proofs=[];failures=[]
    for ci,a in enumerate(boundary_cs):
        p=pairing_polynomial(a,candidate);cert=whole_halfline(p,max_depth=32,max_nodes=4000)
        if cert['status']=='SUBDIVISION_CAP':cert=locate_strict_failure(p,max_depth=64,max_nodes=10000)
        proofs.append({'corner':ci,'polynomial':[str(x) for x in p],'certificate':cert})
        if cert['status']=='NONPOSITIVE_EXACT':failures.append(Q(cert['t']))
    rec['proofs']=proofs
    if all(x['certificate']['status']=='STRICT_POSITIVITY' and 'leaves' in x['certificate'] for x in proofs):
        for x in proofs:verify_leaves_by_power([Q(a) for a in x['polynomial']],x['certificate'])
        rec['status']='COMMON_NUMERATOR_PROVED';unperturbed_rounds.append(rec);break
    new=sorted(set(failures)-set(search_nodes))
    if not new:rec['status']='BERNSTEIN_CAP_OR_DUPLICATE_UNRESOLVED';unperturbed_rounds.append(rec);break
    rec['status']='BATCH_EXACT_FREQUENCY_REFINEMENT';rec['new_t']=[str(t) for t in new]
    unperturbed_rounds.append(rec);search_nodes=sorted(set(search_nodes+new))
else:unperturbed_rounds[-1]['terminal']='THREE_ROUND_LIMIT'
print('unperturbed boundary-box exchange:',[{'iteration':r['iteration'],'atoms':r['atom_count'],'pivots':r['pivots'],
 'status':r['status'],'new_t':r.get('new_t'),'terminal':r.get('terminal')} for r in unperturbed_rounds])
