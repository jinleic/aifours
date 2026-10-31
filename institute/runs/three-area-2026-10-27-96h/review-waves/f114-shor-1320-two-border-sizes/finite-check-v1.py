#!/usr/bin/env python3
"""One-run integer replay of the frozen f114 finite claims; never imports author code."""
from collections import Counter, defaultdict
from copy import deepcopy
from itertools import combinations, product
from math import comb, gcd
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
MANIFEST_SHA = 'ad3f0ad3e4a7d80afa037fe238e791f267d993ba0c0cbf8945abe72224c30eaf'
N = 1320
A = (0, 3, 8, 11)
Y = (0, 1, 7, 13, 14)


class Failure(Exception):
    pass


def demand(condition, reason):
    if not condition:
        raise Failure(reason)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'],
                          check=True, text=True, capture_output=True).stdout.strip()


def rejected(fn, reason):
    try:
        fn()
    except Failure as exc:
        demand(str(exc) == reason, 'CONTROL_WRONG_REASON:' + str(exc))
        return reason
    raise Failure('CONTROL_NOT_REJECTED:' + reason)


def check_source(b, spec):
    demand(sha(b) == spec['sha256'], 'SOURCE_SHA')
    demand(len(b) == spec['bytes'], 'SOURCE_BYTES')
    demand(b.count(b'\n') == spec['LF'], 'SOURCE_LF')
    b.decode('utf-8')


def difference_classes(xs, n):
    return {gcd(x-y, n) for x, y in combinations(xs, 2)}


def candidate_set(n, anchors, forbidden):
    return {x for x in range(n)
            if all(x == a or gcd(x-a, n) not in forbidden for a in anchors)}


def conflicts(x, y, forbidden, n=N):
    return x != y and gcd(x-y, n) in forbidden


def validate_tiling(n, p, q):
    demand(len(p) == len(set(p)) and len(q) == len(set(q)), 'TILING_DUPLICATE')
    frequencies = Counter((x+y) % n for x in p for y in q)
    demand(set(frequencies) == set(range(n)) and all(v == 1 for v in frequencies.values()),
           'TILING_NOT_DIRECT_COVER')
    demand(not (difference_classes(p, n) & difference_classes(q, n)), 'TILING_GCD')


def verify_packing(data, pc, qc, ga, gy):
    demand(set(data) == {'n', 'P80_divisor_screen_witness', 'P_triangles', 'Q_conflict_cliques'},
           'PACK_SCHEMA')
    demand(data['n'] == N, 'PACK_N')
    tris = data['P_triangles']
    demand(len(tris) == 16, 'P_TRIANGLE_COUNT')
    used = set()
    for tri in tris:
        demand(len(tri) == 3 and len(set(tri)) == 3, 'P_TRIANGLE_DUPLICATE')
        demand(set(tri) <= pc, 'P_TRIANGLE_CANDIDATE')
        demand(not (used & set(tri)), 'P_TRIANGLE_OVERLAP')
        demand(all(conflicts(x, y, gy) for x, y in combinations(tri, 2)), 'P_TRIANGLE_EDGE')
        used.update(tri)
    qs = data['Q_conflict_cliques']
    demand(len(qs) == 130, 'Q_CLIQUE_COUNT')
    used_q = set()
    for group in qs:
        demand(bool(group) and len(group) == len(set(group)), 'Q_CLIQUE_DUPLICATE')
        demand(set(group) <= qc, 'Q_CLIQUE_CANDIDATE')
        demand(not (used_q & set(group)), 'Q_CLIQUE_OVERLAP')
        demand(all(conflicts(x, y, ga) for x, y in combinations(group, 2)), 'Q_CLIQUE_EDGE')
        used_q.update(group)
    demand(used_q == qc, 'Q_CLIQUE_COVERAGE')
    w = data['P80_divisor_screen_witness']
    demand(len(w) == 80 and len(set(w)) == 80, 'P80_DUPLICATE')
    demand(set(A) <= set(w) <= pc, 'P80_CANDIDATE')
    demand(not any(conflicts(x, y, gy) for x, y in combinations(w, 2)), 'P80_EDGE')
    return {'P_triangle_count': len(tris), 'P_triangle_vertices': len(used),
            'P_bound': len(pc)-2*len(tris), 'Q_clique_count': len(qs),
            'Q_clique_size_histogram': dict(sorted(Counter(map(len, qs)).items())),
            'Q_covered_vertices': len(used_q), 'Q_bound': len(qs),
            'P80_size': len(w), 'P80_witness': w}


