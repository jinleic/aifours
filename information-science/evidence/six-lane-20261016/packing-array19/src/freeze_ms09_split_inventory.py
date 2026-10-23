#!/usr/bin/env python3
"""Freeze the exact pending easy M2 ms09 one-column job set and rigorous retained-output upper bounds BEFORE any
new generating helper (parent approval 2026-10-18 ~01:0x). This is resource/inventory calculation, not placement
materialization or a SAT/nonexistence result. Run behind with_token15.
The DP counts all per-row-class (a,b,p) choices satisfying the existing extend_b row-budget and capacity conditions
and totals (4,4,2), but ignores inter-class incompatibilities. Every actual extend_b raw assignment is one DP path;
therefore orbit placements <= raw assignments <= this exact DP upper count. Every placement has ten row numbers
<=18 in three lists, so JSON output <=60*upper+65536 bytes (header/receipt margin). Bound >64MiB => DEFER, not enumerate.
The exact orbit count is NOT fabricated: the complete orbit universe is frozen here; actual complete num_placements
and the list SHA must be pinned after generation and before any batch solve (pending parent denominator clarification).
"""
import hashlib
import json
import os
import time
from collections import Counter

import aggregate15 as AG

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C2 = os.path.join(LANE, 'cycle2')
ALLOWANCE = 64 * 1024 * 1024
P0 = [4, 3, 3, 3, 3, 3]


