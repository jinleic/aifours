# Exact tangent-preserving rational simplification for the five-contact box.
from fractions import Fraction as Q
if fsolve_rounds[-1]['status']!='ALL_RHO_LT_ONE_COMMON_NUMERATOR':raise ValueError('NO_WITNESS')
raw=[Q(v) for v in fsolve_rounds[-1]['numerator']];base=[v/raw[-1] for v in raw]
T=[row['vector'] for row in ftang if row['sign']==1]
def solve5(A,b):
    M=[[Q(x) for x in row]+[Q(y)] for row,y in zip(A,b)]
    for k in range(5):
        i=next((i for i in range(k,5) if M[i][k]),None)
        if i is None:raise ValueError('SINGULAR')
        M[k],M[i]=M[i],M[k];v=M[k][k];M[k]=[x/v for x in M[k]]
        for i in range(5):
            if i!=k:
                v=M[i][k];M[i]=[x-v*y for x,y in zip(M[i],M[k])]
    return [M[i][-1] for i in range(5)]
fround=[]
for den in (1,10,100,1000,10000,100000,1000000,10000000,100000000):
    b=[Q(0)]*8;b[0]=base[0];b[7]=Q(1);x=base[6];b[6]=Q((2*x.numerator*den+x.denominator)//(2*x.denominator),den)
    vals=solve5([[row[j] for j in (1,2,3,4,5)] for row in T],[-sum(row[j]*b[j] for j in (0,6,7)) for row in T])
    for j,v in zip((1,2,3,4,5),vals):b[j]=v
    rec={'denominator':den,'numerator':[str(v) for v in b]}
    if not all(v>0 for v in b):rec['status']='NONPOSITIVE_COEFFICIENT';fround.append(rec);continue
    if any(sum(row[k]*b[k] for k in range(8))!=0 for row in T):raise ValueError('TANGENCY')
    checks=[];polys=[];residuals=[]
    for ci,a in enumerate(fvertices):
        p=pairing_polynomial(a,b);polys.append(p);res=p
        for t in froots[ci]:res=quotient_by_root(quotient_by_root(res,t),t)
        residuals.append(res);checks.append(exact_nonnegative_halfline(res,maxdepth=40,maxnodes=18000))
    rec['boundary_checks']=checks
    if not all(p['status']=='NONNEGATIVE_PROVED' for p in checks):rec['status']='BOUNDARY_NOT_CERTIFIED';fround.append(rec);continue
    cp=pairing_polynomial(fcenter,b);proof=whole_halfline(cp,max_depth=40,max_nodes=15000)
    if proof['status']!='STRICT_POSITIVITY' or 'leaves' not in proof:rec['status']='CENTER_NOT_CERTIFIED';fround.append(rec);continue
    verify_leaves_by_power(cp,proof)
    rec.update({'status':'ALL_RHO_LT_ONE_COMMON_NUMERATOR','boundary_polynomials':[[str(x) for x in p] for p in polys],
     'boundary_residual_polynomials':[[str(x) for x in p] for p in residuals],'center_polynomial':[str(x) for x in cp],
     'center_proof':proof,'center_margin':str(Q(proof['margin']))});fround.append(rec);break
print('five-contact exact rounding:',[{'denominator':r['denominator'],'status':r['status'],'numerator':r['numerator'],
 'boundary_status':[p['status'] for p in r.get('boundary_checks',[])],'center_margin':r.get('center_margin')} for r in fround])
