#!/usr/bin/env python3
"""Write receipt-v2.json (exclusive create): hashes, counts, verifier relations, dispositions, limits.
v2: same content as make_receipt.py, written after the final verdict-v1.md edit; also hashes receipt-v1.json.
Usage: /usr/bin/python3 -B make_receipt_v2.py
"""
import hashlib
import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo

DESK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REVIEW = os.path.dirname(DESK)
ORIG = ('/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/tz43-gcdcqs18/evidence/'
        'fdgdd18-d15-inflated/fdgdd_5_18_inflated_D15.txt')


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def rel(*parts):
    return os.path.join(DESK, *parts)


def main():
    out_path = rel('receipt-v2.json')
    if os.path.exists(out_path):
        raise SystemExit('refusing to overwrite ' + out_path)
    m1 = json.load(open(rel('build-manifest.json')))
    m2 = json.load(open(rel('build-manifest-v2.json')))
    x1 = json.load(open(rel('checker-matrix-v1.json')))
    x2 = json.load(open(rel('checker-matrix-v2.json')))
    files = ['lemma-v1.md', 'lemma-v2.md', 'dispositions-v1.md', 'verdict-v1.md', 'checkpoint-01.md',
             'inputs/master_H_5_6.json', 'fdgdd_5_18_konig_tripled.txt', 'incidence-colourings.json',
             'fixtures/mut_a_colour_vertex_swap.txt', 'fixtures/mut_b_colour_shift_A_vertex.txt',
             'fixtures/mut_c_wrong_third_sum_constant.txt', 'fixtures/mut_d_duplicate_frame_class.txt',
             'build-manifest.json', 'build-manifest-v2.json', 'checker-matrix-v1.json', 'checker-matrix-v2.json',
             'review-prompts-v1.json', 'runs/replay-brew-OB-hashes-v1.json', 'runs/build-v1.stdout.txt',
             'runs/build-v2-verify.stdout.txt', 'code/build_tripled_fdgdd.py', 'code/build_tripled_fdgdd_v2.py',
             'code/run_checker_matrix.py', 'code/run_checker_matrix_v2.py', 'code/make_review_prompts.py',
             'code/make_receipt.py', 'code/make_receipt_v2.py', 'receipt-v1.json', 'dispositions-v1.md']
    review_files = ['tz43-tripling-codex-v1.prompt.txt', 'tz43-tripling-codex-v1.note.md',
                    'tz43-tripling-codex-v1.receipt.json', 'tz43-tripling-claude-v1.prompt.txt',
                    'tz43-tripling-claude-v1.note.md', 'tz43-tripling-claude-v1.receipt.json']

    def outcomes(mx):
        res = {}
        for r in mx['rows']:
            key = '%s/%s' % (r['checker'], r['case'])
            obs = r['failed_checks'] if r['checker'] == 'parent' else r['invariant']
            res.setdefault(key, {'runs': 0, 'ok': 0, 'exit': set(), 'observed': set()})
            res[key]['runs'] += 1
            res[key]['ok'] += int(r['ok'])
            res[key]['exit'].add(r['exit'])
            res[key]['observed'].add(json.dumps(obs))
        return dict((k, {'runs': v['runs'], 'ok': v['ok'], 'exit': sorted(v['exit']),
                         'observed': sorted(v['observed'])}) for k, v in sorted(res.items()))

    receipt = {
        'desk': 'Tz43TriplingAudit (auxiliary to closed math-1 section 4(3); no new gate)',
        'written_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
        'object': 'FDGDD(3,4,5{18}) in Tan-Zhou arXiv:2503.11934v1 LF 246-247; constructive frames via zero-sum tripling',
        'files_sha256': dict((p, sha(rel(p))) for p in files),
        'review_files_sha256': dict((p, sha(os.path.join(REVIEW, p))) for p in review_files),
        'original_certificate': {'path': ORIG, 'sha256': sha(ORIG),
                                 'block_prefix_lines_byte_identical': m1['stats'][
                                     'header_groups_blocks_prefix_byte_identical_to_original'],
                                 'prefix_lines': m1['stats']['original_prefix_lines']},
        'checkers': {
            'parent_definition_checker': {'path': x2['parent_checker'], 'sha256': x2['parent_checker_sha256'],
                                          'relation': 'parent-side omp desk implementation written from the '
                                                      'definition (model family not re-verified here; presumably '
                                                      'Claude-family like the orchestrator); pre-existing, unchanged'},
            'claude_prompt_only_checker': {'path': x2['claude_checker'], 'sha256': x2['claude_checker_sha256'],
                                           'relation': 'prompt-only claude-opus-5-5 authored, parent executed; '
                                                       'same vendor family as the orchestrator; pre-existing, '
                                                       'unchanged'},
            'generator_internal_checks': 'construction-side only; not counted as an independent checker',
            'cross_vendor_execution': 'none for this certificate: both executing checkers are Claude-side '
                                      'implementations; the cross-vendor Codex contribution is a static review'},
        'structure_counts': m1['stats'],
        'outputs_v1_equal_v2_regeneration': m1['outputs'] == m2['outputs'],
        'matrix_v1': {'sha256': sha(rel('checker-matrix-v1.json')), 'summary': x1['summary'],
                      'outcomes': outcomes(x1)},
        'matrix_v2': {'sha256': sha(rel('checker-matrix-v2.json')), 'summary': x2['summary'],
                      'outcomes': outcomes(x2), 'bound': {'generator': x2['generator_sha256_bound'],
                                                          'master': x2['master_sha256_bound'],
                                                          'original': x2['original_sha256_bound']}},
        'reviews': {
            'tz43-tripling-codex-v1': {'model': 'gpt-6.1-sol', 'effort': 'max', 'sandbox': 'read-only',
                                       'vendor_relation': 'cross-vendor to the Claude-family orchestrator',
                                       'disposition': 'ACCEPT', 'findings': 0, 'static_only': True},
            'tz43-tripling-claude-v1': {'model': 'claude-opus-5-5', 'effort': 'max', 'tools': [],
                                        'vendor_relation': 'same vendor family as the orchestrator',
                                        'disposition': 'ACCEPT-WITH-FIXES', 'findings': {'MINOR': 10},
                                        'all_findings_disposed': 'dispositions-v1.md'}},
        'verdict': 'Valid purely constructive replacement of the frame-SAT step for FDGDD(3,4,5{18}); the master '
                   'H(5,6,4,3) provenance (KM SAT, directly checked) and the other section 4(3) ingredients are '
                   'unchanged; the original accepted certificate 3e22f502 remains the accepted witness.',
        'novelty': 'NOT CLAIMED (Lemma 1 routine from Koenig; likely folklore; no literature screen at this desk)',
        'limits': ['only group size 6 -> 18 (r = 3), 5 groups', 'v2 lemma/code not re-reviewed (MINOR fixes only)',
                   'H(5,6,4,3) existence quoted secondhand', 'no formal proof, no human review',
                   'fan-widening and other scout leads not assessed'],
    }
    with open(out_path, 'x') as f:
        json.dump(receipt, f, indent=1)
        f.write('\n')
    print(sha(out_path))


if __name__ == '__main__':
    main()
