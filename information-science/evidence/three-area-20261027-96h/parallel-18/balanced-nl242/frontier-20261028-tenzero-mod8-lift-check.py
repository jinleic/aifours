#!/opt/homebrew/bin/python3
"""Verify an explicit rank8 ten-point even-half mod8 lift and formal counts."""
import argparse
import json
import math
import pathlib

TERMS=[4,8,12,20,36,24,40,192,19,35,13,49,14,50,28,44,52,56,208,224]
Z={0,64,128,193,194,199,203,223,239,255}

def g0(x):return sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(4))+(x&51).bit_count()

def h(x):return sum(int(x&t==t) for t in TERMS)%2

def Kcolumn(n,w):
    out=[1,n-2*w]
    for j in range(1,n):
        v=(n-2*w)*out[-1]-(n-j+1)*out[-2]
        assert v%(j+1)==0;out.append(v//(j+1))
    return out


def main():
    p=argparse.ArgumentParser();p.add_argument('--counts',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    src=json.loads(args.counts.read_text(encoding='utf-8'));A={int(t):v for t,v in src['histogram'].items()}
    assert src['status']=='sat' and all(t.bit_count()<=3 for t in TERMS)
    qzero=[x for x in range(256) if g0(x)%2==0];qone=[x for x in range(256) if g0(x)%2]
    assert len(qzero)==136 and len(qone)==120 and Z<=set(qzero)
    g=[(g0(x)+2*h(x))%4 for x in range(256)]
    assert {x for x in qzero if g[x]==0}==Z
    assert all(g[x]==2 for x in qzero if x not in Z)
    assert sum(g[x]==3 for x in qone)==60
    assert A[0]==9 and sum(A.values())==511 and sum(t*A[t] for t in A)==128
    assert sum(t*t*A[t] for t in A)==16384 and sum(A[t] for t in A if t%2)==256
    assert A[-4]+A[4]==126 and A[-2]+A[6]==60 and A[-6]+A[2]==60
    w=A[-5]+A[-1]+A[3]+A[7];P=A[-7]+A[-1]+A[1]+A[7]
    assert w in (120,136) and P<=210 and P%4==2 and 92<=A[-7]+A[7]<=210
    cols={t:Kcolumn(256,128+t) for t in A}
    nums=[math.comb(256,j)+sum(A[t]*cols[t][j] for t in A) for j in range(257)]
    assert all(x>=0 and x%512==0 for x in nums)
    dual=[x//512 for x in nums];assert dual==[int(x) for x in src['dual_coefficients_decimal']]
    assert dual[0]==1 and dual[1]==dual[2]==dual[256]==0 and dual[255] in (0,1)
    # Mutation at the origin breaks the required zero condition.
    assert (g[0]^2)!=0
    result={'formal_Z8_count':len(Z),'q_zero_count':len(qzero),'q_one_count':len(qone),
            'explicit_cubic_terms':TERMS,'all_256_even_residues_checked':True,'g3_count':60,
            'formal_histogram_zeros':10,'odd_Q_weight':w,'P_weight':P,'peak_count':A[-7]+A[7],
            'all_257_dual_counts_nonnegative_integral':True,'mutation_rejected':True,
            'scope':'compatible even residue and scalar checks, no common odd placement or Boolean inverse'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('formal ten-zero lift qzero=136 g3=60 P=',P,'oddQ=',w,flush=True)


if __name__=='__main__':main()
