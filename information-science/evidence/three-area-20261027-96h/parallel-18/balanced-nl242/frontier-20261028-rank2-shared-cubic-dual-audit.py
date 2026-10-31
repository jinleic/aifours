#!/opt/homebrew/bin/python3
"""Check all 257 formal dual counts of the shared-cubic NON-WITNESS."""
import argparse
import collections
import json
import math
import pathlib


def kcolumn(n,w):
    out=[1,n-2*w]
    for j in range(1,n):
        v=(n-2*w)*out[-1]-(n-j+1)*out[-2]
        assert v%(j+1)==0;out.append(v//(j+1))
    return out


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    r=json.loads(a.input.read_text());k=r['spectrum_k'];assert len(k)==512 and k[0]==0
    A=collections.Counter(k[1:]);cols={t:kcolumn(256,128+t) for t in A}
    nums=[math.comb(256,j)+sum(A[t]*cols[t][j] for t in A) for j in range(257)]
    assert all(v>=0 and v%512==0 for v in nums);dual=[v//512 for v in nums]
    assert dual[0]==1 and dual[1]==dual[2]==dual[256]==0 and dual[255] in(0,1)
    out={'scope':'formal unsigned dual integrality/positivity only; not a code or Boolean witness',
         'histogram_nonzero_frequency':dict(sorted(A.items())),'all_257_duals_integral_nonnegative':True,
         'dual_coefficients_decimal':[str(v) for v in dual]}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('all 257 formal dual counts nonnegative integers; realization NOT implied')


if __name__=='__main__':main()
