# Bounded exact exchange search on one already-checked actual anisotropic box.
# Eval-only: no native solver, author checker or floating-point arithmetic.
# Requires previously loaded exact simplex, Routh/determinant, Bernstein and
# independent power-to-Bernstein review kernels. Six rounds maximum.

def pair_vector_t(a,t):
    raw=[]
    for k in range(8):
        v=sum(a[j]*((-1)**abs((k-j)//2))*t**((j+k)//2) for j in range(8) if (j+k)%2==0)
        raw.append(v)
    scale=lcm(*(v.denominator for v in raw))
    return [int(scale*v) for v in raw],scale

def independent_pair_t(a,b,t):
    E=lambda p:p[0]-p[2]*t+p[4]*t*t-p[6]*t*t*t
    O=lambda p:p[1]-p[3]*t+p[5]*t*t-p[7]*t*t*t
    return E(a)*E(b)+t*O(a)*O(b)

chosen=next(r for r in aniso_report if r['wide']=='101/100' and r['narrow_j']==6)
lo=[Q(x) for x in chosen['lower']];hi=[Q(x) for x in chosen['upper']];cs=corners(lo,hi)
routh=[routh_ok(a) for a in cs];det=[integer_hurwitz(a) for a in cs]
if routh!=det or not all(routh):raise ValueError('ACTUAL_BOX_STABILITY')
# New failing t from the prior exact search plus the original eight squared nodes.
tgrid=sorted(set([w*w for w in frequencies]+[Q(1,7),Q(7,25)]))
adaptive_rounds=[]
for iteration in range(6):
    atoms=[]
    for ci,a in enumerate(cs):
        for t in tgrid:
            column,scale=pair_vector_t(a,t);atoms.append((ci,t,column,scale))
    C=[[atom[2][k] for atom in atoms] for k in range(8)]
    sol=exact_minimax(C,pivot_cap=1000)
    rec={'iteration':iteration+1,'nodes':[str(t) for t in tgrid],'atom_count':len(atoms),'solver_status':sol['status'],'pivots':sol['pivots']}
    if sol['status']!='CERTIFIED_OPTIMUM':
        rec['status']='PIVOT_CAP';adaptive_rounds.append(rec);break
    opt=sol['optimum'];rec['grid_optimum']=str(opt)
    if opt<0:
        L=lcm(*(v.denominator for v in sol['lambda']))
        rawweights=[int(L*v)*atoms[i][3] for i,v in enumerate(sol['lambda'])]
        sums=[]
        for k in range(8):
            e=[Q(0)]*8;e[k]=Q(1)
            value=sum(rawweights[i]*independent_pair_t(cs[atom[0]],e,atom[1]) for i,atom in enumerate(atoms))
            if value>=0:raise ValueError('STRICT_CERTIFICATE_REPLAY')
            sums.append(str(value))
        rec.update({'status':'STRICT_ACTUAL_BOX_CERTIFICATE','raw_weights':rawweights,'strict_sums':sums})
        adaptive_rounds.append(rec);break
    if opt==0:
        rec['status']='ZERO_GRID_MARGIN_UNRESOLVED';adaptive_rounds.append(rec);break
    # Obtain a strictly coefficient-positive real numerator that stays strictly
    # positive on the finite grid, without relying on a floating LP solution.
    dual=sol['dual'];M=max(sum(abs(C[k][i]) for k in range(8)) for i in range(len(atoms)))
    epsilon=opt/(2*M)
    candidate=[v+epsilon for v in dual]
    if not all(x>0 for x in candidate):raise ValueError('POSITIVE_COEFFICIENTS')
    candidate=[v/candidate[7] for v in candidate]
    for i,(ci,t,column,scale) in enumerate(atoms):
        one=sum(candidate[k]*column[k] for k in range(8))
        if one<=0 or one!=scale*independent_pair_t(cs[ci],candidate,t):raise ValueError('GRID_DUAL_REPLAY')
    rec['numerator']=[str(x) for x in candidate]
    proofs=[];failure=None
    for ci,a in enumerate(cs):
        p=pairing_polynomial(a,candidate);cert=whole_halfline(p,max_depth=32,max_nodes=4000)
        if cert['status']=='SUBDIVISION_CAP':cert=locate_strict_failure(p,max_depth=64,max_nodes=10000)
        proofs.append({'corner':ci,'polynomial':[str(x) for x in p],'certificate':cert})
        if cert['status']=='NONPOSITIVE_EXACT' and failure is None:failure=Q(cert['t'])
    rec['proofs']=proofs
    if all(x['certificate']['status']=='STRICT_POSITIVITY' and 'leaves' in x['certificate'] for x in proofs):
        for item in proofs:verify_leaves_by_power([Q(x) for x in item['polynomial']],item['certificate'])
        rec['status']='COMMON_NUMERATOR_PROVED';adaptive_rounds.append(rec);break
    if failure is None:
        rec['status']='BERNSTEIN_CAP_UNRESOLVED';adaptive_rounds.append(rec);break
    if failure in tgrid:raise ValueError('REPEATED_EXACT_FAILURE')
    rec['status']='EXACT_UNSEEN_FREQUENCY_REFINEMENT';rec['new_t']=str(failure)
    adaptive_rounds.append(rec);tgrid=sorted(tgrid+[failure])
else:
    adaptive_rounds[-1]['terminal']='SIX_ROUND_LIMIT'
print('adaptive exact box search:',[{'iteration':r['iteration'],'atom_count':r['atom_count'],'pivots':r.get('pivots'),
 'status':r['status'],'grid_optimum':r.get('grid_optimum'),'new_t':r.get('new_t'),'terminal':r.get('terminal')} for r in adaptive_rounds])
