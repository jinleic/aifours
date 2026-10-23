#!/usr/bin/env python3
"""Clean-directory rebuild and fresh kernel replay of the cyclic (v, 5, 1) CDF certificates.

Usage:
  python3 -B replay.py --write-manifest   # once, by the worker: pin every source by SHA-256
  python3 -B replay.py TAG                # creates replay-TAG/ next to this file; refuses to overwrite

A replay writes only inside replay-TAG/ (build/, logs/, regenerated/, result.json); the Lean
4.34.1 toolchain and the prebuilt Mathlib cache are used read-only through lean_env.sh.  Every
Lean process runs alone (one process at a time, CDF_THREADS=1).  Steps:

 1. pinned files: every file in manifest.json has its recorded SHA-256 (sources, scripts, inputs);
    each raw certificate also matches the SHA-256 in its parent input manifest;
 2. lean_source_scan.py (byte-identical copy of the LKTS kernel scanner) passes its own controls,
    and no Lean source has any hit (sorry, admit, axiom, native_decide, +native, ofReduceBool,
    implemented_by, extern, unsafe, skipKernelTC, csimp, opaque, partial, addDecl, meta code,
    run_cmd/#eval, import Lean, maxHeartbeats 0);
 3. raw -> Lean binding: gen_lean.py regenerates Data{v}.lean and Cert{v}.lean and gen_controls.py
    regenerates Controls*.lean byte-identically; separately, an independent regex reader checks
    that the block literals, header pair and SHA string of every Data{v}.lean equal the raw file;
 4. every module is compiled into replay-TAG/build in dependency order;
 5. every `#print axioms` line of every build log is within {propext, Classical.choice,
    Quot.sound}, and the root and audit types are printed verbatim as expected;
 6. leanchecker --fresh replays CdfKernel.Audit (orders 321, 501, 621, 681), CdfKernel.Audit801,
    CdfKernel.Audit901 and CdfKernel.All (everything, including facts, bridges and controls);
 7. replay-TAG/result.json records hashes, times, peak RSS and the printed target definitions.
"""
from datetime import datetime
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import time
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
ORDERS = {321: 16, 501: 25, 621: 31, 681: 34, 801: 40, 901: 45}
RAW = {v: f'cdf{v}-parent-inputs-v1/cdf_{v}.txt' for v in ORDERS}
MODULES = ['Target', 'Generic',
           'Data321', 'Cert321', 'Data501', 'Cert501', 'Data621', 'Cert621', 'Data681', 'Cert681',
           'Audit', 'Data801', 'Cert801', 'Audit801', 'Data901', 'Cert901', 'Audit901',
           'Facts', 'Bridge', 'Mutations', 'Controls', 'Controls801', 'Controls901', 'All']
FRESH = ['CdfKernel.Audit', 'CdfKernel.Audit801', 'CdfKernel.Audit901', 'CdfKernel.All']
AUDIT_OF = {321: 'Audit', 501: 'Audit', 621: 'Audit', 681: 'Audit', 801: 'Audit801', 901: 'Audit901'}
SCRIPTS = ['gen_lean.py', 'gen_controls.py', 'lean_env.sh', 'build_module.sh', 'lean_source_scan.py',
           'replay.py']
TOOLCHAIN = Path('/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1/bin')
MATHLIB_OLEAN = Path('/private/tmp/seymour-lean-20261014-68365/.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean')


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def write_manifest():
    path = HERE / 'manifest.json'
    require(not path.exists(), 'Refusing to overwrite manifest.json')
    files = {f'CdfKernel/{m}.lean': sha256(HERE / 'CdfKernel' / f'{m}.lean') for m in MODULES}
    files.update({name: sha256(HERE / name) for name in SCRIPTS})
    inputs = {f'review/{rel}': sha256(REVIEW / rel) for rel in RAW.values()}
    manifest = {'recorded_at_pt': stamp(), 'files': files, 'raw_inputs': inputs,
                'scanner_origin': {'path': 'review/lkts-kernel-parent-replay-v1/lean_source_scan.py',
                                   'sha256': sha256(REVIEW / 'lkts-kernel-parent-replay-v1' / 'lean_source_scan.py')}}
    with path.open('x') as stream:
        json.dump(manifest, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'manifest': str(path), 'sha256': sha256(path)}))


