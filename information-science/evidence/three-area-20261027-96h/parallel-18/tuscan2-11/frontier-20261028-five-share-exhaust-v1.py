#!/usr/bin/env python3
"""Exact bounded test of every compatible five-row subset of a fixed array.

Generates every eligible completion row by breadth-first prefix expansion and
then performs exact-cover search with bitset conflict filtering. Candidate
five-subsets are accepted only if their fixed rows already satisfy all direct
D1/D2 and endpoint necessities. Each unfinished subcase is UNKNOWN, never
UNSAT; a found witness must be independently verified from actual rows.
"""
import hashlib
import itertools
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

N = 11


class Limit(Exception):
    pass


def direct_fixed(rows):
    return (len({r[0] for r in rows}) == len(rows) and
            len({r[-1] for r in rows}) == len(rows) and
            all(len({(r[i], r[i+d]) for r in rows for i in range(N-d)}) ==
                len(rows)*(N-d) for d in (1, 2)))


def run_subset(fixed, seconds, node_cap, row_cap):
    started = time.monotonic()
    deadline = started + seconds
    used1 = {(r[i], r[i+1]) for r in fixed for i in range(N-1)}
    used2 = {(r[i], r[i+2]) for r in fixed for i in range(N-2)}
    fixed_starts, fixed_ends = {r[0] for r in fixed}, {r[-1] for r in fixed}
    required = {(a,b) for a in range(N) for b in range(N) if a != b} - used1
    needed_mask = sum(1 << (a*N+b) for a,b in required)
    generated_nodes = 1
    search_nodes = 0
    eligible = []
    complete_rows = False
    complete_cover = False
    result = None
    witness = None
    exhausted_reason = None

    def check_time():
        if generated_nodes + search_nodes > node_cap:
            raise Limit('node_cap')
        if time.monotonic() >= deadline:
            raise Limit('wall_time')

    try:
        # Each list is exactly the set of compatible prefixes of its length.
        level = [((), 0)]
        for depth in range(N):
            next_level = []
            for prefix, used in level:
                for v in range(N):
                    if used & (1 << v) or (depth == 0 and v in fixed_starts):
                        continue
                    if depth and (prefix[-1], v) in used1:
                        continue
                    if depth >= 2 and (prefix[-2], v) in used2:
                        continue
                    if depth == N-1 and v in fixed_ends:
                        continue
                    next_level.append((prefix + (v,), used | (1 << v)))
                    generated_nodes += 1
                    if generated_nodes % 1024 == 0:
                        check_time()
            level = next_level
        if len(level) > row_cap:
            raise Limit('row_cap')
        eligible = [prefix for prefix, _ in level]
        complete_rows = True
        by_feature = defaultdict(int)
        row_features = []
        row_d1 = []
        for i, row in enumerate(eligible):
            e1 = [(r, s) for r,s in zip(row,row[1:])]
            e2 = [(row[t],row[t+2]) for t in range(N-2)]
            features = [('one', a,b) for a,b in e1] + [('two',a,b) for a,b in e2]
            features += [('start',row[0]), ('end',row[-1])]
            row_features.append(features)
            row_d1.append(sum(1 << (a*N+b) for a,b in e1))
            for key in features:
                by_feature[key] |= 1 << i
        conflict = []
        for features in row_features:
            mask = 0
            for key in features:
                mask |= by_feature[key]
            conflict.append(mask)
        edge_options = {a*N+b: by_feature[('one',a,b)] for a,b in required}
        all_candidates = (1 << len(eligible)) - 1
        seen = set()
        chosen = []

        def cover(outstanding, allowed):
            nonlocal search_nodes, witness
            search_nodes += 1
            if search_nodes % 1024 == 0:
                check_time()
            if not outstanding:
                if len(chosen) != N-len(fixed):
                    raise AssertionError('unexpected completion size')
                witness = [eligible[i] for i in chosen]
                return True
            state = (outstanding, allowed)
            if state in seen:
                return False
            seen.add(state)
            choice, count = 0, len(eligible)+1
            remaining = outstanding
            while remaining:
                bit = remaining & -remaining
                index = bit.bit_length()-1
                options = edge_options[index] & allowed
                size = options.bit_count()
                if size == 0:
                    return False
                if size < count:
                    choice, count = options, size
                    if size == 1:
                        break
                remaining ^= bit
            while choice:
                bit = choice & -choice
                index = bit.bit_length()-1
                if row_d1[index] & outstanding != row_d1[index]:
                    raise AssertionError('an allowed row overlaps a previously chosen arc')
                chosen.append(index)
                if cover(outstanding ^ row_d1[index], allowed & ~conflict[index]):
                    return True
                chosen.pop()
                choice ^= bit
            return False

        found = cover(needed_mask, all_candidates)
        complete_cover = True
        result = 'candidate_witness_requires_independent_check' if found else 'no_completion_exhaustive'
    except Limit as exc:
        exhausted_reason = str(exc)
        result = 'unknown_budget_exhausted'
    return {'status': result, 'enumeration_complete': complete_rows,
            'exact_cover_complete': complete_cover, 'generated_nodes': generated_nodes,
            'eligible_rows': len(eligible), 'cover_nodes': search_nodes,
            'elapsed_ms': round((time.monotonic()-started)*1000),
            'budget_reason': exhausted_reason, 'completion_rows': witness}


