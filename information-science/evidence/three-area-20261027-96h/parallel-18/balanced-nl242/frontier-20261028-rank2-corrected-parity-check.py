#!/opt/homebrew/bin/python3
"""Corrected rank2 energy, zero divisibility and signed-magnitude arithmetic."""
import argparse
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    rows=[]
    for D,m in ((12,118),(16,120),(20,122)):
        cap=(7936-64*m)//16
        for Z in range(8,cap+1):
            numerator=7936-16*Z-64*m
            if numerator%32:continue
            E2=numerator//32
            for n1 in range(D+1):
                n3=D-n1;hnum=8*(m-60)-2*D-4*n1
                if hnum%3:continue
                h=hnum//3;n5=h-n3;n7=256-h-n1
                if min(n3,n5,n7)<0 or (E2+2*n3)%4:continue
                rows.append({'D':D,'m':m,'Z':Z,'E2':E2,'E4':64-Z,'E6':192-E2,
                             'n1':n1,'n3':n3,'n5':n5,'n7':n7})
    assert len(rows)==23
    assert {r['Z'] for r in rows if r['D']==12}=={8,12,16,20,24}
    assert {r['Z'] for r in rows if r['D']==16}=={8,12,16}
    assert {r['Z'] for r in rows if r['D']==20}=={8}
    assert all(r['Z']%4==0 and r['E2']%2==0 for r in rows)
    assert (min(r['n7'] for r in rows),max(r['n7'] for r in rows))==(104,113)
    # Local formal even countermodel Z14 has E2=5; no n3 can satisfy parent mod4.
    assert all((5+2*n3)%4!=0 for n3 in range(2))
    out={'scope':'necessary unsigned magnitude profiles only; no Boolean realization',
         'profiles':rows,'invalid_Z14_formal_model_parent_congruence_always_fails':True}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('corrected rank2: 23 profiles, Z multiple4; no divisor8 used')


if __name__=='__main__':main()
