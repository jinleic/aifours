#!/usr/bin/env python3
"""Reproduce the isolated, no-tools other-vendor mathematical review."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument('--focused', action='store_true')
args = parser.parse_args()
prefix = 'focused-review' if args.focused else 'review'

root = Path(__file__).resolve().parents[1]
workspace = root.parents[1]
registry = json.loads((workspace/'docs/knowledge-system/DELEGATE_MODELS.json').read_text())['claude']
out = root/'evidence/continuation-20261014'
inputs = [root/'work/collection-continuation.md', root/'work/verify_collection_continuation.py',
          out/'certificate.json']
prompt = '''You are an independent hostile mathematical referee. Do NOT delegate, use tools, read other files, browse, or modify anything. All permitted mathematical inputs are embedded below. Review the proposed exact finite impossibility argument for arbitrary probabilistic visual cryptography collections, especially whether full ordered forbidden row-matrix distributions (not just column moments) are enforced, whether support pruning preserves every genuine scheme, optimum LP-face complementarity, integer threshold coverage, orbit enumeration completeness, and the explicit terminal separator. Also check the general cone lemma for fixed-length BASIS tradeoffs and global COLLECTION contrast. The code has not yet had its decisive final replay; do not mistake claimed exploratory counts for execution evidence. Parent is independently rebuilding an oracle. You need not prove literature novelty; none is claimed. Find actual logical or encoding defects, counterexamples or missing hypotheses. Distinguish optional improvements from errors. Return concise JSON with fields verdict, mathematical_findings, code_findings, cone_lemma, acceptance_conditions, limitations. A correct-with-fixes verdict must specify exactly the required changes.\n'''
if args.focused:
    inputs = [out/'focused-review-prompt.txt']
    prompt = 'Independent mathematical referee task; permitted context follows.\n'
for path in inputs:
    prompt += '\n===== '+str(path.relative_to(root))+' =====\n'+path.read_text()
(out/f'{prefix}-input.txt').write_text(prompt)
command = ['claude', '--model', registry['model'], '--effort', registry['effort'],
           '--safe-mode', '--no-chrome', '--tools', '', '--permission-mode', 'dontAsk',
           '--no-session-persistence', '--output-format', 'json', '-p', prompt]
(out/f'{prefix}-command.json').write_text(json.dumps({
    'argv': command[:-1]+[f'<contents of {prefix}-input.txt>'], 'cwd': str(root),
    'inputs_sha256': {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
}, indent=2)+'\n')
started = time.monotonic()
try:
    result = subprocess.run(command, cwd=root, stdin=subprocess.DEVNULL,
                            capture_output=True, text=True, timeout=900)
    stdout, stderr, returncode = result.stdout, result.stderr, result.returncode
except subprocess.TimeoutExpired as exc:
    stdout, stderr, returncode = exc.stdout or '', exc.stderr or '', 124
    if isinstance(stdout, bytes):
        stdout = stdout.decode(errors='replace')
    if isinstance(stderr, bytes):
        stderr = stderr.decode(errors='replace')
(out/f'{prefix}-stdout.json').write_text(stdout)
(out/f'{prefix}-stderr.txt').write_text(stderr)
receipt = {'returncode': returncode, 'seconds': time.monotonic()-started,
           'requested_model': registry['model'], 'requested_effort': registry['effort']}
(out/f'{prefix}-receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps(receipt))
raise SystemExit(returncode)
