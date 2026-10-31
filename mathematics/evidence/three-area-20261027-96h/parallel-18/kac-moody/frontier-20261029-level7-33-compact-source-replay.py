#!/usr/bin/env python3
"""Alternate complete normalized270-source bytes and Hadamard Gram replay.

Old independently implemented literal Lyndon algebra is pinned through its
frozen evidence manifest; NO compact-source producer is imported. The Gram
uses the Hadamard-diagonal tensor expression, not full-source G application.
"""
import argparse
import hashlib
import importlib.util
import io
import json
import math
from collections import Counter,defaultdict
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
MANIFEST='frontier-20261029-level7-33-actual-quotient-bound3-manifest-v1.json'
MANIFEST_SHA='d052b3d1a3fb8ed4b65c3a302844b3942708e38bacf757b14f489ed813a0cf36'
LITERAL='frontier-20261029-invariant-actual22-corner-replay.py'
LITERAL_SHA='a1cf8aa7d4b085384bdc48e01978bd56f20beff5c4b8faf9b61eea3621b6d8d6'


def raw_pin(name,sha):
    assert isinstance(name,str) and Path(name).name==name
    raw=(ROOT/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
    return raw


def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser();ap.add_argument('--sha256',required=True);args=ap.parse_args()
    name='frontier-20261029-level7-33-compact-source-v1.json'
    C=json.loads(raw_pin(name,args.sha256))
    manifest=json.loads(raw_pin(MANIFEST,MANIFEST_SHA))
    for pin in manifest['files']:
        if pin['file'].endswith('.py'):raw_pin(pin['file'],pin['sha256'])
    raw_pin(LITERAL,LITERAL_SHA)
    L=load('literal_matrix_gram_tools',LITERAL);F=L.flint
    old=load('pinned_independent_full_primitive_replay','frontier-20261029-level7-canonical-independent-replay.py')
    S=json.loads(raw_pin(C['source']['file'],C['source']['sha256']))
    prior=json.loads(raw_pin(C['completed_input_source_replay']['file'],C['completed_input_source_replay']['sha256']))
    assert S['degree']==C['degree']==[3,3,7]
    assert prior['all_free_source_membership_and_Witt_completeness_checked']
    assert prior['source_pencil_sha256']==C['source']['sha256']
    G,degrees=L.literal_module()
    states={(0,0):['']}
    for _ in range(7):
        nxt=defaultdict(list)
        for (a,b),prefixes in states.items():
            for j,(da,db) in enumerate(degrees):
                if a+da<=3 and b+db<=3:nxt[a+da,b+db].extend(p+str(j) for p in prefixes)
        states=nxt
    universe=sorted(states[3,3]);assert len(universe)==5376
    codes=np.array([L.code(tuple(map(int,w))) for w in universe],dtype=np.uint32)
    words,V=[L.array(pin) for pin in C['files']]
    assert words.dtype==np.dtype('uint32') and V.dtype==np.dtype('int64')
    assert np.array_equal(codes,words) and V.shape==(270,5376)
    assert tuple(S['source_words'])==old.ind.lyndon_words((3,3,7))
    assert old.seventh_dimensions(3,3)==(768,270)
    expansions=[old.ind.ind.standard_bracket(w) for w in S['source_words']]
    lookup={w:i for i,w in enumerate(universe)}
    rebuilt=np.zeros_like(V);denominators=[]
    for i,row in enumerate(S['horizontal_kernel_coefficients']):
        parsed={int(j):Q(c) for j,c in row.items()}
        den=math.lcm(*(c.denominator for c in parsed.values()));denominators.append(den)
        vector=Counter()
        for j,c in parsed.items():
            multiplier=int(c*den)
            for w,b in expansions[j].items():
                assert Q(b).denominator==1
                vector[w]+=multiplier*int(b)
        assert all(abs(int(c))<2**63 for c in vector.values())
        for w,c in vector.items():rebuilt[i,lookup[w]]=c
    assert denominators==C['row_denominators']
    assert np.array_equal(rebuilt,V)
    for data,pin in zip((codes,rebuilt),C['files']):
        stream=io.BytesIO();np.save(stream,data,allow_pickle=False)
        assert hashlib.sha256(stream.getvalue()).hexdigest()==pin['sha256']
    print('PASS alternate complete270 normalized source and BOTH NPY byte identities',flush=True)

    # Fresh finite-matrix Gram verifies the universal diagonalization used.
    assert G[3][3]==G[4][4]==2 and G[3][4]==G[4][3]==1 and G[7][7]==4
    W=rebuilt.copy();zero=np.zeros(5376,dtype=np.int64);three=zero.copy();seven=zero.copy()
    positions={int(w):i for i,w in enumerate(codes)}
    peak=max(abs(int(W.min())),abs(int(W.max())))
    for pos in range(7):
        assert peak*2**(pos+1)<2**63
        shift=3*(6-pos);letters=(codes>>shift)&7
        c3=np.flatnonzero(letters==3)
        c4=np.array([positions[int(codes[i])^(7<<shift)] for i in c3],dtype=np.int64)
        a=W[:,c3].copy();b=W[:,c4].copy();W[:,c3]=a+b;W[:,c4]=a-b
        zero+=(letters==3)|(letters==4);three+=(letters==3);seven+=(letters==7)
    weights=np.array([2**(7-int(z))*3**int(t)*4**int(s) for z,t,s in zip(zero,three,seven)],dtype=np.int64)
    weighted_bound=max(abs(int(W.min())),abs(int(W.max())))*int(weights.max())
    assert weighted_bound<2**63
    weighted=W*weights
    scaled=F.fmpz_mat(weighted.tolist())*F.fmpz_mat(W.tolist()).transpose()
    expected=F.fmpz_mat([[int(c) for c in row] for row in C['source_gram']])
    assert scaled==128*expected
    assert expected==expected.transpose() and expected.det()
    result={'owner':'MathKacMoody-2','input_file':name,'input_sha256':args.sha256,
            'source':C['source'],'prior_full_source_replay':C['completed_input_source_replay'],
            'pinned_literal_code_manifest':{'file':MANIFEST,'sha256':MANIFEST_SHA},
            'literal_matrix_helper':{'file':LITERAL,'sha256':LITERAL_SHA},
            'complete_normalized_source_vectors_reconstructed':270,
            'entire_tensor_word_count':5376,'both_source_NPY_files_regenerated_byte_for_byte':True,
            'all_compact_Gram_entries_independently_reconstructed':72900,
            'diagonal_source_basis_change_verified':True,
            'Hadamard_weighted_entry_int64_bound':weighted_bound,
            'Gram_arithmetic':'FLINT arbitrary integers; all tensor entries have explicit signed-int64 bounds',
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'numpy_version':np.__version__,'flint_version':F.__version__,
            'status':'PASS_ENTIRE_NORMALIZED270_SOURCE_BYTES_AND_HADAMARD_GRAM',
            'limits':'Separate existing literal Lyndon implementation and different whole Gram formula; same owner and NumPy/FLINT libraries. Original full source membership/completeness replay is reused and bound, not rerun. No actual small-row quotient or D3-rank result, parent, formal/kernel, configured-family/human, native-library or novelty acceptance.'}
    output=ROOT/'frontier-20261029-level7-33-compact-source-replay-v1.json'
    with output.open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print('PASS complete270 compact source and entire Gram',output.name,flush=True)


if __name__=='__main__':main()
