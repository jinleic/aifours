#!/usr/bin/env python3
"""R8 incremental binding (PA19SubcaseBinding). Reuses the frozen R8 driver bind_subcases.py (imported
unchanged; its SHA-256 must equal the one in subcase-binding-result.json) and its pinned-src copies.

Subcommands (run from this directory with python3.14 -B -I, one process, under nice):
  pin-records  one time: byte copies of the frozen selection (sample-manifest.json items) into
               pinned-records/, made only where the live bytes still equal the snapshot SHA-256
  late         census of split records absent from population.jsonl (written after the R8 snapshot)
               and of snapshot records that changed or vanished; structural checks and in-memory
               formula regeneration with the declared encoder/serializer for every late record;
               each call writes a new incremental/inc-NNN/ directory (exist_ok=False)

Formula binding only: no solver, proof checker, CNF file or proof file; no UNSAT acceptance;
PA(19,8,6) undecided. subcase-binding-result.json is never modified.
"""
import ast
import json
import os
import sys
import time
from collections import Counter, OrderedDict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))
import bind_subcases as B  # noqa: E402

MAIN_RESULT = HERE / 'subcase-binding-result.json'
REC_DIR = HERE / 'pinned-records'
REC_MAN = HERE / 'pinned-records.sha256'
INC = HERE / 'incremental'
R5_SERIALIZERS = {'stream_check9.py': 'd3bcda4c149bf5b2ae94daa9539edb1a43f80bd113e77aebe93a735fb6aec901',
                  'stream_check8.py': '2aff810ca4761b435a4c65bddb8fe29f20dd809dd7c0a4c272df891c80d09cbe'}
NON_SPLIT = {'hard', 'hard5', 'proofstream', 'm2skel_drat', 'm2skel_strict', 'claims', 'checker-smoke', 'timing',
             'retention-measure', 'skel-b', 'control18', 'control13-part', 'control13-m2part', 'control13-v5',
             'a3', 'part', 'm2part_drat'}


def script_sha():
    return B.sha(Path(__file__).resolve().read_bytes())


def proc():
    d = B.proc_info()
    d['incremental_script_sha256'] = script_sha()
    return d


def main_receipt():
    b = MAIN_RESULT.read_bytes()
    r = json.loads(b)
    if r['code']['driver']['sha256'] != B.driver_sha():
        raise SystemExit('bind_subcases.py differs from the driver recorded in the main receipt')
    return r, B.sha(b)


def cmd_pin_records():
    B.require_flags()
    res, res_sha = main_receipt()
    man = json.loads(B.MANIFEST.read_bytes())
    REC_DIR.mkdir(exist_ok=False)
    lines, skipped = [], []
    for it in man['items']:
        p = B.L / it['path']
        try:
            b = p.read_bytes()
        except FileNotFoundError:
            skipped.append({'path': it['path'], 'reason': 'missing'})
            continue
        h = B.sha(b)
        if h != it['sha256']:
            skipped.append({'path': it['path'], 'reason': 'changed since snapshot', 'now_sha256': h,
                            'snapshot_sha256': it['sha256']})
            continue
        dst = REC_DIR / it['path']
        dst.parent.mkdir(parents=True, exist_ok=True)
        B.write_new(dst, b)
        os.chmod(dst, 0o444)
        if B.sha(dst.read_bytes()) != h:
            raise SystemExit('copy mismatch %s' % dst)
        lines.append('%s  %s' % (h, it['path']))
    mb = ('\n'.join(lines) + '\n').encode()
    B.write_new(REC_MAN, mb)
    os.chmod(REC_MAN, 0o444)
    B.readme('pin-records: %d of %d frozen-selection records copied byte-exact to pinned-records/ (manifest '
             'pinned-records.sha256 %s); skipped %d %s; main receipt %s unchanged' % (
                 len(lines), len(man['items']), B.sha(mb), len(skipped), skipped[:3], res_sha))
    print(json.dumps({'copied': len(lines), 'skipped': skipped, 'manifest_sha256': B.sha(mb)}, indent=1))


