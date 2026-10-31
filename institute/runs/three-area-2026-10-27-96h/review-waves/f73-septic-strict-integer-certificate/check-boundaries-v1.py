#!/usr/bin/env python3
"""Independent exact replays: interpolation, collapsed rectangles, repeated roots."""
from fractions import Fraction as Q
from math import comb
import json


def check(ok, message):
    if not ok:
        raise RuntimeError(message)


def polynomial_mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def eval_parts(a, w):
    real = sum(a[k] * (-1)**(k//2) * w**k for k in range(0, len(a), 2))
    imag = sum(a[k] * (-1)**((k-1)//2) * w**k for k in range(1, len(a), 2))
    return real, imag


def solve(a, b):
    n = len(b)
    augmented = [[Q(x) for x in row] + [Q(y)] for row, y in zip(a, b)]
    for k in range(n):
        pivot = next((i for i in range(k,n) if augmented[i][k]), None)
        check(pivot is not None, 'interpolation matrix singular')
        augmented[k], augmented[pivot] = augmented[pivot], augmented[k]
        d = augmented[k][k]
        augmented[k] = [x / d for x in augmented[k]]
        for i in range(n):
            if i != k:
                d = augmented[i][k]
                augmented[i] = [x-d*y for x,y in zip(augmented[i],augmented[k])]
    return [row[-1] for row in augmented]


def corner(lo, hi, ev, od):
    a = []
    for j in range(7):
        upper = (j//2) % 2 ^ (ev if j%2 == 0 else od)
        a.append(hi[j] if upper else lo[j])
    return a + [Q(1)]


def values(a, t):
    return (a[0] - a[2]*t + a[4]*t*t - a[6]*t*t*t,
            a[1] - a[3]*t + a[5]*t*t - t*t*t)


def vector(a, x):
    return [sum(((-1 if ((k-j)//2)%2 else 1) * a[j] * x**((j+k)//2) *
                 (1-x)**(7-(j+k)//2)) for j in range(8) if (j+k)%2 == 0)
            for k in range(8)]


def trim(a):
    a = [Q(x) for x in a]
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a


def divmod_poly(a,b):
    a,b = trim(a),trim(b)
    check(b != [0], 'zero polynomial divisor')
    q = [Q(0)] * max(1, len(a)-len(b)+1)
    while a != [0] and len(a)>=len(b):
        d = len(a)-len(b)
        c = a[-1]/b[-1]
        q[d] += c
        for k,x in enumerate(b):
            a[k+d] -= c*x
        a = trim(a)
    return trim(q),a


def derivative(a):
    return trim([k*a[k] for k in range(1,len(a))] or [0])


def gcd_poly(a,b):
    a,b = trim(a),trim(b)
    while b != [0]:
        _,r=divmod_poly(a,b)
        a,b=b,r
    return trim([v/a[-1] for v in a])


def sturm_distinct_positive(a):
    a = trim(a)
    check(a != [0], 'zero polynomial is identically zero, not root-countable')
    gcd=gcd_poly(a,derivative(a))
    squarefree,rem=divmod_poly(a,gcd)
    check(rem == [0], 'squarefree division failed')
    sequence=[squarefree]
    d=derivative(squarefree)
    if d != [0]:
        sequence.append(d)
        while True:
            _,r=divmod_poly(sequence[-2],sequence[-1])
            if r == [0]:
                break
            sequence.append([-v for v in r])
    def variations(vals):
        signs=[1 if v>0 else -1 for v in vals if v!=0]
        return sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))
    # This routine is used only when a(0) != 0; +infinity takes leading signs.
    check(a[0] != 0, 'zero-frequency root requires a separate endpoint test')
    return variations([x[0] for x in sequence])-variations([x[-1] for x in sequence]),squarefree


def main():
    center=[comb(7,j)*10**(7-j) for j in range(8)]
    lo=[Q(v-1) for v in center[:7]]
    hi=[Q(v+1) for v in center[:7]]
    denominators=[]
    for u,v in [(1,1),(-1,1),(1,-1)]:
        a=list(map(Q,center))
        a[0]+=u
        a[1]+=v
        check(all(lo[j]<=a[j]<=hi[j] for j in range(7)), 'interpolation member outside one box')
        denominators.append(a)
    zero_a=Q(center[0]-1)
    interpolation=[]
    for m in range(4):
        for zero in (0,1):
            for infinity in (0,1):
                if m+zero+infinity==0:
                    continue
                q=2*m+zero
                rows=[]
                rhs=[]
                for j,w in enumerate(range(1,m+1)):
                    target=eval_parts(denominators[j],w)
                    rows.append([(-1)**(k//2)*w**k if k%2==0 else 0 for k in range(q)])
                    rows.append([(-1)**((k-1)//2)*w**k if k%2 else 0 for k in range(q)])
                    rhs.extend(target)
                if zero:
                    rows.append([int(k==0) for k in range(q)])
                    rhs.append(zero_a)
                c=solve(rows,rhs) if q else []
                b=c+[Q(0)]*(8-len(c))
                if infinity:
                    R=[Q(0),Q(1)] if zero else [Q(1)]
                    for w in range(1,m+1):
                        R=polynomial_mul(R,[Q(w*w),Q(0),Q(1)])
                    shifted=[Q(0)]*(7-q)+R
                    b=[x+y for x,y in zip(b,shifted)]
                    check(len(shifted)==8 and b[7]==1, 'infinity correction')
                for j,w in enumerate(range(1,m+1)):
                    ar,ai=eval_parts(denominators[j],w)
                    br,bi=eval_parts(b,w)
                    check((br,bi)==(ar,ai), 'finite interpolation values')
                    check(br*ar+bi*ai==ar*ar+ai*ai>0, 'finite interpolation pairing')
                if zero:
                    check(b[0]==zero_a and b[0]*zero_a>0, 'zero interpolation')
                interpolation.append({'positive_nodes':m,'zero':bool(zero),'infinity':bool(infinity),
                                      'q':q,'positive_at_all_listed_atoms':True})

    box_modes={'full_width':[], 'even_collapsed':[0,2,4,6], 'odd_collapsed':[1,3,5],
               'fully_collapsed':list(range(7)), 'a0_collapsed':[0]}
    rectangle_cases=[]
    for mode, collapsed in box_modes.items():
        high=hi[:]
        for j in collapsed:
            high[j]=lo[j]
        actual=[l+(u-l)/3 for l,u in zip(lo,high)]+[Q(1)]
        cs=[corner(lo,high,ev,od) for ev,od in ((0,0),(0,1),(1,0),(1,1))]
        for t in map(Q,(0,1,4,9)):
            e,o=values(actual,t)
            emin,omin=values(cs[0],t)
            emax,_=values(cs[2],t)
            _,omax=values(cs[1],t)
            check(emin<=e<=emax and omin<=o<=omax, 'actual value not in rectangle')
            alpha=(e-emin)/(emax-emin) if emax!=emin else Q(0)
            beta=(o-omin)/(omax-omin) if omax!=omin else Q(0)
            weights=[(1-alpha)*(1-beta),(1-alpha)*beta,alpha*(1-beta),alpha*beta]
            check(sum(weights)==1 and all(w>=0 for w in weights), 'invalid convex weights')
            x=t/(1+t)
            target=vector(actual,x)
            result=[sum(w*vector(a,x)[k] for w,a in zip(weights,cs)) for k in range(8)]
            check(target==result,'actual corner functional hull')
        check(all(vector(a,Q(1)) == [0]*7+[1] for a in cs+[actual]), 'infinity corner collapse')
        rectangle_cases.append({'mode':mode,'finite_t':[0,1,4,9],'infinity':True,'exact':True})

    repeated=polynomial_mul(polynomial_mul([-1,1],[-1,1]), polynomial_mul(polynomial_mul([1,1],[1,1]),polynomial_mul(polynomial_mul([1,1],[1,1]),[1,1])))
    roots,squarefree=sturm_distinct_positive(repeated)
    check(repeated[0]==1 and repeated[-1]==1 and roots==1, 'even-multiplicity Sturm control')
    check(eval_parts([],Q(1))==(0,0), 'empty polynomial arithmetic control')
    # p(t)=t(1+t)^6: p(0)=0, so the endpoint test must reject before the positive-root count.
    zero_at_origin=polynomial_mul([0,1],polynomial_mul(polynomial_mul([1,1],[1,1]),polynomial_mul(polynomial_mul([1,1],[1,1]),polynomial_mul([1,1],[1,1]))))
    check(zero_at_origin[0]==0 and zero_at_origin[-1]==1, 'zero endpoint polynomial')
    print(json.dumps({'result':'EXACT_BOUNDARY_CONTROLS_PASSED',
        'interpolation_cases':interpolation,
        'corner_convex_hull_cases':rectangle_cases,
        'repeated_root_control':{'P':'(t-1)^2(t+1)^5','P_at_zero':str(repeated[0]),
           'leading_coefficient':str(repeated[-1]),'distinct_positive_roots':roots,
           'squarefree_coefficients_ascending':[str(x) for x in squarefree],
           'why_rejected':'positive root at t=1 despite even multiplicity and no sign change'},
        'zero_frequency_control':{'P':'t(t+1)^6','P_at_zero':str(zero_at_origin[0]),
           'why_rejected':'endpoint strictness fails at t=0'},
        'limits':'Finite exact replays only, not a general proof or negative-witness search.'}, indent=2,sort_keys=True))


if __name__=='__main__':
    main()
