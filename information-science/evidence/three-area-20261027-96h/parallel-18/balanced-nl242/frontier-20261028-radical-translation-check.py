#!/opt/homebrew/bin/python3
"""Check simultaneous translation of the even and odd radical phases."""
import argparse
import json
import pathlib


def fwht(vals):
    a=list(vals);d=1
    while d<len(a):
        for i in range(0,len(a),2*d):
            for j in range(d):x,y=a[i+j],a[i+j+d];a[i+j],a[i+j+d]=x+y,x-y
        d*=2
    return a


def main():
    p=argparse.ArgumentParser();p.add_argument('--balanced',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    for k in range(0,8,2):
        for s in (0,1):assert ((-1 if s else 1)*k-k-4*s*((k//2)%2))%8==0
    for k in (1,3,5,7):assert (((-k-1)//2)-((k-1)//2))%2==1
    for lam in range(4):
        for rho in range(4):
            for psi in range(4):
                assert (lam^psi)^(rho^psi)==lam^rho
                if psi==rho:assert (rho^psi)==0 and (lam^psi)==(lam^rho)
    # Two independent frequencies: every prescribed character occurs 128 times.
    z1,z2=238,350
    totals=[0]*4
    for t in range(512):totals[(t&z1).bit_count()%2+2*((t&z2).bit_count()%2)]+=1
    assert totals==[128]*4
    f=[int(x) for x in json.loads(args.balanced.read_text(encoding='utf-8'))['bits']]
    assert len(f)==512 and sum(f)==256
    T=0
    for x,v in enumerate(f):
        if v:T^=x
    assert T!=0
    W=fwht([1-2*v for v in f]);assert all(v%4==0 for v in W);k=[v//4 for v in W]
    for t in (0,1,2,3,7,16,31,63,64,127,128,255,256,350,432,511):
        ft=[f[x^t] for x in range(512)]
        kt=[v//4 for v in fwht([1-2*v for v in ft])]
        assert all(kt[a]==(-1 if (a&t).bit_count()%2 else 1)*k[a] for a in range(512))
        for a in range(512):
            if not (a&T).bit_count()%2:assert (kt[a]//2)%2==(k[a]//2)%2
            else:assert (((kt[a]-1)//2)^((k[a]-1)//2))%2==(a&t).bit_count()%2
    receipt={'even_residue_identity_checked':True,'odd_Q_sign_identity_checked':True,
             'all_64_phase_translations_checked':True,'each_radical_character_translation_count':totals,
             'balanced_control_T':T,'balanced_control_translations_checked':16,
             'scope':'translation identities only; no fourzero target or existence proof'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('even/odd identities=ok phases=64 shifts/character=128 balanced_shifts=16',flush=True)


if __name__=='__main__':main()