def sc_module(name, rd, ref_seg):
    """Pin and import a later stream_check revision for its cnf_bytes_of (only after checking that the
    function text equals stream_check4's and the bytes equal the R5 pin and the live file)."""
    live = B.L / 'src' / name
    b = live.read_bytes()
    pdir = rd / 'pinned-src'
    pdir.mkdir(exist_ok=True)
    B.write_new(pdir / name, b)
    os.chmod(pdir / name, 0o444)
    seg = ast.get_source_segment(b.decode(), next(n for n in ast.parse(b.decode()).body
                                                  if isinstance(n, ast.FunctionDef) and n.name == 'cnf_bytes_of'))
    info = {'sha256': B.sha(b), 'equals_R5_pin': B.sha(b) == R5_SERIALIZERS.get(name), 'R5_pin': R5_SERIALIZERS.get(name),
            'cnf_bytes_of_identical_to_stream_check4': seg == ref_seg}
    if not (info['equals_R5_pin'] and info['cnf_bytes_of_identical_to_stream_check4']):
        return None, info
    sys.path.insert(0, str(pdir))
    mod = __import__(name[:-3])
    if Path(mod.__file__).resolve() != (pdir / name).resolve():
        raise SystemExit('wrong %s import' % name)
    return mod, info


def list_split_records():
    out = OrderedDict()
    for fam, rel in B.FAMILY_DIRS:
        base = B.L / rel
        for d in sorted(os.listdir(base)):
            dp = base / d
            if not dp.is_dir():
                continue
            for fn in sorted(os.listdir(dp)):
                if fn in B.NONRECORD or B.parse_name(fn) is None:
                    continue
                out['%s/%s/%s' % (rel, d, fn)] = (fam, d, fn)
    return out


def other_trees():
    found = {}
    base = B.L / 'cycle2'
    for d in sorted(os.listdir(base)):
        dp = base / d
        if not dp.is_dir() or d in NON_SPLIT:
            continue
        n = 0
        for root, _, fs in os.walk(dp):
            n += sum(1 for f in fs if B.parse_name(f) is not None)
        if n:
            found['cycle2/' + d] = n
    return found


def m1_list(pins, fam, tag, cache):
    """(E, binding dict). Parent-bound for the 74 R6 cases; otherwise the lane list, flagged unverified."""
    if (fam, tag) in cache:
        return cache[(fam, tag)]
    rel = 'cycle2/%s/%s/ext.json' % (fam, tag)
    info, b = B.file_info(B.L / rel, keep=True)
    c = pins['cases'].get(tag)
    bind = {'path': rel, 'sha256': info.get('sha256'), 'size': info.get('size'), 'mtime': info.get('mtime')}
    E = None
    if b is not None:
        try:
            E = json.loads(b)
            bind['n'] = len(E['full'])
            bind['raw'] = E.get('raw')
            bind['fields_ok'] = E.get('source') == tag + '.json' and E.get('num_full') == bind['n']
        except (ValueError, KeyError, TypeError) as ex:
            bind['parse_error'] = repr(ex)
            E = None
    if c is not None and c['m1_ext']['path'] == rel:
        bind['reference'] = 'R6 m1_regen %s' % c['m1_ext']['R6_m1_regen']
        bind['parent_verified'] = E is not None and info.get('sha256') == c['m1_ext']['R6_m1_regen'] and bind['fields_ok']
    else:
        bind['reference'] = None
        bind['parent_verified'] = False
    cache[(fam, tag)] = (E, bind)
    return E, bind


def m2_list(pins, d, cache, r6n):
    if ('m2', d) in cache:
        return cache[('m2', d)]
    tag = next((t for t, c in pins['cases'].items() if c['m2_dir'] == d), None)
    rel = 'cycle2/m2part_drat/%s/ext.json' % d
    info, b = B.file_info(B.L / rel, keep=True)
    bind = {'path': rel, 'sha256': info.get('sha256'), 'bound_m1_tag': tag}
    E = None
    if b is not None:
        try:
            E = json.loads(b)
            bind['n'] = len(E['placements'])
        except (ValueError, KeyError, TypeError) as ex:
            bind['parse_error'] = repr(ex)
            E = None
    if tag is None:
        bind['parent_verified'] = False
        bind['reference'] = None
    else:
        c = pins['cases'][tag]
        ref = c['m2_ext']['R6_m2_regen_normalized_production_source']
        bind['reference'] = 'R6 m2_regen_normalized_production_source %s' % ref
        mi = c['multiset']
        bind['R6_count'] = r6n.get(tag)
        bind['fields_ok'] = bool(E is not None and E.get('index') == c['b_index']
                                 and E.get('num_placements') == bind.get('n') == r6n.get(tag))
        bind['source_ok'] = E is not None and E.get('source') == str(B.L / 'cycle2' / 'skel-b' / ('skeletons-b-ms%02d.json' % mi))
        bind['parent_verified'] = bool(E is not None and info.get('sha256') == ref and bind['fields_ok'] and bind['source_ok'])
    cache[('m2', d)] = (E, bind)
    return E, bind


