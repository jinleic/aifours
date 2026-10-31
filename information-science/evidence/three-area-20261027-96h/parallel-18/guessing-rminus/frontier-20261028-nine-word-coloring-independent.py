#!/usr/bin/env python3
"""Independent lookup/decoder and wheel check for a pinned 9-word support."""
from hashlib import sha256
from itertools import combinations,product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-nine-word-coloring-obstruction-result.json','d47007043b84ee4b6e9ad88af271d7ecf29931235de98f0af2949b5aaa1c5415')
OUT=ROOT/'frontier-20261028-nine-word-coloring-independent-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
T=((1,2,3),(1,3,4),(2,3,9),(3,4,8),(3,8,9));W=(1,2,3,4,8,9)
E={tuple(sorted((v,w))) for v in W for w in N[v] if w in W}


def verify(words,expected_count=9):
    if len(words)!=expected_count:raise ValueError('COUNT')
    if any(len(row)!=10 or any(not isinstance(x,int) or not 0<=x<32 for x in row) for row in words):raise ValueError('ALPHABET')
    if len(set(map(tuple,words)))!=len(words):raise ValueError('DISTINCT')
    for v in range(1,11):
        lookup={}
        for word in words:
            key=tuple(word[w-1] for w in N[v]);out=word[v-1]
            if key in lookup and lookup[key]!=out:raise ValueError('FD')
            lookup[key]=out
            reconstructed=0
            for t,tri in enumerate(T):
                if v in tri:
                    others=[u for u in tri if u!=v]
                    reconstructed|=(((word[others[0]-1]>>t)^(word[others[1]-1]>>t))&1)<<t
            if reconstructed!=out:raise ValueError('DECODER')
    forced=set()
    for a,b in combinations(words,2):
        D=tuple(v for v in range(1,11) if a[v-1]!=b[v-1])
        if len(D)==2:forced.add(D)
    if len(E)!=10 or not E<=forced:raise ValueError('WHEEL_FORCE')
    valid=0
    for c in product(range(3),repeat=6):
        f=dict(zip(W,c));valid+=all(f[a]!=f[b] for a,b in E)
    if valid:raise ValueError('WHEEL_COLOR')
    # Exact uniform entropy comparison: product(block_size^(2 block_size)) vs m^(17m).
    m=len(words);left=1
    for i in range(10):
        counts={}
        for word in words:counts[word[i]]=counts.get(word[i],0)+1
        for size in counts.values():left*=size**(2*size)
    right=m**(17*m)
    return {'FD_neighbor_lookups_checked':10*len(words),'decoder_words_checked':10*len(words),
            'forced_wheel_edges':len(E),'proper_three_colorings':valid,
            'uniform_gap_positive':left>right,'uniform_gap_zero':left==right}


def main():
    raw=(ROOT/SOURCE[0]).read_bytes()
    if sha256(raw).hexdigest()!=SOURCE[1]:raise ValueError('HASH')
    src=json.loads(raw);words=src['words'];checks=verify(words);controls={}
    def reject(name,rows,reason,count=9):
        try:verify(rows,expected_count=count)
        except ValueError as exc:
            if str(exc)!=reason:raise ValueError(('WRONG_REASON',name,str(exc)))
            controls[name]=reason
        else:raise ValueError(('MUTATION_ACCEPTED',name))
    bad=[x[:] for x in words];bad[1]=bad[0][:];reject('duplicate_word',bad,'DISTINCT')
    bad=[x[:] for x in words];bad[1]=[0]*10;bad[1][4]=1;reject('single_vertex_conflict',bad,'FD')
    bad=[x[:] for x in words];bad[1][0]=32;reject('out_of_alphabet',bad,'ALPHABET')
    bad=[x[:] for i,x in enumerate(words) if i!=6];reject('missing_forced_edge_word',bad,'WHEEL_FORCE',8)
    out={'source_receipt_sha256':SOURCE[1],'exact_checks':checks,'all_checked':True,'mutation_controls':controls,
         'limits':'Finite support and decoder/color obstruction only. No claim of strict gain, general entropy bound or independent scientific review.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
