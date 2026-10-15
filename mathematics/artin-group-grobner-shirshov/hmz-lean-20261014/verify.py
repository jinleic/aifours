#!/usr/bin/env python3
"""Frozen scoped Lean replay; success is not full Artin-theorem acceptance."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
CACHE = Path('/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean')
LAKE = '/Users/jinleic/.elan/bin/lake'
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}
FORBIDDEN = re.compile(r'\b(sorry|admit|axiom|unsafe|native_decide|ofReduceBool|implemented_by|skipKernelTC|initialize|run_cmd|elab|macro|syntax)\b')


def clean_lean(text):
    result = []
    index = 0
    depth = 0
    quoted = False
    while index < len(text):
        two = text[index:index + 2]
        if depth:
            if two == '/-':
                depth += 1
                index += 2
            elif two == '-/':
                depth -= 1
                index += 2
            else:
                index += 1
        elif quoted:
            if text[index] == '\\':
                index += 2
            elif text[index] == '"':
                quoted = False
                index += 1
            else:
                index += 1
        elif two == '/-':
            depth = 1
            index += 2
        elif two == '--':
            end = text.find('\n', index)
            index = len(text) if end < 0 else end
        elif text[index] == '"':
            quoted = True
            index += 1
        else:
            result.append(text[index])
            index += 1
    return ''.join(result)


def run(source, output):
    command = [LAKE, 'env', 'lean', str(source)]
    start = time.monotonic()
    result = subprocess.run(command, cwd=CACHE, text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, timeout=240)
    (ROOT / output).write_text(result.stdout)
    return {'command': command, 'cwd': str(CACHE), 'returncode': result.returncode,
            'seconds': time.monotonic() - start, 'log': output}, result.stdout


receipt = {'schema': 'artin-hmz-lean-acceptance/1',
           'scope': 'Partial claims only; does not certify full Theorem G or HMZ acceptance.'}
try:
    source = ROOT / 'Formal.lean'
    control = ROOT / 'NegativeControl.lean'
    claims = json.loads((ROOT / 'claims.json').read_text())
    entries = claims['claims']
    assert entries, 'No theorem claims supplied'
    receipt['source_sha256'] = {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in (source, control, ROOT / 'claims.json')}
    lexical = clean_lean(source.read_text())
    bad = FORBIDDEN.findall(lexical)
    assert not bad, f'Forbidden Lean constructs: {bad}'
    assert FORBIDDEN.search(clean_lean('theorem bad : False := by sorry')), 'Scanner control failed'
    imports = re.findall(r'^import\s+(.+)$', lexical, re.M)
    receipt['imports'] = imports
    assert all(all(name.startswith('Mathlib') for name in row.split()) for row in imports), 'Self-contained proof must import Mathlib only; reference OAI by attribution'
    receipt['lean'], log = run(source, 'lean.log')
    assert receipt['lean']['returncode'] == 0, 'Formal Lean compilation failed'
    observed = {}
    for name, raw in re.findall(r"'([^']+)' depends on axioms:\s*\[([^]]*)\]", log):
        observed[name] = [part.strip() for part in raw.split(',') if part.strip()]
    for name in re.findall(r"'([^']+)' does not depend on any axioms", log):
        observed[name] = []
    for entry in entries:
        name = entry['name']
        assert entry['source'] == 'Formal.lean', f'Unexpected source for {name}'
        assert re.search(r'^#print\s+' + re.escape(name) + r'\s*$', lexical, re.M), f'Missing statement print: {name}'
        assert re.search(r'^#print axioms\s+' + re.escape(name) + r'\s*$', lexical, re.M), f'Missing axiom print: {name}'
        assert name in observed, f'No actual axiom output: {name}'
        assert set(observed[name]) <= ALLOWED, f'Illegal axioms: {name}: {observed[name]}'
        assert set(entry['axioms']) == set(observed[name]), f'Claimed axiom mismatch: {name}'
    receipt['observed_axioms'] = observed
    receipt['negative_control'], negative_log = run(control, 'negative-control.log')
    assert receipt['negative_control']['returncode'] != 0, 'Wrong theorem was accepted'
    assert 'error:' in negative_log, 'Negative control failed without Lean diagnostic'
    assert 'unknown module' not in negative_log and 'file not found' not in negative_log, 'Negative control is broken infrastructure, not a rejected theorem'
    receipt['success'] = True
except Exception as error:
    receipt['success'] = False
    receipt['error'] = str(error)
(ROOT / 'verification.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
sys.exit(0 if receipt['success'] else 1)
