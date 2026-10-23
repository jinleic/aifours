#!/usr/bin/env python3
"""One final independent replay and discriminating mutations; write receipts."""
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    raw = path.read_bytes()
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def main():
    started = time.monotonic()
    commands = [
        (['code/check.py'], 0, None),
        (['code/check.py', '--mutate-spectrum'], 1, 'fixed-half direct spectrum mismatch'),
        (['code/check.py', '--mutate-certificate'], 1, 'incomplete or invalid quadratic certificate'),
        (['code/check.py', '--mutate-final-certificate'], 1, 'invalid final mixed-difference certificate'),
    ]
    receipts = []
    for args, expected, message in commands:
        t0 = time.monotonic()
        completed = subprocess.run([sys.executable] + args, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=300)
        passed = completed.returncode == expected and (message is None or message in completed.stdout)
        receipts.append({'command': ['python3'] + args, 'return_code': completed.returncode,
                         'expected_return_code': expected, 'expected_assertion': message,
                         'passed': passed, 'elapsed_seconds': time.monotonic() - t0,
                         'output': completed.stdout})
        if not passed:
            (ROOT / 'results/failed-final-replay.json').write_text(json.dumps(receipts, indent=2) + '\n')
            raise SystemExit('Independent replay or discriminating control failed; receipt retained.')
    check = json.loads((ROOT / 'results/check.json').read_text())
    assert check['status'] == 'PASS' and check['resolved_classes'] == 252
    screen = json.loads(gzip.decompress((ROOT / 'results/screen.json.gz').read_bytes()))
    parity = json.loads((ROOT / 'results/final-parity.json').read_text())
    pins = {}
    for rel in ['README.md', 'proof.md', 'code/screen.py', 'code/parity_certificate.py', 'code/check.py', 'code/final_verify.py',
                'inputs/slice-screen.json.gz', 'results/screen.json.gz', 'results/final-parity.json']:
        pins[rel] = digest(ROOT / rel)
    prior = []
    for i in range(3):
        p = ROOT / f'inputs/prior-slice-completion{i}-run.json'
        r = json.loads(p.read_text())
        assert r['status'] == 'UNKNOWN' and r['stop_reason'] == 'proof-size limit'
        prior.append({'path': str(p.relative_to(ROOT)), **digest(p), 'status': 'UNKNOWN',
                      'stop_reason': r['stop_reason'], 'elapsed_seconds': r['seconds'], 'proof_limit_mb': r['proof_limit_mb']})
    cases = []
    for i, r in enumerate(screen['classes']):
        cases.append({'source': r['source'], 'normal': r['normal'], 'status': 'EXCLUDED',
                      'literal_capacity_group': screen['identity_spectral_group_for_all_252'][i],
                      'certificate_stage': r['class_stage'] if r['class_stage'] != 'UNKNOWN' else 'final-parity-coset'})
    seed = {'problem': 'info-p0403', 'target': 'Balanced 9-variable Boolean function with nonlinearity at least 242',
            'bit_order': 'bits[x]=f(x); x_i=(x>>i)&1',
            'input': {'path': 'inputs/slice-screen.json.gz', **digest(ROOT / 'inputs/slice-screen.json.gz')},
            'completed_corpus': cases, 'resolved_classes': 252, 'unknown_classes': 0, 'unattempted_classes': 0,
            'safe_equivalence': 'Literal equality of absolute 256-term slice spectra, identity spectral-coordinate map; 154 groups; no full EA classification claim.',
            'mechanism': 'Known 2-adic quadratic residue and affine sign normalization, local capacity/Parseval, odd autocorrelation residues, and complete affine correction-parity enumeration.',
            'verification_command': ['python3', 'code/check.py'],
            'frontier': 'PROOF-OBLIGATION: GLOBAL-CONSTRUCTION-OR-EXCLUSION',
            'next_obligation': 'Do not retry these exhausted halves. Select genuinely new degree-eight half tables outside this pinned corpus and apply exact quadratic/canonical/moment screens before completion search, or prove a universal obstruction on pairs of odd half spectra.',
            'positive_acceptance': '512 indexed bits; explicit character shift at a Walsh zero; weight256; all512 magnitudes<=28 by both direct character sums and FWHT.',
            'forbidden_inference': 'This finite corpus does not imply global absence of a balanced NL242 function; old UNKNOWN solver attempts remain UNKNOWN.'}
    seed_raw = (json.dumps(seed, separators=(',', ':')) + '\n').encode()
    (ROOT / 'seed-bundle.json.gz').write_bytes(gzip.compress(seed_raw, mtime=0))
    out = {'status': 'PASS', 'problem': 'info-p0403', 'book_solution': False,
           'claim': 'All252 fixed-half classes that passed the epoch-2 necessary screen have exact balanced maximum240.',
           'resolved_classes': 252, 'unknown_classes': 0, 'unattempted_classes': 0,
           'new_exclusions_by_stage': {'quadratic-Parseval-zero': 152, 'autocorrelation-residue-energy': 71,
                                       'canonical-inverse-energy': 28, 'final-parity-coset': 1},
           'literal_capacity_groups': 154, 'full_original_corpus_closed_with_imported_screen': 31744,
           'imported_previous_exclusions_not_rerun': 31492,
           'explicit_balanced_NL242_witness': None, 'global_balanced_maximum': [240, 242],
           'final_parity': {k: parity[k] for k in ['source', 'normal', 'energy_deficit_budget', 'affine_rank', 'affine_dimension', 'enumerated_parities', 'minimum_forced_deficit']},
           'proof_controls': check['controls'], 'final_moment_control': check['final_parity']['planted_bound32_moment_control'],
           'independent_checker_source_hash': check['checker_source_sha256'], 'input_and_source_pins': pins,
           'prior_unknowns_preserved': prior, 'commands': receipts,
           'new_production_seconds': {'screen': screen['elapsed_seconds'], 'final_parity': parity['elapsed_seconds']},
           'production_commands_executed': [
               {'command': ['python3', 'code/screen.py'], 'return_code': 0, 'elapsed_seconds': screen['elapsed_seconds']},
               {'command': ['python3', 'code/parity_certificate.py'], 'return_code': 0, 'elapsed_seconds': parity['elapsed_seconds']}],
           'final_replay_elapsed_seconds': time.monotonic() - started,
           'corrected_initial_control_failure': {
               'path': 'results/failed-final-replay.json',
               **digest(ROOT / 'results/failed-final-replay.json'),
               'cause': 'Published unbalanced NL242 seed has support XOR0 and no odd slice; corrected the positive-control scope, not the exclusion mechanism.'},
           'frontier': seed['frontier'], 'next_obligation': seed['next_obligation'],
           'limitations': ['Restricted overlapping fixed-half corpus, not arbitrary degree-eight functions.',
                           'No novelty claim: residue/canonical-sign tools are prior art; finite application is the present output.',
                           'Not Lean-verified or human peer-reviewed.',
                           'No solver-only result is used as an exclusion.'],
           'seed_bundle': {'path': 'seed-bundle.json.gz', **digest(ROOT / 'seed-bundle.json.gz')}}
    (ROOT / 'result.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: out[k] for k in ['status', 'resolved_classes', 'unknown_classes', 'unattempted_classes', 'new_exclusions_by_stage', 'final_replay_elapsed_seconds']}, sort_keys=True))


if __name__ == '__main__':
    main()
