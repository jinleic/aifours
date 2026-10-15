#!/usr/bin/env python3
"""Frozen evidence checks, not a decision procedure for universal Serre equality."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time

ROOT = Path(__file__).resolve().parent
CACHE = Path('/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean')
LAKE = '/Users/jinleic/.elan/bin/lake'
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}


def lexical_code(text):
    out, i, depth, quoted = [], 0, 0, False
    while i < len(text):
        if depth:
            if text.startswith('/-', i):
                depth += 1
                i += 2
            elif text.startswith('-/', i):
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
        elif text.startswith('/-', i):
            depth = 1
            i += 2
        elif text.startswith('--', i):
            end = text.find('\n', i)
            i = len(text) if end == -1 else end
        elif text[i] == '"':
            quoted = True
            out.append(' ')
            i += 1
        else:
            out.append(text[i])
            i += 1
    return ''.join(out)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compile_lean(name):
    command = [LAKE, 'env', 'lean', str(ROOT / name)]
    started = time.monotonic()
    run = subprocess.run(command, cwd=CACHE, text=True, capture_output=True, timeout=600)
    log = run.stdout + run.stderr
    (ROOT / (name + '.log')).write_text(log)
    return {'command': command, 'cwd': str(CACHE), 'returncode': run.returncode,
            'seconds': time.monotonic() - started, 'log': name + '.log'}, log


claims = json.loads((ROOT / 'claims.json').read_text())
assert isinstance(claims['full_goal_solved'], bool)
assert claims['claims'], 'No claimed theorem roots'
for name in ('Formal.lean', 'NegativeControl.lean', 'REPORT.md', 'REFERENCES.md'):
    assert (ROOT / name).is_file(), 'Missing ' + name
formal = (ROOT / 'Formal.lean').read_text()
code = lexical_code(formal)
banned = r'\b(sorry|admit|axiom|native_decide|unsafe|implemented_by|skipKernelTC|initialize|run_cmd|elab|macro|syntax|opaque|partial|extern)\b|Lean\.ofReduceBool|#eval'
assert not re.search(banned, code), 'Forbidden proof escape in Formal.lean'
imports = re.findall(r'^import\s+([^\n]+)', code, re.MULTILINE)
assert imports and all(all(x.startswith('Mathlib') for x in row.split()) for row in imports), 'Only audited Mathlib imports allowed'
for claim in claims['claims']:
    assert all(key in claim for key in ('source', 'name', 'statement', 'scope', 'assumptions', 'axioms', 'content_status'))
    assert claim['source'] == 'Formal.lean'
    assert set(claim['axioms']) <= ALLOWED
    assert re.search(r'^#print\s+' + re.escape(claim['name']) + r'\s*$', code, re.MULTILINE)
    assert re.search(r'^#print\s+axioms\s+' + re.escape(claim['name']) + r'\s*$', code, re.MULTILINE)
positive, positive_log = compile_lean('Formal.lean')
negative, negative_log = compile_lean('NegativeControl.lean')
assert positive['returncode'] == 0, 'Formal.lean failed: see its log'
assert negative['returncode'] != 0 and 'error:' in negative_log, 'Negative control unexpectedly accepted'
for claim in claims['claims']:
    pattern = re.escape(claim['name']) + r"'? depends on axioms: \[([^\]]*)\]"
    found = re.search(pattern, positive_log)
    no_axioms = re.search(re.escape(claim['name']) + r"'? does not depend on any axioms", positive_log)
    assert found or no_axioms, 'Missing actual axiom print for ' + claim['name']
    actual = set() if no_axioms else {x.strip() for x in found.group(1).split(',') if x.strip()}
    assert actual <= ALLOWED, 'Unapproved axioms: ' + repr(actual)
    assert actual == set(claim['axioms']), 'Claims/printed axiom mismatch: ' + claim['name']
receipt = {
    'schema': 'kac-moody-hmz-lean-evidence/1',
    'partial_evidence_checks_pass': True,
    'full_goal_claimed_solved': claims['full_goal_solved'],
    'universal_acceptance': 'NOT ESTABLISHED BY THIS CHECKER; actual reviewer must audit theorem scope and proof',
    'positive': positive, 'negative_control': negative,
    'imports': imports, 'permitted_axioms': sorted(ALLOWED),
    'source_sha256': {name: digest(ROOT / name) for name in ('TASK.md', 'verify.py', 'Formal.lean', 'NegativeControl.lean', 'claims.json', 'REPORT.md', 'REFERENCES.md')},
    'toolchain': (CACHE / 'lean-toolchain').read_text().strip(),
    'comparator_run': False, 'nanoda_run': False,
}
(ROOT / 'verification.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
