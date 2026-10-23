#!/usr/bin/env python3
"""PA19FinalFormulaBindings M2-split extension v1 (separate pinned extension, Main IRC ~04:2x): formula binding of the
M2 partbatch records cycle2/m2part_drat/msXX_bNNNNN/batch_*.json that M2 split coverage relies on, by the same method
as fb_m2_v1: point-in-time census first, in-RAM rebuild with the declared producer, compare, discard. Records already
bound by R8 (subcase-binding-result.json, the full m2part_drat stratum of 14:56) are reused by unchanged hash. Each
list (ext.json, extend_b output) is classified parent-bound only if its bytes equal R6's normalized-production-source
prediction with the R8-style field checks; otherwise FORMULA_EQUAL_LIST_PENDING (no extend_b replay here). No solver,
proof checker or proof; not UNSAT acceptance; not M2 coverage; STATUS not read.

Run: /opt/homebrew/opt/python@3.14/bin/python3.14 -B -I <desk>/fb_m2part_v1.py CMD --lane <LANE> [options]
  pin      --name N      census -> m2part-pins-N.json, m2part-jobs-N.jsonl.gz
  controls --pins SHA    in-memory overlays -> m2part-controls-N.json (must all be as expected before run)
  run      --pins SHA    rebuild -> m2part-N.jsonl.gz, m2part-run-N.json
"""
import copy
import gzip
import json
import os
import re
import sys
import time
import types
from collections import Counter, OrderedDict
from pathlib import Path

HERE = Path(__file__).resolve().parent
M2_SRC = HERE / 'fb_m2_v1.py'
M2_SHA = '49506607d3f6a50a10f4d9ceb5b526b7729cef125023968d9b1cbd73a1ad6f58'


def _load_m2():
    import hashlib
    b = M2_SRC.read_bytes()
    if hashlib.sha256(b).hexdigest() != M2_SHA:
        raise SystemExit('fb_m2_v1.py changed')
    mod = types.ModuleType('fb_m2_v1')
    mod.__file__ = str(M2_SRC)
    sys.modules['fb_m2_v1'] = mod
    exec(compile(b, str(M2_SRC), 'exec'), mod.__dict__)
    return mod


M = _load_m2()
F = M.F
L, REPO, S_IN = F.L, F.REPO, F.S_IN
PART = L / 'cycle2' / 'm2part_drat'
DIRRE = re.compile(r'^ms0([1-9])_b(\d{5})$')
BATCH = re.compile(r'^batch_(\d{5,6})_(\d{5,6})\.json$')


