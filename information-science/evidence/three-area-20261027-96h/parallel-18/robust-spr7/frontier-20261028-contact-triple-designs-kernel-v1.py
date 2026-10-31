# Complete bounded 3x5x5 rational contact-grid design, not a general search.
# No solver or scientific subprocess; exact root-gap markers and Routh tests.
from fractions import Fraction as Q
from itertools import product
ct_E=[cx_center[0],-cx_center[2],cx_center[4],-cx_center[6]]
ct_O=[cx_center[1],-cx_center[3],cx_center[5],Q(-1)]
ct_grid=[list(map(Q,(2,3,4))),list(map(Q,(13,15,17,19,21))),list(map(Q,(55,60,65,70,75)))]
ct_results={'tested':0,'odd_feasible':0,'even_feasible':0,'stable_at_999_over_1000':0,'unstable_at_999_over_1000':0,'candidates':[]}
for xpts in product(*ct_grid):
    ct_results['tested']+=1
    odd=quad_interpolate(xpts,[abs(cx_eval(ct_O,t)) for t in xpts])
    if not all(0<odd[j]<cx_center[2*j+1] for j in range(3)):continue
    ct_results['odd_feasible']+=1
    base=quad_interpolate(xpts,[abs(cx_eval(ct_E,t)) for t in xpts]);der=quad_interpolate(xpts,[-t**3 for t in xpts]);allowed=(Q(0),cx_center[6])
    for j in range(3):
        allowed=open_bound(*allowed,base[j],der[j],cx_center[2*j])
        if allowed is None:break
    if allowed is None:continue
    ct_results['even_feasible']+=1
    h6=sum(allowed)/2;ev=[base[j]+der[j]*h6 for j in range(3)]+[h6];widths=[ev[0],odd[0],ev[1],odd[1],ev[2],odd[2],ev[3]]
    if not all(0<widths[j]<cx_center[j] for j in range(7)):raise ValueError('WIDTH')
    for t in xpts:
        if sum(ev[j]*t**j for j in range(4))!=abs(cx_eval(ct_E,t)) or sum(odd[j]*t**j for j in range(3))!=abs(cx_eval(ct_O,t)):raise ValueError('TARGET')
    rho=Q(999,1000);lo=[cx_center[j]-rho*widths[j] for j in range(7)];hi=[cx_center[j]+rho*widths[j] for j in range(7)];a=corners(lo,hi)
    good=all(routh_ok(v) for v in a)
    if good:
        if not all(integer_hurwitz(v) for v in a):raise ValueError('MINOR_MISMATCH')
        ct_results['stable_at_999_over_1000']+=1
        ct_results['candidates'].append({'contacts':[str(t) for t in xpts],'halfwidths':[str(v) for v in widths]})
    else:ct_results['unstable_at_999_over_1000']+=1
print('bounded contact-design census:',ct_results)
