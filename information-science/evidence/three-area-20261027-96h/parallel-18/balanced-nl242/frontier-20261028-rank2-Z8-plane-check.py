#!/opt/homebrew/bin/python3
"""Formal sharpness controls for the rank-two eight-zero radical plane."""
import argparse
import collections
import json
import pathlib


def fw(a):
    a=list(a);s=1
    while s<len(a):
        for i in range(0,len(a),2*s):
            for j in range(i,i+s):x,y=a[j],a[j+s];a[j]=x+y;a[j+s]=x-y
        s*=2
    return a


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    r=json.loads(a.input.read_text());k=r['spectrum_k'];zero={x for x,v in enumerate(k) if v==0}
    basis=[3,12,20];S={0}
    for b in basis:S|={x^b for x in tuple(S)}
    assert zero==S and len(S)==8 and all(x<256 for x in S)
    q=[(v//2)%2 for v in k[:256]];assert q.count(0)==64
    assert all(q[x^y]==q[x] for x in range(256) for y in S)
    # Direct 6-variable minimum-support positive controls with leading cubic monomial.
    H=[int(x&7==0) for x in range(64)]
    assert sum(H)==8 and H[0]
    terms=H[:]
    for i in range(6):
        for x in range(64):
            if x&(1<<i):terms[x]^=terms[x^(1<<i)]
    assert max(i.bit_count() for i,v in enumerate(terms) if v)==3
    # The explicit formal placement meets the even-half equality, but is not Boolean.
    assert all(abs(k[x])==4 for x in range(256) if q[x]==0 and x not in S)
    assert all(abs(k[x])==6 for x in range(256) if q[x]==1)
    assert sum(v*v for v in k[:256])==64*122
    assert sum(v not in(-128,128) for v in fw(k))==497
    # Positive non-equality control: nonzero cubic supported on an affine 4-flat of size16.
    H16=[int(x&3==0) for x in range(64)];assert sum(H16)==16 and H16[0]
    changed=H[:];changed[0]=0;assert sum(changed)==7
    out={'scope':'exact even-half formal NON-WITNESS and min-support controls',
         'formal_zero_plane':sorted(S),'plane_basis':basis,'q_zero_count':64,
         'even_half_energy':sum(v*v for v in k[:256]),'formal_full_inverse_failures':497,
         'six_variable_degree3_sharp_support':8,'six_variable_degree2_larger_support':16,
         'one_point_mutation_below_minimum_support':7}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('rank2 radical Z8 plane and formal even-energy equality checked; NON-WITNESS')


if __name__=='__main__':main()
