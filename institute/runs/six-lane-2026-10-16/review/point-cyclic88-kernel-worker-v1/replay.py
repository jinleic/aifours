#!/usr/bin/env python3
"""Clean-directory rebuild and fresh kernel replay of the point-cyclic 2-(88,4,1) nonexistence proof.

Usage:
  python3 -B replay.py --write-manifest   # once, by the worker: pin every source by SHA-256
  python3 -B replay.py TAG                # creates replay-TAG/ next to this file; refuses to overwrite

A replay writes only inside replay-TAG/ (build/, logs/, result.json); the Lean 4.34.1 toolchain and
the prebuilt Mathlib d13f23b cache are used read-only through lean_env.sh.  Every Lean process runs
alone (one process at a time, PC88_THREADS=1).  Steps:

 1. pinned files: every file in manifest.json has its recorded SHA-256 (Lean sources, scripts); the
    formalised proof input PROOF.md has its pinned SHA-256; the toolchain binaries, the Mathlib
    olean and the cache's lean-toolchain / lakefile.lean / lake-manifest.json match the manifest;
    every target definition is still at the recorded file:line;
 2. lean_source_scan.py (byte-identical copy of the LKTS/CDF kernel scanner) passes its own
    controls, and no Lean source has any hit (sorry, admit, axiom, native_decide, +native,
    ofReduceBool, implemented_by, extern, unsafe, skipKernelTC, csimp, opaque, partial, addDecl,
    meta code, run_cmd/#eval, import Lean, maxHeartbeats 0);
 3. every module is compiled into replay-TAG/build in dependency order;
 4. no build log has an error; every `#print axioms` line is within {propext, Classical.choice,
    Quot.sound}; the Audit log equals the pinned expected output byte for byte (it prints every
    target definition, the root types and the axioms);
 5. leanchecker --fresh replays PC88Kernel.Audit (its whole import closure, Mathlib included, in a
    fresh kernel environment);
 6. replay-TAG/result.json records hashes, times, peak RSS, the build logs and the axiom reports.
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
MODULES = ['Target', 'Generic', 'Canonical', 'Bridge', 'Audit']
FRESH = ['PC88Kernel.Audit']
SCRIPTS = ['lean_env.sh', 'build_module.sh', 'lean_source_scan.py', 'replay.py']
PROOF_INPUT = 'point-cyclic88-parent-inputs-v1/PROOF.md'
PROOF_SHA256 = '227c200c6c0adb2874d4e1e482e88ad4de5edbe43c4ce12f8e1625f70de36bfa'
TOOLCHAIN = Path('/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1/bin')
CACHE = Path('/private/tmp/seymour-lean-20261014-68365')
MATHLIB = CACHE / '.lake/packages/mathlib'
MATHLIB_OLEAN = MATHLIB / '.lake/build/lib/lean/Mathlib.olean'
MATHLIB_REV = 'd13f23b723b8a846827a245b89c10fc7d3f11612'
CACHE_FILES = ['lean-toolchain', 'lakefile.lean', 'lake-manifest.json']
ROOTS = {
    'PC88.Audit.root': 'PC88.Target',
    'PC88.Bridge.target': 'PC88.Target',
    'PC88.Canonical.canonicalTarget': 'PC88.CanonicalTarget',
    'PC88.Audit.canonical': 'PC88.CanonicalTarget',
}
# Every definition the statement of `PC88.Target` depends on (beyond Lean core / Prop logic).
# (name, file relative to the anchor, anchor, regex of the defining line)
DEFINITIONS = [
    ('PC88.IsDesign', 'PC88Kernel/Target.lean', 'worker', r'^def IsDesign\b'),
    ('PC88.IsParallelClass', 'PC88Kernel/Target.lean', 'worker', r'^def IsParallelClass\b'),
    ('PC88.IsResolution', 'PC88Kernel/Target.lean', 'worker', r'^def IsResolution\b'),
    ('PC88.blockImage', 'PC88Kernel/Target.lean', 'worker', r'^def blockImage\b'),
    ('PC88.IsResolutionAut', 'PC88Kernel/Target.lean', 'worker', r'^def IsResolutionAut\b'),
    ('PC88.IsFullCycle', 'PC88Kernel/Target.lean', 'worker', r'^def IsFullCycle\b'),
    ('PC88.IsPointCyclicResolution', 'PC88Kernel/Target.lean', 'worker',
     r'^def IsPointCyclicResolution\b'),
    ('PC88.Target', 'PC88Kernel/Target.lean', 'worker', r'^def Target\b'),
    ('PC88.CanonicalTarget (special case, not part of Target)', 'PC88Kernel/Target.lean', 'worker',
     r'^def CanonicalTarget\b'),
    ('Equiv.Perm.IsCycle', 'Mathlib/GroupTheory/Perm/Cycle/Basic.lean', 'mathlib', r'^def IsCycle \('),
    ('Equiv.Perm.SameCycle', 'Mathlib/GroupTheory/Perm/Cycle/Basic.lean', 'mathlib',
     r'^def SameCycle \('),
    ('Equiv.Perm.support', 'Mathlib/GroupTheory/Perm/Support.lean', 'mathlib', r'^def support \('),
    ('Equiv.Perm', 'Mathlib/Logic/Equiv/Defs.lean', 'mathlib', r'^abbrev Equiv\.Perm '),
    ('Equiv', 'Mathlib/Logic/Equiv/Defs.lean', 'mathlib', r'^structure Equiv '),
    ('Equiv.toEmbedding', 'Mathlib/Logic/Embedding/Basic.lean', 'mathlib',
     r'^protected def toEmbedding '),
    ('Finset', 'Mathlib/Data/Finset/Defs.lean', 'mathlib', r'^structure Finset '),
    ('Finset.map', 'Mathlib/Data/Finset/Image.lean', 'mathlib', r'^def map \('),
    ('Finset.image', 'Mathlib/Data/Finset/Image.lean', 'mathlib', r'^def image \('),
    ('Finset.card', 'Mathlib/Data/Finset/Card.lean', 'mathlib', r'^def card \(s : Finset'),
    ('Fintype', 'Mathlib/Data/Fintype/Defs.lean', 'mathlib', r'^class Fintype '),
    ('Fintype.card', 'Mathlib/Data/Fintype/Card.lean', 'mathlib', r'^def card \(α\)'),
    ('Equiv.addRight (CanonicalTarget only; to_additive of Equiv.mulRight)',
     'Mathlib/Algebra/Group/Units/Equiv.lean', 'mathlib', r'^protected def mulRight \(a : G\)'),
    ('ZMod (CanonicalTarget only)', 'Mathlib/Data/ZMod/Defs.lean', 'mathlib', r'^def ZMod '),
]
SEMANTICS = {
    'points': 'An arbitrary type V with [Fintype V], Fintype.card V = 88, and an arbitrary [DecidableEq V] instance (the statement quantifies over both instances).',
    'blocks': 'B : Finset (Finset V), a set of blocks.  IsDesign B requires every block to have exactly 4 points and every 2-subset {x, y} (x != y) to lie in exactly one block (ExistsUnique).  A repeated block would put each of its pairs in two blocks, so a set of blocks loses nothing for lambda = 1.',
    'parallel_class': 'IsParallelClass B P := P ⊆ B and every point lies in exactly one block of P (ExistsUnique).  By DEFINITION a class is a set of blocks of B partitioning the point set.',
    'resolution': 'IsResolution B R := every P in R is a parallel class of B (definition above) and every block of B lies in exactly one member of R (ExistsUnique).  By DEFINITION: classes are partitions of the point set into blocks of B, and R partitions B.  NOT in the definition: |P| = 22, |R| = 29, |B| = 638; the proof DERIVES |P| = 22 (PC88.Canonical.class_card) and |R| <= 29 (PC88.Canonical.R_card_le) from the definitions on ZMod 88 (|R| = 29 and |B| = 638 are not needed and not proved).',
    'image_convention': 'blockImage σ X := X.map σ.toEmbedding = σ(X) (the image of the block X under the point permutation σ).  The image of a class P is P.image (blockImage σ) = {σ(X) : X ∈ P}; the image of the block set is B.image (blockImage σ).',
    'automorphism': 'IsResolutionAut B R σ := B.image (blockImage σ) = B (σ maps the block set onto itself) and for every P in R, P.image (blockImage σ) ∈ R (σ maps every parallel class onto a parallel class of R).  Source wording: "an automorphism of the underlying design that maps each parallel class ... to a parallel class".',
    'cycle': 'IsFullCycle σ := σ.IsCycle ∧ σ.support = Finset.univ (Mathlib IsCycle: some point moves and all moved points are in one cycle; with support = univ every point moves, i.e. σ is a single card(V)-cycle).  Source Definition 5: "has an automorphism permuting the points in one cycle".',
    'point_cyclic_resolution': 'IsPointCyclicResolution B R := IsDesign B ∧ IsResolution B R ∧ ∃ σ, IsFullCycle σ ∧ IsResolutionAut B R σ.',
    'target': 'Target.{u} := ∀ (V : Type u) [Fintype V] [DecidableEq V], Fintype.card V = 88 → ∀ B R, ¬ IsPointCyclicResolution B R.  The root PC88.Audit.root : PC88.Target.{u} is universe-polymorphic.',
    'canonical_special_case': 'CanonicalTarget: V = ZMod 88, σ = Equiv.addRight 1 (x ↦ x + 1).  PC88.Bridge.target_of_canonical proves CanonicalTarget → Target by relabelling along e : ZMod 88 ≃ V, e i = σ^(i.val) x₀, which satisfies e (i + 1) = σ (e i) (PC88.Bridge.exists_equiv_of_fullCycle); PC88.Bridge.canonical_of_target proves Target.{0} → CanonicalTarget (Equiv.addRight 1 is a full cycle, PC88.Bridge.isFullCycle_addRight_one).',
    'not_hypotheses': 'T1, class stabilizers 11/22, counts 22/29, short-block structure and the forbidden pair are not hypotheses of any theorem: they are derived inside PC88.Canonical (short_diff, stab_cases, vadd44_of_stab, class_card, R_card_le, card_orb_mul_card_stab, card_dvd_of_free, orbit_short_bound, arith_final, mem8_of_card, false_of_hyp).',
}


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def locate_definitions():
    found = []
    for name, rel, anchor, pattern in DEFINITIONS:
        base = HERE if anchor == 'worker' else MATHLIB
        path = base / rel
        lines = path.read_text().splitlines()
        hits = [i + 1 for i, line in enumerate(lines) if re.search(pattern, line)]
        require(len(hits) == 1, f'Definition {name}: expected exactly one match of {pattern!r} in {rel}, got {hits}')
        found.append({'name': name, 'file': (rel if anchor == 'worker' else f'mathlib:{rel}'),
                      'line': hits[0], 'text': lines[hits[0] - 1].strip(), 'file_sha256': sha256(path)})
    return found


def write_manifest():
    path = HERE / 'manifest.json'
    require(not path.exists(), 'Refusing to overwrite manifest.json')
    files = {f'PC88Kernel/{m}.lean': sha256(HERE / 'PC88Kernel' / f'{m}.lean') for m in MODULES}
    files.update({name: sha256(HERE / name) for name in SCRIPTS})
    require(sha256(REVIEW / PROOF_INPUT) == PROOF_SHA256, 'PROOF.md does not have the pinned SHA-256')
    manifest = {
        'recorded_at_pt': stamp(),
        'files': files,
        'proof_input': {'path': f'review/{PROOF_INPUT}', 'sha256': PROOF_SHA256},
        'toolchain': {'lean_sha256': sha256(TOOLCHAIN / 'lean'),
                      'leanchecker_sha256': sha256(TOOLCHAIN / 'leanchecker'),
                      'mathlib_rev': MATHLIB_REV,
                      'mathlib_olean_sha256': sha256(MATHLIB_OLEAN),
                      'cache_files': {name: sha256(CACHE / name) for name in CACHE_FILES}},
        'scanner_origin': {'path': 'review/cdf-kernel-worker-v1/lean_source_scan.py',
                           'sha256': sha256(REVIEW / 'cdf-kernel-worker-v1' / 'lean_source_scan.py')},
        'expected_audit_log_sha256': sha256(HERE / 'logs' / 'Audit.build.log'),
        'roots': ROOTS,
        'target_definitions': locate_definitions(),
        'semantics': SEMANTICS,
    }
    with path.open('x') as stream:
        json.dump(manifest, stream, indent=2, ensure_ascii=False)
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
    for sub in ['build', 'logs']:
        (out / sub).mkdir()
    env = dict(os.environ, PC88_BUILD=str(out / 'build'), PC88_LOGS=str(out / 'logs'), PC88_THREADS='1')
    result = {'status': 'FAILED', 'tag': tag, 'started_at_pt': stamp(), 'steps': [],
              'driver_sha256': sha256(__file__),
              'trust_limits': [
                  'Same Lean 4.34.1 kernel implementation (lean and leanchecker of one toolchain); not Comparator, not an independent kernel.',
                  'Prebuilt Mathlib d13f23b oleans from the read-only cache are trusted as compiled artifacts for elaboration; leanchecker --fresh re-checks every declaration in the import closure of PC88Kernel.Audit, Mathlib included, in a fresh kernel environment.',
                  'decide proofs are kernel reductions over ZMod 88 / Fin 5 / Nat.divisors 88 with GMP-accelerated Nat literals (part of the trusted kernel); no native code evaluation, no Lean.ofReduceBool.',
                  'The meaning of the root rests on the reviewer reading PC88Kernel/Target.lean (IsDesign, IsParallelClass, IsResolution, blockImage, IsResolutionAut, IsFullCycle, IsPointCyclicResolution, Target) and the Mathlib definitions listed in manifest.json target_definitions.']}
    result_path = out / 'result.json'
    try:
        manifest = json.loads((HERE / 'manifest.json').read_text())
        result['manifest_sha256'] = sha256(HERE / 'manifest.json')
        for rel, digest in manifest['files'].items():
            require(sha256(HERE / rel) == digest, f'Pinned file changed: {rel}')
        require(set(manifest['files']) == {f'PC88Kernel/{m}.lean' for m in MODULES} | set(SCRIPTS),
                'Manifest does not list exactly the expected files')
        require(sorted(p.name for p in (HERE / 'PC88Kernel').glob('*.lean')) ==
                sorted(f'{m}.lean' for m in MODULES), 'Unexpected Lean file in PC88Kernel/')
        proof_sha = sha256(REVIEW / PROOF_INPUT)
        require(proof_sha == PROOF_SHA256 == manifest['proof_input']['sha256'], 'PROOF.md changed')
        result['proof_input'] = {'path': f'review/{PROOF_INPUT}', 'sha256': proof_sha}
        tool = manifest['toolchain']
        require(sha256(TOOLCHAIN / 'lean') == tool['lean_sha256'], 'lean binary changed')
        require(sha256(TOOLCHAIN / 'leanchecker') == tool['leanchecker_sha256'], 'leanchecker binary changed')
        require(sha256(MATHLIB_OLEAN) == tool['mathlib_olean_sha256'], 'Mathlib.olean changed')
        for name, digest in tool['cache_files'].items():
            require(sha256(CACHE / name) == digest, f'Cache file changed: {name}')
        definitions = locate_definitions()
        require([(d['name'], d['file'], d['line']) for d in definitions] ==
                [(d['name'], d['file'], d['line']) for d in manifest['target_definitions']],
                'A target definition moved')
        result['target_definitions'] = definitions
        spec = importlib.util.spec_from_file_location('pc88_lean_scan', HERE / 'lean_source_scan.py')
        scanner = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(scanner)
        require(sha256(HERE / 'lean_source_scan.py') == manifest['scanner_origin']['sha256'],
                'Scanner is not byte-identical to the CDF/LKTS scanner')
        scan = {'scanner_sha256': sha256(HERE / 'lean_source_scan.py'), 'controls': scanner.controls(), 'files': {}}
        require(scan['controls']['positive_ok'] and scan['controls']['negative_ok'], 'Scanner controls failed')
        for module in MODULES:
            path = HERE / 'PC88Kernel' / f'{module}.lean'
            hits, declarations, imports = scanner.scan_text(path.read_text())
            require(not hits, f'Forbidden Lean construct in {module}: {hits}')
            scan['files'][module] = {'sha256': sha256(path), 'hits': hits, 'imports': imports,
                                     'declarations': len(declarations)}
        result['source_scan'] = scan
        version, _, _ = run(['sh', '-c', '. ./lean_env.sh; exec "$LEAN" --version'], 'lean-version', out,
                            result['steps'], env)
        result['toolchain'] = {'lean_version': version.strip(), **tool}
        builds, axioms = {}, {}
        for module in MODULES:
            run(['sh', 'build_module.sh', f'PC88Kernel/{module}.lean'], f'build-{module}', out,
                result['steps'], env)
            log_path = out / 'logs' / f'{module}.build.log'
            log = log_path.read_text()
            timing = (out / 'logs' / f'{module}.build.time').read_text()
            require(not re.search(r':\d+:\d+: error', log), f'Error message in build log of {module}')
            builds[module] = {**time_metrics(timing), 'warnings': len(re.findall(r':\d+:\d+: warning', log)),
                              'build_log_sha256': sha256(log_path),
                              'olean_sha256': sha256(out / 'build' / 'PC88Kernel' / f'{module}.olean')}
            found = parse_axioms(log)
            for name, listed in found.items():
                require(set(listed) <= ALLOWED_AXIOMS, f'Unexpected axiom for {name}: {listed}')
            if found:
                axioms[module] = found
        audit_log = (out / 'logs' / 'Audit.build.log').read_text()
        require(sha256(out / 'logs' / 'Audit.build.log') == manifest['expected_audit_log_sha256'],
                'Audit output differs from the pinned expected output')
        for root, typ in ROOTS.items():
            require(f'{root} : {typ}' in audit_log, f'Missing root type line for {root}')
            require(root in axioms['Audit'], f'Missing axiom report for {root}')
        require('def PC88.Target.{u} : Prop :=' in audit_log, 'Missing printed Target definition')
        result['builds'] = builds
        result['axioms'] = axioms
        result['printed_audit_output'] = audit_log
        fresh = {}
        for module in FRESH:
            stdout, stderr, item = run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v "$1"',
                                        'fresh', module], f'fresh-{module}', out, result['steps'], env, timeout=3600)
            require(f'replaying {module} with --fresh' in stdout, f'No replay marker for {module}')
            fresh[module] = {**time_metrics(stderr), 'exit_code': item['exit_code'], 'wall_seconds': item['wall_seconds'],
                             'stdout_sha256': sha256(HERE / item['stdout'])}
        result['fresh_replay'] = fresh
        result['roots'] = {root: {'type': typ, 'axioms': axioms['Audit'][root],
                                  'fresh_replay_module': 'PC88Kernel.Audit'} for root, typ in ROOTS.items()}
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