def spec_for(pins, r0, tag, cache):
    if ('spec', tag) in cache:
        return cache[('spec', tag)]
    rel = 'cases19skel/specs/%s.json' % tag
    li, lb = B.file_info(B.L / rel, keep=True)
    si, sb = B.file_info(B.S / rel, keep=True)
    bound = li.get('sha256') is not None and li.get('sha256') == si.get('sha256') == r0.get(rel)
    spec = json.loads(sb) if bound else None
    m = B.M1TAG.match(tag)
    ident = bool(spec) and bool(m) and spec.get('multiset_index') == int(m.group(1)) and spec.get('skel_index') == int(m.group(2))
    val = (spec, {'path': rel, 'sha256': si.get('sha256'), 'R0_pin': r0.get(rel), 'bound': bound, 'identity_ok': ident})
    cache[('spec', tag)] = val
    return val


def regen(mods, sers, fam, kind, enc, rev, spec, E, skb, b_index, idxs):
    if fam in ('a3', 'part'):
        ser = sers.get(rev)
        if ser is None:
            raise KeyError('serializer for stream_check_revision %r' % (rev,))
        if kind == 'single':
            m = {'encode_full.py': mods['encode_full'], 'encode_full2.py': mods['encode_full2'],
                 'encode_partq.py': mods['encode_partq']}[enc]
            sub = dict(spec)
            sub['placed'] = E['full'][idxs[0]]
            before = B.jdigest([spec, sub['placed']])
            F, X, info = m.build(sub)
            b = ser.cnf_bytes_of(F)
            return b, info, before == B.jdigest([spec, sub['placed']]), '%s.build + %s.cnf_bytes_of' % (enc[:-3], ser.__name__)
        if enc != 'encode_partbatch.py':
            raise KeyError(enc)
        pls = [E['full'][i] for i in idxs]
        before = B.jdigest([spec, pls])
        F, X, sel = mods['encode_partbatch'].build(spec, pls)
        b = ser.cnf_bytes_of(F)
        return b, None, before == B.jdigest([spec, pls]), 'encode_partbatch.build + %s.cnf_bytes_of' % ser.__name__
    return B.build(mods, fam, kind, enc, rev, spec, E, skb, b_index, idxs)


