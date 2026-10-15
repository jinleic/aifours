#!/usr/bin/env python3
"""Frozen artifact checks; success does not assert the original theorem is solved."""
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
CACHE = Path('/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean')
LAKE = '/Users/jinleic/.elan/bin/lake'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def code_only(text):
    out = []
    depth = 0
    quoted = False
    line_comment = False
    index = 0
    while index < len(text):
        pair = text[index:index + 2]
        char = text[index]
        if line_comment:
            if char == '\n':
                line_comment = False
                out.append('\n')
            index += 1
        elif depth:
            if pair == '/-':
                depth += 1
                index += 2
            elif pair == '-/':
                depth -= 1
                index += 2
            else:
                index += 1
        elif quoted:
            if char == '\\':
                index += 2
            else:
                if char == '"':
                    quoted = False
                index += 1
        elif pair == '--':
            line_comment = True
            index += 2
        elif pair == '/-':
            depth = 1
            index += 2
        elif char == '"':
            quoted = True
            index += 1
        else:
            out.append(char)
            index += 1
    return ''.join(out)

stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
output = ROOT / 'verification' / stamp
output.mkdir(parents=True, exist_ok=False)
receipt = {'created_at_utc': stamp, 'full_goal_acceptance': False,
           'meaning': 'Artifact checks only; original-goal acceptance requires independent mathematical review.',
           'cache_cwd': str(CACHE), 'checks': {}, 'source_sha256': {}}
errors = []
required = ['Formal.lean', 'NegativeControl.lean', 'claims.json', 'mathematical-progress.md', 'references.md']
for name in required:
    path = ROOT / name
    if not path.is_file():
        errors.append('Missing required file: ' + name)
    else:
        receipt['source_sha256'][name] = sha(path)

banned = r'\b(sorry|admit|axiom|unsafe|native_decide|ofReduceBool|implemented_by|skipKernelTC|run_cmd|initialize|elab|macro|syntax|addDecl|partial|extern)\b|#eval'
positive_source = ROOT / 'Formal.lean'
if positive_source.is_file():
    clean = code_only(positive_source.read_text())
    found = sorted(set(re.findall(banned, clean)))
    receipt['checks']['forbidden_mechanisms'] = found
    if found:
        errors.append('Forbidden proof mechanism(s): ' + repr(found))
    imports = re.findall(r'^\s*import\s+(.+)$', clean, re.MULTILINE)
    receipt['imports'] = imports
    if any(not part.startswith('Mathlib') for line in imports for part in line.split()):
        errors.append('Formal.lean must be self-contained except direct Mathlib imports.')

claims = None
if (ROOT / 'claims.json').is_file():
    try:
        claims = json.loads((ROOT / 'claims.json').read_text())
        if not isinstance(claims, dict) or not isinstance(claims.get('full_goal_solved'), bool):
            errors.append('claims.json requires Boolean full_goal_solved.')
        receipt['declared_full_goal_solved'] = claims.get('full_goal_solved')
    except Exception as exc:
        errors.append('Invalid claims.json: ' + str(exc))

for name, expected in [('Formal.lean', 0), ('NegativeControl.lean', 'reject')]:
    path = ROOT / name
    if not path.is_file():
        continue
    command = [LAKE, 'env', 'lean', str(path)]
    result = subprocess.run(command, cwd=CACHE, text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, timeout=300)
    (output / (name + '.log')).write_text(result.stdout)
    entry = {'command': command, 'returncode': result.returncode,
             'log': str((output / (name + '.log')).relative_to(ROOT))}
    if name == 'Formal.lean':
        entry['axiom_lines'] = [line for line in result.stdout.splitlines() if 'depends on axioms:' in line]
        if result.returncode != 0:
            errors.append('Formal.lean failed elaboration.')
        if not entry['axiom_lines']:
            errors.append('No #print axioms evidence in positive compilation.')
        used_axioms = set()
        for match in re.finditer(r'depends on axioms:\s*\[([^\]]*)\]', result.stdout, re.DOTALL):
            used_axioms.update(part.strip() for part in match.group(1).split(',') if part.strip())
        entry['used_axioms'] = sorted(used_axioms)
        if used_axioms - {'propext', 'Classical.choice', 'Quot.sound'}:
            errors.append('Nonpermitted axioms: ' + repr(sorted(used_axioms)))
        if not re.search(r'^\s*#print\s+(?!axioms\b)\S+', positive_source.read_text(), re.MULTILINE):
            errors.append('Missing printed theorem statement.')
    elif result.returncode == 0 or 'error:' not in result.stdout:
        errors.append('NegativeControl.lean did not produce a Lean error.')
    elif any(text in result.stdout for text in ['unknown module prefix', 'no such file', 'unexpected token', 'unexpected end of input']):
        errors.append('Negative control failed for an import/syntax issue, not a meaningful mathematical rejection.')
    receipt['checks'][name] = entry

receipt['errors'] = errors
receipt['artifact_checks_passed'] = not errors
(output / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({'receipt': str(output / 'receipt.json'), 'artifact_checks_passed': not errors,
                  'full_goal_acceptance': False, 'errors': errors}, indent=2))
sys.exit(bool(errors))
