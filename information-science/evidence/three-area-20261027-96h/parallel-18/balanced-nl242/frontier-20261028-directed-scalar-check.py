#!/opt/homebrew/bin/python3
"""Independent exact scalar checks for formal radical-fiber multisets."""
import argparse
import json
import pathlib

ALLOWED={144:{28,52,56,60,84},112:{36,44,52,60,68,72,76,84,92,100,108}}
PHASE={(112,12),(112,28),(128,16),(144,4),(144,20)}


def main():
    p=argparse.ArgumentParser();p.add_argument('--inputs',nargs='+',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    rows=[]
    for path in args.inputs:
        d=json.loads(path.read_text(encoding='utf-8'));a={int(t):v for t,v in d['histogram'].items()}
        assert d['status']=='sat' and set(a)==set(range(-7,8)) and all(v>=0 for v in a.values())
        assert a[0]==3 and sum(a.values())==511 and sum(t*a[t] for t in a)==128
        assert sum(t*t*a[t] for t in a)==16384 and sum(a[t] for t in a if t%2)==256
        z=4+a[-4]+a[4];w=a[-5]+a[-1]+a[3]+a[7];P=a[-7]+a[-1]+a[1]+a[7];c=a[-5]+a[3];m=a[-2]+a[6]
        peaks=a[-7]+a[7];assert z in ALLOWED and m in ALLOWED[z] and 92<=peaks<=234
        assert w in (112,128,144) and P%4==0 and P<=224 and P!=220
        if d['lambda_mode']:assert 2*m==256-z
        if d['qrad_bit']:assert w==128
        else:assert w in (112,144)
        if P==224:assert (w,c) in PHASE
        if P==216:assert c==20 if w==128 else c%8==4
        if P==212 and w==112:assert c>=16
        assert sum(t*a[t] for t in a if not t%2) in (0,128)
        g=3*(a[-7]+a[7]-a[-1]-a[1])-2*(a[-3]+a[3]);assert g%16==0
        dual=[int(x) for x in d['dual_coefficients_decimal']]
        assert len(dual)==257 and all(x>=0 for x in dual) and 5296<=dual[3]<=5594 and 30<=dual[254]<=71
        assert dual[255] in (0,1)
        rows.append({'file':str(path),'lambda':d['lambda_mode'],'qrad_bit':d['qrad_bit'],
                     'z':z,'Q_weight':w,'even_g3':m,'P_weight':P,'peaks':peaks,'global_g':g,
                     'scalar_filters_checked':True})
    receipt={'models':rows,'scope':'formal counts only; no labeled Walsh spectrum or Boolean witness'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('models=',len(rows),'all_scalar_checks=true',flush=True)


if __name__=='__main__':main()
