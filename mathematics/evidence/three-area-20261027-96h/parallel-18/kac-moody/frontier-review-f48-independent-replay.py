#!/usr/bin/env python3
"""Independent exact Tuscan T1 trade and fixed-five-row completion replay.

Uses direct directed Hamilton-path recursion and independent bitset exact
cover.  The listed rows are copied from the two review candidates; no author
program or output JSON is imported.  Distances are linear, never cyclic.
"""
import itertools
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parent
N=11; SENTINEL=11; N12=12
A=[
(6,5,1,4,2,8,3,7,9,0,10),(2,4,7,6,9,10,1,3,8,5,0),
(10,2,1,0,7,3,5,8,6,4,9),(4,3,2,0,8,10,5,7,1,9,6),
(9,3,0,2,6,10,8,4,1,7,5),(3,6,1,10,0,4,8,9,5,2,7),
(1,2,5,6,8,0,3,10,9,7,4),(7,8,2,9,4,6,0,1,5,10,3),
(8,1,6,3,4,10,7,0,5,9,2),(5,4,0,9,8,7,10,6,2,3,1),
(0,6,7,2,10,4,5,3,9,1,8)]
B=[
(4,2,10,9,5,8,7,3,0,1,6),(6,9,2,4,7,1,8,5,0,10,3),
(4,10,7,2,1,0,3,5,9,8,6),(5,1,2,8,10,7,6,0,9,4,3),
(9,3,2,6,8,0,5,10,1,7,4),(8,0,2,9,6,1,3,7,10,4,5),
(10,8,1,4,6,2,5,3,9,7,0),(9,1,10,2,0,4,8,3,6,5,7),
(10,6,3,8,4,9,0,7,1,5,2),(2,3,1,8,9,10,5,4,0,6,7),
(3,10,0,8,2,7,5,6,4,1,9)]


