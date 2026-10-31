#!/usr/bin/env python3
"""Exact quotient screens for every candidate rank-13 local-plane subcode.

The accompanying written classification reduces candidates to five
three-component triangle covers and eight disjoint-triangle packings with
seven nonzero choices at the remaining vertex. No solver is used.
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-triangle-baseline-result.json'
EXPECTED='1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82'
OUTPUT=ROOT/'frontier-20261028-rank13-all-local-subcodes-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}


def rank(rows):
    piv={}
    for x in rows:
        while x:
            p=x.bit_length()-1
            if p in piv:x ^= piv[p]
            else:piv[p]=x;break
    return len(piv)


def span(values):
    result={0}
    for x in values:result |= {z^x for z in tuple(result)}
    return result


def components(indices,triangles):
    left=set(indices);out=[]
    while left:
        part={left.pop()};changed=True
        while changed:
            changed=False
            for j in tuple(left):
                if any(set(triangles[j])&set(triangles[k]) for k in part):
                    part.add(j);left.remove(j);changed=True
        out.append(sorted(part))
    return sorted(out)


def main():
    raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    tri=[tuple(x) for x in json.loads(raw)['chosen_triangles']]
    if len(tri)!=10 or len(set(tri))!=10:raise ValueError('TRIANGLES')
    if any(all(y in N[x] for x,y in combinations(q,2)) for q in combinations(range(1,11),4)):
        raise ValueError('K4')
    occ={v:[j for j,t in enumerate(tri) if v in t] for v in range(1,11)}
    if any(len(o)!=3 for o in occ.values()):raise ValueError('COVER')
    if any(any(y not in N[x] for x,y in combinations(t,2)) for t in tri):raise ValueError('NOT_TRIANGLE')
    form={}
    for j,t in enumerate(tri):
        for p,v in enumerate(t):
            form[v,j]=(1<<(2*j)) if p==0 else (1<<(2*j+1)) if p==1 else (3<<(2*j))
    candidates=[]
    for inds in combinations(range(10),4):
        if len(set().union(*(set(tri[j]) for j in inds)))==10 and len(components(inds,tri))==3:
            picks={v:[j for j in occ[v] if j in inds] for v in range(1,11)}
            candidates.append(('cover',inds,None,None,picks))
    covercount=len(candidates)
    packcount=0
    for inds in combinations(range(10),3):
        if len(set().union(*(set(tri[j]) for j in inds)))!=9:continue
        missing=next(v for v in range(1,11) if all(v not in tri[j] for j in inds));packcount+=1
        for mask in range(1,8):
            picks={v:([j for i,j in enumerate(occ[v]) if mask&(1<<i)] if v==missing
                      else [j for j in occ[v] if j in inds]) for v in range(1,11)}
            candidates.append(('packing',inds,missing,mask,picks))
    if covercount!=5 or packcount!=8 or len(candidates)!=61:raise ValueError('CLASSIFICATION_COUNTS')
    records=[]
    for kind,inds,missing,mask,picks in candidates:
        local=[]
        for v in range(1,11):
            if not picks[v]:raise ValueError('EMPTY_LOCAL_FORM')
            x=0
            for j in picks[v]:x ^= form[v,j]
            local.append(x)
        rows=[]
        for x in local:
            if rank(rows+[x])>len(rows):rows.append(x)
        if len(rows)!=7 or any(rank(rows+[form[v,j] for j in occ[v]])-7!=2 for v in range(1,11)):
            raise ValueError(('RANK',kind,inds,missing,mask))
        rspace={0:0}
        for i,x in enumerate(rows):
            for y,k in tuple(rspace.items()):rspace[y^x]=k^(1<<i)
        lam=[rspace[x] for x in local]
        g_of_r=[sum((((lam[v-1]&r).bit_count()&1)<<(v-1)) for v in range(1,11)) for r in range(128)]
        inverse={g:r for r,g in enumerate(g_of_r)}
        if len(inverse)!=128:raise ValueError('QUOTIENT_RANK')
        tags={}
        for j,t in enumerate(tri):
            for p,v in enumerate(t):
                c=(1<<(2*j+p)) if p<2 else 0
                r=sum(((c&x).bit_count()&1)<<i for i,x in enumerate(rows))
                tags[v,j]=(1<<j)|(r<<10)
        bad=set()
        for v in range(1,11):
            non=set(range(1,11))-set(N[v])-{v}
            other=span([tags[u,j] for u in non for j in occ[u]])
            own=[tags[v,j] for j in occ[v]]
            for bitset in range(1,8):
                x=0
                for i in range(3):
                    if bitset&(1<<i):x ^= own[i]
                bad.update(x^y for y in other)
        if 0 in bad:raise ValueError('K_FD')
        off_basis=[sum(1<<(v-1) for v in range(1,11)
                       if j in picks[v] and tri[j].index(v)==2) for j in range(10)]
        off=[0]*1024
        for s in range(1,1024):
            lo=s&-s;off[s]=off[s^lo]^off_basis[lo.bit_length()-1]
        zero=[];single={}
        for s in range(1024):
            for v in range(11):
                target=0 if v==0 else 1<<(v-1)
                r=inverse.get(target^off[s])
                if r is None or (s|(r<<10)) in bad:continue
                if v==0:zero.append([s,r])
                else:single.setdefault(v,[]).append([s,r])
        if zero!=[[0,0]]:raise ValueError(('ZERO_CLASS_ANOMALY',kind,inds,missing,mask,zero))
        if len(single)>2:raise ValueError(('MORE_SINGLETONS',kind,inds,missing,mask,single))
        records.append({'kind':kind,'selected_triangles':inds,'remaining_vertex':missing,
                        'remaining_vertex_local_mask':mask,'K_rank':13,'vertex_image_ranks':[2]*10,
                        'forbidden_quotient_classes':len(bad),'zero_pattern_allowed':zero,
                        'allowed_singleton_vertices':sorted(single),'allowed_singleton_counts':{str(v):len(a) for v,a in single.items()}})
    out={'baseline_result_sha256':EXPECTED,'triangle_cover_candidates':covercount,
         'disjoint_triangle_packings':packcount,'remaining_vertex_local_choices':7,
         'candidate_subcodes_checked':len(records),'K_rank':13,'case_records':records,
         'all_zero_patterns_have_only_baseline_class':True,'max_allowed_singleton_vertices':max(len(x['allowed_singleton_vertices']) for x in records),
         'limits':'Completeness relies on the accompanying written dependency classification. It rules out one equal-weight target inside this parity-code family, not general laws.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='case_records'},indent=2))


if __name__=='__main__':main()
