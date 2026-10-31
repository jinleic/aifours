#!/usr/bin/env python3
"""Independent exact direct-sum/finite-geometry audit for the f60 caller.

Reads only the three pinned source seed tables, not the author's computation or
receipts. Checks all local sign tables, all six-sets, three 512-frequency
outside fibres, all 448 valid spectra and the seed-1 local Hamming-four graph.
"""
from collections import Counter,deque
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SEEDS=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/frontier-20261028-published-seeds.txt')
EXPECTED='116ab5a7709dd35d951ddc878af227e5e05ce269d8293e5c0c269e158bd051f2'
OUTPUT=ROOT/'frontier-review-f60-affine-core-independent-result.json'
X0=365
BASES=((27,45,195,325),(63,90,139,278),(27,45,195,325))
X=Counter({-22:15,-6:1,10:5,26:11})
Y=Counter({-22:16,10:4,26:12})


def parity(x):return x.bit_count()&1


def span(basis):
    if len(basis)!=4 or any(type(x) is not int or not 0<=x<512 for x in basis):
        raise ValueError('INVALID_BASIS')
    points=[]
    for code in range(16):
        v=0
        for j,b in enumerate(basis):
            if code&(1<<j):v^=b
        points.append(v)
    if len(set(points))!=16:raise ValueError('BASIS_NOT_INDEPENDENT')
    return points


def transform(signs):
    w=list(signs);step=1
    while step<len(w):
        for lo in range(0,len(w),2*step):
            for j in range(lo,lo+step):
                a,b=w[j],w[j+step];w[j]=a+b;w[j+step]=a-b
        step*=2
    return w


def local_spectrum(mask):return transform([1-2*((mask>>i)&1) for i in range(16)])


