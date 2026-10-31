#!/usr/bin/env python3
"""Independent source-only replay for the 162-dimensional level-six case.

Replaces a timed-out monolithic replay by a bounded proof stage: Witt/Weyl
lowest dimension, independent tree-Lyndon basis, triangular coefficient
independence and entire horizontal maps checked columnwise. No determinant
or f3-entry claim is made here.
"""
import hashlib
import importlib.util
import json
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('independent',ROOT/'frontier-20261028-levi-critical-independent-replay.py')
ind=importlib.util.module_from_spec(spec);spec.loader.exec_module(ind)
DEGREE=(4,4,6)


def char_word(power,scale):
    out=Counter({(0,0):1})
    for _ in range(power):
        nxt=Counter()
        for (a,b),n in out.items():
            for x,y in ind.WEIGHTS:nxt[a+scale*x,b+scale*y]+=n
        out=nxt
    return out


def main():
    dest=ROOT/'frontier-20261028-level6-446-staged-source-replay-v1.json'
    if dest.exists():raise FileExistsError(dest)
    raw=(ROOT/'frontier-20261028-level6-446-leading-map-cone-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='606b1cfe1fdadf3d741b0d5aa649ac59a7fc7ca094ff68cf242096cc76adf3ed'
    P=json.loads(raw);assert P['status']=='LEADING_INJECTIVE_COFAC_CONE'
    terms=[char_word(6,1),char_word(3,2),char_word(2,3),char_word(1,6)]
    allweights=set().union(*map(set,terms));character={}
    for w in allweights:
        c=terms[0][w]-terms[1][w]-terms[2][w]+terms[3][w];assert c%6==0;character[w]=c//6
    def m(a,b):return character.get((a,b),0)
    mult=m(4,4)-m(3,4)-m(4,3)+m(2,3)+m(3,2)-m(2,2)
    words=P['source_words'];assert len(words)==m(4,4)==1116 and tuple(words)==ind.lyndon_words(DEGREE)
    coeffs=[{int(i):Q(q) for i,q in c.items()} for c in P['horizontal_kernel_coefficients']]
    assert len(coeffs)==mult==162
    ends=[max(c) for c in coeffs];assert len(set(ends))==len(ends) and all(c[e]==1 for c,e in zip(coeffs,ends))
    print('source words/triangular coefficient independence/Witt lowest dimension PASS',flush=True)
    # Compute independent horizontal actions of each Lyndon source just once.
    for g in ('f1','f2'):
        actions=[ind.act(ind.ind.standard_bracket(w),g,0,0) for w in words]
        for j,c in enumerate(coeffs):
            v={}
            for index,q in c.items():ind.ind.add_scaled(v,actions[index],q)
            assert not v,('horizontal residual',g,j)
        print('whole horizontal action',g,'PASS for all',len(coeffs),'vectors',flush=True)
    result={'degree':DEGREE,'leading_data_sha256':digest,'free_source_dim':len(words),'lowest_dimension':mult,
            'full_Lyndon_source_words_verified':True,'distinct_maximal_coefficient_indices_and_unit_leads':True,
            'all_162_f1_f2_actions_zero_in_full_tensor_target':True,
            'witt_weyl_lowest_multiplicity':mult,'status':'PASS_COMPLETE_INDEPENDENT_SOURCE_ONLY',
            'not_checked':'f3 target entries, leading determinant, Cartan/ideal proof, independent scientific review'}
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS complete independent level6 source: 1116 words and all 162 lowest vectors;',dest.name,flush=True)

if __name__=='__main__':main()