def run(command, name, out_dir, steps, env, timeout=1800):
    started = time.monotonic()
    stdout = out_dir / 'logs' / f'{name}.stdout.txt'
    stderr = out_dir / 'logs' / f'{name}.stderr.txt'
    with stdout.open('x') as out, stderr.open('x') as err:
        proc = subprocess.Popen(command, cwd=HERE, stdin=subprocess.DEVNULL, stdout=out, stderr=err,
                                env=env, start_new_session=True)
        timed_out = False
        try:
            code = proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(proc.pid, signal.SIGTERM)
            code = proc.wait(timeout=30)
    item = {'step': name, 'command': command, 'exit_code': code, 'timeout': timed_out,
            'wall_seconds': round(time.monotonic() - started, 3),
            'stdout': str(stdout.relative_to(HERE)), 'stderr': str(stderr.relative_to(HERE))}
    steps.append(item)
    print(json.dumps({'step': name, 'exit_code': code, 'wall_seconds': item['wall_seconds']}), flush=True)
    require(code == 0 and not timed_out, f'{name} did not complete successfully')
    return stdout.read_text(), stderr.read_text(), item


def time_metrics(text):
    real = re.search(r'([0-9.]+) real', text)
    rss = re.search(r'([0-9]+)\s+maximum resident set size', text)
    return {'real_seconds': float(real.group(1)) if real else None,
            'max_rss_bytes': int(rss.group(1)) if rss else None}


def read_lean_data(path, v):
    """Independent reader of a generated Data module (does not use gen_lean.py)."""
    text = Path(path).read_text()
    sha = re.search(rf'def data{v}RawSha256 : String := "([0-9a-f]{{64}})"', text)
    head = re.search(rf'def data{v}Header : Nat × Nat := \((\d+), (\d+)\)', text)
    body = re.search(rf'def data{v} : List \(List Nat\) := \[\n(.*?)\n\]\n', text, re.S)
    require(sha and head and body, f'Data{v}.lean: unexpected layout')
    rows = [[int(x) for x in re.fullmatch(r'\s*\[([0-9, ]*)\],?', line).group(1).split(', ')]
            for line in body.group(1).split('\n')]
    return sha.group(1), (int(head.group(1)), int(head.group(2))), rows


def read_raw(path):
    """Independent reader of a raw certificate (does not use gen_lean.py)."""
    lines = Path(path).read_bytes().decode('ascii').splitlines()
    head = lines[0].split()
    require(len(head) == 3 and head[0] == 'CDF', f'{path}: bad header')
    return (int(head[1]), int(head[2])), [[int(x) for x in line.split()] for line in lines[1:]]


def parse_axioms(log):
    axioms = {name: sorted(x.strip() for x in listed.split(',') if x.strip())
              for name, listed in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log)}
    for name in re.findall(r"'([^']+)' does not depend on any axioms", log):
        axioms[name] = []
    return axioms


