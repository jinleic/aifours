#!/usr/bin/env python3
"""Addendum aggregator v1: RESULT-addendum-v1.json for the stages after RESULT.json (eb6e591f...ef6c): M2 split
(fb_m2part_v1), the ms09_b00002 extend_b list replay (fb_m2list_v1) and the M2 delta census/run after the 05:21 freeze
(fb_m2_v2 --no-token, Main IRC). Reads only desk files, each checked against the SHA logged when it was written; no lane
read, no evaluation. Binding only: no UNSAT acceptance, no M2 coverage, STATUS not read.
Run: python3.14 -B -I fb_addendum_v1.py --delta-pins SHA
"""
import gzip
import hashlib
import json
import sys
import time
from collections import Counter, OrderedDict
from pathlib import Path

HERE = Path(__file__).resolve().parent
KNOWN = {'m2part-pins-p1.json': '3accf20721e66a4f65829ad2bdc7411016358ada742350d1b6ba7c61fc270f9a',
         'm2part-controls-p1.json': 'cb23ea810ad6c682f5e42f37df37e4c5931befe706303a41cbb43e454ef212b5',
         'm2part-run-p1.json': 'f94f746ac8f7778782db397a8e53cc276efd75d37e0cad8749bcd4fdc6e34006',
         'm2list/ms09_b00002-replay-v1.json': '3954a54a7835451066e455cb153e80607d9d3930d125d39dd0e5bd0c18d069f5',
         'm2-pins-v1.json': 'eaecc88ff256324f513f28beeaa9307b6fc93b66498d0aaa4a356bae17bae75c',
         'RESULT.json': 'eb6e591f7422d7b0b06d045458cf01f572d0da8a2e3e8d59cfb16090c046ef6c'}


def fsha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def jl(p):
    return json.loads(Path(p).read_bytes())