def digest(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def upper_count(data, index):
    sk = data['skeletons'][index]
    c0, leave = data['c0'], data['L']
    special = [p for p in data['profiles'] if list(p) != P0]
    assert c0 == 5 and len(special) == 3 and all(list(p) == [4, 4, 3, 3, 3, 2] for p in special)
    ns = len(special)
    types = [tuple(t) for t in sk['types']]
    degrees = [sum(v in t for t in types) for v in range(c0)]
    members = list(types)
    for v in range(c0):
        members += [(v,)] * (4 - degrees[v])
    members += [()] * sk['empty']
    assert len(members) == 19
    classes = Counter(members)

    def row_ok(t, e):
        return t + e - (ns - 1) <= 2 and t + e + (ns - 1) >= 2 - leave

    dp = {(0, 0, 0): 1}
    options = []
    for ms, cap in classes.items():
        per_block = 1 if ms else cap
        choices = []
        for a in range(min(per_block, cap, 4) + 1):
            for b in range(min(per_block, cap - a, 4) + 1):
                for p in range(min(per_block, cap - a - b, 2) + 1):
                    rest = cap - a - b - p
                    if a + b and not row_ok(len(ms), 1):
                        continue
                    if p and not row_ok(len(ms), -1):
                        continue
                    if rest and not row_ok(len(ms), 0):
                        continue
                    choices.append((a, b, p))
        options.append({'membership': list(ms), 'rows': cap, 'role_count_options': len(choices)})
        nd = {}
        for (sa, sb, sp), n in dp.items():
            for a, b, p in choices:
                state = (sa + a, sb + b, sp + p)
                if state[0] <= 4 and state[1] <= 4 and state[2] <= 2:
                    nd[state] = nd.get(state, 0) + n
        dp = nd
    upper = dp.get((4, 4, 2), 0)
    return upper, options


def main():
    skpath = os.path.join(C2, 'skel-b', 'skeletons-b-ms09.json')
    data = json.load(open(skpath))
    easy = []
    for line in open(os.path.join(C2, 'm2-jobs-easy.txt')):
        if not line.startswith('9:'):
            continue
        rng = line.strip().split(':', 1)[1]
        if '-' in rng:
            lo, hi = map(int, rng.split('-'))
            easy.extend(range(lo, hi + 1))
        else:
            easy.append(int(rng))
    assert len(easy) == 28 and len(set(easy)) == 28
    jobs, skipped = [], []
    for bi in sorted(easy):
        direct = AG.jl(os.path.join(C2, 'm2skel_drat', 'ms09_b%05d.json' % bi))
        partdir = os.path.join(C2, 'm2part_drat', 'ms09_b%05d' % bi)
        summary = AG.jl(os.path.join(partdir, 'summary_batched.json'))
        if AG.certified(direct) or (summary and summary.get('decided_unsat')):
            skipped.append({'b_index': bi, 'reason': 'already complete direct or split; no new enumeration/solve'})
            continue
        ext = os.path.join(partdir, 'ext.json')
        ub, opts = upper_count(data, bi)
        jobs.append({'job': '9:%d' % bi, 'b_index': bi, 'missing_list': not os.path.exists(ext),
                     'existing_list_sha256': digest(ext) if os.path.exists(ext) else None,
                     'raw_assignment_dp_upper': ub, 'complete_output_upper_bytes': 60 * ub + 65536,
                     'within_64mib_allowance': 60 * ub + 65536 <= ALLOWANCE,
                     'class_options': opts, 'skeleton_sha256': hashlib.sha256(json.dumps(data['skeletons'][bi], sort_keys=True).encode()).hexdigest(),
                     'denominator': 'ALL compatible class assignments modulo full skeleton automorphisms and A/B swap; exact orbit count to be pinned, never truncated'})
    assert len(jobs) == 26 and len(skipped) == 2
    hard = []
    for line in open(os.path.join(C2, 'm2-jobs-part.txt')):
        if not line.startswith('9:'):
            continue
        bi = int(line.strip().split(':')[1])
        ep = os.path.join(C2, 'm2part_drat', 'ms09_b%05d' % bi, 'ext.json')
        e = json.load(open(ep))
        assert e['num_placements'] == len(e['placements'])
        hard.append({'job': '9:%d' % bi, 'path': os.path.relpath(ep, LANE), 'sha256': digest(ep), 'num_placements': e['num_placements']})
    assert len(hard) == 43
    # Bound sanity checks against three already-complete enumerations; no files altered.
    controls = []
    for bi in (2, 20, 55):
        e = json.load(open(os.path.join(C2, 'm2part_drat', 'ms09_b%05d' % bi, 'ext.json')))
        ub, _ = upper_count(data, bi)
        raw = e['raw_class_assignments']
        assert e['num_placements'] <= raw <= ub
        controls.append({'b_index': bi, 'actual_raw': raw, 'actual_orbits': e['num_placements'], 'dp_upper': ub, 'bound_holds': True})
    srcs = ['extend_b.py', 'encode_skel_b.py', 'stream_check15.py', 'extend_exclusive15.py', 'run_m2_15.py', 'freeze_ms09_split_inventory.py']
    out = {'host_clock': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'scope': 'exact26 pending easy jobs, original43 hard lists retained unchanged',
           'source_sha256': {p: digest(os.path.join(LANE, 'src', p)) for p in srcs}, 'skeleton_file_sha256': digest(skpath),
           'stage_allowance_bytes': ALLOWANCE, 'jobs': jobs, 'skipped_complete': skipped, 'hard_lists_unchanged': hard,
           'bound_controls': controls, 'eligible_missing_jobs': [j['job'] for j in jobs if j['missing_list'] and j['within_64mib_allowance']],
           'deferred_excess_bounds': [j for j in jobs if not j['within_64mib_allowance']],
           'complete_placement_denominator_rule': 'every orbit from complete frozen extend_b enumeration; exact num_placements + SHA frozen before batch solve; no partial list accepted'}
    dest = os.path.join(C2, 'ms09-split-inventory-%s.json' % time.strftime('%Y%m%dT%H%M%S'))
    with open(dest, 'x') as f:
        json.dump(out, f, indent=1)
    print(dest)
    print(json.dumps({'pending_jobs': len(jobs), 'missing_eligible': len(out['eligible_missing_jobs']),
                      'deferred_excess_count': len(out['deferred_excess_bounds']),
                      'max_output_upper_bytes': max(j['complete_output_upper_bytes'] for j in jobs), 'hard_lists_preserved': len(hard)}))


if __name__ == '__main__':
    main()
