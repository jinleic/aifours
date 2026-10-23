#!/usr/bin/env python3
"""replay.py -- clean-directory rebuild and fresh kernel replay of the Lean 4 proof that BTD(12,15;6,2,10;8,6)
does not exist (lane btd12-15, formalization of notes/nonexistence-proof-r2.md).

Usage (from anywhere; paths are relative to this file):
  /usr/bin/python3 -B replay.py --write-manifest     pin every source/script/toolchain file (manifest.json, exclusive)
  /usr/bin/python3 -B replay.py TAG                  replay into replay-TAG/ (refuses an existing directory)

A replay writes only inside replay-TAG/ (build/, logs/, scan.json, result.json).  The Lean 4.34.1 toolchain and the
prebuilt Mathlib cache are used read-only through lean_env.sh.  One Lean process at a time, BTD_THREADS=1.
No process is killed, no subprocess timeout is used.  Steps:
 1. every pinned file has its recorded SHA-256 and BTDKernel/ contains exactly the pinned Lean files;
 2. lean_source_scan.py (byte-identical copy of the parent-lane scanner) passes its controls and reports no hit
    (sorry, admit, axiom, native_decide, +native, ofReduceBool, implemented_by, extern, unsafe, skipKernelTC, csimp,
    opaque, partial, addDecl, meta code, run_cmd/#eval, import Lean, maxHeartbeats 0) in any Lean source;
 3. Target, Proof, Controls, Audit are compiled into replay-TAG/build in this order; every build exits 0 with no
    error line; every `#print axioms` line lists only propext, Classical.choice, Quot.sound; the Audit log contains the
    explicit root statement;
 4. negative control: ControlFail must FAIL (nonzero exit, the expected error messages, no olean written);
 5. `leanchecker --fresh -v` replays BTDKernel.Audit and BTDKernel.Controls, i.e. their whole import closure
    (Mathlib included), in a fresh kernel environment; both must exit 0 with the replay marker;
 6. replay-TAG/result.json records hashes, times, peak RSS, exit codes and the axiom reports; verdict PASS or FAIL.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLCHAIN = Path('/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1/bin')
MATHLIB = Path('/private/tmp/seymour-lean-20261014-68365/.lake/packages/mathlib/.lake/build/lib/lean')
MATHLIB_OLEANS = ['Mathlib.olean', 'Mathlib/LinearAlgebra/Matrix/SchurComplement.olean',
                  'Mathlib/LinearAlgebra/Matrix/Determinant/Basic.olean',
                  'Mathlib/Algebra/Order/BigOperators/Ring/Finset.olean', 'Mathlib/Tactic.olean']
MODULES = ['Target', 'Proof', 'Controls', 'Audit']
NEGATIVE = 'ControlFail'
FRESH = ['BTDKernel.Audit', 'BTDKernel.Controls']
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
SCRIPTS = ['lean_env.sh', 'build_module.sh', 'lean_source_scan.py', 'replay.py']
NEGATIVE_EXPECT = [r"Tactic `decide` proved that the proposition\s+∀ \(i : Fin 3\), \{j \| M3bad1 i j = 1\}\.card = 1\s+is false",
                   r"ControlFail\.lean:\d+:\d+: error: unsolved goals\s+⊢ False"]
ROOT_EXPECT = ['BTD12.Audit.root : ¬∃ M,', '(∀ (i : Fin 12) (j : Fin 15), M i j = 0 ∨ M i j = 1 ∨ M i j = 2) ∧',
               '(∀ (i : Fin 12), {j | M i j = 1}.card = 6) ∧', '(∀ (i : Fin 12), {j | M i j = 2}.card = 2) ∧',
               '(∀ (j : Fin 15), ∑ i, M i j = 8) ∧ ∀ (i k : Fin 12), i ≠ k → ∑ j, M i j * M k j = 6']


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 22), b''):
            h.update(chunk)
    return h.hexdigest()


def pinned_paths():
    files = {f'BTDKernel/{m}.lean': HERE / 'BTDKernel' / f'{m}.lean' for m in MODULES + [NEGATIVE]}
    files.update({s: HERE / s for s in SCRIPTS})
    files.update({f'toolchain/{b}': TOOLCHAIN / b for b in ('lean', 'leanchecker')})
    files.update({f'mathlib/{o}': MATHLIB / o for o in MATHLIB_OLEANS})
    return files


def write_manifest():
    out = HERE / 'manifest.json'
    data = {'created_host': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            'files': {k: sha256(p) for k, p in pinned_paths().items()}}
    with open(out, 'x') as f:
        json.dump(data, f, indent=1)
        f.write('\n')
    print(json.dumps(data, indent=1))
    return 0


def run(cmd, env, cwd, log_prefix):
    t0 = time.time()
    p = subprocess.run(cmd, env=env, cwd=cwd, capture_output=True, text=True)
    el = time.time() - t0
    with open(f'{log_prefix}.stdout', 'x') as f:
        f.write(p.stdout)
    with open(f'{log_prefix}.stderr', 'x') as f:
        f.write(p.stderr)
    return p, el


def rss_and_real(text):
    rss = re.search(r'(\d+)\s+maximum resident set size', text)
    real = re.search(r'([\d.]+)\s+real', text)
    return (int(rss.group(1)) if rss else None, float(real.group(1)) if real else None)


def replay(tag):
    out = HERE / f'replay-{tag}'
    out.mkdir()
    build, logs = out / 'build', out / 'logs'
    build.mkdir()
    logs.mkdir()
    result = {'tag': tag, 'started_host': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'checks': {}, 'builds': {},
              'fresh': {}, 'axioms': {}}
    ok = True

    def check(name, cond, detail=None):
        nonlocal ok
        result['checks'][name] = {'ok': bool(cond), 'detail': detail}
        ok &= bool(cond)

    # 1. pins
    manifest = json.loads((HERE / 'manifest.json').read_text())
    bad = [k for k, p in pinned_paths().items() if sha256(p) != manifest['files'].get(k)]
    check('pinned_files_match', not bad, bad)
    lean_files = sorted(p.name for p in (HERE / 'BTDKernel').glob('*.lean'))
    check('btdkernel_contains_exactly_pinned', lean_files == sorted(f'{m}.lean' for m in MODULES + [NEGATIVE]), lean_files)
    result['manifest_sha256'] = sha256(HERE / 'manifest.json')
    # 2. scan
    scan = subprocess.run([sys.executable, '-B', str(HERE / 'lean_source_scan.py')] +
                          [str(HERE / 'BTDKernel' / f'{m}.lean') for m in MODULES + [NEGATIVE]],
                          capture_output=True, text=True)
    with open(out / 'scan.json', 'x') as f:
        f.write(scan.stdout)
    rep = json.loads(scan.stdout)
    check('source_scan_clean', scan.returncode == 0 and rep['clean'],
          {k: v['forbidden_hits'] for k, v in rep['files'].items() if v['forbidden_hits']})
    # 3. builds
    env = dict(os.environ, BTD_BUILD=str(build), BTD_LOGS=str(logs), BTD_THREADS='1')
    for m in MODULES:
        p, el = run(['sh', str(HERE / 'build_module.sh'), f'BTDKernel/{m}.lean'], env, str(HERE), str(logs / f'{m}.driver'))
        log = (logs / f'{m}.build.log').read_text()
        tm = (logs / f'{m}.build.time').read_text()
        rss, real = rss_and_real(tm)
        errors = [line for line in log.split('\n') if ': error' in line]
        axioms = re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log)
        ax = {name: sorted(a.strip() for a in lst.split(',') if a.strip()) for name, lst in axioms}
        result['axioms'].update(ax)
        result['builds'][m] = {'exit': p.returncode, 'errors': errors, 'peak_rss_bytes': rss, 'real_s': real,
                               'log_sha256': sha256(logs / f'{m}.build.log'),
                               'olean_sha256': sha256(build / 'BTDKernel' / f'{m}.olean')
                               if (build / 'BTDKernel' / f'{m}.olean').exists() else None}
        check(f'build_{m}', p.returncode == 0 and not errors, errors[:5])
        if ax:
            check(f'axioms_{m}', all(set(v) <= ALLOWED_AXIOMS for v in ax.values()), ax)
        if m == 'Audit':
            check('audit_root_statement_explicit', all(s in log for s in ROOT_EXPECT))
            check('audit_root_axioms', ax.get('BTD12.Audit.root') == sorted(ALLOWED_AXIOMS), ax.get('BTD12.Audit.root'))
    # 4. negative control
    p, el = run(['sh', str(HERE / 'build_module.sh'), f'BTDKernel/{NEGATIVE}.lean'], env, str(HERE),
                str(logs / f'{NEGATIVE}.driver'))
    log = (logs / f'{NEGATIVE}.build.log').read_text()
    result['builds'][NEGATIVE] = {'exit': p.returncode, 'log_sha256': sha256(logs / f'{NEGATIVE}.build.log'),
                                  'olean_written': (build / 'BTDKernel' / f'{NEGATIVE}.olean').exists()}
    check('negative_control_fails_as_intended',
          p.returncode != 0 and all(re.search(rx, log) for rx in NEGATIVE_EXPECT)
          and not (build / 'BTDKernel' / f'{NEGATIVE}.olean').exists())
    # 5. fresh kernel replay
    for mod in FRESH:
        p, el = run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v "$1"', 'fresh', mod],
                    env, str(HERE), str(logs / f'fresh-{mod}'))
        rss, real = rss_and_real(p.stderr)
        marker = f'replaying {mod} with --fresh' in p.stdout
        result['fresh'][mod] = {'exit': p.returncode, 'marker': marker, 'wall_s': round(el, 1), 'peak_rss_bytes': rss,
                                'stdout_sha256': sha256(logs / f'fresh-{mod}.stdout')}
        check(f'fresh_{mod}', p.returncode == 0 and marker)
    result['ended_host'] = time.strftime('%Y-%m-%dT%H:%M:%S%z')
    result['verdict'] = 'PASS' if ok else 'FAIL'
    with open(out / 'result.json', 'x') as f:
        json.dump(result, f, indent=1)
        f.write('\n')
    print(json.dumps({k: v['ok'] for k, v in result['checks'].items()}, indent=1))
    print('VERDICT', result['verdict'])
    return 0 if ok else 1


def main(argv):
    if len(argv) == 2 and argv[1] == '--write-manifest':
        return write_manifest()
    if len(argv) == 2 and re.fullmatch(r'[A-Za-z0-9_-]+', argv[1]):
        return replay(argv[1])
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv))