def main():
    args = dict(zip(sys.argv[1::2], sys.argv[2::2]))
    for n, w in KNOWN.items():
        if fsha(HERE / n) != w:
            raise SystemExit('input changed: %s' % n)
    files = OrderedDict((n, w) for n, w in KNOWN.items())
    # M2 split
    pp, cr, rr = jl(HERE / 'm2part-pins-p1.json'), jl(HERE / 'm2part-controls-p1.json'), jl(HERE / 'm2part-run-p1.json')
    if fsha(HERE / rr['rows_file']['path']) != rr['rows_file']['sha256']:
        raise SystemExit('m2part rows changed')
    files[rr['rows_file']['path']] = rr['rows_file']['sha256']
    rows = [json.loads(x) for x in gzip.decompress((HERE / rr['rows_file']['path']).read_bytes()).decode().splitlines() if x.strip()]
    # ms09_b00002 replay with Main's parent acceptance conditions
    lr = jl(HERE / 'm2list/ms09_b00002-replay-v1.json')
    cmp_ = lr.get('comparison') or {}
    fifo = lr.get('fifo') or {}
    conds = OrderedDict([('status_byte_equal', lr.get('status') == 'BYTE_EQUAL'),
                         ('interpreter_sha_equals_frozen_pin', lr['pins']['interpreter']['sha256'] ==
                          'cbf84109626aa1013bbe408fbb9590bd0f1c1548f038b2221c6b8b87de26ca43'),
                         ('fifo_bytes_equal_comparison_bytes_le_32MiB', fifo.get('bytes') == cmp_.get('replay_bytes')
                          and (fifo.get('bytes') or 0) <= 32 * 1024 * 1024),
                         ('fifo_sha_equal_comparison_sha', fifo.get('sha256') == cmp_.get('replay_sha256')),
                         ('reader_completed_no_error', fifo.get('opened') is True and fifo.get('reader_error') is None
                          and fifo.get('reader_alive') is False),
                         ('no_guard_trip_rc0', lr.get('rc') == 0 and not (lr.get('helper') or {}).get('guard_tripped')),
                         ('post_inputs_unchanged', lr.get('post_inputs_unchanged') is True)])
    list_ok = all(conds.values())
    final = Counter()
    pending = []
    for r in rows:
        st = r['status']
        if st == 'FORMULA_EQUAL_LIST_PENDING' and r['path'].startswith('cycle2/m2part_drat/ms09_b00002/') and list_ok:
            st = 'PASS_LIST_REPLAYED'
        final[st] += 1
        if st not in ('PASS', 'PRIOR_R8_PASS', 'PASS_LIST_REPLAYED'):
            pending.append({'path': r['path'], 'status': st, 'checks_false': r.get('checks_false'), 'reason': r.get('reason')})
    m2split = OrderedDict([('pins', 'm2part-pins-p1.json'), ('census', pp['census']), ('controls_all_as_expected', cr['all_as_expected']),
                           ('controls_count', len(cr['controls'])), ('run_by_status', rr['by_status']), ('final_status', dict(final)),
                           ('not_bound', pending), ('dirs', len(pp['lists'])),
                           ('dirs_batch_union_covers_list', sum(1 for v in pp['lists'].values() if v['batch_union_covers_list'])),
                           ('dirs_batch_union_not_covering', [k for k, v in pp['lists'].items() if not v['batch_union_covers_list']]),
                           ('lists', {'R6_prediction_bound': pp['census']['lists_parent_bound'],
                                      'replayed_byte_equal': ['ms09_b00002'] if list_ok else []})])
    replay = OrderedDict([('receipt', 'm2list/ms09_b00002-replay-v1.json'), ('status', lr.get('status')),
                          ('output_bytes', fifo.get('bytes')), ('output_sha256', fifo.get('sha256')),
                          ('stored_sha256', cmp_.get('stored_sha256')), ('seconds', (lr.get('helper') or {}).get('seconds')),
                          ('peak_child_rss_kb', (lr.get('helper') or {}).get('peak_rss_kb')), ('token', lr.get('token')),
                          ('parent_acceptance_conditions', conds), ('list_bound', list_ok), ('cmd', lr.get('cmd'))])
    # delta
    dp = next(p for p in HERE.glob('m2-pins-*.json') if fsha(p) == args['--delta-pins'])
    dpins = jl(dp)
    files[dp.name] = args['--delta-pins']
    dname = dp.name[len('m2-pins-'):-len('.json')]
    drun = HERE / ('m2-run-%s.json' % dname)
    dres = None
    if drun.exists():
        d = jl(drun)
        files[drun.name] = fsha(drun)
        if fsha(HERE / d['progress_file']['path']) != d['progress_file']['sha256']:
            raise SystemExit('delta rows changed')
        files[d['progress_file']['path']] = d['progress_file']['sha256']
        drows = []
        with gzip.open(HERE / d['progress_file']['path'], 'rt') as f:
            for line in f:
                if line.strip():
                    drows.append(json.loads(line))
        dres = OrderedDict([('end_reason', d['end_reason']), ('evaluated', d['evaluated']), ('by_kind_status', d['by_kind_status']),
                            ('token', d['token']), ('resources', d['resources']),
                            ('not_pass', [r for r in drows if r['status'] != 'PASS'][:40])])
    ctl2 = HERE / 'm2-controls-v2.json'
    c2 = None
    if ctl2.exists():
        c = jl(ctl2)
        files[ctl2.name] = fsha(ctl2)
        c2 = {'all_as_expected': c['all_as_expected'], 'count': len(c['controls']), 'token': c.get('token'),
              'unexpected': [x['id'] for x in c['controls'] if not x['as_expected']]}
    delta = OrderedDict([('pins', dp.name), ('base_pin', dpins.get('base_pin')), ('frozen_at', dpins.get('recorded_started')),
                         ('census', dpins['census']), ('skipped_unchanged', dpins.get('delta_skipped_unchanged')),
                         ('removed_since_base', dpins.get('delta_removed')), ('token', dpins.get('token')),
                         ('controls_v2_on_v1_pins', c2), ('run', dres)])
    for n in ('fb_m2_v2.py', 'fb_addendum_v1.py', 'fb_m2part_v1.py', 'fb_m2list_v1.py'):
        files[n] = fsha(HERE / n)
    res = OrderedDict([('title', 'PA19FinalFormulaBindings addendum v1: M2 split, ms09_b00002 list replay, M2 delta after 05:21'),
                       ('recorded_at', time.strftime('%Y-%m-%dT%H:%M:%S%z')), ('extends', {'RESULT.json': KNOWN['RESULT.json']}),
                       ('not_claimed', 'Formula/list binding only; no solver/checker/native replay; no UNSAT acceptance; M2 coverage '
                                       'open; STATUS not read; producer re-execution is not an independently authored encoder.'),
                       ('m2_split', m2split), ('ms09_b00002_list_replay', replay), ('m2_delta', delta), ('files_sha256', files)])
    with open(HERE / 'RESULT-addendum-v1.json', 'x') as f:
        json.dump(res, f, indent=1)
        f.write('\n')
    print(json.dumps({'m2_split_final': dict(final), 'list_ok': list_ok, 'delta_census': dpins['census'],
                      'delta_run': dres and dres['by_kind_status'], 'controls_v2': c2,
                      'sha256': fsha(HERE / 'RESULT-addendum-v1.json')}, indent=1))


if __name__ == '__main__':
    main()
