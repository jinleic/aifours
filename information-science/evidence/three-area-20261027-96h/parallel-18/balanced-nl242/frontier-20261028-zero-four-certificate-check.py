#!/opt/homebrew/bin/python3
"""Exact forward and inverse MacWilliams replay for one relaxed count vector."""
import argparse
import json
import math
import pathlib


def krawtchouk_column(n,w):
    out=[1,n-2*w]
    for j in range(1,n):
        numerator=(n-2*w)*out[-1]-(n-j+1)*out[-2]
        assert numerator%(j+1)==0
        out.append(numerator//(j+1))
    return out


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--input',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True)
    args=p.parse_args()
    if args.output.exists(): raise FileExistsError(args.output)
    src=json.loads(args.input.read_text(encoding='utf-8'))
    if src['status']!='sat': raise ValueError('no proposed count vector')
    a={int(k):int(v) for k,v in src['histogram'].items()}
    assert set(a)==set(range(-7,8)) and all(v>=0 for v in a.values())
    assert a[0]==3 and sum(a.values())==511
    assert sum(t*a[t] for t in a)==128
    assert sum(t*t*a[t] for t in a)==16384
    assert sum(a[t] for t in a if t%2)==256
    assert sum(t*a[t] for t in a if t%2==0) in (0,128)
    columns={t:krawtchouk_column(256,128+t) for t in a}
    numerators=[math.comb(256,j)+sum(a[t]*columns[t][j] for t in a) for j in range(257)]
    assert all(v%512==0 for v in numerators)
    d=[v//512 for v in numerators]
    assert d==[int(v) for v in src['dual_coefficients_decimal']]
    assert all(v>=0 for v in d) and sum(d)==1<<247
    assert d[0]==1 and d[1]==d[2]==d[256]==0 and d[255] in (0,1)
    # Reverse MacWilliams transform, using a completely new Krawtchouk column
    # for every dual weight; recover all 257 primal coefficients.
    dual_columns=[krawtchouk_column(256,j) for j in range(257)]
    inverse_nums=[sum(d[j]*dual_columns[j][i] for j in range(257)) for i in range(257)]
    assert all(v%(1<<247)==0 for v in inverse_nums)
    inverse=[v//(1<<247) for v in inverse_nums]
    expected=[0]*257; expected[0]=1
    for t in a: expected[128+t]=a[t]
    assert inverse==expected
    mutated=dict(a); mutated[0]+=1
    assert (1+sum(mutated.values()))%512!=0
    receipt={'forward_divisibility_all_257':True,'all_dual_coefficients_nonnegative':True,
             'dual_sum_power_247':True,'inverse_transform_all_257':True,
             'all_moment_checks_passed':True,'four_zeros_count_only':True,
             'peak_28_count':a[-7]+a[7], 'dual_endpoint_values':{str(j):str(d[j]) for j in (0,1,2,254,255,256)},
             'mutation_rejected':True,'actual_boolean_witness':False}
    with args.output.open('x',encoding='utf-8') as out:
        json.dump(receipt,out,indent=2,sort_keys=True); out.write('\n')
    print('forward=257 inverse=257 dual_nonnegative=true four_zero_counts=true peak28=',receipt['peak_28_count'])


if __name__=='__main__': main()
