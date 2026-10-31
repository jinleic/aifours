#!/opt/homebrew/bin/python3
"""Independent direct-transform and polar audit of a D28 non-witness."""
import argparse
import json
import pathlib


def fw(a):
    a=list(a);s=1
    while s<len(a):
        for i in range(0,len(a),2*s):
            for j in range(i,i+s):x,y=a[j],a[j+s];a[j]=x+y;a[j+s]=x-y
        s*=2
    return a


def rank(rows):
    b={}
    for v in rows:
        while v:
            i=v.bit_length()-1
            if i in b:v^=b[i]
            else:b[i]=v;break
    return len(b)


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,required=True);p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    r=json.loads(a.input.read_text());k=r['spectrum_k'];assert len(k)==512 and k[0]==0
    direct=[sum(k[x]*(-1 if ((x&y).bit_count()%2) else 1) for x in range(512)) for y in range(512)]
    assert direct==fw(k)
    W2=fw([v*v for v in direct]);assert all(v%512==0 for v in W2)
    corr=[v//512 for v in W2];assert corr[0]==16384
    assert sum(v!=0 for v in corr[1:])==r['nonzero_correlation_failures']==511
    assert corr[1]==r['correlation_at_1']==8032 and sum(v not in(-128,128) for v in direct)==r['full_inverse_not_sign_count']==497
    e=[(v//2)%2 for v in k[:256]];o=[int(v%4==3) for v in k[256:]]
    def pol(vals):return [[vals[0]^vals[1<<i]^vals[1<<j]^vals[(1<<i)^(1<<j)] for j in range(8)] for i in range(8)]
    P=pol(e);assert P==pol(o)
    for vals in (e,o):
        for x in range(256):
            for i in range(8):
                for j in range(8):assert vals[x]^vals[x^(1<<i)]^vals[x^(1<<j)]^vals[x^(1<<i)^(1<<j)]==P[i][j]
    rows=[sum(P[i][j]<<j for j in range(8)) for i in range(8)];assert rank(rows)==2 and e.count(0)==64
    h=[int(abs(v) in (3,5)) for v in k[256:]];aa=h[:]
    for i in range(8):
        for x in range(256):
            if x&(1<<i):aa[x]^=aa[x^(1<<i)]
    assert max(i.bit_count() for i,v in enumerate(aa) if v)==7
    zeros=[i for i,v in enumerate(k) if not v];assert zeros==r['zero_positions'] and len(zeros)==8
    assert sum(k)==128 and sum(v*v for v in k)==16384 and sum(v*v for v in k[:256])==64*122
    out={'scope':'independent audit of D28 NON-WITNESS', 'direct_inverse_agrees_with_fwht':True,
         'autocorrelations_crosschecked_by_inverse_square':True,'polar_rank':2,'q_zero_count':64,
         'all_even_odd_second_derivatives_checked':True,'odd_h_degree':7,'Walsh_zero_count':8,
         'full_inverse_not_sign_count':497,'nonzero_correlation_failures':511,'correlation_at_1':8032}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('independent D28 audit: rank2, cubic failure, 497 inverse and 511 correlation failures')


if __name__=='__main__':main()
