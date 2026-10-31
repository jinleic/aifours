#!/opt/homebrew/bin/python3
"""Check the explicit affine-energy failure and balanced Parseval control."""
import argparse
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--formal',type=pathlib.Path,required=True)
    p.add_argument('--balanced',type=pathlib.Path,required=True);p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    k=json.loads(args.formal.read_text(encoding='utf-8'))['spectrum_k']
    truth=[int(x) for x in json.loads(args.balanced.read_text(encoding='utf-8'))['bits']]
    assert len(k)==len(truth)==512 and sum(truth)==256
    flat=[a for a in range(512) if a&195==195]
    assert len(flat)==32
    even_q1=sum(a<256 and k[a]%4==2 for a in flat)
    odd_p0=sum(a>=256 and abs(k[a]) in (3,5) for a in flat)
    energy=sum(k[a]*k[a] for a in flat)
    assert (even_q1,odd_p0,energy,energy%16)==(10,4,984,8)
    residue=(4*even_q1+9*odd_p0+(16-odd_p0))%16
    assert residue==8 and (residue-8)%16==0  # one P0->P1 mutation removes the contradiction
    # Direct character sums and spatial-coset Parseval for all 16 cosets of
    # span(e0,e1,e6,e7), with an actual balanced Boolean table.
    signs=[1-2*b for b in truth]
    W=[sum(signs[x]*(-1 if (a&x).bit_count()%2 else 1) for x in range(512)) for a in range(512)]
    assert all(v%4==0 for v in W)
    U=[1,2,64,128];free=[4,8,16,32,256];controls=[]
    for lam in range(16):
        target=sum(U[j] for j in range(4) if lam>>j&1)
        E=sum((W[a]//4)**2 for a in range(512) if a&195==target)
        coset_values=[]
        for rep in range(32):
            x=sum(free[j] for j in range(5) if rep>>j&1);v=0
            for direction in range(16):
                u=sum(U[j] for j in range(4) if direction>>j&1)
                v+=signs[x^u]*(-1 if (direction&lam).bit_count()%2 else 1)
            coset_values.append(v)
        assert all(v%2==0 for v in coset_values)
        assert sum(coset_values)==W[target]
        assert E==2*sum(v*v for v in coset_values) and E%16==0
        controls.append(E)
    result={'flat_mask':195,'flat_size':32,'even_q1':even_q1,'odd_p0':odd_p0,
            'actual_formal_flat_energy':energy,'formal_flat_energy_mod16':8,
            'balanced_control_all_16_cosets':True,'balanced_coset_energies':controls,
            'direct_character_sums':True,'targeted_residue_mutation_changes_failure':True,
            'note':'Finite controls do not replace the all-variable proof.'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('flat_energy=',energy,'mod16=8 balanced_controls=16',flush=True)


if __name__=='__main__':main()