def main(tag):
    require(re.fullmatch(r'[A-Za-z0-9_-]+', tag), 'TAG must be alphanumeric')
    out = HERE / f'replay-{tag}'
    out.mkdir(exist_ok=False)
    for sub in ['build', 'logs', 'regenerated']:
        (out / sub).mkdir()
    env = dict(os.environ, CDF_BUILD=str(out / 'build'), CDF_LOGS=str(out / 'logs'), CDF_THREADS='1')
    result = {'status': 'FAILED', 'tag': tag, 'started_at_pt': stamp(), 'steps': [],
              'driver_sha256': sha256(__file__),
              'trust_limits': [
                  'Same Lean 4.34.1 kernel implementation (lean and leanchecker of one toolchain); not Comparator, not an independent kernel.',
                  'Prebuilt Mathlib d13f23b oleans from the read-only cache are trusted as compiled artifacts for elaboration; leanchecker --fresh re-checks every imported declaration, Mathlib included, in a fresh kernel environment.',
                  'decide +kernel proofs are kernel reductions with GMP-accelerated Nat literals (part of the trusted kernel); no native code evaluation, no Lean.ofReduceBool.',
                  'The meaning of the roots rests on the reviewer reading CdfKernel/Target.lean (Cdf.diffs, Cdf.IsCDF, Cdf.Target).',
                  'The raw-to-literal binding is checked by a Python generator and an independent Python reader, not inside Lean.']}
    result_path = out / 'result.json'
    try:
        manifest = json.loads((HERE / 'manifest.json').read_text())
        result['manifest_sha256'] = sha256(HERE / 'manifest.json')
        for rel, digest in manifest['files'].items():
            require(sha256(HERE / rel) == digest, f'Pinned file changed: {rel}')
        require(set(manifest['files']) == {f'CdfKernel/{m}.lean' for m in MODULES} | set(SCRIPTS),
                'Manifest does not list exactly the expected files')
        require(sorted(p.name for p in (HERE / 'CdfKernel').glob('*.lean')) ==
                sorted(f'{m}.lean' for m in MODULES), 'Unexpected Lean file in CdfKernel/')
        inputs = {}
        for v, rel in RAW.items():
            raw = REVIEW / rel
            digest = sha256(raw)
            require(manifest['raw_inputs'][f'review/{rel}'] == digest, f'Raw input changed: {rel}')
            parent = json.loads((raw.parent / 'manifest.json').read_text())
            entry = parent.get('witnesses', parent).get(raw.name)
            require(entry and entry['sha256'] == digest, f'Parent manifest disagrees for {rel}')
            inputs[str(v)] = {'path': f'review/{rel}', 'sha256': digest, 'bytes': raw.stat().st_size,
                              'parent_manifest_sha256_match': True}
        result['inputs'] = inputs
        spec = importlib.util.spec_from_file_location('cdf_lean_scan', HERE / 'lean_source_scan.py')
        scanner = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(scanner)
        scan = {'scanner_sha256': sha256(HERE / 'lean_source_scan.py'), 'controls': scanner.controls(), 'files': {}}
        require(scan['controls']['positive_ok'] and scan['controls']['negative_ok'], 'Scanner controls failed')
        for module in MODULES:
            path = HERE / 'CdfKernel' / f'{module}.lean'
            hits, _, imports = scanner.scan_text(path.read_text())
            require(not hits, f'Forbidden Lean construct in {module}: {hits}')
            scan['files'][module] = {'sha256': sha256(path), 'hits': hits, 'imports': imports}
        result['source_scan'] = scan
        version, _, _ = run(['sh', '-c', '. ./lean_env.sh; exec "$LEAN" --version'], 'lean-version', out,
                            result['steps'], env)
        result['toolchain'] = {'lean_version': version.strip(),
                               'lean_sha256': sha256(TOOLCHAIN / 'lean'),
                               'leanchecker_sha256': sha256(TOOLCHAIN / 'leanchecker'),
                               'mathlib_olean_sha256': sha256(MATHLIB_OLEAN),
                               'mathlib_rev': 'd13f23b723b8a846827a245b89c10fc7d3f11612'}
        binding = {}
        for v, rel in RAW.items():
            raw = REVIEW / rel
            run([sys.executable, '-B', 'gen_lean.py', str(raw), str(out / 'regenerated'), '--v', str(v),
                 '--expect-sha256', inputs[str(v)]['sha256'], '--label', f'review/{rel}'],
                f'generate{v}', out, result['steps'], env)
            for kind in ['Data', 'Cert']:
                require((out / 'regenerated' / f'{kind}{v}.lean').read_bytes() ==
                        (HERE / 'CdfKernel' / f'{kind}{v}.lean').read_bytes(), f'{kind}{v}.lean is not regenerated byte-identically')
            lean_sha, lean_head, lean_rows = read_lean_data(HERE / 'CdfKernel' / f'Data{v}.lean', v)
            raw_head, raw_rows = read_raw(raw)
            require(lean_sha == inputs[str(v)]['sha256'], f'SHA string mismatch for {v}')
            require(lean_head == raw_head == (v, 5), f'Header mismatch for {v}')
            require(lean_rows == raw_rows and len(raw_rows) == ORDERS[v] and all(len(r) == 5 for r in raw_rows),
                    f'Block literal mismatch for {v}')
            binding[str(v)] = {'regenerated_byte_identical': ['Data', 'Cert'], 'independent_reader_match': True,
                               'blocks': len(raw_rows), 'data_lean_sha256': sha256(HERE / 'CdfKernel' / f'Data{v}.lean'),
                               'cert_lean_sha256': sha256(HERE / 'CdfKernel' / f'Cert{v}.lean')}
        controls_out, _, _ = run([sys.executable, '-B', 'gen_controls.py', str(out / 'regenerated')],
                                 'generate-controls', out, result['steps'], env)
        for name in ['Controls', 'Controls801', 'Controls901']:
            require((out / 'regenerated' / f'{name}.lean').read_bytes() ==
                    (HERE / 'CdfKernel' / f'{name}.lean').read_bytes(), f'{name}.lean is not regenerated byte-identically')
        result['data_binding'] = binding
        result['generator_parser_controls'] = json.loads(controls_out)['parser_controls']
        builds, axioms, printed = {}, {}, {}
        for module in MODULES:
            _, _, item = run(['sh', 'build_module.sh', f'CdfKernel/{module}.lean'], f'build-{module}', out,
                             result['steps'], env)
            log = (out / 'logs' / f'{module}.build.log').read_text()
            timing = (out / 'logs' / f'{module}.build.time').read_text()
            require(not re.search(r':\d+:\d+: error', log), f'Error message in build log of {module}')
            builds[module] = {**time_metrics(timing), 'warnings': len(re.findall(r':\d+:\d+: warning', log)),
                              'olean_sha256': sha256(out / 'build' / 'CdfKernel' / f'{module}.olean')}
            found = parse_axioms(log)
            for name, listed in found.items():
                require(set(listed) <= ALLOWED_AXIOMS, f'Unexpected axiom for {name}: {listed}')
            if found:
                axioms[module] = found
            if module in ('Audit', 'Audit801', 'Audit901', 'Bridge'):
                printed[module] = log
        for v, n in ORDERS.items():
            root = f'Cdf.Kernel.exists_cdf{v}'
            cert_log = (out / 'logs' / f'Cert{v}.build.log').read_text()
            require(f'{root} : ∃ (B : Fin {n} → Fin 5 → Fin {v}), Cdf.IsCDF B' in cert_log, f'Missing root type for {v}')
            require(root in axioms[f'Cert{v}'], f'Missing axiom report for {root}')
            audit_log = printed[AUDIT_OF[v]]
            require(f'Cdf.Audit.target{v} : Cdf.Target {v}' in audit_log, f'Missing audit type for {v}')
            require(f'Cdf.Audit.target{v}' in axioms[AUDIT_OF[v]], f'Missing audit axiom report for {v}')
        result['builds'] = builds
        result['axioms'] = axioms
        result['printed_audit_output'] = printed
        fresh = {}
        for module in FRESH:
            stdout, stderr, item = run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v "$1"',
                                        'fresh', module], f'fresh-{module}', out, result['steps'], env, timeout=3600)
            require(f'replaying {module} with --fresh' in stdout, f'No replay marker for {module}')
            fresh[module] = {**time_metrics(stderr), 'exit_code': item['exit_code'], 'wall_seconds': item['wall_seconds']}
        result['fresh_replay'] = fresh
        result['roots'] = {str(v): {'root': f'Cdf.Kernel.exists_cdf{v}',
                                    'type': f'∃ (B : Fin {n} → Fin 5 → Fin {v}), Cdf.IsCDF B',
                                    'audit': f'Cdf.Audit.target{v} : Cdf.Target {v}',
                                    'axioms': axioms[f'Cert{v}'][f'Cdf.Kernel.exists_cdf{v}'],
                                    'fresh_replay_module': f'CdfKernel.{AUDIT_OF[v]}'} for v, n in ORDERS.items()}
        result['status'] = 'REBUILD_AND_FRESH_KERNEL_REPLAY_PASS'
    except Exception as exc:
        result['error'] = f'{type(exc).__name__}: {exc}'
    finally:
        result['finished_at_pt'] = stamp()
        with result_path.open('x') as stream:
            json.dump(result, stream, indent=2, ensure_ascii=False)
            stream.write('\n')
        print(json.dumps({'status': result['status'], 'result': str(result_path), 'error': result.get('error')},
                         indent=2), flush=True)
    return 0 if result['status'] == 'REBUILD_AND_FRESH_KERNEL_REPLAY_PASS' else 1


if __name__ == '__main__':
    if sys.argv[1:] == ['--write-manifest']:
        write_manifest()
        raise SystemExit(0)
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1]))
