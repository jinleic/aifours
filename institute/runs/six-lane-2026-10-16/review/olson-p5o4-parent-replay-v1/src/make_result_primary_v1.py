#!/usr/bin/env python3
"""Assemble RESULT-primary-v1.json for the PRIMARY route (route 1: proved filter (d) + ordered DP) of the parent replay
of C5'.  Pins NOTE-primary-v1.md and the SHA-256 of every desk file; the optional route 2 (no-filter brute force) is
reported with its exact status (completed strata / stopped UNKNOWN runs) and is not part of the verdict.
Usage: python3 -B make_result_primary_v1.py DESK
"""
import datetime
import glob
import hashlib
import json
import os
import re
import sys

WORKER = '/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/p5o4-v1'
PINS = {'PLAN-v1.md': '7d7793cbf137f2ddf01d7cc64872657ba26d15fbac0276101894972038e50588',
        'out/run1/verdict.json': 'ca156d58a1cbe6aa64418e732a205b499190ab290b1cafd0ee8a0c42266ddf0f',
        'out/run1/dp_avoiders.txt': '78a91ba247016568e5b23ba06d5b6221ca989211ddaf79f82229e7c5807d5967'}
ROUTE1_LOGS = ['controls-v2.log', 'enum-clean-v2.log', 'enum-bug-untwisted-v2.log', 'enum-bug-target8-v2.log',
               'enum-bug-parity-v2.log', 'check-all-avoiders-v2.log', 'indep-check-v1.log', 'compare-primary-v1.log']


