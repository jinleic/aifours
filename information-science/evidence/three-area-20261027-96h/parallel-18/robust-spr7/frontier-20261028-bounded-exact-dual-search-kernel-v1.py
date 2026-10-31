# Bounded exact actual-box / strict-cone search, to be executed in Python Eval only.
# All scientific arithmetic is integers/Fraction; imports no optimizer or author checker.
from fractions import Fraction as Q
from math import gcd, lcm

# Primal LP: min max_k sum_i lambda_i C[k,i], lambda>=0, sum lambda=1.
# Fraction simplex uses Bland entering/leaving; verifies primal/dual exactly.
def exact_minimax(C, pivot_cap=1000):
    d=len(C); n=len(C[0])
    if d!=8 or n<1 or any(len(row)!=n for row in C):raise ValueError('MATRIX')
    if any(type(v)!=int for row in C for v in row):raise ValueError('NONINTEGER_MATRIX')
    shift=1+max(abs(v) for row in C for v in row)
    peak=max(range(d), key=lambda k:C[k][0])
    z=n; slack=lambda k:n+1+k
    nonbasic=list(range(1,n))+[slack(peak)]
    rows={}
    rows[0]=(Q(1),{i:Q(-1) for i in range(1,n)})
    rows[z]=(Q(shift+C[peak][0]),{**{i:Q(C[peak][i]-C[peak][0]) for i in range(1,n)},slack(peak):Q(1)})
    for k in range(d):
        if k==peak:continue
        v=C[peak][0]-C[k][0]
        cc={i:Q(C[peak][i]-C[k][i]-v) for i in range(1,n)}
        cc[slack(peak)]=Q(1)
        rows[slack(k)]=(Q(v),cc)
    objective_const=-rows[z][0]
    objective={i:-v for i,v in rows[z][1].items()}
    pivots=0
    while True:
        positive=[j for j in nonbasic if objective.get(j,0)>0]
        if not positive:break
        if pivots>=pivot_cap:return {'status':'PIVOT_CAP','pivots':pivots}
        enter=min(positive)
        candidates=[(val/(-coef.get(enter,0)),base) for base,(val,coef) in rows.items() if coef.get(enter,0)<0]
        if not candidates:raise ValueError('UNBOUNDED')
        _,leave=min(candidates)
        val,coef=rows.pop(leave); a=coef[enter]
        newval=-val/a
        newcoef={leave:Q(1)/a}
        for j,v in coef.items():
            if j!=enter and v:newcoef[j]=-v/a
        for base in list(rows):
            bv,bc=rows[base];bc=dict(bc);factor=bc.pop(enter,Q(0));bv+=factor*newval
            if factor:
                for j,v in newcoef.items():bc[j]=bc.get(j,Q(0))+factor*v
            rows[base]=(bv,{j:v for j,v in bc.items() if v})
        factor=objective.pop(enter,Q(0));objective_const+=factor*newval
        if factor:
            for j,v in newcoef.items():objective[j]=objective.get(j,Q(0))+factor*v
        objective={j:v for j,v in objective.items() if v}
        rows[enter]=(newval,{j:v for j,v in newcoef.items() if v})
        nonbasic.remove(enter);nonbasic.append(leave)
        if any(val<0 for val,_ in rows.values()):raise ValueError('PRIMAL_FEASIBILITY')
        pivots+=1
    lambdas=[rows.get(i,(Q(0),{}))[0] for i in range(n)]
    if sum(lambdas)!=1 or any(x<0 for x in lambdas):raise ValueError('PRIMAL_LAMBDA')
    vector=[sum(Q(C[k][i])*lambdas[i] for i in range(n)) for k in range(d)]
    optimum=max(vector)
    if rows.get(z,(Q(0),{}))[0] != shift+optimum:raise ValueError('PRIMAL_OBJECTIVE')
    # Recover LP dual by solving basis-transpose y=c_B over exact rationals.
    basis=list(rows)
    def A(row,var):
        if row==0:return Q(1) if var<n else Q(0)
        k=row-1
        if var<n:return Q(C[k][var])
        if var==z:return Q(-1)
        return Q(1) if var==slack(k) else Q(0)
    mat=[[A(row,var) for row in range(d+1)]+[Q(-1) if var==z else Q(0)] for var in basis]
    for col in range(d+1):
        pivot=next((r for r in range(col,d+1) if mat[r][col]),None)
        if pivot is None:raise ValueError('DUAL_SINGULAR')
        mat[col],mat[pivot]=mat[pivot],mat[col]
        v=mat[col][col];mat[col]=[x/v for x in mat[col]]
        for r in range(d+1):
            if r!=col:
                f=mat[r][col]
                if f:mat[r]=[x-f*y for x,y in zip(mat[r],mat[col])]
    dual=[mat[i][-1] for i in range(d+1)]
    if any(x<0 for x in dual[1:]) or sum(dual[1:])!=1:raise ValueError('DUAL_SIMPLEX')
    if -dual[0]!=optimum:raise ValueError('DUAL_OBJECTIVE')
    if any(sum(dual[k+1]*C[k][i] for k in range(d))<optimum for i in range(n)):raise ValueError('DUAL_COLUMN')
    return {'status':'CERTIFIED_OPTIMUM','pivots':pivots,'optimum':optimum,'lambda':lambdas,'dual':dual[1:],'vector':vector}

