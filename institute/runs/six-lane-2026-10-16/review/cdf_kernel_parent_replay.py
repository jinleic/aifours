"""Parent replay of the CDF Lean existence proofs, independent of the worker's replay driver.

1. Copies the 14 modules needed for the roots (Target, Generic, Data*, Cert*) and the two Lean environment
   scripts from cdf-kernel-worker-v1 into cdf-kernel-parent-replay-v1/ (refuses to overwrite).
2. Binds raw certificates to Lean literals with a parent-written reader (no worker generator or reader).
3. Scans the copied sources for forbidden constructs (parent-written pattern list).
4. Adds ParentAudit.lean: the parent writes the target proposition out in full (no Cdf.IsCDF or Cdf.diffs in
   the statement), so the kernel must check that each worker root proves exactly this unfolded statement.
5. Builds every module once (-j1), parses the axiom reports, then runs leanchecker --fresh on ParentAudit.
"""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import time
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
SRC = HERE / 'cdf-kernel-worker-v1'
OUT = HERE / 'cdf-kernel-parent-replay-v1'
ORDERS = {321: 16, 501: 25, 621: 31, 681: 34, 801: 40, 901: 45}
SHAS = {321: '0304c61ba5f0a756259c0d12970f1e0d6c4e4909d931e997c7e37312dc37034b',
        501: '517e02fa330269323f70de11e66ac89aac97da106775efb7dca1d674fd7aab74',
        621: '257d85f25cd85afc06f6762f1a8f7d4f72e37cbfde806927838f1ac6b7ae05f5',
        681: '16af75391a6b01bd6fc7ee8ec45bd3b53396bd72403e667297af89c1dc09f7b7',
        801: '0a75e7d93920415f04a51967bd5a4033765f040f3b19af9f603d16b6d616186c',
        901: '06bd6ae8b5349d8e2b1b11aae3be9297abcc46af9858c4370d0a98f8a8ee56d3'}
MODULES = ['Target', 'Generic'] + [f'Data{v}' for v in ORDERS] + [f'Cert{v}' for v in ORDERS]
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
FORBIDDEN = [r'\bsorry\b', r'\badmit\b', r'native_decide', r'ofReduceBool', r'implemented_by', r'@\[\s*extern',
             r'\bunsafe\b', r'^\s*(private\s+|protected\s+|noncomputable\s+)*axiom\b', r'\bopaque\b', r'\bmacro\b',
             r'\bsyntax\b', r'^\s*elab\b', r'run_cmd', r'run_tac', r'#eval', r'\binitialize\b', r'import\s+Lean\b',
             r'debug\.skipKernelTC', r'addDeclWithoutChecking', r'Lean\.Elab', r'Lean\.Meta']


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def run(command, name, steps, timeout=1800):
    started = time.monotonic()
    proc = subprocess.run(command, cwd=OUT, capture_output=True, text=True, timeout=timeout)
    (OUT / 'parent-logs' / f'{name}.stdout.txt').write_text(proc.stdout)
    (OUT / 'parent-logs' / f'{name}.stderr.txt').write_text(proc.stderr)
    steps.append({'name': name, 'command': command, 'exit_code': proc.returncode,
                  'wall_seconds': round(time.monotonic() - started, 3)})
    print(json.dumps(steps[-1]), flush=True)
    require(proc.returncode == 0, f'{name} failed')
    return proc.stdout + proc.stderr


def read_data_module(path, v):
    text = path.read_text()
    header = re.search(r'def data%dHeader : Nat × Nat := \((\d+), (\d+)\)' % v, text)
    raw_sha = re.search(r'def data%dRawSha256 : String := "([0-9a-f]{64})"' % v, text)
    body = re.search(r'def data%d : List \(List Nat\) := \[\n(.*?)\n\]' % v, text, re.S)
    require(header and raw_sha and body, f'Data{v}: expected definitions not found')
    defs = re.findall(r'^\s*(?:def|theorem|instance|abbrev|lemma|axiom|structure|class)\s+(\S+)', text, re.M)
    require(sorted(defs) == sorted([f'data{v}RawSha256', f'data{v}Header', f'data{v}']), f'Data{v}: unexpected declarations {defs}')
    rows = []
    for line in body.group(1).split('\n'):
        m = re.fullmatch(r'  \[(\d+), (\d+), (\d+), (\d+), (\d+)\],?', line)
        require(m is not None, f'Data{v}: unparsable row {line!r}')
        rows.append([int(x) for x in m.groups()])
    return (int(header.group(1)), int(header.group(2))), raw_sha.group(1), rows


