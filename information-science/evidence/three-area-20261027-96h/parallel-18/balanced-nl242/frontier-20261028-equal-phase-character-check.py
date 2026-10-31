#!/opt/homebrew/bin/python3
"""Check signed-fiber inequalities for all equal radical phase patterns."""
import argparse
import itertools
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    counts={}
    for lam in range(4):
        chi=[-1 if (lam&r).bit_count()%2 else 1 for r in range(4)]
        seen=0
        for base in (0,1):
            egroups=[((-6,2) if (base^((lam&r).bit_count()%2))==0 else (-2,6)) for r in range(4)]
            for row in itertools.product(*egroups):
                y=[a*b for a,b in zip(row,chi)];E=sum(a*a for a in y);S=sum(y)**2
                assert all(a in (-6,2) for a in y) or all(a in (-2,6) for a in y)
                assert 10*E-S<=864;seen+=1
        ecount=seen;seen=0
        for base in (0,1):
            groups=[((-7,-3,1,5) if (base^((lam&r).bit_count()%2))==0 else (-5,-1,3,7)) for r in range(4)]
            for row in itertools.product(*groups):
                y=[a*b for a,b in zip(row,chi)];E=sum(a*a for a in y);S=sum(y)**2
                assert all(a in (-7,-3,1,5) for a in y) or all(a in (-5,-1,3,7) for a in y)
                assert 10*E-S<=1464;seen+=1
        ocount=seen
        for row in itertools.product((-4,4),repeat=4):
            y=[a*b for a,b in zip(row,chi)]
            assert 10*sum(a*a for a in y)-sum(y)**2<=640
        counts[str(lam)]={'qone_rows':ecount,'odd_rows':ocount,'qzero_rows':16}
    # If one incorrectly omits the character, mixed-phase rows can violate
    # both inequalities; this control detects the sign-orientation mistake.
    assert 10*sum(x*x for x in (-6,-6,6,6))-sum((-6,-6,6,6))**2>864
    assert 10*sum(x*x for x in (-7,-7,7,7))-sum((-7,-7,7,7))**2>1464
    receipt={'all_equal_functionals_0_1_2_3_checked':counts,'correct_character_required':True,
             'unmodulated_sign_mutations_rejected':True,'scope':'local finite controls, not target existence'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('equal phases=4 all local sign-orientation inequalities checked',flush=True)


if __name__=='__main__':main()
