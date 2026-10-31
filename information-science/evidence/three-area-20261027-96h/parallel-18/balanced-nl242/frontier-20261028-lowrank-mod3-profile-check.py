#!/opt/homebrew/bin/python3
"""Exact integer enumeration for the universal mod-3 signed-switch refinement."""
import argparse
import collections
import json
import pathlib


def enumerate_profiles(rank):
    N=1<<rank;mmax=122 if rank==2 else 112
    Ds=range(12,29,4) if rank==2 else range(8,25,2)
    rows=[]
    for D in Ds:
        choices={a-b for a in range(N+1) for b in range(N+1-a) if (a+2*b)%3==(1-2*D)%3}
        for S in sorted(choices):
            m=116+D//2+(2 if rank==2 else 1)*S
            if m%2 or m>mmax or m<0:continue
            for n1 in range(D+1):
                n3=D-n1;hnum=8*(m-60)-2*D-4*n1
                if hnum%3:continue
                h=hnum//3;n5=h-n3;n7=256-h-n1
                if min(n3,n5,n7)<0:continue
                rows.append({'D':D,'m':m,'S':S,'n1':n1,'n3':n3,'n5':n5,'n7':n7})
    return rows


def main():
    p=argparse.ArgumentParser();p.add_argument('--placement',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    tables={r:enumerate_profiles(r) for r in (2,4)}
    assert len(tables[2])==30 and {x['D'] for x in tables[2]}=={12,16,20,28}
    assert {x['m'] for x in tables[2]}=={116,118,120,122}
    assert (min(x['n7'] for x in tables[2]),max(x['n7'] for x in tables[2]))==(102,122)
    assert len(tables[4])==23 and {x['D'] for x in tables[4]}=={8,10,12,14,16}
    assert {x['m'] for x in tables[4]}=={108}
    assert (min(x['n7'] for x in tables[4]),max(x['n7'] for x in tables[4]))==(134,144)
    p0=json.loads(a.placement.read_text());k=p0['spectrum_k'];assert len(k)==512
    actual_abs=collections.Counter(map(abs,k[256:]))
    positive={'D':28,'m':122,'S':-4,'n1':actual_abs[1],'n3':actual_abs[3],
              'n5':actual_abs[5],'n7':actual_abs[7]}
    assert positive in tables[2] and p0['full_inverse_not_sign_count']==497
    out={'scope':'exact necessary-profile arithmetic; positive control is a formal NON-WITNESS',
         'rank2_profiles':tables[2],'rank4_profiles':tables[4],
         'rank2_formal_nonwitness_profile':positive,'rank2_formal_inverse_failures':497}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('rank2 30 profiles, rank4 23 profiles; formal D28 non-witness remains')


if __name__=='__main__':main()
