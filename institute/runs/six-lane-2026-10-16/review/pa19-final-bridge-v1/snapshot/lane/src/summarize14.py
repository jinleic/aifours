#!/usr/bin/env python3
"""[Margin variant: aggregate14 base plus exact frozen cell cover; both prior13 and new14 records accepted under the same full predicate. Output STATUS14.json; base STATUS14_BASE.json.]
Run the existing strict summarize11 aggregation, then add ONLY the frozen six-unit cover of ms06_s00468
(cell row8,column6). The six exact files s00..s05 must each have the correct identity, unit literal, pinned-base
SHA, reconstructed subcase-CNF SHA/size, and full revision-13 predicate. The summary file is never trusted. A miss
leaves the original case open; any SAT record is listed even if malformed. Output STATUS12.json; STATUS11 remains
the base aggregation without this cell-cover route.
"""
import contextlib
import hashlib
import io
import json
import os

import aggregate14 as B

LANE = B.LANE
TAG = 'ms06_s00468'
BASE_SHA = '137407b6532fea61a682467507462e146cef6dd546b9a496a6bd18ad0ceba994'
ROW, COL = 8, 6


def cell_cover(sats):
    base = open(os.path.join(LANE, 'cases19skel', 'cnf', TAG + '.cnf'), 'rb').read()
    if hashlib.sha256(base).hexdigest() != BASE_SHA:
        return {'all_six_checked': False, 'error': 'pinned base SHA mismatch'}
    head, sep, body = base.partition(b'\n')
    p, cnf, nv, nc = head.split()
    assert sep and (p, cnf) == (b'p', b'cnf') and base.endswith(b'\n')
    body_sha = hashlib.sha256(body).hexdigest()
    records = []
    for symbol in range(6):
        rel = os.path.join('cycle2', 'cell-cover', TAG, 'r08_c06', 's%02d.json' % symbol)
        r = B.jl(os.path.join(LANE, rel))
        if r and r.get('status') == 'SAT':
            sats.append(('cell-cover', rel))
        literal = 421 + symbol
        unit = ('%d 0\n' % literal).encode()
        expected = ('p cnf %d %d\n' % (int(nv), int(nc) + 1)).encode() + body + unit
        expected_sha = hashlib.sha256(expected).hexdigest()
        binding = bool(r and r.get('tag') == TAG and type(r.get('row')) is int and r['row'] == ROW
                       and type(r.get('column')) is int and r['column'] == COL
                       and type(r.get('symbol')) is int and r['symbol'] == symbol
                       and type(r.get('unit_literal')) is int and r['unit_literal'] == literal
                       and r.get('unit_clause') == unit.decode() and r.get('base_header') == head.decode()
                       and r.get('base_cnf_sha256') == BASE_SHA and r.get('base_body_sha256') == body_sha
                       and r.get('base_byte_identical') is True and r.get('exact_one_unit_append') is True
                       and r.get('base_bytes') == len(base) and r.get('cnf_sha256') == expected_sha
                       and r.get('cnf_bytes') == len(expected))
        checked = bool(binding and r.get('stream_check_revision') in (13, 14) and B.certified(r))
        records.append({'symbol': symbol, 'file': rel, 'unit_literal': literal, 'expected_cnf_sha256': expected_sha,
                        'binding_ok': binding, 'checked': checked})
    return {'tag': TAG, 'row': ROW, 'column': COL, 'base_cnf_sha256': BASE_SHA, 'records': records,
            'all_six_checked': len(records) == 6 and all(r['checked'] for r in records)}


def main():
    with contextlib.redirect_stdout(io.StringIO()):
        B.main()
    out = json.load(open(os.path.join(LANE, 'STATUS14_BASE.json')))
    cover = cell_cover(out['sat_results'])
    out['cell_cover_s00468'] = cover
    if cover['all_six_checked'] and TAG in out['M1_open_tags']:
        out['M1_open_tags'].remove(TAG)
        out['M1_open'] = len(out['M1_open_tags'])
        p = out['per_multiset']['ms06']
        p['M1_certified'] += 1
        p['M1_how']['cell-six-unit'] = 1
        if TAG not in out['M2_open_tags']:
            p['both'] += 1
    with open(os.path.join(LANE, 'STATUS14.json'), 'w') as f:
        json.dump(out, f, indent=1)
    print(json.dumps({k: v for k, v in out.items() if not k.endswith('_tags') and k != 'uncertified_list'}, indent=1))


if __name__ == '__main__':
    main()