def events(row,d):return [(row[i],row[i+d]) for i in range(N-d)]
def score(rows,d):
    c=Counter(pair for row in rows for pair in events(row,d))
    return {'events':sum(c.values()),'distinct':len(c),'pair_collisions':sum(v*(v-1)//2 for v in c.values())}
def bit12(i,j):return 1<<(i*N12+j)
def aug(row):
    seq=(SENTINEL,)+tuple(row)+(SENTINEL,)
    return sum(bit12(seq[i],seq[i+1]) for i in range(N+1))
def bit11(i,j):return 1<<(i*N+j)
def mask(row,d):return sum(bit11(i,j) for i,j in events(row,d))
FULL=sum(bit11(i,j) for i in range(N) for j in range(N) if i!=j)


def cycles(edge_mask):
    """Enumerate every Hamilton cycle rooted at sentinel via direct DFS."""
    path=[]
    def visit(last,used,edges):
        if len(path)==N:
            close=bit12(last,SENTINEL)
            if edge_mask&close:yield (tuple(path),edges|close)
            return
        for v in range(N):
            flag=1<<v; arc=bit12(last,v)
            if not used&flag and edge_mask&arc:
                path.append(v)
                yield from visit(v,used|flag,edges|arc)
                path.pop()
    yield from visit(SENTINEL,0,0)


def only_cycle(edge_mask):
    """Validate that a complement is exactly one directed Hamilton cycle."""
    successor=[]
    for u in range(N12):
        choices=[v for v in range(N12) if edge_mask&bit12(u,v)]
        if len(choices)!=1:return None
        successor.append(choices[0])
    seen={SENTINEL};row=[];u=SENTINEL
    for _ in range(N):
        u=successor[u]
        if u in seen or u==SENTINEL:return None
        seen.add(u);row.append(u)
    if successor[u]!=SENTINEL or len(seen)!=N12:return None
    if edge_mask!=aug(tuple(row)):return None
    return tuple(row)


def verify_trades(k):
    num_decompositions=0;num_first=0;minimum=None;case_minima=[]
    augrows=[aug(row) for row in A]
    for ids in itertools.combinations(range(N),k):
        removed=set(ids)
        fixed=[row for i,row in enumerate(A) if i not in removed]
        residual=0
        for i in ids:
            assert not residual&augrows[i]
            residual|=augrows[i]
        local_count=0;local_first=0;local_min=None
        for first,e1 in cycles(residual):
            local_first+=1
            rem=residual&~e1
            if k==2:
                second=only_cycle(rem)
                if second is None or first>second:continue
                candidates=(first,second)
                val=score(fixed+list(candidates),2)['pair_collisions']
                local_count+=1;local_min=val if local_min is None else min(local_min,val)
            else:
                for second,e2 in cycles(rem):
                    if first>second:continue
                    third=only_cycle(rem&~e2)
                    if third is None or second>third:continue
                    val=score(fixed+[first,second,third],2)['pair_collisions']
                    local_count+=1;local_min=val if local_min is None else min(local_min,val)
        assert local_count and local_min is not None
        num_first+=local_first;num_decompositions+=local_count
        minimum=local_min if minimum is None else min(minimum,local_min)
        case_minima.append({'rows_zero_indexed':ids,'first_cycles':local_first,
                            'decompositions':local_count,'min_d2_pair_collisions':local_min})
    return {'removed_rows':k,'cases':len(case_minima),'first_cycles':num_first,
            'decompositions':num_decompositions,'minimum':minimum,'per_case':case_minima}


def fixed_compatible(rows):
    if len({x[0] for x in rows})!=len(rows) or len({x[-1] for x in rows})!=len(rows):return False
    for d in (1,2):
        seen=0
        for row in rows:
            m=mask(row,d)
            if seen&m:return False
            seen|=m
    return True


def enumerate_eligible(fixed):
    used1=0;used2=0
    starts=sum(1<<row[0] for row in fixed);ends=sum(1<<row[-1] for row in fixed)
    for row in fixed:used1|=mask(row,1);used2|=mask(row,2)
    answer=[];prefix=[]
    def search(used,own1,own2):
        if len(prefix)==N:
            if not (ends>>prefix[-1])&1:
                answer.append((tuple(prefix),own1,own2,1<<prefix[0],1<<prefix[-1]))
            return
        for v in range(N):
            bit=1<<v
            if used&bit or (not prefix and starts&bit):continue
            a1=bit11(prefix[-1],v) if prefix else 0
            a2=bit11(prefix[-2],v) if len(prefix)>=2 else 0
            if a1&used1 or a2&used2:continue
            prefix.append(v)
            search(used|bit,own1|a1,own2|a2)
            prefix.pop()
    search(0,0,0)
    return answer,used1,used2,starts,ends


def complete_fixed(fixed):
    eligible,u1,u2,starts,ends=enumerate_eligible(fixed)
    by_arc={i:[] for i in range(N*N)}
    for idx,(_,m1,_,_,_) in enumerate(eligible):
        bits=m1
        while bits:
            l=bits&-bits;by_arc[l.bit_length()-1].append(idx);bits-=l
    visited=0
    def recurse(mask1,mask2,st,en,depth):
        nonlocal visited
        visited+=1
        missing=FULL&~mask1
        if not missing:
            assert depth==N-len(fixed)
            return True
        best=None;bits=missing
        while bits:
            l=bits&-bits;arc=l.bit_length()-1;bits-=l
            choices=[]
            for j in by_arc[arc]:
                _,m1,m2,ss,ee=eligible[j]
                if not (m1&mask1 or m2&mask2 or ss&st or ee&en):choices.append(j)
            if not choices:return False
            if best is None or len(choices)<len(best):
                best=choices
                if len(best)==1:break
        for j in best:
            _,m1,m2,ss,ee=eligible[j]
            if recurse(mask1|m1,mask2|m2,st|ss,en|ee,depth+1):return True
        return False
    found=recurse(u1,u2,starts,ends,0)
    return {'eligible_rows':len(eligible),'search_nodes':visited,'completion_found':found}


def main():
    for rows in (A,B):
        assert len(rows)==N and all(sorted(row)==list(range(N)) for row in rows)
    A1,A2,B1,B2=score(A,1),score(A,2),score(B,1),score(B,2)
    assert (A1['distinct'],A1['pair_collisions'],A2['distinct'],A2['pair_collisions'])==(110,0,84,15)
    assert (B1['distinct'],B2['distinct'],B1['pair_collisions']+B2['pair_collisions'])==(106,95,8)
    pairs=verify_trades(2)
    assert (pairs['cases'],pairs['decompositions'],pairs['minimum'])==(55,65,15)
    triples=verify_trades(3)
    assert (triples['cases'],triples['first_cycles'],triples['decompositions'],triples['minimum'])==(165,6404,534,15)
    candidates=[ids for ids in itertools.combinations(range(N),5) if fixed_compatible([B[i] for i in ids])]
    assert len(candidates)==15
    five=[]
    for ids in candidates:
        res=complete_fixed([B[i] for i in ids])
        assert not res['completion_found']
        five.append({'rows_one_indexed':tuple(i+1 for i in ids),**res})
    path=ROOT/'frontier-review-f48-independent-replay-v1.json'
    if path.exists():raise FileExistsError(path)
    path.write_text(json.dumps({'A_distance1':A1,'A_distance2':A2,'B_distance1':B1,'B_distance2':B2,
                                'pairs':pairs,'triples':triples,'compatible_five_subsets':len(candidates),
                                'five_subset_replays':five,'all_five_completions_absent':True,
                                'method':'independent direct sentinel DFS and bitset exact-cover MRV; exact integer operations',
                                'not_formal_or_external_model_review':True},indent=2)+'\n',encoding='utf-8')
    print('PASS: A D1/D2 110/84, B D1/D2 106/95; all 55 pairs/165 triples; 15 compatible five-subsets exhausted; no completion')
    print('pair decompositions',pairs['decompositions'],'triple first cycles',triples['first_cycles'],
          'triple decompositions',triples['decompositions'],'min D2',triples['minimum'])
    print(path.name)


if __name__=='__main__':main()
