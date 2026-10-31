#!/usr/bin/env python3
"""Exact support-cell enumeration for four-party cross-pair local maps.

Input: the pinned published 60-term tensor table, with SHA-256 below. For each
of 21 layouts per party (no cross-pair, one of eight H--K pairs, or two of twelve
disjoint H--K matchings), compute the number of output positions which receive
contributions from exactly one source word. There are 21^4=194481 layouts.

Two independently structured algorithms are compared for EVERY layout:
  * group the 60 source words by their Cartesian output block/cell, then sum
    cell sizes where the number of source words is one;
  * expand each source word to its reachable output words and count output
    coordinates receiving exactly one source word.
All calculations are integers. The count is a rigorous support LOWER bound for
arbitrary nonzero tensor coefficients and entrywise-nonzero matrices on the
selected 2x2 blocks, independent of signs and phases. The program checks the
input shape and intended-error mutations and writes one exclusive JSON receipt.
It does not prove an unrestricted four-factor orbit bound or a global AME bound.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import itertools
import json
from pathlib import Path
import time

EXPECTED_SHA256='cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38'
H=(1,2);K=(0,3,4,5)


def validate_support(words):
    if len(words)!=len(set(words)):raise ValueError('duplicate tensor word')
    if len(words)!=60:raise ValueError('expected 60 tensor words')
    if any(len(w)!=4 or any(type(v)!=int or v<0 or v>=6 for v in w) for w in words):raise ValueError('invalid tensor coordinate')


def parse_table(raw):
    seen_cells=set();words=[];types=Counter()
    for line in raw.decode('ascii').splitlines():
        if not line.strip() or line.startswith('#'):continue
        p=line.split()
        if len(p)<3:raise ValueError('bad table row')
        try:a,b=int(p[0]),int(p[1])
        except ValueError as e:raise ValueError('bad pair indices') from e
        if not 0<=a<6 or not 0<=b<6 or (a,b) in seen_cells:raise ValueError('invalid or duplicate AB cell')
        seen_cells.add((a,b))
        for t in p[2:]:
            if len(t)!=3 or t[0] not in '+-s' or t[1] not in '012345' or t[2] not in '012345':raise ValueError('bad coefficient token')
            types[t[0]]+=1;words.append((a,b,int(t[1]),int(t[2])))
    if seen_cells!=set(itertools.product(range(6),repeat=2)):raise ValueError('AB table coverage')
    validate_support(words)
    if types!={'+':30,'-':18,'s':12}:raise ValueError('coefficient type counts')
    return tuple(sorted(words)),dict(types)


def layouts():
    single=[((h,k),) for h in H for k in K]
    double=[((1,k1),(2,k2)) for k1 in K for k2 in K if k1!=k2]
    return [()]+single+double


def map_for(layout):
    mp=[(v,) for v in range(6)];used=set()
    for h,k in layout:
        if h not in H or k not in K or h in used or k in used:raise ValueError('invalid cross-pair matching')
        used.update((h,k));mp[h]=mp[k]=tuple(sorted((h,k)))
    return tuple(mp)


def by_cell(words,maps):
    groups=Counter(tuple(maps[i][w[i]] for i in range(4)) for w in words)
    return sum(len(c[0])*len(c[1])*len(c[2])*len(c[3]) for c,q in groups.items() if q==1)


def by_output(words,maps):
    output=Counter()
    for w in words:
        for z in itertools.product(*(maps[i][w[i]] for i in range(4))):output[z]+=1
    return sum(v==1 for v in output.values())


def expect_error(fn,args,message):
    try:fn(*args)
    except ValueError as e:
        if str(e)!=message:raise ValueError('wrong mutation error: '+str(e)) from e
        return message
    raise ValueError('mutation unexpectedly accepted: '+message)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('table',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    raw=a.table.read_bytes();actual=hashlib.sha256(raw).hexdigest()
    if actual!=EXPECTED_SHA256:raise ValueError('source SHA-256 mismatch')
    words,types=parse_table(raw);L=layouts();M=[map_for(x) for x in L]
    if len(L)!=21 or len(set(L))!=21 or by_cell(words,(M[0],)*4)!=60:raise ValueError('layout or identity control')
    if expect_error(validate_support,(words[:-1],),'expected 60 tensor words')!='expected 60 tensor words':raise ValueError('drop control')
    if expect_error(validate_support,(words+(words[0],),),'duplicate tensor word')!='duplicate tensor word':raise ValueError('duplicate control')
    if expect_error(map_for,(((1,0),(2,0)),),'invalid cross-pair matching')!='invalid cross-pair matching':raise ValueError('overlap control')
    if expect_error(map_for,(((1,2),),),'invalid cross-pair matching')!='invalid cross-pair matching':raise ValueError('noncross control')
    # Mutation control: an output in a two-source cell may cancel, even when
    # the 2x2 matrices are invertible and all their entries are nonzero.
    chosen=(M[1],)*4;groups=defaultdict(list)
    for w in words:groups[tuple(chosen[i][w[i]] for i in range(4))].append(w)
    double=next((cell,ws) for cell,ws in sorted(groups.items()) if len(ws)==2)
    # On each pair block take [[1,1],[1,-1]] with row ordering (H,K). Select
    # the H output in each pair coordinate; singleton entries equal1. Both
    # source factors in this output are +1; assign their source amplitudes
    # +1 and -1, respectively. Both are nonzero and their output sum is zero.
    cell,ws=double;target=tuple(1 if len(cell[i])==2 else cell[i][0] for i in range(4))
    reaches=[w for w in words if all(target[i] in chosen[i][w[i]] for i in range(4))]
    if len(reaches)!=2 or set(reaches)!=set(ws) or 1+(-1)!=0:raise ValueError('two-source cancellation control')
    stats=defaultdict(lambda:{'cases':0,'minimum':None,'maximum':None,'minimizer':None});digest=hashlib.sha256();mismatches=0;t0=time.monotonic()
    for idx in itertools.product(range(21),repeat=4):
        maps=tuple(M[i] for i in idx);a_count=by_cell(words,maps);b_count=by_output(words,maps)
        if a_count!=b_count:mismatches+=1;raise ValueError('independent-method mismatch')
        active=sum(i!=0 for i in idx);doubles=sum(i>=9 for i in idx);rec=stats[(active,doubles)];rec['cases']+=1
        if rec['minimum'] is None or a_count<rec['minimum']:rec['minimum']=a_count;rec['minimizer']=idx
        if rec['maximum'] is None or a_count>rec['maximum']:rec['maximum']=a_count
        digest.update((','.join(map(str,idx))+':'+str(a_count)+'\n').encode('ascii'))
    rows=[{'active_parties':a,'double_parties':d,**stats[a,d]} for a,d in sorted(stats)]
    if sum(r['cases'] for r in rows)!=21**4 or min(r['minimum'] for r in rows)!=60:raise ValueError('family coverage')
    if min(r['minimum'] for r in rows if r['active_parties']==4)!=108:raise ValueError('all-four bound')
    if min(r['minimum'] for r in rows if r['active_parties']>0)!=81:raise ValueError('nonmonomial bound')
    result={'scope':'Exact source-support lower-bound controls, not formal proof, novelty clearance, or unrestricted AME result.',
      'source_sha256':actual,'source_cells':36,'source_nonzeros':len(words),'coefficient_token_types':types,'parties_each_layouts':len(L),'families':21**4,
      'two_complete_integer_methods_equal_on_all_layouts':mismatches==0,'mismatches':mismatches,'score_stream_sha256':digest.hexdigest(),
      'counts_by_active_and_double_parties':rows,'all_family_min':60,'nonzero_active_min':81,'all_four_active_min':108,
      'controls':{'identity_unique_source_outputs':60,'drop_word':'expected 60 tensor words','duplicate_word':'duplicate tensor word',
         'overlapping_pairs':'invalid cross-pair matching','noncross_pair':'invalid cross-pair matching',
         'two_source_cancellation':{'source_words':ws,'target':target,'amplitudes':[1,-1],'matrix':'[[1,1],[1,-1]]','target_value':0}},
      'elapsed_monotonic_seconds':time.monotonic()-t0}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'families':result['families'],'mismatches':mismatches,'all_family_min':60,'nonzero_active_min':81,'all_four_active_min':108,
      'score_stream_sha256':result['score_stream_sha256'],'elapsed_monotonic_seconds':result['elapsed_monotonic_seconds']},indent=2))


if __name__=='__main__':main()
