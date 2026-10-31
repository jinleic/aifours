#!/usr/bin/env python3
"""Target every minimum-conflict outsider of one verified binary support.

Each candidate is checked against the original neighbour lookup; SAT/UNSAT
statuses apply only to the explicitly held 83-word subset. This is not a global
bound. No historical solver result is treated as a correctness premise.
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import time
from z3 import Bool, Not, Or, PbGe, Solver, is_true, sat

here = Path(__file__).resolve().parent
PROFILE = here / 'frontier-20261028-binary-conflict-profile-result.json'
CANDIDATE = here / 'frontier-20261028-fd-law-search-precise-result.json'
OUTPUT = here / 'frontier-20261028-targeted-exchanges-result.json'
NEIGHBOURS = {
    1: (2,3,4,5,6,7), 2: (1,3,7,9,10), 3: (1,2,4,8,9),
    4: (1,3,5,8,10), 5: (1,4,6,9,10), 6: (1,5,7,8,9),
    7: (1,2,6,8,10), 8: (3,4,6,7,9,10), 9: (2,3,5,6,8),
    10: (2,4,5,7,8),
}


def conflict(a, b):
    for v, neighbours in NEIGHBOURS.items():
        if (a >> (v-1)) & 1 != (b >> (v-1)) & 1:
            if all((a >> (u-1)) & 1 == (b >> (u-1)) & 1 for u in neighbours):
                return True
    return False


def valid(words):
    return len(set(words)) == len(words) and all(not conflict(a,b) for a,b in combinations(words, 2))


def main():
    started = time.monotonic()
    profile_raw, candidate_raw = PROFILE.read_bytes(), CANDIDATE.read_bytes()
    profile, candidate = json.loads(profile_raw), json.loads(candidate_raw)
    original = set(candidate['support_words_one_based_bitsets'])
    assert len(original) == 88 and valid(sorted(original))
    results, best = [], set(original)
    for idx, item in enumerate(profile['minimum_witnesses']):
        outsider = item['word']
        blockers = {w for w in original if conflict(outsider, w)}
        assert len(blockers) == 5 and blockers == set(item['blockers']) and outsider not in original
        keep = original - blockers
        pool = [w for w in range(1024) if w not in keep and all(not conflict(w, k) for k in keep)]
        assert outsider in pool and blockers <= set(pool)
        choices = [Bool(f'x_{idx}_{w}') for w in pool]
        constraints = [Or(Not(choices[i]), Not(choices[j]))
                       for i,j in combinations(range(len(pool)),2) if conflict(pool[i], pool[j])]
        solver = Solver()
        solver.set(timeout=2000)
        solver.add(constraints)
        solver.add(choices[pool.index(outsider)])
        solver.add(PbGe([(x,1) for x in choices], 6))
        status = solver.check()
        entry = {'outsider': outsider, 'removed_blockers': sorted(blockers),
                 'pool_size': len(pool), 'improve_to_89_status': str(status)}
        if status == sat:
            model = solver.model()
            chosen = {w for w, x in zip(pool, choices) if is_true(model.eval(x, model_completion=True))}
            replacement = keep | chosen
            assert len(replacement) >= 89 and valid(sorted(replacement))
            if len(replacement) > len(best):
                best = replacement
            entry['new_support_size'] = len(replacement)
            entry['new_support'] = sorted(replacement)
        else:
            solver2 = Solver()
            solver2.set(timeout=2000)
            solver2.add(constraints)
            solver2.add(choices[pool.index(outsider)])
            solver2.add(PbGe([(x,1) for x in choices], 5))
            move = solver2.check()
            entry['same_size_status'] = str(move)
            if move == sat:
                model = solver2.model()
                chosen = {w for w,x in zip(pool, choices) if is_true(model.eval(x, model_completion=True))}
                replacement = keep | chosen
                assert len(replacement) >= 88 and valid(sorted(replacement))
                entry['same_size_support'] = sorted(replacement)
                if len(replacement) > len(best):
                    best = replacement
        results.append(entry)
    output = {'profile_sha256': sha256(profile_raw).hexdigest(),
              'candidate_sha256': sha256(candidate_raw).hexdigest(),
              'outsiders_attempted': len(results), 'attempts': results,
              'best_size': len(best), 'best_support': sorted(best),
              'independent_lookup_pair_check': valid(sorted(best)),
              'original_20_over_3_strict_test': len(best)**3 > 2**20,
              'elapsed_seconds': time.monotonic() - started,
              'limits': 'Only minimum-five-conflict outsiders and these fixed retained subsets; no global binary or other-alphabet optimum is established.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:
        json.dump(output,stream,indent=2)
        stream.write('\n')
    summary = {'outsiders_attempted':len(results),'best_size':len(best),
               'improvement_status_counts':{},'same_size_status_counts':{},
               'elapsed_seconds':output['elapsed_seconds'], 'limits':output['limits']}
    for entry in results:
        a=entry['improve_to_89_status']; summary['improvement_status_counts'][a]=summary['improvement_status_counts'].get(a,0)+1
        if 'same_size_status' in entry:
            a=entry['same_size_status']; summary['same_size_status_counts'][a]=summary['same_size_status_counts'].get(a,0)+1
    print(json.dumps(summary,indent=2))


if __name__ == '__main__':
    main()
