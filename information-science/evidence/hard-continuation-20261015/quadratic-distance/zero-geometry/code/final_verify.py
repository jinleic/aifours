#!/usr/bin/env python3
"""Single completed-research audit and meaningful mutations, including python-O."""
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
    started = time.monotonic()
    receipts = []
    visits = [([], 0, None),
              (['--corrupt-classification'], 1, 'E-extension compatibility mismatch'),
              (['--corrupt-kernel'], 1, 'kernel cubic degree mismatch'),
              (['--corrupt-projection'], 1, 'projection energy bound mismatch')]
    commands = [([sys.executable, 'code/audit.py'] + flags, expected, assertion) for flags, expected, assertion in visits]
    commands.append(([sys.executable, '-O', 'code/audit.py', '--corrupt-kernel'], 1, 'kernel cubic degree mismatch'))
    for command, expected, assertion in commands:
        t = time.monotonic()
        run = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=300)
        passed = run.returncode == expected and (assertion is None or assertion in run.stdout)
        receipts.append({'command': ['python3'] + command[1:], 'return_code': run.returncode,
                         'expected_return_code': expected, 'expected_assertion': assertion, 'passed': passed,
                         'elapsed_seconds': time.monotonic() - t, 'output': run.stdout})
        if not passed:
            n = 1
            while (ROOT / f'results/failed-final-audit-{n}.json').exists():
                n += 1
            (ROOT / f'results/failed-final-audit-{n}.json').write_text(json.dumps(receipts, indent=2) + '\n')
            raise SystemExit('Independent proof arithmetic or corruption audit failed; receipt preserved.')
    checked = json.loads((ROOT / 'results/audit.json').read_text())
    classification_raw = (ROOT / 'results/classification.json.gz').read_bytes()
    classified = json.loads(gzip.decompress(classification_raw))
    carry = json.loads((ROOT / 'results/carry-probe.json').read_text())
    gate = json.loads((ROOT / 'inputs/review-gate.json').read_text())
    if checked['status'] != 'PASS' or checked['classification']['compatible_total'] != 211:
        raise ValueError('Incomplete independent classification receipt')
    files = ['README.md', 'PROOF.md', 'code/classify.py', 'code/carry_probe.py', 'code/audit.py', 'code/final_verify.py',
             'inputs/odd-pair-codex-attempt.txt', 'inputs/quadratic-distance-PROOF.txt', 'inputs/quadratic-distance-SHARPER.txt',
             'inputs/parent-candidate-review.json', 'inputs/parent-candidate-audit.json', 'inputs/review-gate.json',
             'results/classification.json.gz', 'results/carry-probe.json', 'results/audit.json']
    pins = {f: pin(ROOT / f) for f in files}
    other_types = [[2, 192], [4, 160], [6, 112], [6, 128], [6, 144], [8, 120], [8, 136]]
    seed = {'problem': 'info-p0403', 'scope': 'New candidate exclusion of balanced quadratic residue type(rank4,weight128), not global nonexistence.',
            'hypotheses': ['Reviewed zero moments and linear8-point zero-flat from balance.',
                           'Reviewed exact slack accounting giving c=0 and the0/16/24 restricted magnitude pattern.',
                           'Canonical transform alphabet0,+64,-64 for p.',
                           'Next-bit degree<=4 with Pfaffian quartic.'],
            'normal_form': 'D=u0u1+u2u3+z',
            'coordinate_maps': 'Every zero-flat has explicit linear D-stabilizer columns in classification.json.gz; normalize p by composition with the inverse.',
            'geometry': checked['classification'],
            'remaining_geometries_excluded_by_candidate_projection': [
                {'tau': f['tau'], 'E_lifts': f['independently_enumerated_E'], 'energy_lower': f['energy_lower'], 'energy_upper': f['energy_upper']} for f in checked['families']],
            'candidate_excluded_residue_type': [4, 128], 'other_seven_residue_types': other_types,
            'one_to_three_zero_corollary': {'variables': 9, 'NL_upper_bound': 240,
                                           'depends_on_new_type_exclusion': False, 'priority': 'UNRESOLVED'},
            'proof_review_gate': gate['new_exclusion_proof_status'],
            'frontier': 'FRESH-INDEPENDENT-PROOF-REVIEW',
            'next_obligation': 'Parent obtains fresh independent review of PROOF.md and exact receipts before promoting the candidate type exclusion/corollary. Do not rerun exhausted searches. Other seven types require a separate new argument and authorization.',
            'verification_command': ['python3', 'code/audit.py'],
            'not_a_Boolean_witness': True, 'publication_or_priority_claim': False}
    payload = (json.dumps(seed, separators=(',', ':')) + '\n').encode()
    (ROOT / 'seed-bundle.json.gz').write_bytes(gzip.compress(payload, mtime=0))
    out = {'status': 'PASS_FINITE_AUDIT', 'new_proof_status': gate['new_exclusion_proof_status'],
           'claim': 'Assuming the reviewed zero-set/magnitude and next-bit lemmas with errata, NO balanced9-variable peak<=28 function has residue type(rank4,weight128).',
           'book_solution': False, 'global_nonexistence_claim': False,
           'candidate_excluded_type': [4, 128], 'other_residue_types': other_types,
           'geometry': checked['classification'],
           'E_families': [{k: f[k] for k in ['tau', 'kernel_dimension', 'independently_enumerated_E', 'character_counts', 'energy_lower', 'energy_upper', 'strict_contradiction']} for f in checked['families']],
           'alternative_tau3_audit': checked['alternative_tau3_fiber_audit'],
           'discarded_carry_probe': checked['discarded_carry_route_independent_audit'],
           'one_to_three_zero_corollary': checked['one_to_three_zero_corollary_audit'],
           'review_gate': gate, 'source_and_input_pins': pins,
           'research_commands': [
               {'command': ['python3', 'code/classify.py'], 'return_code': 0, 'elapsed_seconds': classified['elapsed_seconds']},
               {'command': ['python3', 'code/carry_probe.py'], 'return_code': 0, 'elapsed_seconds': carry['elapsed_seconds']}],
           'verification_commands': receipts,
           'novelty': 'UNESTABLISHED; known residue/canonical-sign tools and no new-general-method claim.',
           'formal_verification': False, 'human_peer_review': False,
           'no_other_type_research_or_old_search_rerun': True,
           'frontier': seed['frontier'], 'next_obligation': seed['next_obligation'],
           'seed_bundle': {'path': 'seed-bundle.json.gz', **pin(ROOT / 'seed-bundle.json.gz')},
           'final_audit_elapsed_seconds': time.monotonic() - started}
    (ROOT / 'result.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: out[k] for k in ['status', 'new_proof_status', 'candidate_excluded_type', 'book_solution', 'final_audit_elapsed_seconds']}, sort_keys=True))


if __name__ == '__main__':
    main()
