#!/usr/bin/env python3
"""Independently decode and verify all 174251 syndrome-plane clique witnesses.

No producer modules or precomputed forbidden-difference sets are imported.
Each of the three nonzero words is checked against the original graph.
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'frontier-20261028-triangle-baseline-result.json'
BASE_HASH='1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82'
CERT=ROOT/'frontier-20261028-all-syndrome-planes-certificate-result.json'
CERT_HASH='e607cd0ff871cf744193c50cd70476759a465a5b45f020706afc5cabe4f261af'
OUTPUT=ROOT/'frontier-20261028-all-syndrome-planes-independent-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}


def pin(path,digest):
    raw=path.read_bytes()
    if sha256(raw).hexdigest()!=digest:raise ValueError(('HASH',path.name))
    return json.loads(raw)


def main():
    triangles=[tuple(t) for t in pin(BASE,BASE_HASH)['chosen_triangles']]
    source=pin(CERT,CERT_HASH);records=source['special_witnesses'];special={}
    for row in records:
        key=(row['syndrome_a'],row['syndrome_b'])
        if key in special:raise ValueError(('DUPLICATE',key))
        special[key]=(row['code_coeff_a'],row['code_coeff_b'])
    if len(special)!=174:raise ValueError('SPECIAL_COUNT')
    if len(triangles)!=10 or any(sum(v in t for t in triangles)!=3 for v in range(1,11)):
        raise ValueError('COVER')
    if any(any(b not in N[a] for a,b in combinations(t,2)) for t in triangles):raise ValueError('NONTRIANGLE')
    if any(all(b in N[a] for a,b in combinations(q,2)) for q in combinations(range(1,11),4)):
        raise ValueError('K4')
    occurrences={v:[j for j,t in enumerate(triangles) if v in t] for v in range(1,11)}
    pos={(v,j):3*(v-1)+occurrences[v].index(j) for v in occurrences for j in occurrences[v]}
    vmask={v:7<<(3*(v-1)) for v in range(1,11)}
    neighmask={v:sum(vmask[u] for u in N[v]) for v in range(1,11)}
    tmask=[sum(1<<pos[v,j] for v in t) for j,t in enumerate(triangles)]
    stars={v:sum(1<<j for j,t in enumerate(triangles) if v in t) for v in range(1,11)}
    def syndrome(word):return sum(((word&mask).bit_count()&1)<<j for j,mask in enumerate(tmask))
    def bad(word):return any((word&vmask[v]) and not (word&neighmask[v]) for v in range(1,11))
    def decode(s,c):
        if not 0<=c<1<<20:raise ValueError('COEFFICIENT_RANGE')
        word=0
        for j,t in enumerate(triangles):
            a,b=(c>>(2*j))&1,(c>>(2*j+1))&1
            for u,bit in zip(t,(a,b,a^b^((s>>j)&1))):
                if bit:word |= 1<<pos[u,j]
        return word
    # For common-isolating-vertex cases independently materialize the actual
    # 30-bit differences, not the producer's 20-bit forbidden sets.
    maps={}
    for v in range(1,11):
        non=set(range(1,11))-set(N[v])-{v};basis=[]
        for j,t in enumerate(triangles):
            u=v if v in t else next(u for u in t if u in non)
            basis.append(1<<pos[u,j])
        table=[0]*1024
        for s in range(1,1024):
            bit=s&-s;table[s]=table[s^bit]^basis[bit.bit_length()-1]
        maps[v]=table
    planes=common=extra=checks=0;used=set()
    for a in range(1,1024):
        for b in range(a+1,1024):
            if (a^b)<b:continue
            planes+=1
            v=next((v for v in range(1,11) if (a&stars[v]) and (b&stars[v])
                    and (a&stars[v])!=(b&stars[v])),None)
            if v is None:
                if (a,b) not in special:raise ValueError(('MISSING_SPECIAL',a,b))
                x,y=special[a,b];d1,d2=decode(a,x),decode(b,y);used.add((a,b));extra+=1
            else:
                if (a,b) in special:raise ValueError(('UNEXPECTED_SPECIAL',a,b))
                d1,d2=maps[v][a],maps[v][b];common+=1
            for d,s in ((d1,a),(d2,b),(d1^d2,a^b)):
                if syndrome(d)!=s or not bad(d):raise ValueError(('WITNESS',a,b,s))
                checks+=1
    if used!=set(special) or planes!=174251 or common!=174077 or extra!=174 or checks!=522753:
        raise ValueError('COUNTS')
    out={'baseline_result_sha256':BASE_HASH,'certificate_sha256':CERT_HASH,
         'all_graph_K4_checks':210,'planes_checked':planes,'common_vertex_planes':common,
         'special_planes':extra,'nonzero_30bit_differences_checked':checks,
         'syndrome_and_original_neighbour_isolation_checked':True,
         'limits':'Checks finite witnesses for q=8 binary triangle-code syndrome planes; the global guessing-number problem remains open.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
