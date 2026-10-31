# Exact endpoint-aware exchange on a DIFFERENT actual box: wide=21/20,
# s^6-width=1/2. Old and new earlier numerators both fail by exact checks.
# Eval-only; uses previously defined same-owner exact algorithms, no native solver.
harder=next(r for r in aniso_report if r['wide']=='21/20' and r['narrow_j']==6)
harder_lo=[Q(x) for x in harder['lower']];harder_hi=[Q(x) for x in harder['upper']];harder_cs=corners(harder_lo,harder_hi)
harder_routh=[routh_ok(a) for a in harder_cs];harder_dets=[integer_hurwitz(a) for a in harder_cs]
if harder_routh!=harder_dets or not all(harder_routh):raise ValueError('ACTUAL_BOX_STABILITY')
harder_tgrid=sorted(set(endpoint_tgrid+[Q(17,47),Q(7,25),Q(3),Q(0)]))
harder_rounds=[]
for iteration in range(4):
    atoms=[]
    for ci,a in enumerate(harder_cs):
        for t in harder_tgrid:
            direct,local=pair_vector_t(a,t)
            atoms.append((ci,t,[Q(v,local)/(1+t)**7 for v in direct]))
    atoms.append((None,None,[Q(0)]*7+[Q(1)]))
    common=lcm(*(v.denominator for atom in atoms for v in atom[2]))
    C=[[int(common*atom[2][k]) for atom in atoms] for k in range(8)]
    sol=exact_minimax(C,pivot_cap=1200)
    rec={'iteration':iteration+1,'nodes':[str(t) for t in harder_tgrid]+['infinity'],
         'atom_count':len(atoms),'common_scale':str(common),'solver_status':sol['status'],'pivots':sol['pivots']}
    if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';harder_rounds.append(rec);break
    opt=sol['optimum'];rec['normalized_grid_margin']=str(opt/common)
    if opt<0:
        raw=[sol['lambda'][i]*Q(common,1)/(1+atom[1])**7 if atom[1] is not None else sol['lambda'][i]*common for i,atom in enumerate(atoms)]
        factor=lcm(*(v.denominator for v in raw));weights=[int(factor*v) for v in raw];sums=[]
        for k in range(8):
            e=[Q(0)]*8;e[k]=Q(1)
            val=sum(weights[i]*(independent_pair_t(harder_cs[atom[0]],e,atom[1]) if atom[1] is not None else e[7]) for i,atom in enumerate(atoms))
            if val>=0:raise ValueError('STRICT_CERTIFICATE_REPLAY')
            sums.append(str(val))
        rec.update({'status':'STRICT_ACTUAL_BOX_CERTIFICATE','raw_weights':weights,'strict_sums':sums});harder_rounds.append(rec);break
    if opt==0:rec['status']='ZERO_GRID_MARGIN_UNRESOLVED';harder_rounds.append(rec);break
    dual=sol['dual'];M=max(sum(abs(C[k][i]) for k in range(8)) for i in range(len(atoms)))
    eps=opt/(2*M);candidate=[v+eps for v in dual];candidate=[v/candidate[7] for v in candidate]
    if not all(x>0 for x in candidate):raise ValueError('POSITIVE_COEFFICIENTS')
    for i,(ci,t,vec) in enumerate(atoms):
        actual=independent_pair_t(harder_cs[ci],candidate,t)/(1+t)**7 if t is not None else candidate[7]
        if actual<=0 or sum(candidate[k]*C[k][i] for k in range(8))!=common*actual:raise ValueError('GRID_DUAL_REPLAY')
    rec['numerator']=[str(x) for x in candidate];proofs=[];failure=None
    for ci,a in enumerate(harder_cs):
        p=pairing_polynomial(a,candidate);cert=whole_halfline(p,max_depth=32,max_nodes=4000)
        if cert['status']=='SUBDIVISION_CAP':cert=locate_strict_failure(p,max_depth=64,max_nodes=10000)
        proofs.append({'corner':ci,'polynomial':[str(x) for x in p],'certificate':cert})
        if cert['status']=='NONPOSITIVE_EXACT' and failure is None:failure=Q(cert['t'])
    rec['proofs']=proofs
    if all(x['certificate']['status']=='STRICT_POSITIVITY' and 'leaves' in x['certificate'] for x in proofs):
        for x in proofs:verify_leaves_by_power([Q(a) for a in x['polynomial']],x['certificate'])
        rec['status']='COMMON_NUMERATOR_PROVED';harder_rounds.append(rec);break
    if failure is None:rec['status']='BERNSTEIN_CAP_UNRESOLVED';harder_rounds.append(rec);break
    if failure in harder_tgrid:raise ValueError('REPEATED_EXACT_FAILURE')
    rec['status']='EXACT_UNSEEN_FREQUENCY_REFINEMENT';rec['new_t']=str(failure)
    harder_rounds.append(rec);harder_tgrid=sorted(harder_tgrid+[failure])
else:harder_rounds[-1]['terminal']='FOUR_ROUND_LIMIT'
print('harder actual-box exact exchange:',[{'iteration':x['iteration'],'atoms':x['atom_count'],'pivots':x['pivots'],
 'status':x['status'],'normalized_grid_margin':x.get('normalized_grid_margin'),'new_t':x.get('new_t'),'terminal':x.get('terminal')} for x in harder_rounds])
