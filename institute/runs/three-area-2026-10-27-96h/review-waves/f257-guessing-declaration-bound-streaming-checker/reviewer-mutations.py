#!/usr/bin/env python3
"""In-memory single-site mutants of the frozen f257 checker; synthetic data only."""
import copy
import hashlib
import json
import signal
import subprocess
import sys
import time
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHECKER = ROOT / 'checker-v4.py'
OUT = ROOT / 'reviewer-mutations-result.json'
LIMIT = time.monotonic() + 115


def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def stop(_sig, _frame):
    raise TimeoutError('MUTATION_RUN_INTERRUPTED_OR_LIMIT')


def load(source):
    ns = {'__name__': 'f257_synthetic_mutant', '__file__': str(CHECKER)}
    exec(compile(source, '<in-memory-checker>', 'exec'), ns)
    ns['DEADLINE'] = LIMIT
    return ns


def contract_for(ns, path, record):
    archive = path.read_bytes()
    with zipfile.ZipFile(path) as z:
        infos = z.infolist()
        packet = z.read('packet-manifest.json')
    return {'sha256': sha(archive), 'bytes': len(archive), 'members': len(infos),
            'uncompressed': sum(i.file_size for i in infos), 'packet_sha256': sha(packet),
            'certificates': 1, 'rows': len(record['rows']), 'planes': 1, 'four_cases': 0, 'classes': 0,
            'coefficient_members': ('coefficients/synthetic.jsonl',), 'graph_member': 'data/graph.json',
            'class_member': 'data/classes.json', 'four_member': 'data/four.jsonl', 'plane_member': 'data/planes.jsonl',
            'fixture_universe': [(1, 2, 3)]}


def outcome(ns, case, record, binding, raw):
    fixture_system = {'type': 'functional_branch', 'coordinate_id': '5*A+b', 'A_vertex_subset_mask': [0, 1023],
                      'b': {'0': 'none', '1': 'S=(A_bit,B_bit)', '2': 'A_bit', '3': 'B_bit', '4': 'A_bit XOR B_bit'},
                      'nonempty_coordinates': 5119}
    scope = {'colors': [0, 1] + [None] * 8, 'coloring': '01--------', 'class_id_zero_based': 0}
    try:
        if case == 'declaration_pin':
            ns['guard_declaration_digest'](raw + b' ')
        elif case == 'unknown_descriptor':
            ns['row_vector'](['unrecognized', 1], fixture_system, scope)
        elif case == 'gate_selector':
            ns['row_vector'](['gate', 2], fixture_system, scope)
        elif case == 'local_decoder':
            ns['row_vector'](['functional-local-fd', 1, 0], fixture_system, scope)
        elif case == 'state_visibility':
            ns['row_vector'](['state-neighborhood', 2], fixture_system, scope)
        elif case == 'data_formula':
            vec, relation = ns['row_vector'](['data-processing', 1, 2], fixture_system, scope)
            return 'FORMULA_OK' if (vec, relation) == ({7: 1, 6: -1}, 'le') else 'FORMULA_WRONG:' + repr(vec)
        elif case == 'pair_formula':
            vec, relation = ns['row_vector'](['pair-determines-state', 1, 3, 4], fixture_system, scope)
            return 'FORMULA_OK' if (vec, relation) == ({6: 1, 5: 1, 8: -1, 9: -1}, 'le') else 'FORMULA_WRONG:' + repr(vec)
        elif case == 'color_action':
            ident = list(range(1, 11))
            item = {'coordinate_system': fixture_system, 'scope': scope, 'action_count': 2,
                    'actions': [[ident, [0, 1, 2]], [ident, [1, 0, 2]]]}
            ns['validate_actions'](item, False)
        elif case in ('relation', 'sign', 'inner_weight', 'image'):
            mutated = copy.deepcopy(record)
            if case == 'relation':
                mutated['rows'][0]['relation'] = 'le'
            elif case == 'sign':
                mutated['rows'][0]['name']['multiplier'] = -2
                mutated['rows'][0]['multiplier'] = '-2'
            elif case == 'inner_weight':
                mutated['rows'][0]['name']['multiplier'] = 7
            else:
                mutated['rows'][0]['image_vectors'][0][0][1] = 9
            ns['verify_identity'](mutated, binding, 5000)
        elif case in ('plane_set', 'member_hash'):
            path = ROOT / ('reviewer-synthetic-wrong-plane.zip' if case == 'plane_set' else 'reviewer-synthetic-bad-member.zip')
            ns['verify_archive'](path, contract_for(ns, path, record), 1, 5000, 1)
        elif case == 'deadline':
            ns['DEADLINE'] = time.monotonic() - 1
            ns['tick']()
        else:
            raise RuntimeError('BAD_CASE:' + case)
    except (ns['Reject'], ns['Unknown']) as exc:
        return type(exc).__name__ + ':' + str(exc)
    return 'ACCEPTED'


