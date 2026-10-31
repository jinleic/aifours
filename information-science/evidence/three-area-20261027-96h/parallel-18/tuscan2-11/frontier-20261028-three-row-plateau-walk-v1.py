#!/usr/bin/env python3
"""Seeded finite T1-preserving three-row plateau walk, not a no-go proof.

At each step enumerate all three-row Hamilton-cycle decompositions, select a
random previously unseen minimum-score neighbor within a fixed band of the
best score, and iterate. This admits sideways moves and bounded backtracking.
All rows are free over time; no Latin or wrapped distance-two events are used.
A reported zero score must be checked independently from actual rows.
"""
import hashlib
import importlib.util
import itertools
import json
import random
import sys
import time
from pathlib import Path

helper_path = Path(__file__).with_name('frontier-20261028-three-row-trade-v1.py')
spec = importlib.util.spec_from_file_location('three_row_trade_helper', helper_path)
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
N, M = h.N, h.M


def key(rows):
    return tuple(sorted(tuple(row) for row in rows))


def main(argv):
    if len(argv) != 7:
        raise ValueError('usage: SCRIPT INPUT OUTPUT SEED MAX_STEPS MAX_SECONDS SCORE_BAND')
    source, output = Path(argv[1]), Path(argv[2])
    seed, max_steps, seconds, band = int(argv[3]), int(argv[4]), float(argv[5]), int(argv[6])
    if max_steps <= 0 or seconds <= 0 or band < 0:
        raise ValueError('invalid limits')
    raw = source.read_bytes()
    rows = json.loads(raw)['rows']
    if len(rows) != N or any(sorted(r) != list(range(N)) for r in rows):
        raise ValueError('expected eleven permutation rows')
    if len(h.counts(rows,1)) != N*(N-1) or h.pair_score(h.counts(rows,1)) != 0:
        raise ValueError('source not adjacency-complete')
    randomizer = random.Random(seed)
    started, deadline = time.monotonic(), time.monotonic()+seconds
    current = [r[:] for r in rows]
    best_rows = [r[:] for r in rows]
    current_score = best = h.pair_score(h.counts(rows,2))
    seen = {key(rows)}
    trace = []
    cutoff = False
    total_groups = total_decompositions = 0
    status = 'step_limit'
    for step in range(max_steps):
        if time.monotonic() >= deadline:
            cutoff, status = True, 'time_limit'
            break
        chosen, chosen_group, candidate_score, ties = None, None, None, 0
        groups = list(itertools.combinations(range(N),3))
        randomizer.shuffle(groups)
        for group in groups:
            if time.monotonic() >= deadline:
                cutoff = True
                break
            arcs = [h.succ(current[t]) for t in group]
            graph = [tuple(sorted(arcs[r][v] for r in range(3))) for v in range(M)]
            if any(len(set(a)) != 3 for a in graph):
                raise AssertionError('duplicate augmented arc')
            fixed = [r for i,r in enumerate(current) if i not in group]
            fixed2 = h.counts(fixed,2)
            total_groups += 1
            for first in h.all_hamilton_rows(graph):
                first_succ = h.succ(first)
                remain = [tuple(x for x in graph[v] if x != first_succ[v]) for v in range(M)]
                p,q,components = h.bipartite_split(remain)
                for mask in range(1 << (len(components)-1)):
                    pp,qq = p[:],q[:]
                    for ci in range(1,len(components)):
                        if mask & (1 << (ci-1)):
                            for v in components[ci]:
                                pp[v],qq[v] = qq[v],pp[v]
                    second,third = h.decode(pp),h.decode(qq)
                    if second is None or third is None or first > second or first > third:
                        continue
                    total_decompositions += 1
                    combined = fixed2.copy()
                    combined.update((r[i],r[i+2]) for r in (first,second,third) for i in range(N-2))
                    score = h.pair_score(combined)
                    if score > best+band or (candidate_score is not None and score > candidate_score):
                        continue
                    candidate = [r[:] for r in current]
                    for idx,row in zip(group,(first,second,third)):
                        candidate[idx] = list(row)
                    signature = key(candidate)
                    if signature in seen:
                        continue
                    if candidate_score is None or score < candidate_score:
                        chosen,chosen_group,candidate_score,ties = candidate,group,score,1
                    elif score == candidate_score:
                        ties += 1
                        if randomizer.randrange(ties) == 0:
                            chosen,chosen_group = candidate,group
        if chosen is None:
            status = 'time_limit' if cutoff else 'no_unseen_neighbor_within_band'
            break
        current,current_score = chosen,candidate_score
        seen.add(key(current))
        if current_score < best:
            best,best_rows = current_score,[r[:] for r in current]
        trace.append({'step':step+1,'score':current_score,'best_score':best,
                      'changed_slots_1based':[v+1 for v in chosen_group],
                      'equal_best_unseen_candidates':ties,
                      'full_neighborhood_scanned':not cutoff})
        if best == 0:
            status = 'candidate_witness_requires_independent_check'
            break
        if cutoff:
            status = 'time_limit'
            break
    d1,d2 = h.counts(best_rows,1),h.counts(best_rows,2)
    if h.pair_score(d1) != 0 or h.pair_score(d2) != best:
        raise AssertionError('best table score mismatch')
    result = {'source':str(source),'source_sha256':hashlib.sha256(raw).hexdigest(),
              'helper_sha256':hashlib.sha256(helper_path.read_bytes()).hexdigest(),
              'seed':seed,'max_steps':max_steps,'seconds':seconds,'score_band':band,
              'status':status,'elapsed_ms':round((time.monotonic()-started)*1000),
              'steps_taken':len(trace),'distinct_states_seen':len(seen),
              'row_groups_scanned':total_groups,'hamilton_decompositions_examined':total_decompositions,
              'initial_d2_pair_collisions':h.pair_score(h.counts(rows,2)),
              'best_pair_collision_score':best,'d1_pair_collisions':0,'d2_pair_collisions':best,
              'd1_excess_events':h.excess(d1),'d2_excess_events':h.excess(d2),
              'zero_score_claim':best==0,'rows':best_rows,'trace':trace,
              'scope':'A finite heuristic walk among T1 tables; any failure is not a no-go.'}
    with output.open('x',encoding='utf-8') as stream:
        json.dump(result,stream,indent=2,sort_keys=True)
        stream.write('\n')
    print(json.dumps({k:result[k] for k in ('status','elapsed_ms','steps_taken','distinct_states_seen',
        'row_groups_scanned','hamilton_decompositions_examined','initial_d2_pair_collisions',
        'best_pair_collision_score','zero_score_claim')}))


if __name__ == '__main__':
    main(sys.argv)
