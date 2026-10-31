#!/opt/homebrew/bin/python3
"""Independently check one balanced Z8=8 sharpness example."""
import argparse
import hashlib
import json
import pathlib


def rank(rows):
    piv={}
    for v in rows:
        while v:
            j=v.bit_length()-1
            if j in piv:v^=piv[j]
            else:piv[j]=v;break
    return len(piv)


def main():
    p=argparse.ArgumentParser();p.add_argument('--candidate',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    raw=json.loads(args.candidate.read_text(encoding='utf-8'))['bits']
    assert len(raw)==512 and set(raw)<={'0','1'}
    bits=[int(v) for v in raw];assert sum(bits)==256
    T=0
    for x in range(512):
        if bits[x]:T^=x
    assert T==141
    W=[sum((1-2*bits[x])*(-1 if (a&x).bit_count()%2 else 1) for x in range(512)) for a in range(512)]
    assert W[0]==0 and all(v%4==0 for v in W) and sum(v*v for v in W)==512*512
    assert max(map(abs,W))==80
    k=[v//4 for v in W];K=[a for a in range(512) if (a&T).bit_count()%2==0]
    piv={};basis=[]
    for a in K:
        v=a
        while v:
            b=v.bit_length()-1
            if b in piv:v^=piv[b]
            else:piv[b]=v;basis.append(a);break
    assert len(basis)==8 and all(k[a]%2==0 for a in K)
    def q(a):return (k[a]//2)%2
    def B(a,b):return q(a^b)^q(a)^q(b)
    gram=[sum(B(a,b)<<j for j,b in enumerate(basis)) for a in basis]
    r=rank(gram);assert r==2
    radical=[a for a in K if all(B(a,b)==0 for b in basis)]
    z8=[a for a in K if k[a]%8==0];zeros=[a for a in range(512) if not W[a]]
    assert len(radical)==64 and len(z8)==8 and len(zeros)==3
    assert 0 in z8 and all(a^b in z8 for a in z8 for b in z8)
    assert set(z8)<=set(radical)
    receipt={'truth_sha256':hashlib.sha256(raw.encode()).hexdigest(),'weight':sum(bits),'T':T,
             'direct_512x512_character_sums':True,'parseval':True,'peak':80,'nonlinearity':216,
             'actual_walsh_zero_indices':zeros,'z8_indices':z8,'z8_count':len(z8),
             'z8_linear_3plane':True,'even_quadratic_polar_rank':r,'radical_size':len(radical),
             'z8_subset_of_radical_in_this_example':True,'target_met':False}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('Z8=',len(z8),'rank=',r,'peak=',max(map(abs,W)),'target=false',flush=True)


if __name__=='__main__':main()
