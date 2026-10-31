#!/usr/bin/env python3
"""Fresh finite graph and actual occupied-gap checks for the lower raw bound."""
import argparse
import json


def cycle_match(bits):
    def path(es):
        prev2=prev1=0
        for e in es:
            cur=max(prev1,prev2+1) if e else prev1
            prev2,prev1=prev1,cur
        return prev1
    omit=path(bits[:-1])
    take=1+path(bits[1:-2]) if bits[-1] else 0
    return max(omit,take)


def component_matching(bits):
    n=len(bits)
    if all(bits):return n//2,n
    cut=next(i for i,v in enumerate(bits) if not v)
    size=1;nu=0;odd=0
    for k in range(1,n+1):
        if bits[(cut+k)%n]:size+=1
        else:
            nu+=size//2;odd+=size%2;size=1
    return nu,odd


def exhaust_graphs(p):
    F=3*p-2
    total=proper=low=0
    for mask in range(1<<F):
        bits=[bool(mask>>k&1) for k in range(F)]
        total+=1
        if all(bits):continue
        proper+=1
        nu,odd=component_matching(bits)
        if nu!=cycle_match(bits) or 2*nu+odd!=F:
            raise ValueError('GRAPH_MATCHING_IDENTITY')
        if nu<=p-3:
            low+=1
            if bits.count(False)<p+4:raise ValueError('ABSENT_EDGE_BOUND')
    return {'F':F,'all_masks':total,'proper':proper,'low_matching':low}


def candidate(p):
    b=(p-1)//2
    w=[[0,1],[b,0],[0,1],[b,0],[0,1],[b,0]]+[[1,1]]*(2*p-5)+[[2,1]]*3+[[b,0]]
    for j in range(3,p):w.extend(([j,1],[b,0]))
    return w


def actual(w,p):
    refs=[i for i,(_,e) in enumerate(w) if e]
    F=len(refs);bits=[];same=[]
    for t,i in enumerate(refs):
        j=refs[(t+1)%F]
        gap=w[i+1:j] if t+1<F else w[i+1:]+w[:j]
        if len(gap)>1:raise ValueError('NOT_SINGLETON')
        equal=w[i][0]==w[j][0]
        same.append(equal)
        bits.append(bool(gap) or not equal)
    # Break at a true actual boundary; no reflection-only projection shortcut.
    start=(next(t for t,x in enumerate(bits) if x)+1)%F
    lengths=[];size=1
    for q in range(F):
        t=(start+q)%F
        if bits[t]:lengths.append(size);size=1
        else:size+=1
    if len(lengths)!=sum(bits) or sum(lengths)!=F:
        raise ValueError('ACTUAL_BLOCK_BOUNDARY')
    o=sum(n%2 for n in lengths);e=sum(n%2==0 for n in lengths)
    H=sum(n//2 for n in lengths);k=p-1-H
    nu=cycle_match(bits)
    if o!=p+2*k or (nu<=p-3 and 2*k+e>p-6):
        raise ValueError('ACTUAL_LOWER_BOUND')
    # Intentional projection error: count same-value boundaries ignoring rho.
    wrong_runs=F-sum(same)
    if wrong_runs==len(lengths):raise ValueError('PROJECTION_CONTROL_NOT_EXERCISED')
    return {'p':p,'actual_blocks':len(lengths),'actual_odd':o,'actual_even':e,
            'raw_matching':nu,'empty_equal_gaps':bits.count(False),
            'projection_only_run_count':wrong_runs,'occupied_equal_gap_control':'detected mismatch'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True);args=parser.parse_args()
    result={'result':'PASS_ACTUAL_OCCUPIED_GAP_RAW_BOUND_CHECK',
            'exhaustive_cyclic_graphs':{str(p):exhaust_graphs(p) for p in (3,5,7)},
            'actual_candidate_words':[actual(candidate(p),p) for p in (7,11,13,17)],
            'scope':'finite graph masks and explicit actual words; no historical floor or repaired theorem promotion'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
