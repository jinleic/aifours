#!/opt/homebrew/bin/python3
"""Construct and audit a labelled ten-zero non-witness with several exact filters."""
import argparse
import collections
import importlib.util
import json
import math
import pathlib


def load(name, module):
    p=pathlib.Path(__file__).with_name(name)
    spec=importlib.util.spec_from_file_location(module,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m


def main():
    p=argparse.ArgumentParser();p.add_argument('--counts',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    lift=load('frontier-20261028-tenzero-mod8-lift-check.py','lift')
    counts=json.loads(args.counts.read_text(encoding='utf-8'));A={int(t):v for t,v in counts['histogram'].items()}
    simplex={0,1,2,7,11,31,47,63}
    def q6(x):return sum(((x>>i)&1)*((x>>(i+1))&1) for i in (0,2,4))%2
    def q8(x):return q6(x&63)^(((x>>6)&1)*((x>>7)&1))
    D={x for x in range(64) if q6(x)^((12&x).bit_count()%2)^1}
    slices=[simplex,simplex,simplex,simplex^D]
    h=[int((x&63) in slices[x>>6]) for x in range(256)]
    Q=[q8(x)^(x&1)^1 for x in range(256)]
    assert sum(h)==46 and sum(Q)==136 and sum(u*v for u,v in zip(h,Q))==24
    h_anf=h[:]
    for j in range(8):
        for x in range(256):
            if x&(1<<j):h_anf[x]^=h_anf[x^(1<<j)]
    assert all(not v or x.bit_count()<=4 for x,v in enumerate(h_anf))
    assert [x for x,v in enumerate(h_anf) if v and x.bit_count()==4]==[15,51,60,195,204,240]
    q=[lift.g0(x)%2 for x in range(256)]
    g=[(lift.g0(x)+2*lift.h(x))%4 for x in range(256)]
    assert len(lift.Z)==10 and {x for x in range(256) if g[x]==0}==lift.Z and 0 in lift.Z
    k=[0]*512
    def put(indices,dist,offset=0):
        assert len(indices)==sum(n for _,n in dist)
        pos=0
        for val,n in dist:
            for i in indices[pos:pos+n]:k[i+offset]=val
            pos+=n
    put([x for x in range(256) if g[x]==2],[(-4,A[-4]),(4,A[4])])
    put([x for x in range(256) if g[x]==1],[(-6,A[-6]),(2,A[2])])
    put([x for x in range(256) if g[x]==3],[(-2,A[-2]),(6,A[6])])
    put([x for x in range(256) if Q[x]==0 and h[x]==0],[(-7,A[-7]),(1,A[1])],256)
    put([x for x in range(256) if Q[x]==0 and h[x]==1],[(-3,A[-3]),(5,A[5])],256)
    put([x for x in range(256) if Q[x]==1 and h[x]==0],[(-1,A[-1]),(7,A[7])],256)
    put([x for x in range(256) if Q[x]==1 and h[x]==1],[(-5,A[-5]),(3,A[3])],256)
    assert k[0]==0 and collections.Counter(k[1:])==collections.Counter(A)
    assert max(map(abs,k))==7 and sum(k)==128 and sum(v*v for v in k)==16384
    assert all(((k[x]//2)%4)==g[x] for x in range(256))
    assert all((k[256+x]%4==3)==bool(Q[x]) for x in range(256))
    assert all((abs(k[256+x]) not in (1,7))==bool(h[x]) for x in range(256))
    assert all((g[x]%2)==q[x] for x in range(256))
    # Exact full correlations and inverse character sums, not a witness verifier shortcut.
    corrs=[sum(k[a]*k[a^s] for a in range(512)) for s in range(1,512)]
    inv=[sum((-1 if ((a&x).bit_count()%2) else 1)*k[a] for a in range(512)) for x in range(512)]
    assert inv[0]==128 and any(v not in (-128,128) for v in inv)
    assert any(corrs)
    result={'scope':'labelled formal spectrum satisfying listed filters; NON-WITNESS',
            'T_coordinate':256,'k_values':k,'zero_positions':[x for x,v in enumerate(k) if v==0],
            'odd_Q_weight':sum(Q),'peakunit_weight':sum(1-v for v in h),
            'phase_intersection':sum(u*v for u,v in zip(h,Q)),
            'even_mod8_and_cubic_all_256_checked':True,'odd_quadratic_and_quartic_all_256_checked':True,
            'histogram_matches_scalar_dual_model':True,'k_sum':sum(k),'k_square_sum':sum(v*v for v in k),
            'nonzero_shift_correlation_failures':sum(v!=0 for v in corrs),
            'max_abs_nonzero_shift_correlation':max(map(abs,corrs)),
            'inverse_not_plus_minus_128':sum(v not in (-128,128) for v in inv),
            'inverse_min':min(inv),'inverse_max':max(inv),
            'all_511_correlation_sums':corrs,'all_512_inverse_sums':inv}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('formal non-witness:',result['nonzero_shift_correlation_failures'],'correlation failures;',
          result['inverse_not_plus_minus_128'],'inverse failures',flush=True)


if __name__=='__main__':main()
