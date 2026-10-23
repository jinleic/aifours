#!/usr/bin/env python3
"""Clean-directory rebuild and fresh kernel replay of the point-cyclic existence proofs for v = 112, 136, 160, 196.

Usage:
  python3 -B replay.py --write-manifest   # once, by the worker: pin every source by SHA-256 (no overwrite)
  python3 -B replay.py TAG                # creates replay-TAG/ next to this file and refuses to overwrite it

A replay writes only inside replay-TAG/ (build/, logs/, regenerated/, binding-audit.json, result.json). The Lean 4.34.1
toolchain and the prebuilt Mathlib d13f23b cache are used read-only through lean_env.sh. Every Lean process runs alone
(PC100_THREADS=1). Nothing is deleted or overwritten. Steps:

 1. Pinned files. Every file in manifest.json has its recorded SHA-256, and PCTableKernelR2/ contains exactly the pinned
    Lean files. PC100Kernel/Target.lean and PC100Kernel/Check.lean are byte-identical to the accepted v = 100 package
    (their SHA-256 in ../../point-cyclic100/lean-kernel/manifest.json). The raw certificates and seeds have their
    pinned SHA-256. The toolchain binaries, the Mathlib olean and the cache files match the manifest. Every listed
    definition is still at the recorded file:line.
 2. gen_lean.py, gen_cert.py and gen_controls.py regenerate every generated module into regenerated/, byte-identical to
    the pinned modules.
 3. audit_binding.py (stdlib) checks:
    - the literals equal the raw certificates;
    - the Theorem C' expansion of each seed is byte-identical to its certificate;
    - the Lean objects are the certificates' blocks and classes.
    Its corruption controls must be rejected by the intended checks.
 4. lean_source_scan.py (byte copy of the shared scanner) passes its controls, and no Lean source has a hit.
 5. Every module is compiled into replay-TAG/build in dependency order. No build log has an error, every
    `#print axioms` line is within {propext, Classical.choice, Quot.sound}, and the audit log equals the pinned expected
    output byte for byte.
 6. Negative control: PCTableKernelR2/ControlFail.lean must FAIL. The kernel rejects both corrupted `certCheck ... =
    true` claims, both dependent theorems depend on `sorryAx`, and no olean is written.
 7. leanchecker --fresh replays the audit and controls modules (their whole import closure, Mathlib included).
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
ACCEPTED = LANE.parent / 'point-cyclic100' / 'lean-kernel'
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
ORDERS = [112, 136, 160, 196]
PKG = 'PCTableKernelR2'
GENERIC = ['PC100Kernel/Target', 'PC100Kernel/Check']
GENERATED = [f'{PKG}/Data{v}' for v in ORDERS] + [f'{PKG}/Cert{v}' for v in ORDERS] + \
    [f'{PKG}/Audit', f'{PKG}/Controls', f'{PKG}/ControlFail']
MODULES = GENERIC + [m for v in ORDERS for m in (f'{PKG}/Data{v}', f'{PKG}/Cert{v}')] + [f'{PKG}/Audit', f'{PKG}/Controls']
NEGATIVE = [f'{PKG}/ControlFail']
AUDIT = f'{PKG}/Audit'
FRESH = [f'{PKG}.Audit', f'{PKG}.Controls']
ROOTS = {}
for _v in ORDERS:
    ROOTS[f'PCTable.Audit.root{_v}'] = f'PC100.Target {_v}'
    ROOTS[f'PCTable.Audit.root{_v}_shift'] = f'PC100.TargetShift {_v}'
    ROOTS[f'PCTable.Audit.root{_v}_counts'] = f'PC100.TargetCounts {_v}'
    ROOTS[f'PCTable.Audit.root{_v}_cycleType'] = f'(PC100.shift {_v}).cycleType = {{{_v}}}'
LEAN_FILES = GENERIC + GENERATED
SCRIPTS = ['lean_env.sh', 'build_module.sh', 'lean_source_scan.py', 'gen_lean.py', 'gen_cert.py', 'gen_controls.py',
           'audit_binding.py', 'replay.py']
INPUTS = {
    112: ('certs/v112/pc112_t1.cert', '96265b66f4495e5927224599c941993d96bed85fb3d008b7dd53b925224a440d',
          'certs/v112/pc112_t1.seed', '9836c5030b61ad3c2bef183a4145a9029c605bdec7258e24c51e0236be22d4b1'),
    136: ('certs/v136/pc136_t3.cert', '61874100bd9333a6df83fbbecbbc807e139d985187ddcab6919ea4f815895c56',
          'certs/v136/pc136_t3.seed', '7f5057833fb25edabd3e6ad78d6dae81bed94a1a4a0aef4ef070ea484280da5b'),
    160: ('certs/v160/pc160_t3.cert', '8928dd9bd61c77da974d352f26f1980248445c5912428d943d4db3e22141a923',
          'certs/v160/pc160_t3.seed', 'd81b4af2546c7130c6288c305c6cf948c87569aa2dfd953addfb4d0374f219f7'),
    196: ('certs/v196/pc196_t2.cert', '0828bf23d3bcd8a00a544cf7b8f1ae9e3a39279bc71a98fedd229eda5c6d8db5',
          'certs/v196/pc196_t2.seed', '2709520472d8941518674a584560e26c782fce663040de2cfd6f63338ba36d26'),
}
ACCEPTED_GENERIC = {'PC100Kernel/Target.lean': '26f601366d6b9c18d3a187e1b5eea6a6ee8e25f212723cbc85fa785f0382c4fa',
                    'PC100Kernel/Check.lean': 'f65e523eac4a4dd47a74adfac896ebf27f6dcdc32f7992ec17fe5dbe07d3ed92'}
NEGATIVE_EXPECT = None   # filled from the manifest (patterns recorded from the worker build log)
TOOLCHAIN = Path('/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1/bin')
CORE_SRC = Path('/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1/src/lean')
CACHE = Path('/private/tmp/seymour-lean-20261014-68365')
MATHLIB = CACHE / '.lake/packages/mathlib'
MATHLIB_OLEAN = MATHLIB / '.lake/build/lib/lean/Mathlib.olean'
MATHLIB_REV = 'd13f23b723b8a846827a245b89c10fc7d3f11612'
CACHE_FILES = ['lean-toolchain', 'lakefile.lean', 'lake-manifest.json']
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
] + [(f'PC100.Kernel.cert{v} (witness only, generated)', f'{PKG}/Data{v}.lean', 'worker', rf'^def cert{v} :')
     for v in ORDERS] + [
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
    ('Equiv.Perm.cycleType', 'Mathlib/GroupTheory/Perm/Cycle/Type.lean', 'mathlib', r'^def cycleType '),
    ('Equiv.addRight (to_additive of Equiv.mulRight)', 'Mathlib/Algebra/Group/Units/Equiv.lean', 'mathlib',
     r'^protected def mulRight \(a : G\)'),
    ('Fin.addCommGroup (the + of Fin n)', 'Mathlib/Algebra/Group/Fin/Basic.lean', 'mathlib',
     r'^instance addCommGroup \(n : ℕ\) \[NeZero n\]'),
    ('Fin', 'Init/Prelude.lean', 'core', r'^structure Fin \(n : Nat\)'),
    ('Fin.add', 'Init/Data/Fin/Basic.lean', 'core', r'^protected def add :'),
]


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
        lines = (base / rel).read_text().splitlines()
        hits = [i + 1 for i, line in enumerate(lines) if re.search(pattern, line)]
        require(len(hits) == 1, f'Definition {name}: expected one match of {pattern!r} in {rel}, got {hits}')
        found.append({'name': name, 'file': (rel if anchor == 'worker' else f'{anchor}:{rel}'), 'line': hits[0],
                      'text': lines[hits[0] - 1].strip(), 'file_sha256': sha256(base / rel)})
    return found


def negative_patterns():
    log = (HERE / 'logs-r2' / 'ControlFail.build.log').read_text()
    pats = []
    for m in re.finditer(r'^(' + re.escape(PKG) + r'/ControlFail\.lean:\d+:\d+): error: \(kernel\) application type mismatch',
                         log, re.M):
        pats.append(re.escape(m.group(1)) + r': error: \(kernel\) application type mismatch')
    pats += [r'decide \(certCheck 196 cert196swap = true\) = true',
             r'decide \(certCheck 112 cert112relabel = true\) = true',
             r"'PCTable\.Controls\.swap196_isDesign' depends on axioms: \[propext, sorryAx, Classical\.choice, Quot\.sound\]",
             r"'PCTable\.Controls\.relabel112_shift' depends on axioms: \[propext, sorryAx, Classical\.choice, Quot\.sound\]"]
    return pats


def write_manifest():
    path = HERE / 'manifest.json'
    require(not path.exists(), 'Refusing to overwrite manifest.json')
    files = {f'{m}.lean': sha256(HERE / f'{m}.lean') for m in LEAN_FILES}
    files.update({name: sha256(HERE / name) for name in SCRIPTS})
    for rel, digest in ACCEPTED_GENERIC.items():
        require(files[rel] == digest, f'{rel} is not the accepted v = 100 module')
    for v, (crel, csha, srel, ssha) in INPUTS.items():
        require(sha256(LANE / crel) == csha and sha256(LANE / srel) == ssha, f'input {v} SHA-256 mismatch')
    pats = negative_patterns()
    require(len(pats) == 6, f'expected 2 kernel errors in the worker ControlFail log, got patterns {pats}')
    manifest = {
        'recorded_at_pt': stamp(),
        'files': files,
        'accepted_generic_modules': {'source': 'point-cyclic100/lean-kernel/manifest.json', 'sha256': ACCEPTED_GENERIC},
        'inputs': {str(v): {'cert': {'path': f'point-cyclic-table200/{c}', 'sha256': cs},
                            'seed': {'path': f'point-cyclic-table200/{s}', 'sha256': ss}}
                   for v, (c, cs, s, ss) in INPUTS.items()},
        'toolchain': {'lean_sha256': sha256(TOOLCHAIN / 'lean'), 'leanchecker_sha256': sha256(TOOLCHAIN / 'leanchecker'),
                      'mathlib_rev': MATHLIB_REV, 'mathlib_olean_sha256': sha256(MATHLIB_OLEAN),
                      'cache_files': {name: sha256(CACHE / name) for name in CACHE_FILES}},
        'scanner_origin': {'path': 'review/cdf-kernel-worker-v1/lean_source_scan.py',
                           'sha256': sha256(REVIEW / 'cdf-kernel-worker-v1' / 'lean_source_scan.py')},
        'expected_audit_log_sha256': sha256(HERE / 'logs-r2' / 'Audit.build.log'),
        'negative_patterns': pats,
        'modules': MODULES, 'negative': NEGATIVE, 'fresh': FRESH, 'roots': ROOTS,
        'definitions': locate_definitions(),
    }
    with path.open('x') as stream:
        json.dump(manifest, stream, indent=2, ensure_ascii=False)
        stream.write('\n')
    print(json.dumps({'manifest': str(path), 'sha256': sha256(path)}))


def run(command, name, out_dir, steps, env, timeout=3600, expect_success=True):
    started = time.monotonic()
    stdout = out_dir / 'logs' / f'{name}.stdout.txt'
    stderr = out_dir / 'logs' / f'{name}.stderr.txt'
    with stdout.open('x') as out, stderr.open('x') as err:
        proc = subprocess.Popen(command, cwd=HERE, stdin=subprocess.DEVNULL, stdout=out, stderr=err, env=env,
                                start_new_session=True)
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
    result = {'status': 'FAILED', 'tag': tag, 'started_at_pt': stamp(), 'steps': [], 'driver_sha256': sha256(__file__),
              'trust_limits': [
                  'Same Lean 4.34.1 kernel implementation (lean and leanchecker of one toolchain); not Comparator.',
                  'Prebuilt Mathlib d13f23b oleans from the read-only cache are trusted as compiled artifacts for elaboration; leanchecker --fresh re-checks every declaration of the import closure of the replayed modules, Mathlib included.',
                  'decide +kernel proofs are kernel reductions of Bool-valued checkers over Nat / List with GMP-accelerated Nat literals; no native code evaluation, no Lean.ofReduceBool.',
                  'The raw-certificate-to-literal equality and the seed-to-certificate expansion are the external stdlib audit audit_binding.py, not Lean theorems.',
                  'The meaning of the roots rests on reading PC100Kernel/Target.lean (byte-identical to the accepted v = 100 module) and the Mathlib/core definitions listed in manifest.json.']}
    result_path = out / 'result.json'
    try:
        manifest = json.loads((HERE / 'manifest.json').read_text())
        result['manifest_sha256'] = sha256(HERE / 'manifest.json')
        for rel, digest in manifest['files'].items():
            require(sha256(HERE / rel) == digest, f'Pinned file changed: {rel}')
        require(set(manifest['files']) == {f'{m}.lean' for m in LEAN_FILES} | set(SCRIPTS),
                'Manifest does not list exactly the expected files')
        require(sorted(p.name for p in (HERE / PKG).glob('*.lean')) ==
                sorted(Path(m).name + '.lean' for m in GENERATED), f'Unexpected Lean file in {PKG}/')
        accepted = json.loads((ACCEPTED / 'manifest.json').read_text())['files']
        for rel, digest in ACCEPTED_GENERIC.items():
            require(sha256(HERE / rel) == digest == accepted[rel] == sha256(ACCEPTED / rel),
                    f'{rel} differs from the accepted v = 100 module')
        for v, (crel, csha, srel, ssha) in INPUTS.items():
            require(sha256(LANE / crel) == csha == manifest['inputs'][str(v)]['cert']['sha256'], f'cert {v} changed')
            require(sha256(LANE / srel) == ssha == manifest['inputs'][str(v)]['seed']['sha256'], f'seed {v} changed')
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
        # 2. regenerate
        regen = out / 'regenerated'
        run(['python3', '-B', 'gen_lean.py', str(regen)], 'generate-data', out, result['steps'], env)
        run(['python3', '-B', 'gen_cert.py', str(regen)] + [str(v) for v in ORDERS], 'generate-cert', out,
            result['steps'], env)
        run(['python3', '-B', 'gen_controls.py', str(regen)], 'generate-controls', out, result['steps'], env)
        result['regenerated'] = {}
        for m in GENERATED:
            name = Path(m).name + '.lean'
            require((regen / name).read_bytes() == (HERE / f'{m}.lean').read_bytes(), f'Regenerated {name} differs')
            result['regenerated'][name] = sha256(regen / name)
        # 3. binding audit
        receipt = out / 'binding-audit.json'
        run(['python3', '-B', 'audit_binding.py', str(receipt)], 'binding-audit', out, result['steps'], env)
        audit = json.loads(receipt.read_text())
        require(audit['status'] == 'BINDING_AUDIT_PASS', 'binding audit failed')
        require(audit.get('manifest_pins_match') is True, 'binding audit pin mismatch')
        require(all(c['as_intended'] for c in audit['controls'].values()), 'binding audit control failed')
        result['binding_audit'] = {'receipt': str(receipt.relative_to(HERE)), 'sha256': sha256(receipt),
                                   'status': audit['status'],
                                   'controls': {k: [c['as_intended'], c.get('check')] for k, c in audit['controls'].items()},
                                   'orders': {k: [x['t'], x['K'], x['blocks'], x['classes'], x['expansion_byte_identical']]
                                              for k, x in audit['result'].items()}}
        # 4. source scan
        spec = importlib.util.spec_from_file_location('pct_scan', HERE / 'lean_source_scan.py')
        scanner = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(scanner)
        require(sha256(HERE / 'lean_source_scan.py') == manifest['scanner_origin']['sha256'], 'Scanner differs')
        scan = {'scanner_sha256': sha256(HERE / 'lean_source_scan.py'), 'controls': scanner.controls(), 'files': {}}
        require(scan['controls']['positive_ok'] and scan['controls']['negative_ok'], 'Scanner controls failed')
        for m in LEAN_FILES:
            hits, declarations, imports = scanner.scan_text((HERE / f'{m}.lean').read_text())
            require(not hits, f'Forbidden Lean construct in {m}: {hits}')
            scan['files'][m] = {'sha256': sha256(HERE / f'{m}.lean'), 'hits': hits, 'imports': imports,
                                'declarations': len(declarations)}
        result['source_scan'] = scan
        # 5. rebuild
        version, _, _ = run(['sh', '-c', '. ./lean_env.sh; exec "$LEAN" --version'], 'lean-version', out,
                            result['steps'], env)
        result['toolchain'] = {'lean_version': version.strip(), **tool}
        builds, axioms = {}, {}
        for m in MODULES:
            base = Path(m).name
            run(['sh', 'build_module.sh', f'{m}.lean'], f'build-{base}', out, result['steps'], env)
            log = (out / 'logs' / f'{base}.build.log').read_text()
            timing = (out / 'logs' / f'{base}.build.time').read_text()
            require(not re.search(r':\d+:\d+: error', log), f'Error message in build log of {m}')
            builds[m] = {**time_metrics(timing), 'warnings': len(re.findall(r':\d+:\d+: warning', log)),
                         'build_log_sha256': sha256(out / 'logs' / f'{base}.build.log'),
                         'olean_sha256': sha256(out / 'build' / f'{m}.olean')}
            found = parse_axioms(log)
            for name, listed in found.items():
                require(set(listed) <= ALLOWED_AXIOMS, f'Unexpected axiom for {name}: {listed}')
            if found:
                axioms[m] = found
        audit_log = (out / 'logs' / 'Audit.build.log').read_text()
        require(sha256(out / 'logs' / 'Audit.build.log') == manifest['expected_audit_log_sha256'],
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
        for m in NEGATIVE:
            base = Path(m).name
            _, _, item = run(['sh', 'build_module.sh', f'{m}.lean'], f'build-{base}', out, result['steps'], env,
                             expect_success=False)
            log = (out / 'logs' / f'{base}.build.log').read_text()
            require(item['exit_code'] != 0, f'Negative control {m} unexpectedly built')
            for pattern in manifest['negative_patterns']:
                require(re.search(pattern, log), f'Negative control {m}: missing {pattern!r}')
            require(not (out / 'build' / f'{m}.olean').exists(), f'Negative control {m} produced an olean')
            negatives[m] = {'exit_code': item['exit_code'], 'build_log_sha256': sha256(out / 'logs' / f'{base}.build.log'),
                            'log': log}
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
        result['roots'] = {root: {'type': typ, 'axioms': axioms[AUDIT][root], 'fresh_replay_module': f'{PKG}.Audit'}
                           for root, typ in ROOTS.items()}
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
