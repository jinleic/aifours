#!/opt/homebrew/bin/python3
"""Check the symplectic construction excluding a four-point zero set at rank eight."""
import argparse
import json
import pathlib


def B(a,b):return sum((((a>>(2*i))&1)*((b>>(2*i+1))&1)) ^ (((a>>(2*i+1))&1)*((b>>(2*i))&1)) for i in range(4))%2

def q(a):return sum(((a>>(2*i))&1)*((a>>(2*i+1))&1) for i in range(4))%2

def span(basis):
    result=[0]
    for b in basis:result += [x^b for x in result]
    return result

def rank(rows):
    piv={}
    for row in rows:
        while row:
            i=row.bit_length()-1
            if i in piv:row^=piv[i]
            else:piv[i]=row;break
    return len(piv)


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    Z=set(span([1,4]));D=span([2,8,16]);L=[x for x in range(256) if all(not B(x,d) for d in D)]
    assert len(Z)==4 and all(q(z)==0 for z in Z)
    assert len(D)==8 and all(not B(a,b) for a in D for b in D)
    assert len(L)==32 and Z.intersection(L)=={0}
    basis=[2,8,16,64,128];assert set(span(basis))==set(L)
    gram=[sum(B(x,y)<<j for j,y in enumerate(basis)) for x in basis]
    assert rank(gram)==2
    # K/L is represented by e0,e2,e5 in this coordinate choice.
    rows=[];covered=set()
    for rep in span([1,4,32]):
        A={rep^x for x in L};assert not (covered&A);covered|=A
        nq=sum(q(x) for x in A);nz=len(A&Z);assert nq%8==0
        k={x:(0 if x in Z else (4 if not q(x) else 2)) for x in A}
        E=sum(t*t for t in k.values())%32
        assert E==(16*(nz%2))%32
        rows.append({'representative':rep,'q_ones':nq,'zero_count':nz,'even_energy_mod32':E})
    assert len(covered)==256 and sorted(x['zero_count'] for x in rows)==[0]*4+[1]*4
    assert {x['even_energy_mod32'] for x in rows}=={0,16}
    receipt={'symplectic_rank':8,'zero_plane':sorted(Z),'isotropic_D_basis':[2,8,16],
             'L_basis':basis,'L_restricted_rank':2,'L_disjoint_from_zero_plane':True,
             'all_eight_cosets':rows,'energy_residues_conflict':True,
             'note':'formal category control; all-variable symplectic proof is separate'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('rank8 Lrank2 qcounts divisible8 zero parity=4+4 energy residues=0,16',flush=True)


if __name__=='__main__':main()
