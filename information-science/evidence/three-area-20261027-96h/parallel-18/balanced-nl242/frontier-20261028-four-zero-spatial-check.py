#!/opt/homebrew/bin/python3
"""Independently replay the formal spectrum's selected spatial properties."""
import argparse
import itertools
import json
import pathlib


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--input',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True)
    args=p.parse_args()
    if args.output.exists(): raise FileExistsError(args.output)
    data=json.loads(args.input.read_text(encoding='utf-8'))
    if not data['found_formal_placement']: raise ValueError('no placement')
    P=int(data['p_truth_bits_le_hex'],16); Q=int(data['q_truth_bits_le_hex'],16)
    k=data['spectrum_k']
    assert len(k)==512 and k[0]==0 and max(map(abs,k))==7
    assert sum(k)==128 and sum(t*t for t in k)==16384
    assert [i for i,x in enumerate(k) if not x]==[0,1,2,3]
    assert [i for i,x in enumerate(k) if abs(x)==4]==[4,5,6,7]
    assert all((t&1)==(i>>8) for i,t in enumerate(k))
    assert P.bit_count()==150 and Q.bit_count()==120 and (P&Q).bit_count()==80
    for x in range(256):
        expect=sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(4))%2
        assert (Q>>x)&1==expect
        assert (P>>x)&1==(abs(k[256+x]) in (1,7))
        assert k[256+x]%4==1+2*expect
    # All affine 5-flats of F_2^8, using independent RREF generation.
    checked=0; subspaces=0
    for pivots in itertools.combinations(range(8),5):
        free=[x for x in range(8) if x not in pivots]
        slots=[(r,c) for c in free for r in range(5) if c>pivots[r]]
        for assignment in range(1<<len(slots)):
            basis=[1<<p for p in pivots]
            for j,(r,c) in enumerate(slots):
                if assignment>>j&1: basis[r]|=1<<c
            span=[0]
            for b in basis: span += [v^b for v in span]
            assert len(span)==32
            subspaces+=1
            for coset in range(8):
                origin=sum(1<<free[j] for j in range(3) if coset>>j&1)
                flat=sum(1<<(origin^v) for v in span)
                assert (P&flat).bit_count()%2==0
                checked+=1
    assert subspaces==97155 and checked==777240
    # A changed P bit must break the parity of the first coordinate 5-flat.
    sample=(1<<32)-1
    assert (P&sample).bit_count()%2==0 and ((P^1)&sample).bit_count()%2==1
    direct=[sum(v*(-1 if (a&x).bit_count()%2 else 1) for a,v in enumerate(k)) for x in range(512)]
    bad=sum(abs(v)!=128 for v in direct)
    assert bad==data['inverse_nonsign_count'] and max(map(abs,direct))==data['inverse_max_abs']
    autocorrelation=[sum(k[a]*k[a^b] for a in range(512)) for b in range(512)]
    assert autocorrelation[0]==16384
    nonzero=[b for b in range(1,512) if autocorrelation[b]!=0]
    assert bad>0 and nonzero
    receipt={'selected_spatial_filters_checked':True,'all_affine_5_flats_checked':checked,
             'distinct_linear_5_subspaces_checked':subspaces,'q_is_specified_quadratic':True,
             'spectrum_inverse_direct_512x512':True,'inverse_nonsign_count':bad,
             'inverse_max_abs':max(map(abs,direct)),'nonzero_offorigin_autocorrelations':len(nonzero),
             'zero_xor_and_magnitude4_xor_verified':True,'mutation_rejected':True,
             'actual_boolean_witness':False,
             'limits':'Does not test all adopted Walsh constraints; not a Boolean function.'}
    with args.output.open('x',encoding='utf-8') as out: json.dump(receipt,out,indent=2,sort_keys=True); out.write('\n')
    print('affine5flats=',checked,'inverse_nonsign=',bad,'nonzero_autocorr=',len(nonzero),flush=True)


if __name__=='__main__': main()
