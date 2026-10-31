#!/opt/homebrew/bin/python3
"""Independently audit T, derivative support, and polar of a real Boolean control."""
import argparse
import functools
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--candidate',type=pathlib.Path,required=True)
    p.add_argument('--walsh-audit',type=pathlib.Path,required=True);p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    f=[int(x) for x in json.loads(a.candidate.read_text())['bits']];w=json.loads(a.walsh_audit.read_text())['reports'][0]['walsh_values']
    assert len(f)==len(w)==512 and sum(f)==256 and w[0]==0
    T=functools.reduce(int.__xor__,(i for i,x in enumerate(f) if x),0);assert T==256
    m=sum(f[x]==f[x^T] for x in range(256));assert m==126
    assert all(v%8==0 for v in w[:256]);q=[(v//8)%2 for v in w[:256]]
    B=[[q[0]^q[1<<i]^q[1<<j]^q[(1<<i)^(1<<j)] for j in range(8)] for i in range(8)]
    for x in range(256):
        for i in range(8):
            for j in range(8):assert q[x]^q[x^(1<<i)]^q[x^(1<<j)]^q[x^(1<<i)^(1<<j)]==B[i][j]
    rows=[sum(B[i][j]<<j for j in range(8)) for i in range(8)];basis={}
    for row in rows:
        while row:
            col=row.bit_length()-1
            if col in basis:row^=basis[col]
            else:basis[col]=row;break
    assert len(basis)==8 and q.count(0)==120 and max(map(abs,w[:256]))==64 and max(map(abs,w))==68
    assert sum(v*v for v in w[:256])==1024*m
    result={'scope':'independent rank and derivative audit of a real high-peak NON-TARGET',
            'weight':256,'T':T,'agreeing_pairs':m,'derivative_weight':512-2*m,
            'polar_matrix_rows':rows,'polar_rank':len(basis),'q_zero_count':q.count(0),
            'all_second_derivatives_checked':True,'even_peak':64,'full_peak':68,'target_met':False}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(result,dst,indent=2,sort_keys=True);dst.write('\n')
    print('rank8 T=256 m=126, even peak64, full peak68: NON-TARGET')


if __name__=='__main__':main()
