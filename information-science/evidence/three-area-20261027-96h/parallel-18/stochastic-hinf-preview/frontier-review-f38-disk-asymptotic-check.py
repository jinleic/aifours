#!/usr/bin/env python3
"""Independent exact arithmetic diagnostics for f38; no optimizer solver."""
from fractions import Fraction as F
import json


def add(*ps):
    out = {}
    for p in ps:
        for k,v in p.items():
            out[k] = out.get(k,F(0)) + v
    return {k:v for k,v in out.items() if v}


def mul(a,b):
    out = {}
    for x,v in a.items():
        for y,w in b.items():
            k = tuple(i+j for i,j in zip(x,y))
            out[k] = out.get(k,F(0)) + v*w
    return {k:v for k,v in out.items() if v}


def scale(p,c):
    return {k:v*F(c) for k,v in p.items() if v*c}


def main():
    # Polynomial variables (x,y,p), p being a formal pi. Verify the
    # factorization without setting pi to a numerical value.
    x={(1,0,0):F(1)}
    y={(0,1,0):F(1)}
    p={(0,0,1):F(1)}
    lhs=add(scale(mul(x,mul(y,y)),3), scale(mul(y,mul(y,y)),-3),
            scale(mul(p,y),4), scale(mul(p,x),-4))
    rhs=mul(add(x,scale(y,-1)),add(scale(mul(y,y),3),scale(p,-4)))
    if lhs!=rhs:
        raise RuntimeError("formal variational factorization failed")

    # Direct exact integration on the L1 unit diamond.
    area=4*(F(1)-F(1,2))
    one_axis=4*(F(1,3)-F(1,4))
    second_moment=2*one_axis
    if (area,second_moment)!=(F(2),F(2,3)):
        raise RuntimeError("diamond integral failed")

    # Explicit S=rD synthetic family: evaluate infinite layer sums using
    # closed geometric moments, entirely in rational arithmetic.
    rows=[]
    for denominator in (4,8,16):
        s=F(1,denominator)
        b=s**4
        r=s
        m0=1/(1-b)
        m1=b/(1-b)**2
        m2=b*(1+b)/(1-b)**3
        m3=b*(1+4*b+b*b)/(1-b)**4
        m4=b*(1+11*b+11*b*b+b**3)/(1-b)**5
        Z=2*(r*r*m0+2*r*m1+m2)
        N=F(2,3)*(r**4*m0+4*r**3*m1+6*r*r*m2+4*r*m3+m4)
        area0=2*r*r
        moment0=F(2,3)*r**4
        zerr=Z-area0-2*b
        nerr=N-moment0-F(2,3)*b
        denominator_error=b*r+b*b
        if not (0<=zerr<=100*denominator_error and 0<=nerr<=500*denominator_error):
            raise RuntimeError("synthetic exact layer bound failed")
        rows.append({"b":str(b),"r":str(r),
                     "normalizer_error_over_br_plus_b2":str(zerr/denominator_error),
                     "moment_error_over_br_plus_b2":str(nerr/denominator_error)})

    # Independent rational check of the radial trial at m=s^4, gamma=s.
    radial=[]
    for denominator in (4,8,16):
        s=F(1,denominator); m=s**4; g=s
        A=m+2*m*m; B=m+6*m*m+6*m**3; C=m+14*m*m+36*m**3+24*m**4
        D=g*g+2*m*g+A
        N=g**4+4*m*g**3+6*A*g*g+4*B*g+C
        w=N/(2*D)
        if abs(w-s*s)>4*s**3:
            raise RuntimeError("radial trial check failed")
        radial.append({"s":str(s),"(Wtrial-s^2)/s^3":str((w-s*s)/(s**3))})

    print(json.dumps({
        "formal_variational_factorization": "PASS: (x-y)(3y^2-4pi)",
        "diamond_area":str(area),"diamond_euclidean_second_moment":str(second_moment),
        "synthetic_diamond_core_exact_layer_checks":rows,
        "radial_trial_exact_checks":radial,
        "limits":"Synthetic S=rD is NOT the true optimizer; finite rational checks do not prove uniform big-O, shape convergence or the imported all-law theorem."
    },indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
