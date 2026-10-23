#!/usr/bin/env python3
"""Single final audit pass for remaining-types plus discriminating corruptions (also under python -O)."""
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
    runs = [(['code/audit.py'], 0, None),
            (['code/audit.py', '--corrupt-witness'], 1, 'witness size'),
            (['code/audit.py', '--corrupt-threshold'], 1, 'projection threshold classification'),
            (['code/audit.py', '--corrupt-parity-table'], 1, 'Lemma 6.4 parity-weight table'),
            (['code/audit.py', '--corrupt-coupling'], 1, 'Lemma 2.2 coupling on genuine pair'),
            (['-O', 'code/audit.py', '--corrupt-coupling'], 1, 'Lemma 2.2 coupling on genuine pair')]
    receipts = []
    for args, expected, assertion in runs:
        t = time.monotonic()
        r = subprocess.run([sys.executable] + args, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=1200)
        ok = r.returncode == expected and (assertion is None or assertion in r.stdout)
        receipts.append({'command': ['python3'] + args, 'return_code': r.returncode, 'expected_return_code': expected,
                         'expected_assertion': assertion, 'passed': ok, 'elapsed_seconds': time.monotonic() - t,
                         'output_tail': r.stdout[-1500:]})
        if not ok:
            n = 1
            while (ROOT / ('results/failed-final-audit-%d.json' % n)).exists():
                n += 1
            (ROOT / ('results/failed-final-audit-%d.json' % n)).write_text(json.dumps(receipts, indent=2) + '\n')
            raise SystemExit('final audit failed; receipt preserved')
    audit = json.loads((ROOT / 'results/audit.json').read_text())
    produced = json.loads(gzip.decompress((ROOT / 'results/explore.json.gz').read_bytes()))
    files = ['README.md', 'PROOF.md', 'code/explore.py', 'code/rank2_probe.py', 'code/audit.py', 'code/final_verify.py',
             'inputs/slice-screen.json.gz', 'results/explore.json.gz', 'results/audit.json']
    files += sorted('results/' + p.name for p in (ROOT / 'results').glob('rank2-probe-*.json'))
    pins = {f: pin(ROOT / f) for f in files}
    types = ['(2,192)', '(4,160)', '(6,112)', '(6,128)', '(6,144)', '(8,120)', '(8,136)']
    seed = {'problem': 'info-p0403', 'lane': 'quadratic-distance/remaining-types',
            'excluded_types_this_lane': [], 'remaining_types': types,
            'previously_excluded': '(4,128) in ../zero-geometry (model-reviewed ACCEPT)',
            'new_necessary_conditions': ['partition + dual correlation (Lemma 1.1-1.2)', 'J1+E in RM(3,8) (Lemma 2.2)',
                                         'coset energy identity (Lemma 3.1)', 'single-character threshold table (Prop 3.3)',
                                         '(6,144): K-invariant Z => c>=12 (Thm 4.1)', '(2,192) coset lemmas 6.1-6.8'],
            'stopping_points': 'scalar witnesses for all seven types; projection lever vacuous for (6,112),(6,128),(8,*); '
                               'equivariance not forced for (2,192),(4,160); (2,192) joint count relaxation: see probe statuses',
            'frontier': 'PARTIAL / NEW-MATHEMATICS-REQUIRED',
            'next_obligation': 'Decide the full (2,192) joint coset count relaxation with a checkable certificate (UNKNOWN by solver), '
                               'or use Boolean realizability of per-coset E_c/X_c spectra; separate global argument for rank 6/8.',
            'verification_command': ['python3', 'code/audit.py']}
    (ROOT / 'seed-bundle.json.gz').write_bytes(gzip.compress((json.dumps(seed, separators=(',', ':')) + '\n').encode(), mtime=0))
    out = {'status': 'PASS_FINITE_AUDIT', 'book_solution': False, 'new_type_exclusions': [],
           'claims': seed['new_necessary_conditions'], 'remaining_types': types,
           'structures': audit['structures'], 'scalar_witness_stats': audit['scalar_witness_stats'],
           'parity_weight_table': audit['parity_weight_table'],
           'rank2_relaxation_witnesses_verified': audit['rank2_relaxation_witnesses_verified'],
           'rank2_probe_statuses_no_claim_unless_sat': audit['rank2_probe_statuses_no_claim_unless_sat'],
           'producer_full_relaxation_status': audit['producer_full_relaxation_status'],
           'genuine_cap32_pairs_checked': audit['genuine_cap32_pairs_checked'],
           'research_commands': [{'command': ['python3', 'code/explore.py'], 'return_code': 0, 'elapsed_seconds': produced['elapsed_seconds']}] +
                                [{'command': ['python3', 'code/rank2_probe.py', '--tag', k.split('rank2-probe-')[1][:-5]], 'status': v['status'],
                                  'seconds': v['seconds'], 'limit': v['limit']} for k, v in audit['rank2_probe_statuses_no_claim_unless_sat'].items()],
           'verification_commands': receipts, 'pins': pins,
           'seed_bundle': {'path': 'seed-bundle.json.gz', **pin(ROOT / 'seed-bundle.json.gz')},
           'frontier': seed['frontier'], 'next_obligation': seed['next_obligation'],
           'limitations': ['No remaining type excluded.', 'Solver UNKNOWN/UNSAT never promoted.',
                           'Count relaxations are not Boolean functions.', 'Model-written; not Lean/peer reviewed; novelty unestablished.'],
           'final_audit_elapsed_seconds': time.monotonic() - started}
    (ROOT / 'result.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: out[k] for k in ('status', 'new_type_exclusions', 'final_audit_elapsed_seconds')}))


if __name__ == '__main__':
    main()
