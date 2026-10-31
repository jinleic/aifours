# Finite exact NumPy int64 scan in the reviewer's Eval kernel, after f26 and
# frontier-review-f39-source-constraints-kernel-v1.py. No author code imported.
import numpy as f39_np

f39_labels=('sparse','closure')
f39_H={key:f39_np.array([f39_P[key][i] for i in range(1024)],dtype=f39_np.int64) for key in f39_labels}
f39_M=max(int(a.max()) for a in f39_H.values())
# Each conditional MI is <= 2M; |c|<=8M; 0<=d<=4M;
# a minimizer has n<=8M+1. All intermediates are safely below int64.
f39_safe=4*f39_M+2*(8*f39_M+1)*(8*f39_M)+(8*f39_M+1)*(8*f39_M+2)*(4*f39_M)
if f39_safe >= 2**63: raise ValueError('INT64_BOUND')

def f39_np_cmi(H,A,B,Z):
    return H[A|Z]+H[B|Z]-H[A|B|Z]-H[Z]

f39_stats={k:{'count':0,'min_twice_slack':None,'max_minimizer_n':0,'zero_d_count':0} for k in f39_labels}
f39_universe=6**10
f39_chunk=250000
for f39_start in range(0,f39_universe,f39_chunk):
    f39_codes=f39_np.arange(f39_start,min(f39_start+f39_chunk,f39_universe),dtype=f39_np.int64)
    f39_work=f39_codes.copy()
    f39_masks=[f39_np.zeros(f39_codes.size,dtype=f39_np.int64) for _ in range(5)]
    for f39_i in range(10):
        f39_digit=f39_work%6
        for f39_block in range(1,6): f39_masks[f39_block-1] |= (f39_digit==f39_block).astype(f39_np.int64)<<f39_i
        f39_work//=6
    f39_A,f39_B,f39_C,f39_D,f39_Z=f39_masks
    f39_selected=(f39_A>0)&(f39_B>0)&(f39_C>0)&(f39_D>0)&(f39_A<f39_B)
    f39_A,f39_B,f39_C,f39_D,f39_Z=(x[f39_selected] for x in f39_masks)
    for f39_key in f39_labels:
        f39_h=f39_H[f39_key]
        f39_a=f39_np_cmi(f39_h,f39_A,f39_B,f39_C|f39_Z)
        f39_Delta=f39_np_cmi(f39_h,f39_A,f39_B,f39_Z)-f39_np_cmi(f39_h,f39_A,f39_B,f39_D|f39_Z)-f39_np_cmi(f39_h,f39_C,f39_D,f39_Z)
        f39_d=f39_np_cmi(f39_h,f39_A,f39_C,f39_B|f39_Z)+f39_np_cmi(f39_h,f39_B,f39_C,f39_A|f39_Z)
        f39_c=f39_a-f39_Delta
        if f39_np.any(f39_d<0): raise ValueError('NEGATIVE_D')
        f39_zero=(f39_d==0)
        if f39_np.any(f39_zero & (f39_c<0)): raise ValueError('NEGATIVE_EVENTUAL_LINEAR')
        f39_den=f39_np.where(f39_zero,1,f39_d)
        # The first n>=1 with F_(n+1)-F_n=c+(n+1)d >=0.
        f39_n=f39_np.maximum(1,(f39_np.maximum(0,-f39_c)+f39_den-1)//f39_den-1)
        f39_n=f39_np.where(f39_zero,1,f39_n)
        f39_value=2*f39_a+2*f39_n*f39_c+f39_n*(f39_n+1)*f39_d
        if f39_np.any(f39_value<0):raise ValueError('NEGATIVE_FN')
        stats=f39_stats[f39_key]
        stats['count']+=int(f39_A.size)
        stats['zero_d_count']+=int(f39_zero.sum())
        if f39_A.size:
            minimum=int(f39_value.min()); largest=int(f39_n.max())
            if stats['min_twice_slack'] is None or minimum<stats['min_twice_slack']:stats['min_twice_slack']=minimum
            stats['max_minimizer_n']=max(stats['max_minimizer_n'],largest)
for f39_key in f39_labels:
    if f39_stats[f39_key]['count']!=13729980:raise ValueError('SUBSTITUTION_COUNT')
print('f39 all-order exact scan:',{'scale':f39_scale,'int64_magnitude_bound':f39_safe,'assignments_before_filters':f39_universe,'results':f39_stats})
