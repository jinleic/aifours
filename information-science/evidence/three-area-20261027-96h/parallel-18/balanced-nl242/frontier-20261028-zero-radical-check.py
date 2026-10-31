#!/opt/homebrew/bin/python3
"""Controls for 5-flat q/zero parity and a concrete rank-four obstruction."""
import argparse
import json
import pathlib


def fwht(a):
    v=list(a);step=1
    while step<len(v):
        for i in range(0,len(v),2*step):
            for j in range(step):
                x,y=v[i+j],v[i+j+step];v[i+j],v[i+j+step]=x+y,x-y
        step*=2
    return v


def span(basis):
    out=[0]
    for b in basis:out += [x^b for x in out]
    return out


def independent_kernel(T):
    piv={};basis=[]
    for a in range(512):
        if (a&T).bit_count()%2:continue
        v=a
        while v:
            p=v.bit_length()-1
            if p in piv:v^=piv[p]
            else:piv[p]=v;basis.append(a);break
    assert len(basis)==8
    return basis


def main():
    p=argparse.ArgumentParser();p.add_argument('--balanced',type=pathlib.Path,required=True)
    p.add_argument('--formal',type=pathlib.Path,required=True);p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    f=[int(x) for x in json.loads(args.balanced.read_text(encoding='utf-8'))['bits']]
    assert len(f)==512 and sum(f)==256
    T=0
    for x,v in enumerate(f):
        if v:T^=x
    assert T!=0
    W=fwht([1-2*v for v in f]);assert all(x%4==0 for x in W);k=[x//4 for x in W]
    basis=independent_kernel(T);L=span(basis[:5]);reps=span(basis[5:]);odd=next(a for a in range(512) if (a&T).bit_count()%2)
    B=[odd^x for x in L];Eb=sum(k[a]**2 for a in B)
    qpar=[];zpar=[];energy=[]
    for rep in reps:
        A=[rep^x for x in L]
        nq=sum((k[a]//2)%2 for a in A);nz=sum(k[a]%8==0 for a in A)
        E=sum(k[a]**2 for a in A)
        assert nq%4==0 and E%32==(16*((nq//4+nz)%2))%32
        assert (E+Eb)%32==0
        qpar.append((nq//4)%2);zpar.append(nz%2);energy.append(E%32)
    assert len(set(x^y for x,y in zip(qpar,zpar)))==1 and len(set(energy))==1
    # reps are generated as subset sums of the final three basis vectors.
    a=qpar[:]
    for j in range(3):
        for x in range(8):
            if x>>j&1:a[x]^=a[x^(1<<j)]
    assert all(not a[x] for x in range(8) if x.bit_count()>1)
    formal=json.loads(args.formal.read_text(encoding='utf-8'))['spectrum_k']
    L2=span([1,2,4,16,32]);rows=[]
    for rep in (0,8):
        A=[rep^x for x in L2]
        nq=sum((formal[x]//2)%2 for x in A);nz=sum(formal[x]==0 for x in A);E=sum(formal[x]**2 for x in A)
        assert nq%8==0
        rows.append({'representative':rep,'q_ones':nq,'zeros':nz,'energy_mod32':E%32})
    assert [r['energy_mod32'] for r in rows]==[16,0]
    receipt={'balanced_control_T':T,'balanced_control_q_quotient_anf_degree_at_most_1':True,
             'balanced_control_eight_even_energies_mod32':energy,'balanced_control_z8_and_q_parities':list(zip(zpar,qpar)),
             'formal_rank4_rows':rows,'formal_rank4_energy_difference_mod32':16,
             'note':'finite controls; the all-rank theorem needs the written proof'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('balanced T=',T,'qpar affine=true formal even-energy residues=16,0',flush=True)


if __name__=='__main__':main()
