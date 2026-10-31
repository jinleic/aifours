# Bounded anisotropic exact actual-box search; execute only inside Python Eval.
# Depends on independently written bounded-exact and Bernstein kernels in this
# session; no author optimizer/checker import and no scientific subprocess.
aniso_wide=[Q(101,100),Q(21,20)]
aniso_narrow=Q(1,2)
aniso_report=[]
for wide in aniso_wide:
    for shrunk in range(7):
        f=[wide]*7;f[shrunk]=aniso_narrow
        mid=[(x+y)/2 for x,y in zip(ray_base_lo,ray_base_hi)]
        rad=[f[j]*(ray_base_hi[j]-ray_base_lo[j])/2 for j in range(7)]
        lo=[x-y for x,y in zip(mid,rad)];hi=[x+y for x,y in zip(mid,rad)]
        rec={'wide':str(wide),'narrow_j':shrunk,'lower':[str(x) for x in lo],'upper':[str(x) for x in hi]}
        if not all(0<x<y for x,y in zip(lo,hi)):
            rec['status']='NONPOSITIVE_OR_DEGENERATE';aniso_report.append(rec);continue
        cs=corners(lo,hi)
        rs=[routh_ok(a) for a in cs];ds=[integer_hurwitz(a) for a in cs]
        if rs!=ds:raise ValueError('STABILITY_REPLAY_MISMATCH')
        rec['corner_hurwitz']=rs
        if not all(rs):
            rec['status']='NOT_ALL_FOUR_HURWITZ';aniso_report.append(rec);continue
        ps=[pairing_polynomial(a,ray_b) for a in cs]
        bez=[whole_halfline(p) for p in ps]
        rec['pairing_polynomials']=[[str(x) for x in p] for p in ps]
        rec['whole_halfline']=bez
        if all(x['status']=='STRICT_POSITIVITY' for x in bez):
            rec['status']='COMMON_BSTAR_CERTIFIED'
            rec['pairing_margin']=str(min(Q(x['margin']) for x in bez))
            aniso_report.append(rec);continue
        atoms=[]
        for i,a in enumerate(cs):
            for w in frequencies:
                vec,scale=pair_vector(a,w);atoms.append((i,w,vec,scale))
        C=[[atom[2][k] for atom in atoms] for k in range(8)]
        sol=exact_minimax(C,pivot_cap=500)
        rec['grid_solver_status']=sol['status'];rec['pivots']=sol['pivots']
        if sol['status']=='CERTIFIED_OPTIMUM':
            rec['grid_optimum']=str(sol['optimum']);rec['grid_dual']=[str(x) for x in sol['dual']]
            for i,w,vec,scale in atoms:
                if sum(sol['dual'][k]*vec[k] for k in range(8))!=scale*independent_pair(cs[i],sol['dual'],w):raise ValueError('PAIRING_REPLAY')
            if sol['optimum']<0:
                L=lcm(*(v.denominator for v in sol['lambda']))
                weights=[int(L*v)*atoms[i][3] for i,v in enumerate(sol['lambda'])]
                sums=[]
                for k in range(8):
                    unit=[Q(0)]*8;unit[k]=Q(1)
                    total=sum(weights[i]*independent_pair(cs[a[0]],unit,a[1]) for i,a in enumerate(atoms))
                    if total>=0:raise ValueError('STRICT_PAIRING_REPLAY')
                    sums.append(str(total))
                rec['status']='STRICT_ACTUAL_BOX_CERTIFICATE'
                rec['raw_atom_weights']=weights;rec['strict_sums']=sums
            else:rec['status']='GRID_NONNEGATIVE_DUAL; BOUNDS_OUTSIDE_GRID_UNSETTLED'
        else:rec['status']='GRID_PIVOT_CAP; BOUNDS_UNSETTLED'
        aniso_report.append(rec)
print('anisotropic exact search:',[{'wide':r['wide'],'narrow_j':r['narrow_j'],'status':r['status'],'corner_hurwitz':r.get('corner_hurwitz'),
 'b_status':[x['status'] for x in r.get('whole_halfline',[])],'pairing_margin':r.get('pairing_margin'),'grid_optimum':r.get('grid_optimum'),'pivots':r.get('pivots')} for r in aniso_report])
