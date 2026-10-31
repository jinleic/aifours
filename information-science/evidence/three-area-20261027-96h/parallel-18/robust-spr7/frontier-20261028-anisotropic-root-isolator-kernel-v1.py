# Exact root-band discovery for the chosen actual rational box; Eval only.
# Uses no numerical roots, no author checker, and no scientific subprocess.
from fractions import Fraction as Q

def root_val(p,t):
    z=Q(0)
    for x in reversed(p):z=z*t+x
    return z

def isolate_three(p):
    step=Q(1,100); intervals=[]; left=Q(0);vleft=root_val(p,left)
    for k in range(1,2001):
        right=k*step;vright=root_val(p,right)
        if vright==0:
            l=right-Q(1,1000000);r=right+Q(1,1000000)
            if root_val(p,l)*root_val(p,r)>=0:raise ValueError('EXACT_GRID_ROOT_BRACKET')
            intervals.append((l,r))
        elif vleft and vleft*vright<0:
            intervals.append((left,right))
        left=right;vleft=vright
    if len(intervals)!=3:raise ValueError('ROOT_DISCOVERY_COUNT')
    out=[]
    for left,right in intervals:
        for _ in range(28):
            mid=(left+right)/2; vm=root_val(p,mid)
            if vm==0:
                left=mid-(right-left)/8;right=mid+(right-left)/8
                if root_val(p,left)*root_val(p,right)>=0:raise ValueError('DYADIC_ROOT_BRACKET')
            elif root_val(p,left)*vm<0:right=mid
            else:left=mid
        out.append((left,right))
    return out

root_polys={'E-':[lo[0],-hi[2],lo[4],-hi[6]],'E+':[hi[0],-lo[2],hi[4],-lo[6]],
            'O-':[lo[1],-hi[3],lo[5],Q(-1)],'O+':[hi[1],-lo[3],hi[5],Q(-1)]}
root_intervals={key:isolate_three(poly) for key,poly in root_polys.items()}
root_bands=[]
for i in range(3):
    for k in ('E','O'):
        root_bands.append((min(root_intervals[k+'-'][i][0],root_intervals[k+'+'][i][0]),
                           max(root_intervals[k+'-'][i][1],root_intervals[k+'+'][i][1])))
if any(root_bands[i][1]>=root_bands[i+1][0] for i in range(5)):raise ValueError('BANDS_NOT_SEPARATED')
print('exact common root bands:',[(str(x),str(y)) for x,y in root_bands])
