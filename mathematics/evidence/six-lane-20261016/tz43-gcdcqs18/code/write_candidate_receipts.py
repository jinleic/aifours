#!/usr/bin/env python3
"""Create immutable receipts for the finite A partial and its order-74 consequence after all replay files land.
Run from the lane root. No checker or solver is launched here; inputs are the retained receipts and raw files.
Usage: write_candidate_receipts.py GC|MC NEW_OUTPUT.json
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: E402,F401
from lane_guard import xopen  # noqa: E402
import hashlib
import json
import re
import shutil
from datetime import datetime

GC = 'evidence/gcdcqs18-z8z3z3/gcdcqs18_4_2_z8z3z3.txt'
MC = 'evidence/mcdsqs74-c21/mcdsqs74_c21.txt'
SHA_GC = '1382d572f8024c9b93ff6f5cf8aff942a9538119e8462ba54b02b6f160da282e'
SHA_MC = 'eaff77fc63cc408756f72b6f6213eb7449a13e1efc5ba0c40401fc51d4f216c3'
RUN = 'runs/a4/sk2_x36_col_4_4_2_2_1'
REPLAY = 'runs/a4/replay_sk2_x36_4_4_2_2_1'


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def file_info(p):
    return {'path': p, 'bytes': os.path.getsize(p), 'sha256': sha(p)}


def same(a, b):
    return open(a, 'rb').read() == open(b, 'rb').read()


def timing(p):
    text = open(p).read()
    result = {'path': p, 'sha256': sha(p)}
    for label, rx in (('wall_seconds', r'([0-9.]+) real'), ('user_seconds', r'([0-9.]+) user'),
                      ('system_seconds', r'([0-9.]+) sys'), ('max_rss_bytes', r'(\d+)\s+maximum resident set size')):
        match = re.search(rx, text)
        if match:
            result[label] = int(match.group(1)) if label == 'max_rss_bytes' else float(match.group(1))
    return result


def lane_data():
    files = [os.path.join(d, f) for d, _, fs in os.walk('.') for f in fs]
    return {'bytes_before_receipt': sum(os.path.getsize(p) for p in files), 'files_before_receipt': len(files),
            'host_free_disk_bytes': shutil.disk_usage('.').free,
            'ownership_concurrency': '<=3 owned busy jobs while parent reserved one checking slot',
            'scope': 'per-step RSS is measured; no claim that a single-process peak is an aggregate-RSS measurement'}


def controls(path, expected):
    doc = json.load(open(path))
    assert doc['as_intended'] == expected
    if 'mutations' in doc:
        assert doc['mutations'] == expected
    return {'receipt': file_info(path), 'mutations': expected, 'both_routes_as_intended': expected,
            'fixtures': [file_info(os.path.join(os.path.dirname(path), f))
                         for f in sorted(os.listdir(os.path.dirname(path))) if f.endswith('.txt')]}


def gc_receipt():
    assert sha(GC) == SHA_GC
    ev = os.path.dirname(GC)
    route1 = json.load(open(f'{ev}/gcdcqs18_4_2_z8z3z3.route1-check.json'))
    route2 = open(f'{ev}/gcdcqs18_4_2_z8z3z3.route2-check.txt').read().strip()
    assert route1['result'] == 'PASS' and route1['sha256'] == SHA_GC and route2.startswith('PASS ')
    src = json.load(open(f'{RUN}/summary.json'))
    replay = f'{REPLAY}/gcdcqs18_4_2_z8z3z3_sk2_s1.txt'
    assert same(GC, replay), 'full producer replay is not byte-identical'
    seed = f'{ev}/seed-v1.json'
    seed_doc = json.load(open(seed))
    assert seed_doc['source_sha256'] == SHA_GC and seed_doc['byte_identical_regeneration'] is True
    expansion = 'runs/a4/replay_seed_v1/gcdcqs18_seed_expanded.txt'
    assert same(GC, expansion), 'stdlib seed replay is not byte-identical'
    used = ['pipeline_s5.py', 'pipeline_s.py', 'pipeline_s2.py', 'cqs_km_s.py', 'colour_model.py', 'lanelib.py',
            'lane_guard.py', 'check_gcdcqs_s.py', 'check_gcdcqs_s.c', 'mutations_fmt.py', 'seed_gcdcqs18.py']
    return {
        'object': 'gcDCQS(18^4:2)', 'status': 'CANDIDATE-PARTIAL: object A only, parent verification separate',
        'certificate': file_info(GC),
        'finite_definition': {'points': 74, 'stem': [72, 73], 'groups': 'four groups of 18, labels per certificate',
                              'covered_triples': 60264, 'blocks': 15066, 'group_points': 72,
                              'group_derived_triples_each': 819, 'colours': 37, 'holefree': 10,
                              'stem_derived_triples_each': 648, 'stem_frame_classes_each': 36,
                              'class_sizes_every_group_point': '24^24 23^3 18^5 17^4 16'},
        'primary_source': file_info('sources/tz/tan-zhou-2503.11934.txt'),
        'definition_lines': 'CQS LF 256-266; gcSTS LF 211-220; KF LF 237-240; gcDCQS LF 281-288',
        'contract': {'path': 'institute/runs/six-lane-2026-10-16/screening/math-1-tz43-contract.json',
                     'sha256': 'cfafe572e7ba1a2feaaa4224b3ab562d501295c0b07f0df9d8095ed3f9946a17'},
        'producer': {'model': 'Z8 x Z3^2 translations, t8 swaps stems, Singer S^2 multiplier; |G|=288, R=C4',
                     'arguments': src['args'], 'accepted_sample': 1, 'km_seed': 1, 'colouring_seed': 1,
                     'KM_sample0_colour': 'UNKNOWN at native 900 s; sample1 KM includes its blocking clause',
                     'avoid_stabilizer_orders': [4, 4, 2, 2, 1], 'excluded_KM_rows': src['excl36_rows_forbidden'],
                     'source_run': file_info(f'{RUN}/summary.json'),
                     'accepted_model_dimensions': {k: src['samples'][1][k] for k in
                                                   ('km_vars', 'km_clauses', 'col_vars', 'col_clauses',
                                                    'triple_orbits', 'km_seconds', 'col_seconds')},
                     'selected_CNF_and_models': [file_info(f'{RUN}/{p}') for p in
                         ('km_0.cnf', 'km_1.cnf', 'km_1.cnf.log', 'col_1.cnf', 'col_1.cnf.log')],
                     'correctness_scope': 'raw verification assumes none of the symmetry/model restrictions'},
        'checkers': {'route1': {'code': file_info('code/check_gcdcqs_s.py'), 'result': route1,
                               'receipt': file_info(f'{ev}/gcdcqs18_4_2_z8z3z3.route1-check.json')},
                     'route2': {'author': 'Tz43CCheckers from frozen definition/format; did not read route1',
                                'code': file_info('code/check_gcdcqs_s.c'),
                                'binary': file_info('code/bin/check_gcdcqs_s_c'), 'result': route2},
                     'calibration': 'published RDCQS(8^4:2) Lemma3.1, gcDCQS(8^4:0), gcDCQS(32^4:0); both routes PASS',
                     'independence': 'stdlib Python route1 and separately authored C route2; parent routes not counted here'},
        'controls': controls(f'{ev}/mutations/mutation-results.json', 12),
        'replays': {'full_producer': {'output': file_info(replay), 'byte_identical': True,
                                      'summary': file_info(f'{REPLAY}/summary.json')},
                    'stdlib_seed': {'seed': file_info(seed), 'output': file_info(expansion), 'byte_identical': True,
                                    'block_orbits': len(seed_doc['block_representatives']),
                                    'block_orbit_sizes': seed_doc['block_orbit_sizes'],
                                    'action_negative_control': seed_doc['action_negative_control']}},
        'code_hashes': {p: sha(f'code/{p}') for p in used},
        'resources': {'source_search': timing(f'{RUN}.time.txt'), 'producer_replay': timing(f'{REPLAY}.time.txt'),
                      'route1': timing(f'{ev}/route1.time.txt'), 'route2': timing(f'{ev}/route2.time.txt'),
                      'mutations': timing(f'{ev}/mutations.time.txt'), 'data': lane_data()},
        'limits': 'No novelty/priority claim; no unrestricted nonexistence result. The frozen gate still needs FDGDD or RDGDD(3,4,5{18}).',
    }


def mc_receipt():
    assert sha(MC) == SHA_MC and sha(GC) == SHA_GC
    ev = os.path.dirname(MC)
    route1 = json.load(open(f'{ev}/mcdsqs74_c21.py39-check.json'))
    route2 = open(f'{ev}/mcdsqs74_c21.c-check.txt').read().strip()
    assert route1['result'] == 'PASS' and route1['sha256'] == SHA_MC and route2.startswith('PASS ')
    replay = 'runs/c/replay-mcdsqs74-c21.txt'
    assert same(MC, replay), 'order-74 producer replay is not byte-identical'
    return {
        'object': 'mcDSQS(74) by Tan-Zhou Construction2.1 (g,n,s)=(18,4,2)',
        'status': 'CANDIDATE finite consequence of object A; not the complete tz43 gate',
        'certificate': file_info(MC), 'blocks': 16206, 'triples': 64824, 'points': 74,
        'format_note': 'Raw UTF-8 file includes U+222A in a hash-comment only; noncomment certificate lines are ASCII. '
                       'The copied worker checkers permit UTF-8 comments. Parent strict-ASCII projection checks are separate, '
                       'not claimed as acceptance of these unchanged raw bytes.',
        'derived_triples_per_point': 876, 'colours': 37,
        'minimality': 'a PPC on73 points has at most24 triples; 36*24=864<876, so37 colours are necessary',
        'inputs': [file_info(GC), file_info('sources/sxk/sxk_prop3_transcription.json')],
        'builder': file_info('code/build_mcdsqs74.py'),
        'bridge_note': file_info(f'{ev}/construction-2.1-hypotheses.md'),
        'bridge_scope': 'gcDSQS(20,2)=mcDSQS(20) justified using each other-stem degree9 across10 classes; the output is checked directly',
        'checkers': {'python': {'code': file_info('code/mcdsqs/check_mcdsqs.py'), 'result': route1},
                     'C': {'code': file_info('code/mcdsqs/check_mcdsqs.c'),
                           'binary': file_info('code/bin/check_mcdsqs_c'), 'result': route2},
                     'independence': 'copied definition-first stdlib/C implementations from the earlier mcDSQS lane; no symmetry assumed'},
        'controls': controls(f'{ev}/mutations/mutation-results.json', 15),
        'replay': {'output': file_info(replay), 'byte_identical': True},
        'resources': {'build': timing('runs/c/build.time.txt'), 'python_checker': timing('runs/c/pycheck.time.txt'),
                      'data': lane_data()},
        'limits': 'No family theorem from this certificate alone, no novelty/priority claim; B remains required.',
    }


def main():
    mode, out = sys.argv[1:3]
    rec = {'recorded_at_host': datetime.now().astimezone().isoformat(),
           'receipt_generator': file_info(__file__), **{'GC': gc_receipt, 'MC': mc_receipt}[mode]()}
    with xopen(out) as fh:
        json.dump(rec, fh, indent=1, ensure_ascii=False)
        fh.write('\n')
    print(json.dumps(file_info(out)))


if __name__ == '__main__':
    main()
