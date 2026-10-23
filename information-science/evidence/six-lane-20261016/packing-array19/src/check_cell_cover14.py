#!/usr/bin/env python3
"""Metadata/binding controls for the exact frozen six-unit s00468 cover in summarize14. Reads the real six receipts,
mutates only in-memory reads (never evidence files) and writes one new small receipt. Run behind with_token14.
Controls per symbol: missing receipt; wrong base SHA; wrong subcase SHA; wrong unit literal; duplicate symbol;
wrong CNF byte length; unchecked flag; reader failure; replay failure; non-VERIFIED checker line; SAT status.
Every altered cover must remain uncertified; SAT must still be listed. These are aggregation controls, not an
independent mathematical proof checker and not solver-proof mutation tests.
"""
import copy
import json
import os
import time
import summarize14 as A


def main():
    original = A.B.jl
    actual = A.cell_cover([])
    assert actual['all_six_checked'], 'actual six-unit cover is not fully bound/certified'
    checks = []
    mutations = ['missing', 'base_sha', 'subcase_sha', 'unit_literal', 'duplicate_symbol', 'cnf_bytes',
                 'unchecked', 'reader_failure', 'replay_failure', 'checker_not_verified', 'sat']
    try:
        for symbol in range(6):
            suffix = '/s%02d.json' % symbol
            for mutation in mutations:
                def altered(path, suffix=suffix, mutation=mutation, symbol=symbol):
                    r = original(path)
                    if not path.endswith(suffix) or '/cell-cover/' not in path or not r:
                        return r
                    if mutation == 'missing':
                        return None
                    r = copy.deepcopy(r)
                    if mutation == 'base_sha':
                        r['base_cnf_sha256'] = '0' * 64
                    elif mutation == 'subcase_sha':
                        r['cnf_sha256'] = '0' * 64
                    elif mutation == 'unit_literal':
                        r['unit_literal'] += 1
                    elif mutation == 'duplicate_symbol':
                        r['symbol'] = (symbol + 1) % 6
                    elif mutation == 'cnf_bytes':
                        r['cnf_bytes'] += 1
                    elif mutation == 'unchecked':
                        r['checked'] = False
                    elif mutation == 'reader_failure':
                        r['reader_ok'] = False
                    elif mutation == 'replay_failure':
                        r['replay_ok'] = False
                    elif mutation == 'checker_not_verified':
                        r['drat_trim']['s_lines'] = ['s NOT VERIFIED']
                    elif mutation == 'sat':
                        r['status'] = 'SAT'
                    return r
                A.B.jl = altered
                sats = []
                cover = A.cell_cover(sats)
                okay = not cover['all_six_checked'] and (mutation != 'sat' or bool(sats))
                checks.append({'symbol': symbol, 'mutation': mutation, 'cover_rejected': not cover['all_six_checked'],
                               'sat_listed': bool(sats), 'expected': okay})
                assert okay, (symbol, mutation)
    finally:
        A.B.jl = original
    result = {'host_clock': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'actual_cover_all_six_bound': actual['all_six_checked'],
              'base_cnf_sha256': actual['base_cnf_sha256'], 'controls': checks,
              'control_count': len(checks), 'all_expected': all(c['expected'] for c in checks),
              'scope': 'in-memory aggregate metadata/binding mutations only; no proof files/copies altered or checked'}
    path = os.path.join(A.LANE, 'cycle2', 'cell-cover-controls-%s.json' % time.strftime('%Y%m%dT%H%M%S'))
    with open(path, 'x') as f:
        json.dump(result, f, indent=1)
    print(path)
    print(json.dumps({k: result[k] for k in ('actual_cover_all_six_bound', 'control_count', 'all_expected')}))


if __name__ == '__main__':
    main()
