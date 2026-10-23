#!/usr/bin/env python3
"""PA19FinalFormulaBindings aggregation v1: RESULT.json + exposure-leaf-hashes-v1.json from this desk's frozen outputs.
Reads only desk files (each re-hashed against the hash its producer logged/recorded) and the parent-pinned receipts
already verified at pin time; no lane file, no solver/checker, no new evaluation. Formula/list binding only: no UNSAT
acceptance, no M1/M2 coverage verdict, PA(19,8,6) undecided.

Run: /opt/homebrew/opt/python@3.14/bin/python3.14 -B -I <desk>/fb_finalize_v1.py --pins SHA [--m2 NAME=SHA ...]
"""
import gzip
import hashlib
import json
import os
import sys
import time
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PASS_LIST = ('BYTE_EQUAL', 'SEMANTIC_EQUAL_ALL_FIELDS')
FINAL_OK = ('PASS', 'PRIOR_R8_PASS', 'PRIOR_INC001_V2_PASS')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fsha(p):
    return sha(Path(p).read_bytes())


def now():
    return time.strftime('%Y-%m-%dT%H:%M:%S%z')


def gz_lines(p):
    out = []
    with gzip.open(p, 'rt') as f:
        for line in f:
            out.append(json.loads(line))
    return out


def main():
    args = dict(zip(sys.argv[1::2], sys.argv[2::2]))
    if not (sys.flags.dont_write_bytecode and sys.flags.isolated):
        raise SystemExit('run with -B -I')
    pins_b = (HERE / 'pins-v1.json').read_bytes()
    if sha(pins_b) != args.get('--pins'):
        raise SystemExit('pins sha mismatch')
    pins = json.loads(pins_b)
    jobs_b = (HERE / pins['jobs_file']['path']).read_bytes()
    if sha(jobs_b) != pins['jobs_file']['sha256']:
        raise SystemExit('jobs changed')
    jobs = [json.loads(x) for x in gzip.decompress(jobs_b).decode().splitlines()]
    outputs = OrderedDict()

    def rec_out(name):
        p = HERE / name
        if p.exists():
            outputs[name] = {'sha256': fsha(p), 'bytes': p.stat().st_size}
        return p

    # ---------------- split: every chosen record exactly once across parts
    parts = sorted(HERE.glob('split-run-v1-p*.json'))
    runs = []
    by_i = {}
    dup = []
    for rp in parts:
        run = json.loads(rp.read_bytes())
        prog = HERE / run['progress_file']['path']
        if fsha(prog) != run['progress_file']['sha256']:
            raise SystemExit('progress file changed: %s' % prog.name)
        rec_out(rp.name)
        rec_out(prog.name)
        runs.append({k: run[k] for k in ('part', 'started', 'finished', 'end_reason', 'token', 'evaluated_this_part',
                                         'done_before', 'by_status_this_part', 'resources', 'driver_sha256')})
        for r in gz_lines(prog):
            if r['i'] in by_i:
                dup.append(r['i'])
            by_i[r['i']] = r
    # list replays
    lists = OrderedDict()
    for lp in sorted((HERE / 'lists').glob('*-replay-v1-c*.json')) if (HERE / 'lists').exists() else []:
        d = json.loads(lp.read_bytes())
        rec_out('lists/' + lp.name)
        prev = lists.get(d['tag'])
        if prev is None or prev['status'] not in PASS_LIST:
            lists[d['tag']] = {'status': d['status'], 'receipt': 'lists/' + lp.name, 'receipt_sha256': fsha(lp),
                               'chunk': d.get('chunk'), 'seconds': (d.get('helper') or {}).get('seconds'),
                               'peak_child_rss_kb': (d.get('helper') or {}).get('peak_rss_kb'),
                               'child_rss_cap_kb': d.get('child_rss_cap_kb'), 'rc': d.get('rc'),
                               'guard_tripped': (d.get('helper') or {}).get('guard_tripped'),
                               'guard_reasons': (d.get('helper') or {}).get('guard_reasons'),
                               'replay_sha256': (d.get('fifo') or {}).get('sha256'), 'replay_bytes': (d.get('fifo') or {}).get('bytes'),
                               'stored_sha256': d['stored']['sha256'], 'comparison': (d.get('comparison') or {}).get('verdict'),
                               'differences': (d.get('comparison') or {}).get('differences'),
                               'stdout_summary_matches': d.get('stdout_summary_matches'), 'reason': d.get('reason')}
    chunks = []
    for cp in sorted((HERE / 'lists').glob('chunk-*-v1.json')) if (HERE / 'lists').exists() else []:
        c = json.loads(cp.read_bytes())
        rec_out('lists/' + cp.name)
        chunks.append({'file': 'lists/' + cp.name, 'sha256': fsha(cp), 'start': c.get('start'), 'end': c.get('end'),
                       'exclusive_locks': c.get('exclusive_locks'), 'deferred': c.get('deferred'),
                       'results': c.get('results'), 'driver_sha256': c.get('driver_sha256')})
    pending_tags = pins['split_census']['lists_pending_replay']
    list_bound = {t: (lists.get(t, {}).get('status') in PASS_LIST) for t in pending_tags}

    # per-record final status
    final = Counter()
    by_route = defaultdict(Counter)
    case_rows = OrderedDict()
    unresolved = []
    for j in jobs:
        r = by_i.get(j['i'])
        cp = pins['split_cases'][j['case']]
        grp = '%s|%s' % (j['route'], j['case'][:4])
        if r is None:
            st = 'NOT_EVALUATED'
        elif r['status'] == 'FORMULA_EQUAL_LIST_PENDING':
            st = 'PASS_LIST_REPLAYED' if list_bound.get(j['case']) else 'FORMULA_EQUAL_LIST_PENDING'
        else:
            st = r['status']
        final[st] += 1
        by_route[grp][st] += 1
        c = case_rows.setdefault(j['case'], OrderedDict([('route', j['route']), ('n', cp['list']['n']),
                                                          ('list_sha256', cp['list']['sha256']),
                                                          ('list_binding', 'parent-R6/v2' if cp['list']['parent_bound'] else
                                                           ('replayed-' + str(lists.get(j['case'], {}).get('status'))
                                                            if j['case'] in lists else 'PENDING (no replay)')),
                                                          ('spec_sha256', cp['spec']['S_sha256']),
                                                          ('chosen', 0), ('status', Counter())]))
        c['chosen'] += 1
        c['status'][st] += 1
        if st not in FINAL_OK + ('PASS_LIST_REPLAYED',):
            unresolved.append({'i': j['i'], 'case': j['case'], 'path': j['path'], 'status': st,
                               'checks_false': (r or {}).get('checks_false'), 'reason': (r or {}).get('reason')})
    for c in case_rows.values():
        c['all_records_bound'] = all(k in FINAL_OK + ('PASS_LIST_REPLAYED',) for k in c['status'])
        c['status'] = dict(c['status'])
    split = OrderedDict([
        ('denominator_chosen_records', len(jobs)), ('evaluated_records', len(by_i)), ('duplicate_evaluations', len(dup)),
        ('final_status', dict(final)), ('by_route_ms_final_status', {k: dict(v) for k, v in sorted(by_route.items())}),
        ('prior_bound_reused_by_unchanged_hash', sum(v for k, v in final.items() if k.startswith('PRIOR'))),
        ('cases', len(case_rows)), ('cases_all_records_bound', sum(c['all_records_bound'] for c in case_rows.values())),
        ('cases_not_all_bound', [t for t, c in case_rows.items() if not c['all_records_bound']]),
        ('unresolved_or_pending_records', len(unresolved)), ('unresolved_first_50', unresolved[:50]),
        ('runs', runs)])
    # ---------------- E0
    e0r = HERE / 'e0-result-v1.json'
    e0 = None
    if e0r.exists():
        d = json.loads(e0r.read_bytes())
        if fsha(HERE / d['rows_file']['path']) != d['rows_file']['sha256']:
            raise SystemExit('e0 rows changed')
        rec_out('e0-result-v1.json')
        rec_out(d['rows_file']['path'])
        e0 = {k: d[k] for k in ('denominator', 'evaluated', 'by_status', 'not_pass', 'started', 'finished', 'token',
                                'resources', 'stored_cnf_bytes_hashed', 'transformation')}
    # ---------------- controls
    ctl = None
    if (HERE / 'controls-v1.json').exists():
        d = json.loads((HERE / 'controls-v1.json').read_bytes())
        rec_out('controls-v1.json')
        ctl = {'count': d['count'], 'all_as_expected': d['all_as_expected'],
               'unexpected': [c['id'] for c in d['controls'] if not c['as_expected']],
               'ids': [c['id'] for c in d['controls']], 'token': d.get('token'), 'resources': d.get('resources')}
    # ---------------- M2 (optional)
    m2 = OrderedDict()
    for spec in [v for k, v in zip(sys.argv[1::2], sys.argv[2::2]) if k == '--m2']:
        nm, psha = spec.split('=')
        pp = next(p for p in HERE.glob('m2-pins-*.json') if fsha(p) == psha)
        mp = json.loads(pp.read_bytes())
        rec_out(pp.name)
        rec_out(mp['jobs_file']['path'])
        mj = [json.loads(x) for x in gzip.decompress((HERE / mp['jobs_file']['path']).read_bytes()).decode().splitlines()]
        rr = HERE / ('m2-run-%s.json' % nm)
        run = json.loads(rr.read_bytes()) if rr.exists() else None
        rows = {}
        if run:
            rec_out(rr.name)
            if fsha(HERE / run['progress_file']['path']) != run['progress_file']['sha256']:
                raise SystemExit('m2 progress changed')
            rec_out(run['progress_file']['path'])
            rows = {r['i']: r for r in gz_lines(HERE / run['progress_file']['path'])}
        cnt = Counter()
        strict = Counter()
        bad = []
        for j in mj:
            r = rows.get(j['i'])
            st = r['status'] if r else 'NOT_EVALUATED'
            sp = 'strict-pass' if j.get('strict_predicate_reasons') == [] else 'strict-fail'
            cnt['%s|%s' % (j['kind'], st)] += 1
            strict['%s|%s|%s' % (j['kind'], sp, st)] += 1
            if st != 'PASS':
                bad.append({'path': j['path'], 'status': st, 'checks_false': (r or {}).get('checks_false'),
                            'strict_predicate_reasons': j.get('strict_predicate_reasons'), 'reason': (r or {}).get('reason')})
        m2[nm] = {'pins': pp.name, 'pins_sha256': psha, 'census': mp['census'], 'base_pin': mp.get('base_pin'),
                  'records': len(mj), 'by_kind_status': dict(cnt), 'by_kind_strict_status': dict(sorted(strict.items())),
                  'not_pass': bad[:60], 'not_pass_count': len(bad),
                  'run': {k: run[k] for k in ('started', 'finished', 'end_reason', 'token', 'evaluated', 'resources')} if run else None}
    if (HERE / 'm2-controls-v1.json').exists():
        d = json.loads((HERE / 'm2-controls-v1.json').read_bytes())
        rec_out('m2-controls-v1.json')
        m2['controls'] = {'all_as_expected': d['all_as_expected'], 'count': len(d['controls']),
                          'unexpected': [c['id'] for c in d['controls'] if not c['as_expected']]}
    # ---------------- exposure leaf hashes for the native-replay desk (bridge F-A NONE class, 238 cases)
    expo_cases = {t for t, c in pins['split_cases'].items() if c.get('delivery_exposure_case')}
    leaves = []
    for j in jobs:
        if j['case'] not in expo_cases:
            continue
        r = by_i.get(j['i']) or {}
        rev_ok = j['rev'] in (5, 9)
        if not rev_ok:
            continue
        st = r.get('status')
        if st == 'FORMULA_EQUAL_LIST_PENDING':
            st = 'PASS_LIST_REPLAYED' if list_bound.get(j['case']) else st
        leaves.append(OrderedDict([('case', j['case']), ('path', j['path']), ('record_sha256', j['rec_sha']),
                                   ('lo', j['lo']), ('hi', j['hi']), ('rev', j['rev']), ('solver', j['solver']),
                                   ('parent_cnf', (r.get('gen') or [None, None, None, None])), ('status', st),
                                   ('source', 'reused ' + j['prior']['receipt'] if j['prior'] else 'rebuilt fb_v1 split')]))
    leaf_doc = OrderedDict([('title', 'Parent leaf CNF hashes for the split records of the bridge F-A NONE-class cases '
                                      '(rev 5 / rev 9 chosen split records only; b/c5 base CNFs are R5-bound)'),
                            ('recorded_at', now()), ('split_cases', sorted(expo_cases)),
                            ('base_cnf_cases_note', 'route b (198) and c5 (37) exposure cases use their R5-bound base CNFs '
                                                    '(PA19FinalReceiptAudit M1-manifest base_cnf_sha256); not repeated here'),
                            ('leaves', leaves), ('count', len(leaves))])
    lb = (json.dumps(leaf_doc, indent=1) + '\n').encode()
    with open(HERE / 'exposure-leaf-hashes-v1.json', 'xb') as f:
        f.write(lb)
    rec_out('exposure-leaf-hashes-v1.json')
    # ---------------- code
    code = OrderedDict((n, fsha(HERE / n)) for n in ('fb_v1.py', 'fb_v2.py', 'fb_m2_v1.py', 'fb_finalize_v1.py')
                       if (HERE / n).exists())
    res = OrderedDict([
        ('title', 'PA19FinalFormulaBindings v1: parent formula/placement binding for the PA(19,8,6) M1-complete candidate'),
        ('recorded_at', now()),
        ('not_claimed', 'Formula and placement-list binding only. No SAT solver, proof checker or native proof replay ran; '
                        'no UNSAT acceptance, no M1/M2 coverage verdict, no theorem; PA(19,8,6) undecided. List replays '
                        'are re-executions of the unchanged lane producer (extend_p1q.py), not an independently authored '
                        'enumerator; split/E0 rebuilds re-execute the declared lane encoders, not new encodings.'),
        ('pins', {'pins-v1.json': args['--pins'], 'jobs-v1.jsonl.gz': pins['jobs_file']['sha256'],
                  'reference_receipts': {k: v['sha256'] for k, v in pins['reference_receipts'].items()},
                  'code_pins': {k: v['sha256'] for k, v in pins['code'].items()}, 'serializers': pins['serializers'],
                  'interpreters': pins['interpreters'], 'networkx': pins['networkx']}),
        ('census', {'split': pins['split_census'], 'e0': pins['e0']['census'], 'list_plan': pins['list_plan']}),
        ('split', split), ('lists', {'pending_tags': pending_tags, 'replays': lists,
                                     'bound': sum(1 for v in list_bound.values() if v),
                                     'not_bound': [t for t, v in list_bound.items() if not v], 'chunks': chunks}),
        ('e0', e0), ('controls', ctl), ('m2', m2 or None), ('code_sha256', code), ('outputs', outputs)])
    with open(HERE / 'RESULT.json', 'x') as f:
        json.dump(res, f, indent=1)
        f.write('\n')
    print(json.dumps({'split_final': dict(final), 'cases_all_bound': split['cases_all_records_bound'],
                      'lists_bound': res['lists']['bound'], 'lists_not_bound': res['lists']['not_bound'],
                      'e0': e0 and e0['by_status'], 'controls': ctl and ctl['all_as_expected'],
                      'm2': {k: v.get('by_kind_status') for k, v in m2.items() if isinstance(v, dict) and 'by_kind_status' in v},
                      'RESULT_sha256': fsha(HERE / 'RESULT.json')}, indent=1))


if __name__ == '__main__':
    main()
