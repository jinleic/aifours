# Bounded rational root-bracket discovery for the four parity cubics.
from fractions import Fraction as Q
cx_root_poly={'E-':[cx_lo[0],-cx_hi[2],cx_lo[4],-cx_hi[6]],'E+':[cx_hi[0],-cx_lo[2],cx_hi[4],-cx_lo[6]],
              'O-':[cx_lo[1],-cx_hi[3],cx_lo[5],Q(-1)],'O+':[cx_hi[1],-cx_lo[3],cx_hi[5],Q(-1)]}
def cx_eval(poly,t):
    out=Q(0)
    for c in poly[::-1]:out=out*t+c
    return out
def cx_isolate(poly):
    intervals=[];left=Q(0);lv=cx_eval(poly,left);step=Q(1,100)
    for j in range(1,25601):
        right=j*step;rv=cx_eval(poly,right)
        if rv==0:
            a=right-step/10000;b=right+step/10000
            if cx_eval(poly,a)*cx_eval(poly,b)>=0:raise ValueError('ROOT_GRID')
            intervals.append((a,b))
        elif lv and lv*rv<0:intervals.append((left,right))
        if len(intervals)==3:break
        left=right;lv=rv
    if len(intervals)!=3:raise ValueError('ROOT_COUNT')
    refined=[]
    for left,right in intervals:
        for k in range(28):
            mid=(left+right)/2;v=cx_eval(poly,mid)
            if v==0:left=mid-(right-left)/8;right=mid+(right-left)/8
            elif cx_eval(poly,left)*v<0:right=mid
            else:left=mid
        if cx_eval(poly,left)*cx_eval(poly,right)>=0:raise ValueError('ROOT_REFINE')
        refined.append((left,right))
    return refined
cx_intervals={key:cx_isolate(p) for key,p in cx_root_poly.items()}
cx_bands=[]
for j in range(3):
    for parity in ('E','O'):
        cx_bands.append((min(cx_intervals[parity+'-'][j][0],cx_intervals[parity+'+'][j][0]),max(cx_intervals[parity+'-'][j][1],cx_intervals[parity+'+'][j][1])))
if any(cx_bands[j][1]>=cx_bands[j+1][0] for j in range(5)):raise ValueError('BAND_CROSSING')
print('complex-box rational root bands:',[(str(a),str(b)) for a,b in cx_bands])
