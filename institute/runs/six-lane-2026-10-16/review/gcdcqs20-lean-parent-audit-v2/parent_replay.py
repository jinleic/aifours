#!/usr/bin/python3
"""Parent-owned replay of the GcdcqsKernel Lean development (gcDCQS(20^4:0), mcDSQS(80), chi'(79) = 40).

Steps: pin-check the worker's 51 files and the two raw certificates; copy the build closure of Gc80.Audit80 into
./src; regenerate the 20 data modules from the parent-pinned raw certificates with the pinned generator and require
byte identity; run the parent's own forbidden-token scan; rebuild every module sequentially into a fresh ./build;
build the parent-authored ParentAudit.lean and require the two parent statement mutations to fail with a type
mismatch; run `leanchecker --fresh` on ParentAudit; parse `#print axioms`. One Lean process at a time; no timeouts
or kills. Refuses to overwrite parent-result.json, ./src, ./build, ./regen.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent
WORKER = REVIEW / 'gcdcqs20-kernel-worker-v1'
OUT = HERE / 'parent-result.json'
for p in [OUT, HERE / 'src', HERE / 'build', HERE / 'regen']:
    if p.exists():
        sys.exit('refusing existing ' + p.name)
TOOLCHAIN = Path('/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1')
CACHE = Path('/private/tmp/seymour-lean-20261014-68365/.lake/packages')


def now():
    return subprocess.check_output(['date', '+%Y-%m-%d %H:%M:%S %Z'], text=True).strip()


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


res = {'started_at_pt': now(), 'steps': [], 'supersedes': 'gcdcqs20-lean-parent-audit-v1 (retained): its line-based token scan matched the words native_decide/ofReduceBool inside doc comments stating they are NOT used, and stopped before building. v2 strips Lean comments before scanning and reports comment mentions separately; the #print axioms check remains the definitive guard.'}
manifest = json.loads((WORKER / 'manifest.json').read_text())
files = manifest['files']
res['worker_manifest_sha256'] = sha(WORKER / 'manifest.json')
res['pins'] = {k: sha(WORKER / k) == v for k, v in files.items()}
raw = {'gcdcqs20-parent-inputs-v1/gcdcqs20-e1s1_p10.txt': '58b51b50b5281df613c5fae0a3b0178a374554a2f062e55bd8fc25250922a0ca',
       'mcdsqs80-parent-inputs-v1/mcdsqs80_c21_A.txt': '49f500c5eedd9a79553e1228d0232e203a749bbda04e3a891c52778dbe9d44a3'}
res['raw_pins'] = {k: sha(REVIEW / k) == v for k, v in raw.items()}
ok = all(res['pins'].values()) and all(res['raw_pins'].values())

# Build closure of Gc80.Audit80 in dependency order (from the import graph read by the parent).
order = ['McdKernel/Target', 'McdKernel/Check', 'McdKernel/Counts', 'Gc80/GcTarget', 'Gc80/Derived',
         'Gc80/Check80', 'Gc80/Counts79']
order += ['Gc80/Data%s%s' % (c, s) for c in ('Gc', 'Mc') for s in ['B'] + ['P%d' % i for i in range(8)]]
order += ['Gc80/DataGc', 'Gc80/DataMc']
order += ['Gc80/Cert%sPts%d' % (c, i) for c in ('Mc', 'Gc') for i in range(4)]
order += ['Gc80/CertMc', 'Gc80/CertGc', 'Gc80/Audit80']
res['build_order'] = order
(HERE / 'src' / 'McdKernel').mkdir(parents=True)
(HERE / 'src' / 'Gc80').mkdir()
for m in order:
    if m + '.lean' not in files:
        ok = False
        res['missing_from_manifest'] = m
        break
    shutil.copyfile(WORKER / (m + '.lean'), HERE / 'src' / (m + '.lean'))
shutil.copyfile(HERE / 'ParentAudit.lean', HERE / 'src' / 'ParentAudit.lean')
for n in ['NegHoleFree11', 'NegColours41']:
    shutil.copyfile(HERE / (n + '.lean'), HERE / 'src' / (n + '.lean'))
res['parent_file_sha256'] = {n: sha(HERE / n) for n in ['ParentAudit.lean', 'NegHoleFree11.lean',
                                                         'NegColours41.lean', 'parent_replay.py']}


def run(name, cmd, cwd, env=None):
    t0 = time.monotonic()
    p = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)
    row = {'name': name, 'exit_code': p.returncode, 'wall_seconds': round(time.monotonic() - t0, 3),
           'stdout_tail': p.stdout[-1200:], 'stderr_tail': p.stderr[-1200:]}
    res['steps'].append(row)
    with (HERE / 'steps.jsonl').open('a') as f:
        f.write(json.dumps({'at': now(), 'name': name, 'exit_code': p.returncode,
                            'wall_seconds': row['wall_seconds']}) + '\n')
    return p


# Regenerate data modules from the parent-pinned raw certificates and compare bytes.
if ok:
    env = dict(os.environ, GC80_REVIEW=str(REVIEW), PYTHONDONTWRITEBYTECODE='1')
    p = run('regenerate-data', ['/usr/bin/python3', '-B', str(WORKER / 'gen_lean80.py'), str(HERE / 'regen')],
            HERE, env)
    regen = sorted((HERE / 'regen' / 'Gc80').glob('Data*.lean'))
    res['regenerated'] = {f.name: f.read_bytes() == (WORKER / 'Gc80' / f.name).read_bytes() for f in regen}
    ok = p.returncode == 0 and len(regen) == 20 and all(res['regenerated'].values())

patterns = [r'\bsorry\b', r'\badmit\b', r'native_decide', r'ofReduceBool', r'ofReduceNat', r'implemented_by',
            r'\bextern\b', r'\bunsafe\b', r'^\s*axiom\b', r'\bopaque\b', r'csimp', r'\bmacro\b', r'\bsyntax\b',
            r'\belab\b', r'\bnotation\b', r'run_cmd', r'#eval', r'skipKernelTC', r'import\s+Lean\b', r'debug\.',
            r'Lean\.Elab']
def strip_comments(text):
    """Blank Lean comments (nested /- -/ and -- line comments) outside string literals; keep newlines."""
    out, i, depth, n = [], 0, 0, len(text)
    while i < n:
        two = text[i:i + 2]
        if depth == 0 and text[i] == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == '\\' else 1
            out.append(text[i:j + 1])
            i = j + 1
        elif two == '/-':
            depth += 1
            out.append('  ')
            i += 2
        elif depth and two == '-/':
            depth -= 1
            out.append('  ')
            i += 2
        elif depth:
            out.append('\n' if text[i] == '\n' else ' ')
            i += 1
        elif two == '--':
            j = text.find('\n', i)
            j = n if j < 0 else j
            out.append(' ' * (j - i))
            i = j
        else:
            out.append(text[i])
            i += 1
    return ''.join(out)


res['scan'] = {}
for f in sorted((HERE / 'src').rglob('*.lean')):
    if f.name.startswith('Neg'):
        continue
    raw_lines = f.read_text().split('\n')
    code_lines = strip_comments(f.read_text()).split('\n')
    res['scan'][str(f.relative_to(HERE / 'src'))] = {
        'forbidden_hits': [(i + 1, q) for i, line in enumerate(code_lines) for q in patterns if re.search(q, line)],
        'comment_mentions': [(i + 1, q) for i, line in enumerate(raw_lines) for q in patterns
                             if re.search(q, line) and not re.search(q, code_lines[i])],
        'set_options': [(i + 1, line.strip()) for i, line in enumerate(code_lines) if 'set_option' in line]}
ok = ok and not any(v['forbidden_hits'] for v in res['scan'].values())

lean_path = str(HERE / 'build') + ''.join(':' + str(CACHE / p / '.lake/build/lib/lean') for p in
                                          ['mathlib', 'batteries', 'aesop', 'Qq', 'proofwidgets', 'plausible',
                                           'LeanSearchClient', 'importGraph'])
lenv = dict(os.environ, LEAN_PATH=lean_path)
(HERE / 'logs').mkdir(exist_ok=True)


def build(mod):
    out = HERE / 'build' / (mod + '.olean')
    out.parent.mkdir(parents=True, exist_ok=True)
    p = run('build-' + mod, ['/usr/bin/time', '-l', str(TOOLCHAIN / 'bin/lean'), '-j', '1', '-R', '.', '-o', str(out),
                             '-i', str(HERE / 'build' / (mod + '.ilean')), mod + '.lean'], HERE / 'src', lenv)
    (HERE / 'logs' / (mod.replace('/', '__') + '.log')).write_text(p.stdout + '\n--- stderr ---\n' + p.stderr)
    return p


for m in order + ['ParentAudit']:
    if ok:
        ok = build(m).returncode == 0
res['negatives'] = {}
if ok:
    for n in ['NegHoleFree11', 'NegColours41']:
        p = build(n)
        text = (p.stdout + p.stderr).lower()
        res['negatives'][n] = {'exit_code': p.returncode, 'type_mismatch_reported': 'type mismatch' in text,
                               'olean_written': (HERE / 'build' / (n + '.olean')).exists()}
    ok = all(v['exit_code'] != 0 and v['type_mismatch_reported'] and not v['olean_written']
             for v in res['negatives'].values())
if ok:
    p = run('fresh-ParentAudit', ['/usr/bin/time', '-l', str(TOOLCHAIN / 'bin/leanchecker'), '--fresh', '-v',
                                  'ParentAudit'], HERE / 'src', lenv)
    res['fresh_output_tail'] = (p.stdout + p.stderr)[-2500:]
    ok = p.returncode == 0 and 'replaying ParentAudit with --fresh' in p.stdout + p.stderr
alog = HERE / 'logs' / 'ParentAudit.log'
ax = re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", alog.read_text()) if alog.exists() else []
res['axioms'] = {k: [a.strip() for a in v.split(',')] for k, v in ax}
expected = {'ParentGc80Audit.pGroups_eq', 'ParentGc80Audit.chi79', 'ParentGc80Audit.gc80',
            'ParentGc80Audit.gc80_parameters', 'ParentGc80Audit.mc80'}
res['axioms_ok'] = set(res['axioms']) == expected and all(
    set(v) <= {'propext', 'Classical.choice', 'Quot.sound'} for v in res['axioms'].values())
res['status'] = 'PARENT_GC80_BINDING_REBUILD_AND_FRESH_KERNEL_PASS' if ok and res['axioms_ok'] else 'FAIL'
res['finished_at_pt'] = now()
res['limits'] = ('One Lean 4.34.1 kernel implementation for lean and leanchecker; read-only prebuilt Mathlib cache; '
                 'not Comparator. Existence roots do not depend on the literal binding to the raw files; the data '
                 'regeneration check binds them.')
with OUT.open('x') as f:
    json.dump(res, f, indent=2)
    f.write('\n')
print(res['status'])
raise SystemExit(0 if res['status'].endswith('_PASS') else 1)
