#!/usr/bin/env python3
"""Clean-directory rebuild and fresh kernel replay of the mcDSQS(38) roots.

Usage:
  python3 -B replay.py --write-manifest   # once, by the worker: pin every source by SHA-256
  python3 -B replay.py TAG                # creates replay-TAG/ next to this file; refuses to
                                          # overwrite it

A replay writes only inside replay-TAG/ (build/, logs/, regenerated/, binding-audit.json,
result.json); the Lean 4.34.1 toolchain and the prebuilt Mathlib d13f23b cache are used read-only
through lean_env.sh.  Every Lean process runs alone (one process at a time, MCD_THREADS=1).
Steps:

 1. pinned files: every file in manifest.json has its recorded SHA-256 (Lean sources, scripts);
    McdKernel/ contains exactly the pinned Lean files; the raw certificate has its pinned
    SHA-256; the toolchain binaries, the Mathlib olean and the cache's lean-toolchain /
    lakefile.lean / lake-manifest.json match the manifest; every listed definition is still at
    the recorded file:line;
 2. gen_lean.py regenerates McdKernel/Data38.lean from the raw certificate into regenerated/,
    byte-identical to the pinned module;
 3. audit_binding.py (stdlib, no code shared with gen_lean.py) checks that the Lean literals
    equal the raw certificate section by section, re-checks the raw certificate definition-first,
    and runs its corruption controls, which must all behave as intended;
 4. lean_source_scan.py (byte-identical copy of the CDF/LKTS/PC88/RDSQS kernel scanner) passes
    its own controls, and no Lean source has any hit (sorry, admit, axiom, native_decide,
    +native, ofReduceBool, implemented_by, extern, unsafe, skipKernelTC, csimp, opaque, partial,
    addDecl, meta code, run_cmd/#eval, import Lean, maxHeartbeats 0);
 5. every module is compiled into replay-TAG/build in dependency order; no build log has an
    error; every `#print axioms` line is within {propext, Classical.choice, Quot.sound}; the
    Audit38 log equals the pinned expected output byte for byte (it prints every target
    definition, the witness definitions, the root types and the axioms);
 6. negative control: McdKernel/ControlFail38.lean, the full pipeline on a corrupted POINT 5
    section, must FAIL: the kernel rejects `decide +kernel` on `colCheck ... = true`, and the
    dependent colouring theorem depends on `sorryAx`; no olean is written;
 7. leanchecker --fresh replays McdKernel.Audit38 and McdKernel.Controls38 (their whole import
    closures, Mathlib included) in a fresh kernel environment;
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
REVIEW = HERE.parent
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
MODULES = ['Target', 'Check', 'Counts', 'Data38', 'Cert38', 'Controls38', 'Audit38']
NEGATIVE = ['ControlFail38']
FRESH = ['McdKernel.Audit38', 'McdKernel.Controls38']
LEAN_FILES = sorted(MODULES + NEGATIVE)
SCRIPTS = ['lean_env.sh', 'build_module.sh', 'lean_source_scan.py', 'gen_lean.py',
           'audit_binding.py', 'replay.py']
RAW = 'mcdsqs38-parent-inputs-v1/mcdsqs38_g342_s0.txt'
RAW_SHA256 = '973f93e4646e48df64b70b3a64811afcdc87b10a1767222f54ffe65d3a303f1c'
ROOTS = {
    'Mcd.Audit.root38_coloured': 'Mcd.TargetColoured 38 19',
    'Mcd.Audit.root37_lower': 'Mcd.ColourLowerBound 37 19',
    'Mcd.Audit.root37_chi': 'Mcd.chiPrime 37 = 19',
    'Mcd.Audit.root38_mc': 'Mcd.TargetMc 38',
    'Mcd.Audit.witness38': 'Mcd.IsMcDSQS Mcd.Kernel.mcdsqs38 ∧',
    'Mcd.Audit.root38_coloured_unfolded': '∃ B,',
    'Mcd.Audit.root37_lower_unfolded': '∀ (W : Type u_1) [inst : Fintype W] [DecidableEq W],',
    'Mcd.Audit.root37_chi_unfolded': 'sInf',
    'Mcd.Audit.root38_mc_unfolded': '∃ B,',
}
NEGATIVE_EXPECT = {
    'ControlFail38': [
        r'McdKernel/ControlFail38\.lean:17:2: error: \(kernel\) application type mismatch',
        r"'Mcd\.Kernel\.Controls\.swap_colouring' depends on axioms: \[propext, sorryAx, "
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
    ('Mcd.IsSQS', 'McdKernel/Target.lean', 'worker', r'^def IsSQS\b'),
    ('Mcd.IsSTS', 'McdKernel/Target.lean', 'worker', r'^def IsSTS\b'),
    ('Mcd.derivedBlocks', 'McdKernel/Target.lean', 'worker', r'^def derivedBlocks\b'),
    ('Mcd.IsPPC', 'McdKernel/Target.lean', 'worker', r'^def IsPPC\b'),
    ('Mcd.IsColouring', 'McdKernel/Target.lean', 'worker', r'^def IsColouring\b'),
    ('Mcd.chiPrime', 'McdKernel/Target.lean', 'worker', r'^noncomputable def chiPrime\b'),
    ('Mcd.TargetColoured', 'McdKernel/Target.lean', 'worker', r'^def TargetColoured\b'),
    ('Mcd.IsMcDSQS', 'McdKernel/Target.lean', 'worker', r'^def IsMcDSQS\b'),
    ('Mcd.TargetMc', 'McdKernel/Target.lean', 'worker', r'^def TargetMc\b'),
    ('Mcd.ColourLowerBound', 'McdKernel/Target.lean', 'worker', r'^def ColourLowerBound\b'),
    ('Mcd.Kernel.RawQuad (witness only)', 'McdKernel/Check.lean', 'worker', r'^abbrev RawQuad\b'),
    ('Mcd.Kernel.RawTriple (witness only)', 'McdKernel/Check.lean', 'worker', r'^abbrev RawTriple\b'),
    ('Mcd.Kernel.pt (witness only)', 'McdKernel/Check.lean', 'worker', r'^def pt\b'),
    ('Mcd.Kernel.quad (witness only)', 'McdKernel/Check.lean', 'worker', r'^def quad\b'),
    ('Mcd.Kernel.tri (witness only)', 'McdKernel/Check.lean', 'worker', r'^def tri\b'),
    ('Mcd.Kernel.blockSet (witness only)', 'McdKernel/Check.lean', 'worker',
     r'^@\[irreducible\] def blockSet\b'),
    ('Mcd.Kernel.tripleSet (witness only)', 'McdKernel/Check.lean', 'worker',
     r'^@\[irreducible\] def tripleSet\b'),
    ('Mcd.Kernel.classSet (witness only)', 'McdKernel/Check.lean', 'worker',
     r'^@\[irreducible\] def classSet\b'),
    ('Mcd.Kernel.blocks38 (witness only, generated)', 'McdKernel/Data38.lean', 'worker',
     r'^def blocks38 :'),
    ('Mcd.Kernel.colour38 (witness only, generated)', 'McdKernel/Data38.lean', 'worker',
     r'^def colour38 :'),
    ('Mcd.Kernel.mcdsqs38 (witness only)', 'McdKernel/Cert38.lean', 'worker', r'^def mcdsqs38\b'),
    ('Mcd.Kernel.colouring38 (witness only)', 'McdKernel/Cert38.lean', 'worker',
     r'^def colouring38\b'),
    ('ExistsUnique', 'Mathlib/Basic/ExistsUnique.lean', 'mathlib', r'^def ExistsUnique '),
    ('Finset', 'Mathlib/Data/Finset/Defs.lean', 'mathlib', r'^structure Finset '),
    ('Finset.card', 'Mathlib/Data/Finset/Card.lean', 'mathlib', r'^def card \(s : Finset'),
    ('Finset.image', 'Mathlib/Data/Finset/Image.lean', 'mathlib', r'^def image \('),
    ('Finset.filter', 'Mathlib/Data/Finset/Filter.lean', 'mathlib', r'^def filter \(s : Finset'),
    ('Finset.erase', 'Mathlib/Data/Finset/Erase.lean', 'mathlib', r'^def erase \(s : Finset'),
    ('Finset.Nonempty', 'Mathlib/Data/Finset/Empty.lean', 'mathlib',
     r'^protected def Nonempty \(s : Finset'),
    ('Disjoint', 'Mathlib/Order/Disjoint.lean', 'mathlib', r'^def Disjoint \(a b : α\)'),
    ('InfSet (sInf)', 'Mathlib/Order/SetNotation.lean', 'mathlib', r'^class InfSet '),
    ('InfSet ℕ (sInf on ℕ: least element via Nat.find, 0 for the empty set)',
     'Mathlib/Order/Lattice/Nat.lean', 'mathlib', r'^noncomputable instance : InfSet ℕ'),
    ('Fintype', 'Mathlib/Data/Fintype/Defs.lean', 'mathlib', r'^class Fintype '),
    ('Fintype.card', 'Mathlib/Data/Fintype/Card.lean', 'mathlib', r'^def card \(α\)'),
    ('Fin', 'Init/Prelude.lean', 'core', r'^structure Fin \(n : Nat\)'),
]
SEMANTICS = {
    'points': 'TargetColoured / TargetMc: the point set is Fin 38 = {0, ..., 37}; chiPrime n ranges over STS on Fin n; ColourLowerBound n r: every type W with [Fintype W], Fintype.card W = n, and an arbitrary [DecidableEq W] instance.',
    'sqs': 'IsSQS B := (∀ X ∈ B, X.card = 4) ∧ ∀ T, T.card = 3 → ∃! X, X ∈ B ∧ T ⊆ X.',
    'sts': 'IsSTS S := (∀ T ∈ S, T.card = 3) ∧ ∀ P, P.card = 2 → ∃! T, T ∈ S ∧ P ⊆ T.',
    'derived_design': 'derivedBlocks B x := (B.filter (x ∈ ·)).image (·.erase x) = {X \\ {x} : X ∈ B, x ∈ X} (Tan–Zhou B_x).',
    'ppc': 'IsPPC D P := P.Nonempty ∧ P ⊆ D ∧ ∀ T ∈ P, ∀ T′ ∈ P, T ≠ T′ → Disjoint T T′ (a nonempty set of pairwise disjoint blocks of D; Tan–Zhou partial parallel class).',
    'colouring': 'IsColouring D C := (∀ P ∈ C, IsPPC D P) ∧ ∀ T ∈ D, ∃! P, P ∈ C ∧ T ∈ P: a partition of D into colour classes, each a PPC; an r-colouring has C.card = r (Tan–Zhou r-block-colouring).',
    'chi_prime': 'chiPrime n := sInf {r | ∃ S on Fin n, IsSTS S ∧ ∃ C, IsColouring S C ∧ C.card = r}: Tan–Zhou χ′(n) = min over all STS(n) D of χ′(D).  sInf on ℕ is the least element (Nat.find) of a nonempty set and 0 for the empty set; the set is proved nonempty for n = 37 (sts37_witness).',
    'roots': 'root38_coloured : TargetColoured 38 19 (an SQS on Fin 38 whose derived design at every point has a 19-colouring); root37_lower : ColourLowerBound 37 19 (data-independent); root37_chi : chiPrime 37 = 19; root38_mc : TargetMc 38, with IsMcDSQS B := IsSQS B ∧ ∀ x, ∃ C, IsColouring (derivedBlocks B x) C ∧ C.card = chiPrime (38 - 1); unfolded versions of root38_coloured, root37_lower, root37_chi and root38_mc state them with Mathlib notions only.',
    'witness': 'mcdsqs38 := blockSet 38 blocks38 = {quad 38 b : b a raw block line}; colouring38 x := classSet 38 (colour38.getD x.val []) = the classes of the raw POINT x section ({tri 38 e : e in raw CLASS j}).  The χ′(37) witness is tripleSet 37 col38_37 with classSet 37 col38_37: the raw POINT 37 section (numbers 0..36) read on Fin 37.',
    'binding': 'blocks38 and col38_x are the raw BLOCKS and POINT x sections copied verbatim in raw order by gen_lean.py (raw SHA-256 checked; replay step 2 regenerates Data38.lean byte-identically); data38_range (kernel) shows every number is below 38, so no reduction modulo 38 occurs.  audit_binding.py (replay step 3) independently re-parses the raw file and the Lean literals and checks section-by-section equality.  Since the literals ARE the raw certificate, the Lean theorems are about exactly the raw blocks and the raw POINT x classes; no symmetry of the certificate is used.',
    'not_hypotheses': 'The SQS property, every colouring, the STS(37) property and all counts are not hypotheses of any root: they are kernel evaluations (blocks38_sqsCheck, colour38_check_a..d, col38_37_stsCheck, data38_shape, data38_range by decide +kernel) fed to data-independent soundness theorems (isSQS_of_check, colouring_of_check, sts_of_check) and the data-independent counting lemmas (Counts.card_sts_mul, card_ppc_mul_le, sum_card_colouring, colourLowerBound_37, chiPrime_eq_of).',
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
    files = {f'McdKernel/{m}.lean': sha256(HERE / 'McdKernel' / f'{m}.lean') for m in LEAN_FILES}
    files.update({name: sha256(HERE / name) for name in SCRIPTS})
    require(sha256(REVIEW / RAW) == RAW_SHA256, 'raw SHA-256 mismatch')
    manifest = {
        'recorded_at_pt': stamp(),
        'files': files,
        'input': {'path': f'review/{RAW}', 'sha256': RAW_SHA256},
        'toolchain': {'lean_sha256': sha256(TOOLCHAIN / 'lean'),
                      'leanchecker_sha256': sha256(TOOLCHAIN / 'leanchecker'),
                      'mathlib_rev': MATHLIB_REV,
                      'mathlib_olean_sha256': sha256(MATHLIB_OLEAN),
                      'cache_files': {name: sha256(CACHE / name) for name in CACHE_FILES}},
        'scanner_origin': {'path': 'review/cdf-kernel-worker-v1/lean_source_scan.py',
                           'sha256': sha256(REVIEW / 'cdf-kernel-worker-v1' / 'lean_source_scan.py')},
        'expected_audit_log_sha256': sha256(HERE / 'logs' / 'Audit38.build.log'),
        'modules': MODULES, 'negative': NEGATIVE, 'fresh': FRESH,
        'roots': ROOTS,
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
    env = dict(os.environ, MCD_BUILD=str(out / 'build'), MCD_LOGS=str(out / 'logs'), MCD_THREADS='1')
    result = {'status': 'FAILED', 'tag': tag, 'started_at_pt': stamp(), 'steps': [],
              'driver_sha256': sha256(__file__),
              'trust_limits': [
                  'Same Lean 4.34.1 kernel implementation (lean and leanchecker of one toolchain); not Comparator, not an independent kernel.',
                  'Prebuilt Mathlib d13f23b oleans from the read-only cache are trusted as compiled artifacts for elaboration; leanchecker --fresh re-checks every declaration in the import closure of the replayed modules, Mathlib included, in a fresh kernel environment.',
                  'decide +kernel proofs are kernel reductions of Bool-valued checkers over Nat / List with GMP-accelerated Nat literals (part of the trusted kernel); no native code evaluation, no Lean.ofReduceBool.',
                  'The Lean literals are the raw certificate copied verbatim (regenerated byte-identically in step 2 and compared section by section in step 3); the theorems are about those literals.',
                  'The meaning of the roots rests on the reviewer reading McdKernel/Target.lean (IsSQS, IsSTS, derivedBlocks, IsPPC, IsColouring, chiPrime, TargetColoured, IsMcDSQS, TargetMc, ColourLowerBound), the unfolded root statements in the Audit38 log, and the Mathlib/core definitions listed in manifest.json definitions.']}
    result_path = out / 'result.json'
    try:
        manifest = json.loads((HERE / 'manifest.json').read_text())
        result['manifest_sha256'] = sha256(HERE / 'manifest.json')
        for rel, digest in manifest['files'].items():
            require(sha256(HERE / rel) == digest, f'Pinned file changed: {rel}')
        require(set(manifest['files']) == {f'McdKernel/{m}.lean' for m in LEAN_FILES} | set(SCRIPTS),
                'Manifest does not list exactly the expected files')
        require(sorted(p.name for p in (HERE / 'McdKernel').glob('*.lean')) ==
                sorted(f'{m}.lean' for m in LEAN_FILES), 'Unexpected Lean file in McdKernel/')
        require(sha256(REVIEW / RAW) == RAW_SHA256 == manifest['input']['sha256'], 'raw certificate changed')
        result['input'] = manifest['input']
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
        run(['python3', '-B', 'gen_lean.py', str(out / 'regenerated')], 'generate38', out, result['steps'], env)
        regenerated = out / 'regenerated' / 'Data38.lean'
        require(regenerated.read_bytes() == (HERE / 'McdKernel' / 'Data38.lean').read_bytes(),
                'Regenerated Data38.lean differs from the pinned module')
        result['regenerated'] = {'Data38.lean': sha256(regenerated)}
        # 3. binding audit
        audit_receipt = out / 'binding-audit.json'
        run(['python3', '-B', 'audit_binding.py', str(audit_receipt)], 'binding-audit', out, result['steps'], env)
        audit = json.loads(audit_receipt.read_text())
        require(audit['status'] == 'BINDING_AUDIT_PASS', 'binding audit failed')
        require(audit['lean_data_module'].get('manifest_pin_matches') is True, 'binding audit pin mismatch')
        require(all(c['as_intended'] for c in audit['controls'].values()), 'binding audit control failed')
        result['binding_audit'] = {'receipt': str(audit_receipt.relative_to(HERE)), 'sha256': sha256(audit_receipt),
                                   'status': audit['status'], 'result': audit['result'],
                                   'controls': {k: c['as_intended'] for k, c in audit['controls'].items()}}
        # 4. source scan
        scan_spec = importlib.util.spec_from_file_location('mcd_lean_scan', HERE / 'lean_source_scan.py')
        scanner = importlib.util.module_from_spec(scan_spec)
        scan_spec.loader.exec_module(scanner)
        require(sha256(HERE / 'lean_source_scan.py') == manifest['scanner_origin']['sha256'],
                'Scanner is not byte-identical to the CDF/LKTS/PC88/RDSQS scanner')
        scan = {'scanner_sha256': sha256(HERE / 'lean_source_scan.py'), 'controls': scanner.controls(), 'files': {}}
        require(scan['controls']['positive_ok'] and scan['controls']['negative_ok'], 'Scanner controls failed')
        for module in LEAN_FILES:
            path = HERE / 'McdKernel' / f'{module}.lean'
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
            run(['sh', 'build_module.sh', f'McdKernel/{module}.lean'], f'build-{module}', out, result['steps'], env)
            log_path = out / 'logs' / f'{module}.build.log'
            log = log_path.read_text()
            timing = (out / 'logs' / f'{module}.build.time').read_text()
            require(not re.search(r':\d+:\d+: error', log), f'Error message in build log of {module}')
            builds[module] = {**time_metrics(timing), 'warnings': len(re.findall(r':\d+:\d+: warning', log)),
                              'build_log_sha256': sha256(log_path),
                              'olean_sha256': sha256(out / 'build' / 'McdKernel' / f'{module}.olean')}
            found = parse_axioms(log)
            for name, listed in found.items():
                require(set(listed) <= ALLOWED_AXIOMS, f'Unexpected axiom for {name}: {listed}')
            if found:
                axioms[module] = found
        audit_log = (out / 'logs' / 'Audit38.build.log').read_text()
        require(sha256(out / 'logs' / 'Audit38.build.log') == manifest['expected_audit_log_sha256'],
                'Audit output differs from the pinned expected output')
        for root, typ in ROOTS.items():
            require(f'{root} : {typ}' in audit_log, f'Missing root type line for {root}')
            require(root in axioms['Audit38'], f'Missing axiom report for {root}')
        require('def Mcd.TargetMc : ℕ → Prop :=' in audit_log, 'Missing printed TargetMc definition')
        result['builds'] = builds
        result['axioms'] = axioms
        result['printed_audit_output'] = audit_log
        # 6. negative control
        negatives = {}
        for module in NEGATIVE:
            _, _, item = run(['sh', 'build_module.sh', f'McdKernel/{module}.lean'], f'build-{module}', out,
                             result['steps'], env, expect_success=False)
            log_path = out / 'logs' / f'{module}.build.log'
            log = log_path.read_text()
            require(item['exit_code'] != 0, f'Negative control {module} unexpectedly built')
            for pattern in NEGATIVE_EXPECT[module]:
                require(re.search(pattern, log), f'Negative control {module}: missing {pattern!r}')
            require(not (out / 'build' / 'McdKernel' / f'{module}.olean').exists(),
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
        result['roots'] = {root: {'type_prefix': typ, 'axioms': axioms['Audit38'][root],
                                  'fresh_replay_module': 'McdKernel.Audit38'} for root, typ in ROOTS.items()}
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