def independence_stats(xs, forbidden):
    """Exhaust all subsets of a small residue class, not just a matching bound."""
    counts = {}
    witness = None
    maximum = -1
    for size in range(len(xs)+1):
        num = 0
        for subset in combinations(xs, size):
            if all(not conflicts(x, y, forbidden) for x, y in combinations(subset, 2)):
                num += 1
                if size > maximum:
                    maximum, witness = size, list(subset)
        counts[size] = num
    return {'size': len(xs), 'independent_counts_by_size': counts,
            'maximum': maximum, 'maximizer': witness}


def check_pairs(pairs, pool, forbidden, expected_count, reason):
    demand(len(pairs) == expected_count, reason + '_COUNT')
    flattened = [v for pair in pairs for v in pair]
    demand(all(len(pair) == 2 for pair in pairs) and len(set(flattened)) == len(flattened),
           reason + '_DISJOINT')
    demand(set(flattened) <= set(pool), reason + '_POOL')
    demand(all(conflicts(x, y, forbidden) for x, y in pairs), reason + '_EDGE')


def neighborhood(graph, chosen):
    result = set()
    for x in chosen:
        result.update(graph[x])
    return result


def hall_distribution(left, right, graph, k):
    """Intersect non-neighbor masks; graph has the exact integer edge relation."""
    full = (1 << len(right)) - 1
    nonneighbor = []
    for x in left:
        mask = full
        for j, y in enumerate(right):
            if y in graph[x]:
                mask &= ~(1 << j)
        nonneighbor.append(mask)
    counts = Counter()
    minimum = len(right)+1
    examples = []
    for inds in combinations(range(len(left)), k):
        bits = full
        for idx in inds:
            bits &= nonneighbor[idx]
        count = len(right) - bits.bit_count()
        counts[count] += 1
        if count < minimum:
            minimum = count
            examples = [[left[i] for i in inds]]
        elif count == minimum:
            examples.append([left[i] for i in inds])
    demand(sum(counts.values()) == comb(len(left), k), 'HALL_ENUMERATION')
    return {'k': k, 'subsets': sum(counts.values()), 'minimum': minimum,
            'minimizers': counts[minimum], 'minimizing_subsets': examples,
            'histogram': dict(sorted(counts.items()))}


def hall_threshold(graph, chosen, threshold):
    demand(len(neighborhood(graph, chosen)) >= threshold, 'HALL_NEIGHBORS')


def verify_match(match, c2, c4):
    demand(len(match) == 6, 'P264_COUNT')
    demand(all(gcd(x-y, N) == 264 for x, y in match), 'P264_GCD')
    demand({x for x, _ in match} == set(c2) and {y for _, y in match} == set(c4),
           'P264_COVER')


def validate_seed(seed, extras, anchors, forbidden):
    demand(len(seed) == 6 and len(set(seed)) == 6, 'SEED_DUPLICATE')
    demand(all(sum(x in extras[j] for x in seed) == 2 for j in (1, 2, 7)), 'SEED_CLASSES')
    demand(not any(conflicts(x, y, forbidden) for x, y in combinations(seed, 2)), 'SEED_CONFLICT')
    demand(not any(conflicts(x, y, forbidden) for x in seed for y in anchors), 'SEED_ANCHOR')