def cmd_pin(args):
    name = args['--name']
    fb, need, ok = F.disk_gate(4 * 1024 * 1024)
    if not ok:
        F.log('m2part pin %s DEFERRED: free %d < gate %d' % (name, fb, need))
        raise SystemExit('disk gate')
    m1r, esb, q0b = M.load_libs()
    t0 = time.time()
    with F.Token() as tok:
        token = {'name': tok.name, 'acquired_at': tok.acquired_at, 'waited_s': tok.waited_s}
        refs = F.check_refs()
        if not all(v['match'] for v in refs.values()):
            raise SystemExit('reference receipt mismatch')
        r8p = json.loads((F.R8D / 'pins.json').read_bytes())
        r8 = json.loads(F.REF['r8_result'][0].read_bytes())
        r8items = {it['path']: it for it in r8['items']}
        pred = {c['m2_dir']: (t, c['m2_ext']['R6_m2_regen_normalized_production_source'], c['m2_ext'].get('n'), c['b_index'])
                for t, c in r8p['cases'].items()}
        r6n = {c['tag']: c['counts']['m2_num'] for c in json.loads(F.REF['r6_result'][0].read_bytes())['cases']}
        lists, rows = OrderedDict(), []
        started = F.now()
        for dp in sorted(p for p in PART.iterdir() if p.is_dir()):
            d = dp.name
            m = DIRRE.match(d)
            recs = sorted(f for f in os.listdir(dp) if BATCH.match(f))
            if not recs:
                continue
            mi, bi = int(m.group(1)), int(m.group(2))
            eb = (dp / 'ext.json').read_bytes()
            E = json.loads(eb)
            n = len(E['placements'])
            pr = pred.get(d)
            li = OrderedDict([('path', 'cycle2/m2part_drat/%s/ext.json' % d), ('sha256', F.sha(eb)), ('bytes', len(eb)), ('n', n),
                              ('fields_ok', E.get('index') == bi and E.get('num_placements') == n
                               and E.get('source') == str(L / 'cycle2' / 'skel-b' / ('skeletons-b-ms%02d.json' % mi))),
                              ('R6_prediction', pr[1] if pr else None), ('R6_count', r6n.get(pr[0]) if pr else None),
                              ('bound_m1_tag', pr[0] if pr else None), ('summary_batched_present', (dp / 'summary_batched.json').exists())])
            li['parent_bound'] = bool(pr and li['sha256'] == pr[1] and li['fields_ok'] and n == li['R6_count'])
            cov = bytearray(n)
            for fn in recs:
                rel = 'cycle2/m2part_drat/%s/%s' % (d, fn)
                data = (dp / fn).read_bytes()
                try:
                    rec = json.loads(data)
                except ValueError:
                    rows.append(OrderedDict([('path', rel), ('dir', d), ('rec_sha', F.sha(data)), ('unreadable', True)]))
                    continue
                lo, hi = map(int, BATCH.match(fn).groups())
                why, tier = m1r.stream_predicate(rec)
                it = r8items.get(rel)
                prior = ({'receipt': 'pa19-subcase-binding-v1/subcase-binding-result.json', 'receipt_record_sha256': it['record_sha256'],
                          'generated': [it['generated'][k] for k in ('cnf_sha256', 'cnf_bytes', 'vars', 'clauses')]}
                         if it and it.get('status') == 'PASS' and it.get('record_sha256') == F.sha(data) else None)
                for i in range(lo, min(hi, n - 1) + 1):
                    cov[i] = 1
                rows.append(OrderedDict([('path', rel), ('dir', d), ('multiset', mi), ('b_index', bi), ('lo', lo), ('hi', hi),
                                         ('rec_sha', F.sha(data)), ('rev', rec.get('stream_check_revision')),
                                         ('status', rec.get('status')), ('encoder', rec.get('encoder')),
                                         ('runner', rec.get('runner')), ('declared_indices', rec.get('indices')),
                                         ('recorded', [rec.get('cnf_sha256'), rec.get('cnf_bytes')]),
                                         ('strict_predicate_reasons', why), ('strict_predicate_tier', tier), ('prior', prior)]))
            li['records'] = len(recs)
            li['batch_union_covers_list'] = n > 0 and all(cov)
            lists[d] = li
        for i, r in enumerate(rows):
            r['i'] = i
        finished = F.now()
    cnt = Counter('rev=%s|%s|%s|%s' % (r.get('rev'), r.get('status'), 'prior' if r.get('prior') else 'rebuild',
                                       'strict-pass' if r.get('strict_predicate_reasons') == [] else 'strict-fail') for r in rows)
    pins = OrderedDict([('title', 'PA19 M2 split (m2part_drat) formula-binding census %s' % name), ('recorded_started', started),
                        ('recorded_finished', finished), ('token', token), ('reference_receipts', refs),
                        ('code', {'fb_m2part_v1.py': F.sha_file(Path(__file__).resolve())[0], 'fb_m2_v1.py': M2_SHA,
                                  'encode_skel_b.py': M.ESB[1], 'm1_receipts_v1.py': M.M1R[1]}),
                        ('lists', lists), ('census', {'dirs_with_records': len(lists), 'records': len(rows), 'by_plan': dict(sorted(cnt.items())),
                                                      'lists_parent_bound': sum(1 for v in lists.values() if v['parent_bound']),
                                                      'lists_producer_only': [k for k, v in lists.items() if not v['parent_bound']]}),
                        ('production_call', 'run_m2_12-15.py run_split / run_m2partbatch5: nv, cl = encode_skel_b.build_partbatch(D["c0"], '
                                            '[tuple(t) for t in sk["types"]], sk["empty"], special, [E["placements"][i] for i in idx]); '
                                            'encode_skel_b.cnf_bytes(nv, cl); record indices = [idx[0], idx[-1]]'),
                        ('resources', {**F.usage(), 'elapsed_s': round(time.time() - t0, 2)})])
    jp, pp = F.HERE / ('m2part-jobs-%s.jsonl.gz' % name), F.HERE / ('m2part-pins-%s.json' % name)
    jb = gzip.compress(('\n'.join(F.jline(r) for r in rows) + '\n').encode(), mtime=0)
    F.write_x(jp, jb)
    pins['jobs_file'] = {'path': jp.name, 'sha256': F.sha(jb), 'lines': len(rows)}
    F.dump_x(pp, pins)
    F.log('m2part pin %s: %d records in %d dirs (%s); lists parent-bound %d; %s sha %s' % (
        name, len(rows), len(lists), dict(cnt), pins['census']['lists_parent_bound'], pp.name, F.sha_file(pp)[0]))
    print(json.dumps({'pins_sha256': F.sha_file(pp)[0], 'census': pins['census']}, indent=1))