def corners(lo,hi):
    E=((lo[0],hi[2],lo[4],hi[6]),(hi[0],lo[2],hi[4],lo[6]))
    O=((lo[1],hi[3],lo[5]),(hi[1],lo[3],hi[5]))
    return [[e[0],o[0],e[1],o[1],e[2],o[2],e[3],Q(1)] for e in E for o in O]

def routh_ok(a):
    rows=[[a[7],a[5],a[3],a[1]],[a[6],a[4],a[2],a[0]]]
    for _ in range(6):
        u,v=rows[-2:]
        if v[0]<=0:return False
        rows.append([(v[0]*u[j+1]-u[0]*v[j+1])/v[0] for j in range(3)]+[Q(0)])
    return all(row[0]>0 for row in rows)

def bareiss_det(mat):
    a=[list(row) for row in mat];n=len(a);sign=1;prev=1
    if n==1:return a[0][0]
    for k in range(n-1):
        if a[k][k]==0:
            r=next((r for r in range(k+1,n) if a[r][k]!=0),None)
            if r is None:return 0
            a[k],a[r]=a[r],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numer=a[i][j]*pivot-a[i][k]*a[k][j]
                if numer%prev:raise ValueError('BAREISS_DIVISION')
                a[i][j]=numer//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

def integer_hurwitz(a):
    den=lcm(*(x.denominator for x in a))
    c=[int(den*a[7-j]) for j in range(8)]
    def coeff(j):return c[j] if 0<=j<=7 else 0
    signs=[]
    for n in range(1,8):
        mat=[[coeff(2*(j+1)-(i+1)) for j in range(n)] for i in range(n)]
        signs.append(bareiss_det(mat)>0)
    return all(signs)