def main(argv):
    if len(argv) != 6:
        raise ValueError('usage: SCRIPT SOURCE OUTPUT SECONDS_PER_CASE NODE_CAP ROW_CAP')
    source, output = Path(argv[1]), Path(argv[2])
    seconds = float(argv[3])
    node_cap, row_cap = int(argv[4]), int(argv[5])
    if seconds <= 0 or node_cap <= 0 or row_cap <= 0:
        raise ValueError('resource caps must be positive')
    raw = source.read_bytes()
    rows = json.loads(raw)['rows']
    if len(rows) != N or any(sorted(r) != list(range(N)) for r in rows):
        raise ValueError('expected eleven permutation rows')
    start = time.monotonic()
    subsets = [idx for idx in itertools.combinations(range(N),5)
               if direct_fixed([rows[i] for i in idx])]
    records = []
    candidate = None
    for subset in subsets:
        fixed = [rows[i] for i in subset]
        case = run_subset(fixed, seconds, node_cap, row_cap)
        case['fixed_rows_1based'] = [i+1 for i in subset]
        records.append(case)
        print(json.dumps({k:case[k] for k in ('fixed_rows_1based','status','eligible_rows','cover_nodes','elapsed_ms')}),flush=True)
        if case['status'] == 'candidate_witness_requires_independent_check':
            candidate = [list(row) for row in fixed] + [list(row) for row in case['completion_rows']]
            break
    completed_all = len(records) == len(subsets)
    all_excluded = completed_all and all(r['status'] == 'no_completion_exhaustive' for r in records)
    out = {'source': str(source), 'source_sha256': hashlib.sha256(raw).hexdigest(),
           'total_five_subsets': 462, 'fixed_compatible_subsets': len(subsets),
           'cases_run': len(records), 'cases': records, 'all_compatible_subsets_excluded': all_excluded,
           'limits': {'seconds_per_case': seconds, 'node_cap': node_cap, 'row_cap': row_cap},
           'elapsed_ms': round((time.monotonic()-start)*1000),
           'scope': 'Only reuse of exact row strings from this candidate. No unrestricted no-go.'}
    if candidate is not None:
        out.update({'rows':candidate,'zero_score_claim':True,'best_pair_collision_score':0,
                    'd1_pair_collisions':0,'d2_pair_collisions':0,
                    'd1_excess_events':0,'d2_excess_events':0})
    with output.open('x',encoding='utf-8') as stream:
        json.dump(out,stream,indent=2,sort_keys=True)
        stream.write('\n')
    print(json.dumps({'cases_run':len(records),'fixed_compatible_subsets':len(subsets),
                      'all_compatible_subsets_excluded':all_excluded,
                      'candidate_witness':candidate is not None,'elapsed_ms':out['elapsed_ms']}))


if __name__ == '__main__':
    main(sys.argv)
