#!/opt/homebrew/bin/python3
"""Exact rank2 magnitude profiles from energy and adopted E2+2O3 congruence."""
import argparse
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    rows=[]
    for D,m,zeros in ((12,118,(8,16,24)),(16,120,(8,16)),(20,122,(8,))):
        for Z in zeros:
            numerator=7936-16*Z-64*m;assert numerator>=0 and numerator%32==0
            E2=numerator//32
            for n1 in range(D+1):
                n3=D-n1;hnum=8*(m-60)-2*D-4*n1
                if hnum%3:continue
                h=hnum//3;n5=h-n3;n7=256-h-n1
                if min(n3,n5,n7)<0 or (E2+2*n3)%4:continue
                rows.append({'D':D,'m':m,'Z':Z,'E2':E2,'E4':64-Z,'E6':192-E2,
                             'n1':n1,'n3':n3,'n5':n5,'n7':n7})
    assert len(rows)==16 and {r['n1'] for r in rows if r['D']==12}=={2,8}
    assert {r['n1'] for r in rows if r['D']==16}=={4,10,16}
    assert {r['n1'] for r in rows if r['D']==20}=={0,6,12,18}
    assert (min(r['n7'] for r in rows),max(r['n7'] for r in rows))==(104,112)
    assert all(r['E2']%4==0 and r['n3']%2==0 for r in rows)
    out={'scope':'necessary scalar profiles only; no code or Boolean realization','profiles':rows}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('16 rank2 magnitude profiles; all n1/n3 even and 104<=n7<=112')


if __name__=='__main__':main()