def load(args):
    pp = next((p for p in F.HERE.glob('m2part-pins-*.json') if F.sha_file(p)[0] == args['--pins']), None)
    if pp is None:
        raise SystemExit('no m2part pins with that sha')
    pins = json.loads(pp.read_bytes())
    jb = (F.HERE / pins['jobs_file']['path']).read_bytes()
    if F.sha(jb) != pins['jobs_file']['sha256']:
        raise SystemExit('jobs changed')
    return pp, pins, [json.loads(x) for x in gzip.decompress(jb).decode().splitlines()]


class Ctx:
    def __init__(self, pins):
        self.pins, self.inp, self._E = pins, None, {}

    def lst(self, d):
        if d not in self._E:
            li = self.pins['lists'][d]
            b = (L / li['path']).read_bytes()
            self._E[d] = (json.loads(b) if F.sha(b) == li['sha256'] else None, F.sha(b))
        return self._E[d]


def evaluate(esb, inp, ctx, job, ov=None):
    ov = ov or {}
    res = OrderedDict([('i', job['i']), ('path', job['path'])])
    checks = OrderedDict()
    try:
        data = (L / job['path']).read_bytes()
    except FileNotFoundError:
        res['status'], res['reason'] = 'UNRESOLVED', 'record_missing'
        return res
    res['rec_sha'] = F.sha(data)
    if res['rec_sha'] != job['rec_sha']:
        res['checks_false'], res['status'] = ['record_sha_equals_pinned'], 'UNRESOLVED'
        return res
    if job.get('prior') and not ov:
        ok = job['prior']['receipt_record_sha256'] == res['rec_sha']
        res['gen'], res['status'] = job['prior']['generated'], ('PRIOR_R8_PASS' if ok else 'UNRESOLVED')
        return res
    rec = json.loads(data)
    if 'rec' in ov:
        rec = ov['rec'](copy.deepcopy(rec))
    d = job['dir']
    E, eh = ov['list'] if 'list' in ov else ctx.lst(d)
    li = ctx.pins['lists'][d]
    checks['list_sha_equals_pinned'] = E is not None and eh == ov.get('pinned_list_sha', li['sha256'])
    checks['multiset_field_equals_dir'] = rec.get('multiset') == job['multiset']
    checks['b_index_field_equals_dir'] = rec.get('b_index') == job['b_index']
    checks['indices_pair_equals_filename'] = rec.get('indices') == [job['lo'], job['hi']]
    checks['declared_encoder_build_partbatch'] = rec.get('encoder') == 'encode_skel_b.build_partbatch'
    lo, hi = ov.get('lohi', (job['lo'], job['hi']))
    checks['indices_within_list'] = E is not None and 0 <= lo <= hi < len(E['placements'])
    D = inp.skel(job['multiset'])
    checks['b_list_bound'] = D is not None
    cs = rec.get('cnf_sha256')
    checks['recorded_cnf_sha256_wellformed'] = isinstance(cs, str) and F.HEX64.match(cs) is not None
    bad = [k for k, v in checks.items() if v is False]
    if bad:
        res['checks_false'] = bad
        res['status'] = 'FAIL_INPUT_BINDING' if ('list_sha_equals_pinned' in bad or 'b_list_bound' in bad) else 'FAIL_STRUCTURAL'
        return res
    sk = D['skeletons'][job['b_index']]
    special = [p for p in D['profiles'] if list(p) != M.P0]
    pls = [E['placements'][i] for i in range(lo, hi + 1)]
    before = F.jdigest([D['c0'], sk, special, pls])
    t = time.perf_counter()
    try:
        nv, cl = esb.build_partbatch(D['c0'], [tuple(x) for x in sk['types']], sk['empty'], special, pls)
        b = esb.cnf_bytes(nv, cl)
    except Exception as ex:  # never a PASS
        res['checks_false'], res['status'], res['reason'] = ['rebuild_possible'], 'UNRESOLVED', 'rebuild not possible: %r' % (ex,)
        return res
    res['build_s'] = round(time.perf_counter() - t, 3)
    checks['inputs_not_mutated_by_encoder'] = before == F.jdigest([D['c0'], sk, special, pls])
    nvh, nch = F.header(b)
    res['gen'] = [F.sha(b), len(b), nvh, nch]
    res['rec'] = [rec.get('cnf_sha256'), rec.get('cnf_bytes')]
    checks['cnf_sha256_equal'] = res['gen'][0] == rec.get('cnf_sha256')
    checks['cnf_bytes_equal'] = res['gen'][1] == rec.get('cnf_bytes')
    bad = [k for k, v in checks.items() if v is False]
    res['checks_false'] = bad
    res['status'] = ('PASS' if li['parent_bound'] else 'FORMULA_EQUAL_LIST_PENDING') if not bad else 'MISMATCH'
    return res


