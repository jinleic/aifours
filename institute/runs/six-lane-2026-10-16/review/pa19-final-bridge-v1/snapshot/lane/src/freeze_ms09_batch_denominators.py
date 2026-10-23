#!/usr/bin/env python3
"""After all approved ms09 list generation, pin the COMPLETE exact denominator/hash inventory BEFORE batch solves.
Read-only on lists/receipts; writes a new creation-only small JSON receipt. Run under an existing token, or while the
operator holds the natural exclusive boundary with no research stages. Completed direct/split coverage is skipped,
never rerun. Every newly generated job must have a matching complete-denominator pin and a clean helper guard.
All43 original hard-list hashes must still match the frozen resource inventory. No solver/enumerator/proof copy.
"""
import hashlib
import json
import os
import time

import aggregate15 as A

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C2 = os.path.join(LANE, 'cycle2')
INVENTORY = os.path.join(C2, 'ms09-split-inventory-20261018T010710.json')
INVENTORY_SHA = 'd45499bdcb4718a38fafa0f82f49c8d28d06ab680444b6e1ad2cad6c82ca414a'


def digest(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def main():
    assert digest(INVENTORY) == INVENTORY_SHA
    inv = json.load(open(INVENTORY))
    new_ids = {j['b_index'] for j in inv['jobs']}
    for old in inv['hard_lists_unchanged']:
        assert digest(os.path.join(LANE, old['path'])) == old['sha256']
    complete, pending, sats = [], [], []
    for bi in range(71):
        name = 'ms09_b%05d' % bi
        direct = A.jl(os.path.join(C2, 'm2skel_drat', name + '.json'))
        if direct and direct.get('status') == 'SAT':
            sats.append({'case': name, 'source': 'direct'})
        if A.certified(direct):
            complete.append({'job': '9:%d' % bi, 'method': 'direct', 'record_sha256': digest(os.path.join(C2, 'm2skel_drat', name + '.json'))})
            continue
        d = os.path.join(C2, 'm2part_drat', name)
        ep = os.path.join(d, 'ext.json')
        ext = json.load(open(ep))
        n = ext['num_placements']
        assert type(n) is int and n >= 0 and n == len(ext['placements'])
        sha = digest(ep)
        if bi in new_ids:
            pins = []
            for f in os.listdir(d):
                if f.startswith('complete-denominator-') and f.endswith('.json'):
                    pin = json.load(open(os.path.join(d, f)))
                    helper = pin.get('helper') or {}
                    if pin.get('sha256') == sha and pin.get('num_placements') == n and pin.get('bytes') == os.path.getsize(ep):
                        assert helper.get('rc') == 0 and helper.get('guard_tripped') is False and helper.get('stop') == 'self'
                        assert (helper.get('admission') or {}).get('projected_plan_within_enforced_cap') is True
                        pins.append({'path': os.path.relpath(os.path.join(d, f), LANE), 'sha256': digest(os.path.join(d, f))})
            assert pins, ('missing complete clean denominator pin', name)
        else:
            pins = []
        cov = A.split_cover(d, n, sats, 'm2part_drat')
        item = {'job': '9:%d' % bi, 'path': os.path.relpath(ep, LANE), 'list_sha256': sha, 'list_bytes': os.path.getsize(ep),
                'complete_placement_denominator': n, 'checked_placement_indices': len(cov.intersection(range(n))),
                'batch_size': 100, 'full_batch_count': (n + 99)//100, 'complete_pins': pins}
        if len(cov.intersection(range(n))) == n:
            item['method'] = 'complete one-column cover'
            complete.append(item)
        else:
            pending.append(item)
    assert not sats, ('SAT claim blocks nonexistence ledger', sats)
    out = {'host_clock': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'inventory_sha256': INVENTORY_SHA,
           'ms09_cases': 71, 'already_complete_cases': complete, 'pending_batch_jobs': pending,
           'pending_case_count': len(pending), 'pending_complete_placement_denominator_sum': sum(x['complete_placement_denominator'] for x in pending),
           'total_expected_full_batches': sum(x['full_batch_count'] for x in pending),
           'original_43_hard_lists_unchanged': True, 'no_truncation': True,
           'settings': {'solve_seconds': 600, 'check_seconds': 1200, 'batch': 100, 'count_ceiling': 2,
                        'predicate': 'full unchanged guard15 standard-checker predicate; any miss stays UNKNOWN'},
           'scope': 'exact complete list counts/hashes before any remaining batch solve; helper generation alone is not solver acceptance'}
    path = os.path.join(C2, 'ms09-batch-denominators-%s.json' % time.strftime('%Y%m%dT%H%M%S'))
    with open(path, 'x') as f:
        json.dump(out, f, indent=1)
    print(path)
    print(json.dumps({k: out[k] for k in ('ms09_cases','pending_case_count','pending_complete_placement_denominator_sum','total_expected_full_batches','original_43_hard_lists_unchanged')}))


if __name__ == '__main__':
    main()
