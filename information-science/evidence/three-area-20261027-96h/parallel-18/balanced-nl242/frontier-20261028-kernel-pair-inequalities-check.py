#!/opt/homebrew/bin/python3
"""Exact pairwise and aggregate checks for the kernel-direction certificate."""
import argparse
import itertools
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--near-miss-check',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    near=json.loads(args.near_miss_check.read_text(encoding='utf-8'))
    assert near['all_other_full_pairing_model_constraints_checked'] and near['crossing_replaced_by']==72
    groups=[('zero',(-4,4)),('qone',(-6,2)),('odd_Q0',(-7,-3,1,5)),('odd_Q1',(-5,-1,3,7))]
    limits={'zero':(320,128,256),'qone':(352,144,576),'odd_Q0':(392,196,448),'odd_Q1':(392,196,448)}
    summary={}
    for name,values in groups:
        maxima=[None,None,None];counts=[0,0,0];rows=[]
        for a,b in itertools.combinations_with_replacement(values,2):
            e=a*a+b*b;c=a*b;cross=int(name.startswith('odd') and ((abs(a) in (1,7))!=(abs(b) in (1,7))))
            vals=(7*e-6*c,3*e-2*c-96*cross,7*e+2*c)
            tests=(not name.startswith('odd') or not cross,True,not name.startswith('odd') or bool(cross))
            for i in range(3):
                if tests[i]:
                    assert vals[i]<=limits[name][i];counts[i]+=1
                    maxima[i]=vals[i] if maxima[i] is None else max(maxima[i],vals[i])
            rows.append({'pair':[a,b],'energy':e,'product':c,'cross':cross,'expressions':list(vals)})
        assert tuple(maxima)==limits[name]
        assert all(maxima[i]>limits[name][i]-1 for i in range(3))
        summary[name]={'maxima':maxima,'checked_counts':counts,'rows':rows,'minus_one_mutation_rejected':True}
    gaps={}
    for z in (112,144):
        n0=(z-4)//2;ne=(256-z)//2;no=128
        rhs0=320*n0+352*ne+392*no;lhs0=7*16384
        rhs64=128*n0+144*ne+196*no;lhs64=3*16384-96*64
        rhs128=256*n0+576*ne+448*no;lhs128=7*16384
        gap=[lhs0-rhs0,lhs64-rhs64,lhs128-rhs128]
        assert all(x>0 for x in gap)
        gaps[str(z)]={'zero_pairs':n0,'qone_pairs':ne,'odd_pairs':no,'gaps':gap}
    assert gaps['112']['gaps']==[21888,640,2048] and gaps['144']['gaps']==[22400,896,7168]
    for linear in range(256):
        for c in (0,1):
            wt=sum(((linear&x).bit_count()%2)^c for x in range(256))
            assert wt in (0,128,256)
    result={'groups':summary,'aggregate_gaps':gaps,'all_affine_derivative_weights_checked':512,
            'near_miss_crossing':72,'near_miss_other_constraints_independently_checked':True,
            'note':'finite controls and human-checkable inequalities; written soundness remains necessary'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('pair inequalities checked; crossing=0,64,128 gaps positive; near-miss=72',flush=True)


if __name__=='__main__':main()
