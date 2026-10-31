# Exact bivariate Bernstein certification of an interval of three-contact
# shapes. b0,b2,b4 are solved from exact tangent equations while the other
# four monic coefficients remain fixed. Cramer's rule clears the determinant:
# b(x) has degree <=3 and each boundary pairing has degree <=4 in x.
from fractions import Fraction as Q
from math import comb

def gauss_inverse(A):
    n=len(A);M=[[Q(x) for x in row]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        p=next((i for i in range(j,n) if M[i][j]),None)
        if p is None:raise ValueError('INVERSE')
        M[j],M[p]=M[p],M[j];v=M[j][j];M[j]=[x/v for x in M[j]]
        for i in range(n):
            if i!=j:
                v=M[i][j];M[i]=[a-v*b for a,b in zip(M[i],M[j])]
    return [row[n:] for row in M]
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
zgrid=[Q(j,4) for j in range(5)]
B=[[Q(comb(4,k))*z**k*(1-z)**(4-k) for k in range(5)] for z in zgrid]
Binv=gauss_inverse(B)
base_free={j:ub[j] for j in (1,3,5,6,7)}
u_contacts=[(2,Q(3)),(1,Q(15)),(2,Q(65))]
def shape_sample(x):
    widths=shape_widths(x);lo=[cx_center[j]-widths[j] for j in range(7)];hi=[cx_center[j]+widths[j] for j in range(7)];vertices=corners(lo,hi)
    A=[];rhs=[]
    for ci,t in u_contacts:
        a=vertices[ci]
        if parity(a,t)!=(Q(0),Q(0)):raise ValueError('CONTACT')
        ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
        ob=base_free[1]-base_free[3]*t+base_free[5]*t*t-t**3
        A.append([ep,-t*ep,t*t*ep]);rhs.append(ep*base_free[6]*t**3-t*op*ob)
    determinant=det3(A)
    if determinant==0:raise ValueError('SINGULAR')
    unknown=solve3(A,rhs);b=[Q(0)]*8
    for j in base_free:b[j]=base_free[j]
    for j,v in zip((0,2,4),unknown):b[j]=v
    sign=1 if det_at_center>0 else -1
    b=[v*determinant*sign for v in b]
    if b[7]<=0:raise ValueError('DETERMINANT_SIGN')
    values=b[:];contacts={1:[Q(15)],2:[Q(3),Q(65)]}
    for ci,a in enumerate(vertices):
        poly=pairing_polynomial(a,b);res=poly
        for t in contacts.get(ci,[]):res=quotient_by_root(quotient_by_root(res,t),t)
        for leaf in u_frozen['boundary_nonnegative_proofs'][ci]['leaves']:
            values.extend(bernstein(res,Q(leaf['left']),Q(leaf['right'])))
    cp=pairing_polynomial(cx_center,b)
    for leaf in u_frozen['center_proof']['leaves']:values.extend(bernstein(cp,Q(leaf['left']),Q(leaf['right'])))
    return values

# Tangent matrix at the original rational center shape.
xc=Q(1530997,1512675);w=shape_widths(xc);verts=corners([cx_center[j]-w[j] for j in range(7)],[cx_center[j]+w[j] for j in range(7)])
A0=[]
for ci,t in u_contacts:
    a=verts[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;A0.append([ep,-t*ep,t*t*ep])
det_at_center=det3(A0)
if det_at_center==0:raise ValueError('CENTER_DETERMINANT')
shape_neighborhood=[]
for eps in (Q(1,10**6),Q(1,10**9),Q(1,10**12),Q(1,10**15),Q(1,10**18)):
    left=xc-eps;right=xc+eps
    if not iv[0]<left<right<iv[1]:raise ValueError('SHAPE_INTERVAL')
    samples=[shape_sample(left+(right-left)*z) for z in zgrid]
    if any(len(v)!=len(samples[0]) for v in samples):raise ValueError('SAMPLE_DIMENSIONS')
    mins=[]
    for j in range(len(samples[0])):
        coeff=[sum(Binv[i][r]*samples[r][j] for r in range(5)) for i in range(5)]
        mins.append(min(coeff))
    rec={'epsilon':str(eps),'left':str(left),'right':str(right),'inequalities':len(mins),'positive_bernstein_coefficients':all(v>0 for v in mins),'minimum':str(min(mins))}
    shape_neighborhood.append(rec)
    if rec['positive_bernstein_coefficients']:rec['status']='CERTIFIED_NEIGHBORHOOD';break
    rec['status']='SIGN_NOT_CERTIFIED'
print('shape-neighborhood bivariate Bernstein:',shape_neighborhood)
