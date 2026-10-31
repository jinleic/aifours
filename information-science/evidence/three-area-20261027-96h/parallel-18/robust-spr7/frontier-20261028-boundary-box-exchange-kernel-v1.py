# Exact bounded search on r=679/640, the largest stable box in the previous
# five-bisection bracket. Eval only; 3 rational-simplex rounds maximum.
boundary_r=Q(679,640)
boundary_lo,boundary_hi=make_wide_box(boundary_r);boundary_cs=corners(boundary_lo,boundary_hi)
br=[routh_ok(a) for a in boundary_cs];bd=[integer_hurwitz(a) for a in boundary_cs]
if br!=bd or not all(br):raise ValueError('ACTUAL_BOX_STABILITY')
# First attempt the already certified b_H, checking all frequencies exactly.
boundary_old=[Q(x) for x in hard_frozen['numerator']]
boundary_old_polys=[pairing_polynomial(a,boundary_old) for a in boundary_cs]
boundary_old_proofs=[whole_halfline(p,max_depth=32,max_nodes=4000) for p in boundary_old_polys]
for i,proof in enumerate(boundary_old_proofs):
    if proof['status']=='SUBDIVISION_CAP':boundary_old_proofs[i]=locate_strict_failure(boundary_old_polys[i],max_depth=64,max_nodes=10000)
boundary_old_success=all(x['status']=='STRICT_POSITIVITY' and 'leaves' in x for x in boundary_old_proofs)
if boundary_old_success:
    for p,proof in zip(boundary_old_polys,boundary_old_proofs):verify_leaves_by_power(p,proof)
    boundary_rounds=[{'status':'EARLIER_COMMON_NUMERATOR_PROVED','numerator':[str(x) for x in boundary_old],
      'proofs':boundary_old_proofs,'polynomials':[[str(x) for x in p] for p in boundary_old_polys]}]
else:
    boundary_tgrid=sorted(set(harder_tgrid+[Q(0)]+[Q(x['t']) for x in boundary_old_proofs if x['status']=='NONPOSITIVE_EXACT']))
    boundary_rounds=[]
    for iteration in range(3):
        atoms=[]
        for ci,a in enumerate(boundary_cs):
            for t in boundary_tgrid:
                direct,local=pair_vector_t(a,t);atoms.append((ci,t,[Q(v,local)/(1+t)**7 for v in direct]))
        atoms.append((None,None,[Q(0)]*7+[Q(1)]))
        common=lcm(*(v.denominator for atom in atoms for v in atom[2]))
        C=[[int(common*atom[2][k]) for atom in atoms] for k in range(8)]
        sol=exact_minimax(C,pivot_cap=1200)
        rec={'iteration':iteration+1,'nodes':[str(t) for t in boundary_tgrid]+['infinity'],
          'atom_count':len(atoms),'common_scale':str(common),'solver_status':sol['status'],'pivots':sol['pivots']}
        if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';boundary_rounds.append(rec);break
        opt=sol['optimum'];rec['normalized_grid_margin']=str(opt/common)
        if opt<0:
            raw=[sol['lambda'][i]*Q(common,1)/(1+atom[1])**7 if atom[1] is not None else sol['lambda'][i]*common for i,atom in enumerate(atoms)]
            scale=lcm(*(v.denominator for v in raw));weights=[int(scale*v) for v in raw];sums=[]
            for k in range(8):
                e=[Q(0)]*8;e[k]=Q(1)
                value=sum(weights[i]*(independent_pair_t(boundary_cs[atom[0]],e,atom[1]) if atom[1] is not None else e[7]) for i,atom in enumerate(atoms))
                if value>=0:raise ValueError('STRICT_CERTIFICATE_REPLAY')
                sums.append(str(value))
            rec.update({'status':'STRICT_ACTUAL_BOX_CERTIFICATE','raw_weights':weights,'strict_sums':sums});boundary_rounds.append(rec);break
        if opt==0:rec['status']='ZERO_GRID_MARGIN_UNRESOLVED';boundary_rounds.append(rec);break
        dual=sol['dual'];M=max(sum(abs(C[k][i]) for k in range(8)) for i in range(len(atoms)))
        eps=opt/(2*M);candidate=[v+eps for v in dual];candidate=[v/candidate[7] for v in candidate]
        if not all(x>0 for x in candidate):raise ValueError('POSITIVE_COEFFICIENTS')
        for i,(ci,t,vec) in enumerate(atoms):
            value=independent_pair_t(boundary_cs[ci],candidate,t)/(1+t)**7 if t is not None else candidate[7]
            if value<=0 or sum(candidate[k]*C[k][i] for k in range(8))!=common*value:raise ValueError('GRID_DUAL_REPLAY')
        rec['numerator']=[str(x) for x in candidate];proofs=[];failure=None
        for ci,a in enumerate(boundary_cs):
            p=pairing_polynomial(a,candidate);cert=whole_halfline(p,max_depth=32,max_nodes=4000)
            if cert['status']=='SUBDIVISION_CAP':cert=locate_strict_failure(p,max_depth=64,max_nodes=10000)
            proofs.append({'corner':ci,'polynomial':[str(x) for x in p],'certificate':cert})
            if cert['status']=='NONPOSITIVE_EXACT' and failure is None:failure=Q(cert['t'])
        rec['proofs']=proofs
        if all(x['certificate']['status']=='STRICT_POSITIVITY' and 'leaves' in x['certificate'] for x in proofs):
            for x in proofs:verify_leaves_by_power([Q(a) for a in x['polynomial']],x['certificate'])
            rec['status']='COMMON_NUMERATOR_PROVED';boundary_rounds.append(rec);break
        if failure is None:rec['status']='BERNSTEIN_CAP_UNRESOLVED';boundary_rounds.append(rec);break
        if failure in boundary_tgrid:raise ValueError('REPEATED_EXACT_FAILURE')
        rec['status']='EXACT_UNSEEN_FREQUENCY_REFINEMENT';rec['new_t']=str(failure)
        boundary_rounds.append(rec);boundary_tgrid=sorted(boundary_tgrid+[failure])
    else:boundary_rounds[-1]['terminal']='THREE_ROUND_LIMIT'
print('boundary-box exact search:',{'r':str(boundary_r),'earlier_numerator':[p['status'] for p in boundary_old_proofs],
 'rounds':[{'iteration':r.get('iteration'),'atoms':r.get('atom_count'),'pivots':r.get('pivots'),'status':r['status'],
 'new_t':r.get('new_t'),'terminal':r.get('terminal')} for r in boundary_rounds]})
