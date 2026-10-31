#!/opt/homebrew/bin/python3
"""Small sharpness controls and exact rank-two zero-count arithmetic."""
import argparse
import json
import pathlib


def degree(v):
    a=list(v)
    for i in range(6):
        for x in range(64):
            if x&(1<<i):a[x]^=a[x^(1<<i)]
    return max((i.bit_count() for i,v in enumerate(a) if v),default=-1)


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    sets={8:{x for x in range(64) if x&7==0},16:{x for x in range(64) if x&3==0},
          24:{x for x in range(64) if x&7 in(0,1,2)}}
    controls={}
    for size,S in sets.items():
        h=[int(x in S) for x in range(64)];assert len(S)==size and h[0] and degree(h)<=3
        controls[str(size)]={'weight':size,'degree':degree(h),'contains_origin':True}
    rows=[]
    for D,m in ((12,118),(16,120),(20,122)):
        cap=(7936-64*m)//16;possible=[z for z in range(8,cap+1,8)]
        rows.append({'D':D,'m':m,'energy_Z_upper':cap,'Z_options':possible})
    assert [v['Z_options'] for v in rows]==[[8,16,24],[8,16],[8]]
    out={'scope':'degree-three indicator controls on F2^6; no Boolean target witness',
         'profiles':rows,'cubic_weight_controls':controls}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('rank2 Z options 8/16/24, 8/16, 8; degree≤3 positive controls')


if __name__=='__main__':main()
