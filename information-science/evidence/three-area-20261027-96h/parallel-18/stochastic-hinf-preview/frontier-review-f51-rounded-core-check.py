#!/usr/bin/env python3
"""Independent exact coefficient checks and bounded Decimal R-branch diagnostics.

The numerical branch is conditional on the stated scalar stationarity/zero
system; it is not an independent global all-law optimizer certification.
"""
from decimal import Decimal, localcontext
from fractions import Fraction as F
import json


def decimal_pi():
    one=Decimal(1); two=Decimal(2); four=Decimal(4)
    a=one; b=one/two.sqrt(); t=one/four; p=one
    for _ in range(8):
        new_a=(a+b)/two
        b=(a*b).sqrt()
        t-=p*(a-new_a)*(a-new_a)
        a=new_a
        p*=two
    return (a+b)*(a+b)/(four*t)


def arcsin_series(x):
    if not (Decimal(0)<=x<Decimal(1)):
        raise ValueError("arcsin argument not in [0,1)")
    # a_n=binomial(2n,n)/(4^n(2n+1)), recurrence for term values.
    term=x; out=x; n=0
    while n<2000:
        term *= x*x*Decimal((2*n+1)**2)/(Decimal(2*n+2)*Decimal(2*n+3))
        out += term
        n+=1
        if abs(term)<Decimal('1e-75'):
            return out
    raise RuntimeError("arcsin series did not converge")


def branch_data(t,m):
    one=Decimal(1); two=Decimal(2); three=Decimal(3)
    T2=m+two*m*m
    T3=m+6*m*m+6*m**3
    T4=m+14*m*m+36*m**3+24*m**4
    var=m+m*m
    C0=m/three+Decimal(3)*m*m/2+m**3
    target=C0+t*var
    def P(d): return Decimal(4)*d**3/3+2*m*d*d+m*m*d
    if P(t)<=target:
        return None
    lo=Decimal(0); hi=t
    for _ in range(250):
        mid=(lo+hi)/2
        if P(mid)<target: lo=mid
        else: hi=mid
    d=(lo+hi)/2
    lam=2*t*t+2*d*d+2*m*(t+d)+T2
    if not (T2<lam<4*m*m+4*m+one/3):
        return None
    c=t-d; A=lam-var; w=2*t
    radical=A-c*c
    if not (A>0 and radical>0 and 0<c<A.sqrt()):
        return None
    J3=(c*radical.sqrt()*(5*A-2*c*c)+3*A*A*arcsin_series(c/A.sqrt()))/8
    Rint=-Decimal(2)*J3/3+(m*A-m**3/3)*c-c**4/3+lam*c*c/2
    Uint=(w**3/3+m*w*w+(T2-lam)*w)*c
    Uint+=(-w*w-2*m*w+2*lam-T2)*c*c/2
    Uint+=Decimal(2)*(w+m)*c**3/3-Decimal(2)*c**4/3
    M2=w*w+2*m*w+T2
    M4=w**4+4*m*w**3+6*T2*w*w+4*T3*w+T4
    HD=Decimal(2)*M4/3-2*lam*M2
    return {"d":d,"lambda":lam,"H":HD+8*(Rint-Uint),"T2":T2}


def solve_case(q, pi):
    s=Decimal(1)/Decimal(q)**3
    b=s**4
    m=b/(1-b)
    lo=Decimal('0.4')*s; hi=Decimal('0.8')*s
    left=branch_data(lo,m); right=branch_data(hi,m)
    if left is None or right is None or left["H"]*right["H"]>=0:
        raise RuntimeError(f"no valid sign bracket at q={q}")
    ls=left["H"]
    for _ in range(160):
        mid=(lo+hi)/2
        cur=branch_data(mid,m)
        if cur is None: raise RuntimeError(f"left rounded branch at q={q}")
        if cur["H"]*ls>0: lo=mid; ls=cur["H"]
        else: hi=mid
    t=(lo+hi)/2; data=branch_data(t,m)
    R=(Decimal(4)/(3*pi)).sqrt().sqrt()
    c0=R*R
    c1=Decimal(8)*Decimal(2).sqrt()/(3*pi*R)
    c2=Decimal(8)*Decimal(2).sqrt()/(5*pi*R**3*(Decimal(4).ln()*Decimal(2)/3).exp())
    # s^(11/3) = q^(-11), exact for s=q^(-3).
    s113=Decimal(1)/Decimal(q)**11
    c2_est=(c0*s*s+c1*s**3-data["lambda"])/s113
    d_scaled=data["d"]**3/m
    ratio_t=t/s
    return {"q":q,"s":str(s),"t_over_s":str(ratio_t),
            "d_cubed_over_m":str(d_scaled),"V":str(data["lambda"]),
            "c2_estimate":str(c2_est),"c2_predicted":str(c2),
            "H_R_residual":str(data["H"]),"rounded_screen_0_lt_d_lt_t":bool(0<data["d"]<t)}


def main():
    # Independent exact strip/cap coefficients; sqrt(2), pi stay symbolic.
    edge_integral=F(2,3)
    strip_cubic=F(1,3)
    vertex_cubic=F(2,3)
    if 4*edge_integral!=F(8,3) or 4*(strip_cubic+vertex_cubic)!=4:
        raise RuntimeError("strip/vertex symbolic coefficients differ")
    one_cap=F(4,3)*F(2,5)
    four_cap=4*one_cap
    cap_support_ratio=(four_cap/F(8,3))*2*F(1,4)
    if (one_cap,four_cap,cap_support_ratio)!=(F(8,15),F(32,15),F(2,5)):
        raise RuntimeError("cap leading ratio differs")
    with localcontext() as ctx:
        ctx.prec=85
        pi=decimal_pi()
        cases=[solve_case(q,pi) for q in (4,6,8,10)]
        print(json.dumps({
            "exact_four_edge_linear_moment_coefficient_sqrt2":str(4*edge_integral),
            "exact_four_edge_plus_vertex_cubic_coefficient_sqrt2":str(4*(strip_cubic+vertex_cubic)),
            "exact_one_cap_coefficient":str(one_cap),
            "exact_four_caps_coefficient":str(four_cap),
            "exact_cap_fraction_of_support_term":str(cap_support_ratio),
            "decimal_rounded_branch_cases":cases,
            "limits":"The finite-precision Decimal root diagnostics use the imported R-branch stationary formulas and do not prove the global optimizer, uniqueness, o-terms or novelty."
        },indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
