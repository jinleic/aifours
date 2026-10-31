#!/opt/homebrew/bin/python3
"""Verify the kernel model's intended crossing-72 positive near-miss."""
import argparse
import collections
import json
import math
import pathlib


def Kcolumn(n,w):
    out=[1,n-2*w]
    for j in range(1,n):
        numerator=(n-2*w)*out[-1]-(n-j+1)*out[-2]
        assert numerator%(j+1)==0;out.append(numerator//(j+1))
    return out


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    src=json.loads(args.input.read_text(encoding='utf-8'))
    if src['status']!='sat':raise ValueError('no near-miss model')
    A={int(t):v for t,v in src['histogram'].items()};observed=collections.Counter({0:3});energy=0;moment=0;C=0;cross=0
    allowed={'zero':{-4,4},'g1':{-6,2},'g3':{-2,6},'Q0':{-7,-3,1,5},'Q1':{-5,-1,3,7}}
    totalpairs=0
    for tag,records in src['pairings'].items():
        assert tag in allowed
        for row in records:
            x,y=row['values'];n=row['pairs'];assert n>0 and x in allowed[tag] and y in allowed[tag]
            observed[x]+=n;observed[y]+=n;energy+=n*(x*x+y*y);moment+=n*(x+y);C+=n*x*y;totalpairs+=n
            if tag in ('Q0','Q1') and ((abs(x) in (1,7))!=(abs(y) in (1,7))):cross+=n
    assert all(observed[t]==A[t] for t in range(-7,8))
    assert totalpairs==254 and A[0]==3 and sum(A.values())==511
    assert energy==16384 and moment==128 and C==0 and cross==72
    z=4+A[-4]+A[4];w=A[-5]+A[-1]+A[3]+A[7];P=A[-7]+A[-1]+A[1]+A[7];c=A[-5]+A[3];m=A[-2]+A[6]
    assert z in (112,144) and w in (112,144) and 2*m==256-z
    assert P%4==0 and P<=224 and P!=220 and 92<=A[-7]+A[7]<=234
    phase={(112,12),(112,28),(128,16),(144,4),(144,20)}
    if P==224:assert (w,c) in phase
    if P==216:assert c%8==4
    if P==212 and w==112:assert c>=16
    assert sum(A[t] for t in A if t%2)==256 and sum(t*A[t] for t in A if not t%2) in (0,128)
    columns={t:Kcolumn(256,128+t) for t in A}
    numerators=[math.comb(256,j)+sum(A[t]*columns[t][j] for t in A) for j in range(257)]
    assert all(n>=0 and n%512==0 for n in numerators)
    dual=[n//512 for n in numerators]
    assert dual==[int(v) for v in src['dual_coefficients_decimal']]
    assert dual[0]==1 and dual[1]==dual[2]==dual[256]==0 and dual[255] in (0,1)
    assert cross not in (0,64,128)  # exactly the deliberately removed condition
    receipt={'crossing_replaced_by':72,'original_affine_crossing_condition_violated':True,
             'all_other_full_pairing_model_constraints_checked':True,'actual_boolean_witness':False,
             'nonzero_frequency_count':sum(A.values()),'pair_count':totalpairs,'energy':energy,'first_moment':moment,
             'kernel_correlation_ordered':2*C,'z':z,'Q_weight':w,'P_weight':P,'peak_count':A[-7]+A[7],
             'all_257_duals_nonnegative_integral':True,'scope':'formal pairing near-miss, not a labeled Boolean spectrum'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('near-miss cross=72 pairs=',totalpairs,'E=',energy,'C=',2*C,'all other checks=true',flush=True)


if __name__=='__main__':main()
