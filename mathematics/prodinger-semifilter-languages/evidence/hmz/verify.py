#!/usr/bin/env python3
"""Check final Lean artifact; mathematical scope still requires independent review."""
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
CACHE = Path('/Users/jinleic/jinleic-workspace/scratch/ai4s-math-hmz-20261014/verification/lean-verify')
formal = ROOT / 'Formal.lean'
claims_path = ROOT / 'claims.json'
if not formal.is_file() or not claims_path.is_file():
    raise SystemExit('Missing completed Formal.lean or claims.json')
source = formal.read_text()
# Lexical guard is intentionally only a guard, not a replacement for kernel checking.
without_comments = re.sub(r'/\*.*?\*/|/\-.*?\-/', '', source, flags=re.S)
without_comments = re.sub(r'--[^\n]*', '', without_comments)
forbidden = re.findall(r'\b(?:sorry|admit|axiom|native_decide|ofReduceBool|unsafe|opaque|extern|implemented_by|run_cmd|initialize)\b|#eval', without_comments)
if forbidden:
    raise SystemExit('Forbidden formal token(s): ' + repr(forbidden))
claims = json.loads(claims_path.read_text())
if not isinstance(claims, (list, dict)):
    raise SystemExit('claims.json must be a list or object describing theorem roots')
env = dict(os.environ)
env['PATH'] = str(Path.home() / '.elan/bin') + ':' + env.get('PATH', '')
env['LEAN_NUM_THREADS'] = '4'
receipts = []
for name, expect in [('Formal.lean', 0), ('NegativeControl.lean', 1)]:
    command = ['lake', 'env', 'lean', '-j', '4', str(ROOT / name)]
    result = subprocess.run(command, cwd=CACHE, env=env, text=True, capture_output=True, timeout=360)
    log = result.stdout + result.stderr
    stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    output = ROOT / 'verification' / stamp
    output.mkdir(parents=True)
    (output / (name + '.log')).write_text(log)
    passed = result.returncode == 0 if expect == 0 else result.returncode != 0 and 'decide' in log and 'false' in log
    receipts.append({'file': name, 'sha256': hashlib.sha256((ROOT / name).read_bytes()).hexdigest(), 'command': command, 'returncode': result.returncode, 'passed': passed, 'log': str(output / (name + '.log'))})
receipt = {'schema': 'semifilter-lean-check/1', 'checked_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(), 'claims_sha256': hashlib.sha256(claims_path.read_bytes()).hexdigest(), 'checks': receipts, 'scope': 'Lean default kernel and false-proposition control; not Comparator, not novelty or statement-faithfulness certification.'}
receipt_path = ROOT / 'verification' / ('receipt-' + dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ') + '.json')
receipt_path.write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
sys.exit(0 if all(r['passed'] for r in receipts) else 1)
