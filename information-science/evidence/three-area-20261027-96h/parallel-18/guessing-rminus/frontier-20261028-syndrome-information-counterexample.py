#!/usr/bin/env python3
"""Exact counterexample to a tempting syndrome-information inequality.

An existing 88-word binary FD support is embedded into the first coordinate
of the q=8 triangle cover. Entropy comparisons are reduced to integers.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'frontier-20261028-triangle-baseline-result.json'
BASE_HASH='1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82'
LAW=ROOT/'frontier-20261028-fd-law-search-precise-result.json'
LAW_HASH='c82613f4fb2ae9f70192eedf73c5cc755de332e3be4d8cb0ddedc20899586bfc'
OUT=ROOT/'frontier-20261028-syndrome-information-counterexample-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}


def get(path,expected):
    raw=path.read_bytes()
    if sha256(raw).hexdigest()!=expected:raise ValueError(('INPUT_HASH',path.name))
    return json.loads(raw)


def count_product(cnt):
    out=1
    for x in cnt.values():out*=x**x
    return out


def main():
    triangles=[tuple(t) for t in get(BASE,BASE_HASH)['chosen_triangles']]
    words=get(LAW,LAW_HASH)['support_words_one_based_bitsets'];n=len(words)
    if n!=88 or len(set(words))!=n or any(not 0<=w<1024 for w in words):raise ValueError('WORDS')
    for x,y in combinations(words,2):
        d=x^y
        if any(d&(1<<(v-1)) and all(not d&(1<<(u-1)) for u in N[v]) for v in range(1,11)):
            raise ValueError(('FD',x,y))
    occurrence={v:[j for j,t in enumerate(triangles) if v in t] for v in range(1,11)}
    if any(len(z)!=3 for z in occurrence.values()):raise ValueError('COVER')
    def sigma(w):
        return sum((sum((w>>(v-1))&1 for v in t if occurrence[v][0]==j)%2)<<j
                   for j,t in enumerate(triangles))
    sc=Counter(sigma(w) for w in words);left=count_product(sc)**17;right=n**(17*n)
    for v in range(1,11):
        singles=Counter((w>>(v-1))&1 for w in words)
        joint=Counter((((w>>(v-1))&1),sigma(w)) for w in words)
        left*=count_product(singles)**2;right*=count_product(joint)**2
    if left<=right:raise ValueError('INEQUALITY_NOT_REFUTED')
    out={'base_sha256':BASE_HASH,'binary_support_sha256':LAW_HASH,'uniform_support_size':n,
         'q8_embedding':'Each vertex symbol is (binary bit,0,0) in its triangle-occurrence component order.',
         'all_pairwise_original_neighbour_FDs_checked':n*(n-1)//2*10,
         'syndrome_distribution':dict(sorted(sc.items())),
         'exact_entropy_claim':'3 H(S) > 2 sum_v I(X_v;S), for base-two or any common logarithm base',
         'integer_comparison_L_gt_R':True,'L_bits':left.bit_length(),'R_bits':right.bit_length(),
         'integer_comparison':'L=(prod_s n_s^n_s)^17 * prod_v(prod_b n_vb^n_vb)^2; R=n^(17n)*prod_v(prod_bs n_vbs^n_vbs)^2',
         'limits':'This refutes only the proposed syndrome-information inequality. It does not establish or refute any improved R-minus guessing-number bound.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