def sha(path):
    with open(path, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def load(path):
    with open(path) as fh:
        return json.load(fh)


def run_record(log):
    txt = open(log).read()
    real = re.search(r'([\d.]+) real', txt)
    rss = re.search(r'(\d+)\s+maximum resident set size', txt)
    ex = re.findall(r'^exit=(\d+)$', txt, re.M)
    dates = [ln for ln in txt.splitlines() if re.match(r'^[A-Z][a-z]{2} [A-Z][a-z]{2} +\d+ \d\d:\d\d:\d\d [A-Z]+ \d{4}$', ln)]
    return dict(log=os.path.basename(log), start=dates[0] if dates else None, end=dates[-1] if len(dates) > 1 else None,
                wall_s=float(real.group(1)) if real else None, maxrss_bytes=int(rss.group(1)) if rss else None,
                exit=int(ex[-1]) if ex else None)


def main():
    desk = sys.argv[1]
    out = os.path.join(desk, 'out')
    now = datetime.datetime.now().astimezone().isoformat(timespec='seconds')
    worker = {k: dict(path=os.path.join(WORKER, k), sha256=sha(os.path.join(WORKER, k)), expected=v,
                      ok=sha(os.path.join(WORKER, k)) == v) for k, v in PINS.items()}
    enum = load(os.path.join(out, 'enum-clean-v2', 'summary.json'))
    cmp_ = load(os.path.join(out, 'compare-primary-v1', 'compare.json'))
    ctl = load(os.path.join(out, 'controls-v2', 'controls.json'))
    ind = load(os.path.join(out, 'indep-check-v1', 'indep_check.json'))
    route1_runs = [run_record(os.path.join(out, n)) for n in ROUTE1_LOGS]
    other_logs = sorted(p for p in glob.glob(os.path.join(out, '*.log')) if os.path.basename(p) not in ROUTE1_LOGS)
    other_runs = [run_record(p) for p in other_logs]
    per_H = []
    for h in enum['per_H']:
        per_H.append(dict(H=h['H'], R=h['R'], l_tuples=h['ltuples_enumerated'], y_tuples=h['ytuples'],
                          rotation_multisets=h['multisets_enumerated'], multisets_solved_by_d=h['multisets_filter_solved'],
                          multisets_surviving_d=h['multisets_survivors'],
                          multisets_surviving_d_rigid=h['multisets_survivors_rigid'],
                          run_multiset_4tuples_enumerated=h['dists_enumerated'],
                          run_multiset_4tuples_formula_C_R19_19=h['dists_formula_C(R+19,19)'],
                          run_multiset_4tuples_solved_by_d=h['dists_filter_solved'],
                          run_multiset_4tuples_surviving_d=h['dists_survivors'],
                          labelled_reps_formula=h['words_formula'],
                          labelled_reps_solved_by_d_counted=h['words_filter_solved_counted'],
                          labelled_reps_decided_by_dp=h['words_dp_enumerated'],
                          labelled_reps_avoiding=h['words_dp_avoid'],
                          classes_H_dist_y=h['dists_enumerated'] * h['ytuples'],
                          avoider_classes_all_l=h['classes_all_l_avoid'], mixed_classes=h['classes_mixed'],
                          nonrigid_avoiding_reps=h['nonrigid_avoider_words'],
                          sequence_run_labelled_reps=h['literal_words'], checks_ok=h['checks_ok']))
    t = enum['totals']
    route1_exit0 = all(r['exit'] == 0 for r in route1_runs)
    nonrigid = t['nonrigid_avoider_words']
    confirmed = (all(w['ok'] for w in worker.values()) and enum['all_checks_ok'] and nonrigid == 0
                 and t['mixed_classes'] == 0 and cmp_['all_ok'] and ctl['failures'] == 0 and ind['all_ok']
                 and route1_exit0)
    verdict = 'CONFIRMED' if confirmed else ('REFUTED' if nonrigid > 0 else 'UNKNOWN')
    files = {}
    for p in sorted(glob.glob(os.path.join(desk, '**', '*'), recursive=True)):
        rel = os.path.relpath(p, desk)
        if os.path.isfile(p) and rel != 'RESULT-primary-v1.json' and not rel.startswith('tmp' + os.sep):
            files[rel] = dict(sha256=sha(p), bytes=os.path.getsize(p))
    st = cmp_['route2_brute_status']
    res = dict(
        title="Parent replay of worker claim C5' (ordered Olson, D_10, p = 5, four odd blocks, length 18, target 10):"
              " PRIMARY route (proved filter (d) + ordered DP)",
        written_host_clock=now,
        verdict=verdict,
        note=dict(path='NOTE-primary-v1.md', sha256=files['NOTE-primary-v1.md']['sha256']),
        claim="Every word R1 S1 R2 S2 R3 S3 R4 S4 (length 18, S_i = sigma_{y_i}^{l_i}, l_i odd, rotation runs possibly empty,"
              " x = 0 allowed, adjacent y may be equal) with no identity 10-subword (index order, linear word) has all"
              " rotation letters in one {rho_c, rho_-c}, c != 0.",
        scope="C5' on the domain D only, as a finite exact statement conditional on the correctness of this parent code;"
              " the worker's reduction C5 -> C5' (PLAN-v1 Sec. 2, R1/R2 via PM*) is not re-audited here. No novelty claim.",
        terminology="labelled representation = (H; l-tuple; 4-tuple of run multisets; y-tuple); its linear word has runs"
                    " sorted by value. Distinct labelled representations can spell the same raw word (e.g. PC-k2 has 6),"
                    " so representation counts are not raw-word counts. class = (H; run-multiset 4-tuple; y-tuple).",
        worker_artifacts=worker,
        independence='own code from PLAN-v1 Sec. 1-3 definitions; no worker code read, imported, copied or run; the'
                     ' worker plan text (incl. its plan-time counts) was displayed in full by the read tool and the'
                     ' worker avoider list was used only for the final comparison',
        method=dict(
            facts_proved_in_NOTE=['(a) run multisets', '(b) sigma_y^j = sigma_y^(j mod 2)', '(c) H >= 5 solved',
                                  '(d) j <= H pairs + zero-sum rotation sub-multiset of size 10-2j solved'],
            route_1='every (H, M), H = 0..7, decided by (d); all C(R+19,19) run-multiset 4-tuples enumerated explicitly;'
                    ' every (l, y) completion of every (d)-surviving tuple decided by the ordered DP (prefix-shared and'
                    ' from-scratch, compared representation by representation); (d)-solved tuples counted with'
                    ' multiplicity C(H+3,3)*625; (d) is used only to skip, never to declare an avoider',
            naive='all 43,758 index 10-subsets with the group law (C++ and an independent Python implementation)'),
        counts=dict(per_H=per_H,
                    labelled_reps_H0_4=t['words_formula_H0_4'], labelled_reps_H0_7=t['words_formula_H0_7'],
                    task_closed_form_H0_4=1021369625000,
                    closed_form_match=t['words_formula_H0_4'] == 1021369625000,
                    classes_H0_4=cmp_['strata']['classes_H0_4_enumerated'], classes_H0_4_expected=613973068750,
                    strata_exact_0_7=cmp_['strata']['strata_exact_0_7'],
                    per_H_independent_python_match=[r['ok'] for r in cmp_['strata']['per_H']],
                    reps_decided_by_dp=t['words_dp_enumerated'], reps_counted_by_d=t['words_filter_solved_counted'],
                    sequence_run_reps_H0_4=ind['totals']['literal_words_H0_4'],
                    sequence_run_reps_H0_7=ind['totals']['literal_words_H0_7']),
        results=dict(avoider_classes=t['avoider_classes_all_l'], avoiding_labelled_reps=t['avoider_words'],
                     mixed_classes=t['mixed_classes'], nonrigid_avoiding_reps=nonrigid,
                     nonrigid_avoider_classes_recomputed=cmp_['nonrigid_avoider_classes'],
                     avoider_multiset_census=cmp_['avoider_multiset_census']),
        comparison_with_worker=dict(set_equal=cmp_['set_equal'], per_H_equal=cmp_['per_H_equal'],
                                    parent=cmp_['parent'], worker=cmp_['worker_file'],
                                    only_parent=cmp_['only_parent'], only_worker=cmp_['only_worker'],
                                    same_order=cmp_['same_order_as_worker_file'],
                                    byte_identical=cmp_['byte_identical_to_worker_file'],
                                    comparator_mutation_tests=cmp_['comparator_mutation_tests']),
        controls=dict(group_selftest=ctl['group_selftest'], pc_k2=ctl['pc_k2'], pc_k2_under_bugs=ctl['pc_k2_under_bugs'],
                      rigid_predicate_unit_failures=ctl['rigid_predicate_unit_failures'],
                      S1=ctl['S1_random_domain_words'], S2=ctl['S2_random_survivor_multiset_words'],
                      S3=ctl['S3_filter_solved_multisets'], python_naive=ind['naive'],
                      python_filter_d=ind['filter_d'],
                      naive_check_all_avoider_words=cmp_['naive_check_all_avoider_words'],
                      negative_controls_enum=cmp_['negative_controls_enum']),
        route2_optional_brute=dict(
            role='optional cross-check, not part of this verdict',
            completed_strata=cmp_['route2_completed_strata'],
            completed_reps=sum(r['words'] for r in st if r['status'] == 'COMPLETED'),
            completed_avoiding_reps=sum(r['words_avoid'] for r in st if r['status'] == 'COMPLETED'),
            completed_filter_violations=sum(r['filter_violations'] for r in st if r['status'] == 'COMPLETED'),
            not_covered='H = 2 and H = 3 (152,938,500,000 reps): v2 shards stopped by the external SIGTERM of 09:25:51'
                        ' (brute-H2-s1of2-v2) and by this desk at 09:28:03 (brute-H2-s0of2-v2, exit=143), both UNKNOWN;'
                        ' the rerun launcher run_brute_rerun_v3.sh failed to start (setsid EPERM), no v2r2 shard ran',
            runs=st),
        route1_runs=route1_runs, route1_runs_exit0=route1_exit0, other_runs=other_runs,
        superseded_or_unexecuted=['src/compare_v1.py', 'src/compare_v2.py', 'src/compare_v3.py', 'src/make_result_v1.py',
                                  'src/make_result_v2.py', 'src/make_result_v3.py', 'src/run_brute_rerun_v3.sh (failed to start)'],
        discrepancies=[] if confirmed else ['see compare-primary-v1/compare.json fails: %s' % cmp_['fails']],
        files_sha256=files)
    path = os.path.join(desk, 'RESULT-primary-v1.json')
    with open(path, 'x') as fh:
        json.dump(res, fh, indent=1)
        fh.write('\n')
    print('verdict=%s RESULT-primary sha256=%s NOTE-primary sha256=%s' % (verdict, sha(path), res['note']['sha256']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
