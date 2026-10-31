#!/opt/homebrew/bin/python3
"""Directly verify the mod-8 moment expansion on an actual balanced truth table."""
import argparse
import itertools
import json
import pathlib


def basis_kernel(T):
    piv={};out=[]
    for a in range(512):
        if (a&T).bit_count()%2:continue
        v=a
        while v:
            b=v.bit_length()-1
            if b in piv:v^=piv[b]
            else:piv[b]=v;out.append(a);break
    if len(out)!=8:raise ValueError('T must be nonzero')
    return out


def rank(rows):
    piv={}
    for v in rows:
        while v:
            i=v.bit_length()-1
            if i in piv:v^=piv[i]
            else:piv[i]=v;break
    return len(piv)


def main():
    p=argparse.ArgumentParser();p.add_argument('--balanced',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    bits=list(map(int,json.loads(args.balanced.read_text(encoding='utf-8'))['bits']))
    assert len(bits)==512 and sum(bits)==256
    M=[x for x,v in enumerate(bits) if v];T=0
    for x in M:T^=x
    assert T!=0
    basis=basis_kernel(T);masks=[sum(((b&x).bit_count()%2)<<i for i,b in enumerate(basis)) for x in M]
    linear=[sum((m>>i)&1 for m in masks) for i in range(8)]
    assert all(v%2==0 for v in linear)
    pairs={(i,j):sum(((m>>i)&1)*((m>>j)&1) for m in masks) for i in range(8) for j in range(i+1,8)}
    triples={(i,j,l):sum(((m>>i)&1)*((m>>j)&1)*((m>>l)&1) for m in masks)
             for i in range(8) for j in range(i+1,8) for l in range(j+1,8)}
    mismatches=mutant=0
    for a in range(256):
        freq=0
        for i,b in enumerate(basis):
            if a>>i&1:freq^=b
        W=sum((1-2*bits[x])*(-1 if (freq&x).bit_count()%2 else 1) for x in range(512))
        assert W%4==0 and (W//4)%2==0
        actual=(W//8)%4
        predicted=(sum((linear[i]//2)*(a>>i&1) for i in range(8))
                   -sum(v*(a>>i&1)*(a>>j&1) for (i,j),v in pairs.items())
                   +2*sum(v*(a>>i&1)*(a>>j&1)*(a>>l&1) for (i,j,l),v in triples.items()))%4
        mismatches+=actual!=predicted
        mutated=(predicted+2*(a&1)*((a>>1)&1)*((a>>2)&1))%4
        mutant+=actual!=mutated
    assert mismatches==0 and mutant>0
    canonical=[]
    for arf in (0,1):
        def q(x):return (sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))+arf*((x&1)+((x>>1)&1)))%2
        z=sum(q(x)==0 for x in range(256))
        rows=[sum((q((1<<i)^(1<<j))^q(1<<i)^q(1<<j))<<j for j in range(8)) for i in range(8)]
        assert rank(rows)==6 and z==(144 if arf==0 else 112)
        canonical.append({'arf':arf,'rank':6,'q_zero_count':z})
    result={'balanced_control_T':T,'kernel_frequencies_checked':256,'direct_character_sums':True,
            'mod8_expansion_mismatches':mismatches,'cubic_mutation_mismatches':mutant,
            'canonical_arf_checks':canonical,'note':'finite controls do not substitute for all-variable proof'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('kernel_freq=256 mod8_mismatch=0 mutant=',mutant,'canonical_z=144,112',flush=True)


if __name__=='__main__':main()
