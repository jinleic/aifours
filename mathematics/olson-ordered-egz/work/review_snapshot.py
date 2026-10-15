#!/usr/bin/env python3
"""Run one read-only, hash-pinned Codex review of the completed partial result."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / 'evidence' / 'review'
FILES = ['proof.md', 'claims.json', 'sources/references.md',
         'sources/dimitrov-2004-ocr.txt', 'evidence/source-observations.json',
         'work/DihedralLowerBound.lean', 'work/NegativeControl.lean',
         'work/ordered_smt.py', 'work/interval_route.py',
         'evidence/c3rtc4-smt.json', 'evidence/a4-smt.json',
         'evidence/interval-route.json', 'evidence/dihedral-lower-bound-lean.json',
         'evidence/negative-control-lean.log']


def main():
    SNAP.mkdir(parents=True, exist_ok=False)
    hashes = {}
    for relative in FILES:
        source = ROOT / relative
        target = SNAP / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        hashes[relative] = hashlib.sha256(source.read_bytes()).hexdigest()
    schema = {'type': 'object', 'additionalProperties': False,
              'required': ['verdict', 'summary', 'findings'],
              'properties': {'verdict': {'type': 'string', 'enum': ['correct-partial', 'needs-fix', 'incorrect']},
                             'summary': {'type': 'string'},
                             'findings': {'type': 'array', 'items': {'type': 'object', 'additionalProperties': False,
                                'required': ['severity', 'location', 'problem', 'correction'],
                                'properties': {'severity': {'type': 'string', 'enum': ['major', 'minor']},
                                               'location': {'type': 'string'}, 'problem': {'type': 'string'},
                                               'correction': {'type': 'string'}}}}}}
    (SNAP / 'schema.json').write_text(json.dumps(schema, indent=2) + '\n')
    prompt = '''You are an independent adversarial mathematical reviewer. Read ONLY the files in this snapshot directory; do not read parent paths, invoke external tools beyond read-only file inspection, delegate, write, build, test or run any scripts. The snapshot is public mathematical research, dated2026-10-14; do not correct new source claims from training-data memory.

Exact book target: every finite group G of order n and every ordered sequence of length2n-1 has indices i1<...<in whose product in that order is identity. The dossier explicitly DOES NOT claim this solved. Audit proof.md's actual infinite odd-dihedral lower bound, the complementary-cyclic boundary-insertion argument, and the DP/SMT encoding soundness. Check that the Lean theorem has the actual group cardinality, length2n-2, and List.Sublist quantifier, and is NOT a falsely advertised counterexample. The negative control failed because decide proved the proposition false. Check the fixed-word raw enumeration receipts, UNKNOWN labels and no-novelty language against source observations. No need to review proof formatting or recompute all finite cases. Original Olson1976 full text and2016 full proof were not recovered; flag any stronger claims than the sources support. Inspect SMT low-layer pruning and forward-only Horn constraints carefully. Identify only real mathematical, scope or evidentiary defects with exact file/line references. A correct known partial result with zero full resolutions is an acceptable verdict. Return the schema, concisely.'''
    (SNAP / 'prompt.txt').write_text(prompt + '\n')
    models = json.loads(Path('/Users/jinleic/jinleic-workspace/docs/knowledge-system/DELEGATE_MODELS.json').read_text())
    model = models['codex']
    command = ['codex', 'exec', '-m', model['model'], '-c', 'model_reasoning_effort=' + model['effort'],
               '--sandbox', 'read-only', '--ephemeral', '--skip-git-repo-check', '-C', str(SNAP),
               '--output-schema', str(SNAP / 'schema.json'), '-o', str(SNAP / 'result.json'), prompt]
    started = time.monotonic()
    with (SNAP / 'stdout.log').open('w') as out, (SNAP / 'stderr.log').open('w') as err:
        result = subprocess.run(command, cwd=SNAP, stdin=subprocess.DEVNULL, stdout=out, stderr=err,
                                timeout=1200)
    receipt = {'command': command, 'model': model, 'source_sha256': hashes,
               'returncode': result.returncode, 'elapsed_seconds': time.monotonic() - started,
               'sandbox': 'read-only; does not confine reads; prompt restricts snapshot only'}
    (SNAP / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({'returncode': result.returncode, 'elapsed_seconds': receipt['elapsed_seconds'],
                      'result': json.loads((SNAP / 'result.json').read_text()) if (SNAP / 'result.json').exists() else None}, indent=2))
    raise SystemExit(result.returncode)


if __name__ == '__main__':
    main()
