# Continue the selected actual rational box with common compactified column
# normalization. Exact Fraction simplex in Eval only; no native solver.
# Requires the previously loaded adaptive and exact Bernstein/replay kernels.
normalized_rounds=[]
normalized_tgrid=list(tgrid)
for iteration in range(4):
    atoms=[]
    for ci,a in enumerate(cs):
        for t in normalized_tgrid:
            direct,local=pair_vector_t(a,t)
            vals=[Q(v,local)/(1+t)**7 for v in direct]
            atoms.append((ci,t,vals))
    common_scale=lcm(*(v.denominator for atom in atoms for v in atom[2]))
    C=[[int(common_scale*atom[2][k]) for atom in atoms] for k in range(8)]
    sol=exact_minimax(C,pivot_cap=1000)
    rec={'iteration':iteration+1,'nodes':[str(t) for t in normalized_tgrid],
         'atom_count':len(atoms),'common_scale':str(common_scale),'solver_status':sol['status'],'pivots':sol['pivots']}
    if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';normalized_rounds.append(rec);break
    opt=sol['optimum'];rec['normalized_grid_margin']=str(opt/common_scale)
    if opt<0:
        raw=[sol['lambda'][i]*Q(common_scale,1)/(1+atom[1])**7 for i,atom in enumerate(atoms)]
        weight_scale=lcm(*(v.denominator for v in raw));weights=[int(weight_scale*v) for v in raw]
        sums=[]
        for k in range(8):
            e=[Q(0)]*8;e[k]=Q(1)
            value=sum(weights[i]*independent_pair_t(cs[atom[0]],e,atom[1]) for i,atom in enumerate(atoms))
            if value>=0:raise ValueError('STRICT_CERTIFICATE_REPLAY')
            sums.append(str(value))
        rec.update({'status':'STRICT_ACTUAL_BOX_CERTIFICATE','raw_weights':weights,'strict_sums':sums})
        normalized_rounds.append(rec);break
    if opt==0:rec['status']='ZERO_GRID_MARGIN_UNRESOLVED';normalized_rounds.append(rec);break
    dual=sol['dual'];M=max(sum(abs(C[k][i]) for k in range(8)) for i in range(len(atoms)))
    eps=opt/(2*M)
    candidate=[v+eps for v in dual];candidate=[v/candidate[7] for v in candidate]
    if not all(x>0 for x in candidate):raise ValueError('POSITIVE_COEFFICIENTS')
    for i,(ci,t,vals) in enumerate(atoms):
        raw=independent_pair_t(cs[ci],candidate,t)
        if raw<=0 or sum(candidate[k]*C[k][i] for k in range(8))!=common_scale*raw/(1+t)**7:
            raise ValueError('GRID_DUAL_REPLAY')
    rec['numerator']=[str(x) for x in candidate];proofs=[];failure=None
    for ci,a in enumerate(cs):
        p=pairing_polynomial(a,candidate);cert=whole_halfline(p,max_depth=32,max_nodes=4000)
        if cert['status']=='SUBDIVISION_CAP':cert=locate_strict_failure(p,max_depth=64,max_nodes=10000)
        proofs.append({'corner':ci,'polynomial':[str(x) for x in p],'certificate':cert})
        if cert['status']=='NONPOSITIVE_EXACT' and failure is None:failure=Q(cert['t'])
    rec['proofs']=proofs
    if all(x['certificate']['status']=='STRICT_POSITIVITY' and 'leaves' in x['certificate'] for x in proofs):
        for x in proofs:verify_leaves_by_power([Q(a) for a in x['polynomial']],x['certificate'])
        rec['status']='COMMON_NUMERATOR_PROVED';normalized_rounds.append(rec);break
    if failure is None:rec['status']='BERNSTEIN_CAP_UNRESOLVED';normalized_rounds.append(rec);break
    if failure in normalized_tgrid:raise ValueError('REPEATED_EXACT_FAILURE')
    rec['status']='EXACT_UNSEEN_FREQUENCY_REFINEMENT';rec['new_t']=str(failure)
    normalized_rounds.append(rec);normalized_tgrid=sorted(normalized_tgrid+[failure])
else:
    normalized_rounds[-1]['terminal']='FOUR_ROUND_LIMIT'
print('normalized exact exchange:',[{'iteration':x['iteration'],'atoms':x['atom_count'],'pivots':x['pivots'],
 'status':x['status'],'normalized_grid_margin':x.get('normalized_grid_margin'),'new_t':x.get('new_t'),'terminal':x.get('terminal')} for x in normalized_rounds])
