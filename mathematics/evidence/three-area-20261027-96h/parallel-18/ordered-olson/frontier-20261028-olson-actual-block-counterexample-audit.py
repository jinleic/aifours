#!/usr/bin/env python3
"""Independent proof-instance audit of occupied-equal-gap block splitting."""
import argparse
import json


def product(word,indices,p):
    x,e=0,0
    for i in indices:
        y,b=word[i]
        x=(x+(-y if e else y))%p
        e^=b
    return x,e




def actual_blocks(word):
    out=[]
    prev_is_ref=False
    for value,kind in word:
        if kind:
            if prev_is_ref and out[-1][0]==value:
                out[-1][1]+=1
            else:
                out.append([value,1])
            prev_is_ref=True
        else:
            prev_is_ref=False
    return out


def check(p):
    w=[[0,1],[1,0],[0,1],[1,0]]+[[0,1]]*(2*p-3)+[[1,0]]
    for j in range(1,p-1):w.extend(([j,1],[1,0]))
    w.append([p-1,1])
    refs=[i for i,(_,e) in enumerate(w) if e]
    rot=[i for i,(_,e) in enumerate(w) if not e]
    if len(w)!=4*p-1 or len(refs)!=3*p-2 or len(rot)!=p+1:
        raise ValueError('COUNTS')
    b=actual_blocks(w)
    if sum(n%2 for _,n in b)!=p+2 or sum(not n%2 for _,n in b)!=0:
        raise ValueError('ACTUAL_BLOCKS')
    if [n for value,n in b if value==0]!=[1,1,2*p-3]:
        raise ValueError('SPLIT_ZERO_BLOCK')
    # Exhaust all nonempty tail subsets; zeros are identical and all precede tail.
    zeros=refs[:2*p-1];tail=refs[2*p-1:]
    classes=0
    for mask in range(1,1<<(p-1)):
        T=[tail[k] for k in range(p-1) if mask>>k&1]
        chosen=sorted(zeros[:2*p-len(T)]+T)
        if len(chosen)!=2*p or product(w,chosen,p)==(0,0):
            raise ValueError('REF_COUNTEREXAMPLE')
        classes+=1
    edges=[]
    for q,i in enumerate(refs):
        j=refs[(q+1)%len(refs)]
        gap=w[i+1:j] if q+1<len(refs) else w[i+1:]+w[:j]
        if len(gap)>1:raise ValueError('GAP')
        if gap or w[i][0]!=w[j][0]:edges.append((q,(q+1)%len(refs)))
    graph={i:set() for i in range(len(refs))}
    for i,j in edges:graph[i].add(j);graph[j].add(i)
    active={i for i in graph if graph[i]}
    ends=[i for i in active if len(graph[i])==1]
    if len(ends)!=2:raise ValueError('RAW_PATH_ENDPOINTS')
    path=[ends[0]]
    while path[-1]!=ends[1]:
        choices=graph[path[-1]]-set(path)
        if len(choices)!=1:raise ValueError('RAW_PATH')
        path.append(next(iter(choices)))
    if len(path)!=p+3 or len(active)!=p+3 or len(edges)!=p+2:
        raise ValueError('RAW_PATH_SIZE')
    d=(-pow(3,-1,p))%p
    selector=sorted(zeros[:p-3]+rot+[tail[0],tail[d]])
    if len(selector)!=2*p or product(w,selector,p)!=(0,0):
        raise ValueError('MIXED_SELECTOR')
    # Move first same-label separator to formerly empty last→first boundary.
    changed=w[:1]+w[2:]+[[1,0]]
    cb=actual_blocks(changed)
    if sum(n%2 for _,n in cb)!=p or sum(not n%2 for _,n in cb)!=1:
        raise ValueError('OCCUPIED_GAP_MUTATION')
    return {'p':p,'actual_odd':p+2,'actual_even':0,'raw_matching':len(path)//2,
            'within_lower':len(path)//2<=p-3,'tail_subsets_exhausted':classes,
            'exact_mixed_selector':selector,'same_label_gap_mutation_detected':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result={'result':'PASS_INDEPENDENT_ACTUAL_BLOCK_COUNTEREXAMPLE',
            'instances':[check(p) for p in (7,11,13,17)],
            'scope':'explicit SEL-covered counterexamples to unrestricted actual-block REF lift'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
