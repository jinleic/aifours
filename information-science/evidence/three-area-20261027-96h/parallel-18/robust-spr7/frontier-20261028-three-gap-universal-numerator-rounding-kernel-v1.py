# Simplify exact all-scale candidate without destroying the three tangencies.
# Four free monic coefficients are rounded, and three even coefficients are
# solved exactly from contact derivative identities. All halfline checks replay.
from fractions import Fraction as Q
if centered_rounds[-1]['status']!='ONE_NUMERATOR_FOR_ALL_RHO_LT_ONE':raise ValueError('NO_SOURCE_WITNESS')
base=[Q(x) for x in centered_rounds[-1]['dual']];base=[x/base[-1] for x in base]
tangent=[row['vector'] for row in limit_atoms if row['kind']=='tangent' and row['sign']==1]
if len(tangent)!=3:raise ValueError('TANGENT_ROWS')
def solve3(A,b):
    m=[[Q(x) for x in row]+[Q(y)] for row,y in zip(A,b)]
    for k in range(3):
        i=next((i for i in range(k,3) if m[i][k]),None)
        if i is None:raise ValueError('SINGULAR')
        m[k],m[i]=m[i],m[k];s=m[k][k];m[k]=[x/s for x in m[k]]
        for i in range(3):
            if i==k:continue
            s=m[i][k];m[i]=[x-s*y for x,y in zip(m[i],m[k])]
    return [m[i][-1] for i in range(3)]
free=(1,3,5,6);unknown=(0,2,4);universal_round=[]
for den in (100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000):
    b=[Q(0)]*8;b[7]=Q(1)
    for j in free:
        x=base[j];b[j]=Q((2*x.numerator*den+x.denominator)//(2*x.denominator),den)
    vals=solve3([[r[j] for j in unknown] for r in tangent],[-sum(r[j]*b[j] for j in free+(7,)) for r in tangent])
    for j,v in zip(unknown,vals):b[j]=v
    rec={'denominator':den,'numerator':[str(x) for x in b]}
    if not all(x>0 for x in b):rec['status']='NONPOSITIVE_COEFFICIENT';universal_round.append(rec);continue
    if any(sum(r[k]*b[k] for k in range(8))!=0 for r in tangent):raise ValueError('TANGENT_PRESERVATION')
    checks=[];polys=[];contacts={1:[Q(15)],2:[Q(3),Q(65)]}
    for ci,a in enumerate(limit_cs):
        poly=pairing_polynomial(a,b);polys.append(poly);residual=poly
        for t in contacts.get(ci,[]):residual=quotient_by_root(quotient_by_root(residual,t),t)
        checks.append(exact_nonnegative_halfline(residual,maxdepth=40,maxnodes=16000))
    rec['boundary_checks']=checks
    if not all(p['status']=='NONNEGATIVE_PROVED' for p in checks):rec['status']='BOUNDARY_NOT_CERTIFIED';universal_round.append(rec);continue
    centerpoly=pairing_polynomial(cx_center,b);proof=whole_halfline(centerpoly,max_depth=45,max_nodes=20000)
    if proof['status']!='STRICT_POSITIVITY' or 'leaves' not in proof:rec['status']='CENTER_NOT_CERTIFIED';universal_round.append(rec);continue
    verify_leaves_by_power(centerpoly,proof)
    rec.update({'status':'ONE_NUMERATOR_FOR_ALL_RHO_LT_ONE','boundary_polynomials':[[str(x) for x in p] for p in polys],
                'center_polynomial':[str(x) for x in centerpoly],'center_proof':proof,'center_margin':str(Q(proof['margin']))});universal_round.append(rec);break
print('three-gap universal numerator rounding:',[{'denominator':r['denominator'],'status':r['status'],'numerator':r['numerator'],
  'boundary_status':[p['status'] for p in r.get('boundary_checks',[])],'center_margin':r.get('center_margin')} for r in universal_round])