def cmd_late():
    B.require_flags()
    t0 = time.time()
    res, res_sha = main_receipt()
    pins, pins_sha, pop = B.load_pins_pop()
    r0 = json.loads(B.R0.read_bytes())['files']
    byp = {e['path']: e for e in pop}
    INC.mkdir(exist_ok=True)
    k = 1
    while (INC / ('inc-%03d' % k)).exists():
        k += 1
    rd = INC / ('inc-%03d' % k)
    rd.mkdir(exist_ok=False)
    B.readme('late %s start' % rd.name)
    for n, e in pins['replay_sources'].items():
        if B.sha((B.PINNED / n).read_bytes()) != e['sha256']:
            raise SystemExit('pinned source changed: %s' % n)
    mods = B.load_modules()
    ref_seg = ast.get_source_segment((B.PINNED / 'stream_check4.py').read_text(), next(
        n for n in ast.parse((B.PINNED / 'stream_check4.py').read_text()).body
        if isinstance(n, ast.FunctionDef) and n.name == 'cnf_bytes_of'))
    sers = {4: mods['stream_check4'], 5: mods['stream_check5']}
    sc_info = {}
    listing_started = B.now()
    now_recs = list_split_records()
    listing_ended = B.now()
    late_paths = [p for p in now_recs if p not in byp]
    if late_paths:
        revs = set()
        for p in late_paths:
            _, rec, err = B.read_record(B.L / p)
            if rec is not None:
                revs.add(rec.get('stream_check_revision'))
        for rev, name in ((9, 'stream_check9.py'), (8, 'stream_check8.py')):
            if rev in revs:
                mod, info = sc_module(name, rd, ref_seg)
                sc_info[name] = info
                if mod is not None:
                    sers[rev] = mod
    changed, removed = [], []
    for p, e in byp.items():
        if p not in now_recs:
            removed.append(p)
            continue
        try:
            h = B.sha((B.L / p).read_bytes())
        except FileNotFoundError:
            removed.append(p)
            continue
        if h != e['sha256']:
            changed.append({'path': p, 'snapshot_sha256': e['sha256'], 'now_sha256': h})
    cache = {}
    inp = B.Inputs(pins)
    r6n = {c['tag']: c['counts']['m2_num'] for c in json.loads(B.R6.read_bytes())['cases']}
    lists = OrderedDict()
    out_lines = []
    counts = Counter()
    for p in late_paths:
        fam, d, fn = now_recs[p]
        r = OrderedDict([('path', p), ('family', fam), ('dir', d)])
        data, rec, err = B.read_record(B.L / p)
        if err:
            r['status'] = 'PENDING'
            r['reason'] = 'record %s at read' % err
            out_lines.append(json.dumps(r, separators=(',', ':')))
            counts[r['status']] += 1
            continue
        st = (B.L / p).stat()
        r['record_sha256'] = B.sha(data)
        r['mtime'] = time.strftime('%Y-%m-%dT%H:%M:%S%z', time.localtime(st.st_mtime))
        r['declared'] = {'encoder': rec.get('encoder'), 'runner': rec.get('runner'),
                         'stream_check_revision': rec.get('stream_check_revision')}
        r['checker_class'] = B.checker_class(rec)
        r['worker_claim'] = B.worker_claim(rec)
        r['recorded'] = {'cnf_sha256': rec.get('cnf_sha256'), 'cnf_bytes': rec.get('cnf_bytes')}
        skb, b_index, tag = None, None, None
        if fam == 'm2part_drat':
            E, lb = m2_list(pins, d, cache, r6n)
            tag = lb.get('bound_m1_tag')
            if tag is not None:
                b_index = pins['cases'][tag]['b_index']
                kh, skb = inp.skelb(pins['cases'][tag]['multiset'])
                lb['skel_b_sha256'] = kh
        else:
            tag = d
            E, lb = m1_list(pins, fam, d, cache)
        lists[lb['path']] = lb
        r['case'] = tag
        r['list'] = {'path': lb['path'], 'sha256': lb.get('sha256'), 'parent_verified': lb['parent_verified']}
        n = None if E is None else len(E['placements'] if fam == 'm2part_drat' else E['full'])
        checks, kind, suf, idxs = B.structural(fam, d, fn, rec, n)
        spec, sinfo = spec_for(pins, r0, tag, cache) if tag else (None, {'bound': False, 'identity_ok': False})
        checks['spec_bytes_bound_S_L_R0'] = sinfo['bound']
        checks['case_identity_spec'] = sinfo['identity_ok']
        if fam == 'm2part_drat':
            checks['m2_dir_bound_to_R6_case'] = tag is not None
            checks['skel_b_bytes_bound'] = skb is not None if tag is not None else False
        r['kind'], r['suffix'] = kind, suf
        if (idxs is None or E is None or spec is None or checks.get('indices_within_pinned_list') is not True
                or not checks['declared_encoder_expected'] or any(v is False for v in checks.values())):
            r['checks'] = checks
            r['mismatches'] = [k for k, v in checks.items() if v is False]
            r['status'] = 'FAIL' if r['mismatches'] else 'PENDING'
            r['reason'] = 'inputs or indices not bound; formula not regenerated'
            out_lines.append(json.dumps(r, separators=(',', ':')))
            counts[r['status']] += 1
            continue
        t = time.perf_counter()
        try:
            b, info, unmut, call = regen(mods, sers, fam, kind, rec.get('encoder'), rec.get('stream_check_revision'),
                                         spec, E, skb, b_index, idxs)
        except KeyError as ex:
            r['checks'] = checks
            r['status'] = 'PENDING'
            r['reason'] = 'declared encoder/serializer not supported: %r' % (ex,)
            out_lines.append(json.dumps(r, separators=(',', ':')))
            counts[r['status']] += 1
            continue
        r['build_s'] = round(time.perf_counter() - t, 3)
        nv, nc = B.header(b)
        r['generated'] = {'cnf_sha256': B.sha(b), 'cnf_bytes': len(b), 'vars': nv, 'clauses': nc, 'call': call}
        del b
        checks['inputs_not_mutated_by_encoder'] = unmut
        checks['cnf_sha256_equal'] = r['generated']['cnf_sha256'] == rec.get('cnf_sha256')
        checks['cnf_bytes_equal'] = r['generated']['cnf_bytes'] == rec.get('cnf_bytes')
        if info is not None and 'leave' in rec:
            checks['leave_vector_equal'] = info.get('leave') == rec.get('leave')
        r['checks'] = checks
        r['mismatches'] = [k for k, v in checks.items() if v is False]
        if r['mismatches']:
            r['status'] = 'FAIL'
        elif lb['parent_verified']:
            r['status'] = 'PASS'
        else:
            r['status'] = 'FORMULA_EQUAL_LIST_UNVERIFIED'
            r['reason'] = ('formula equals the declared encoder applied to the bound spec and the lane placement list; '
                           'that list has no parent replay yet (counts as PENDING)')
        out_lines.append(json.dumps(r, separators=(',', ':')))
        counts[r['status']] += 1
        if B.usage()['maxrss_bytes'] > B.RSS_STOP or B.free_bytes() < B.FREE_FLOOR + 200_000_000:
            counts['STOPPED_EARLY'] += 1
            break
    lb_ = ('\n'.join(out_lines) + '\n').encode() if out_lines else b''
    B.write_new(rd / 'late-census.jsonl', lb_)
    os.chmod(rd / 'late-census.jsonl', 0o444)
    recs = [json.loads(x) for x in out_lines]
    new_m2 = []
    for tag, c in pins['cases'].items():
        if not c['m2_ext']['L']['exists']:
            info = B.file_info(B.L / c['m2_ext']['path'])
            if info['exists']:
                new_m2.append({'tag': tag, 'path': c['m2_ext']['path'], 'sha256': info['sha256'],
                               'R6_prediction': c['m2_ext']['R6_m2_regen_normalized_production_source'],
                               'equals_R6_prediction': info['sha256'] == c['m2_ext']['R6_m2_regen_normalized_production_source']})
    m2_absent = [{'tag': t, 'm2_dir': c['m2_dir'], 'R6_predicted_ext_sha256': c['m2_ext']['R6_m2_regen_normalized_production_source'],
                  'R6_count': c['m2_ext'].get('n')}
                 for t, c in pins['cases'].items() if not B.file_info(B.L / c['m2_ext']['path'])['exists']]
    unverified = [v for v in lists.values() if not v['parent_verified']]
    by_dir = Counter((x['family'], x['dir'], x['status']) for x in recs)
    nxt = []
    for v in unverified:
        if v['path'].startswith('cycle2/m2part_drat/'):
            nxt.append('M2 list %s (sha %s) is not bound: compare with the R6 prediction (pins.json) or replay extend_b '
                       'for its b-index before its batches can PASS.' % (v['path'], v.get('sha256')))
        else:
            nxt.append('R6-style replay of extend_p1q.py m=1 (snapshot copy sha %s, venv python, networkx 3.7) for %s; '
                       'the result must equal %s (sha %s, n=%s, raw=%s). R6 peaked at 1.42e9 bytes RSS for n=27082 '
                       '(ms09_s00061); [INFERENCE] n=%s may need more, so check RSS headroom against the 3 GiB cap first. '
                       'Then rerun "incremental_bind.py late" to promote its FORMULA_EQUAL_LIST_UNVERIFIED records.' % (
                           pins['sources']['extend_p1q.py']['L']['sha256'], v['path'].split('/')[2], v['path'],
                           v.get('sha256'), v.get('n'), v.get('raw'), v.get('n')))
    if m2_absent:
        nxt.append('%d M2 placement lists were still absent at this census; each new cycle2/m2part_drat/<dir>/ext.json '
                   'must equal its R6-predicted SHA-256 (listed in m2_lists_absent) before its batches bind.' % len(m2_absent))
    nxt.append('Records keep arriving (run_hard9 on ms06 A3\'\' batches, M2 partbatch runners): run '
               '"nice -n 10 python3.14 -B -I incremental_bind.py late" again (new inc-NNN directory); every counted split '
               'record should reach PASS here or in a later parent census.')
    nxt.append('No status here is an UNSAT acceptance; a parent drat-trim check per record route is still required, and '
               'retired lrat-check-only (_r2) or lane-written checker records never count.')
    out = OrderedDict()
    out['title'] = 'PA(19,8,6) R8 incremental binding census %s' % rd.name
    out['scope'] = ('Split records under cycle2/{a3,part,m2part_drat} that were absent from the R8 snapshot '
                    '(population.jsonl, %s .. %s), census: structural checks and in-memory formula regeneration with the '
                    'declared encoder and serializer from pinned sources; snapshot records re-hashed for changes. '
                    'Formula binding only.' % (pins['population']['snapshot_started'], pins['population']['snapshot_ended']))
    out['not_claimed'] = res['not_claimed']
    out['status_rules'] = {
        'PASS': 'structural checks true, spec bytes equal S/L/R0 pins, placement list parent-verified (R6 regenerated '
                'M1 list or R6-predicted M2 list), formula sha256 and bytes equal the record',
        'FORMULA_EQUAL_LIST_UNVERIFIED': 'as PASS but the placement list is the lane list without a parent replay '
                                         '(counts as PENDING)',
        'FAIL': 'any check false', 'PENDING': 'unreadable record, unsupported encoder/serializer or unbound inputs'}
    out['main_receipt'] = {'path': MAIN_RESULT.name, 'sha256': res_sha, 'verdict': res['verdict']}
    out['code'] = {'bind_subcases.py': B.driver_sha(), 'incremental_bind.py': script_sha(),
                   'later_serializers': sc_info}
    out['listing'] = {'started': listing_started, 'ended': listing_ended, 'records_now': len(now_recs),
                      'snapshot_records': len(byp), 'late': len(late_paths), 'changed': changed, 'removed': removed,
                      'other_trees_with_record_names': other_trees()}
    out['counts'] = dict(counts)
    out['counts']['late_not_evaluated'] = len(late_paths) - len(recs)
    out['by_dir_status'] = ['%s/%s %s: %d' % (f, d, s, v) for (f, d, s), v in sorted(by_dir.items())]
    out['lists_used'] = list(lists.values())
    out['new_m2_ext_lists'] = new_m2
    out['m2_lists_absent'] = m2_absent
    out['late_census'] = {'path': 'late-census.jsonl', 'sha256': B.sha(lb_), 'records': len(recs)}
    out['mismatches'] = [{'path': x['path'], 'mismatches': x.get('mismatches'), 'recorded': x.get('recorded'),
                          'generated': x.get('generated')} for x in recs if x['status'] == 'FAIL']
    out['next_actions'] = nxt
    out['resources'] = {**B.usage(), 'elapsed_s': round(time.time() - t0, 2), 'free_bytes': B.free_bytes(),
                        'maxrss_unit': 'bytes'}
    out['proc'] = proc()
    out['finished'] = B.now()
    B.dump_new(rd / 'inc-result.json', out)
    os.chmod(rd / 'inc-result.json', 0o444)
    B.readme('late %s: listing %s..%s, late %d (%s), changed %d, removed %d; inc-result.json sha %s' % (
        rd.name, listing_started, listing_ended, len(late_paths), dict(counts), len(changed), len(removed),
        B.sha((rd / 'inc-result.json').read_bytes())))
    print(json.dumps({k: out[k] for k in ('listing', 'counts', 'by_dir_status', 'new_m2_ext_lists', 'mismatches',
                                          'next_actions', 'resources')}, indent=1)[:6000])


def main():
    os.chdir(HERE)
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'pin-records':
        cmd_pin_records()
    elif cmd == 'late':
        cmd_late()
    else:
        raise SystemExit(__doc__)


if __name__ == '__main__':
    main()
