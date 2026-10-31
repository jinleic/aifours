#!/usr/bin/env python3
"""Independent exact v4 two-cycle PH7 endpoint review checker.

Reconstructs the polynomial system, a rational contraction certificate,
all stated interval inequalities via Bernstein/box bounds, the full free
7x7 matrix, the actual numerator, and every normalizer row.  No author
checker or certificate is read.  Uses the already-installed SymPy library.
"""
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('previous_review_helpers',ROOT/'frontier-review-f18-ph7-independent-check.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
S,R=a.S,a.R
U,V,z,y,c=S.symbols('U V z y c',real=True)
du,dv,dz,t=S.symbols('du dv dz t',real=True)
U0=R(1338787907,10**9);V0=R(1042029691,10**9);Z0=R(820420441,10**9)
radius=R(1,10**7)
D=lambda q:q*((q+1)**2+z)**2


def zero(v,label):a.zero(v,label)


def absolute_tail(expr, variables, radii):
    p=S.Poly(S.expand(expr),*variables)
    result=S.Rational(0)
    constant=p.coeff_monomial((0,)*len(variables))
    for powers,coefficient in p.terms():
        if any(powers):
            assert coefficient.is_Rational
            term=abs(coefficient)
            for radius_i,power in zip(radii,powers):term*=radius_i**power
            result+=term
    return constant,result


def bernstein_polynomials(poly,var,lo,hi):
    q=S.Poly(S.cancel(poly),var)
    n=q.degree()
    tpoly=S.Poly(S.expand(q.as_expr().subs(var,lo+(hi-lo)*t)),t)
    coefficients=[tpoly.nth(i) for i in range(n+1)]
    return [S.cancel(sum(coefficients[i]*S.binomial(k,i)/S.binomial(n,i)
                         for i in range(k+1))) for k in range(n+1)]


def main():
    p0=5*U+2*V-4
    q0=10*U**2+10*U*V-20*U+V**2-8*V-2*z+10
    Rpoly=S.Poly(S.expand((y+U)**5*(y+V)**2-D(y)*(y*y+p0*y+q0)),y)
    D10=Rpoly.nth(2);E4=Rpoly.nth(4);E3=Rpoly.nth(3);E1=Rpoly.nth(1)-2*V*D10
    assert Rpoly.nth(7)==Rpoly.nth(6)==Rpoly.nth(5)==0
    F=S.Matrix([E4,E3,E1]);variables=(U,V,z);center={U:U0,V:V0,z:Z0}
    J=F.jacobian(variables);J0=J.subs(center);assert J0.det()!=0
    inverse=J0.inv();assert inverse*J0==S.eye(3)
    displacement=inverse*F.subs(center)
    error=max(abs(v) for v in displacement);assert error<radius/100
    defect=S.eye(3)-inverse*J
    row_bounds=[]
    for i in range(3):
        total=S.Rational(0)
        for j in range(3):
            shifted=S.expand(defect[i,j].subs({U:U0+du,V:V0+dv,z:Z0+dz},simultaneous=True))
            constant,tail=absolute_tail(shifted,(du,dv,dz),(radius,radius,radius))
            assert constant==0
            total+=tail
        row_bounds.append(total)
    contraction=max(row_bounds);assert contraction<R(1,100)
    low,high=R(7,9),R(820421,10**6)
    assert low<Z0-radius<Z0+radius<high<R(8,9)

    e=a.esym([U,U,U,U,V,V]);A,B,C3=e[1:4]
    H0=B+4*A-A*A-6;L=B-4*A+10-2*z;N=4*H0+4-C3-B*(4-A)-4*z
    zero(E4-(L*p0-N),'E4 endpoint match')
    p=S.cancel(N/L);q=S.cancel((A-4)*p+H0-2*z);w=S.cancel(p+4-A)
    B0=S.cancel(p-2*U);C0=S.cancel(q-U*p+U*U);Q=y*y+p*y+q
    zero(Q-((y+U)**2+B0*(y+U)+C0),'actual numerator Q')
    phi=S.cancel(e[4]+C3*w-((6+2*z)*q+(4+4*z)*p+(1+z)**2))
    R2=S.cancel(e[5]+e[4]*w-(4+4*z)*q-(1+z)**2*p)
    R1=S.cancel(e[6]+e[5]*w-(1+z)**2*q);R0=S.cancel(e[6]*w)
    D1=S.cancel(R2-3*U*phi);D2=S.cancel(R1-3*U**2*phi-2*V*D1)
    D3=S.cancel(R0-U**3*phi-V**2*D1-V*D2)
    # At E4=0, p=p0, q=q0, w=U.  Check the remaining
    # endpoint residuals in those substitutions directly, not numerically.
    zero(((A-4)*p0+H0-2*z)-q0,'q0 endpoint')
    phi0=S.expand(e[4]+C3*U-((6+2*z)*q0+(4+4*z)*p0+(1+z)**2))
    zero(phi0-E3,'E3 endpoint feedback')
    zero((Rpoly.nth(1)-2*V*Rpoly.nth(2))-E1,'E1 endpoint feedback')
    # All formal-z identity by clearing the ONLY denominator L.
    polynomial=(y+w)*(y+U)**4*(y+V)**2-phi*(y+U)**3-D1*(y+V)**2-D2*(y+V)-D3-D(y)*Q
    zero(L*polynomial,'complete substituted determinant coefficient identity')

    cleared={'L':L,'Lp':S.cancel(L*p),'Lq':S.cancel(L*q),'Lw':S.cancel(L*w),
             'LB':S.cancel(L*B0),'LC':S.cancel(L*C0),'LD1':S.cancel(L*D1),'LD3':S.cancel(L*D3)}
    floors={'L':1,'Lp':7,'Lq':9,'Lw':2,'LB':3,'LC':2,'LD1':3,'LD3':2}
    for name in list(cleared):cleared[name]=S.cancel(cleared[name]-floors[name])
    cleared['minus_dz_Lphi_minus_6']=S.cancel(-S.diff(S.cancel(L*phi),z)-6)
    cleared['minus_dz_LD2_minus_9/10']=S.cancel(-S.diff(S.cancel(L*D2),z)-R(9,10))
    bounds={}
    for name,expr in cleared.items():
        assert S.denom(expr)==1 or S.denom(expr).is_Integer,(name,S.denom(expr))
        coefficients=bernstein_polynomials(expr,z,low,high)
        minima=[]
        for coefficient in coefficients:
            shifted=S.expand(coefficient.subs({U:U0+du,V:V0+dv},simultaneous=True))
            center_value,tail=absolute_tail(shifted,(du,dv),(radius,radius))
            assert center_value-tail>0,(name,center_value,tail)
            minima.append(center_value-tail)
        bounds[name]={'degree':len(coefficients)-1,'coefficient_lower_bounds':[str(v) for v in minima],
                      'least_lower_bound':str(min(minima))}

    # Full FREE feedback matrix: independent checks of determinant, numerator,
    # and normalizer tie, without treating fixed-rate v2 as a general checker.
    W,Phi,X1,X2,X3,P,Qc0,K=S.symbols('W Phi X1 X2 X3 P Qc0 K')
    G=S.Matrix([[-U,1,0,0,0,0,0],[0,-U,1,0,0,0,0],[0,0,-U,1,0,0,0],
                [0,0,0,-W,1,0,0],[X1,0,0,0,-U,1,0],
                [X2,0,0,0,0,-V,1],[X3,0,0,Phi,0,0,-V]])
    M=y*S.eye(7)-G
    det=S.expand(M.det(method='domain-ge'))
    closed=(y+W)*(y+U)**4*(y+V)**2-Phi*(y+U)**3-X1*(y+V)**2-X2*(y+V)-X3
    zero(det-closed,'free 7x7 determinant')
    bb,cc=S.symbols('bb cc');beta=S.Matrix([[cc,bb,1,0,0,0,0]]);e7=S.Matrix([0,0,0,0,0,0,1])
    zero((M+e7*beta).det(method='domain-ge')-det-(cc+bb*(y+U)+(y+U)**2),'free actual numerator')
    qq=c*c+P*c+Qc0;Bfree=P-2*U;Cfree=Qc0-U*P+U*U
    hh1=1/qq;hh2=(c+U)*hh1;hh3=(c+U)*hh2;hh4=(c+U)*hh3
    hh7=(K+X3*hh1+Phi*hh4)/(c+V);hh6=(hh7+X2*hh1)/(c+V);hh5=(hh6+X1*hh1)/(c+U)
    hv=S.Matrix([hh1,hh2,hh3,hh4,hh5,hh6,hh7]); residual=(c*S.eye(7)-G)*hv-K*e7
    for j in (0,1,2,4,5,6):zero(residual[j],f'free normalizer row {j+1}')
    beta0=S.Matrix([[Cfree,Bfree,1,0,0,0,0]])
    zero((beta0*hv)[0]-1,'free beta h')
    zero(residual[3]*qq*(c+U)*(c+V)**2-(closed.subs(y,c)-K*qq),'free central row identity')

    result={'sympy_version':S.__version__,
            'contraction_bound_exact':str(contraction),'center_displacement_exact':str(error),
            'box_radius':str(radius),'all_jacobian_centered_bounds_and_root_box':'PASS',
            'all_10_uniform_Bernstein_box_bounds':bounds,
            'endpoint_E4_E3_E1_and_complete_symbolic_identity':'PASS',
            'free7x7_determinant_numerator_6rows_center_identity_beta':'PASS',
            'scope':'independent exact rational symbolic checker; no author checker/certificate read',
            'not_formal_or_external_model_review':True}
    out=ROOT/'frontier-review-f50-ph7-endpoint-independent-check-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: SymPy {S.__version__}; exact contraction <1/100 and center residual <radius/100; 10 uniform Bernstein-box bounds; endpoint identities; free 7x7 det/numerator/normalizer')
    print(out.name)


if __name__=='__main__':main()
