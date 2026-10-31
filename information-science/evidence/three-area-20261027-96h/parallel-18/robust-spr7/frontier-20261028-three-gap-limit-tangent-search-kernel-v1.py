# Exact limiting Farkas search at rho=1. Physical boundary pairing rows are
# supplemented by both signs of three contact derivatives. The latter are
# justified only for a *single* numerator working at every rho<1, or as limits
# of positive physical rows at nearby t and rho. Negative output must be
# transferred to and independently checked on an actual rho<1 box.
from fractions import Fraction as Q
from math import lcm
limit_cs=tg_boundary_cs
limit_grid=[Q(x) for x in (0,1,2,4,7,8,9,10,12,14,16,20,25,30,40,50,60,70,80,100)]
limit_atoms=[]
for ci,a in enumerate(limit_cs):
    for t in limit_grid:
        direct,den=pair_vector_t(a,t);limit_atoms.append({'kind':'physical','corner':ci,'t':t,'vector':[Q(v,den)/(1+t)**7 for v in direct]})
limit_atoms.append({'kind':'infinity','corner':None,'t':None,'vector':[Q(0)]*7+[Q(1)]})
for ci,t in ((2,Q(3)),(1,Q(15)),(2,Q(65))):
    deriv=[]
    for k in range(8):
        unit=[Q(0)]*8;unit[k]=Q(1);poly=pairing_polynomial(limit_cs[ci],unit)
        if sum(poly[j]*t**j for j in range(8))!=0:raise ValueError('NONZERO_CONTACT')
        deriv.append(sum(j*poly[j]*t**(j-1) for j in range(1,8))/(1+t)**7)
    for sign in (1,-1):limit_atoms.append({'kind':'tangent','corner':ci,'t':t,'sign':sign,'vector':[sign*v for v in deriv]})
limit_scale=lcm(*(v.denominator for row in limit_atoms for v in row['vector']));limit_C=[[int(limit_scale*row['vector'][k]) for row in limit_atoms] for k in range(8)]
limit_sol=exact_minimax(limit_C,pivot_cap=2500)
limit_result={'solver_status':limit_sol['status'],'atoms':len(limit_atoms),'physical_grid':[str(t) for t in limit_grid],'pivots':limit_sol['pivots']}
if limit_sol['status']=='CERTIFIED_OPTIMUM':
    limit_opt=limit_sol['optimum']/limit_scale;limit_result['margin']=str(limit_opt)
    if limit_opt<0:
        vector=[sum(limit_sol['lambda'][i]*limit_atoms[i]['vector'][k] for i in range(len(limit_atoms))) for k in range(8)]
        if not all(v<0 for v in vector):raise ValueError('LIMIT_SIGNS')
        support=[]
        for i,w in enumerate(limit_sol['lambda']):
            if w:
                row=limit_atoms[i];support.append({'kind':row['kind'],'corner':row['corner'],'t':str(row['t']) if row['t'] is not None else 'infinity','sign':row.get('sign'),'weight':str(w)})
        limit_result.update({'status':'STRICT_LIMIT_TANGENT_CERTIFICATE','support':support,'coefficient_sums':[str(v) for v in vector]})
    elif limit_opt==0:limit_result.update({'status':'ZERO_LIMIT_NO_STRICT_CERTIFICATE_ON_GRID','dual':[str(v) for v in limit_sol['dual']]})
    else:raise ValueError('SIGN_PAIR_MUST_FORCE_NONPOSITIVE')
else:limit_result['status']='PIVOT_CAP'
print('limit-tangent exact result:',limit_result)