def cmd_controls(args):
    pp, pins, jobs = load(args)
    m1r, esb, q0b = M.load_libs()
    inp, ctx = _inputs(pins), Ctx(pins)
    out = []
    with F.Token() as tok:
        token = {'name': tok.name, 'waited_s': tok.waited_s}
        j = next(x for x in jobs if not x.get('prior') and x.get('rev') in (14, 15) and x['lo'] > 0)
        nb = next(x for x in jobs if x['dir'] == j['dir'] and x['i'] != j['i'])
        mine = ctx.lst(j['dir'])[0]['placements'][j['lo']:j['hi'] + 1]
        od, ob, oE = None, None, None
        for k, v in pins['lists'].items():  # another dir's pinned list whose entries at this range differ
            if k == j['dir'] or v['n'] <= j['hi'] or k[:4] != j['dir'][:4]:
                continue
            cb = (L / v['path']).read_bytes()
            cE = json.loads(cb)
            if cE['placements'][j['lo']:j['hi'] + 1] != mine:
                od, ob, oE = k, cb, cE
                break
        if od is None:
            raise SystemExit('no other list with differing entries for the wrong-list control')
        wrong = json.loads((L / nb['path']).read_bytes())['cnf_sha256']
        cases = [('P_B_rebuild', j, {}, ['PASS', 'FORMULA_EQUAL_LIST_PENDING'], []),
                 ('P_C1_wrong_range', j, {'lohi': (j['lo'] - 1, j['hi'] - 1), 'force': True}, ['MISMATCH'], ['cnf_sha256_equal']),
                 ('P_C2_wrong_list', j, {'list': (oE, F.sha(ob))}, ['FAIL_INPUT_BINDING'], ['list_sha_equals_pinned']),
                 ('P_C2b_wrong_list_pinned', j, {'list': (oE, F.sha(ob)), 'pinned_list_sha': F.sha(ob)}, ['MISMATCH', 'UNRESOLVED'],
                  ['cnf_sha256_equal', 'rebuild_possible']),
                 ('P_C3_wellformed_wrong_sha', j, {'rec': lambda r, w=wrong: dict(r, cnf_sha256=w)}, ['MISMATCH'], ['cnf_sha256_equal']),
                 ('P_C4_declared_build_v2', j, {'rec': lambda r: dict(r, encoder='encode_skel_b.build_v2')}, ['FAIL_STRUCTURAL'],
                  ['declared_encoder_build_partbatch'])]
        for cid, job, ov, want, why in cases:
            ov2 = {k: v for k, v in ov.items() if k != 'force'}
            try:
                r = evaluate(esb, inp, ctx, job, ov2 or {'_': 1})
            except Exception as ex:
                r = {'status': 'EXCEPTION', 'reason': repr(ex)}
            got = r.get('checks_false') or ([r['reason']] if r.get('reason') else [])
            anyof = cid == 'P_C2b_wrong_list_pinned'
            ok = r.get('status') in want and ((any(w in got for w in why)) if anyof else all(w in got for w in why))
            out.append(OrderedDict([('id', cid), ('target', job['path']), ('expected_status', want), ('expected_reasons', why),
                                    ('status', r.get('status')), ('reasons', got), ('gen', r.get('gen')), ('as_expected', ok)]))
        # omitted batch: coverage of the dir's list without one record
        recs = [x for x in jobs if x['dir'] == j['dir']]
        n = pins['lists'][j['dir']]['n']
        cov = bytearray(n)
        for x in recs:
            if x['i'] != j['i']:
                for i in range(x['lo'], min(x['hi'], n - 1) + 1):
                    cov[i] = 1
        holes = n - sum(cov)
        out.append(OrderedDict([('id', 'P_C5_omitted_batch'), ('target', j['path']), ('holes_after', holes),
                                ('expected_holes', j['hi'] - j['lo'] + 1),
                                ('as_expected', pins['lists'][j['dir']]['batch_union_covers_list'] and holes == j['hi'] - j['lo'] + 1)]))
    name = pp.name[len('m2part-pins-'):-len('.json')]
    res = OrderedDict([('title', 'PA19 M2 split binding controls (in-memory overlays)'), ('pins', pp.name), ('token', token),
                       ('controls', out), ('all_as_expected', all(c['as_expected'] for c in out)), ('finished', F.now())])
    F.dump_x(F.HERE / ('m2part-controls-%s.json' % name), res)
    F.log('m2part controls %s: %d/%d as expected; sha %s' % (name, sum(c['as_expected'] for c in out), len(out),
                                                            F.sha_file(F.HERE / ('m2part-controls-%s.json' % name))[0]))
    print(json.dumps({'all_as_expected': res['all_as_expected'], 'unexpected': [c for c in out if not c['as_expected']]}, indent=1))


