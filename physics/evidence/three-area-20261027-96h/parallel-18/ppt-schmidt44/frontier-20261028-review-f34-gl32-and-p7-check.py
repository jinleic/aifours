#!/usr/bin/env python3
"""Independent exact GL(3,2) coset and P7-support checks.

Finite verification of GL(3,2) incidence/completion and a squarefree
necessary-condition overapproximation, not a Sun7 or general descent proof.
"""
from collections import Counter, deque
from math import gcd, prod
import json


def act(m, x):
    return (m[0] if x & 1 else 0) ^ (m[1] if x & 2 else 0) ^ (m[2] if x & 4 else 0)


def cov(alpha, m):
    return sum(((alpha & col).bit_count() & 1) << j for j, col in enumerate(m))


def gl32():
    matrices = [(a,b,c) for a in range(1,8) for b in range(1,8) if b!=a
                for c in range(1,8) if c not in (a,b,a^b)]
    idx = {m:i for i,m in enumerate(matrices)}
    table = [[idx[tuple(act(a,x) for x in b)] for b in matrices] for a in matrices]
    return matrices, table, idx[(1,2,4)]


def bit_indices(mask):
    while mask:
        bit=mask & -mask
        yield bit.bit_length()-1
        mask ^= bit


def closure(gens, table, identity):
    found=1<<identity
    todo=[identity]
    while todo:
        x=todo.pop()
        for g in gens:
            y=table[x][g]; bit=1<<y
            if not found & bit:
                found|=bit; todo.append(y)
    return found


def subgroup_enumeration(table, identity):
    n=len(table); seen={1<<identity:()}; todo=deque(seen)
    while todo:
        h=todo.popleft(); gens=seen[h]
        for g in range(n):
            if not h & (1<<g):
                ng=gens+(g,); nh=closure(ng,table,identity)
                if nh not in seen: seen[nh]=ng; todo.append(nh)
    for h in seen:
        members=list(bit_indices(h))
        if any(not h & (1<<table[x][y]) for x in members for y in members):
            raise AssertionError('bad subgroup closure')
    return list(seen)


def all_cosets(table, subs):
    n=len(table); out=[]
    for h in subs:
        members=list(bit_indices(h)); left=(1<<n)-1
        while left:
            g=(left & -left).bit_length()-1
            c=sum(1<<table[g][x] for x in members)
            if c.bit_count()!=len(members) or c & ~left: raise AssertionError('bad coset')
            left ^= c
            out.append((n//len(members),c))
    return out


def incidence_checks(matrices, actual_index7):
    records=[]
    for p in range(1,8):
        for a in range(1,8):
            records.append(('P',p,a,sum(1<<j for j,m in enumerate(matrices) if act(m,p)==a)))
    for alpha in range(1,8):
        for beta in range(1,8):
            records.append(('L',alpha,beta,sum(1<<j for j,m in enumerate(matrices) if cov(alpha,m)==beta)))
    masks=[x[3] for x in records]
    if len(set(masks))!=98 or set(masks)!=set(actual_index7):
        raise AssertionError('labelled cosets do not equal all actual index-seven cosets')
    adjacency=[0]*98
    for i in range(98):
        ty,p,a,mi=records[i]
        for j in range(i+1,98):
            ty2,p2,a2,mj=records[j]
            disjoint=not (mi & mj)
            if ty==ty2:
                predicted=(p==p2 and a!=a2) or (p!=p2 and a==a2)
            else:
                if ty=='L':
                    alpha,beta,pnt,target=p,a,p2,a2
                else:
                    pnt,target,alpha,beta=p,a,p2,a2
                predicted=((beta & pnt).bit_count() & 1)!=((alpha & target).bit_count() & 1)
            if predicted!=disjoint: raise AssertionError(('incidence mismatch',i,j))
            if disjoint: adjacency[i]|=1<<j; adjacency[j]|=1<<i
    all_group=(1<<len(matrices))-1
    lookup={m:i for i,m in enumerate(masks)}
    count=0; multiplicity=Counter(); types=Counter()

    def explore(candidates, chosen, covered):
        nonlocal count
        if len(chosen)==6:
            count+=1
            complement=all_group ^ covered
            matches=int(complement in lookup)
            multiplicity[matches]+=1
            types[sum(records[i][0]=='P' for i in chosen)]+=1
            return
        need=6-len(chosen)
        while candidates.bit_count()>=need:
            bit=candidates & -candidates; i=bit.bit_length()-1; candidates^=bit
            explore(candidates & adjacency[i],chosen+(i,),covered|masks[i])

    explore((1<<98)-1,(),0)
    return {'labels':len(records),'pair_relations_checked':98*97//2,'six_sets':count,
            'completion_multiplicity':dict(multiplicity),'six_sets_by_point_cosets':dict(sorted(types.items()))}


def p7_supports():
    primes=(2,3,5,7)
    vals=sorted(prod(p for j,p in enumerate(primes) if mask & (1<<j)) for mask in range(1,16))
    stages=[1]+[0]*8; seven=0; nonseven=0
    def visit(values):
        nonlocal seven,nonseven
        k=len(values)
        if k==8:
            if sum(v%7==0 for v in values)>=3:
                seven+=1
                if any(v%7 for v in values): nonseven+=1
            return
        for a in vals:
            if values and a<values[-1]: continue
            if all(2<=gcd(a,b)<=7 for b in values):
                stages[k+1]+=1; visit(values+(a,))
    visit(())
    return {'prefix_counts':stages,'eight_supports_with_three_sevens':seven,
            'such_supports_with_nonseven':nonseven}


def main():
    matrices,table,identity=gl32()
    subgroups=subgroup_enumeration(table,identity)
    cosets=all_cosets(table,subgroups)
    index7=[m for i,m in cosets if i==7]
    print(json.dumps({'group_order':len(matrices),'subgroups':len(subgroups),
                      'subgroups_by_index':dict(sorted(Counter(len(matrices)//x.bit_count() for x in subgroups).items())),
                      'actual_left_cosets':len(cosets),
                      'incidence':incidence_checks(matrices,index7),
                      'p7_squarefree':p7_supports()},indent=2))


if __name__=='__main__': main()
