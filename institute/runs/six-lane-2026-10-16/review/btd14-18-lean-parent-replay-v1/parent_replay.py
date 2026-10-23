#!/usr/bin/python3
"""Parent-owned BTD(14,18;7,1,9;7,4) binding/rebuild/fresh-kernel audit.
Uses the established btd12-15 parent replay procedure, with independent literal targets and negative controls.
One Lean process at a time; no subprocess timeouts or process kills. Refuses existing output/build artifacts.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
OUT = HERE / 'parent-result.json'
if OUT.exists() or (HERE / 'build').exists():
    sys.exit('refusing existing result/build')


def now():
    return subprocess.check_output(['date', '+%Y-%m-%d %H:%M:%S %Z'], text=True).strip()


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


srcs = ['BTDKernel/Target.lean', 'BTDKernel/Proof.lean', 'BTDKernel/Audit.lean']
negs = ['NegLambdaFive', 'NegColSumEight', 'NegTwoTwos', 'NegFifteenRows']
wm = json.loads((HERE / 'worker-manifest.json').read_text())['files']
res = {'started_at_pt': now(), 'steps': [], 'source_pins': {s: sha(HERE / s) for s in srcs}}
res['pins_match_worker_manifest'] = all(res['source_pins'][s] == wm[s] for s in srcs)
res['parent_file_sha256'] = {s: sha(HERE / s) for s in
                           ['ParentAudit.lean', 'parent_replay.py', 'lean_env.sh', 'build_module.sh']
                           + [n + '.lean' for n in negs]}
# Recheck the actual binaries and direct Mathlib artifacts against the worker's pins.
toolchain = Path('/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1')
mathlib = Path('/private/tmp/seymour-lean-20261014-68365/.lake/packages/mathlib/.lake/build/lib/lean')
runtime = {**{'toolchain/' + n: toolchain / 'bin' / n for n in ['lean', 'leanchecker']},
           **{k: mathlib / k.removeprefix('mathlib/') for k in wm if k.startswith('mathlib/')}}
res['runtime_pins'] = {k: {'sha256': sha(p), 'match': sha(p) == wm[k]} for k, p in runtime.items()}
patterns = [r'\bsorry\b', r'\badmit\b', r'native_decide', r'ofReduceBool', r'ofReduceNat', r'implemented_by',
            r'\bextern\b', r'\bunsafe\b', r'^\s*axiom\b', r'\bopaque\b', r'csimp', r'\bmacro\b',
            r'\bsyntax\b', r'\belab\b', r'\bnotation\b', r'run_cmd', r'#eval', r'skipKernelTC',
            r'import\s+Lean\b', r'debug\.', r'Lean\.Elab']
res['scan'] = {}
for s in srcs + ['ParentAudit.lean']:
    lines = (HERE / s).read_text().split('\n')
    res['scan'][s] = {
        'forbidden_hits': [(i + 1, p) for i, line in enumerate(lines) for p in patterns if re.search(p, line)],
        'set_options': [(i + 1, line) for i, line in enumerate(lines) if 'set_option' in line],
        'imports': [line for line in lines if line.startswith('import ')]}


def run(name, command):
    started = time.monotonic()
    p = subprocess.run(command, cwd=HERE, capture_output=True, text=True)
    row = {'name': name, 'command': command, 'exit_code': p.returncode,
           'wall_seconds': round(time.monotonic() - started, 3),
           'stdout_tail': p.stdout[-1500:], 'stderr_tail': p.stderr[-1500:]}
    res['steps'].append(row)
    with (HERE / 'steps.jsonl').open('a') as f:
        f.write(json.dumps({'at': now(), **row}) + '\n')
    return p


ok = (res['pins_match_worker_manifest'] and all(v['match'] for v in res['runtime_pins'].values())
      and not any(v['forbidden_hits'] for v in res['scan'].values()))
for s in srcs + ['ParentAudit.lean']:
    if ok:
        ok = run('build-' + s, ['sh', 'build_module.sh', s]).returncode == 0
res['negatives'] = {}
if ok:
    for n in negs:
        p = run('negative-' + n, ['sh', 'build_module.sh', n + '.lean'])
        text = (HERE / 'logs' / (n + '.build.log')).read_text()
        res['negatives'][n] = {'exit_code': p.returncode, 'type_mismatch_reported': 'type mismatch' in text.lower(),
                               'olean_written': (HERE / 'build' / (n + '.olean')).exists()}
    ok = all(v['exit_code'] != 0 and v['type_mismatch_reported'] and not v['olean_written']
             for v in res['negatives'].values())
if ok:
    p = run('fresh-ParentAudit', ['sh', '-c',
            '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v ParentAudit'])
    res['fresh_output_tail'] = (p.stdout + p.stderr)[-3000:]
    ok = p.returncode == 0 and 'replaying ParentAudit with --fresh' in p.stdout + p.stderr
alog = HERE / 'logs/ParentAudit.build.log'
axioms = re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", alog.read_text()) if alog.exists() else []
res['axioms'] = {k: [a.strip() for a in v.split(',')] for k, v in axioms}
res['axioms_ok'] = (set(res['axioms']) == {'ParentBtd14Audit.no_btd', 'ParentBtd14Audit.small_exists'}
                    and all(set(v) <= {'propext', 'Classical.choice', 'Quot.sound'} for v in res['axioms'].values()))
res['status'] = 'PARENT_BTD14_BINDING_REBUILD_AND_FRESH_KERNEL_PASS' if ok and res['axioms_ok'] else 'FAIL'
res['finished_at_pt'] = now()
res['limits'] = ('One Lean4.34.1 kernel implementation for lean and leanchecker; prebuilt read-only Mathlib cache; '
                 'not Comparator or an independent external kernel. The parent-authored type gives the binding.')
with OUT.open('x') as f:
    json.dump(res, f, indent=2)
    f.write('\n')
print(res['status'])
raise SystemExit(0 if res['status'].endswith('_PASS') else 1)
