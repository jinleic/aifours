#!/usr/bin/env python3
"""PRIMARY-route comparison for the parent replay of C5' (route 1: proved filter (d) + ordered DP on every survivor).

Same checks as compare_v3.py for route 1 (exact strata H = 0..7, per-H counts against independently derived Python
totals incl. 1,021,369,625,000 labelled representations and 613,973,068,750 classes, avoider set vs the worker's
dp_avoiders.txt, rigidity, naive confirmation of every avoiding representation, controls, negative controls), but the
optional no-filter brute force (route 2) is only REPORTED (per run: completed with exit=0 / stopped UNKNOWN / not yet
finished) and is not required.  Writes DESK/out/compare-primary-v1/{compare.json, my_avoiders_worker_format.txt}.
Usage: python3 -B compare_primary_v1.py DESK WORKER_AVOIDERS WORKER_AVOIDERS_SHA256
"""
import collections
import hashlib
import json
import os
import re
import sys

P = 5
TASK_TOTAL_H04 = 1021369625000
TASK_CLASSES_H04 = 613973068750
BRUTE_RUNS = (['brute-H0-s%dof6-v2' % s for s in range(6)] + ['brute-H1-s%dof4-v2' % s for s in range(4)]
              + ['brute-H2-s0of2-v2r2', 'brute-H2-s1of2-v2r2', 'brute-H3-s0of1-v2r2']
              + ['brute-H%d-s0of1-v2' % h for h in (4, 5, 6, 7)])
STOPPED_RUNS = ['brute-H2-s1of2-v2', 'brute-H2-s0of2-v2']