def local_sidon():
    masks=set();sets=[]
    for points in combinations(range(16),6):
        if len({x^y for x,y in combinations(points,2)})!=15:continue
        signs=[-1]
        for x in range(1,16):
            s=sum(1-2*parity(a&x) for a in points)
            if s not in (-2,2):raise ValueError(('BAD_FOURIER_INVERSE',points,x,s))
            signs.append(-s//2)
        mask=sum((v==-1)<<x for x,v in enumerate(signs))
        L=local_spectrum(mask)
        if any(L[a]!=(-6 if a in points else 2) for a in range(16)):
            raise ValueError('SIDON_INVERSION')
        if mask in masks:raise ValueError('DUPLICATE_SIDON_INVERSE')
        masks.add(mask);sets.append(points)
    if len(masks)!=448:raise ValueError(('SIDON_COUNT',len(masks)))
    incidence=[sum(a in S for S in sets) for a in range(16)]
    if incidence!=[168]*16:raise ValueError(('INCIDENCE',incidence))
    exhaustive={m for m in range(1<<16) if all(-6<=x<=2 for x in local_spectrum(m))}
    if masks!=exhaustive:raise ValueError(('EXHAUSTIVE_LOCAL_MISMATCH',len(exhaustive)))
    return masks,sets


def outside_data(seed,basis):
    offsets=span(basis);flat=[X0^v for v in offsets];outside=set(range(512))-set(flat)
    signs=[1-2*bit for bit in seed];R=[];alphas=[]
    for a in range(512):
        alpha=sum(parity(a&basis[j])<<j for j in range(4))
        value=(1-2*parity(a&X0))*sum(signs[x]*(1-2*parity(a&x)) for x in outside)
        R.append(value);alphas.append(alpha)
    fibres=[Counter(R[a] for a in range(512) if alphas[a]==alpha) for alpha in range(16)]
    if any(sum(f.values())!=32 or f not in (X,Y) for f in fibres):
        raise ValueError(('OUTSIDE_FIBRE_MISMATCH',basis,fibres))
    types=['X' if f==X else 'Y' for f in fibres]
    if Counter(types)!=Counter({'X':6,'Y':10}):raise ValueError(('OUTSIDE_CLASS_COUNTS',types))
    return flat,R,alphas,types


def check_seed(seed,basis,masks):
    flat,R,alphas,types=outside_data(seed,basis)
    W=[sum((1-2*seed[x])*(1-2*parity(a&x)) for x in range(512)) for a in range(512)]
    if max(map(abs,W))!=28 or 0 in W:raise ValueError('PUBLISHED_SEED_PEAK_OR_ZERO')
    hist=Counter(abs(x) for x in W)
    target=Counter({4:30,12:46,20:226,28:210})
    if hist!=target:raise ValueError(('PUBLISHED_SEED_HIST',hist))
    local_original=sum(seed[x]<<i for i,x in enumerate(flat))
    if local_original not in masks:raise ValueError('SEED_NOT_LOCAL_VALID')
    peak_count=0;zero_count=0;histograms=set()
    for m in masks:
        L=local_spectrum(m)
        global_W=[R[a]+L[alphas[a]] for a in range(512)]
        if max(map(abs,global_W))>28:raise ValueError('PEAK_BOUND')
        peak_count+=1;zero_count+=int(0 in global_W)
        histograms.add(tuple(sorted(Counter(abs(x) for x in global_W).items())))
    if peak_count!=448 or zero_count!=0 or histograms!={tuple(sorted(target.items()))}:
        raise ValueError(('LOCAL_FULL_HIST',peak_count,zero_count,histograms))
    return {'seed_weight':sum(seed),'seed_W0':W[0],
            'seed_peak':max(map(abs,W)),'seed_zero_count':W.count(0),
            'flat_positions':flat,'outside_X_classes':types.count('X'),'outside_Y_classes':types.count('Y'),
            'valid_local_assignments':peak_count,'balanceable_local_assignments':zero_count,
            'all_valid_absolute_histogram':dict(sorted(target.items()))},(R,alphas,local_original)


def graph_and_span(masks,first):
    ordered=sorted(masks);adj={x:[] for x in ordered};moves=set();nonplane=[]
    for i,x in enumerate(ordered):
        for y in ordered[i+1:]:
            delta=x^y
            if delta.bit_count()==4:
                adj[x].append(y);adj[y].append(x);moves.add(delta)
                indices=[j for j in range(16) if delta&(1<<j)]
                xor=0
                for j in indices:xor^=j
                if xor:nonplane.append((x,y,indices))
    degrees=Counter(len(v) for v in adj.values());edges=sum(map(len,adj.values()))//2
    unseen=set(ordered);components=[]
    while unseen:
        x=unseen.pop();Q=deque([x]);size=0
        while Q:
            v=Q.popleft();size+=1
            for u in adj[v]:
                if u in unseen:unseen.remove(u);Q.append(u)
        components.append(size)
    if degrees!=Counter({45:448}) or edges!=10080 or components!=[448] or nonplane:
        raise ValueError(('GRAPH',degrees,edges,components,len(nonplane)))
    span_set={0}
    for move in sorted(moves):span_set|={x^move for x in span_set}
    if len(span_set)!=1024:raise ValueError(('MOVE_SPAN_SIZE',len(span_set)))
    R,alphas,initial=first
    peak_hist=Counter();target=0
    for delta in span_set:
        L=local_spectrum(initial^delta);W=[R[a]+L[alphas[a]] for a in range(512)]
        p=max(map(abs,W));peak_hist[p]+=1
        if p<=28 and 0 in W:target+=1
    if peak_hist!=Counter({28:448,32:560,40:16}) or target:
        raise ValueError(('SPAN_HIST',peak_hist,target))
    return {'states':448,'all_unordered_pairs_checked':len(ordered)*(len(ordered)-1)//2,
            'Hamming4_edges':edges,'degree_histogram':dict(degrees),
            'component_sizes':components,'nonplane_Hamming4_edges':len(nonplane),
            'distinct_Hamming4_moves':len(moves),'move_span_size':len(span_set),
            'move_span_rank':10,'move_span_peak_histogram':dict(sorted(peak_hist.items())),
            'move_span_balanced_peak28_targets':target}


def main():
    raw=SEEDS.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    lines=[line.strip() for line in raw.decode('ascii').splitlines() if line and not line.startswith('#')]
    if len(lines)!=3 or any(len(s)!=128 for s in lines):raise ValueError('SEED_LENGTH')
    seeds=[[int(bit) for char in s for bit in f'{int(char,16):04b}'] for s in lines]
    masks,sets=local_sidon();results=[];contexts=[]
    for seed,basis in zip(seeds,BASES):
        result,context=check_seed(seed,basis,masks);results.append(result);contexts.append(context)
    graph=graph_and_span(masks,contexts[0])
    try:span((27,45,195,27))
    except ValueError as exc:
        if str(exc)!='BASIS_NOT_INDEPENDENT':raise
        mutation='BASIS_NOT_INDEPENDENT'
    else:raise ValueError('BASIS_MUTATION_ACCEPTED')
    out={'seed_sha256':EXPECTED,'local_six_subsets_checked':8008,
         'sidon_six_sets_and_boolean_inverse':len(sets),'full_local_sign_tables_checked':65536,
         'exact_Sidon_vs_full_local_table_equality':True,
         'incidence_per_frequency':168,'nonincidence_per_frequency':280,
         'seed_results':results,'seed1_local_graph':graph,
         'duplicate_basis_mutation_rejection':mutation,
         'limits':'Exact finite checks for the three named input tables and all local signs; no global existence/nonexistence, novelty or independent-model review.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
