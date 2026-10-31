# Exact bounded design search for three simultaneous stability-boundary gaps.
# The selected nominal center is (s+1)prod_{v=2,4,8}((s+1)^2+v^2).
# At three rational frequencies, interpolate independent coefficient halfwidths
# so both parity intervals reach zero. A uniformly shrunk box is checked using
# actual corners. A grid miss is NOT a general obstruction.
from fractions import Fraction as Q
from itertools import product

def quad_interpolate(xs,ys):
    coeff=[Q(0),Q(0),Q(0)]
    for i in range(3):
        j,k=[v for v in range(3) if v!=i];den=(xs[i]-xs[j])*(xs[i]-xs[k]);v=ys[i]/den
        coeff[0]+=v*xs[j]*xs[k];coeff[1]-=v*(xs[j]+xs[k]);coeff[2]+=v
    return coeff

def open_bound(lo,hi,base,slope,upper):
    if slope==0:return (lo,hi) if 0<base<upper else None
    a=-base/slope;b=(upper-base)/slope
    if a>b:a,b=b,a
    lo=max(lo,a);hi=min(hi,b)
    return (lo,hi) if lo<hi else None

E=[cx_center[0],-cx_center[2],cx_center[4],-cx_center[6]]
O=[cx_center[1],-cx_center[3],cx_center[5],Q(-1)]
eis=cx_isolate(E);ois=cx_isolate(O)
grid=[list(map(Q,(2,3,4))),list(map(Q,(13,15,17,19,21))),list(map(Q,(55,60,65,70,75)))]
for i in range(3):
    if not all(eis[i][1]<t<ois[i][0] for t in grid[i]):raise ValueError('TARGET_OUTSIDE_GAP')
threegap={'tested':0,'odd_feasible':0,'even_feasible':0,'shrunk_stable':0,'candidates':[]}
for xs in product(*grid):
    threegap['tested']+=1
    yo=[abs(cx_eval(O,t)) for t in xs];odd=quad_interpolate(xs,yo)
    if not all(0<odd[k]<cx_center[2*k+1] for k in range(3)):continue
    threegap['odd_feasible']+=1
    ye=[abs(cx_eval(E,t)) for t in xs];base=quad_interpolate(xs,ye)
    derivative=quad_interpolate(xs,[-t**3 for t in xs]);bound=(Q(0),cx_center[6])
    for k in range(3):
        bound=open_bound(*bound,base[k],derivative[k],cx_center[2*k])
        if bound is None:break
    if bound is None:continue
    threegap['even_feasible']+=1
    h6=sum(bound)/2;even=[base[k]+derivative[k]*h6 for k in range(3)]+[h6]
    h=[even[0],odd[0],even[1],odd[1],even[2],odd[2],even[3]]
    if not all(0<h[j]<cx_center[j] for j in range(7)):raise ValueError('HALFWIDTH')
    for i,t in enumerate(xs):
        if sum(even[k]*t**k for k in range(4))!=abs(cx_eval(E,t)) or sum(odd[k]*t**k for k in range(3))!=abs(cx_eval(O,t)):raise ValueError('TARGET_EQUALITY')
    scale=Q(999,1000);lo=[cx_center[j]-scale*h[j] for j in range(7)];hi=[cx_center[j]+scale*h[j] for j in range(7)]
    stable=all(routh_ok(a) for a in corners(lo,hi))
    if stable:
        if not all(integer_hurwitz(a) for a in corners(lo,hi)):raise ValueError('DETERMINANT_REPLAY')
        threegap['shrunk_stable']+=1
        threegap['candidates'].append({'points':[str(t) for t in xs],'halfwidth':[str(v) for v in h],'scale':str(scale),
                                       'lower':[str(v) for v in lo],'upper':[str(v) for v in hi]})
        break
print('three-gap design exact bounded result:',threegap)
