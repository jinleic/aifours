#!/usr/bin/env python3
"""Independently audit every cut/omission via BFS inverse-removal closure."""
import argparse
from collections import Counter,deque
import hashlib
import json


def group_product(items,p):
    x,e=0,0
    for y,f in items:
        x=(x+(-y if e else y))%p
        e ^= f
    return x,e


def build(p,b):
    out=[(0,1)]*(2*p-7)+[(b,0)]+[(1,1)]*2+[(0,1)]+[(p-1,1)]*2+[(0,1),(b,0)]
    for j in range(1,p):
        out.extend(((j,1),(b,0)))
    return tuple(out)


def refl_support(word,p):
    dp=[set() for _ in range(2*p+1)]
    dp[0].add(0)
    values=[v for v,e in word if e]
    for i,y in enumerate(values):
        for k in range(min(i,2*p-1),-1,-1):
            dp[k+1].update((z+(y if k%2==0 else -y))%p for z in dp[k])
    return dp[2*p]


def raw_paths(word,p):
    refs=[i for i,(_,b) in enumerate(word) if b]
    F=len(refs)
    G=[set() for _ in refs]
    for k,i in enumerate(refs):
        j=refs[(k+1)%F]
        gap=word[i+1:j] if k+1<F else word[i+1:]+word[:j]
        if len(gap)>1 or any(e for _,e in gap):
            raise ValueError('CYCLIC_GAP')
        if gap or word[i][0]!=word[j][0]:
            G[k].add((k+1)%F)
            G[(k+1)%F].add(k)
    seen=set()
    sizes=[]
    for i in range(F):
        if i in seen:
            continue
        todo=[i]
        comp=set()
        while todo:
            k=todo.pop()
            if k in comp:continue
            comp.add(k)
            todo.extend(G[k]-comp)
        seen |= comp
        if len(comp)>1 and sum(len(G[v])==1 for v in comp)!=2:
            raise ValueError('RAW_NOT_PATHS')
        sizes.append(len(comp))
    if sorted(sizes)!=sorted([p+2,3,2]+[1]*(2*p-9)):
        raise ValueError('RAW_COMPONENTS')
    return sum(x//2 for x in sizes)


def good4(seq,p):
    rot=[x for x,e in seq if not e]
    refl=[x for x,e in seq if e]
    if len(rot)!=2 or len(refl)!=2:
        return False
    A=sum(rot)%p
    B=(refl[0]-refl[1])%p
    C,e=group_product(seq,p)
    return e==0 and (A!=B or C==(2*A)%p)


def gen_membership(seq,p):
    N=len(seq)
    if N%2:
        return False
    if not N:
        return True
    chart=[[False]*(N+1) for _ in range(N+1)]
    for size in range(2,N+1,2):
        for left in range(N-size+1):
            right=left+size
            yes=(size==2 and seq[left][1]==seq[left+1][1])
            if not yes and size==4:
                yes=good4(seq[left:right],p)
            if not yes and size>=4 and not seq[left][1] and not seq[right-1][1]:
                yes=chart[left+1][right-1]
            if not yes:
                yes=any(chart[left][mid] and chart[mid][right] for mid in range(left+2,right-1,2))
            chart[left][right]=yes
    return chart[0][N]


def inverse(a,b,p):
    return a[1]==b[1] and ((a[0]==b[0]) if a[1] else ((a[0]+b[0])%p==0))


def independent_scan(word,p):
    initial=set()
    N=len(word)
    for cut in range(N):
        cutword=word[cut:]+word[:cut]
        for omit in range(N):
            initial.add(cutword[:omit]+cutword[omit+1:])
    pending=deque(sorted(initial))
    seen=set(initial)
    digest=hashlib.sha256()
    while pending:
        seq=pending.popleft()
        digest.update(len(seq).to_bytes(2,'big'))
        digest.update(bytes(v for pair in seq for v in pair))
        if gen_membership(seq,p):
            return {'outcome':'GEN_REACHED_BY_INVERSE_REMOVALS','initial_unique':len(initial),
                    'closure_seen_before_witness':len(seen),'visited_digest':digest.hexdigest()}
        for k in range(len(seq)-1):
            if inverse(seq[k],seq[k+1],p):
                nxt=seq[:k]+seq[k+2:]
                if nxt not in seen:
                    seen.add(nxt)
                    pending.append(nxt)
    return {'outcome':'NO_GEN_REACHABLE_AFTER_ANY_INVERSE_REMOVALS',
            'initial_unique':len(initial),'closure_states':len(seen),'visited_digest':digest.hexdigest()}


def validate(word,p,b):
    if len(word)!=4*p-1 or any(e not in (0,1) or x<0 or x>=p for x,e in word):
        raise ValueError('INPUT_SHAPE')
    if any(x!=b for x,e in word if not e):
        raise ValueError('ROTATION_VALUE')
    if tuple(word)!=build(p,b):
        raise ValueError('CANDIDATE_NOT_EXACT')


def run_case(item):
    p=item['p']
    if p not in (11,13) or item['a']!=1 or item['rotation']!=(p-1)//2:
        raise ValueError('INPUT_PARAMETER')
    word=tuple(tuple(v) for v in item['word'])
    b=item['rotation']
    validate(word,p,b)
    refs=Counter(x for x,e in word if e)
    if refs[0]!=2*p-5 or refs[1]!=3 or refs[p-1]!=3 or len([1 for _,e in word if not e])!=p+1:
        raise ValueError('COUNTS')
    if raw_paths(word,p)!=(p+5)//2:
        raise ValueError('MATCHING')
    if 0 in refl_support(word,p):
        raise ValueError('REF_SHOULD_FAIL')
    L=2*p-7
    idx=list(range(L+6))+[L+7]
    if len(idx)!=2*p or group_product([word[i] for i in idx],p)!=(0,0):
        raise ValueError('MIXED_SELECTOR')
    mutated=list(word)
    nextrot=next(i for i,(_,e) in enumerate(mutated) if not e)
    mutated[nextrot]=(0,0)
    try:
        validate(tuple(mutated),p,b)
    except ValueError as exc:
        if str(exc)!='ROTATION_VALUE':raise
    else:
        raise ValueError('ROTATION_MUTATION_SURVIVED')
    good=build(p,1)[1:]
    if not gen_membership(good,p):
        raise ValueError('POSITIVE_GEN_CONTROL')
    base=((1,0),(0,1),(1,0),(0,1))
    expanded=((1,0),(0,1),(0,1),(0,1),(1,0),(0,1))
    if not gen_membership(base,p) or gen_membership(expanded,p):
        raise ValueError('IP_ONLY_CONTROL_SETUP')
    reduced=expanded[:1]+expanded[3:]
    if reduced!=base or not inverse(expanded[1],expanded[2],p):
        raise ValueError('IP_ONLY_CONTROL_REDUCTION')
    if gen_membership(expanded[:-1],p):
        raise ValueError('ODD_LENGTH_CONTROL')
    scan=independent_scan(word,p)
    if scan['outcome']!='NO_GEN_REACHABLE_AFTER_ANY_INVERSE_REMOVALS':
        raise ValueError('IPGEN_CERTIFICATE_FOUND')
    return {'p':p,'matching':(p+5)//2,'reflection_only_zero_absent':True,
            'exact_mixed_selector':idx,'IPGEN_scan':scan,
            'controls':['ROTATION_VALUE','POSITIVE_GEN_CONTROL','IP_ONLY_CONTROL_REDUCTION','ODD_LENGTH_CONTROL']}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    with open(args.input,'rb') as src:
        raw=src.read()
    data=json.loads(raw)
    if data.get('kind')!='KAPPA1_E2_UNPROMOTED_CANDIDATE_WORDS' or len(data['cases'])!=2:
        raise ValueError('INPUT_MANIFEST')
    result={'result':'PASS_INDEPENDENT_BFS_IP_AUDIT','input_sha256':hashlib.sha256(raw).hexdigest(),
            'cases':[run_case(item) for item in data['cases']],
            'scope':'two fixed words; grammar-normalization and OLD/GS/DS3 require separate independent review'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