def read_raw(path):
    lines = [l for l in path.read_text().split('\n') if l and not l.startswith('#')]
    require(lines[0].startswith('CDF '), 'raw header')
    _, v, k = lines[0].split(' ')
    return (int(v), int(k)), [[int(x) for x in l.split(' ')] for l in lines[1:]]


def parent_audit_source():
    lines = [f'import CdfKernel.Cert{v}' for v in ORDERS]
    lines += ['', '/-! Parent-authored audit statements (written by the integration parent, 2026-10-17).',
              'The proposition is spelled out from the definition of a cyclic (v,5,1) difference family:',
              'n maps Fin 5 → Fin v that are injective, whose ordered within-block differences (subtraction in',
              'Fin v, i.e. modulo v) contain every nonzero residue exactly once and the residue 0 never.',
              'It does not mention `Cdf.IsCDF`, `Cdf.diffs` or `Cdf.Target`; the kernel must unfold those to accept',
              'each worker root as a proof of this statement. -/', '', 'namespace ParentCdfAudit', '',
              'def ParentStatement (v n : Nat) : Prop :=',
              '  ∃ B : Fin n → Fin 5 → Fin v,',
              '    (∀ i : Fin n, ∀ j k : Fin 5, B i j = B i k → j = k) ∧',
              '    (∀ d : Fin v, d.val ≠ 0 →',
              '      (((Finset.univ : Finset (Fin n × Fin 5 × Fin 5)).filter fun t => t.2.1 ≠ t.2.2).val.map',
              '        fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = 1) ∧',
              '    (∀ d : Fin v, d.val = 0 →',
              '      (((Finset.univ : Finset (Fin n × Fin 5 × Fin 5)).filter fun t => t.2.1 ≠ t.2.2).val.map',
              '        fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = 0)', '']
    for v, n in ORDERS.items():
        lines.append(f'theorem cdf{v} : ParentStatement {v} {n} := Cdf.Kernel.exists_cdf{v}')
    lines += ['', 'end ParentCdfAudit', '']
    lines += [f'#print axioms ParentCdfAudit.cdf{v}' for v in ORDERS]
    return '\n'.join(lines) + '\n'


