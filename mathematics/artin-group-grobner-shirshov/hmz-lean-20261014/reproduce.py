#!/usr/bin/env python3
"""Replay final partial formal claims and exact reduced-strategy controls."""
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
receipt = {'schema': 'artin-hmz-lean-integrated/1', 'started_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'full_original_goal_kernel_certified': False, 'hmz_accepted': False,
           'scope': 'Conditional exact-rule completeness and finite controls, not a full Artin GS theorem.'}
try:
    process = json.loads((ROOT / 'hmz-evidence/process.json').read_text())
    for name in ('TASK.md', 'verify.py'):
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == process['frozen_sha256'][name]
    commands = []
    for name, log in [('verify.py', 'frozen-checker.log'), ('reduced_filter_control.py', 'reduced-filter-checker.log')]:
        command = [sys.executable, str(ROOT / name)]
        result = subprocess.run(command, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=600)
        (ROOT / log).write_text(result.stdout)
        commands.append({'command': command, 'returncode': result.returncode, 'log': log})
        assert result.returncode == 0, f'{name} failed; read {log}'
    receipt['commands'] = commands
    negative = (ROOT / 'negative-control.log').read_text()
    source_lines = (ROOT / 'NegativeControl.lean').read_text().splitlines()
    error_lines = [int(x) for x in re.findall(r'^.*NegativeControl\.lean:(\d+):\d+: error(?:\([^)]*\))?:', negative, re.M)]
    names = []
    for error_line in error_lines:
        declarations = [re.match(r'theorem\s+(\w+)', line) for line in source_lines[:error_line]]
        names.append([m.group(1) for m in declarations if m][-1])
    assert names == ['dropped_output_valid', 'reversed_blocks_valid'], f'Unexpected negative failures: {names}'
    true_controls = ['ArtinNegative.local_balance_is_valid', 'ArtinNegative.actual_path_accepts',
                     'ArtinNegative.correct_output_is_valid', 'ArtinNegativeOrder.actual_braid_relation',
                     'ArtinNegativeOrder.actual_accepted_output']
    allowed = {'propext', 'Classical.choice', 'Quot.sound'}
    controls = {}
    for name in true_controls:
        match = re.search("'" + re.escape(name) + r"' depends on axioms:\s*\[([^]]*)\]", negative)
        if match:
            controls[name] = [x.strip() for x in match.group(1).split(',') if x.strip()]
        else:
            assert "'" + name + "' does not depend on any axioms" in negative, f'Missing true-control output: {name}'
            controls[name] = []
        assert set(controls[name]) <= allowed
    assert 'sorryAx' not in negative
    claims = json.loads((ROOT / 'claims.json').read_text())
    for name in ('Formal.lean', 'NegativeControl.lean'):
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == claims['source_files'][name]['sha256']
    observed = json.loads((ROOT / 'verification.json').read_text())['observed_axioms']
    assert set(observed) == {c['name'] for c in claims['claims']}
    assert all(c['full_goal'] is False for c in claims['claims'])
    receipt.update({'partial_checks_passed': True, 'theorem_count': len(claims['claims']),
                    'negative_rejected_theorems': names, 'negative_true_control_axioms': controls,
                    'axiom_union': sorted(set().union(*map(set, observed.values()))),
                    'source_sha256': {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                                      for name in ['Formal.lean', 'NegativeControl.lean', 'claims.json', 'verify.py', 'reproduce.py', 'reduced_filter_control.py']}})
except Exception as error:
    receipt.update({'partial_checks_passed': False, 'error': str(error)})
receipt['ended_at_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
(ROOT / 'acceptance.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
sys.exit(0 if receipt['partial_checks_passed'] else 1)
