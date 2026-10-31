#!/usr/bin/env python3
"""Find an actual two-sign word with no triangle of low-M reflection pairs."""
import argparse
import itertools
import json


def find_prefix(p,m,n):
    F=p+3
    visited=0
    path=[0]
    edges=[]
    def low(u):
        return m-u<=2*p-2 and n+u<=2*p-2
    def rec(plus,minus):
        nonlocal visited
        visited+=1
        if len(path)==F:
            return list(path)
        current=path[-1]
        # Minimize budget spent: every proposed prefix increment is realized
        # by a monotone block in that gap, with all unused rotations outside.
        increments=sorted(range(-(n-minus),m-plus+1),key=lambda x:(abs(x),x))
        for delta in increments:
            nxt=current+delta
            if any(low(path[b]-path[a]) and low(nxt-path[a]) and low(nxt-path[b]) for a,b in edges):
                continue
            pp=plus+max(delta,0)
            nn=minus+max(-delta,0)
            new_edges=[(i,len(path)) for i,q in enumerate(path) if low(nxt-q)]
            path.append(nxt)
            edges.extend(new_edges)
            result=rec(pp,nn)
            if result is not None:
                return result
            del path[-1]
            if new_edges:
                del edges[-len(new_edges):]
        return None
    return rec(0,0),visited


def materialize(p,m,n,prefixes):
    plus=minus=0
    word=[[0,1]]
    for before,after in zip(prefixes,prefixes[1:]):
        d=after-before
        plus+=max(d,0)
        minus+=max(-d,0)
        word.extend([[1,0]]*max(d,0))
        word.extend([[p-1,0]]*max(-d,0))
        word.append([0,1])
    word.extend([[1,0]]*(m-plus))
    word.extend([[p-1,0]]*(n-minus))
    return word


def verify(p,m,n,prefixes,word):
    R=3*p-4
    if len(word)!=4*p-1 or sum(b==0 for _,b in word)!=R:
        raise ValueError('not full actual original word')
    refs=[i for i,(_,b) in enumerate(word) if b]
    if len(refs)!=p+3:
        raise ValueError('reflection count')
    low=[]
    for i,j in itertools.combinations(refs,2):
        signed=[(-a if i<k<j else a)%p for k,(a,b) in enumerate(word) if not b]
        M=max(signed.count(1),signed.count(p-1))
        if M<=2*p-2:
            low.append((i,j))
    edge=set(low)
    if any((i,j) in edge and (j,k) in edge and (i,k) in edge for i,j,k in itertools.combinations(refs,3)):
        raise ValueError('unexpected low-M triangle')
    return len(low)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    p=5
    results=[]
    for m,n in ((2*p-1,p-3),(2*p-2,p-2),(2*p-3,p-1)):
        prefixes,visited=find_prefix(p,m,n)
        if prefixes is None:
            results.append({'p':p,'m':m,'n':n,'no_witness_found':True,'visited_nodes':visited})
            continue
        word=materialize(p,m,n,prefixes)
        low=verify(p,m,n,prefixes,word)
        results.append({'p':p,'m':m,'n':n,'prefixes':prefixes,'word':word,
                        'low_pair_edges':low,'visited_nodes':visited})
    result={'result':'BOUNDED_PREFIX_SEARCH_COMPLETED','cases':results,
            'scope':'obstruction to triangle-only method; no avoidance or full theorem claim'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