def main():
    OUT.mkdir(exist_ok=False)
    (OUT / 'parent-logs').mkdir()
    (OUT / 'CdfKernel').mkdir()
    result = {'status': 'FAILED', 'started_at_pt': stamp(), 'driver_sha256': sha(__file__), 'steps': []}
    try:
        worker = json.loads((SRC / 'result.json').read_text())
        copied = {}
        for name in ['lean_env.sh', 'build_module.sh']:
            shutil.copyfile(SRC / name, OUT / name)
            copied[name] = sha(OUT / name)
        for module in MODULES:
            shutil.copyfile(SRC / 'CdfKernel' / f'{module}.lean', OUT / 'CdfKernel' / f'{module}.lean')
            copied[f'CdfKernel/{module}.lean'] = sha(OUT / 'CdfKernel' / f'{module}.lean')
        result['copied_sha256'] = copied
        result['worker_result_sha256'] = sha(SRC / 'result.json')
        # 2. raw -> Lean literal binding, parent reader
        binding = {}
        for v, n in ORDERS.items():
            raw_path = HERE / f'cdf{v}-parent-inputs-v1' / f'cdf_{v}.txt'
            require(sha(raw_path) == SHAS[v], f'pinned raw hash {v}')
            raw_header, raw_rows = read_raw(raw_path)
            lean_header, lean_sha, lean_rows = read_data_module(OUT / 'CdfKernel' / f'Data{v}.lean', v)
            require(raw_header == (v, 5) == lean_header, f'header {v}')
            require(lean_sha == SHAS[v], f'sha literal {v}')
            require(raw_rows == lean_rows and len(raw_rows) == n, f'literal rows {v}')
            cert = (OUT / 'CdfKernel' / f'Cert{v}.lean').read_text()
            require(f'theorem exists_cdf{v} : ∃ B : Fin {n} → Fin 5 → Fin {v}, Cdf.IsCDF B' in cert, f'root statement text {v}')
            binding[str(v)] = {'blocks': n, 'raw_sha256': SHAS[v], 'rows_equal': True}
        result['literal_binding'] = binding
        # 3. forbidden-construct scan and set_option inventory
        hits, options = [], {}
        for path in sorted((OUT / 'CdfKernel').glob('*.lean')):
            text = path.read_text()
            stripped = re.sub(r'/-.*?-/', '', text, flags=re.S)
            stripped = re.sub(r'--[^\n]*', '', stripped)
            for pattern in FORBIDDEN:
                if re.search(pattern, stripped, re.M):
                    hits.append({'file': path.name, 'pattern': pattern})
            options[path.name] = sorted(set(re.findall(r'set_option\s+(\S+)', stripped)))
        result['forbidden_hits'] = hits
        result['set_options'] = options
        require(not hits, 'forbidden constructs present')
        require(all(set(v) <= {'pp.funBinderTypes', 'maxRecDepth', 'maxHeartbeats'} for v in options.values()), 'unexpected set_option')
        imports = {p.name: re.findall(r'^import\s+(\S+)', p.read_text(), re.M) for p in (OUT / 'CdfKernel').glob('*.lean')}
        require(imports['Target.lean'] == ['Mathlib.Data.Fintype.Prod'], 'Target imports')
        require(imports['Generic.lean'] == ['CdfKernel.Target'], 'Generic imports')
        require(all(imports[f'Data{v}.lean'] == [] for v in ORDERS), 'Data modules import nothing')
        require(all(imports[f'Cert{v}.lean'] == ['CdfKernel.Generic', f'CdfKernel.Data{v}'] for v in ORDERS), 'Cert imports')
        result['imports'] = imports
        # 4. parent-authored audit module
        audit = OUT / 'ParentAudit.lean'
        with audit.open('x') as stream:
            stream.write(parent_audit_source())
        result['parent_audit_sha256'] = sha(audit)
        # 5. build all modules once, then the audit, then fresh replay
        for module in MODULES:
            run(['sh', 'build_module.sh', f'CdfKernel/{module}.lean'], f'build-{module}', result['steps'])
        run(['sh', 'build_module.sh', 'ParentAudit.lean'], 'build-ParentAudit', result['steps'])
        log = (OUT / 'logs' / 'ParentAudit.build.log').read_text()
        axioms = {name: [x.strip() for x in listed.split(',') if x.strip()]
                  for name, listed in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log)}
        require(set(axioms) == {f'ParentCdfAudit.cdf{v}' for v in ORDERS}, f'axiom reports {sorted(axioms)}')
        require(all(set(a) <= ALLOWED_AXIOMS for a in axioms.values()), 'nonstandard axioms')
        result['axioms'] = axioms
        fresh = run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v "$1"',
                     'parent-fresh', 'ParentAudit'], 'fresh-ParentAudit', result['steps'], timeout=3000)
        require('ParentAudit' in fresh, 'fresh replay marker')
        result['status'] = 'PARENT_TARGET_REBUILD_AND_FRESH_KERNEL_REPLAY_PASS'
        result['limit'] = ('Same Lean kernel implementation as the worker (no Comparator, no second kernel); decide +kernel uses '
                           'the kernel GMP-accelerated Nat arithmetic; raw-to-literal binding checked in Python; the semantic '
                           'match between the parent statement and the literature notion is a reading, reviewed separately.')
    except Exception as exc:
        result['error'] = f'{type(exc).__name__}: {exc}'
    finally:
        result['finished_at_pt'] = stamp()
        with (OUT / 'parent-result.json').open('x') as stream:
            json.dump(result, stream, indent=2)
            stream.write('\n')
        print(json.dumps({k: result.get(k) for k in ('status', 'error', 'axioms')}, indent=2), flush=True)
    return 0 if result['status'].endswith('PASS') else 1


if __name__ == '__main__':
    raise SystemExit(main())