def sha(path):
    with open(path, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def lines(path):
    with open(path) as fh:
        return [ln.rstrip('\n') for ln in fh if ln.strip()]


def load(path):
    with open(path) as fh:
        return json.load(fh)


def parse_mine(ln):
    f = dict(kv.split('=', 1) for kv in ln.split('|'))
    runs = [[] if r == '-' else [int(ch) for ch in r] for r in f['runs'].split('/')]
    k, n = (int(t) for t in f['lavoid'].split('/'))
    return int(f['H']), runs, f['y'], k, n


def to_worker(H, runs, y):
    dist = '/'.join(','.join(str(r.count(x)) for x in range(P)) for r in runs)
    return 'H=%d|dist=%s|y=%s' % (H, dist, y)


def worker_values(ln):
    f = dict(kv.split('=', 1) for kv in ln.split('|'))
    counts = [[int(t) for t in r.split(',')] for r in f['dist'].split('/')]
    return int(f['H']), [sum(r[x] for r in counts) for x in range(P)]


def rigid(m):
    vals = {x for x in range(P) if m[x]}
    return any(vals <= {c, (-c) % P} for c in range(1, P))


def hkey(s):
    return int(re.match(r'H=(\d+)\|', s).group(1))


def log_exit(path):
    if not os.path.exists(path):
        return None
    ex = re.findall(r'^exit=(\d+)$', open(path).read(), re.M)
    return int(ex[-1]) if ex else None


def main():
    desk, wpath, wsha = sys.argv[1], sys.argv[2], sys.argv[3]
    out = os.path.join(desk, 'out')
    cdir = os.path.join(out, 'compare-primary-v1')
    os.mkdir(cdir)
    res, fails = {'script': 'compare_primary_v1.py'}, []

    en = os.path.join(out, 'enum-clean-v2')
    summ = load(os.path.join(en, 'summary.json'))
    ind = load(os.path.join(out, 'indep-check-v1', 'indep_check.json'))
    raw_mine = lines(os.path.join(en, 'avoider_classes.txt'))
    mine = [parse_mine(ln) for ln in raw_mine]
    mixed = lines(os.path.join(en, 'mixed_classes.txt'))
    nonrig = lines(os.path.join(en, 'nonrigid_avoider_classes.txt'))
    res['enum_clean_v2_log_exit'] = log_exit(os.path.join(out, 'enum-clean-v2.log'))
    if not summ['all_checks_ok'] or res['enum_clean_v2_log_exit'] != 0:
        fails.append('enum-clean-v2 checks/exit')
    if mixed or nonrig:
        fails.append('mixed or nonrigid classes present')
    if any(k != n for (_, _, _, k, n) in mine):
        fails.append('avoider line with partial l-avoidance')
    v1same = {f: sha(os.path.join(out, 'enum-clean-v1', f)) == sha(os.path.join(en, f))
              for f in ('avoider_classes.txt', 'mixed_classes.txt', 'nonrigid_avoider_classes.txt', 'survivor_multisets.txt')}
    res['enum_v1_v2_outputs_identical'] = v1same
    if not all(v1same.values()):
        fails.append('v1/v2 enum outputs differ')

    strata = [h['H'] for h in summ['per_H']]
    pyH = {d['H']: d for d in ind['per_H']}
    strata_ok = strata == list(range(8)) and sorted(pyH) == list(range(8))
    rows = []
    for h in summ['per_H']:
        d = pyH.get(h['H'], {})
        r = dict(H=h['H'], checks_ok=h['checks_ok'],
                 multisets_eq=h['multisets_enumerated'] == d.get('multisets') == d.get('multisets_formula'),
                 survivors_eq=h['multisets_survivors'] == d.get('survivors') and
                 h['multisets_survivors_rigid'] == d.get('survivors_rigid'),
                 dists_eq=h['dists_enumerated'] == h['sum_over_M_prod_C(m_x+3,3)'] == d.get('dists') == d.get('sum_over_M_prod'),
                 survivor_dists_eq=h['dists_survivors'] == d.get('survivor_dists'),
                 words_eq=h['words_filter_solved_counted'] + h['words_dp_enumerated'] == h['words_formula'] == d.get('words'),
                 dp_words_eq=h['words_dp_enumerated'] == d.get('survivor_words'),
                 seq_run_reps_eq=h['literal_words'] == d.get('literal_words'))
        r['ok'] = all(v for k, v in r.items() if k != 'H')
        rows.append(r)
    sumH04 = sum(h['words_formula'] for h in summ['per_H'] if h['H'] <= 4)
    clsH04 = sum(h['dists_enumerated'] * 625 for h in summ['per_H'] if h['H'] <= 4)
    res['strata'] = dict(enum_strata=strata, strata_exact_0_7=strata_ok, per_H=rows,
                         representations_H0_4_enumerated=sumH04,
                         representations_H0_4_python=ind['totals']['words_H0_4'],
                         representations_H0_4_task=TASK_TOTAL_H04,
                         classes_H0_4_enumerated=clsH04, classes_H0_4_task=TASK_CLASSES_H04)
    if not (strata_ok and all(r['ok'] for r in rows) and sumH04 == ind['totals']['words_H0_4'] == TASK_TOTAL_H04
            and clsH04 == TASK_CLASSES_H04):
        fails.append('strata / per-H counts')

    mapped = [to_worker(H, runs, y) for (H, runs, y, _, _) in mine]
    with open(os.path.join(cdir, 'my_avoiders_worker_format.txt'), 'x') as fh:
        fh.write(''.join(m + '\n' for m in mapped))
    w_actual_sha = sha(wpath)
    wl = lines(wpath)
    ms, ws = set(mapped), set(wl)
    perH = lambda L: {str(k): v for k, v in sorted(collections.Counter(hkey(s) for s in L).items())}
    res['worker_file'] = dict(path=wpath, sha256=w_actual_sha, sha256_expected=wsha, sha_ok=w_actual_sha == wsha,
                              lines=len(wl), distinct=len(ws), per_H=perH(wl))
    res['parent'] = dict(lines=len(mapped), distinct=len(ms), per_H=perH(mapped),
                         mapped_file_sha256=sha(os.path.join(cdir, 'my_avoiders_worker_format.txt')))
    res['set_equal'] = ms == ws
    res['per_H_equal'] = perH(mapped) == perH(wl)
    res['only_parent'] = sorted(ms - ws)[:20]
    res['only_worker'] = sorted(ws - ms)[:20]
    res['same_order_as_worker_file'] = mapped == wl
    res['worker_file_is_sorted'] = wl == sorted(wl)
    res['byte_identical_to_worker_file'] = res['parent']['mapped_file_sha256'] == w_actual_sha
    if not (res['worker_file']['sha_ok'] and res['set_equal'] and res['per_H_equal'] and len(ms) == len(mapped)
            and len(ws) == len(wl) and len(wl) > 0):
        fails.append('avoider set comparison failed')

    census = collections.Counter()
    nr_parent = 0
    for (H, runs, y, _, _) in mine:
        m = tuple(sum(r.count(x) for r in runs) for x in range(P))
        census[(H, m)] += 1
        nr_parent += not rigid(m)
    nr_worker = sum(not rigid(worker_values(ln)[1]) for ln in wl)
    res['nonrigid_avoider_classes'] = dict(parent=nr_parent, worker=nr_worker)
    res['avoider_multiset_census'] = ['H=%d M=%s classes=%d' % (H, ','.join(map(str, m)), c)
                                      for (H, m), c in sorted(census.items())]
    if nr_parent or nr_worker:
        fails.append('nonrigid avoider')

    drop = set(mapped[1:])
    alt = mapped[0][:-1] + str((int(mapped[0][-1]) + 1) % P)
    res['comparator_mutation_tests'] = dict(drop_one_detected=drop != ws, alter_one_y_detected=(drop | {alt}) != ws,
                                            empty_list_detected=set() != ws,
                                            nonrigid_injection_detected=not rigid((1, 0, 0, 0, 0)) and not rigid((0, 1, 1, 0, 0)))
    if not all(res['comparator_mutation_tests'].values()):
        fails.append('comparator self-test')

    ck = lines(os.path.join(out, 'check-all-avoiders-v2', 'check.txt'))
    words = [ln for ln in ck if not ln.startswith('#')]
    both_avoid = sum(1 for ln in words if ln.endswith('|dp=AVOID|naive=AVOID'))
    res['naive_check_all_avoider_words'] = dict(word_lines=len(words), dp_and_naive_avoid=both_avoid,
                                                expected=summ['totals']['avoider_words'],
                                                log_exit=log_exit(os.path.join(out, 'check-all-avoiders-v2.log')))
    if not (len(words) == both_avoid == summ['totals']['avoider_words'] > 0) or res['naive_check_all_avoider_words']['log_exit'] != 0:
        fails.append('naive check of avoider words')

    neg = {}
    for bug in ('untwisted', 'target8', 'parity'):
        s = load(os.path.join(out, 'enum-bug-%s-v2' % bug, 'summary.json'))
        av = lines(os.path.join(out, 'enum-bug-%s-v2' % bug, 'avoider_classes.txt'))
        neg[bug] = dict(avoider_classes=s['totals']['avoider_classes_all_l'], avoider_words=s['totals']['avoider_words'],
                        dp_words=s['totals']['words_dp_enumerated'], outcome_changed=set(av) != set(raw_mine),
                        log_exit=log_exit(os.path.join(out, 'enum-bug-%s-v2.log' % bug)))
    res['negative_controls_enum'] = neg
    if not all(v['outcome_changed'] and v['log_exit'] == 0 for v in neg.values()):
        fails.append('a negative control did not fire')

    ctl = load(os.path.join(out, 'controls-v2', 'controls.json'))
    res['controls_v2_failures'] = ctl['failures']
    res['indep_check_all_ok'] = ind['all_ok']
    if ctl['failures'] or not ind['all_ok']:
        fails.append('controls or independent check')

    # ---- OPTIONAL route 2 (no-filter brute force): status only, not required here
    status = []
    for name in BRUTE_RUNS + STOPPED_RUNS:
        sp = os.path.join(out, name, 'summary.json')
        ex = log_exit(os.path.join(out, name + '.log'))
        s = None
        if os.path.exists(sp) and os.path.getsize(sp) > 0:
            s = load(sp)
        st = ('COMPLETED' if (ex == 0 and s and s.get('checks_ok')) else
              'STOPPED_UNKNOWN' if name in STOPPED_RUNS else 'NOT_FINISHED_OR_FAILED')
        status.append(dict(run=name, status=st, log_exit=ex,
                           H=s['H'] if s else None, words=s['words_dp_enumerated'] if s else None,
                           words_avoid=s['words_avoid'] if s else None,
                           filter_violations=s['filter_violations'] if s else None))
    res['route2_brute_status'] = status
    res['route2_completed_strata'] = sorted({r['H'] for r in status if r['status'] == 'COMPLETED' and r['H'] is not None
                                             and all(q['status'] == 'COMPLETED' for q in status
                                                     if q['run'].startswith('brute-H%d-' % r['H'])
                                                     and q['run'] not in STOPPED_RUNS)})
    res['fails'] = fails
    res['all_ok'] = not fails
    with open(os.path.join(cdir, 'compare.json'), 'x') as fh:
        json.dump(res, fh, indent=1)
        fh.write('\n')
    print('primary compare all_ok=%s fails=%s set_equal=%s byte_identical=%s route2_completed_strata=%s' % (
        res['all_ok'], fails, res['set_equal'], res['byte_identical_to_worker_file'], res['route2_completed_strata']))
    return 0 if res['all_ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