def pair_vector(a,w):
    C=[]
    for k in range(8):
        val=Q(0)
        for j in range(8):
            if (j+k)%2==0:val+=a[j]*((-1)**(abs((k-j)//2)))*w**(j+k)
        C.append(val)
    scale=lcm(*(v.denominator for v in C))
    return [int(scale*v) for v in C],scale

def independent_pair(a,b,w):
    t=w*w
    E=lambda p:p[0]-p[2]*t+p[4]*t*t-p[6]*t*t*t
    O=lambda p:p[1]-p[3]*t+p[5]*t*t-p[7]*t*t*t
    return E(a)*E(b)+t*O(a)*O(b)

# Solver controls: the explicit optimum for +/- coordinate vectors is +/-1/8.
unit_neg=[[-int(i==k) for i in range(8)] for k in range(8)]
unit_pos=[[int(i==k) for i in range(8)] for k in range(8)]
control_neg=exact_minimax(unit_neg);control_pos=exact_minimax(unit_pos)
if control_neg['status']!='CERTIFIED_OPTIMUM' or control_neg['optimum']!=Q(-1,8):raise ValueError('NEGATIVE_CONTROL')
if control_pos['status']!='CERTIFIED_OPTIMUM' or control_pos['optimum']!=Q(1,8):raise ValueError('POSITIVE_CONTROL')

# Exact finite search family: six specified symmetric width factors about the
# pinned full-width rational K0, with four actual corners and eight rational w.
# This is NOT a universal test, and K0's old numerical search is not imported.
lo0=[Q(x,1000) for x in (4435,10747,23670,40980,10632,13071,1089)]
hi0=[Q(x,1000) for x in (4586,11496,24364,43182,11217,14315,1147)]
factors=[Q(1),Q(101,100),Q(21,20),Q(11,10),Q(5,4),Q(3,2)]
frequencies=[Q(1,2),Q(2,3),Q(1),Q(3,2),Q(2),Q(5,2),Q(3),Q(4)]
search=[]
for factor in factors:
    midpoint=[(a+b)/2 for a,b in zip(lo0,hi0)]
    radius=[factor*(b-a)/2 for a,b in zip(lo0,hi0)]
    lo=[m-r for m,r in zip(midpoint,radius)];hi=[m+r for m,r in zip(midpoint,radius)]
    if not all(0<a<b for a,b in zip(lo,hi)):
        search.append({'factor':str(factor),'status':'NONPOSITIVE_OR_DEGENERATE'});continue
    cs=corners(lo,hi)
    routh=[routh_ok(a) for a in cs]
    determinants=[integer_hurwitz(a) for a in cs]
    if routh!=determinants:raise ValueError('INDEPENDENT_STABILITY_MISMATCH')
    if not all(routh):
        search.append({'factor':str(factor),'status':'NOT_ALL_FOUR_HURWITZ','corner_status':routh});continue
    atoms=[]
    for i,a in enumerate(cs):
        for w in frequencies:
            vec,scale=pair_vector(a,w);atoms.append((i,w,vec,scale))
    C=[[atom[2][k] for atom in atoms] for k in range(8)]
    result=exact_minimax(C)
    if result['status']!='CERTIFIED_OPTIMUM':
        search.append({'factor':str(factor),'status':result['status'],'pivots':result['pivots']});continue
    optimum=result['optimum'];dual=result['dual']
    # Distinct direct E/O convolution is an independent exact pairing replay.
    for i,w,vec,scale in atoms:
        if sum(dual[k]*vec[k] for k in range(8))!=scale*independent_pair(cs[i],dual,w):raise ValueError('PAIRING_REPLAY')
    entry={'factor':str(factor),'status':'STRICT_CERTIFICATE' if optimum<0 else 'GRID_NONNEGATIVE_DUAL',
           'pivots':result['pivots'],'optimum':str(optimum),'dual':[str(v) for v in dual]}
    if optimum<0:
        L=lcm(*(v.denominator for v in result['lambda']))
        integer_weights=[int(L*v) for v in result['lambda']]
        sums=[sum(integer_weights[i]*C[k][i] for i in range(len(atoms))) for k in range(8)]
        raw_weights=[integer_weights[i]*atoms[i][3] for i in range(len(atoms))]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1)
            replay=sum(raw_weights[i]*independent_pair(cs[atom[0]],unit,atom[1]) for i,atom in enumerate(atoms))
            if replay!=sums[k] or replay>=0:raise ValueError('STRICT_PAIRING_REPLAY')
        entry.update({'raw_weight_by_corner_and_frequency':raw_weights,'strict_coefficient_sums':sums,
                      'lower':[str(x) for x in lo],'upper':[str(x) for x in hi]})
    search.append(entry)
print('bounded exact search:',{'controls':{'negative_basis':str(control_neg['optimum']),'positive_basis':str(control_pos['optimum'])},
 'factors':[str(x) for x in factors],'frequencies':[str(x) for x in frequencies], 'results':search})
