#!/usr/bin/env python3
"""Frozen local evidence gate; semantic full-goal acceptance remains a reviewer duty."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
CACHE = Path('/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean')
LAKE = '/Users/jinleic/.elan/bin/lake'
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}
parser = argparse.ArgumentParser()
parser.add_argument('--partial', action='store_true')
args = parser.parse_args()


def strip_noncode(text):
    result, i, depth, string = [], 0, 0, False
    while i < len(text):
        if depth:
            if text.startswith('/-', i):
                depth += 1
                i += 2
            elif text.startswith('-/', i):
                depth -= 1
                i += 2
            else:
                result.append('\n' if text[i] == '\n' else ' ')
                i += 1
        elif string:
            if text[i] == '\\':
                i += 2
            elif text[i] == '"':
                string = False
                i += 1
            else:
                i += 1
        elif text.startswith('/-', i):
            depth = 1
            i += 2
        elif text.startswith('--', i):
            end = text.find('\n', i)
            i = len(text) if end < 0 else end
        elif text[i] == '"':
            string = True
            i += 1
        else:
            result.append(text[i])
            i += 1
    if depth or string:
        raise ValueError('Unterminated comment or string')
    return ''.join(result)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lean(path):
    command = [LAKE, 'env', 'lean', str(path)]
    result = subprocess.run(command, cwd=CACHE, capture_output=True, text=True, timeout=300)
    log_path = ROOT / (path.stem + '.verification.log')
    log_path.write_text(result.stdout + result.stderr)
    return {'command': command, 'cwd': str(CACHE), 'returncode': result.returncode,
            'log': log_path.name, 'sha256': digest(path)}, result.stdout + result.stderr


receipt = {'scope': 'partial-evidence-only' if args.partial else 'full-goal-gate', 'errors': []}
try:
    claims_path = ROOT / 'claims.json'
    claims = json.loads(claims_path.read_text())
    sources = claims['sources']
    if sources != ['Formal.lean']:
        raise ValueError('Frozen gate expects the self-contained Formal.lean source')
    source = ROOT / 'Formal.lean'
    source_text = source.read_text()
    forbidden = r'\b(?:sorry|admit|axiom|native_decide|ofReduceBool|implemented_by|skipKernelTC|unsafe|initialize|run_cmd|elab|macro|syntax|addDecl)\b'
    code = strip_noncode(source_text)
    if re.search(forbidden, code):
        raise ValueError('Forbidden proof escape in Formal.lean')
    imports = re.findall(r'^\s*import\s+(.+)$', code, re.MULTILINE)
    if not imports or any(not module.startswith('Mathlib') for line in imports for module in line.split()):
        raise ValueError('Only explicit Mathlib imports permitted in self-contained source')
    theorems = claims['theorems']
    if not theorems:
        raise ValueError('No claimed mathematical theorem')
    names = [entry['name'] for entry in theorems]
    if len(set(names)) != len(names) or any(not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_.]*', name) for name in names):
        raise ValueError('Invalid or duplicate theorem names')
    for entry in theorems:
        for field in ('statement', 'assumptions', 'scope', 'axioms', 'contribution'):
            if field not in entry:
                raise ValueError('Missing theorem field ' + field)
    audit = ROOT / 'AcceptanceAudit.lean'
    audit.write_text(source_text + '\n' + '\n'.join('#print ' + name + '\n#print axioms ' + name for name in names) + '\n')
    receipt['lean'], log = lean(audit)
    if receipt['lean']['returncode'] != 0:
        raise ValueError('Lean rejected Formal.lean/audit')
    axiom_reports = {}
    for name in names:
        match = re.search(r"'" + re.escape(name) + r"' depends on axioms:\s*\[([^\]]*)\]", log)
        empty = re.search(r"'" + re.escape(name) + r"' does not depend on any axioms", log)
        if not match and not empty:
            raise ValueError('Missing observed axiom report: ' + name)
        observed = set() if empty else {word.strip() for word in match.group(1).split(',') if word.strip()}
        if not observed <= ALLOWED:
            raise ValueError('Unpermitted axioms: ' + name)
        declared = set(next(item['axioms'] for item in theorems if item['name'] == name))
        if declared != observed:
            raise ValueError('Axiom manifest differs from actual output: ' + name)
        axiom_reports[name] = sorted(observed)
    receipt['axioms'] = axiom_reports
    negative = ROOT / 'NegativeControl.lean'
    if re.search(forbidden, strip_noncode(negative.read_text())):
        raise ValueError('Negative control contains a forbidden proof escape')
    receipt['negative_control'], negative_log = lean(negative)
    if receipt['negative_control']['returncode'] == 0 or 'error:' not in negative_log:
        raise ValueError('Negative control was not rejected by Lean')
    if not claims.get('negative_control'):
        raise ValueError('Negative-control mathematical meaning not documented')
    receipt['source_sha256'] = {name: digest(ROOT / name) for name in ['Formal.lean', 'NegativeControl.lean', 'claims.json']}
    receipt['full_goal_solved'] = claims['full_goal_solved']
    receipt['target57_solved'] = claims['target57_solved']
    receipt['target87_solved'] = claims['target87_solved']
    receipt['partial_evidence_passed'] = True
    if not args.partial and claims['full_goal_solved'] is not True:
        receipt['errors'].append('The universal original goal remains unsolved; partial evidence is not RLAR acceptance.')
except Exception as exc:
    receipt['errors'].append(str(exc))
receipt['passed'] = not receipt['errors']
receipt_path = ROOT / ('verification-partial.json' if args.partial else 'verification-full.json')
receipt_path.write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
sys.exit(0 if receipt['passed'] else 1)
