#!/usr/bin/env python3
"""Independent erasable-gap chart for one fixed same-rotation candidate."""
import argparse
import functools
import hashlib
import itertools
import json


def inverse(a,b,p):
    return a[1]==b[1] and ((a[0]==b[0]) if a[1] else (a[0]+b[0])%p==0)


def group_product(items,p):
    x,e=0,0
    for y,f in items:
        x=(x+(-y if e else y))%p
        e^=f
    return x,e


def good4(items,p):
    rot=[x for x,e in items if not e]
    ref=[x for x,e in items if e]
    if len(rot)!=2 or len(ref)!=2:return False
    A=sum(rot)%p
    B=(ref[0]-ref[1])%p
    C,e=group_product(items,p)
    return e==0 and (A!=B or C==2*A%p)


def erasable_table(seq,p):
    n=len(seq)
    D=[[False]*(n+1) for _ in range(n+1)]
    for i in range(n+1):D[i][i]=True
    for i in range(n):
        stack=[]
        for j in range(i,n):
            if stack and inverse(stack[-1],seq[j],p):stack.pop()
            else:stack.append(seq[j])
            D[i][j+1]=not stack
    return D


def chart(seq,p):
    n=len(seq)
    if n%2:return False
    D=erasable_table(seq,p)
    @functools.lru_cache(None)
    def G(i,j):
        width=j-i
        if width==0:return True
        if width%2:return False
        if D[i][j]:return True
        # A same-type 2-letter base with an inverse-erasable interior.
        if seq[i][1]==seq[j-1][1] and D[i+1][j-1]:return True
        # A rotation-wrapped already certified inner block.
        if not seq[i][1] and not seq[j-1][1] and G(i+1,j-1):return True
        # Arbitrary consecutive concatenation, including erasable gaps.
        if any(G(i,k) and G(k,j) for k in range(i+2,j,2)):return True
        # GOOD4 actual surviving terminals, with inverse-erasable gaps.
        for k in range(i+1,j-2,2):
            if not D[i+1][k]:continue
            for l in range(k+1,j-1,2):
                if D[k+1][l] and D[l+1][j-1] and good4((seq[i],seq[k],seq[l],seq[j-1]),p):
                    return True
        return False
    return G(0,n)


def scan(word,p):
    unique=set()
    tested=0
    n=len(word)
    for cut in range(n):
        w=word[cut:]+word[:cut]
        for omit in range(n):
            seq=w[:omit]+w[omit+1:]
            if seq in unique:continue
            unique.add(seq)
            tested+=1
            if chart(seq,p):
                return {'outcome':'CERTIFICATE_REACHABLE','cut':cut,'omission_in_cut':omit,'unique_examined':tested}
    return {'outcome':'NO_CERTIFICATE_IN_CHART','unique_examined':tested}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--p',type=int,required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    with open(args.input,'rb') as src:raw=src.read()
    data=json.loads(raw)
    item=next(v for v in data['cases'] if v['p']==args.p)
    p=item['p']
    word=tuple(tuple(x) for x in item['word'])
    if len(word)!=4*p-1 or any(x<0 or x>=p or e not in (0,1) for x,e in word):
        raise ValueError('INPUT_SHAPE')
    if len({x for x,e in word if not e})!=1 or not next(x for x,e in word if not e):
        raise ValueError('SIX_BASE_NOT_EXCLUDED')
    base=((1,0),(0,1),(1,0),(0,1))
    expanded=((1,0),(0,1),(0,1),(0,1),(1,0),(0,1))
    if not good4(base,p) or not chart(base,p) or not chart(expanded,p):
        raise ValueError('IP_INSERTION_POSITIVE_CONTROL')
    if chart(expanded[:-1],p):
        raise ValueError('ODD_LENGTH_CONTROL')
    report=scan(word,p)
    result={'result':'INDEPENDENT_ERASABLE_GAP_CHART_COMPLETED',
            'input_sha256':hashlib.sha256(raw).hexdigest(),'p':p,'scan':report,
            'controls':['IP_INSERTION_POSITIVE_CONTROL','ODD_LENGTH_CONTROL'],
            'scope':'one fixed word; chart and grammar normalization require independent review'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
