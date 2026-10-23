#!/usr/bin/env python3
"""Clean-directory rebuild and fresh kernel replay of the point-cyclic 2-(100,4,1) existence proof.

Usage:
  python3 -B replay.py --write-manifest   # once, by the worker: pin every source by SHA-256 (no overwrite)
  python3 -B replay.py TAG                # creates replay-TAG/ next to this file and refuses to overwrite it

A replay writes only inside replay-TAG/ (build/, logs/, regenerated/, binding-audit.json, result.json); the
Lean 4.34.1 toolchain and the prebuilt Mathlib d13f23b cache are used read-only through lean_env.sh.  Every
Lean process runs alone (one process at a time, PC100_THREADS=1).  Steps:

 1. pinned files: every file in manifest.json has its recorded SHA-256 (Lean sources, scripts);
    PC100Kernel/ contains exactly the pinned Lean files; the raw certificate, the compact seed and the
    v = 64 control certificate have their pinned SHA-256; the toolchain binaries, the Mathlib olean and the
    cache's lean-toolchain / lakefile.lean / lake-manifest.json match the manifest; every listed definition
    is still at the recorded file:line;
 2. gen_lean.py regenerates PC100Kernel/Data100.lean and Data64.lean from the raw certificates into
    regenerated/, byte-identical to the pinned modules;
 3. audit_binding.py (stdlib) checks that the Lean literals equal the raw certificates, that the Theorem C
    expansion of the compact seed is byte-identical to the raw certificate, and that the Lean semantic
    objects recomputed from the literal are the certificate's blocks and classes; its corruption controls
    must all be rejected by the intended check;
 4. lean_source_scan.py (byte-identical copy of the CDF/PC88/RDSQS kernel scanner) passes its own
    controls, and no Lean source has any hit (sorry, admit, axiom, native_decide, +native, ofReduceBool,
    implemented_by, extern, unsafe, skipKernelTC, csimp, opaque, partial, addDecl, meta code,
    run_cmd/#eval, import Lean, maxHeartbeats 0);
 5. every module is compiled into replay-TAG/build in dependency order; no build log has an error; every
    `#print axioms` line is within {propext, Classical.choice, Quot.sound}; the audit log equals the pinned
    expected output byte for byte (it prints every target definition, the witness definitions, the root
    types and the axioms);
 6. negative control: PC100Kernel/ControlFail100.lean, the full pipeline on two corrupted literals, must
    FAIL: the kernel rejects `decide +kernel` on `certCheck 100 cert100swap = true` and on
    `certCheck 64 tz64trade = true`, and both dependent theorems depend on `sorryAx`; no olean is written;
 7. leanchecker --fresh replays the audit module and the controls module, i.e. their whole import closure,
    Mathlib included, in a fresh kernel environment;
 8. replay-TAG/result.json records hashes, times, peak RSS, logs and the axiom reports.
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
LANE = HERE.parent
REVIEW = Path('/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review')
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
MODULES = ['Target', 'Check', 'Data100', 'Data64', 'Cert100', 'Controls100', 'Audit100']
NEGATIVE = ['ControlFail100']
AUDIT = 'Audit100'
FRESH = ['PC100Kernel.Audit100', 'PC100Kernel.Controls100']
ROOTS = {
    'PC100.Audit.root100': 'PC100.Target 100',
    'PC100.Audit.root100_shift': 'PC100.TargetShift 100',
    'PC100.Audit.root100_counts': 'PC100.TargetCounts 100',
    'PC100.Audit.root100_cycleType': '(PC100.shift 100).cycleType = {100}',
    'PC100.Audit.witness100': 'PC100.IsDesign241 PC100.Kernel.pc100Blocks ∧',
    'PC100.Audit.root100_unfolded': '((Equiv.addRight 1).IsCycle ∧ (Equiv.addRight 1).support = Finset.univ) ∧',
}
LEAN_FILES = MODULES + NEGATIVE
SCRIPTS = ['lean_env.sh', 'build_module.sh', 'lean_source_scan.py', 'gen_lean.py', 'audit_binding.py',
           'replay.py']
INPUTS = {
    'cert': ('certs/v100/pc100_t2.cert', '971f722460020f5a572b4f17f1cffe249488b8de079badbfa0184b9a79b4f7c1'),
    'seed': ('certs/v100/pc100_t2.seed', 'ac727835e2f15075e0697206d81482b634ed76c5f7ff000adc58bef43b256245'),
    'tz64': ('controls/v64/tz64.cert', 'd8c1173596cc60f0276c7aab77bfb2c5c162cedd682f32365b628bf11d9a4b2f'),
}
NEGATIVE_EXPECT = {
    'ControlFail100': [
        r'PC100Kernel/ControlFail100\.lean:23:2: error: \(kernel\) application type mismatch',
        r'decide \(certCheck 100 cert100swap = true\) = true',
        r'PC100Kernel/ControlFail100\.lean:29:2: error: \(kernel\) application type mismatch',
        r'decide \(certCheck 64 tz64trade = true\) = true',
        r"'PC100\.Kernel\.Controls\.swap_isDesign' depends on axioms: \[propext, sorryAx, "
        r'Classical\.choice, Quot\.sound\]',
        r"'PC100\.Kernel\.Controls\.trade_shift' depends on axioms: \[propext, sorryAx, "
        r'Classical\.choice, Quot\.sound\]',
    ],
}
TOOLCHAIN = Path('/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1/bin')
CORE_SRC = Path('/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1/src/lean')
CACHE = Path('/private/tmp/seymour-lean-20261014-68365')
MATHLIB = CACHE / '.lake/packages/mathlib'
MATHLIB_OLEAN = MATHLIB / '.lake/build/lib/lean/Mathlib.olean'
MATHLIB_REV = 'd13f23b723b8a846827a245b89c10fc7d3f11612'
CACHE_FILES = ['lean-toolchain', 'lakefile.lean', 'lake-manifest.json']
# Every definition the statements of the roots depend on (beyond Lean core logic).
# (name, file relative to the anchor, anchor, regex of the defining line)
DEFINITIONS = [
    ('PC100.IsDesign241', 'PC100Kernel/Target.lean', 'worker', r'^def IsDesign241\b'),
    ('PC100.IsParallelClass', 'PC100Kernel/Target.lean', 'worker', r'^def IsParallelClass\b'),
    ('PC100.IsResolution', 'PC100Kernel/Target.lean', 'worker', r'^def IsResolution\b'),
    ('PC100.blockImage', 'PC100Kernel/Target.lean', 'worker', r'^def blockImage\b'),
    ('PC100.IsResolutionAutomorphism', 'PC100Kernel/Target.lean', 'worker', r'^def IsResolutionAutomorphism\b'),
    ('PC100.IsFullCycle', 'PC100Kernel/Target.lean', 'worker', r'^def IsFullCycle\b'),
    ('PC100.IsPointCyclicResolution', 'PC100Kernel/Target.lean', 'worker', r'^def IsPointCyclicResolution\b'),
    ('PC100.shift', 'PC100Kernel/Target.lean', 'worker', r'^def shift\b'),
    ('PC100.Target', 'PC100Kernel/Target.lean', 'worker', r'^def Target\b'),
    ('PC100.TargetShift', 'PC100Kernel/Target.lean', 'worker', r'^def TargetShift\b'),
    ('PC100.TargetCounts', 'PC100Kernel/Target.lean', 'worker', r'^def TargetCounts\b'),
    ('PC100.Kernel.RawBlock (witness only)', 'PC100Kernel/Check.lean', 'worker', r'^abbrev RawBlock\b'),
    ('PC100.Kernel.pt (witness only)', 'PC100Kernel/Check.lean', 'worker', r'^def pt\b'),
    ('PC100.Kernel.blk (witness only)', 'PC100Kernel/Check.lean', 'worker', r'^def blk\b'),
    ('PC100.Kernel.classOf (witness only)', 'PC100Kernel/Check.lean', 'worker', r'^def classOf\b'),
    ('PC100.Kernel.blocks (witness only)', 'PC100Kernel/Check.lean', 'worker', r'^@\[irreducible\] def blocks\b'),
    ('PC100.Kernel.classes (witness only)', 'PC100Kernel/Check.lean', 'worker', r'^@\[irreducible\] def classes\b'),
    ('PC100.Kernel.cert100 (witness only, generated)', 'PC100Kernel/Data100.lean', 'worker', r'^def cert100 :'),
    ('PC100.Kernel.pc100Blocks (witness only)', 'PC100Kernel/Cert100.lean', 'worker', r'^def pc100Blocks\b'),
    ('PC100.Kernel.pc100Classes (witness only)', 'PC100Kernel/Cert100.lean', 'worker', r'^def pc100Classes\b'),
    ('ExistsUnique', 'Mathlib/Basic/ExistsUnique.lean', 'mathlib', r'^def ExistsUnique '),
    ('Finset', 'Mathlib/Data/Finset/Defs.lean', 'mathlib', r'^structure Finset '),
    ('Finset.card', 'Mathlib/Data/Finset/Card.lean', 'mathlib', r'^def card \(s : Finset'),
    ('Finset.image', 'Mathlib/Data/Finset/Image.lean', 'mathlib', r'^def image \('),
    ('Finset.map', 'Mathlib/Data/Finset/Image.lean', 'mathlib', r'^def map \('),
    ('Fintype', 'Mathlib/Data/Fintype/Defs.lean', 'mathlib', r'^class Fintype '),
    ('Finset.univ', 'Mathlib/Data/Fintype/Defs.lean', 'mathlib', r'^def univ : Finset'),
    ('Equiv.Perm', 'Mathlib/Logic/Equiv/Defs.lean', 'mathlib', r'^abbrev Equiv\.Perm '),
    ('Equiv.toEmbedding', 'Mathlib/Logic/Embedding/Basic.lean', 'mathlib', r'^protected def toEmbedding '),
    ('Equiv.Perm.IsCycle', 'Mathlib/GroupTheory/Perm/Cycle/Basic.lean', 'mathlib', r'^def IsCycle '),
    ('Equiv.Perm.support', 'Mathlib/GroupTheory/Perm/Support.lean', 'mathlib', r'^def support '),
    ('Equiv.Perm.cycleType (root100_cycleType only)', 'Mathlib/GroupTheory/Perm/Cycle/Type.lean', 'mathlib',
     r'^def cycleType '),
    ('Equiv.addRight (to_additive of Equiv.mulRight)', 'Mathlib/Algebra/Group/Units/Equiv.lean', 'mathlib',
     r'^protected def mulRight \(a : G\)'),
    ('Fin.addCommGroup (the + of Fin n)', 'Mathlib/Algebra/Group/Fin/Basic.lean', 'mathlib',
     r'^instance addCommGroup \(n : ℕ\) \[NeZero n\]'),
    ('Fin', 'Init/Prelude.lean', 'core', r'^structure Fin \(n : Nat\)'),
    ('Fin.add', 'Init/Data/Fin/Basic.lean', 'core', r'^protected def add :'),
]
SEMANTICS = {
    'points': 'Fin 100 = {0, ..., 99} with addition modulo 100 (Fin.add); PC100.shift 100 = Equiv.addRight 1, i.e. x ↦ x + 1 (root shift100_apply: rfl).',
    'design': 'IsDesign241 B := (∀ X ∈ B, X.card = 4) ∧ ∀ T, T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X.  B is a set of blocks (a repeated block would put its pairs in two blocks).',
    'parallel_class': 'IsParallelClass B P := P ⊆ B ∧ ∀ y, ∃! X, X ∈ P ∧ y ∈ X (blocks of B partitioning the points).',
    'resolution': 'IsResolution B R := (∀ P ∈ R, IsParallelClass B P) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P (R partitions B into parallel classes).',
    'automorphism': 'IsResolutionAutomorphism B R σ := B.image (blockImage σ) = B ∧ ∀ P ∈ R, P.image (blockImage σ) ∈ R, blockImage σ X = X.map σ.toEmbedding: σ maps the block set onto itself and every class onto a class.',
    'cycle': 'IsFullCycle σ := σ.IsCycle ∧ σ.support = Finset.univ (Mathlib IsCycle and support): σ permutes all points in one cycle.  root100_cycleType: cycleType of x ↦ x + 1 on Fin 100 is {100}.',
    'targets': 'Target 100 := ∃ B, IsDesign241 B ∧ ∃ R, IsResolution B R ∧ ∃ σ, IsFullCycle σ ∧ IsResolutionAutomorphism B R σ (TZ 2026 Def. 5).  TargetShift 100 := IsFullCycle (shift 100) ∧ ∃ B R, IsDesign241 B ∧ IsResolution B R ∧ IsResolutionAutomorphism B R (shift 100).  TargetCounts 100 adds B.card = 825, R.card = 33, P.card = 25 (as v(v-1)/12, (v-1)/3, v/4).',
    'witness': 'pc100Blocks = blocks 100 cert100 = {blk 100 e : e listed}, pc100Classes = classes 100 cert100 = {classOf 100 c : c a raw class}, blk e = {e.1, e.2.1, e.2.2.1, e.2.2.2} mod 100 (pc100Blocks_spec, pc100Classes_spec).  witness100 proves IsDesign241, IsResolution, IsResolutionAutomorphism (shift 100), IsFullCycle (shift 100) and the counts 825 / 33 / 25 for these explicit objects.',
    'binding': 'cert100 is the raw certificate (SHA-256 971f…4f7c1) copied verbatim in raw order by gen_lean.py (replay step 2 regenerates it byte-identically); cert100_range (kernel) shows every number is below 100, so no reduction modulo 100 occurs.  audit_binding.py (replay step 3) checks literal = certificate, that the Theorem C expansion of the compact seed (SHA-256 ac72…6245) is byte-identical to the certificate, and that the Lean objects recomputed from the literal are the certificate blocks and classes.  The Lean theorems do not mention the raw files; the raw-to-object equality is this external stdlib audit.',
    'not_hypotheses': 'The pair coverage, the class partitions, the shift invariance and the counts are not hypotheses of any root: they are kernel evaluations (cert100_check, cert100_shape, cert100_range by decide +kernel) fed to the data-independent soundness theorem sound_of_check; the cycle facts come from Mathlib (isCycle_finRotate, support_finRotate, cycleType_finRotate).',
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
        base = {'worker': HERE, 'mathlib': MATHLIB, 'core': CORE_SRC}[anchor]
        path = base / rel
        lines = path.read_text().splitlines()
        hits = [i + 1 for i, line in enumerate(lines) if re.search(pattern, line)]
        require(len(hits) == 1, f'Definition {name}: expected exactly one match of {pattern!r} in {rel}, got {hits}')
        found.append({'name': name, 'file': (rel if anchor == 'worker' else f'{anchor}:{rel}'),
                      'line': hits[0], 'text': lines[hits[0] - 1].strip(), 'file_sha256': sha256(path)})
    return found


def write_manifest():
    path = HERE / 'manifest.json'
    require(not path.exists(), 'Refusing to overwrite manifest.json')
    files = {f'PC100Kernel/{m}.lean': sha256(HERE / 'PC100Kernel' / f'{m}.lean') for m in LEAN_FILES}
    files.update({name: sha256(HERE / name) for name in SCRIPTS})
    for key, (rel, digest) in INPUTS.items():
        require(sha256(LANE / rel) == digest, f'{key} SHA-256 mismatch')
    manifest = {
        'recorded_at_pt': stamp(),
        'files': files,
        'inputs': {key: {'path': f'point-cyclic100/{rel}', 'sha256': digest} for key, (rel, digest) in INPUTS.items()},
        'toolchain': {'lean_sha256': sha256(TOOLCHAIN / 'lean'),
                      'leanchecker_sha256': sha256(TOOLCHAIN / 'leanchecker'),
                      'mathlib_rev': MATHLIB_REV,
                      'mathlib_olean_sha256': sha256(MATHLIB_OLEAN),
                      'cache_files': {name: sha256(CACHE / name) for name in CACHE_FILES}},
        'scanner_origin': {'path': 'review/cdf-kernel-worker-v1/lean_source_scan.py',
                           'sha256': sha256(REVIEW / 'cdf-kernel-worker-v1' / 'lean_source_scan.py')},
        'expected_audit_log_sha256': sha256(HERE / 'logs' / f'{AUDIT}.build.log'),
        'modules': MODULES, 'negative': NEGATIVE, 'fresh': FRESH, 'roots': ROOTS,
        'definitions': locate_definitions(),
        'semantics': SEMANTICS,
    }
    with path.open('x') as stream:
        json.dump(manifest, stream, indent=2, ensure_ascii=False)
        stream.write('\n')
    print(json.dumps({'manifest': str(path), 'sha256': sha256(path)}))


def run(command, name, out_dir, steps, env, timeout=1800, expect_success=True):
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
    require(not timed_out, f'{name} timed out')
    if expect_success:
        require(code == 0, f'{name} did not complete successfully')
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
    for sub in ['build', 'logs', 'regenerated']:
        (out / sub).mkdir()
    env = dict(os.environ, PC100_BUILD=str(out / 'build'), PC100_LOGS=str(out / 'logs'), PC100_THREADS='1')
    result = {'status': 'FAILED', 'tag': tag, 'started_at_pt': stamp(), 'steps': [],
              'driver_sha256': sha256(__file__),
              'trust_limits': [
                  'Same Lean 4.34.1 kernel implementation (lean and leanchecker of one toolchain); not Comparator, not an independent kernel.',
                  'Prebuilt Mathlib d13f23b oleans from the read-only cache are trusted as compiled artifacts for elaboration; leanchecker --fresh re-checks every declaration in the import closure of the replayed modules, Mathlib included, in a fresh kernel environment.',
                  'decide +kernel proofs are kernel reductions of Bool-valued checkers over Nat / List with GMP-accelerated Nat literals (part of the trusted kernel); no native code evaluation, no Lean.ofReduceBool.',
                  'The raw-certificate-to-Lean-object equality and the seed expansion are the external stdlib audit audit_binding.py, not Lean theorems; the Lean literal is the raw certificate, regenerated byte-identically from the raw file.',
                  'The meaning of the roots rests on the reviewer reading PC100Kernel/Target.lean (IsDesign241, IsParallelClass, IsResolution, blockImage, IsResolutionAutomorphism, IsFullCycle, IsPointCyclicResolution, shift, Target, TargetShift, TargetCounts) and the Mathlib/core definitions listed in manifest.json definitions.']}
    result_path = out / 'result.json'
    try:
        manifest = json.loads((HERE / 'manifest.json').read_text())
        result['manifest_sha256'] = sha256(HERE / 'manifest.json')
        for rel, digest in manifest['files'].items():
            require(sha256(HERE / rel) == digest, f'Pinned file changed: {rel}')
        require(set(manifest['files']) == {f'PC100Kernel/{m}.lean' for m in LEAN_FILES} | set(SCRIPTS),
                'Manifest does not list exactly the expected files')
        require(sorted(p.name for p in (HERE / 'PC100Kernel').glob('*.lean')) ==
                sorted(f'{m}.lean' for m in LEAN_FILES), 'Unexpected Lean file in PC100Kernel/')
        for key, (rel, digest) in INPUTS.items():
            require(sha256(LANE / rel) == digest == manifest['inputs'][key]['sha256'], f'{key} changed')
        result['inputs'] = manifest['inputs']
        tool = manifest['toolchain']
        require(sha256(TOOLCHAIN / 'lean') == tool['lean_sha256'], 'lean binary changed')
        require(sha256(TOOLCHAIN / 'leanchecker') == tool['leanchecker_sha256'], 'leanchecker binary changed')
        require(sha256(MATHLIB_OLEAN) == tool['mathlib_olean_sha256'], 'Mathlib.olean changed')
        for name, digest in tool['cache_files'].items():
            require(sha256(CACHE / name) == digest, f'Cache file changed: {name}')
        definitions = locate_definitions()
        require([(d['name'], d['file'], d['line']) for d in definitions] ==
                [(d['name'], d['file'], d['line']) for d in manifest['definitions']],
                'A listed definition moved')
        result['definitions'] = definitions
        # 2. regenerate the data modules
        run(['python3', '-B', 'gen_lean.py', str(out / 'regenerated')], 'generate', out, result['steps'], env)
        result['regenerated'] = {}
        for module in ['Data100', 'Data64']:
            regenerated = out / 'regenerated' / f'{module}.lean'
            require(regenerated.read_bytes() == (HERE / 'PC100Kernel' / f'{module}.lean').read_bytes(),
                    f'Regenerated {module}.lean differs from the pinned module')
            result['regenerated'][f'{module}.lean'] = sha256(regenerated)
        # 3. binding audit
        audit_receipt = out / 'binding-audit.json'
        run(['python3', '-B', 'audit_binding.py', str(audit_receipt)], 'binding-audit', out, result['steps'], env)
        audit = json.loads(audit_receipt.read_text())
        require(audit['status'] == 'BINDING_AUDIT_PASS', 'binding audit failed')
        require(audit.get('manifest_pins_match') is True, 'binding audit pin mismatch')
        require(all(c['as_intended'] for c in audit['controls'].values()), 'binding audit control failed')
        result['binding_audit'] = {'receipt': str(audit_receipt.relative_to(HERE)), 'sha256': sha256(audit_receipt),
                                   'status': audit['status'],
                                   'controls': {k: [c['as_intended'], c.get('check')] for k, c in audit['controls'].items()},
                                   'counts': {k: audit['result'][k] for k in
                                              ['cert_blocks', 'distinct_blocks', 'classes', 'blocks_per_class']},
                                   'expansion_byte_identical': audit['result']['expansion_byte_identical']}
        # 4. source scan
        scan_spec = importlib.util.spec_from_file_location('pc100_lean_scan', HERE / 'lean_source_scan.py')
        scanner = importlib.util.module_from_spec(scan_spec)
        scan_spec.loader.exec_module(scanner)
        require(sha256(HERE / 'lean_source_scan.py') == manifest['scanner_origin']['sha256'],
                'Scanner is not byte-identical to the CDF/PC88/RDSQS scanner')
        scan = {'scanner_sha256': sha256(HERE / 'lean_source_scan.py'), 'controls': scanner.controls(), 'files': {}}
        require(scan['controls']['positive_ok'] and scan['controls']['negative_ok'], 'Scanner controls failed')
        for module in LEAN_FILES:
            path = HERE / 'PC100Kernel' / f'{module}.lean'
            hits, declarations, imports = scanner.scan_text(path.read_text())
            require(not hits, f'Forbidden Lean construct in {module}: {hits}')
            scan['files'][module] = {'sha256': sha256(path), 'hits': hits, 'imports': imports,
                                     'declarations': len(declarations)}
        result['source_scan'] = scan
        # 5. rebuild
        version, _, _ = run(['sh', '-c', '. ./lean_env.sh; exec "$LEAN" --version'], 'lean-version', out,
                            result['steps'], env)
        result['toolchain'] = {'lean_version': version.strip(), **tool}
        builds, axioms = {}, {}
        for module in MODULES:
            run(['sh', 'build_module.sh', f'PC100Kernel/{module}.lean'], f'build-{module}', out, result['steps'], env)
            log_path = out / 'logs' / f'{module}.build.log'
            log = log_path.read_text()
            timing = (out / 'logs' / f'{module}.build.time').read_text()
            require(not re.search(r':\d+:\d+: error', log), f'Error message in build log of {module}')
            builds[module] = {**time_metrics(timing), 'warnings': len(re.findall(r':\d+:\d+: warning', log)),
                              'build_log_sha256': sha256(log_path),
                              'olean_sha256': sha256(out / 'build' / 'PC100Kernel' / f'{module}.olean')}
            found = parse_axioms(log)
            for name, listed in found.items():
                require(set(listed) <= ALLOWED_AXIOMS, f'Unexpected axiom for {name}: {listed}')
            if found:
                axioms[module] = found
        audit_log = (out / 'logs' / f'{AUDIT}.build.log').read_text()
        require(sha256(out / 'logs' / f'{AUDIT}.build.log') == manifest['expected_audit_log_sha256'],
                'Audit output differs from the pinned expected output')
        for root, typ in ROOTS.items():
            require(f'{root} : {typ}' in audit_log, f'Missing root type line for {root}')
            require(root in axioms[AUDIT], f'Missing axiom report for {root}')
        require('def PC100.Target : ℕ → Prop :=' in audit_log, 'Missing printed Target definition')
        result['builds'] = builds
        result['axioms'] = axioms
        result['printed_audit_output'] = audit_log
        # 6. negative control
        negatives = {}
        for module in NEGATIVE:
            _, _, item = run(['sh', 'build_module.sh', f'PC100Kernel/{module}.lean'], f'build-{module}', out,
                             result['steps'], env, expect_success=False)
            log_path = out / 'logs' / f'{module}.build.log'
            log = log_path.read_text()
            require(item['exit_code'] != 0, f'Negative control {module} unexpectedly built')
            for pattern in NEGATIVE_EXPECT[module]:
                require(re.search(pattern, log), f'Negative control {module}: missing {pattern!r}')
            require(not (out / 'build' / 'PC100Kernel' / f'{module}.olean').exists(),
                    f'Negative control {module} produced an olean')
            negatives[module] = {'exit_code': item['exit_code'], 'build_log_sha256': sha256(log_path), 'log': log}
        result['negative_controls'] = negatives
        # 7. fresh replay
        fresh = {}
        for module in FRESH:
            stdout, stderr, item = run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v "$1"',
                                        'fresh', module], f'fresh-{module}', out, result['steps'], env, timeout=3600)
            require(f'replaying {module} with --fresh' in stdout, f'No replay marker for {module}')
            fresh[module] = {**time_metrics(stderr), 'exit_code': item['exit_code'], 'wall_seconds': item['wall_seconds'],
                             'stdout_sha256': sha256(HERE / item['stdout'])}
        result['fresh_replay'] = fresh
        result['roots'] = {root: {'type_prefix': typ, 'axioms': axioms[AUDIT][root],
                                  'fresh_replay_module': f'PC100Kernel.{AUDIT}'} for root, typ in ROOTS.items()}
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
