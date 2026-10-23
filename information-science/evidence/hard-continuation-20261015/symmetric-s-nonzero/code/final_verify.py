#!/usr/bin/env python3
"""Single final independent evidence/encoding replay, with negative controls."""
from pathlib import Path
import gzip
import hashlib
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def pin(path):
    raw = path.read_bytes()
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def main():
    started = time.monotonic()
    receipts = []
    for args, code, assertion in [(['code/check.py'], 0, None),
                                  (['code/check.py', '--corrupt-spectrum'], 1, 'corrupted spectrum'),
                                  (['code/check.py', '--corrupt-encoding'], 1, 'corrupt gate encoding')]:
        t = time.monotonic()
        run = subprocess.run([sys.executable] + args, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=600)
        good = run.returncode == code and (assertion is None or assertion in run.stdout)
        receipts.append({'command': ['python3'] + args, 'return_code': run.returncode, 'expected_return_code': code,
                         'expected_assertion': assertion, 'passed': good, 'elapsed_seconds': time.monotonic() - t,
                         'output': run.stdout})
        if not good:
            number = 1
            while (ROOT / f'results/failed-final-replay-{number}.json').exists():
                number += 1
            (ROOT / f'results/failed-final-replay-{number}.json').write_text(json.dumps(receipts, indent=2) + '\n')
            raise SystemExit('Independent replay failed; failure receipt preserved.')
    audit = json.loads((ROOT / 'results/check.json').read_text())
    exact = json.loads((ROOT / 'results/exact-run.json').read_text())
    pb = json.loads((ROOT / 'results/native-pb-run.json').read_text())
    data = json.loads(gzip.decompress((ROOT / 'inputs/orbits.json.gz').read_bytes()))
    searches = {k: json.loads((ROOT / f'results/search-{k}.json').read_text()) for k in ('3-dsbf', '3-rsbf', 'unrestricted')}
    load_bearing = ['README.md', 'classification.md', 'sources/literature.json', 'sources/lxw-proposition1-excerpt.txt',
                    'code/generate.py', 'code/orbit_search.cpp', 'code/exact_cnf.py', 'code/run_exact.py', 'code/native_pb.py', 'code/check.py', 'code/final_verify.py',
                    'inputs/orbits.json.gz', 'inputs/3-dsbf.matrix.txt', 'inputs/3-rsbf.matrix.txt', 'inputs/unrestricted.matrix.txt',
                    'results/3-dsbf-snonzero.cnf.gz', 'results/3-dsbf-snonzero.encoding.json.gz',
                    'results/control-bound32-snonzero.cnf.gz', 'results/control-bound32-snonzero.encoding.json.gz',
                    'results/search-3-dsbf.json', 'results/search-3-rsbf.json', 'results/search-unrestricted.json',
                    'results/search-recovery-control.json', 'results/exact-run.json', 'results/exact-solver.log',
                    'results/native-pb-run.json', 'results/native-pb.smt2.gz', 'results/check.json']
    pins = {p: pin(ROOT / p) for p in load_bearing}
    candidates = []
    for kind, run in searches.items():
        text = ['?'] * 512
        for j, orbit in enumerate(data['classes'][kind]['orbits']):
            for x in orbit:
                text[x] = run['best_orbit_bits'][j]
        candidates.append({'kind': kind, 'bits': ''.join(text), 'peak': run['best_max_abs_W'],
                           'support_xor': run['best_support_xor'], 'weight': run['best_weight'],
                           'status': 'NOT_A_TARGET_WITNESS', 'source': f'results/search-{kind}.json'})
    bundle = {'problem': 'info-p0403', 'continuation': 'symmetric-s-nonzero',
              'target': 'Any9-variable Walsh peak<=28 with nonzero support XOR, then an actual Walsh zero and explicit balancing shift.',
              'published_type': {'seed_count': 5, 'support_xor': 0, 'weight_mod4': 2, 'walsh_mod8': 4,
                                 'novelty': 'Known residue tools and degree-seven status; no new mechanism claim.'},
              'best_non_witnesses': candidates,
              'orbit_input': {'path': 'inputs/orbits.json.gz', **pins['inputs/orbits.json.gz']},
              'exact_circuit': {'path': 'results/3-dsbf-snonzero.cnf.gz', **pins['results/3-dsbf-snonzero.cnf.gz'], 'status': 'UNKNOWN'},
              'native_pb': {'path': 'results/native-pb.smt2.gz', **pins['results/native-pb.smt2.gz'], 'solver_status': pb['solver_status'], 'certified_status': 'UNKNOWN'},
              'verification_command': ['python3', 'code/check.py'],
              'frontier': 'PROOF-OBLIGATION / NONZERO-TYPE-CONSTRUCTION',
              'next_obligation': 'Use a structural support-type/quadratic-residue decomposition or an independently new degree-eight construction. Do not repeat these seeds/objective or call the proof-capped run UNSAT. Any native-PB UNSAT remains uncertified until independently checked proof output exists.',
              'positive_acceptance': '512 indexed bits; all512 Walsh values by direct character sums and FWHT; if any zero exists, explicit character shift yielding weight256 and peak<=28.'}
    seed_raw = (json.dumps(bundle, separators=(',', ':')) + '\n').encode()
    (ROOT / 'seed-bundle.json.gz').write_bytes(gzip.compress(seed_raw, mtime=0))
    commands = [{'command': 'python3 code/generate.py', 'return_code': 0},
                {'command': 'c++ -O3 -std=c++17 code/orbit_search.cpp -o code/orbit_search', 'return_code': 0}]
    for kind, run in searches.items():
        commands.append({'command': f"code/orbit_search inputs/{kind}.matrix.txt nonzero {run['rng_seed']} 180 results/search-{kind}.json", 'return_code': 0, 'elapsed_seconds': run['elapsed_seconds']})
    commands += [{'command': 'code/orbit_search inputs/3-dsbf.matrix.txt any 20261015040300 30 results/search-recovery-control.json', 'return_code': 0},
                 {'command': 'python3 code/exact_cnf.py --bound 28 --prefix results/3-dsbf-snonzero', 'return_code': 0},
                 {'command': 'python3 code/exact_cnf.py --bound 32 --prefix results/control-bound32-snonzero', 'return_code': 0},
                 {'command': 'python3 code/run_exact.py --seconds 300 --proof-mb 256', 'return_code': 0, 'solver_return_code': exact['return_code'], 'elapsed_seconds': exact['elapsed_seconds']},
                 {'command': 'python3 code/native_pb.py', 'return_code': 0, 'elapsed_seconds': pb['elapsed_seconds']}]
    out = {'status': 'PASS', 'book_solution': False, 'new_negative_theorem': False,
           'type_witness_count': len(audit['type_witnesses']), 'balanced_NL242_witness': None,
           'literature_status': 'Prior support-sum/residue tools located; no novelty claim.',
           'published_seed_type': [{k: r[k] for k in ['name', 'weight', 'support_xor', 'peak', 'walsh_0_mod8_count', 'sha256_ascii_bits']} for r in audit['published_seed_mod8_audits']],
           'heuristic_spaces': {k: {'status': v['status'], 'seconds': v['elapsed_seconds'], 'best_peak': v['best_max_abs_W'], 'best_s': v['best_support_xor'], 'proposals': v['proposals'], 'restarts': v['restarts']} for k, v in searches.items()},
           'exact_spaces': {'3-dsbf': 'UNKNOWN', '3-rsbf': 'UNATTEMPTED', 'unrestricted': 'UNATTEMPTED'},
           'full_circuit_solver': exact, 'native_pb_solver': pb,
           'universal_encoding_audit': audit['target_circuit_universal_audit'], 'controls': audit['controls'],
           'verification_commands': receipts, 'research_commands': commands,
           'load_bearing_pins': pins, 'seed_bundle': {'path': 'seed-bundle.json.gz', **pin(ROOT / 'seed-bundle.json.gz')},
           'large_incomplete_artifact_excluded_from_handoff': {'path': 'results/3-dsbf-snonzero.lrat.gz', 'bytes': exact['retained_proof_bytes'], 'sha256': exact['retained_proof_sha256'], 'status': 'unverified partial trace; retained, not a certificate'},
           'frontier': bundle['frontier'], 'next_obligation': bundle['next_obligation'],
           'limitations': ['Finite seeded non-finds are not exclusions.', 'Exact proof-capped result is UNKNOWN.',
                           'Native-PB solver-only UNSAT, if any, would remain uncertified.',
                           'A nonzero-support-XOR NL242 table without a Walsh zero would still not solve the balanced problem.',
                           'No Lean or human-peer-review claim.'],
           'final_replay_elapsed_seconds': time.monotonic() - started}
    (ROOT / 'result.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: out[k] for k in ['status', 'type_witness_count', 'new_negative_theorem', 'exact_spaces', 'final_replay_elapsed_seconds']}, sort_keys=True))


if __name__ == '__main__':
    main()
