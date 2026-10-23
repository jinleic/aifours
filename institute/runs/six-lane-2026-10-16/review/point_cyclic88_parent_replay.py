"""Parent rebuild and fresh Lean-kernel replay of the full point-cyclic 88 theorem.
Uses a parent-authored unfolded statement; never runs the worker replay driver.
Writes only point-cyclic88-kernel-parent-replay-v1/, refusing completed or partial replays.
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
SRC = HERE / 'point-cyclic88-kernel-worker-v1'
OUT = HERE / 'point-cyclic88-kernel-parent-replay-v1'
MODULES = ['Target', 'Generic', 'Canonical', 'Bridge', 'Audit']
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
FORBIDDEN = [r'\bsorry\b', r'\badmit\b', r'native_decide', r'ofReduceBool',
             r'implemented_by', r'@\[\s*extern', r'\bunsafe\b',
             r'^\s*(private\s+|protected\s+|noncomputable\s+)*axiom\b',
             r'\bopaque\b', r'\bmacro\b', r'\bsyntax\b', r'^\s*elab\b',
             r'run_cmd', r'run_tac', r'#eval', r'\binitialize\b', r'import\s+Lean\b',
             r'debug\.skipKernelTC', r'addDeclWithoutChecking', r'Lean\.Elab', r'Lean\.Meta']
EXPECTED_IMPORTS = {
    'Target': ['Mathlib.GroupTheory.Perm.Cycle.Basic', 'Mathlib.Data.ZMod.Defs'],
    'Generic': ['Mathlib.Algebra.Group.Action.Pointwise.Finset',
                'Mathlib.Algebra.BigOperators.Group.Finset.Basic'],
    'Canonical': ['PC88Kernel.Target', 'PC88Kernel.Generic', 'Mathlib.Data.ZMod.Basic'],
    'Bridge': ['PC88Kernel.Canonical'],
    'Audit': ['PC88Kernel.Target', 'PC88Kernel.Bridge'],
}


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def without_comments(text):
    # Nested Lean block comments and line comments; scanner is supplementary to kernel replay.
    result, i, depth = [], 0, 0
    while i < len(text):
        if text.startswith('/-', i):
            depth += 1
            i += 2
        elif depth and text.startswith('-/', i):
            depth -= 1
            i += 2
        elif depth:
            if text[i] == '\n':
                result.append('\n')
            i += 1
        elif text.startswith('--', i):
            end = text.find('\n', i)
            i = len(text) if end < 0 else end
        else:
            result.append(text[i])
            i += 1
    require(depth == 0, 'unclosed comment')
    return ''.join(result)


def run(command, name, steps, expect_success=True, timeout=1800):
    started = time.monotonic()
    p = subprocess.run(command, cwd=OUT, capture_output=True, text=True, timeout=timeout)
    (OUT / 'parent-logs' / (name + '.stdout.txt')).write_text(p.stdout)
    (OUT / 'parent-logs' / (name + '.stderr.txt')).write_text(p.stderr)
    step = {'name': name, 'command': command, 'exit_code': p.returncode,
            'wall_seconds': round(time.monotonic() - started, 3)}
    steps.append(step)
    print(json.dumps(step), flush=True)
    if expect_success:
        require(p.returncode == 0, name + ' failed')
    return p


def main():
    require((OUT / 'ParentAudit.lean').exists(), 'parent statement missing')
    require(not (OUT / 'parent-result.json').exists(), 'refusing overwrite')
    (OUT / 'parent-logs').mkdir(exist_ok=False)
    (OUT / 'PC88Kernel').mkdir(exist_ok=False)
    result = {'status': 'FAILED', 'started_at_pt': stamp(),
              'driver_sha256': sha(__file__), 'steps': []}
    try:
        require(sha(SRC / 'manifest.json') ==
                '10ef51ee87fca40b425ace3ba9162d1f9ad9d599e788bdc334ce9a1e1f9f689a',
                'worker manifest changed')
        manifest = json.loads((SRC / 'manifest.json').read_text())
        require(sha(SRC / 'replay-worker/result.json') ==
                '75773531ab1aac6305c4fe4a215a4f830955864d6a18d8f56f16dc3344f74952',
                'worker receipt changed')
        copied = {}
        rels = ['lean_env.sh', 'build_module.sh'] + ['PC88Kernel/' + m + '.lean' for m in MODULES]
        for rel in rels:
            require(sha(SRC / rel) == manifest['files'][rel], 'source pin ' + rel)
            shutil.copyfile(SRC / rel, OUT / rel)
            copied[rel] = sha(OUT / rel)
            require(copied[rel] == manifest['files'][rel], 'copy pin ' + rel)
        result['copied_sha256'] = copied
        result['worker_manifest_sha256'] = sha(SRC / 'manifest.json')
        result['worker_receipt_sha256'] = sha(SRC / 'replay-worker/result.json')
        result['parent_audit_sha256'] = sha(OUT / 'ParentAudit.lean')
        hits, options, imports = [], {}, {}
        for path in [OUT / 'PC88Kernel' / (m + '.lean') for m in MODULES] + [OUT / 'ParentAudit.lean']:
            text = without_comments(path.read_text())
            for pattern in FORBIDDEN:
                if re.search(pattern, text, re.M):
                    hits.append({'file': path.name, 'pattern': pattern})
            options[path.name] = sorted(set(re.findall(r'set_option\s+(\S+)', text)))
            imports[path.name] = re.findall(r'^import\s+(\S+)', text, re.M)
        require(not hits, 'forbidden constructs')
        require(all(set(v) <= {'pp.funBinderTypes', 'maxRecDepth', 'maxHeartbeats'}
                    for v in options.values()), 'unexpected options')
        for module in MODULES:
            require(imports[module + '.lean'] == EXPECTED_IMPORTS[module], 'imports ' + module)
        require(imports['ParentAudit.lean'] == ['PC88Kernel.Audit'], 'parent imports')
        result.update(forbidden_hits=hits, set_options=options, imports=imports)
        for module in MODULES:
            run(['sh', 'build_module.sh', 'PC88Kernel/' + module + '.lean'],
                'build-' + module, result['steps'])
        require(sha(OUT / 'logs/Audit.build.log') == manifest['expected_audit_log_sha256'],
                'worker audit output changed')
        run(['sh', 'build_module.sh', 'ParentAudit.lean'], 'build-ParentAudit', result['steps'])
        log = (OUT / 'logs/ParentAudit.build.log').read_text()
        axioms = {name: [a.strip() for a in listed.split(',') if a.strip()]
                  for name, listed in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log)}
        require(set(axioms) == {'ParentPointCyclic88.no_point_cyclic_resolution'}, 'parent root absent')
        require(all(set(a) <= ALLOWED_AXIOMS for a in axioms.values()), 'nonstandard axioms')
        result['axioms'] = axioms
        fresh = run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v ParentAudit'],
                    'fresh-ParentAudit', result['steps'], timeout=3000)
        require('ParentAudit' in fresh.stdout + fresh.stderr, 'fresh marker absent')
        # These are binding controls, not proofs that the mutated propositions are unprovable.
        audit_source = (OUT / 'ParentAudit.lean').read_text()
        controls = {
            'KnownPositive64': audit_source.replace('Fintype.card V = 88', 'Fintype.card V = 64'),
            'DroppedClassPreservation': audit_source.replace(
                '    (hclass_image : ∀ P ∈ R, P.image (fun X => X.map σ.toEmbedding) ∈ R) : False :=',
                '    : False :=').replace('hblock_image hclass_image', 'hblock_image True.intro'),
        }
        result['negative_controls'] = {}
        for name, source in controls.items():
            require(source != audit_source, 'control not mutated ' + name)
            path = OUT / (name + '.lean')
            with path.open('x') as f:
                f.write(source)
            p = run(['sh', 'build_module.sh', path.name], 'negative-' + name,
                    result['steps'], expect_success=False)
            error_log = (OUT / 'logs' / (name + '.build.log')).read_text()
            require(p.returncode != 0 and 'error:' in error_log.lower(), 'control accepted ' + name)
            require('type mismatch' in error_log.lower() or 'application type mismatch' in error_log.lower(),
                    'unintended negative-control failure ' + name)
            result['negative_controls'][name] = {
                'source_sha256': sha(path), 'exit_code': p.returncode,
                'expected_type_error': True, 'log_sha256': sha(OUT / 'logs' / (name + '.build.log'))}
        result['status'] = 'PARENT_TARGET_REBUILD_AND_FRESH_KERNEL_REPLAY_PASS'
        result['limits'] = [
            'Lean and leanchecker share one toolchain: not a second independent kernel and not Comparator.',
            'The semantic match to the primary definitions is a parent reading; the parent statement unfolds all design/resolution predicates.',
            'Only v=88 is formalized here. The all-primes 8p corollary remains a separately reviewed written proof.',
            'Negative controls prove statement/proof-term sensitivity, not logical unprovability of arbitrary mutations.',
        ]
    except Exception as exc:
        result['error'] = type(exc).__name__ + ': ' + str(exc)
    finally:
        result['finished_at_pt'] = stamp()
        with (OUT / 'parent-result.json').open('x') as f:
            json.dump(result, f, indent=2)
            f.write('\n')
        print(json.dumps({k: result.get(k) for k in ['status', 'error', 'axioms']}, indent=2), flush=True)
    return 0 if result['status'].endswith('PASS') else 1


if __name__ == '__main__':
    raise SystemExit(main())