def main():
    for sig in (signal.SIGINT, signal.SIGTERM, signal.SIGALRM):
        signal.signal(sig, stop)
    signal.setitimer(signal.ITIMER_REAL, 115)
    begin = clock()
    try:
        source = CHECKER.read_text(encoding='utf-8')
        source_sha = sha(source.encode())
        baseline = load(source)
        _, raw, bindings = baseline['verify_sources']()
        record_raw = (ROOT / 'reviewer-synthetic-record.json').read_bytes()
        record = json.loads(record_raw)
        binding = json.loads((ROOT / 'reviewer-synthetic-binding.json').read_bytes())
        mutants = [
            ('declaration_pin', "need(sha256(raw)==DECLARATION_SHA, 'DECLARATION_SHA_MISMATCH')", 'pass', 'Reject:DECLARATION_SHA_MISMATCH', 'ACCEPTED'),
            ('unknown_descriptor', "if key not in SCHEMA: raise Unknown('UNSUPPORTED_DESCRIPTOR:' + str(key))", "if key not in SCHEMA: return 'gate','le'", "Unknown:UNSUPPORTED_DESCRIPTOR:('functional_branch', 'unrecognized')", 'ACCEPTED'),
            ('gate_selector', "need(type(name[1]) is int and name[1]==1, 'GATE_BRANCH_NOT_FULL_STATE')", 'pass', 'Reject:GATE_BRANCH_NOT_FULL_STATE', 'ACCEPTED'),
            ('local_decoder', "need(inc=={c}, 'LOCAL_DECODER_NOT_SINGLETON_COLOR')", 'pass', 'Reject:LOCAL_DECODER_NOT_SINGLETON_COLOR', 'ACCEPTED'),
            ('state_visibility', "need(len(incident_colors(v,colors))>=2, 'STATE_NOT_VISIBLE')", 'pass', 'Reject:STATE_NOT_VISIBLE', 'ACCEPTED'),
            ('data_formula', 'for key,value in ((5*a+b,1),(5*a+1,-1)): add(out,key,value)', 'for key,value in ((5*a+b,-1),(5*a+1,1)): add(out,key,value)', 'FORMULA_OK', 'FORMULA_WRONG:{7: -1, 6: 1}'),
            ('pair_formula', 'for key,value in ((5*a+1,1),(5*a,1),(5*a+b,-1),(5*a+c,-1)): add(out,key,value)', 'for key,value in ((5*a+1,1),(5*a,-1),(5*a+b,-1),(5*a+c,-1)): add(out,key,value)', 'FORMULA_OK', 'FORMULA_WRONG:{6: 1, 5: -1, 8: -1, 9: -1}'),
            ('color_action', "need(all(colors[fact[i]] == (None if colors[i] is None else c[colors[i]]) for i in range(10)),\n                 'ACTION_CHANGES_COLORING')", 'pass', 'Reject:ACTION_CHANGES_COLORING', 'ACCEPTED'),
            ('relation', "need(row['relation']==relation,'ROW_RELATION_MISMATCH')", 'pass', 'Reject:ROW_RELATION_MISMATCH', 'ACCEPTED'),
            ('sign', "need(valid,'ROW_SIGN')", 'pass', 'Reject:ROW_SIGN', 'Reject:COEFFICIENT_IDENTITY_MISMATCH'),
            ('inner_weight', "need(type(row['name']['multiplier']) is int and coeff==row['name']['multiplier'], 'INNER_MULTIPLIER_MISMATCH')", 'pass', 'Reject:INNER_MULTIPLIER_MISMATCH', 'ACCEPTED'),
            ('image', 'parse_vector(advertised,max_id,False)==actual', 'True', 'Reject:IMAGE_VECTOR_MISMATCH:D1-synthetic:row=0:action=0', 'ACCEPTED'),
            ('plane_set', "need(actual==universe,'PLANE_UNIVERSE_SET_MISMATCH')", 'pass', 'Reject:PLANE_UNIVERSE_SET_MISMATCH', 'ACCEPTED'),
            ('member_hash', "need(got==item['sha256'] and size==item['bytes'],'MEMBER_PIN_MISMATCH:'+name)", 'pass', 'Reject:MEMBER_PIN_MISMATCH:sources/synthetic.json', 'ACCEPTED'),
            ('deadline', "if time.monotonic() >= DEADLINE:\n        raise Unknown('TIME_LIMIT')", 'if False:\n        pass', 'Unknown:TIME_LIMIT', 'ACCEPTED'),
        ]
        results = []
        for case, original, replacement, expected_original, expected_mutant in mutants:
            if time.monotonic() >= LIMIT:
                raise TimeoutError('MUTATION_TIME_LIMIT')
            if source.count(original) != 1:
                raise RuntimeError('MUTATION_ANCHOR_NOT_UNIQUE:' + case + ':' + str(source.count(original)))
            original_outcome = outcome(baseline, case, record, binding, raw)
            if original_outcome != expected_original:
                raise RuntimeError('ORIGINAL_REASON_MISMATCH:' + case + ':' + original_outcome)
            mutant = load(source.replace(original, replacement, 1))
            mutant_outcome = outcome(mutant, case, record, binding, raw)
            if mutant_outcome != expected_mutant:
                raise RuntimeError('MUTANT_REASON_MISMATCH:' + case + ':' + mutant_outcome)
            results.append({'case': case, 'original': original_outcome, 'mutant': mutant_outcome, 'killed': True})
        result = {'status': 'MUTATION_CONTROLS_PASS', 'clock_start': begin, 'clock_end': clock(),
                  'checker_sha256': source_sha, 'controls_sha256': sha(Path(__file__).read_bytes()),
                  'manifest_sha256': baseline['MANIFEST_SHA'], 'declaration_sha256': baseline['DECLARATION_SHA'],
                  'record_sha256': sha(record_raw), 'source_bindings': bindings, 'mutants': results,
                  'scope': 'single-site in-memory mutants against synthetic data only; no scientific ZIP replay'}
        code = 0
    except Exception as exc:
        result = {'status': 'UNKNOWN', 'clock_start': begin, 'clock_end': clock(),
                  'reason': type(exc).__name__ + ':' + str(exc), 'checker_sha256': sha(CHECKER.read_bytes()),
                  'controls_sha256': sha(Path(__file__).read_bytes())}
        code = 3
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    payload = (json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + '\n').encode()
    with open(OUT, 'xb') as f:
        f.write(payload)
    print(json.dumps({'status': result['status'], 'reason': result.get('reason'), 'receipt': str(OUT),
                      'sha256': sha(payload), 'exit': code}, sort_keys=True))
    return code


if __name__ == '__main__':
    sys.exit(main())
