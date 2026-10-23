#!/usr/bin/env python3
"""Assemble ADDENDUM-v1.json (parent-desk answers to MINORs m1-m7 of the Claude hostile review
olson-p5o4-complete-claim-claude-v1).  Pins ADDENDUM-v1.md and the evidence file, embeds the evidence, and hashes every
desk file that is not already pinned by RESULT-v1.json.  Changes no existing file; writes DESK/ADDENDUM-v1.json with
mode 'x'.
Usage: python3 -B make_addendum_v1.py DESK
"""
import datetime
import glob
import hashlib
import json
import os
import sys


def sha(path):
    with open(path, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main():
    desk = sys.argv[1]
    now = datetime.datetime.now().astimezone().isoformat(timespec='seconds')
    evp = os.path.join(desk, 'out', 'addendum-v1', 'evidence', 'evidence.json')
    with open(evp) as fh:
        ev = json.load(fh)
    with open(os.path.join(desk, 'RESULT-v1.json')) as fh:
        pinned = json.load(fh)['files_sha256']
    new_files = {}
    for p in sorted(glob.glob(os.path.join(desk, '**', '*'), recursive=True)):
        rel = os.path.relpath(p, desk)
        if (os.path.isfile(p) and rel != 'ADDENDUM-v1.json' and rel != 'RESULT-v1.json' and rel not in pinned
                and not rel.startswith('tmp' + os.sep)):
            new_files[rel] = dict(sha256=sha(p), bytes=os.path.getsize(p))
    pins = ev['m5_pins']['enum-clean-v2']['files']
    mo = ev['maximal_oF']
    with open(os.path.join(desk, mo['per_class_file'])) as fh:
        of_rows = [ln.rstrip('\n').rsplit('|', 2) for ln in fh if ln.strip()]
    oF4_iff_nonempty = len(of_rows) == 640 and all((o == 'oF=4') == (ne == 'all_runs_nonempty=1') for _, o, ne in of_rows)
    res = dict(
        title="ADDENDUM-v1 to the parent replay of C5' (D_10, p = 5, four odd blocks): parent-desk fixes for the hostile"
              " review olson-p5o4-complete-claim-claude-v1 (MINORs m1-m7)",
        written_host_clock=now,
        note=dict(path='ADDENDUM-v1.md', sha256=sha(os.path.join(desk, 'ADDENDUM-v1.md'))),
        evidence=dict(path='out/addendum-v1/evidence/evidence.json', sha256=sha(evp), all_ok=ev['all_ok'],
                      fails=ev['fails']),
        review=ev['deliverables']['review_note'],
        unchanged_deliverables={k: ev['deliverables'][k] for k in
                                ('RESULT-v1.json', 'NOTE-v1.md', 'RESULT-primary-v1.json', 'NOTE-primary-v1.md')},
        verdict='CONFIRMED (unchanged)',
        scope="C5' on the domain D only, as a finite exact statement conditional on the correctness of this parent code."
              " (m2) C5 = PLAN-v1 Sec. 2 (R1, R2) + PM* + this C5'; this desk did not audit the reduction; the hostile"
              " review Sec. A1 re-derived PM* in the PLAN-v1 L20 form. No novelty claim. No code was changed.",
        responses=dict(
            m1=dict(status='wording corrected (addendum only)',
                    text='Route 2 supports nothing in the verdict. The verdict rests on route 1 alone: facts (a)-(d)'
                         ' proved; the DP decides every (d)-survivor. Route 2 is the same binary, DP and group table'
                         ' without the filter and only re-confirms the proved fact (d). NOTE-primary-v1 Sec. 6 should'
                         ' read: "A partial, optional no-filter check (H = 0, 1, 4-7 complete; H = 2, 3 UNKNOWN) is in'
                         ' Sec. 7. It is not a premise; (d) is proved in Sec. 2." NOTE-v1\'s "Two routes give this result"'
                         ' is superseded by the same rule; the H = 2, 3 rerun (complete 10:00:51) is not cited.'),
            m2=dict(status='scope stated', text='see scope'),
            m3=dict(status='stated; optional classification done',
                    text='PC-k2 has maximal o_F = 2 and lies in D only through 6 non-maximal splittings of s0^7; A2'
                         ' (H=3, runs -/-/4/4^7, y=0020) also has maximal o_F = 2 (S4, S1, S2 merge). Maximal o_F = 4'
                         ' witnesses: A1 (H=1, runs 4/4/4/1^9, y=0000) and A3 (H=4, runs 4/4/4/444, y=0243), all runs'
                         ' non-empty.',
                    classification=dict(classes_by_oF=mo['classes_by_oF'], classes_by_H_oF=mo['classes_by_H_oF'],
                                        avoiding_reps_by_oF=mo['avoiding_reps_by_oF'], oF0_classes=mo['oF0_classes'],
                                        oF4_classes_are_exactly_the_all_runs_nonempty_classes=oF4_iff_nonempty,
                                        per_class_file=mo['per_class_file'])),
            m4=dict(status='legend added (addendum only)',
                    text='All words_* fields, avoider_words, nonrigid_avoider_words and literal_words count labelled'
                         ' representations, not raw words; literal_words counts sequence-run representations, which'
                         ' still repeat literal words. C(R+3,3)*5^R is per stratum H, before multiplying by'
                         ' C(H+3,3)*625. The verdict quotes only representation counts.'),
            m5=dict(status='pins recorded; fail-closed external check passes; frozen code not changed',
                    pins_enum_clean_v2=pins,
                    empty_file_sha256='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
                    fail_closed_checks={k: v['checks'] for k, v in ev['m5_pins'].items()},
                    fv_remark='fv != 0 also treats an unset entry (-1) as (d)-solved; unreachable because the table is'
                              ' filled for every multiset of size R (C(R+4,4), asserted) and every leaf multiset has'
                              ' size R by construction. Acknowledged, not changed (frozen code).'),
            m6=dict(status='provenance recorded; reproducible rebuild bit-identical; rerun identical except elapsed_s',
                    recorded_build_commands=[
                        dict(time='2026-10-18T08:40:29-07:00', cwd='desk', TMPDIR='desk/tmp',
                             command='clang++ -O2 -std=c++17 -Wall -Wextra -o bin/replay_v1 src/olson_p5o4_replay_v1.cpp',
                             compiler_output='none', source_sha256='d0f7860bb7b1fa58291c07d2614683983a7bb7243e6f362154c3c90761e76521',
                             binary_sha256='b219bcdaeee72bb134897d1d5aada5978dff5c6b3370eaa64013b5ebe79391fc',
                             evidence='session transcript (hashes printed immediately after the build)'),
                        dict(time='2026-10-18T08:43:02-07:00', cwd='desk', TMPDIR='desk/tmp',
                             command='clang++ -O2 -std=c++17 -Wall -Wextra -o bin/replay_v2 src/olson_p5o4_replay_v2.cpp',
                             compiler_output='none', source_sha256='89abe678178c677aeba29ae7cbdc1d8b21fccbb8f2f41c54aeab553710c46b68',
                             binary_sha256='4bb26b02d2ad5b05075e389b07596e7f7c0616c08ce4b8295f9eafdc58ce1cf8',
                             evidence='session transcript (hashes printed immediately after the build)')],
                    toolchain={k: ev['provenance'][k] for k in ('clang_driver', 'clang_resolved', 'clang_version', 'target',
                                                               'sdk_version', 'ld_version', 'macos', 'python')},
                    reproducible_rebuild=ev['provenance']['rebuild'],
                    build_comment_explanation='src/olson_p5o4_replay_v2.cpp was created at 08:42 by `cp -n` from v1 and'
                                              ' edited in exactly three hunks (brute usage comment L13-14; run_brute with'
                                              ' its two section-header comments L464-560; brute dispatcher L837). Line 9'
                                              ' (the Build comment naming replay_v1/_v1.cpp) was inherited unchanged and'
                                              ' is stale; it is not the command used.',
                    source_v1_to_v2=ev['provenance']['source_v1_to_v2'],
                    frozen_file_times=ev['provenance']['frozen_file_times'],
                    runs=ev['runs'],
                    route1_native_runs_latest_end=ev['route1_native_runs_latest_end'],
                    route1_native_runs_all_ended_before_sigterm=ev['route1_native_runs_all_ended_before_sigterm'],
                    sigterm_event=ev['sigterm_event'],
                    route1_files_summary=ev['route1_files_summary'],
                    rehash_all_pinned_files=ev['rehash_all_pinned_files'],
                    fresh_rerun=ev['rerun']),
            m7=dict(status='wording corrected (addendum only)',
                    text='Independent implementation; plan-time counts seen: an unblinded, independent implementation of'
                         ' the same method as worker Stage D (P1\'/(d) filter plus ordered DP), not an independent method.'
                         ' PLAN-v1 incl. its plan-time counts was displayed in full before the code was written. The'
                         ' phrase "both of my independent routes" (final message, 10:02) is withdrawn: routes 1 and 2'
                         ' share one implementation.')),
        legend_summary_json_fields={
            'per_H.multisets_*': 'rotation multisets M of size R (C(R+4,4) per H)',
            'per_H.dists_*': 'run-multiset 4-tuples (C(R+19,19) per H)',
            'per_H.words_formula': 'labelled representations of stratum H: C(H+3,3)*625*C(R+19,19)',
            'per_H.words_filter_solved_counted': 'labelled representations in (d)-solved 4-tuples, counted by multiplicity'
                                                 ' C(H+3,3)*625 (not individually decided)',
            'per_H.words_dp_enumerated': 'labelled representations decided individually by the DP',
            'per_H.words_dp_solved / words_dp_avoid': 'DP-decided labelled representations that are solved / avoid',
            'per_H.classes_*': '(H; run-multiset 4-tuple; y) classes among the (d)-surviving 4-tuples',
            'per_H.nonrigid_avoider_classes / nonrigid_avoider_words': 'non-rigid avoider classes / avoiding labelled'
                                                                       ' representations',
            'per_H.literal_run_sequences_enumerated': 'sequence-run 4-tuples of stratum H: C(R+3,3)*5^R (per H, before'
                                                      ' multiplying by C(H+3,3)*625)',
            'per_H.literal_words': 'sequence-run labelled representations of stratum H: C(H+3,3)*625*C(R+3,3)*5^R; NOT raw'
                                   ' words (literal words repeat, e.g. PC-k2 six times)',
            'totals.avoider_words': 'avoiding labelled representations (11,120)',
            'totals.avoider_classes_all_l': 'avoider classes (640)',
            'totals.nonrigid_avoider_words': 'non-rigid avoiding labelled representations (0)',
            'totals.words_formula_H0_4 / words_formula_H0_7': 'labelled representations, H = 0..4 / 0..7'},
        evidence_embedded=ev,
        new_files_sha256=new_files,
        all_ok=ev['all_ok'] and oF4_iff_nonempty)
    path = os.path.join(desk, 'ADDENDUM-v1.json')
    with open(path, 'x') as fh:
        json.dump(res, fh, indent=1)
        fh.write('\n')
    print('ADDENDUM-v1.json sha256=%s ADDENDUM-v1.md sha256=%s all_ok=%s new_files=%d' % (
        sha(path), res['note']['sha256'], res['all_ok'], len(new_files)))
    return 0 if res['all_ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
