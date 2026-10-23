"""Independent exhaustive half-catalogue/bitset audit of 32-free-site classes.

No producer imports. Every one of the 65536 half spectra is reconstructed
by direct character sums. All 512 full-character rows are checked against
the block transform identity, proving correspondence for every pair of
half assignments. All 2^32 combinations in every listed case are covered
by exact finite set intersections, rather than sampled full transforms.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
import hashlib
from itertools import combinations
import json
from pathlib import Path
import re
import subprocess
import numpy as np


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('--output')
    parser.add_argument('--broken',action='store_true')
    args=parser.parse_args()
    data=json.loads(Path(args.path).read_text())
    if args.broken: data['cases'][0]['assignments_preserving_bound']+=1
    name=data['seed']
    text=Path('selection-inputs/literature/kavut-yucel.reader.md').read_text().split('#### 3.2')[0]
    raw=re.findall(r'(?m)^([0-9A-F]{64}) ([0-9A-F]{64})$',text)
    assert len(raw)==3
    hx=''.join(dict(zip(('dsbf40','dsbf32','rsbf56'),raw))[name])
    assert data['seed_hex']==hx
    f=np.array([int(b) for c in hx for b in format(int(c,16),'04b')],dtype=np.int16)
    H=np.array([[1-2*(bin(a&x).count('1')%2) for x in range(512)] for a in range(512)],dtype=np.int16)
    W=H.astype(np.int32)@(1-2*f).astype(np.int32)
    V=data['ordered_linear_four_flat']
    basis=data['basis']
    assert len(V)==len(set(V))==16 and V[0]==0
    for t in range(16):
        want=0
        for j,b in enumerate(basis):
            if (t>>j)&1: want^=b
        assert V[t]==want
    assert len(basis)==4
    assert all(v^w in V for v in V for w in V)
    reps=sorted({min(x^v for v in V) for x in range(512)})
    assert reps==data['coset_representatives'] and len(reps)==32
    core=data['core_coset_representative']
    flat=json.loads(Path('results/flat-class.json').read_text())['seeds'][name]
    assert sorted(core^v for v in V)==flat['free_points_sorted']
    assert data['pair_selection']=='all' and data['bound']==28
    expected_cases=list(combinations(reps,2))
    assert [tuple(c['coset_representatives']) for c in data['cases']]==expected_cases
    assert len(expected_cases)==496
    # Direct 16-term sums for every catalogue entry; no FWHT or producer.
    H16=np.array([[1-2*(bin(h&t).count('1')%2) for t in range(16)] for h in range(16)],dtype=np.int16)
    masks=np.arange(65536,dtype=np.int32)
    signs=(1-2*((masks[:,None]>>np.arange(16))&1)).astype(np.int16)
    C=signs@H16.T
    assert C.shape==(65536,16)
    assert hashlib.sha256(C.astype('<i2').tobytes()).hexdigest()==data['half_spectrum_catalogue_sha256']
    values=((C+16)//2).astype(np.int8)
    exact=[]; cumulative=[]
    for h in range(16):
        row=[]; acc=[]; mask=0
        for value in range(-16,17,2):
            entry=int.from_bytes(np.packbits(C[:,h]==value,bitorder='little').tobytes(),'little')
            row.append(entry); mask|=entry; acc.append(mask)
        assert mask==(1<<65536)-1
        exact.append(row); cumulative.append(acc)
    dual=np.array([sum((1<<j) for j,b in enumerate(basis) if bin(a&b).count('1')%2) for a in range(512)],dtype=np.int32)
    all_a=np.arange(512)
    total_legal=0
    all_rigid=True
    for number,case in enumerate(data['cases'],1):
        p,q=case['coset_representatives']
        P=[p^v for v in V]
        Q=[q^v for v in V]
        phase_p=H[:,p].astype(np.int32)
        phase_qp=H[:,p^q].astype(np.int32)
        # Verify the complete block character identity, for every row
        # and every free point, before using the catalogue factorization.
        assert np.array_equal(H[:,P],phase_p[:,None]*H16[dual,:])
        assert np.array_equal(H[:,Q],phase_p[:,None]*phase_qp[:,None]*H16[dual,:])
        # Fixed outside contributions are reconstructed directly from
        # the seed and the full character matrix, not the producer's
        # old-half-spectrum/min-max offset formula.
        outside=np.ones(512,dtype=bool)
        outside[P+Q]=False
        R=H[:,outside].astype(np.int32)@(1-2*f[outside]).astype(np.int32)
        normalized=phase_p*R
        allowed=[]; zero=[]
        alive=np.ones(65536,dtype=bool)
        for h in range(16):
            group0=all_a[(dual==h)&(phase_qp==1)]
            group1=all_a[(dual==h)&(phase_qp==-1)]
            assert len(group0)==len(group1)==16
            allowrow=[]; zerorow=[]
            for A in range(-16,17,2):
                # Each individual original Walsh inequality contributes
                # directly to an interval for the second half coefficient.
                lower=max([-28-int(normalized[a])-A for a in group0]+[int(normalized[a])+A-28 for a in group1])
                upper=min([28-int(normalized[a])-A for a in group0]+[int(normalized[a])+A+28 for a in group1])
                lo=max(0,(lower+17)//2)
                hi=min(16,(upper+16)//2)
                mask=(cumulative[h][hi]^(cumulative[h][lo-1] if lo else 0)) if 0<=lo<=hi<=16 else 0
                allowrow.append(mask)
                targets={-int(normalized[a])-A for a in group0}|{int(normalized[a])+A for a in group1}
                z=0
                for B in targets:
                    if B%2==0 and -16<=B<=16: z|=exact[h][(B+16)//2]
                zerorow.append(z)
            allowed.append(allowrow); zero.append(zerorow)
            alive &= np.array([bool(m) for m in allowrow],dtype=bool)[values[:,h]]
        assert int(np.count_nonzero(alive))==case['first_half_patterns_after_individual_filters']
        count=0; countbalanced=0
        digest=hashlib.sha256()
        originalA=sum(int(f[x])<<j for j,x in enumerate(P))
        originalB=sum(int(f[x])<<j for j,x in enumerate(Q))
        for i in np.flatnonzero(alive).tolist():
            legal=(1<<65536)-1
            for h in reversed(range(16)):
                legal &= allowed[h][int(values[i,h])]
                if not legal: break
            if not legal: continue
            count+=bin(legal).count('1')
            z=0
            for h in reversed(range(16)): z|=zero[h][int(values[i,h])]
            countbalanced+=bin(z&legal).count('1')
            digest.update(i.to_bytes(4,'little')); digest.update(legal.to_bytes(8192,'little'))
            if p==core: all_rigid &= legal==(1<<originalB)
            elif q==core: all_rigid &= i==originalA
            else: all_rigid &= i==originalA and legal==(1<<originalB)
        assert count==case['assignments_preserving_bound']
        assert countbalanced==case['assignments_preserving_bound_and_giving_a_zero']==0
        assert digest.hexdigest()==case['legal_second_half_bitsets_sha256']
        assert case['half_patterns_catalogued']==65536 and case['full_assignments_covered']==2**32
        assert case['first_target_pair'] is None
        assert count==(448 if core in (p,q) else 1)
        total_legal+=count
        if number%100==0: print(name,'independently audited cases',number,flush=True)
    assert all_rigid
    # An attaining balanced 240 table belongs to the union: remove its
    # output shift and check that every change lies in the core coset.
    witness=json.loads(Path(flat['attainer']).read_text())
    a=witness['linear_shift']
    support=[x for x,b in enumerate(map(int,witness['bits'])) if b^(bin(a&x).count('1')%2)^int(f[x])]
    assert set(support)<=set(core^v for v in V)
    subprocess.run(['python3','code/check_witness.py',flat['attainer'],'--min-nl','240'],check=True)
    result={'status':'PASS','seed':name,'cases_exhausted':496,'complete_half_catalogue_size':65536,'full_assignments_covered_per_case':2**32,'all_512_character_block_rows_checked':True,'balanced_target_assignments':0,'exact_maximum_balanced_nonlinearity_of_union':240,'all_bound_preserving_tables_change_only_the_core_coset':True,'total_bound_preserving_assignments_with_pair_multiplicity':total_legal,'source_result_sha256':hashlib.sha256(Path(args.path).read_bytes()).hexdigest(),'verification_scope':'complete catalogue and set-intersection coverage, with universal block-character identity; no sampling of the 2^32 assignment range'}
    if args.output: Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True),flush=True)


if __name__=='__main__': main()
