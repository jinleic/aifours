# Exact bounded design search for a FOURTH rational contact. Fixed nominal
# center; the first three contacts run through an explicit 3x11x26 grid.
# No numerical roots, no scientific subprocess, no general impossibility claim.
from fractions import Fraction as Q
from math import isqrt
from itertools import product
four_counts={'triples':0,'odd_feasible':0,'even_feasible':0,'square_discriminant':0,'ordered_fourth':0,'positive_widths':0,'stable_999_over_1000':0,'candidates':[]}
for t1,t2,t3 in product(range(2,5),range(12,23),range(52,78)):
    ts=(Q(t1),Q(t2),Q(t3));four_counts['triples']+=1
    odd=quad_interpolate(ts,[abs(cx_eval(ct_O,t)) for t in ts])
    if not all(0<odd[j]<cx_center[2*j+1] for j in range(3)):continue
    four_counts['odd_feasible']+=1
    base=quad_interpolate(ts,[abs(cx_eval(ct_E,t)) for t in ts]);slope=quad_interpolate(ts,[-t**3 for t in ts]);allowed=(Q(0),cx_center[6])
    for j in range(3):
        allowed=open_bound(*allowed,base[j],slope[j],cx_center[2*j])
        if allowed is None:break
    if allowed is None:continue
    four_counts['even_feasible']+=1
    op=[cx_center[1]+odd[0],-cx_center[3]+odd[1],cx_center[5]+odd[2],Q(-1)]
    q=quotient_by_root(op,Q(t2));disc=q[1]**2-4*q[0]*q[2]
    if disc<0 or isqrt(disc.numerator)**2!=disc.numerator or isqrt(disc.denominator)**2!=disc.denominator:continue
    four_counts['square_discriminant']+=1
    rt=Q(isqrt(disc.numerator),isqrt(disc.denominator));roots=[(-q[1]+sign*rt)/(2*q[2]) for sign in (-1,1)]
    for t4 in roots:
        if not t1<t4<t2 or cx_eval(ct_E,t4)>=0:continue
        four_counts['ordered_fourth']+=1
        A=sum(base[j]*t4**j for j in range(3));B=sum(slope[j]*t4**j for j in range(3))+t4**3
        if not B:continue
        x=(abs(cx_eval(ct_E,t4))-A)/B
        ev=[base[j]+slope[j]*x for j in range(3)]+[x];h=[ev[0],odd[0],ev[1],odd[1],ev[2],odd[2],ev[3]]
        if not all(0<h[j]<cx_center[j] for j in range(7)):continue
        four_counts['positive_widths']+=1
        boundary=corners([cx_center[j]-h[j] for j in range(7)],[cx_center[j]+h[j] for j in range(7)])
        for ci,t in ((2,Q(t1)),(1,Q(t2)),(2,Q(t3)),(3,t4)):
            if parity(boundary[ci],t)!=(Q(0),Q(0)):raise ValueError('CONTACT')
        rho=Q(999,1000);actual=corners([cx_center[j]-rho*h[j] for j in range(7)],[cx_center[j]+rho*h[j] for j in range(7)])
        if not all(routh_ok(a) for a in actual):continue
        if not all(integer_hurwitz(a) for a in actual):raise ValueError('DET_MISMATCH')
        four_counts['stable_999_over_1000']+=1
        four_counts['candidates'].append({'contacts':[str(t1),str(t2),str(t3),str(t4)],'halfwidths':[str(v) for v in h]})
        break
print('four-contact rational bounded design:',four_counts)
