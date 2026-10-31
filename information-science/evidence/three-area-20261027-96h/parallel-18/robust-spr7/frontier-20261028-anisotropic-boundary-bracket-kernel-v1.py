# Exact bounded stability bracketing for nested anisotropic boxes: six widths
# share r, s^6 width is 1/2. Python Eval only; no numerical roots or subprocess.
def make_wide_box(r):
    factors=[r]*6+[Q(1,2)]
    mid=[(x+y)/2 for x,y in zip(ray_base_lo,ray_base_hi)]
    rad=[factors[j]*(ray_base_hi[j]-ray_base_lo[j])/2 for j in range(7)]
    return [x-y for x,y in zip(mid,rad)],[x+y for x,y in zip(mid,rad)]
def exact_stability(r):
    lower,upper=make_wide_box(r)
    if not all(0<x<y for x,y in zip(lower,upper)):return {'r':str(r),'stable':False,'reason':'NONPOSITIVE_OR_DEGENERATE'}
    vertices=corners(lower,upper)
    rs=[routh_ok(a) for a in vertices];ds=[integer_hurwitz(a) for a in vertices]
    if rs!=ds:raise ValueError('STABILITY_REPLAY_MISMATCH')
    return {'r':str(r),'stable':all(rs),'corner_hurwitz':rs}

bracket_records=[];stable_r=Q(21,20);unstable_r=None
for test in [Q(11,10),Q(6,5),Q(5,4),Q(3,2),Q(2)]:
    rec=exact_stability(test);bracket_records.append(rec)
    if rec['stable']:stable_r=test
    else:unstable_r=test;break
if unstable_r is not None:
    for i in range(5):
        mid=(stable_r+unstable_r)/2;rec=exact_stability(mid);bracket_records.append(rec)
        if rec['stable']:stable_r=mid
        else:unstable_r=mid
print('anisotropic exact stability bracket:',{'records':bracket_records,'largest_checked_stable':str(stable_r),
 'smallest_checked_unstable':str(unstable_r) if unstable_r is not None else None,
 'bounded_bisections':5 if unstable_r is not None else 0})
