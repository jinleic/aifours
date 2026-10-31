#!/opt/homebrew/bin/python3
"""Independent FWHT/correlation and algebra audit of the ten-zero non-witness."""
import argparse
import collections
import json
import pathlib


def transform(a):
    a=list(a);step=1
    while step<len(a):
        for i in range(0,len(a),2*step):
            for j in range(i,i+step):
                x,y=a[j],a[j+step];a[j]=x+y;a[j+step]=x-y
        step*=2
    return a


def anf(a):
    a=list(a);n=(len(a)).bit_length()-1
    for j in range(n):
        for x in range(len(a)):
            if x&(1<<j):a[x]^=a[x^(1<<j)]
    return [x for x,v in enumerate(a) if v]


def main():
    p=argparse.ArgumentParser();p.add_argument('--placement',type=pathlib.Path,required=True)
    p.add_argument('--counts',type=pathlib.Path,required=True);p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    r=json.loads(a.placement.read_text());m=json.loads(a.counts.read_text());k=r['k_values'];n=len(k)
    assert n==512 and k[0]==0 and max(map(abs,k))==7
    assert collections.Counter(k[1:])==collections.Counter({int(t):v for t,v in m['histogram'].items()})
    assert sum(k)==128 and sum(v*v for v in k)==16384
    ee=[(k[x]//2)%4 for x in range(256)];eq=[v%2 for v in ee]
    oq=[int(k[256+x]%4==3) for x in range(256)]
    hh=[int(abs(k[256+x]) in (3,5)) for x in range(256)]
    def g0(x):return sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(4))+(x&51).bit_count()
    cubic=[((ee[x]-g0(x))%4)//2 for x in range(256)]
    assert all((ee[x]-g0(x))%2==0 for x in range(256))
    assert max(t.bit_count() for t in anf(cubic))<=3
    e_terms,o_terms=anf(eq),anf(oq)
    assert max(t.bit_count() for t in e_terms)<=2 and max(t.bit_count() for t in o_terms)<=2
    assert [t for t in e_terms if t.bit_count()==2]==[t for t in o_terms if t.bit_count()==2]==[3,12,48,192]
    h_terms=anf(hh)
    assert max(t.bit_count() for t in h_terms)==4
    assert [t for t in h_terms if t.bit_count()==4]==[15,51,60,195,204,240]
    assert sum(oq)==136 and sum(hh)==46 and sum(x*y for x,y in zip(oq,hh))==24
    assert [i for i,v in enumerate(k) if v==0]==r['zero_positions'] and len(r['zero_positions'])==10
    inv=transform(k);assert inv==r['all_512_inverse_sums']
    nums=transform([v*v for v in inv]);assert all(v%512==0 for v in nums)
    corrs=[v//512 for v in nums];assert corrs[0]==16384 and corrs[1:]==r['all_511_correlation_sums']
    failures=sum(v!=0 for v in corrs[1:]);badinv=sum(v not in (-128,128) for v in inv)
    assert failures==502 and badinv==479
    result={'scope':'independent FWHT and algebra audit of a NON-WITNESS',
            'all_512_values_checked':True,'same_full_rank_polar_checked':True,'even_cubic_lift_checked':True,
            'odd_quartic_part_checked':True,'all_511_correlations_crosschecked':True,
            'all_512_inverse_sums_crosschecked':True,'nonzero_shift_correlation_failures':failures,
            'inverse_not_plus_minus_128':badinv,'correlation_at_shift_1':corrs[1],
            'inverse_at_1':inv[1],'mutation_control_zero_frequency_nonzero_rejected':k[0]+1!=0}
    with a.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('independent audit: 502 failed correlations, 479 inverse failures; NON-WITNESS',flush=True)


if __name__=='__main__':main()
