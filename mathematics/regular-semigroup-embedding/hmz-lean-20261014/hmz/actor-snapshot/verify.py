#!/usr/bin/env python3
"""Frozen artifact checks. Passing does not resolve the original embedding problem."""
import datetime as dt
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
FORBIDDEN = re.compile(r'\b(sorry|admit|axiom|unsafe|native_decide|implemented_by|skipKernelTC|initialize|run_cmd)\b|Lean\.ofReduceBool')


def stripped(text):
    result = []
    i = 0
    depth = 0
    quoted = False
    while i < len(text):
        pair = text[i:i + 2]
        if depth:
            if pair == '/-':
                depth += 1
                i += 2
            elif pair == '-/':
                depth -= 1
                i += 2
            else:
                i += 1
        elif quoted:
            if text[i] == '\\':
                i += 2
            elif text[i] == '"':
                quoted = False
                i += 1
            else:
                i += 1
        elif pair == '/-':
            depth = 1
            result.append(' ')
            i += 2
        elif pair == '--':
            newline = text.find('\n', i)
            i = len(text) if newline < 0 else newline
        elif text[i] == '"':
            quoted = True
            result.append(' ')
            i += 1
        else:
            result.append(text[i])
            i += 1
    if depth or quoted:
        raise ValueError('Unterminated comment or string')
    return ''.join(result)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lean(path, log):
    command = [LAKE, 'env', 'lean', str(path)]
    result = subprocess.run(command, cwd=CACHE, capture_output=True, text=True, timeout=240)
    text = result.stdout + result.stderr
    log.write_text(text)
    return {'command': command, 'cwd': str(CACHE), 'returncode': result.returncode,
            'log': str(log.relative_to(ROOT)), 'sha256': digest(path)}, text


def main():
    out = ROOT / 'verification'
    out.mkdir(exist_ok=True)
    receipt = {'date_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
               'full_goal_accepted_by_checker': False,
               'scope': 'Formal artifact and semantic rejection evidence only; HMZ mathematical review is separate.'}
    failures = []
    source = ROOT / 'Formal.lean'
    negative = ROOT / 'NegativeControl.lean'
    claims_path = ROOT / 'claims.json'
    claims_document = json.loads(claims_path.read_text())
    claims = claims_document['claims'] if isinstance(claims_document, dict) else claims_document
    if not claims:
        failures.append('No claimed theorem roots')
    for path in (source, negative):
        matches = FORBIDDEN.findall(stripped(path.read_text()))
        if matches:
            failures.append(f'Forbidden syntax in {path.name}: {matches}')
    positive_result, positive_log = lean(source, out / 'formal.log')
    receipt['positive'] = positive_result
    if positive_result['returncode'] != 0:
        failures.append('Formal.lean failed')
    reports = []
    source_text = source.read_text()
    for claim in claims:
        name = claim.get('theorem') or claim.get('name')
        if not name:
            failures.append('Claim without theorem/name field')
            continue
        if f'#print {name}' not in source_text or f'#print axioms {name}' not in source_text:
            failures.append(f'Missing printed statement/axioms for {name}')
        pattern = rf"'{re.escape(name)}' depends on axioms:\s*\[([^\]]*)\]"
        match = re.search(pattern, positive_log)
        if match:
            axioms = {x.strip() for x in match.group(1).split(',') if x.strip()}
        elif re.search(rf"'{re.escape(name)}' does not depend on any axioms", positive_log):
            axioms = set()
        else:
            failures.append(f'No actual axiom output for {name}')
            axioms = {'MISSING'}
        if not axioms <= ALLOWED:
            failures.append(f'Unexpected axioms for {name}: {sorted(axioms - ALLOWED)}')
        reports.append({'theorem': name, 'observed_axioms': sorted(axioms)})
    receipt['axioms'] = reports
    negative_result, negative_log = lean(negative, out / 'negative.log')
    receipt['negative'] = negative_result
    semantic_markers = ('unsolved goals', 'Type mismatch', 'type mismatch', 'Tactic', 'tactic')
    if negative_result['returncode'] == 0 or not any(m in negative_log for m in semantic_markers):
        failures.append('Negative control did not fail semantically')
    if any(m in negative_log for m in ('unknown module prefix', 'unknown identifier', 'Unknown identifier')):
        failures.append('Negative control contains missing-dependency/identifier error')
    receipt['sources'] = {p.name: digest(p) for p in (source, negative, claims_path)}
    receipt['failures'] = failures
    receipt['artifact_checks_pass'] = not failures
    (out / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
