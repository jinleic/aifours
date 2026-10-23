#!/usr/bin/env python3
"""Clean-directory rebuild and fresh kernel replay of the RDSQS(52) / RDSQS(76) existence proofs.

Usage:
  python3 -B replay.py --write-manifest   # once, by the worker: pin every source by SHA-256
  python3 -B replay.py SUITE TAG          # SUITE in {52, 76}; creates replay-SUITE-TAG/ next to
                                          # this file and refuses to overwrite it

A replay writes only inside replay-SUITE-TAG/ (build/, logs/, regenerated/, binding-audit.json,
result.json); the Lean 4.34.1 toolchain and the prebuilt Mathlib d13f23b cache are used read-only
through lean_env.sh.  Every Lean process runs alone (one process at a time, RDSQS_THREADS=1).
Steps:

 1. pinned files: every file in manifest.json has its recorded SHA-256 (Lean sources, scripts);
    RdsqsKernel/ contains exactly the pinned Lean files; the raw certificate and the compact
    seed have their pinned SHA-256; the toolchain binaries, the Mathlib olean and the cache's
    lean-toolchain / lakefile.lean / lake-manifest.json match the manifest; every listed
    definition is still at the recorded file:line;
 2. gen_lean.py regenerates RdsqsKernel/DataV.lean from the raw certificate and the seed into
    regenerated/, byte-identical to the pinned module;
 3. audit_binding.py (stdlib) re-derives, from the pinned Lean literal and the Lean definitions,
    the generated block set and the resolution at every point, and checks them for equality with
    the raw certificate; its corruption controls must all be rejected by the intended check;
 4. lean_source_scan.py (byte-identical copy of the CDF/LKTS/PC88 kernel scanner) passes its own
    controls, and no Lean source has any hit (sorry, admit, axiom, native_decide, +native,
    ofReduceBool, implemented_by, extern, unsafe, skipKernelTC, csimp, opaque, partial, addDecl,
    meta code, run_cmd/#eval, import Lean, maxHeartbeats 0);
 5. every module of the suite is compiled into replay-SUITE-TAG/build in dependency order; no
    build log has an error; every `#print axioms` line is within {propext, Classical.choice,
    Quot.sound}; the audit log equals the pinned expected output byte for byte (it prints every
    target definition, the witness definitions, the root types and the axioms);
 6. negative control (suite 52): RdsqsKernel/ControlFail52.lean, the full pipeline on a corrupted
    seed, must FAIL: the kernel rejects `decide +kernel` on `seedCheck 52 data52swap = true`, and
    the dependent theorem depends on `sorryAx`;
 7. leanchecker --fresh replays the audit module (and, for suite 52, the controls module), i.e.
    its whole import closure, Mathlib included, in a fresh kernel environment;
 8. replay-SUITE-TAG/result.json records hashes, times, peak RSS, logs and the axiom reports.
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
SHARED = ['Target', 'Generic', 'Check', 'Counts']
SUITES = {
    '52': {
        'v': 52,
        'modules': SHARED + ['Data52', 'Cert52', 'Controls52', 'Audit52'],
        'negative': ['ControlFail52'],
        'audit': 'Audit52',
        'fresh': ['RdsqsKernel.Audit52', 'RdsqsKernel.Controls52'],
        'roots': {
            'Rdsqs.Audit.root52': 'Rdsqs.Target 52',
            'Rdsqs.Audit.root52_all': 'Rdsqs.TargetAll 52',
            'Rdsqs.Audit.root52_counts': 'Rdsqs.TargetCounts 52',
            'Rdsqs.Audit.witness52': 'Rdsqs.IsRDSQS Rdsqs.Kernel.rdsqs52 ∧',
            'Rdsqs.Audit.root52_unfolded': '∃ B,',
        },
    },
    '76': {
        'v': 76,
        'modules': SHARED + ['Data76', 'Cert76', 'Audit76'],
        'negative': [],
        'audit': 'Audit76',
        'fresh': ['RdsqsKernel.Audit76'],
        'roots': {
            'Rdsqs.Audit.root76': 'Rdsqs.Target 76',
            'Rdsqs.Audit.root76_all': 'Rdsqs.TargetAll 76',
            'Rdsqs.Audit.root76_counts': 'Rdsqs.TargetCounts 76',
            'Rdsqs.Audit.witness76': 'Rdsqs.IsRDSQS Rdsqs.Kernel.rdsqs76 ∧',
            'Rdsqs.Audit.root76_unfolded': '∃ B,',
        },
    },
}
LEAN_FILES = sorted({m for s in SUITES.values() for m in s['modules'] + s['negative']})
SCRIPTS = ['lean_env.sh', 'build_module.sh', 'lean_source_scan.py', 'gen_lean.py',
           'audit_binding.py', 'replay.py']
INPUTS = {
    '52': {'raw': 'rdsqs52-parent-inputs-v1/rdsqs52_z52_m23.txt',
           'raw_sha256': '7ae0a828b5af08b4bd9b423564981d85e3703886553638024fdc812f564989a6',
           'seed': 'rdsqs52-parent-replay-v1/rdsqs52_z52_m23_seed.json',
           'seed_sha256': 'a0fe9247f93d1f16007eff24b65c3dddf0f409c33f847f8a7382399b09dcefce'},
    '76': {'raw': 'rdsqs76-parent-inputs-v1/rdsqs76_z76_m3_sample0.txt',
           'raw_sha256': '2f75b37c0439aa9f9c57861505a2e865997dd02249349b708880916d477a75aa',
           'seed': 'rdsqs76-parent-inputs-v1/rdsqs76_z76_m3_sample0_seed.json',
           'seed_sha256': '8d5860f640d1d49163496f996aad97af1e4674855cc2a1c6883327cb272ba0ad'},
}
NEGATIVE_EXPECT = {
    'ControlFail52': [
        r'RdsqsKernel/ControlFail52\.lean:17:2: error: \(kernel\) application type mismatch',
        r"'Rdsqs\.Kernel\.Controls\.swap_isRDSQS' depends on axioms: \[propext, sorryAx, "
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
    ('Rdsqs.IsSQS', 'RdsqsKernel/Target.lean', 'worker', r'^def IsSQS\b'),
    ('Rdsqs.derivedBlocks', 'RdsqsKernel/Target.lean', 'worker', r'^def derivedBlocks\b'),
    ('Rdsqs.IsDerivedParallelClass', 'RdsqsKernel/Target.lean', 'worker',
     r'^def IsDerivedParallelClass\b'),
    ('Rdsqs.IsDerivedResolution', 'RdsqsKernel/Target.lean', 'worker',
     r'^def IsDerivedResolution\b'),
    ('Rdsqs.IsRDSQS', 'RdsqsKernel/Target.lean', 'worker', r'^def IsRDSQS\b'),
    ('Rdsqs.Target', 'RdsqsKernel/Target.lean', 'worker', r'^def Target\b'),
    ('Rdsqs.TargetAll', 'RdsqsKernel/Target.lean', 'worker', r'^def TargetAll\b'),
    ('Rdsqs.TargetCounts', 'RdsqsKernel/Target.lean', 'worker', r'^def TargetCounts\b'),
    ('Rdsqs.Generic.relabel (witness only)', 'RdsqsKernel/Generic.lean', 'worker',
     r'^def relabel\b'),
    ('Rdsqs.Generic.blocksOf (witness only)', 'RdsqsKernel/Generic.lean', 'worker',
     r'^@\[irreducible\] def blocksOf\b'),
    ('Rdsqs.Kernel.RawTriple (witness only)', 'RdsqsKernel/Check.lean', 'worker',
     r'^abbrev RawTriple\b'),
    ('Rdsqs.Kernel.pt (witness only)', 'RdsqsKernel/Check.lean', 'worker', r'^def pt\b'),
    ('Rdsqs.Kernel.tri (witness only)', 'RdsqsKernel/Check.lean', 'worker', r'^def tri\b'),
    ('Rdsqs.Kernel.seedTriples (witness only)', 'RdsqsKernel/Check.lean', 'worker',
     r'^@\[irreducible\] def seedTriples\b'),
    ('Rdsqs.Kernel.seedClasses (witness only)', 'RdsqsKernel/Check.lean', 'worker',
     r'^@\[irreducible\] def seedClasses\b'),
    ('Rdsqs.Kernel.blocks (witness only)', 'RdsqsKernel/Check.lean', 'worker', r'^def blocks\b'),
    ('Rdsqs.Kernel.resAt (witness only)', 'RdsqsKernel/Check.lean', 'worker',
     r'^@\[irreducible\] def resAt\b'),
    ('Rdsqs.Kernel.data52 (witness only, generated)', 'RdsqsKernel/Data52.lean', 'worker',
     r'^def data52 :'),
    ('Rdsqs.Kernel.mults52 (witness only, generated)', 'RdsqsKernel/Data52.lean', 'worker',
     r'^def mults52 :'),
    ('Rdsqs.Kernel.rdsqs52 (witness only)', 'RdsqsKernel/Cert52.lean', 'worker',
     r'^def rdsqs52\b'),
    ('Rdsqs.Kernel.data76 (witness only, generated)', 'RdsqsKernel/Data76.lean', 'worker',
     r'^def data76 :'),
    ('Rdsqs.Kernel.mults76 (witness only, generated)', 'RdsqsKernel/Data76.lean', 'worker',
     r'^def mults76 :'),
    ('Rdsqs.Kernel.rdsqs76 (witness only)', 'RdsqsKernel/Cert76.lean', 'worker',
     r'^def rdsqs76\b'),
    ('ExistsUnique', 'Mathlib/Basic/ExistsUnique.lean', 'mathlib', r'^def ExistsUnique '),
    ('Finset', 'Mathlib/Data/Finset/Defs.lean', 'mathlib', r'^structure Finset '),
    ('Finset.card', 'Mathlib/Data/Finset/Card.lean', 'mathlib', r'^def card \(s : Finset'),
    ('Finset.image', 'Mathlib/Data/Finset/Image.lean', 'mathlib', r'^def image \('),
    ('Finset.map', 'Mathlib/Data/Finset/Image.lean', 'mathlib', r'^def map \('),
    ('Finset.filter', 'Mathlib/Data/Finset/Filter.lean', 'mathlib', r'^def filter \(s : Finset'),
    ('Finset.erase', 'Mathlib/Data/Finset/Erase.lean', 'mathlib', r'^def erase \(s : Finset'),
    ('Fintype', 'Mathlib/Data/Fintype/Defs.lean', 'mathlib', r'^class Fintype '),
    ('Fintype.card', 'Mathlib/Data/Fintype/Card.lean', 'mathlib', r'^def card \(α\)'),
    ('Equiv.addRight (witness only; to_additive of Equiv.mulRight)',
     'Mathlib/Algebra/Group/Units/Equiv.lean', 'mathlib', r'^protected def mulRight \(a : G\)'),
    ('Fin', 'Init/Prelude.lean', 'core', r'^structure Fin \(n : Nat\)'),
    ('Fin.add (witness only)', 'Init/Data/Fin/Basic.lean', 'core', r'^protected def add :'),
    ('Fin.mul (witness only)', 'Init/Data/Fin/Basic.lean', 'core', r'^protected def mul :'),
]
SEMANTICS = {
    'points': 'Target v and TargetCounts v: the point set is Fin v = {0, ..., v-1}.  TargetAll v: every type V with [Fintype V], Fintype.card V = v, and an arbitrary [DecidableEq V] instance (the statement quantifies over both instances).',
    'sqs': 'IsSQS B := (∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset V, T.card = 3 → ∃! X, X ∈ B ∧ T ⊆ X.  B is a set of blocks (a repeated block would put each of its 3-subsets in two blocks).',
    'derived_design': 'derivedBlocks B x := (B.filter (x ∈ ·)).image (·.erase x) = {X \\ {x} : X ∈ B, x ∈ X} (Tan–Zhou B_x), the block set of the derived design on V \\ {x}.',
    'parallel_class': 'IsDerivedParallelClass B x P := P ⊆ derivedBlocks B x ∧ ∀ y ≠ x, ∃! T, T ∈ P ∧ y ∈ T.  By DEFINITION the blocks of P are derived blocks (so they avoid x) and partition V \\ {x}.',
    'resolution': 'IsDerivedResolution B x R := (∀ P ∈ R, IsDerivedParallelClass B x P) ∧ ∀ T ∈ derivedBlocks B x, ∃! P, P ∈ R ∧ T ∈ P.  R partitions B_x into parallel classes of V \\ {x}.',
    'rdsqs': 'IsRDSQS B := IsSQS B ∧ ∀ x : V, ∃ R, IsDerivedResolution B x R: the derived design at EVERY point x is resolvable (no orbit representative is assumed).',
    'counts': 'TargetCounts v additionally states B.card = v(v-1)(v-2)/24 and, at every x, every derived block has 3 points and avoids x, (derivedBlocks B x).card = (v-1)(v-2)/6, and a resolution R with R.card = (v-2)/2 and P.card = (v-1)/3 for all P ∈ R.  These are DERIVED (RdsqsKernel.Counts: card_blocks_mul, derived_card_three, card_derived_mul, card_class_mul, card_resolution_mul) from IsSQS / IsDerivedResolution, not hypotheses.',
    'witness': 'rdsqsV := blocks V dataV = Generic.blocksOf (seedTriples V dataV): all translates ({0} ∪ t) + a (a ∈ Fin V) of the triples t = tri V e = {e.1, e.2.1, e.2.2} mod V of the raw POINT 0 section dataV (rdsqsV_spec restates this with Finset.image).  The resolution at x for multiplier m is resAt V dataV m x = image of seedClasses V dataV under y ↦ m*y + x (Fin V arithmetic).  witnessV proves IsRDSQS rdsqsV and IsDerivedResolution rdsqsV x (resAt V dataV m x) for EVERY x : Fin V and every (m, m′) ∈ multsV.',
    'binding': 'dataV is the raw certificate POINT 0 section copied verbatim in raw order by gen_lean.py (raw SHA-256 checked; replay step 2 regenerates it byte-identically); dataV_range (kernel) shows every number is below V, so no reduction modulo V occurs.  audit_binding.py (replay step 3) recomputes, from the pinned literal and exactly these definitions, the block set and resAt m x for all x and m, and checks: raw block lines pairwise distinct with set = rdsqsV; raw POINT x = resAt m_x x as a set of classes for the seed rule multiplier m_x ∈ multsV, class j of POINT x = image of class j of POINT 0 (order preserved).  The Lean theorems do not mention the raw file; the raw-to-object equality is this external stdlib audit.',
    'not_hypotheses': 'The STS property of the seed, the class partitions, translation closure, multiplier invariance, and all counts are not hypotheses of any root: they are kernel evaluations (dataV_seedCheck, dataV_multCheck, dataV_shape, dataV_range by decide +kernel) fed to data-independent soundness theorems (seed_of_check, isRDSQS_of_check, resAt_of_check, Generic.isSQS_blocksOf, Generic.isDerivedResolution_affine, Counts.*).',
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
    files = {f'RdsqsKernel/{m}.lean': sha256(HERE / 'RdsqsKernel' / f'{m}.lean') for m in LEAN_FILES}
    files.update({name: sha256(HERE / name) for name in SCRIPTS})
    for suite, spec in INPUTS.items():
        require(sha256(REVIEW / spec['raw']) == spec['raw_sha256'], f'raw {suite} SHA-256 mismatch')
        require(sha256(REVIEW / spec['seed']) == spec['seed_sha256'], f'seed {suite} SHA-256 mismatch')
    manifest = {
        'recorded_at_pt': stamp(),
        'files': files,
        'inputs': {suite: {'raw': {'path': f"review/{spec['raw']}", 'sha256': spec['raw_sha256']},
                           'seed': {'path': f"review/{spec['seed']}", 'sha256': spec['seed_sha256']}}
                   for suite, spec in INPUTS.items()},
        'toolchain': {'lean_sha256': sha256(TOOLCHAIN / 'lean'),
                      'leanchecker_sha256': sha256(TOOLCHAIN / 'leanchecker'),
                      'mathlib_rev': MATHLIB_REV,
                      'mathlib_olean_sha256': sha256(MATHLIB_OLEAN),
                      'cache_files': {name: sha256(CACHE / name) for name in CACHE_FILES}},
        'scanner_origin': {'path': 'review/cdf-kernel-worker-v1/lean_source_scan.py',
                           'sha256': sha256(REVIEW / 'cdf-kernel-worker-v1' / 'lean_source_scan.py')},
        'expected_audit_log_sha256': {suite: sha256(HERE / 'logs' / f"{s['audit']}.build.log")
                                      for suite, s in SUITES.items()},
        'suites': {suite: {'modules': s['modules'], 'negative': s['negative'], 'fresh': s['fresh'],
                           'roots': s['roots']} for suite, s in SUITES.items()},
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


def main(suite, tag):
    require(suite in SUITES, 'SUITE must be 52 or 76')
    require(re.fullmatch(r'[A-Za-z0-9_-]+', tag), 'TAG must be alphanumeric')
    spec = SUITES[suite]
    out = HERE / f'replay-{suite}-{tag}'
    out.mkdir(exist_ok=False)
    for sub in ['build', 'logs', 'regenerated']:
        (out / sub).mkdir()
    env = dict(os.environ, RDSQS_BUILD=str(out / 'build'), RDSQS_LOGS=str(out / 'logs'), RDSQS_THREADS='1')
    result = {'status': 'FAILED', 'suite': suite, 'tag': tag, 'started_at_pt': stamp(), 'steps': [],
              'driver_sha256': sha256(__file__),
              'trust_limits': [
                  'Same Lean 4.34.1 kernel implementation (lean and leanchecker of one toolchain); not Comparator, not an independent kernel.',
                  'Prebuilt Mathlib d13f23b oleans from the read-only cache are trusted as compiled artifacts for elaboration; leanchecker --fresh re-checks every declaration in the import closure of the replayed modules, Mathlib included, in a fresh kernel environment.',
                  'decide +kernel proofs are kernel reductions of Bool-valued checkers over Nat / Fin V / List with GMP-accelerated Nat literals (part of the trusted kernel); no native code evaluation, no Lean.ofReduceBool.',
                  'The raw-certificate-to-Lean-object equality (blocks and every POINT x section) is the external stdlib audit audit_binding.py, not a Lean theorem; the Lean literal is the raw POINT 0 section, regenerated byte-identically from the raw file.',
                  'The meaning of the roots rests on the reviewer reading RdsqsKernel/Target.lean (IsSQS, derivedBlocks, IsDerivedParallelClass, IsDerivedResolution, IsRDSQS, Target, TargetAll, TargetCounts) and the Mathlib/core definitions listed in manifest.json definitions.']}
    result_path = out / 'result.json'
    try:
        manifest = json.loads((HERE / 'manifest.json').read_text())
        result['manifest_sha256'] = sha256(HERE / 'manifest.json')
        for rel, digest in manifest['files'].items():
            require(sha256(HERE / rel) == digest, f'Pinned file changed: {rel}')
        require(set(manifest['files']) == {f'RdsqsKernel/{m}.lean' for m in LEAN_FILES} | set(SCRIPTS),
                'Manifest does not list exactly the expected files')
        require(sorted(p.name for p in (HERE / 'RdsqsKernel').glob('*.lean')) ==
                sorted(f'{m}.lean' for m in LEAN_FILES), 'Unexpected Lean file in RdsqsKernel/')
        inp = INPUTS[suite]
        require(sha256(REVIEW / inp['raw']) == inp['raw_sha256'] == manifest['inputs'][suite]['raw']['sha256'],
                'raw certificate changed')
        require(sha256(REVIEW / inp['seed']) == inp['seed_sha256'] == manifest['inputs'][suite]['seed']['sha256'],
                'seed changed')
        result['inputs'] = manifest['inputs'][suite]
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
        # 2. regenerate the data module
        v = spec['v']
        run(['python3', '-B', 'gen_lean.py', str(v), str(out / 'regenerated')], f'generate{v}', out,
            result['steps'], env)
        regenerated = out / 'regenerated' / f'Data{v}.lean'
        require(regenerated.read_bytes() == (HERE / 'RdsqsKernel' / f'Data{v}.lean').read_bytes(),
                f'Regenerated Data{v}.lean differs from the pinned module')
        result['regenerated'] = {f'Data{v}.lean': sha256(regenerated)}
        # 3. binding audit
        audit_receipt = out / f'binding-audit-{v}.json'
        run(['python3', '-B', 'audit_binding.py', str(v), str(audit_receipt)], f'binding-audit{v}', out,
            result['steps'], env)
        audit = json.loads(audit_receipt.read_text())
        require(audit['status'] == 'BINDING_AUDIT_PASS', 'binding audit failed')
        require(audit['lean_data_module'].get('manifest_pin_matches') is True, 'binding audit pin mismatch')
        require(all(c['as_intended'] for c in audit['controls'].values()), 'binding audit control failed')
        result['binding_audit'] = {'receipt': str(audit_receipt.relative_to(HERE)),
                                   'sha256': sha256(audit_receipt), 'status': audit['status'],
                                   'controls': {k: c['as_intended'] for k, c in audit['controls'].items()},
                                   'counts': {k: audit['result'][k] for k in
                                              ['raw_blocks', 'generated_blocks', 'seed_triples', 'seed_classes',
                                               'classes_per_point', 'triples_per_class', 'points']}}
        # 4. source scan
        scan_spec = importlib.util.spec_from_file_location('rdsqs_lean_scan', HERE / 'lean_source_scan.py')
        scanner = importlib.util.module_from_spec(scan_spec)
        scan_spec.loader.exec_module(scanner)
        require(sha256(HERE / 'lean_source_scan.py') == manifest['scanner_origin']['sha256'],
                'Scanner is not byte-identical to the CDF/LKTS/PC88 scanner')
        scan = {'scanner_sha256': sha256(HERE / 'lean_source_scan.py'), 'controls': scanner.controls(), 'files': {}}
        require(scan['controls']['positive_ok'] and scan['controls']['negative_ok'], 'Scanner controls failed')
        for module in spec['modules'] + spec['negative']:
            path = HERE / 'RdsqsKernel' / f'{module}.lean'
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
        for module in spec['modules']:
            run(['sh', 'build_module.sh', f'RdsqsKernel/{module}.lean'], f'build-{module}', out,
                result['steps'], env)
            log_path = out / 'logs' / f'{module}.build.log'
            log = log_path.read_text()
            timing = (out / 'logs' / f'{module}.build.time').read_text()
            require(not re.search(r':\d+:\d+: error', log), f'Error message in build log of {module}')
            builds[module] = {**time_metrics(timing), 'warnings': len(re.findall(r':\d+:\d+: warning', log)),
                              'build_log_sha256': sha256(log_path),
                              'olean_sha256': sha256(out / 'build' / 'RdsqsKernel' / f'{module}.olean')}
            found = parse_axioms(log)
            for name, listed in found.items():
                require(set(listed) <= ALLOWED_AXIOMS, f'Unexpected axiom for {name}: {listed}')
            if found:
                axioms[module] = found
        audit_module = spec['audit']
        audit_log = (out / 'logs' / f'{audit_module}.build.log').read_text()
        require(sha256(out / 'logs' / f'{audit_module}.build.log') == manifest['expected_audit_log_sha256'][suite],
                'Audit output differs from the pinned expected output')
        for root, typ in spec['roots'].items():
            require(f'{root} : {typ}' in audit_log, f'Missing root type line for {root}')
            require(root in axioms[audit_module], f'Missing axiom report for {root}')
        require('def Rdsqs.Target : ℕ → Prop :=' in audit_log, 'Missing printed Target definition')
        result['builds'] = builds
        result['axioms'] = axioms
        result['printed_audit_output'] = audit_log
        # 6. negative controls
        negatives = {}
        for module in spec['negative']:
            _, _, item = run(['sh', 'build_module.sh', f'RdsqsKernel/{module}.lean'], f'build-{module}', out,
                             result['steps'], env, expect_success=False)
            log_path = out / 'logs' / f'{module}.build.log'
            log = log_path.read_text()
            require(item['exit_code'] != 0, f'Negative control {module} unexpectedly built')
            for pattern in NEGATIVE_EXPECT[module]:
                require(re.search(pattern, log), f'Negative control {module}: missing {pattern!r}')
            require(not (out / 'build' / 'RdsqsKernel' / f'{module}.olean').exists(),
                    f'Negative control {module} produced an olean')
            negatives[module] = {'exit_code': item['exit_code'], 'build_log_sha256': sha256(log_path),
                                 'log': log}
        result['negative_controls'] = negatives
        # 7. fresh replay
        fresh = {}
        for module in spec['fresh']:
            stdout, stderr, item = run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v "$1"',
                                        'fresh', module], f'fresh-{module}', out, result['steps'], env, timeout=3600)
            require(f'replaying {module} with --fresh' in stdout, f'No replay marker for {module}')
            fresh[module] = {**time_metrics(stderr), 'exit_code': item['exit_code'], 'wall_seconds': item['wall_seconds'],
                             'stdout_sha256': sha256(HERE / item['stdout'])}
        result['fresh_replay'] = fresh
        result['roots'] = {root: {'type_prefix': typ, 'axioms': axioms[audit_module][root],
                                  'fresh_replay_module': f'RdsqsKernel.{audit_module}'}
                           for root, typ in spec['roots'].items()}
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
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1], sys.argv[2]))
