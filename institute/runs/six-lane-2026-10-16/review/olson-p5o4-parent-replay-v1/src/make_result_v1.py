#!/usr/bin/env python3
"""Assemble RESULT-v1.json for the parent replay of C5' (verdict, counts, controls, comparison, run resources, and
SHA-256 of every source, binary, log and output file in the desk; NOTE-v1.md is hashed, RESULT itself is not).
Usage: python3 -B make_result_v1.py DESK
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
    cmp_ = load(os.path.join(out, 'compare-v1', 'compare.json'))
    ctl = load(os.path.join(out, 'controls-v2', 'controls.json'))
    ind = load(os.path.join(out, 'indep-check-v1', 'indep_check.json'))
    runs = [run_record(p) for p in sorted(glob.glob(os.path.join(out, '*.log')))]
    per_H = [{k: h[k] for k in ('H', 'R', 'ltuples_enumerated', 'multisets_enumerated', 'multisets_filter_solved',
                                'multisets_survivors', 'multisets_survivors_rigid', 'dists_enumerated',
                                'dists_formula_C(R+19,19)', 'dists_filter_solved', 'dists_survivors', 'words_formula',
                                'words_filter_solved_counted', 'words_dp_enumerated', 'words_dp_avoid',
                                'classes_all_l_avoid', 'classes_mixed', 'nonrigid_avoider_words',
                                'literal_words', 'checks_ok')} for h in enum['per_H']]
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
        worker_artifacts=worker,
        method=dict(
            facts_proved_in_NOTE=['(a) run multisets', '(b) sigma_y^j = sigma_y^(j mod 2)', '(c) H >= 5 solved',
                                  '(d) j <= H pairs + zero-sum rotation sub-multiset of size 10-2j solved'],
            route_1_enum='every (H, M) decided by (d); all C(R+19,19) run-multiset 4-tuples enumerated explicitly; every'
                         ' (l, y) completion of every (d)-surviving tuple decided by the ordered DP (prefix-shared and'
                         ' from-scratch, compared word by word); (d)-solved tuples counted with multiplicity C(H+3,3)*625',
            route_2_brute='every word of every layer H = 0..7 (runs as sorted multisets, fact (a) only) decided by the'
                          ' ordered DP, no (c)/(d); (d) checked to never skip an avoider',
            naive='all 43,758 index 10-subsets with the group law (C++ and an independent Python implementation)'),
        counts=dict(per_H=per_H, words_H0_4=t['words_formula_H0_4'], words_H0_7=t['words_formula_H0_7'],
                    task_closed_form_H0_4=1021369625000, closed_form_match=t['words_formula_H0_4'] == 1021369625000,
                    words_dp_route1=t['words_dp_enumerated'], words_counted_by_d_route1=t['words_filter_solved_counted'],
                    words_dp_route2_brute=cmp_['brute_totals']['words'],
                    literal_words_H0_4=ind['totals']['literal_words_H0_4'],
                    literal_words_H0_7=ind['totals']['literal_words_H0_7']),
        results=dict(avoider_classes=t['avoider_classes_all_l'], avoider_words=t['avoider_words'],
                     mixed_classes=t['mixed_classes'], nonrigid_avoider_words=nonrigid,
                     nonrigid_avoider_classes_recomputed=cmp_['nonrigid_avoider_classes'],
                     avoider_multiset_census=cmp_['avoider_multiset_census'],
                     brute_per_H=cmp_['brute_per_H'], brute_totals=cmp_['brute_totals']),
        comparison_with_worker=dict(set_equal=cmp_['set_equal'], parent=cmp_['parent'], worker=cmp_['worker_file'],
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
        runs=runs, all_runs_exit0=all_exit0,
        discrepancies=[] if confirmed else ['see compare.json fails: %s' % cmp_['fails']],
        files_sha256=files)
    path = os.path.join(desk, 'RESULT-v1.json')
    with open(path, 'x') as fh:
        json.dump(res, fh, indent=1)
        fh.write('\n')
    print('verdict=%s RESULT sha256=%s NOTE sha256=%s' % (verdict, sha(path), files.get('NOTE-v1.md', {}).get('sha256')))
    return 0


if __name__ == '__main__':
    sys.exit(main())