def _inputs(pins):
    """B lists via fb_m2_v1.Inputs semantics (S snapshot bytes == S/L/R0 pin and R3 B_byte_equal), re-derived here."""
    r0 = json.loads(F.REF['r0_pin_result'][0].read_bytes())['files']
    r3 = {row['multiset']: row for row in json.loads(M.R3[0].read_bytes())['rows']}
    skels = {}
    for mi in range(1, 10):
        rel = M.skel_rel(mi)
        sh, lh = F.sha_file(S_IN / rel)[0], F.sha_file(L / rel)[0]
        skels[str(mi)] = {'path': rel, 'S_sha256': sh, 'bound': sh == lh == r0.get(rel) and (r3.get(mi) or {}).get('B_byte_equal') is True}
    return M.Inputs({'b_skeleton_lists': skels})


def cmd_run(args):
    pp, pins, jobs = load(args)
    name = pp.name[len('m2part-pins-'):-len('.json')]
    m1r, esb, q0b = M.load_libs()
    inp, ctx = _inputs(pins), Ctx(pins)
    out_p = F.HERE / ('m2part-%s.jsonl.gz' % name)
    rows = []
    t0 = time.time()
    with F.Token() as tok:
        token = {'name': tok.name, 'acquired_at': tok.acquired_at, 'waited_s': tok.waited_s}
        for j in jobs:
            if j.get('unreadable'):
                rows.append(OrderedDict([('i', j['i']), ('path', j['path']), ('status', 'UNRESOLVED'), ('reason', 'unreadable at pin')]))
                continue
            try:
                rows.append(evaluate(esb, inp, ctx, j))
            except Exception as ex:
                rows.append(OrderedDict([('i', j['i']), ('path', j['path']), ('status', 'UNRESOLVED'), ('reason', 'driver exception %r' % (ex,))]))
    F.write_x(out_p, gzip.compress(('\n'.join(F.jline(r) for r in rows) + '\n').encode(), mtime=0))
    st = Counter(r['status'] for r in rows)
    res = OrderedDict([('name', name), ('pins', pp.name), ('token', token), ('evaluated', len(rows)), ('by_status', dict(st)),
                       ('not_pass', [r for r in rows if r['status'] not in ('PASS', 'PRIOR_R8_PASS')][:40]),
                       ('rows_file', {'path': out_p.name, 'sha256': F.sha_file(out_p)[0]}),
                       ('driver_sha256', F.sha_file(Path(__file__).resolve())[0]),
                       ('resources', {**F.usage(), 'elapsed_s': round(time.time() - t0, 2)}), ('finished', F.now())])
    F.dump_x(F.HERE / ('m2part-run-%s.json' % name), res)
    F.log('m2part run %s: %d evaluated, %s; sha %s' % (name, len(rows), dict(st), F.sha_file(F.HERE / ('m2part-run-%s.json' % name))[0]))
    print(json.dumps({k: res[k] for k in ('evaluated', 'by_status', 'resources')}, indent=1))


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else None
    args = F.parse_args(sys.argv[2:])
    F.require_env(args)
    os.chdir(F.HERE)
    fn = {'pin': cmd_pin, 'run': cmd_run, 'controls': cmd_controls}.get(cmd)
    if fn is None:
        raise SystemExit(__doc__)
    fn(args)


if __name__ == '__main__':
    main()