def main():
    started = clock()
    t0 = time.monotonic()
    output = ROOT / 'finite-receipt-v1.json'
    demand(not output.exists(), 'RECEIPT_ALREADY_EXISTS')
    mb = (ROOT / 'manifest-v1.json').read_bytes()
    demand(sha(mb) == MANIFEST_SHA, 'MANIFEST_SHA')
    manifest = json.loads(mb)
    inputs = []
    blobs = []
    for spec in manifest['inputs_in_read_order']:
        b = Path(spec['path']).read_bytes()
        check_source(b, spec)
        blobs.append(b)
        inputs.append({'role': spec['role'], 'path': spec['path'],
                       'sha256': sha(b), 'bytes': len(b), 'LF': b.count(b'\n')})
    demand(len(inputs) == 12, 'INPUT_COUNT')
    mutated = bytearray(blobs[3])
    mutated[0] ^= 1
    source_control = rejected(lambda: check_source(bytes(mutated), manifest['inputs_in_read_order'][3]), 'SOURCE_SHA')

    ga, gy = difference_classes(A, N), difference_classes(Y, N)
    demand(ga == {3, 5, 8, 11} and gy == {1, 2, 6, 12}, 'ANCHOR_GCD')
    pc = candidate_set(N, A, gy)
    qc = candidate_set(N, Y, ga)
    demand(len(pc) == 112 and len(qc) == 286 and set(A) <= pc and set(Y) <= qc,
           'CANDIDATE_COUNTS')
    data = json.loads(blobs[3])
    packing = verify_packing(data, pc, qc, ga, gy)
    demand(packing['P_bound'] == 80 and packing['Q_bound'] == 130, 'PACK_BOUNDS')
    bad = deepcopy(data)
    bad['P_triangles'][0][1] = bad['P_triangles'][0][0]
    triangle_control = rejected(lambda: verify_packing(bad, pc, qc, ga, gy), 'P_TRIANGLE_DUPLICATE')
    bad = deepcopy(data)
    bad['Q_conflict_cliques'][-1] = bad['Q_conflict_cliques'][-1][:-1]
    if not bad['Q_conflict_cliques'][-1]:
        bad['Q_conflict_cliques'][-1] = [data['Q_conflict_cliques'][-2][0]]
    q_mutation_reason = rejected(lambda: verify_packing(bad, pc, qc, ga, gy), 'Q_CLIQUE_COVERAGE')
    bad = deepcopy(data)
    bad['P80_divisor_screen_witness'][1] = bad['P80_divisor_screen_witness'][0]
    p80_control = rejected(lambda: verify_packing(bad, pc, qc, ga, gy), 'P80_DUPLICATE')
    validate_tiling(12, [0, 2, 4], [0, 1, 6, 7])
    tiling_control = rejected(lambda: validate_tiling(12, [0, 2, 4], [0, 1, 6, 8]),
                               'TILING_NOT_DIRECT_COVER')

    divisors = [d for d in range(1, N+1) if N % d == 0 and d <= 80 and N//d <= 130]
    after_11 = [d for d in divisors if d != 11]
    demand(divisors == [11,12,15,20,22,24,30,33,40,44,55,60,66], 'DIVISORS')
    p1 = sorted(x for x in pc if x % 3 == 1)
    p2 = sorted(x for x in pc if x % 5 == 2)
    p4 = sorted(x for x in pc if x % 5 == 4)
    demand(p1 == [88,253,256,415,418,583,748,913,916,1075,1078,1243], 'P3_CLASS')
    demand(p2 == [132,407,792,872,987,1067], 'P5_CLASS2')
    demand(p4 == [264,344,459,539,924,1199], 'P5_CLASS4')
    p3_pairs = [(88,916),(256,748),(253,415),(583,1075)]
    check_pairs(p3_pairs, p1, gy, 4, 'P3_PAIRS')
    p1_stats = independence_stats(p1, gy)
    p2_stats = independence_stats(p2, gy)
    p4_stats = independence_stats(p4, gy)
    demand(p1_stats['maximum'] <= 8 and p2_stats['maximum'] <= 6, 'P_CAPACITY')
    special = {x for x in p1 if x % 5 != 3}
    demand(special == {256,415,916,1075}, 'P15_SPECIAL')
    blocking = {88:916,253:415,418:256,583:1075,748:256,913:415,1078:256,1243:415}
    demand(set(blocking) == set(p1)-special and all(y in special and conflicts(x,y,gy)
           for x,y in blocking.items()), 'P15_BLOCKING')
    p15_relaxed = [c for c in combinations(p1, 5) if sum(x % 5 == 3 for x in c) <= 1]
    p15_survivors = [c for c in p15_relaxed if all(not conflicts(x,y,gy) for x,y in combinations(c,2))]
    demand(len(p15_relaxed) == 8 and not p15_survivors, 'P15_EXHAUSTION')
    no_q4mod6 = [x for x in qc if x % 6 == 4]
    demand(not no_q4mod6, 'Q_MOD6_4')
    q22_edges = {1:[(891,386),(971,276),(561,716),(641,1266)],
                 2:[(627,722),(707,282),(47,612),(1287,1052)],
                 3:[(363,68),(443,618),(693,1058),(773,948)]}
    q22 = {}
    for r in (1, 2, 3):
        xs = sorted(x for x in qc if x % 5 == r and x % 3 != 1)
        demand(len(xs) == 10 and sum(x % 2 for x in xs) == 4, 'Q22_COUNTS')
        check_pairs(q22_edges[r], xs, {5}, 4, 'Q22_PAIRS')
        capacity = independence_stats(xs, {5})
        full_capacity = independence_stats(xs, ga)
        demand(capacity['maximum'] <= 6, 'Q22_CAPACITY')
        fixed_counts = [sum(x % 5 == r and x % 11 == j and x % 3 == 1 for x in qc)
                        for j in range(11)]
        demand(max(fixed_counts) <= 4, 'Q22_FIXED_CRT')
        q22[r] = {'non_one_mod3': xs, 'odd_count': 4, 'gcd5_pairs': q22_edges[r],
                  'gcd5_capacity': capacity, 'full_anchor_gcd_capacity': full_capacity,
                  'fixed_mod11_one_mod3_counts': fixed_counts}
    after_balance = [d for d in after_11 if not (d % 3 == 0 and d//3 > 8)
                     and not (d % 5 == 0 and d//5 > 6)]
    demand(after_balance == [12,15,20,22,24,44], 'BALANCE_FILTER')
    after_15_22 = [d for d in after_balance if d not in (15,22)]
    demand(after_15_22 == [12,20,24,44], 'FOUR_BORDER_FILTER')

    left = sorted(x for x in qc if x % 11 == 0 and x != 0)
    right = sorted(x for x in qc if x % 11 == 3 and x != 14)
    demand(len(left) == len(right) == 25, 'HALL_VERTEX_COUNTS')
    graph = {x:{y for y in right if gcd(x-y, N) in {3,5,8}} for x in left}
    reverse = {y:{x for x in left if y in graph[x]} for y in right}
    demand(all(not conflicts(x, 14, ga) for x in left) and
           all(not conflicts(y, 0, ga) for y in right), 'HALL_ANCHORS')
    forward = hall_distribution(left, right, graph, 9)
    backward = hall_distribution(right, left, reverse, 8)
    demand((forward['minimum'],forward['minimizers']) == (18,11), 'HALL_FORWARD')
    demand((backward['minimum'],backward['minimizers']) == (17,10), 'HALL_BACKWARD')
    mini = {i:{i} for i in range(4)}
    mini_hall = hall_distribution(list(range(4)), list(range(4)), mini, 2)
    demand(mini_hall['histogram'] == {2:6}, 'HALL_POSITIVE_CONTROL')
    mini_bad = {i:set(v) for i,v in mini.items()}
    mini_bad[0].remove(0)
    mini_mutated = hall_distribution(list(range(4)), list(range(4)), mini_bad, 2)
    demand(mini_mutated['histogram'] == {1:3,2:3}, 'HALL_SMALL_MUTATION')
    witness = forward['minimizing_subsets'][0]
    hall_threshold(graph, witness, 18)
    graph_bad = {x:set(v) for x,v in graph.items()}
    removed_target = min(neighborhood(graph, witness))
    removed_edges = sum(removed_target in graph_bad[x] for x in witness)
    for x in witness:
        graph_bad[x].discard(removed_target)
    demand(len(neighborhood(graph_bad, witness)) == 17, 'HALL_MUTATION_SIZE')
    hall_control = rejected(lambda: hall_threshold(graph_bad, witness, 18), 'HALL_NEIGHBORS')

    match = [(132,924),(407,1199),(792,264),(872,344),(987,459),(1067,539)]
    verify_match(match, p2, p4)
    altered_match = list(match)
    altered_match[0] = (132,264)
    match_control = rejected(lambda: verify_match(altered_match, p2, p4), 'P264_GCD')
    pigeonhole = {}
    for k in (3,4):
        no_edge = []
        count = 0
        for c in combinations(p2,k):
            for d in combinations(p4,k):
                count += 1
                if not any(x in c and y in d for x,y in match):
                    no_edge.append([list(c),list(d)])
        pigeonhole[k] = {'tested':count,'avoids_all_six_edges':len(no_edge),
                         'example_if_any': no_edge[0] if no_edge else None}
    demand(pigeonhole[3]['avoids_all_six_edges'] == 20 and
           pigeonhole[4]['tested'] == 225 and pigeonhole[4]['avoids_all_six_edges'] == 0,
           'P264_PIGEONHOLE')

    js = (1,2,7)
    forbidden = ga | {264}
    extras = {j:sorted(x for x in qc if x % 11 == j and x % 3 != 1) for j in js}
    demand([len(extras[j]) for j in js] == [10,10,10], 'SEED_POOLS')
    slots = defaultdict(list)
    for q in sorted(qc):
        if q % 3 == 1:
            slots[(q % 11,q % 8)].append(q)
    demand(len(slots) == 44 and all(x % 2 == 1 for v in slots.values() for x in v), 'SLOTS')
    demand(all(gcd(x-y,N) == 264 for v in slots.values() for x,y in combinations(v,2)),
           'SLOT_CAPACITY')
    pairs = [list(combinations(extras[j], 2)) for j in js]
    total = admitted = slot_reject = quota_reject = residual = 0
    open_hist = Counter()
    quota_first_class = Counter()
    compatible_example = slot_example = quota_example = None
    for triple in product(*pairs):
        seed = tuple(x for pair in triple for x in pair)
        total += 1
        if any(conflicts(x,y,forbidden) for x,y in combinations(seed,2)):
            continue
        if any(conflicts(x,y,forbidden) for x in seed for y in Y):
            continue
        admitted += 1
        if compatible_example is None:
            compatible_example = list(seed)
        opened = Counter()
        for (j,_), group in slots.items():
            if any(all(not conflicts(candidate,s,forbidden) for s in seed) for candidate in group):
                opened[j] += 1
        number_open = sum(opened.values())
        open_hist[number_open] += 1
        if number_open < 22:
            slot_reject += 1
            if slot_example is None:
                slot_example = {'seed':list(seed), 'open_slots':number_open}
            continue
        bounds = {}
        for j in js:
            available = [x for x in extras[j] if x not in seed
                         and all(not conflicts(x,s,forbidden) for s in seed)
                         and all(not conflicts(x,y,forbidden) for y in Y)]
            bounds[j] = 2 + opened[j] + len(available)
        failed = [j for j in js if bounds[j] < 6]
        if failed:
            quota_reject += 1
            quota_first_class[failed[0]] += 1
            if quota_example is None:
                quota_example = {'seed':list(seed), 'open_slots':number_open,
                                 'open_by_mod11':dict(opened), 'class_upper_bounds':bounds,
                                 'failed_classes':failed}
            demand(all(bounds[j] >= 2 for j in js), 'QUOTA_RELAXATION_CONTROL')
        else:
            residual += 1
    demand((total,admitted,slot_reject,quota_reject,residual) == (91125,1143,1089,54,0),
           'SEED_EXHAUSTION')
    validate_seed(compatible_example, extras, Y, forbidden)
    duplicate = list(compatible_example)
    duplicate[1] = duplicate[0]
    seed_control = rejected(lambda: validate_seed(duplicate, extras, Y, forbidden), 'SEED_DUPLICATE')
    semantic_mutation = None
    for i, old in enumerate(compatible_example):
        for replacement in extras[old % 11]:
            trial = list(compatible_example)
            trial[i] = replacement
            try:
                validate_seed(trial, extras, Y, forbidden)
            except Failure as exc:
                if str(exc) == 'SEED_CONFLICT':
                    semantic_mutation = {'original':compatible_example, 'mutated':trial,
                                         'reason':str(exc)}
                    break
        if semantic_mutation:
            break
    demand(semantic_mutation is not None, 'NO_SEED_CONFLICT_MUTATION')
    demand(quota_reject == 54 and all(j in js for j in quota_first_class), 'QUOTA_CONTROL')
    after_hall = [d for d in after_15_22 if d != 12]
    after_forced = [d for d in after_hall if d != 20]
    demand(after_forced == [24,44] and [N//d for d in after_forced] == [55,30], 'FINAL_SIZES')

    result = {
        'kind':'F114_INDEPENDENT_FINITE_REPLAY',
        'start_clock':started, 'clock_before_receipt_write':clock(),
        'elapsed_seconds_monotonic':round(time.monotonic()-t0, 3),
        'python_version':sys.version, 'checker_sha256':sha(Path(__file__).read_bytes()),
        'manifest_sha256':sha(mb), 'inputs_in_manifest_order':inputs,
        'anchors':{'A':A,'Y':Y,'A_difference_gcds':sorted(ga),'Y_difference_gcds':sorted(gy)},
        'candidate_sets':{'P':sorted(pc),'Q':sorted(qc)},
        'packing':packing,
        'divisor_branches':{'packing':divisors,'after_11_prime_balance':after_11,
                            'after_simple_balance':after_balance,'after_15_22':after_15_22,
                            'after_Hall_12':after_hall,'after_264_20':after_forced},
        'residue_checks':{'P_mod3_1':p1,'P_mod3_1_disjoint_pairs':p3_pairs,
                          'P_mod3_1_exact_independence':p1_stats,
                          'P_mod5_2':p2,'P_mod5_2_exact_independence':p2_stats,
                          'P_mod5_4':p4,'P_mod5_4_exact_independence':p4_stats,
                          'P15_blocking_edges':blocking,'P15_relaxed_subsets':p15_relaxed,
                          'P15_gcd_compatible_subsets':len(p15_survivors),
                          'Q_mod6_4_count':len(no_q4mod6),'Q22_classes':q22},
        'hall':{'L':left,'R':right,'edges':sum(map(len,graph.values())),
                'forward':forward,'reverse':backward},
        'forced_264':{'P_matching':match,'P_pigeonhole':pigeonhole,
                      'Q_extra_candidates':extras,'Q_one_mod3_count':sum(map(len,slots.values())),
                      'Q_slot_count':len(slots),
                      'Q_slot_size_histogram':dict(sorted(Counter(map(len,slots.values())).items())),
                      'seeds':total,'compatible':admitted,'slot_rejections':slot_reject,
                      'quota_rejections':quota_reject,'residual':residual,
                      'open_slot_histogram':dict(sorted(open_hist.items())),
                      'quota_first_failure_mod11':dict(sorted(quota_first_class.items())),
                      'compatible_seed_example':compatible_example,
                      'slot_rejection_example':slot_example,'quota_rejection_example':quota_example},
        'controls':{'source_one_byte_flip':source_control,
                    'positive_tiling_Z12':{'P':[0,2,4],'Q':[0,1,6,7]},
                    'mutated_tiling':tiling_control,
                    'mutated_P_triangle':triangle_control,'mutated_Q_partition':q_mutation_reason,
                    'mutated_P80_duplicate':p80_control,
                    'hall_positive_4_by_4':mini_hall,'hall_positive_mutated':mini_mutated,
                    'hall_real_edge_mutation':{'removed_right_vertex':removed_target,
                        'edges_removed':removed_edges,'original_min_subset':witness,
                        'mutated_neighborhood':17,'rejection':hall_control},
                    'mutated_P264_matching':match_control,'P264_positive_3_plus_3':pigeonhole[3],
                    'P15_drop_conflicts_exposes_false_survivors':len(p15_relaxed),
                    'valid_seed':compatible_example,'duplicate_seed':seed_control,
                    'seed_conflict_mutation':semantic_mutation,
                    'quota_relaxed_from_6_to_2_passes_all_54':quota_reject},
        'scope':'Exact necessary integer screens and relaxed seed bound only; not a border theorem, a code solver, an order-1320 exclusion, a formal proof, an independent-family review or novelty clearance.'}
    encoded = (json.dumps(result, indent=2, sort_keys=True) + '\n').encode()
    with output.open('xb') as f:
        f.write(encoded)
    print(json.dumps({'start_clock':started,'clock_before_receipt_write':result['clock_before_receipt_write'],
          'elapsed_seconds_monotonic':result['elapsed_seconds_monotonic'],
          'checker_sha256':result['checker_sha256'],'receipt_sha256':sha(encoded),
          'receipt_bytes':len(encoded),'receipt_LF':encoded.count(b'\n'),
          'counts':{'P':len(pc),'Q':len(qc),'Hall_forward':[forward['minimum'],forward['minimizers']],
                    'Hall_reverse':[backward['minimum'],backward['minimizers']],
                    'seeds':[total,admitted,slot_reject,quota_reject,residual],
                    'final_P_sizes':after_forced}}, indent=2))


if __name__ == '__main__':
    main()
