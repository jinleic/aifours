#!/usr/bin/env python3
"""Assemble RESULT-v1.json for the parent replay of C5' (verdict, counts, controls, comparison, run resources, and
SHA-256 of every source, binary, log and output file in the desk; NOTE-v1.md is hashed, RESULT itself is not).
v2 supersedes the never-executed draft make_result_v1.py (reads compare-v2; counting terminology: labelled
representations (l-tuple, run multisets, y), not distinct raw words).
Usage: python3 -B make_result_v2.py DESK
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
    ex = re.findall(r'^exit=(\d+)', txt, re.M)
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
    cmp_ = load(os.path.join(out, 'compare-v2', 'compare.json'))
    ctl = load(os.path.join(out, 'controls-v2', 'controls.json'))
    ind = load(os.path.join(out, 'indep-check-v1', 'indep_check.json'))
    runs = [run_record(p) for p in sorted(glob.glob(os.path.join(out, '*.log')))]
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
    all_exit0 = all(r['exit'] == 0 for r in runs)
    nonrigid = t['nonrigid_avoider_words']
    confirmed = (all(w['ok'] for w in worker.values()) and enum['all_checks_ok'] and nonrigid == 0
                 and t['mixed_classes'] == 0 and cmp_['all_ok'] and ctl['failures'] == 0 and ind['all_ok'] and all_exit0)
    verdict = 'CONFIRMED' if confirmed else ('REFUTED' if nonrigid > 0 else 'UNKNOWN')
    files = {}
    for p in sorted(glob.glob(os.path.join(desk, '**', '*'), recursive=True)):
        rel = os.path.relpath(p, desk)
        if os.path.isfile(p) and rel != 'RESULT-v1.json' and not rel.startswith('tmp' + os.sep):
            files[rel] = dict(sha256=sha(p), bytes=os.path.getsize(p))
    res = dict(
        title="Parent replay of worker claim C5' (ordered Olson, D_10, p = 5, four odd blocks, length 18, target 10)",
        written_host_clock=now,
        verdict=verdict,
        claim="Every word R1 S1 R2 S2 R3 S3 R4 S4 (length 18, S_i = sigma_{y_i}^{l_i}, l_i odd, rotation runs possibly empty,"
              " x = 0 allowed, adjacent y may be equal) with no identity 10-subword (index order, linear word) has all"
              " rotation letters in one {rho_c, rho_-c}, c != 0.",
        scope="C5' on the domain D only, as a finite exact statement conditional on the correctness of this parent code;"
              " the worker's reduction C5 -> C5' (PLAN-v1 Sec. 2, R1/R2 via PM*) is not re-audited here.",
        terminology="labelled representation = (H; l-tuple; 4-tuple of run multisets; y-tuple); its linear word has runs"
                    " sorted by value. Distinct labelled representations can spell the same raw word (e.g. PC-k2 has 6),"
                    " so representation counts are not raw-word counts. class = (H; run-multiset 4-tuple; y-tuple).",
        worker_artifacts=worker,
        method=dict(
            facts_proved_in_NOTE=['(a) run multisets', '(b) sigma_y^j = sigma_y^(j mod 2)', '(c) H >= 5 solved',
                                  '(d) j <= H pairs + zero-sum rotation sub-multiset of size 10-2j solved'],
            route_1_enum='every (H, M) decided by (d); all C(R+19,19) run-multiset 4-tuples enumerated explicitly; every'
                         ' (l, y) completion of every (d)-surviving tuple decided by the ordered DP (prefix-shared and'
                         ' from-scratch, compared representation by representation); (d)-solved tuples counted with'
                         ' multiplicity C(H+3,3)*625',
            route_2_brute='every labelled representation of every stratum H = 0..7 decided by the ordered DP (fact (a)'
                          ' only, no (c)/(d)); (d) checked never to skip an avoider',
            naive='all 43,758 index 10-subsets with the group law (C++ and an independent Python implementation)'),
        counts=dict(per_H=per_H,
                    labelled_reps_H0_4=t['words_formula_H0_4'], labelled_reps_H0_7=t['words_formula_H0_7'],
                    task_closed_form_H0_4=1021369625000,
                    closed_form_match=t['words_formula_H0_4'] == 1021369625000,
                    classes_H0_4=cmp_['strata']['classes_H0_4_enumerated'],
                    classes_H0_4_expected=613973068750,
                    strata_exact_0_7=cmp_['strata']['strata_exact_0_7'],
                    route1_reps_decided_by_dp=t['words_dp_enumerated'],
                    route1_reps_counted_by_d=t['words_filter_solved_counted'],
                    route2_reps_decided_by_dp=cmp_['brute_totals']['words'],
                    sequence_run_reps_H0_4=ind['totals']['literal_words_H0_4'],
                    sequence_run_reps_H0_7=ind['totals']['literal_words_H0_7']),
        results=dict(avoider_classes=t['avoider_classes_all_l'], avoiding_labelled_reps=t['avoider_words'],
                     mixed_classes=t['mixed_classes'], nonrigid_avoiding_reps=nonrigid,
                     nonrigid_avoider_classes_recomputed=cmp_['nonrigid_avoider_classes'],
                     avoider_multiset_census=cmp_['avoider_multiset_census'],
                     brute_per_H=cmp_['brute_per_H'], brute_totals=cmp_['brute_totals']),
        comparison_with_worker=dict(set_equal=cmp_['set_equal'], per_H_equal=cmp_['per_H_equal'],
                                    parent=cmp_['parent'], worker=cmp_['worker_file'],
                                    only_parent=cmp_['only_parent'], only_worker=cmp_['only_worker'],
                                    same_order=cmp_['same_order_as_worker_file'],
                                    byte_identical=cmp_['byte_identical_to_worker_file'],
                                    comparator_mutation_tests=cmp_['comparator_mutation_tests']),
        controls=dict(group_selftest=ctl['group_selftest'], pc_k2=ctl['pc_k2'], pc_k2_under_bugs=ctl['pc_k2_under_bugs'],
                      S1=ctl['S1_random_domain_words'], S2=ctl['S2_random_survivor_multiset_words'],
                      S3=ctl['S3_filter_solved_multisets'], python_naive=ind['naive'],
                      python_filter_d=ind['filter_d'],
                      naive_check_all_avoider_words=cmp_['naive_check_all_avoider_words'],
                      negative_controls_enum=cmp_['negative_controls_enum']),
        superseded_unexecuted_drafts=['src/compare_v1.py', 'src/make_result_v1.py'],
        runs=runs, all_runs_exit0=all_exit0,
        discrepancies=[] if confirmed else ['see compare-v2/compare.json fails: %s' % cmp_['fails']],
        files_sha256=files)
    path = os.path.join(desk, 'RESULT-v1.json')
    with open(path, 'x') as fh:
        json.dump(res, fh, indent=1)
        fh.write('\n')
    print('verdict=%s RESULT sha256=%s NOTE sha256=%s' % (verdict, sha(path), files.get('NOTE-v1.md', {}).get('sha256')))
    return 0


if __name__ == '__main__':
    sys.exit(main())
