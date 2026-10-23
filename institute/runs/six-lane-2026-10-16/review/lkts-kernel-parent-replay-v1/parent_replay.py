"""Rebind raw LKTS data, rebuild a pinned snapshot, and replay both roots in fresh kernels."""
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
MODULES = ['PriorFormal', 'Generic', 'Data57', 'Cert57', 'Data87', 'Cert87']
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def run(command, name, results, timeout=900):
    started = time.monotonic()
    stdout = HERE / 'parent-logs' / f'{name}.stdout.txt'
    stderr = HERE / 'parent-logs' / f'{name}.stderr.txt'
    with stdout.open('x') as out, stderr.open('x') as err:
        proc = subprocess.Popen(command, cwd=HERE, stdin=subprocess.DEVNULL,
                                stdout=out, stderr=err, start_new_session=True)
        timed_out = False
        try:
            code = proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(proc.pid, signal.SIGTERM)
            code = proc.wait(timeout=30)
    item = {'command': command, 'exit_code': code, 'timeout': timed_out,
            'wall_seconds': round(time.monotonic() - started, 3),
            'stdout': str(stdout.relative_to(HERE)), 'stderr': str(stderr.relative_to(HERE))}
    results.append(item)
    print(json.dumps({'step': name, 'exit_code': code, 'wall_seconds': item['wall_seconds']}), flush=True)
    require(code == 0 and not timed_out, f'{name} did not complete successfully')
    return stdout.read_text()


def main():
    result_path = HERE / 'parent-result.json'
    require(not result_path.exists(), 'Refusing to overwrite an earlier parent result')
    (HERE / 'parent-logs').mkdir(exist_ok=False)
    (HERE / 'regenerated').mkdir(exist_ok=False)
    result = {'status': 'FAILED', 'started_at_pt': stamp(), 'steps': [],
              'driver_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'limit': 'Same Lean kernel implementation in a new process, not Comparator or an independent kernel. Worker mutation controls are preserved, not rerun here.'}
    try:
        manifest = json.loads((HERE / 'manifest.json').read_text())
        for relative, entry in manifest['files'].items():
            require(hashlib.sha256((HERE / relative).read_bytes()).hexdigest() == entry['sha256'],
                    f'Pinned file changed: {relative}')
        result['manifest_sha256'] = hashlib.sha256((HERE / 'manifest.json').read_bytes()).hexdigest()
        spec = importlib.util.spec_from_file_location('parent_lean_scan', HERE / 'lean_source_scan.py')
        scanner = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(scanner)
        scan = {'controls': scanner.controls(), 'files': {}}
        require(scan['controls']['positive_ok'] and scan['controls']['negative_ok'], 'Scanner controls failed')
        for module in MODULES:
            path = HERE / 'LktsKernel' / f'{module}.lean'
            hits, declarations, imports = scanner.scan_text(path.read_text())
            disallowed = {key: lines for key, lines in hits.items() if key != 'heartbeats_zero'}
            require(not disallowed, f'Forbidden Lean escape in {module}: {disallowed}')
            scan['files'][module] = {'hits': hits, 'imports': imports,
                                     'allowed_only': 'maxHeartbeats 0 changes elaboration limits, not kernel trust' if hits else None}
        result['source_scan'] = scan
        result['toolchain'] = run(['sh', '-c', '. ./lean_env.sh; exec "$LEAN" --version'],
                                  'lean-version', result['steps']).strip()
        worker = json.loads((HERE / 'result.json').read_text())
        result['data_binding'] = {}
        for v, label in [(57, 'review/lkts57-construction-snapshot-v1/lkts57_g513.txt'),
                         (87, 'review/lkts87-parent-inputs-v1/lkts87_g903.txt')]:
            sha = worker['inputs_sha256'][f'lkts{v}']
            generated = f'regenerated/Data{v}.lean'
            run([sys.executable, '-B', 'gen_data.py', f'raw{v}.txt', generated,
                 '--v', str(v), '--name', f'data{v}', '--expect-sha256', sha, '--label', label],
                f'generate{v}', result['steps'])
            require((HERE / generated).read_bytes() == (HERE / 'LktsKernel' / f'Data{v}.lean').read_bytes(),
                    f'Raw-to-Lean data binding mismatch for {v}')
            result['data_binding'][str(v)] = {'raw_sha256': sha, 'regenerated_byte_identical': True}
        result['axioms'] = {}
        for module in MODULES:
            run(['sh', 'build_module.sh', f'LktsKernel/{module}.lean'], f'build-{module}', result['steps'])
            if module.startswith('Cert'):
                build_log = (HERE / 'logs' / f'{module}.build.log').read_text()
                axioms = {name: [x.strip() for x in listed.split(',') if x.strip()]
                          for name, listed in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", build_log)}
                for name in re.findall(r"'([^']+)' does not depend on any axioms", build_log):
                    axioms[name] = []
                v = module[4:]
                root = f'Kirkman.KernelCert.exists_lkts{v}'
                require(root in axioms, f'Missing root axiom report {root}')
                require(all(set(values) <= ALLOWED_AXIOMS for values in axioms.values()),
                        f'Unexpected axiom in {module}')
                require(f'{root} : ∃' in build_log, f'Missing existential theorem type {root}')
                result['axioms'][module] = axioms
        for v in [57, 87]:
            module = f'LktsKernel.Cert{v}'
            text = run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v "$1"',
                        'parent-fresh-replay', module], f'fresh{v}', result['steps'])
            require('replaying' in text and module in text, f'No replay marker for {module}')
        result['compiled_sha256'] = {module: hashlib.sha256((HERE / 'build' / 'LktsKernel' / f'{module}.olean').read_bytes()).hexdigest()
                                     for module in MODULES}
        result['status'] = 'PARENT_REBUILD_AND_FRESH_KERNEL_REPLAY_PASS'
    except Exception as exc:
        result['error'] = f'{type(exc).__name__}: {exc}'
    finally:
        result['finished_at_pt'] = stamp()
        with result_path.open('x') as stream:
            json.dump(result, stream, indent=2)
            stream.write('\n')
        print(json.dumps({'status': result['status'], 'result': str(result_path),
                          'error': result.get('error')}, indent=2), flush=True)
    return 0 if result['status'] == 'PARENT_REBUILD_AND_FRESH_KERNEL_REPLAY_PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
