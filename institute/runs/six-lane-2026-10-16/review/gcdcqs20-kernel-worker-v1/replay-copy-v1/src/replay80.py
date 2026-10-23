#!/usr/bin/env python3
"""Clean-directory rebuild and fresh kernel replay of the gcDCQS(20^4 : 0) and mcDSQS(80) roots.

Usage:
  python3 -B replay80.py --write-manifest AUDIT_LOG   # once, by the worker: pin every source by
                                                      # SHA-256 and the expected Audit80 output
  python3 -B replay80.py OUT_DIR [--jobs N]   # OUT_DIR must not exist; it is created, and the
                                              # replay writes only inside it (N <= 4, default 2)

Inputs: the Lean sources and scripts of this directory (pinned in manifest.json), the two raw
certificates under the review directory ($GC80_REVIEW if set, else the parent directory of this
script), the Lean 4.34.1 toolchain and the prebuilt Mathlib d13f23b cache (read-only, through
lean_env.sh).  Every Lean process uses one elaboration thread (MCD_THREADS=1); at most N Lean
processes run at once (default 2).  A step that exceeds its time limit gets SIGTERM and a
bounded wait, and the replay stops with status FAILED (outcome unknown, not a pass).

Steps:
 1. pins: every file in manifest.json has its recorded SHA-256; McdKernel/ and Gc80/ contain
    exactly the pinned Lean files; McdKernel/{Target,Check,Counts}.lean, lean_env.sh and
    build_module.sh are byte-identical to the reviewed mcDSQS(38) parent-replay copies; the raw
    certificates, the toolchain binaries, Mathlib.olean and the cache's lean-toolchain /
    lakefile.lean / lake-manifest.json match; every listed definition is at the recorded line;
 2. gen_lean80.py regenerates the 20 data modules into OUT_DIR/regenerated, byte-identical to
    the pinned Gc80/Data*.lean;
 3. audit_binding80.py (stdlib, no code shared with gen_lean80.py) checks that the Lean
    literals equal the raw certificates section by section, re-checks both raw certificates
    definition-first, and runs its corruption controls, which must all behave as intended;
 4. lean_source_scan.py (byte-identical copy of the reviewed kernel scanner) passes its own
    controls, and no Lean source has any hit;
 5. every module is compiled into OUT_DIR/build in dependency order; no build log has an error;
    every `#print axioms` line is within {propext, Classical.choice, Quot.sound}; the Audit80
    log equals the pinned expected output byte for byte;
 6. negative controls: every Gc80/Neg<Statement>.lean is Gc80/PosTwin.lean with exactly its
    recorded mutation of one statement (re-applied here and compared byte for byte); each must
    FAIL with `Type mismatch` at the mutated theorem, which alone depends on sorryAx;
    NegKernelSwap must FAIL with the kernel rejecting `decide +kernel`; no olean is written;
 7. leanchecker --fresh replays Gc80.Audit80 (all roots) and Gc80.Controls80 (their whole import
    closures, Mathlib included) in a fresh kernel environment;
 8. OUT_DIR/result.json records hashes, times, peak RSS, logs and the axiom reports.
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
REVIEW = Path(os.environ.get('GC80_REVIEW', HERE.parent)).resolve()
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
REUSED = {  # byte-identical copies of the reviewed mcDSQS(38) machinery
    'McdKernel/Target.lean': 'cda6cd33ae29ed77e21367f24a7ddbccdb64351330db43a8191777de42c539b0',
    'McdKernel/Check.lean': 'd92978adddaddf1c232d75540e153cd2de489b1cddf41228220c3e8eccc5f3c3',
    'McdKernel/Counts.lean': 'dd2f30e6f3bb71300d50102032753ddf519acb80efb3b79371e73d71f1667fbd',
    'lean_env.sh': '3a2660673e5e159ef34ec4eee722db2b956c7df2ac63b0ddabfd7992427feef3',
    'build_module.sh': '0b3710ace8b5feb98fb7145894765cedf0098c6b4d32ca8ef97fbeffba332482',
}
REUSED_ORIGIN = 'review/mcdsqs38-kernel-parent-replay-v1 (parent-result.json source_pins)'
DATA = [f'Gc80/Data{k}{s}.lean' for k in ['Gc', 'Mc'] for s in ['B'] + [f'P{m}' for m in range(8)] + ['']]
MODULES = (['McdKernel/Target', 'McdKernel/Check', 'McdKernel/Counts', 'Gc80/GcTarget', 'Gc80/Derived',
            'Gc80/Check80', 'Gc80/Counts79'] + [d[:-5] for d in DATA] +
           [f'Gc80/Cert{k}Pts{m}' for k in ['Mc', 'Gc'] for m in range(4)] +
           ['Gc80/CertMc', 'Gc80/CertGc', 'Gc80/Audit80', 'Gc80/Controls80', 'Gc80/PosTwin'])
MUTATIONS = {
    'NegPointCount81': {'theorem': 'twin_mc80', 'replace': [['Fin 80', 'Fin 81', 4], ['Fin 79', 'Fin 80', 3]],
                        'intent': 'wrong point count: an SQS on Fin 81 whose derived designs have chi′(80) colours'},
    'NegBlockSize5': {'theorem': 'twin_gc80', 'replace': [['(∀ X ∈ A, X.card = 4)', '(∀ X ∈ A, X.card = 5)', 1]],
                      'intent': 'wrong block size: gcDCQS blocks of size 5'},
    'NegColours39': {'theorem': 'twin_gc80', 'replace': [['C.card = 40 ∧', 'C.card = 39 ∧', 1]],
                     'intent': '39 colour classes instead of 40 at every point'},
    'NegHoleFree9': {'theorem': 'twin_gc80', 'replace': [['erase x)).card = 10', 'erase x)).card = 9', 1]],
                     'intent': '9 hole-free classes instead of 10 at every point'},
}
NEGATIVE = list(MUTATIONS) + ['NegKernelSwap']
FRESH = ['Gc80.Audit80', 'Gc80.Controls80']
LEAN_FILES = sorted([f'{m}.lean' for m in MODULES] + [f'Gc80/{n}.lean' for n in NEGATIVE])
SCRIPTS = ['lean_env.sh', 'build_module.sh', 'lean_source_scan.py', 'gen_lean80.py', 'audit_binding80.py',
           'replay80.py']
RAWS = {'review/gcdcqs20-parent-inputs-v1/gcdcqs20-e1s1_p10.txt':
        '58b51b50b5281df613c5fae0a3b0178a374554a2f062e55bd8fc25250922a0ca',
        'review/mcdsqs80-parent-inputs-v1/mcdsqs80_c21_A.txt':
        '49f500c5eedd9a79553e1228d0232e203a749bbda04e3a891c52778dbe9d44a3'}
SCANNER_ORIGIN = 'mcdsqs-kernel-worker-v1/lean_source_scan.py'
ROOTS = {
    'Mcd.Audit.root_mc80': 'Mcd.TargetMc 80',
    'Mcd.Audit.root_chi79': 'Mcd.chiPrime 79 = 40',
    'Mcd.Audit.root_lower79': 'Mcd.ColourLowerBound 79 40',
    'Mcd.Audit.root_coloured80': 'Mcd.TargetColoured 80 40',
    'Mcd.Audit.witness_mc80': 'Mcd.IsMcDSQS Mcd.Kernel.mcdsqs80 ∧',
    'Mcd.Audit.root_chi79_unfolded': 'sInf',
    'Mcd.Audit.root_lower79_unfolded': '∀ (W : Type u_1) [inst : Fintype W] [DecidableEq W],',
    'Mcd.Audit.root_mc80_unfolded': '∃ B,',
    'Mcd.Audit.root_gc80': 'Mcd.TargetGc80',
    'Mcd.Audit.root_gc80_counts': '∃ A, Mcd.IsGcDCQS0 Mcd.groups80 A ∧ A.card = 19400 ∧',
    'Mcd.Audit.groups80_spec': 'Mcd.IsGroupPartition Mcd.groups80 ∧',
    'Mcd.Audit.root_gc80_numerals': '∃ A,',
    'Mcd.Audit.witness_gc80': 'Mcd.IsGcDCQS0 Mcd.groups80 Mcd.Kernel.gcdcqs80 ∧',
    'Mcd.Audit.root_gc80_unfolded': '∃ A,',
}
TOOLCHAIN = Path('/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1/bin')
CORE_SRC = Path('/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1/src/lean')
CACHE = Path('/private/tmp/seymour-lean-20261014-68365')
MATHLIB = CACHE / '.lake/packages/mathlib'
MATHLIB_OLEAN = MATHLIB / '.lake/build/lib/lean/Mathlib.olean'
MATHLIB_REV = 'd13f23b723b8a846827a245b89c10fc7d3f11612'
CACHE_FILES = ['lean-toolchain', 'lakefile.lean', 'lake-manifest.json']
# Every definition the statements of the roots depend on (beyond Lean core logic).
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
    ('Mcd.IsGroupPartition', 'Gc80/GcTarget.lean', 'worker', r'^def IsGroupPartition\b'),
    ('Mcd.IsCQS0', 'Gc80/GcTarget.lean', 'worker', r'^def IsCQS0\b'),
    ('Mcd.IsHoleSTS', 'Gc80/GcTarget.lean', 'worker', r'^def IsHoleSTS\b'),
    ('Mcd.IsGcSTS', 'Gc80/GcTarget.lean', 'worker', r'^def IsGcSTS\b'),
    ('Mcd.IsGcDCQS0', 'Gc80/GcTarget.lean', 'worker', r'^def IsGcDCQS0\b'),
    ('Mcd.grp80', 'Gc80/GcTarget.lean', 'worker', r'^def grp80\b'),
    ('Mcd.groups80', 'Gc80/GcTarget.lean', 'worker', r'^def groups80\b'),
    ('Mcd.TargetGc80', 'Gc80/GcTarget.lean', 'worker', r'^def TargetGc80\b'),
    ('Mcd.Kernel.RawQuad (witness only)', 'McdKernel/Check.lean', 'worker', r'^abbrev RawQuad\b'),
    ('Mcd.Kernel.RawTriple (witness only)', 'McdKernel/Check.lean', 'worker', r'^abbrev RawTriple\b'),
    ('Mcd.Kernel.pt (witness only)', 'McdKernel/Check.lean', 'worker', r'^def pt\b'),
    ('Mcd.Kernel.quad (witness only)', 'McdKernel/Check.lean', 'worker', r'^def quad\b'),
    ('Mcd.Kernel.tri (witness only)', 'McdKernel/Check.lean', 'worker', r'^def tri\b'),
    ('Mcd.Kernel.blockSet (witness only)', 'McdKernel/Check.lean', 'worker', r'^@\[irreducible\] def blockSet\b'),
    ('Mcd.Kernel.tripleSet (witness only)', 'McdKernel/Check.lean', 'worker', r'^@\[irreducible\] def tripleSet\b'),
    ('Mcd.Kernel.classSet (witness only)', 'McdKernel/Check.lean', 'worker', r'^@\[irreducible\] def classSet\b'),
    ('Mcd.Kernel.blocksMc80 (witness only, generated)', 'Gc80/DataMcB.lean', 'worker', r'^def blocksMc80 :'),
    ('Mcd.Kernel.colourMc80 (witness only, generated)', 'Gc80/DataMc.lean', 'worker', r'^def colourMc80 :'),
    ('Mcd.Kernel.blocksGc80 (witness only, generated)', 'Gc80/DataGcB.lean', 'worker', r'^def blocksGc80 :'),
    ('Mcd.Kernel.groupsGc80 (raw GROUPS, generated)', 'Gc80/DataGcB.lean', 'worker', r'^def groupsGc80 :'),
    ('Mcd.Kernel.colourGc80 (witness only, generated)', 'Gc80/DataGc.lean', 'worker', r'^def colourGc80 :'),
    ('Mcd.Kernel.mcdsqs80 (witness only)', 'Gc80/CertMc.lean', 'worker', r'^def mcdsqs80\b'),
    ('Mcd.Kernel.colouringMc80 (witness only)', 'Gc80/CertMc.lean', 'worker', r'^def colouringMc80\b'),
    ('Mcd.Kernel.gcdcqs80 (witness only)', 'Gc80/CertGc.lean', 'worker', r'^def gcdcqs80\b'),
    ('Mcd.Kernel.colouringGc80 (witness only)', 'Gc80/CertGc.lean', 'worker', r'^def colouringGc80\b'),
    ('ExistsUnique', 'Mathlib/Basic/ExistsUnique.lean', 'mathlib', r'^def ExistsUnique '),
    ('Finset', 'Mathlib/Data/Finset/Defs.lean', 'mathlib', r'^structure Finset '),
    ('Finset.card', 'Mathlib/Data/Finset/Card.lean', 'mathlib', r'^def card \(s : Finset'),
    ('Finset.image', 'Mathlib/Data/Finset/Image.lean', 'mathlib', r'^def image \('),
    ('Finset.filter', 'Mathlib/Data/Finset/Filter.lean', 'mathlib', r'^def filter \(s : Finset'),
    ('Finset.erase', 'Mathlib/Data/Finset/Erase.lean', 'mathlib', r'^def erase \(s : Finset'),
    ('Finset.Nonempty', 'Mathlib/Data/Finset/Empty.lean', 'mathlib', r'^protected def Nonempty \(s : Finset'),
    ('Finset.univ', 'Mathlib/Data/Fintype/Defs.lean', 'mathlib', r'^def univ : Finset α'),
    ('Disjoint', 'Mathlib/Order/Disjoint.lean', 'mathlib', r'^def Disjoint \(a b : α\)'),
    ('InfSet (sInf)', 'Mathlib/Order/SetNotation.lean', 'mathlib', r'^class InfSet '),
    ('InfSet ℕ (sInf on ℕ: least element via Nat.find, 0 for the empty set)',
     'Mathlib/Order/Lattice/Nat.lean', 'mathlib', r'^noncomputable instance : InfSet ℕ'),
    ('Fintype', 'Mathlib/Data/Fintype/Defs.lean', 'mathlib', r'^class Fintype '),
    ('Fintype.card', 'Mathlib/Data/Fintype/Card.lean', 'mathlib', r'^def card \(α\)'),
    ('Fin', 'Init/Prelude.lean', 'core', r'^structure Fin \(n : Nat\)'),
]
SEMANTICS = {
    'points': 'Fin 80 = {0, ..., 79} for both designs; chiPrime n ranges over STS on Fin n; ColourLowerBound n r: every type W with [Fintype W], Fintype.card W = n, and an arbitrary [DecidableEq W] instance.',
    'sqs_sts_colouring': 'IsSQS, IsSTS, derivedBlocks, IsPPC, IsColouring, chiPrime, TargetColoured, IsMcDSQS, TargetMc, ColourLowerBound: McdKernel/Target.lean, byte-identical to the reviewed mcDSQS(38) target module (Tan–Zhou §1).',
    'groups': 'grp80 i := {y : Fin 80 | 20 i ≤ y < 20 i + 20}; groups80 := {grp80 0, grp80 1, grp80 2, grp80 3}; groups80_spec (kernel + proofs): a partition into 4 groups of 20 points equal to the raw GROUPS lines.',
    'cqs': 'IsCQS0 Gs A := IsGroupPartition Gs ∧ (∀ X ∈ A, X.card = 4) ∧ (∀ T, T.card = 3 → (∀ G ∈ Gs, ¬ T ⊆ G) → ∃! X, X ∈ A ∧ T ⊆ X) ∧ ∀ T, T.card = 3 → ∀ G ∈ Gs, T ⊆ G → ∀ X ∈ A, ¬ T ⊆ X (Tan–Zhou candelabra system with t = 3, K = {4}, empty stem).',
    'hole_sts': 'IsHoleSTS Y H D := H ⊆ Y ∧ (∀ T ∈ D, T.card = 3 ∧ T ⊆ Y) ∧ (∀ P, P.card = 2 → P ⊆ Y → ¬ P ⊆ H → ∃! T, T ∈ D ∧ P ⊆ T) ∧ ∀ P, P.card = 2 → P ⊆ H → ∀ T ∈ D, ¬ P ⊆ T (STS(|Y|, |H|), Tan–Zhou §2).',
    'gc_sts': 'IsGcSTS Y H D := IsHoleSTS Y H D ∧ ∃ C, IsColouring D C ∧ C.card = chiPrime |Y| ∧ |{P ∈ C | ∀ T ∈ P, Disjoint T H}| = chiPrime |Y| - (|Y| - |H|) / 2 (gcSTS(v, h): r = χ′(v) PPCs, exactly s = χ′(v) - (v - h)/2 of them PPCs of Y \\ H).',
    'gc_dcqs': 'IsGcDCQS0 Gs A := IsCQS0 Gs A ∧ ∀ G ∈ Gs, ∀ x ∈ G, IsGcSTS (univ \\ {x}) (G \\ {x}) (derivedBlocks A x) (Tan–Zhou gcDCQS(g^n : s) with s = 0; the stem condition (2) is vacuous). TargetGc80 := ∃ A, IsGcDCQS0 groups80 A.',
    'roots': 'root_mc80 : TargetMc 80; root_chi79 : chiPrime 79 = 40; root_lower79 : ColourLowerBound 79 40 (data-independent); root_coloured80 : TargetColoured 80 40; root_gc80 : TargetGc80; root_gc80_counts adds |A| = 19400 and |derivedBlocks A x| = 970 at every x; root_gc80_numerals / root_gc80_unfolded state the gc root with 40 colours and exactly 10 classes avoiding G(x) \\ {x}; unfolded versions state the roots with Mathlib notions only (same proof terms).',
    'witness': 'mcdsqs80 := blockSet 80 blocksMc80 and colouringMc80 x := classSet 80 (colourMc80.getD x []): the raw mcDSQS(80) BLOCKS lines and POINT x classes; gcdcqs80 / colouringGc80 likewise for the gcDCQS. The χ′(79) witness is tripleSet 79 colMc80_79 with classSet 79 colMc80_79: the raw mcDSQS POINT 79 section (numbers 0..78) read on Fin 79.',
    'binding': 'The Gc80/Data*.lean literals are the raw certificates copied verbatim in raw order by gen_lean80.py (raw SHA-256 checked; replay step 2 regenerates them byte-identically); audit_binding80.py (step 3) independently re-parses the raw files and the Lean literals and checks section-by-section equality (BLOCKS, GROUPS, every POINT/CLASS in order). The block-list check (kernel) shows every block is a < b < c < d < 80, and the colouring checker every triple a < b < c < 80, so no reduction modulo 80 occurs.',
    'not_hypotheses': 'The SQS / CQS property, the hole structure, every colouring, the hole-free counts, the STS(79) witness and all counts are not hypotheses of any root: they are kernel evaluations (mc_blocks, gc_blocks, mcPt_0..79, gcPt_0..79, mc79_stsCheck, mc79_length, gc_groups_raw, card_grp80 by decide +kernel) fed to data-independent soundness theorems (blockCheck_sound, pointCheck_sound, gcPointCheck_sound, holeCheck_sound, colCheck_spec, card_filter_classSet, colouring_of_check, sts_of_check) and the data-independent lemmas isSQS_of_derived, isCQS0_of_derived, isHoleSTS_of_derived, card_sts_mul, card_ppc_mul_le, sum_card_colouring, colourLowerBound_79, chiPrime_eq_of.',
    'scope': 'Only these two finite witnesses and χ′(79) = 40 are kernel-checked. The Tan–Zhou constructions (Construction 2.1, Corollary 2.6 and the infinite family) are NOT formalized here.',
}


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def apply_mutation(text, spec):
    start = text.index(f'theorem {spec["theorem"]} ')
    end = text.index(':=\n', start)
    seg = text[start:end]
    for old, new, count in spec['replace']:
        require(seg.count(old) == count, f'mutation {old!r}: {seg.count(old)} occurrences, expected {count}')
        seg = seg.replace(old, new)
    return text[:start] + seg + text[end:]


def expected_negative(name):
    twin = (HERE / 'Gc80' / 'PosTwin.lean').read_text()
    out = apply_mutation(twin, MUTATIONS[name])
    return out.replace('# Positive twin of the statement-mutation controls (this module must BUILD)',
                       f'# Negative control {name} (this module must FAIL to build)', 1)


def imports_of(rel):
    text = (HERE / rel).read_text()
    return [m.replace('.', '/') for m in re.findall(r'^import (\S+)', text, re.M)
            if m.startswith('McdKernel.') or m.startswith('Gc80.')]


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


def write_manifest(expected_audit_log):
    path = HERE / 'manifest.json'
    require(not path.exists(), 'Refusing to overwrite manifest.json')
    files = {rel: sha256(HERE / rel) for rel in LEAN_FILES}
    files.update({name: sha256(HERE / name) for name in SCRIPTS})
    for rel, digest in REUSED.items():
        require(files[rel] == digest, f'{rel} is not byte-identical to the reviewed copy')
    for name in MUTATIONS:
        require((HERE / 'Gc80' / f'{name}.lean').read_text() == expected_negative(name),
                f'{name} is not PosTwin with its mutation')
    for rel, digest in RAWS.items():
        require(sha256(REVIEW / rel.removeprefix('review/')) == digest, f'{rel}: SHA-256 mismatch')
    manifest = {
        'recorded_at_pt': stamp(),
        'files': files,
        'reused_byte_identical': {'origin': REUSED_ORIGIN, 'files': REUSED},
        'inputs': RAWS,
        'toolchain': {'lean_sha256': sha256(TOOLCHAIN / 'lean'),
                      'leanchecker_sha256': sha256(TOOLCHAIN / 'leanchecker'),
                      'mathlib_rev': MATHLIB_REV,
                      'mathlib_olean_sha256': sha256(MATHLIB_OLEAN),
                      'cache_files': {name: sha256(CACHE / name) for name in CACHE_FILES}},
        'scanner_origin': {'path': f'review/{SCANNER_ORIGIN}', 'sha256': sha256(REVIEW / SCANNER_ORIGIN)},
        'expected_audit_log_sha256': sha256(expected_audit_log),
        'modules': MODULES, 'negative': NEGATIVE, 'mutations': MUTATIONS, 'fresh': FRESH,
        'roots': ROOTS,
        'definitions': locate_definitions(),
        'semantics': SEMANTICS,
    }
    with path.open('x') as stream:
        json.dump(manifest, stream, indent=2, ensure_ascii=False)
        stream.write('\n')
    print(json.dumps({'manifest': str(path), 'sha256': sha256(path)}))


def start(command, name, out_dir, env):
    stdout = out_dir / 'logs' / f'{name}.stdout.txt'
    stderr = out_dir / 'logs' / f'{name}.stderr.txt'
    out, err = stdout.open('x'), stderr.open('x')
    proc = subprocess.Popen(command, cwd=HERE, stdin=subprocess.DEVNULL, stdout=out, stderr=err, env=env,
                            start_new_session=True)
    return {'proc': proc, 'files': (out, err), 'name': name, 'command': command, 'started': time.monotonic(),
            'stdout': stdout, 'stderr': stderr}


def finish(job, steps, timed_out=False):
    for f in job['files']:
        f.close()
    item = {'step': job['name'], 'command': job['command'], 'exit_code': job['proc'].returncode,
            'timeout': timed_out, 'wall_seconds': round(time.monotonic() - job['started'], 3),
            'stdout': str(job['stdout'].name), 'stderr': str(job['stderr'].name)}
    steps.append(item)
    print(json.dumps({'step': item['step'], 'exit_code': item['exit_code'], 'wall_seconds': item['wall_seconds'],
                      'at': stamp()}), flush=True)
    return item


def terminate(job):
    """SIGTERM to the process group, then a bounded wait; the outcome is unknown, not a pass."""
    try:
        os.killpg(job['proc'].pid, signal.SIGTERM)
    except ProcessLookupError:
        pass
    deadline = time.monotonic() + 60
    while job['proc'].poll() is None and time.monotonic() < deadline:
        time.sleep(1)


def run(command, name, out_dir, steps, env, timeout=3600, expect_success=True):
    job = start(command, name, out_dir, env)
    while job['proc'].poll() is None:
        if time.monotonic() - job['started'] > timeout:
            terminate(job)
            item = finish(job, steps, timed_out=True)
            raise ValueError(f'{name} exceeded {timeout} s (SIGTERM sent; outcome UNKNOWN)')
        time.sleep(0.5)
    item = finish(job, steps)
    if expect_success:
        require(item['exit_code'] == 0, f'{name} did not complete successfully')
    return job['stdout'].read_text(), job['stderr'].read_text(), item


def build_all(modules, jobs, out_dir, steps, env, timeout=3600):
    deps = {m: [d for d in imports_of(f'{m}.lean')] for m in modules}
    for m, ds in deps.items():
        require(all(d in modules for d in ds), f'{m} imports a module outside the build list: {ds}')
    done, running, pending = set(), [], list(modules)
    while pending or running:
        for job in list(running):
            if job['proc'].poll() is not None:
                running.remove(job)
                item = finish(job, steps)
                require(item['exit_code'] == 0, f'{job["name"]} did not complete successfully')
                done.add(job['module'])
            elif time.monotonic() - job['started'] > timeout:
                for other in running:
                    terminate(other)
                    finish(other, steps, timed_out=True)
                raise ValueError(f'{job["name"]} exceeded {timeout} s (SIGTERM sent; outcome UNKNOWN)')
        ready = [m for m in pending if all(d in done for d in deps[m])]
        while ready and len(running) < jobs:
            m = ready.pop(0)
            pending.remove(m)
            job = start(['sh', 'build_module.sh', f'{m}.lean'], f'build-{Path(m).name}', out_dir, env)
            job['module'] = m
            running.append(job)
        if not ready and not running and pending:
            raise ValueError(f'unsatisfiable dependencies: {pending}')
        time.sleep(0.5)


def time_metrics(text):
    real = re.search(r'([0-9.]+) real', text)
    rss = re.search(r'([0-9]+)\s+maximum resident set size', text)
    peak = re.search(r'([0-9]+)\s+peak memory footprint', text)
    return {'real_seconds': float(real.group(1)) if real else None,
            'max_rss_bytes': int(rss.group(1)) if rss else None,
            'peak_memory_footprint_bytes': int(peak.group(1)) if peak else None}


def parse_axioms(log):
    axioms = {name: sorted(x.strip() for x in listed.split(',') if x.strip())
              for name, listed in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log)}
    for name in re.findall(r"'([^']+)' does not depend on any axioms", log):
        axioms[name] = []
    return axioms


def main(out_arg, jobs):
    out = Path(out_arg).resolve()
    out.mkdir(parents=False, exist_ok=False)
    for sub in ['build', 'logs', 'regenerated']:
        (out / sub).mkdir()
    env = dict(os.environ, MCD_BUILD=str(out / 'build'), MCD_LOGS=str(out / 'logs'), MCD_THREADS='1',
               GC80_REVIEW=str(REVIEW))
    result = {'status': 'FAILED', 'source_dir': str(HERE), 'out_dir': str(out), 'review_dir': str(REVIEW),
              'jobs': jobs,
              'started_at_pt': stamp(), 'steps': [], 'driver_sha256': sha256(__file__),
              'trust_limits': [
                  'Same Lean 4.34.1 kernel implementation (lean and leanchecker of one toolchain); not Comparator, not an independent kernel.',
                  'Prebuilt Mathlib d13f23b oleans from the read-only cache are trusted as compiled artifacts for elaboration; leanchecker --fresh re-checks every declaration in the import closure of the replayed modules, Mathlib included, in a fresh kernel environment.',
                  'decide +kernel proofs are kernel reductions of Bool-valued checkers over Nat / List with GMP-accelerated Nat literals (part of the trusted kernel); no native code evaluation, no Lean.ofReduceBool.',
                  'The Lean literals are the raw certificates copied verbatim (regenerated byte-identically in step 2 and compared section by section in step 3); the theorems are about those literals.',
                  'The meaning of the roots rests on the reviewer reading McdKernel/Target.lean and Gc80/GcTarget.lean, the printed definitions and root types in the Audit80 log, and the Mathlib/core definitions listed in manifest.json definitions.',
                  'Only the two finite witnesses and chi′(79) = 40 are kernel-checked; the Tan–Zhou constructions and the infinite family are not formalized.']}
    result_path = out / 'result.json'
    try:
        # 1. pins
        manifest = json.loads((HERE / 'manifest.json').read_text())
        result['manifest_sha256'] = sha256(HERE / 'manifest.json')
        for rel, digest in manifest['files'].items():
            require(sha256(HERE / rel) == digest, f'Pinned file changed: {rel}')
        require(set(manifest['files']) == set(LEAN_FILES) | set(SCRIPTS), 'Manifest does not list exactly the expected files')
        for sub in ['McdKernel', 'Gc80']:
            require(sorted(f'{sub}/{p.name}' for p in (HERE / sub).glob('*.lean')) ==
                    sorted(f for f in LEAN_FILES if f.startswith(f'{sub}/')), f'Unexpected Lean file in {sub}/')
        for rel, digest in REUSED.items():
            require(sha256(HERE / rel) == digest == manifest['reused_byte_identical']['files'][rel],
                    f'{rel} is not the reviewed copy')
        for rel, digest in RAWS.items():
            require(sha256(REVIEW / rel.removeprefix('review/')) == digest == manifest['inputs'][rel], f'{rel} changed')
        result['inputs'] = manifest['inputs']
        tool = manifest['toolchain']
        require(sha256(TOOLCHAIN / 'lean') == tool['lean_sha256'], 'lean binary changed')
        require(sha256(TOOLCHAIN / 'leanchecker') == tool['leanchecker_sha256'], 'leanchecker binary changed')
        require(sha256(MATHLIB_OLEAN) == tool['mathlib_olean_sha256'], 'Mathlib.olean changed')
        for name, digest in tool['cache_files'].items():
            require(sha256(CACHE / name) == digest, f'Cache file changed: {name}')
        definitions = locate_definitions()
        require([(d['name'], d['file'], d['line']) for d in definitions] ==
                [(d['name'], d['file'], d['line']) for d in manifest['definitions']], 'A listed definition moved')
        result['definitions'] = definitions
        # 2. regenerate the data modules
        run(['python3', '-B', 'gen_lean80.py', str(out / 'regenerated')], 'generate', out, result['steps'], env)
        regen = {}
        for rel in DATA:
            require((out / 'regenerated' / rel).read_bytes() == (HERE / rel).read_bytes(),
                    f'Regenerated {rel} differs from the pinned module')
            regen[rel] = sha256(out / 'regenerated' / rel)
        require(sorted(p.name for p in (out / 'regenerated' / 'Gc80').glob('*.lean')) ==
                sorted(Path(d).name for d in DATA), 'Generator wrote unexpected files')
        result['regenerated'] = regen
        # 3. binding audit
        receipt = out / 'binding-audit.json'
        run(['python3', '-B', 'audit_binding80.py', str(HERE), str(receipt)], 'binding-audit', out,
            result['steps'], env)
        audit = json.loads(receipt.read_text())
        require(audit['status'] == 'BINDING_AUDIT_PASS', 'binding audit failed')
        for key, entry in audit['designs'].items():
            require(entry['status'] == 'PASS', f'binding audit {key} failed')
            for rel, digest in entry['lean_data_modules'].items():
                require(digest == manifest['files'][rel], f'binding audit read an unpinned {rel}')
            require(all(c['as_intended'] for c in entry['controls'].values()), f'binding audit {key}: control failed')
        result['binding_audit'] = {'receipt': receipt.name, 'sha256': sha256(receipt),
                                   'designs': {k: {'result': e['result'],
                                                   'controls': {c: o['as_intended'] for c, o in e['controls'].items()}}
                                               for k, e in audit['designs'].items()}}
        # 4. source scan
        spec = importlib.util.spec_from_file_location('gc80_lean_scan', HERE / 'lean_source_scan.py')
        scanner = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(scanner)
        require(sha256(HERE / 'lean_source_scan.py') == manifest['scanner_origin']['sha256'],
                'Scanner is not byte-identical to the reviewed kernel scanner')
        scan = {'scanner_sha256': sha256(HERE / 'lean_source_scan.py'), 'controls': scanner.controls(), 'files': {}}
        require(scan['controls']['positive_ok'] and scan['controls']['negative_ok'], 'Scanner controls failed')
        for rel in LEAN_FILES:
            hits, declarations, imports = scanner.scan_text((HERE / rel).read_text())
            require(not hits, f'Forbidden Lean construct in {rel}: {hits}')
            set_options = re.findall(r'^\s*set_option\s+(\S+)', (HERE / rel).read_text(), re.M)
            scan['files'][rel] = {'sha256': sha256(HERE / rel), 'hits': hits, 'imports': imports,
                                  'declarations': len(declarations), 'set_options': set_options}
        result['source_scan'] = scan
        # 5. rebuild
        version, _, _ = run(['sh', '-c', '. ./lean_env.sh; exec "$LEAN" --version'], 'lean-version', out,
                            result['steps'], env)
        result['toolchain'] = {'lean_version': version.strip(), **tool}
        build_all(MODULES, jobs, out, result['steps'], env)
        builds, axioms = {}, {}
        for m in MODULES:
            base = Path(m).name
            log_path = out / 'logs' / f'{base}.build.log'
            log = log_path.read_text()
            require(not re.search(r':\d+:\d+: error', log), f'Error message in build log of {m}')
            builds[m] = {**time_metrics((out / 'logs' / f'{base}.build.time').read_text()),
                         'warnings': len(re.findall(r':\d+:\d+: warning', log)),
                         'build_log_sha256': sha256(log_path), 'olean_sha256': sha256(out / 'build' / f'{m}.olean')}
            found = parse_axioms(log)
            for name, listed in found.items():
                require(set(listed) <= ALLOWED_AXIOMS, f'Unexpected axiom for {name}: {listed}')
            if found:
                axioms[m] = found
        audit_log_path = out / 'logs' / 'Audit80.build.log'
        require(sha256(audit_log_path) == manifest['expected_audit_log_sha256'],
                'Audit output differs from the pinned expected output')
        audit_log = audit_log_path.read_text()
        for root, typ in ROOTS.items():
            require(f'{root} : {typ}' in audit_log, f'Missing root type line for {root}')
            require(axioms['Gc80/Audit80'].get(root) is not None, f'Missing axiom report for {root}')
        require('def Mcd.TargetGc80 : Prop :=' in audit_log and 'def Mcd.TargetMc : ℕ → Prop :=' in audit_log,
                'Missing printed target definitions')
        result['builds'] = builds
        result['axioms'] = axioms
        result['printed_audit_output'] = audit_log
        # 6. negative controls
        negatives = {}
        for name in NEGATIVE:
            rel = f'Gc80/{name}.lean'
            if name in MUTATIONS:
                require((HERE / rel).read_text() == expected_negative(name), f'{name} is not PosTwin with its mutation')
            _, _, item = run(['sh', 'build_module.sh', rel], f'build-{name}', out, result['steps'], env,
                             expect_success=False)
            log = (out / 'logs' / f'{name}.build.log').read_text()
            require(item['exit_code'] != 0, f'Negative control {name} unexpectedly built')
            require(not (out / 'build' / 'Gc80' / f'{name}.olean').exists(), f'Negative control {name} produced an olean')
            errors = re.findall(r'^Gc80/' + name + r'\.lean:(\d+):(\d+): error: ([^\n]*)', log, re.M)
            found = parse_axioms(log)
            if name in MUTATIONS:
                spec_m = MUTATIONS[name]
                twin = 'twin_mc80' if spec_m['theorem'] == 'twin_gc80' else 'twin_gc80'
                proof_line = (HERE / rel).read_text().split('\n').index(
                    '  Mcd.Audit.root_' + spec_m['theorem'].removeprefix('twin_') + '_unfolded') + 1
                require(errors == [(str(proof_line), '2', 'Type mismatch')],
                        f'{name}: expected exactly one Type mismatch at line {proof_line}, got {errors}')
                require('sorryAx' in found.get(f'Mcd.Twin.{spec_m["theorem"]}', []), f'{name}: mutated theorem lacks sorryAx')
                require(set(found.get(f'Mcd.Twin.{twin}', ['missing'])) <= ALLOWED_AXIOMS, f'{name}: untouched twin affected')
            else:
                require(len(errors) == 1 and errors[0][2] == '(kernel) application type mismatch',
                        f'{name}: expected the kernel to reject decide +kernel, got {errors}')
                require('sorryAx' in found.get('Mcd.Kernel.Controls.gc_swap_colouring', []),
                        f'{name}: dependent theorem lacks sorryAx')
            negatives[name] = {'exit_code': item['exit_code'], 'errors': errors, 'axioms': found,
                               'intent': MUTATIONS.get(name, {}).get('intent', 'kernel rejects decide +kernel on a false check'),
                               'mutation': MUTATIONS.get(name, {}).get('replace'),
                               'build_log_sha256': sha256(out / 'logs' / f'{name}.build.log')}
        result['negative_controls'] = negatives
        # 7. fresh replay
        fresh = {}
        for module in FRESH:
            stdout, stderr, item = run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v "$1"',
                                        'fresh', module], f'fresh-{module}', out, result['steps'], env, timeout=7200)
            require(f'replaying {module} with --fresh' in stdout, f'No replay marker for {module}')
            fresh[module] = {**time_metrics(stderr), 'exit_code': item['exit_code'], 'wall_seconds': item['wall_seconds'],
                             'stdout_sha256': sha256(out / 'logs' / item['stdout'])}
        result['fresh_replay'] = fresh
        result['roots'] = {root: {'type_prefix': typ, 'axioms': axioms['Gc80/Audit80'][root],
                                  'fresh_replay_module': 'Gc80.Audit80'} for root, typ in ROOTS.items()}
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
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '--write-manifest':
        write_manifest(Path(args[1]))
        raise SystemExit(0)
    jobs = 2
    if len(args) == 3 and args[1] == '--jobs':
        jobs = int(args[2])
        args = args[:1]
    if len(args) != 1 or args[0].startswith('-') or not 1 <= jobs <= 4:
        raise SystemExit(__doc__)
    raise SystemExit(main(args[0], jobs))
