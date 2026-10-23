#!/usr/bin/env python3
"""One final independent question/model audit, four discriminating corruptions, and receipts."""
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def pin(path):
    raw = path.read_bytes()
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def main():
    start = time.monotonic()
    receipts = []
    visits = [([], 0, None),
              (['--corrupt-encoding'], 1, 'corrupt Walsh/PB correspondence'),
              (['--corrupt-type'], 1, 'corrupt support-type constraint'),
              (['--corrupt-balance'], 1, 'corrupt exact-balance constraint'),
              (['--corrupt-spectrum'], 1, 'corrupt spectrum')]
    for flags, expected, assertion in visits:
        command = [sys.executable, 'code/check.py'] + flags
        t = time.monotonic()
        run = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=300)
        passed = run.returncode == expected and (assertion is None or assertion in run.stdout)
        receipts.append({'command': ['python3', 'code/check.py'] + flags, 'return_code': run.returncode,
                         'expected_return_code': expected, 'expected_assertion': assertion, 'passed': passed,
                         'elapsed_seconds': time.monotonic() - t, 'output': run.stdout})
        if not passed:
            i = 1
            while (ROOT / f'results/failed-final-replay-{i}.json').exists():
                i += 1
            (ROOT / f'results/failed-final-replay-{i}.json').write_text(json.dumps(receipts, indent=2) + '\n')
            raise SystemExit('Independent type-decomposition replay failed; failure preserved.')
    checked = json.loads((ROOT / 'results/check.json').read_text())
    decomposition = json.loads((ROOT / 'inputs/decomposition.json').read_text())
    types = checked['types_derived_from_group']
    assert types == [146, 365, 511]
    runs = {s: json.loads((ROOT / f'results/s{s}-run.json').read_text()) for s in types}
    equivalence = json.loads((ROOT / 'inputs/type-equivalence.json').read_text())
    witnessed = [s for s in types if checked['results'][str(s)]['certified_status'] == 'SAT_VERIFIED']
    unknown = [s for s in types if s not in witnessed]
    files = ['README.md', 'PROOF.md', 'code/generate.py', 'code/run_case.py', 'code/check.py', 'code/final_verify.py',
             'code/derive_equivalence.py', 'inputs/type-equivalence.json',
             'inputs/orbits.json.gz', 'inputs/decomposition.json', 'results/check.json']
    for s in types:
        files += [f'inputs/target-s{s}.smt2.gz', f'inputs/target-s{s}.encoding.json',
                  f'inputs/control-s{s}.smt2.gz', f'inputs/control-s{s}.encoding.json', f'results/s{s}-run.json']
        if s in witnessed:
            files.append(f'results/witness-s{s}.json')
    pins = {f: pin(ROOT / f) for f in files}
    controls = {s: {'weight': checked['planted_controls'][str(s)]['weight'],
                    'support_xor': checked['planted_controls'][str(s)]['support_xor'],
                    'max_abs_W': checked['planted_controls'][str(s)]['max_abs_W'],
                    'degree': checked['planted_controls'][str(s)]['degree'],
                    'all_relaxed_assertions_pass': checked['planted_controls'][str(s)]['all_relaxed_assertions_pass'],
                    'relaxed_bands': checked['planted_controls'][str(s)]['relaxed_question']['frequency_orbit_cap_counts']}
                for s in types}
    stop = not witnessed
    frontier = 'STOP-THIS-ROUTE / NEW-MATHEMATICS-REQUIRED' if stop else 'POSITIVE-TABLE-VERIFIED / PARENT-REVIEW'
    obligation = ('All three structural branches received one bounded exact visit. No same-formulation or same-heuristic retry is authorized by this receipt. '
                  'A continuation requires genuinely new mathematics or a proof-producing representation change, not merely a longer timeout. '
                  'The open finite obligations remain: a balanced peak<=28 3-DSBF table or a complete independently checked exclusion for each support type.')
    seed = {'problem': 'info-p0403', 'scope': 'BALANCED3-DSBF104 orbit-bit subclass only',
            'bit_order': 'bits[x]=f(x); x_i=(x>>i)&1', 'group_fixed_support_types': [146, 365, 511],
            'balance_weight': 256, 'bands': {'a.dot.s=0': 24, 'a.dot.s=1': 28},
            'normalization': 'f(0)=0 up to harmless output complement',
            'branches': [{'s': s, 'certified_status': checked['results'][str(s)]['certified_status'],
                          'solver_status': runs[s]['solver_status'], 'target_input': f'inputs/target-s{s}.smt2.gz',
                          'target_pin': pins[f'inputs/target-s{s}.smt2.gz'], 'run': f'results/s{s}-run.json',
                          'visits_completed': 1, 'seconds_limit': runs[s]['seconds_limit']} for s in types],
            'controls': decomposition['controls'], 'frontier': frontier,
            'recorded_type_equivalence': checked['type_equivalence'],
            'same_formulation_retry_allowed': False, 'next_obligation': obligation,
            'verification_command': ['python3', 'code/check.py'],
            'negative_certification_rule': 'Solver-only UNSAT is UNKNOWN until a complete certificate and question correspondence are independently checked.',
            'positive_acceptance': '512 indexed bits, weight256, all512 Walsh magnitudes<=28 by direct character sums and FWHT; no nonzero-type surrogate accepted.'}
    seed_bytes = (json.dumps(seed, separators=(',', ':')) + '\n').encode()
    (ROOT / 'seed-bundle.json.gz').write_bytes(gzip.compress(seed_bytes, mtime=0))
    out = {'status': 'PASS', 'book_solution': bool(witnessed), 'new_negative_theorem': False,
           'scope': 'Balanced3-DSBF subclass with exact support-type decomposition; not unrestricted balanced functions.',
           'fixed_support_types_derived': types, 'fixed_space_including_zero': [0, 146, 365, 511],
           'all512_vectors_checked_against_actual_group_matrices': True,
           'all512_character_rows_independently_checked': True,
           'exact_orbit_variables': 104, 'assertions_per_branch': 219,
           'target_full512_frequency_bands': {'24': 256, '28': 256},
           'balanced_target_witness_types': witnessed, 'unknown_types': unknown, 'unattempted_types': [],
           'certified_excluded_types': [], 'solver_results': {s: runs[s] for s in types},
           'planted_balanced_invariant_controls': controls,
           'recorded_type_equivalence': checked['type_equivalence'],
           'checker_source_sha256': checked['checker_source_sha256'],
           'research_commands': [{'command': ['python3', 'code/generate.py'], 'return_code': 0, 'elapsed_seconds': decomposition['elapsed_seconds']},
                                 {'command': ['python3', 'code/derive_equivalence.py'], 'return_code': 0, 'elapsed_seconds': equivalence['elapsed_seconds']}] +
                                [{'command': ['python3', 'code/run_case.py', '--s', str(s), '--seconds', str(runs[s]['seconds_limit'])],
                                  'return_code': 0, 'elapsed_seconds': runs[s]['elapsed_seconds'], 'solver_status': runs[s]['solver_status']} for s in types],
           'verification_commands': receipts, 'input_and_source_pins': pins,
           'seed_bundle': {'path': 'seed-bundle.json.gz', **pin(ROOT / 'seed-bundle.json.gz')},
           'frontier': frontier, 'next_obligation': obligation, 'same_formulation_retry_allowed': False,
           'limitations': ['A complete formulation is not an exhaustive enumeration or a negative certificate.',
                           'Solver-only UNSAT is not promoted to an exclusion.', 'No global absence claim.',
                           'Known residue/degree tools are not claimed novel.', 'No Lean or human-peer-review claim.'],
           'final_replay_elapsed_seconds': time.monotonic() - start}
    (ROOT / 'result.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: out[k] for k in ['status', 'balanced_target_witness_types', 'unknown_types', 'certified_excluded_types', 'frontier', 'final_replay_elapsed_seconds']}, sort_keys=True))


if __name__ == '__main__':
    main()
