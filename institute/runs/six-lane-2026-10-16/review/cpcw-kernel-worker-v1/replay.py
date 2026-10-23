#!/usr/bin/env python3
"""Freeze, clean rebuild, fresh kernel replay and controls for the eight optimal CPCW certificates.

Usage:
  python3 -B replay.py --write-manifest   # once, by the worker: freeze target-inventory.json and
                                          # manifest.json (refuses to overwrite either)
  python3 -B replay.py TAG                # creates replay-TAG/ next to this file; refuses to overwrite

A replay writes only inside replay-TAG/ (build/, logs/, regenerated/, controls/, result.json); the
Lean 4.34.1 toolchain and the prebuilt Mathlib cache are used read-only through lean_env.sh.  Every
Lean process runs alone (one process at a time, CPCW_THREADS=1).  Steps:

 1. pins: every file in manifest.json has its recorded SHA-256 (Lean sources, scripts, the target
    inventory); CpcwKernel/ holds exactly the expected modules; each raw certificate matches its
    pinned SHA-256 and the parent check receipt review/cpcw{v}-parent-check-v1.json (pinned), which
    must read VALID_OPTIMAL_CPCW with the same v, k, codeword count and SHA-256; the control
    receipts are pinned; the toolchain and Mathlib cache pins (binary SHA-256, lean --version,
    Mathlib revision, lake-manifest, Mathlib.olean and every directly imported Mathlib .olean) are
    recomputed and must be equal; the target definitions re-extracted from Target.lean equal the
    frozen inventory;
 2. lean_source_scan.py (byte-identical copy of the LKTS kernel scanner) passes its own controls,
    no Lean source has any hit, and the import graph equals the frozen one;
 3. raw -> Lean binding: gen_lean.py regenerates every Data/Cert module byte-identically (leave
    from the parent check receipt) and gen_controls.py regenerates both control modules
    byte-identically; separately, an independent regex reader checks that the codeword literals,
    header pair and SHA string of every Data module equal the raw file;
 4. every module is compiled once into replay-TAG/build in dependency order (no error line);
 5. every `#print axioms` line of every build log is within {propext, Classical.choice,
    Quot.sound}; the axioms of every root and audit theorem equal the frozen ones; the root and
    audit types are printed verbatim as expected;
 6. leanchecker --fresh replays CpcwKernel.Audit (the audit root covering all eight cases) and
    CpcwKernel.All (everything, including the optimality bound, facts, bridges and controls);
 7. controls in replay-TAG/controls/:
    * generator: gen_lean.py refuses a wrong expected SHA-256, a wrong --v and a wrong --k;
    * statement: a spelled-out statement (no Cpcw definitions) is proved by each of the eight
      roots, while a changed order, weight, codeword count, multiplicity (perfect code) or a crossed
      root is rejected (`Type mismatch`);
    * data, for each case, in a separate mini-build (fresh copies of Target and Generic): one point
      changed in the raw file, with the frozen Cert module byte-identical, fails at the kernel check;
      a changed header with the frozen Cert module fails at the header theorem; a changed header
      regenerated through gen_lean.py fails at the kernel check;
    * overwrite: rerunning this driver with the same TAG, and --write-manifest, are refused;
 8. replay-TAG/result.json records hashes, times, peak RSS, axioms and printed target definitions.
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
ROOT = HERE.parents[4]
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))
import gen_lean  # noqa: E402  (render functions for the data-level controls)

ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
CASES = {(122, 6): 4, (123, 6): 4, (124, 6): 4, (143, 5): 7, (144, 5): 7, (146, 5): 7, (162, 5): 8,
         (167, 5): 8}
TAGS = {(v, k): f'{v}k{k}' for v, k in CASES}
RAW = {(v, k): f'cpcw{v}-parent-inputs-v1/cpcw_{v}_{k}.txt' for v, k in CASES}
PARENT_CHECK = {(v, k): f'cpcw{v}-parent-check-v1.json' for v, k in CASES}
CONTROL_RECEIPTS = ['review/cpcw-parent-controls-v1/negative-result.json',
                    'review/cpcw-parent-controls-v1/positive-result.json',
                    'information-science/evidence/six-lane-20261016/cpcw-optimal-prep/controls/receipt.json']
MODULES = (['Target', 'Generic', 'Optimality'] +
           [f'{kind}{tag}' for tag in TAGS.values() for kind in ('Data', 'Cert')] +
           ['Audit', 'Facts', 'Bridge', 'Mutations', 'ControlsFixtures', 'ControlsPinned', 'All'])
FRESH = ['CpcwKernel.Audit', 'CpcwKernel.All']
SCRIPTS = ['gen_lean.py', 'gen_controls.py', 'lean_env.sh', 'build_module.sh', 'lean_source_scan.py',
           'replay.py']
INVENTORY = 'target-inventory.json'
TARGET_DEFS = ['diffs', 'IsCPCW', 'IsOptimalCPCW', 'Target', 'OptimalTarget']
TOOLCHAIN = Path('/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1/bin')
CACHE = Path('/private/tmp/seymour-lean-20261014-68365')
MATHLIB_LIB = CACHE / '.lake/packages/mathlib/.lake/build/lib/lean'
SCANNER_ORIGIN = 'lkts-kernel-parent-replay-v1/lean_source_scan.py'


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def root_names(v, k):
    tag = TAGS[(v, k)]
    return f'Cpcw.Kernel.exists_cpcw{tag}', f'Cpcw.Audit.target{tag}'


def root_type(v, k):
    return f'∃ (B : Fin {CASES[(v, k)]} → Fin {k} → Fin {v}), Cpcw.IsOptimalCPCW B'


def load_scanner():
    spec = importlib.util.spec_from_file_location('cpcw_lean_scan', HERE / 'lean_source_scan.py')
    scanner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scanner)
    return scanner


def import_graph(scanner):
    graph = {}
    for module in MODULES:
        _, _, imports = scanner.scan_text((HERE / 'CpcwKernel' / f'{module}.lean').read_text())
        graph[module] = imports
    return graph


def toolchain_pins(scanner):
    version = subprocess.run([str(TOOLCHAIN / 'lean'), '--version'], capture_output=True, text=True,
                             check=True).stdout.strip()
    lake_manifest = CACHE / 'lake-manifest.json'
    rev = next(p['rev'] for p in json.loads(lake_manifest.read_text())['packages'] if p['name'] == 'mathlib')
    mathlib_imports = sorted({m for imports in import_graph(scanner).values() for m in imports
                              if m.startswith('Mathlib.')})
    return {'lean_path': str(TOOLCHAIN / 'lean'), 'lean_version': version,
            'lean_sha256': sha256(TOOLCHAIN / 'lean'), 'leanchecker_sha256': sha256(TOOLCHAIN / 'leanchecker'),
            'mathlib_cache': str(CACHE), 'cache_lake_manifest_sha256': sha256(lake_manifest),
            'mathlib_rev': rev, 'mathlib_olean_sha256': sha256(MATHLIB_LIB / 'Mathlib.olean'),
            'direct_mathlib_imports': {m: sha256(MATHLIB_LIB / (m.replace('.', '/') + '.olean'))
                                       for m in mathlib_imports}}


def target_definitions():
    """Exact source text (doc comment included) of the target definitions in Target.lean."""
    text = (HERE / 'CpcwKernel' / 'Target.lean').read_text()
    defs = {}
    for name in TARGET_DEFS:
        match = re.search(r'(/-- (?:(?!-/).)*?-/\ndef ' + name + r' .*?)\n\n', text, re.S)
        require(match is not None, f'definition {name} not found in Target.lean')
        defs[f'Cpcw.{name}'] = match.group(1)
    return defs


def root_statements():
    out = {}
    for (v, k), n in CASES.items():
        tag = TAGS[(v, k)]
        text = (HERE / 'CpcwKernel' / f'Cert{tag}.lean').read_text()
        match = re.search(rf'theorem exists_cpcw{tag} : (.*?) :=\n', text)
        require(match is not None, f'root statement for {tag} not found')
        out[tag] = match.group(1)
    return out


READING = {
    'Cpcw.diffs': 'The source (p. 1) writes △C = {c_i − c_j | i ≠ j} for one codeword; Cpcw.diffs is the '
                  'multiset union of these over all codewords, indexed by positions (i, j, l) with j ≠ l. For '
                  'injective tuples positions and elements correspond bijectively. [written]',
    'Cpcw.IsCPCW': 'Source p. 2: the auto-correlation property means that all differences of a codeword are '
                   'different, and the cross-correlation property means △C1 ∩ △C2 = ∅; with k-subsets these say '
                   'that every residue occurs at most once in the combined multiset (and 0 never occurs). '
                   'Cpcw.isCPCW_iff_correlation (CpcwKernel.Facts, [kernel]) proves IsCPCW equivalent to '
                   'Definition 1 itself: k-subsets C_i = image (B i) with |C_i ∩ (C_i + t)| ≤ 1 for t ≠ 0 and '
                   '|C_i ∩ (C_j + t)| ≤ 1 for i < j. Fin v with core Fin.sub is Z_v (Cpcw.sub_eq_iff_modEq, '
                   '[kernel]).',
    'Cpcw.IsOptimalCPCW': 'Source p. 2: the size of a (v,k,1) CPCW code cannot exceed ⌊(v − 1)/(k(k − 1))⌋, and '
                          'codes reaching this bound are called optimal. Natural-number division is the floor. '
                          'The bound itself is kernel-checked for every family (Cpcw.IsCPCW.le_bound). [written '
                          'for the identification, kernel for the bound]',
    'Cpcw.Target': 'An optimal (v,k,1) CPCW code exists (some n, with n forced by IsOptimalCPCW). [written]',
    'Cpcw.OptimalTarget': 'Target v k together with the upper bound n ≤ (v − 1)/(k(k − 1)) for every family '
                          'satisfying IsCPCW: the maximum size equals the stated bound. [written]',
}


def freeze_records():
    """Compute the target inventory and the manifest (the inventory's own SHA-256 is added on write)."""
    scanner = load_scanner()
    # The frozen axioms come from the development build logs, which must be builds of exactly
    # the sources being frozen.
    frozen_axioms = {}
    for module in MODULES:
        timing = (HERE / 'dev' / 'logs' / f'{module}.build.time').read_text()
        recorded = re.search(r'module=CpcwKernel/' + module + r'\.lean exit=(\d+) sha256=([0-9a-f]{64})', timing)
        require(recorded and recorded.group(1) == '0' and
                recorded.group(2) == sha256(HERE / 'CpcwKernel' / f'{module}.lean'),
                f'dev build log of {module} is not a passing build of the current source')
        frozen_axioms.update(parse_axioms((HERE / 'dev' / 'logs' / f'{module}.build.log').read_text()))
    wanted = [name for v, k in CASES for name in root_names(v, k)] + ['Cpcw.Audit.allEight']
    roots = {}
    for (v, k), n in CASES.items():
        tag = TAGS[(v, k)]
        root, audit = root_names(v, k)
        parent = json.loads((REVIEW / PARENT_CHECK[(v, k)]).read_text())
        roots[tag] = {'v': v, 'k': k, 'codewords': n, 'bound': f'({v} - 1) / ({k} * ({k} - 1)) = {n}',
                      'root': root, 'root_type': root_type(v, k), 'audit': audit,
                      'audit_type': f'Cpcw.OptimalTarget {v} {k}',
                      'raw_input': f'review/{RAW[(v, k)]}', 'raw_sha256': sha256(REVIEW / RAW[(v, k)]),
                      'parent_check_receipt': f'review/{PARENT_CHECK[(v, k)]}',
                      'leave_from_parent_receipt': parent['uncovered_differences'],
                      'leave_theorem': f'Cpcw.Kernel.cpcw{tag}_counts (audit only; no root depends on it)'}
    inventory = {
        'recorded_at_pt': stamp(),
        'target_module': 'CpcwKernel/Target.lean',
        'target_module_sha256': sha256(HERE / 'CpcwKernel' / 'Target.lean'),
        'target_module_imports': import_graph(scanner)['Target'],
        'target_definitions': {name: {'source': text, 'reading': READING[name]}
                               for name, text in target_definitions().items()},
        'core_semantics': 'a - b on Fin v is core Fin.sub, value (v - b + a) % v (printed by the audit with '
                          'pp.explicit: instance Fin.instSub).',
        'roots': roots,
        'root_statements_in_source': root_statements(),
        'audit_conjunction': {'name': 'Cpcw.Audit.allEight',
                              'statement': ' ∧ '.join(f'Cpcw.OptimalTarget {v} {k}' for v, k in CASES)},
        'generic_theorems': {
            'Cpcw.Kernel.isCPCW_of_check': 'soundness of the kernel checker (data-free): check v k n d = true → '
                                           'Cpcw.IsCPCW (blockOf v hv k n d)',
            'Cpcw.Kernel.count_of_check': 'exact count of every residue under the check (data-free)',
            'Cpcw.Kernel.count_of_leaveCheck': 'exact multiset of differences given a recorded leave (audit only)',
            'Cpcw.IsCPCW.card_mul_le': 'counting bound n * (k * (k - 1)) ≤ v - 1 for every family (data-free)',
            'Cpcw.IsCPCW.le_bound': 'n ≤ (v - 1) / (k * (k - 1)) for 2 ≤ k (data-free)',
            'Cpcw.not_exists_of_bound_lt': 'no family above the bound (data-free)',
            'Cpcw.card_mul_eq_of_perfect': 'a perfect code has n * (k * (k - 1)) = v - 1 (data-free)',
            'Cpcw.isCPCW_iff_correlation': 'difference form ⇔ Definition 1 correlation form (data-free, NeZero v)',
            'Cpcw.IsCPCW.codeword_injective': 'distinct codewords for 2 ≤ k (data-free)',
            'Cpcw.IsCPCW.count_half': 'v / 2 is never a difference (data-free)',
            'Cpcw.IsCPCW.packing': 'the development is a strictly cyclic packing for 2 ≤ k (data-free)'},
        'expected_axioms': {name: frozen_axioms[name] for name in wanted},
        'allowed_axioms': sorted(ALLOWED_AXIOMS),
        'claim_scope': ('Eight finite existence statements, each at the optimal bound ⌊(v − 1)/(k(k − 1))⌋ with the '
                        'bound proved for every family. Not difference families (a perfect code is kernel-proved '
                        'impossible for each case), no nonexistence claim, no classification. Correctness only: '
                        'novelty, priority and significance are separate audits.'),
        'not_covered_by_the_kernel': [
            'Reading Target.lean as the literature notion (the [written] items above).',
            'Raw-to-literal binding (gen_lean.py round trip and an independent Python reader).',
            'Kernel independence: lean and leanchecker belong to one Lean 4.34.1 toolchain; not Comparator.',
            'dev/ holds development builds, one development probe file and development runs of the control '
            'functions (dev/driver-test*); none of it is part of the frozen package or of the replay.'],
    }
    files = {f'CpcwKernel/{m}.lean': sha256(HERE / 'CpcwKernel' / f'{m}.lean') for m in MODULES}
    files.update({name: sha256(HERE / name) for name in SCRIPTS})
    manifest = {'recorded_at_pt': stamp(), 'files': files,
                'raw_inputs': {f'review/{rel}': sha256(REVIEW / rel) for rel in RAW.values()},
                'parent_check_receipts': {f'review/{rel}': sha256(REVIEW / rel) for rel in PARENT_CHECK.values()},
                'control_receipts': {rel: sha256(control_receipt_path(rel)) for rel in CONTROL_RECEIPTS},
                'scanner_origin': {'path': f'review/{SCANNER_ORIGIN}', 'sha256': sha256(REVIEW / SCANNER_ORIGIN)},
                'import_graph': import_graph(scanner),
                'toolchain': toolchain_pins(scanner),
                'expected_axioms': inventory['expected_axioms'],
                'allowed_axioms': sorted(ALLOWED_AXIOMS)}
    return inventory, manifest


def write_manifest():
    inventory_path, manifest_path = HERE / INVENTORY, HERE / 'manifest.json'
    require(not inventory_path.exists() and not manifest_path.exists(),
            'Refusing to overwrite target-inventory.json or manifest.json')
    inventory, manifest = freeze_records()
    inventory_bytes = (json.dumps(inventory, indent=2, ensure_ascii=False) + '\n').encode('utf-8')
    manifest['files'][INVENTORY] = hashlib.sha256(inventory_bytes).hexdigest()
    with inventory_path.open('xb') as stream:
        stream.write(inventory_bytes)
    with manifest_path.open('x') as stream:
        json.dump(manifest, stream, indent=2, ensure_ascii=False)
        stream.write('\n')
    print(json.dumps({'inventory': str(inventory_path), 'inventory_sha256': sha256(inventory_path),
                      'manifest': str(manifest_path), 'manifest_sha256': sha256(manifest_path)}))


def control_receipt_path(rel):
    return ROOT / rel if rel.startswith('information') else ROOT / 'institute/runs/six-lane-2026-10-16' / rel


def run(command, name, out_dir, steps, env, timeout=1800, cwd=HERE, expect_success=True):
    started = time.monotonic()
    stdout = out_dir / 'logs' / f'{name}.stdout.txt'
    stderr = out_dir / 'logs' / f'{name}.stderr.txt'
    with stdout.open('x') as out, stderr.open('x') as err:
        proc = subprocess.Popen(command, cwd=cwd, stdin=subprocess.DEVNULL, stdout=out, stderr=err,
                                env=env, start_new_session=True)
        timed_out = False
        try:
            code = proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(proc.pid, signal.SIGTERM)
            code = proc.wait(timeout=30)
    item = {'step': name, 'command': [str(c) for c in command], 'exit_code': code, 'timeout': timed_out,
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


def max_rss_values(node):
    """Every recorded max_rss_bytes value (builds, fresh replays, controls)."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key == 'max_rss_bytes' and isinstance(value, int):
                yield value
            else:
                yield from max_rss_values(value)
    elif isinstance(node, list):
        for value in node:
            yield from max_rss_values(value)


def read_lean_data(path, tag):
    """Independent reader of a generated Data module (does not use gen_lean.py)."""
    text = Path(path).read_text()
    sha = re.search(rf'def data{tag}RawSha256 : String := "([0-9a-f]{{64}})"', text)
    head = re.search(rf'def data{tag}Header : Nat × Nat := \((\d+), (\d+)\)', text)
    body = re.search(rf'def data{tag} : List \(List Nat\) := \[\n(.*?)\n\]\n', text, re.S)
    require(sha and head and body, f'Data{tag}.lean: unexpected layout')
    decls = re.findall(r'^\s*(?:def|theorem|instance|abbrev|lemma|axiom|structure|class|opaque)\s+(\S+)', text, re.M)
    require(sorted(decls) == sorted([f'data{tag}RawSha256', f'data{tag}Header', f'data{tag}']),
            f'Data{tag}.lean: unexpected declarations {decls}')
    rows = [[int(x) for x in re.fullmatch(r'  \[([0-9, ]*)\],?', line).group(1).split(', ')]
            for line in body.group(1).split('\n')]
    return sha.group(1), (int(head.group(1)), int(head.group(2))), rows


def read_raw(path):
    """Independent reader of a raw certificate (does not use gen_lean.py)."""
    raw = Path(path).read_bytes()
    require(raw.endswith(b'\n') and b'\r' not in raw and b'\t' not in raw, f'{path}: line endings')
    lines = raw.decode('ascii').split('\n')[:-1]
    head = lines[0].split(' ')
    require(len(head) == 3 and head[0] == 'CPCW', f'{path}: bad header')
    return (int(head[1]), int(head[2])), [[int(x) for x in line.split(' ')] for line in lines[1:]]


def parse_axioms(log):
    axioms = {name: sorted(x.strip() for x in listed.split(',') if x.strip())
              for name, listed in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log)}
    for name in re.findall(r"'([^']+)' does not depend on any axioms", log):
        axioms[name] = []
    return axioms


def error_lines(text, source_name):
    return [(int(m.group(1)), m.group(2)) for m in
            re.finditer(re.escape(source_name) + r':(\d+):\d+: error[^:]*: (.*)', text)]


def decl_span(path, pattern):
    """Lines (first, last) of the declaration whose header line matches `pattern`, including an
    attached doc comment (Lean reports declaration-level errors at the doc comment) and ending
    before the next blank line."""
    lines = Path(path).read_text().split('\n')
    for index, line in enumerate(lines):
        if re.search(pattern, line):
            first = index
            if index > 0 and lines[index - 1].rstrip().endswith('-/'):
                first = index - 1
                while not lines[first].lstrip().startswith('/--'):
                    first -= 1
            last = index
            while last + 1 < len(lines) and lines[last + 1].strip():
                last += 1
            return first + 1, last + 1
    raise ValueError(f'{pattern!r} not found in {path}')


STATEMENT = '''/-- Spelled out without any `Cpcw` definition: `n` injective maps `Fin k → Fin v` whose ordered
differences (subtraction in `Fin v`) give every nonzero residue at most `c` times and `0` never,
and `n = (v - 1) / (k * (k - 1))`.  Nested exactly as `Cpcw.IsOptimalCPCW`. -/
def S (v k n c : Nat) : Prop :=
  ∃ B : Fin n → Fin k → Fin v,
    ((∀ i : Fin n, ∀ j l : Fin k, B i j = B i l → j = l) ∧
      (∀ d : Fin v, d.val ≠ 0 →
        (((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).val.map
          fun t => B t.1 t.2.1 - B t.1 t.2.2).count d ≤ c) ∧
      (∀ d : Fin v, d.val = 0 →
        (((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).val.map
          fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = 0)) ∧
    n = (v - 1) / (k * (k - 1))

/-- The same with every nonzero residue exactly once (a perfect code / cyclic difference family). -/
def SPerfect (v k n : Nat) : Prop :=
  ∃ B : Fin n → Fin k → Fin v,
    ((∀ i : Fin n, ∀ j l : Fin k, B i j = B i l → j = l) ∧
      (∀ d : Fin v, d.val ≠ 0 →
        (((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).val.map
          fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = 1) ∧
      (∀ d : Fin v, d.val = 0 →
        (((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).val.map
          fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = 0)) ∧
    n = (v - 1) / (k * (k - 1))
'''


def statement_controls():
    positive = '\n'.join(f'theorem t{TAGS[(v, k)]} : S {v} {k} {n} 1 := Cpcw.Kernel.exists_cpcw{TAGS[(v, k)]}'
                         for (v, k), n in CASES.items())
    return {
        'UnfoldedPositive': (positive, True),
        'WrongOrder': ('theorem t : S 123 6 4 1 := Cpcw.Kernel.exists_cpcw122k6', False),
        'WrongWeight': ('theorem t : S 122 5 4 1 := Cpcw.Kernel.exists_cpcw122k6', False),
        'WrongCount': ('theorem t : S 122 6 5 1 := Cpcw.Kernel.exists_cpcw122k6', False),
        'PerfectTarget': ('theorem t : SPerfect 122 6 4 := Cpcw.Kernel.exists_cpcw122k6', False),
        'CrossedRoot': ('theorem t : Cpcw.OptimalTarget 143 5 := Cpcw.Audit.target122k6', False),
    }


def run_statement_controls(out, env, steps):
    cdir = out / 'controls' / 'statement'
    cdir.mkdir(parents=True)
    results = {}
    for name, (body, should_pass) in statement_controls().items():
        src = cdir / f'Control{name}.lean'
        extra = ''
        if should_pass:
            extra = '\n' + '\n'.join(f'#print axioms Control{name}.t{TAGS[c]}' for c in CASES) + '\n'
        with src.open('x') as stream:
            stream.write(f'import CpcwKernel.Audit\n\nnamespace Control{name}\n\n{STATEMENT}\n{body}\n\n'
                         f'end Control{name}\n{extra}')
        stdout, stderr, item = run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEAN" -j 1 "$1"',
                                    'control', str(src)], f'control-statement-{name}', out, steps, env,
                                   timeout=900, expect_success=False)
        text = stdout + stderr
        errors = error_lines(text, src.name)
        span = decl_span(src, r'^theorem t') if not should_pass else None
        if should_pass:
            axioms = parse_axioms(text)
            intended = (item['exit_code'] == 0 and not errors and len(axioms) == len(CASES) and
                        all(set(a) <= ALLOWED_AXIOMS for a in axioms.values()))
        else:
            intended = (item['exit_code'] != 0 and bool(errors) and span[0] <= errors[0][0] <= span[1] and
                        'Type mismatch' in errors[0][1])
        results[name] = {'source_sha256': sha256(src), 'expected_to_compile': should_pass,
                         'exit_code': item['exit_code'], 'errors': errors[:3], 'intended': intended,
                         **time_metrics(stderr)}
        if should_pass:
            results[name]['axioms'] = parse_axioms(text)
    return results


def lean_compile(src_root, src_rel, olean, build_path, name, out, steps):
    env = dict(os.environ, CPCW_BUILD=build_path)
    cmd = ['sh', '-c', '. "$1/lean_env.sh"; cd "$2"; mkdir -p "$(dirname "$3")"; '
                       'exec /usr/bin/time -l "$LEAN" -j 1 -R . -o "$3" "$4"',
           'control', str(HERE), str(src_root), str(olean), src_rel]
    stdout, stderr, item = run(cmd, name, out, steps, env, timeout=900, expect_success=False)
    return stdout + stderr, item, time_metrics(stderr)


def run_data_controls(out, steps):
    """Each control is a self-contained mini-build: byte-identical copies of Target and Generic, the
    changed Data module and the Cert module, compiled in that order into the control's own build/."""
    results = {}
    for (v, k), n in CASES.items():
        tag = TAGS[(v, k)]
        raw = (REVIEW / RAW[(v, k)]).read_bytes()
        blocks = gen_lean.parse(raw, v, k)
        point = [list(b) for b in blocks]
        point[0][k - 1] = (point[0][k - 1] + 1) % v
        point_raw = gen_lean.render_raw(point, v, k)
        header_raw = f'CPCW {v + 1} {k}\n'.encode('ascii') + raw.split(b'\n', 1)[1]
        for kind in ['changed-point', 'changed-header', 'changed-header-regenerated']:
            cdir = out / 'controls' / f'{kind}-{tag}'
            (cdir / 'CpcwKernel').mkdir(parents=True)
            for module in ['Target', 'Generic']:
                (cdir / 'CpcwKernel' / f'{module}.lean').write_bytes(
                    (HERE / 'CpcwKernel' / f'{module}.lean').read_bytes())
            if kind == 'changed-point':
                (cdir / f'cpcw_{v}_{k}.txt').write_bytes(point_raw)
                data = gen_lean.render_data(point, v, k, hashlib.sha256(point_raw).hexdigest(), len(point_raw),
                                            f'CONTROL {kind} of review/{RAW[(v, k)]}')
                cert_tag, failing = tag, f'theorem data{tag}_check '
                (cdir / 'CpcwKernel' / f'Data{tag}.lean').write_text(data)
                (cdir / 'CpcwKernel' / f'Cert{tag}.lean').write_bytes((HERE / 'CpcwKernel' / f'Cert{tag}.lean').read_bytes())
            elif kind == 'changed-header':
                (cdir / f'cpcw_{v}_{k}.txt').write_bytes(header_raw)
                data = gen_lean.render_data(blocks, v, k, hashlib.sha256(header_raw).hexdigest(), len(header_raw),
                                            f'CONTROL {kind} of review/{RAW[(v, k)]}')
                old = f'def data{tag}Header : Nat × Nat := ({v}, {k})'
                require(data.count(old) == 1, 'header line not found once')
                data = data.replace(old, f'def data{tag}Header : Nat × Nat := ({v + 1}, {k})')
                data = data.replace(f'Header line `CPCW {v} {k}`', f'Header line `CPCW {v + 1} {k}`')
                cert_tag, failing = tag, f'theorem data{tag}_header '
                (cdir / 'CpcwKernel' / f'Data{tag}.lean').write_text(data)
                (cdir / 'CpcwKernel' / f'Cert{tag}.lean').write_bytes((HERE / 'CpcwKernel' / f'Cert{tag}.lean').read_bytes())
            else:
                raw_path = cdir / f'cpcw_{v + 1}_{k}.txt'
                raw_path.write_bytes(header_raw)
                cert_tag = f'{v + 1}k{k}'
                failing = f'theorem data{cert_tag}_check '
                run([sys.executable, '-B', 'gen_lean.py', str(raw_path), str(cdir / 'CpcwKernel'), '--v', str(v + 1),
                     '--k', str(k), '--expect-sha256', hashlib.sha256(header_raw).hexdigest(), '--label',
                     f'CONTROL {kind} of review/{RAW[(v, k)]}', '--leave', ''],
                    f'control-{kind}-{tag}-generate', out, steps, dict(os.environ))
            item_results = {}
            for module in ['Target', 'Generic', f'Data{cert_tag}', f'Cert{cert_tag}']:
                text, item, metrics = lean_compile(cdir, f'CpcwKernel/{module}.lean',
                                                   cdir / 'build' / 'CpcwKernel' / f'{module}.olean',
                                                   str(cdir / 'build'), f'control-{kind}-{tag}-{module}', out, steps)
                item_results[module] = {'exit_code': item['exit_code'],
                                        'errors': error_lines(text, f'{module}.lean')[:4], **metrics}
            cert_path = cdir / 'CpcwKernel' / f'Cert{cert_tag}.lean'
            span = decl_span(cert_path, '^' + re.escape(failing))
            data_ok = all(item_results[m]['exit_code'] == 0 and not item_results[m]['errors']
                          for m in ['Target', 'Generic', f'Data{cert_tag}'])
            cert = item_results[f'Cert{cert_tag}']
            message = 'proved that the proposition' if kind != 'changed-header' else 'Not a definitional equality'
            intended = (data_ok and cert['exit_code'] != 0 and bool(cert['errors']) and
                        span[0] <= cert['errors'][0][0] <= span[1] and message in cert['errors'][0][1])
            results[f'{kind}-{tag}'] = {
                'raw_sha256': sha256(next(cdir.glob('cpcw_*.txt'))),
                'cert_source_sha256': sha256(cert_path),
                'cert_is_frozen_source': sha256(cert_path) == sha256(HERE / 'CpcwKernel' / f'Cert{tag}.lean'),
                'expected_failure': f'{failing.strip()} (lines {span[0]}-{span[1]}): {message}',
                'modules': item_results, 'intended': intended}
    return results


def run_generator_controls(out, steps):
    raw = REVIEW / RAW[(122, 6)]
    good = sha256(raw)
    cases = {'wrong-sha': (['--v', '122', '--k', '6', '--expect-sha256', '0' * 64], 'SHA-256 mismatch'),
             'wrong-v': (['--v', '123', '--k', '6', '--expect-sha256', good], 'unexpected header'),
             'wrong-k': (['--v', '122', '--k', '5', '--expect-sha256', good], 'unexpected header')}
    results = {}
    for name, (args, message) in cases.items():
        target = out / 'controls' / 'generator' / name
        stdout, stderr, item = run([sys.executable, '-B', 'gen_lean.py', str(raw), str(target), *args,
                                    '--label', 'CONTROL', '--leave', '61'], f'control-generator-{name}', out, steps,
                                   dict(os.environ), expect_success=False)
        results[name] = {'exit_code': item['exit_code'], 'stderr_tail': stderr.strip().split('\n')[-1],
                         'wrote_nothing': not target.exists(),
                         'intended': item['exit_code'] != 0 and message in stderr and not target.exists()}
    return results


def run_overwrite_controls(out, tag, steps):
    results = {}
    for name, args in {'same-tag': [tag], 'write-manifest': ['--write-manifest']}.items():
        before = {p: sha256(p) for p in [HERE / 'manifest.json', HERE / INVENTORY]}
        stdout, stderr, item = run([sys.executable, '-B', 'replay.py', *args], f'control-overwrite-{name}', out, steps,
                                   dict(os.environ), timeout=120, expect_success=False)
        after = {p: sha256(p) for p in before}
        results[name] = {'exit_code': item['exit_code'], 'stderr_tail': stderr.strip().split('\n')[-1],
                         'intended': item['exit_code'] != 0 and before == after and
                         ('FileExistsError' in stderr or 'Refusing to overwrite' in stderr)}
    return results


def main(tag):
    require(re.fullmatch(r'[A-Za-z0-9_-]+', tag), 'TAG must be alphanumeric')
    out = HERE / f'replay-{tag}'
    out.mkdir(exist_ok=False)
    for sub in ['build', 'logs', 'regenerated', 'controls']:
        (out / sub).mkdir()
    env = dict(os.environ, CPCW_BUILD=str(out / 'build'), CPCW_LOGS=str(out / 'logs'), CPCW_THREADS='1')
    result = {'status': 'FAILED', 'tag': tag, 'started_at_pt': stamp(), 'steps': [],
              'driver_sha256': sha256(__file__),
              'trust_limits': [
                  'Same Lean 4.34.1 kernel implementation (lean and leanchecker of one toolchain); not Comparator, not an independent kernel.',
                  'Prebuilt Mathlib d13f23b oleans from the read-only cache are trusted as compiled artifacts for elaboration; leanchecker --fresh re-checks every imported declaration, Mathlib included, in a fresh kernel environment.',
                  'decide +kernel proofs are kernel reductions with GMP-accelerated Nat literals (part of the trusted kernel); no native code evaluation, no Lean.ofReduceBool.',
                  'The meaning of the roots rests on the reviewer reading CpcwKernel/Target.lean (Cpcw.diffs, Cpcw.IsCPCW, Cpcw.IsOptimalCPCW, Cpcw.Target, Cpcw.OptimalTarget); target-inventory.json marks what is kernel-checked and what is a written reading.',
                  'The raw-to-literal binding is checked by a Python generator and an independent Python reader, not inside Lean.']}
    result_path = out / 'result.json'
    try:
        # 1. pins
        manifest = json.loads((HERE / 'manifest.json').read_text())
        result['manifest_sha256'] = sha256(HERE / 'manifest.json')
        for rel, digest in manifest['files'].items():
            require(sha256(HERE / rel) == digest, f'Pinned file changed: {rel}')
        require(set(manifest['files']) == {f'CpcwKernel/{m}.lean' for m in MODULES} | set(SCRIPTS) | {INVENTORY},
                'Manifest does not list exactly the expected files')
        require(sorted(p.name for p in (HERE / 'CpcwKernel').iterdir()) == sorted(f'{m}.lean' for m in MODULES),
                'Unexpected file in CpcwKernel/')
        for rel, digest in {**manifest['raw_inputs'], **manifest['parent_check_receipts']}.items():
            require(sha256(REVIEW / rel.removeprefix('review/')) == digest, f'Pinned input changed: {rel}')
        for rel, digest in manifest['control_receipts'].items():
            require(sha256(control_receipt_path(rel)) == digest, f'Pinned control receipt changed: {rel}')
        require(sha256(REVIEW / SCANNER_ORIGIN) == manifest['scanner_origin']['sha256'] == sha256(HERE / 'lean_source_scan.py'),
                'Scanner differs from its pinned origin')
        inputs = {}
        for (v, k), n in CASES.items():
            raw = REVIEW / RAW[(v, k)]
            parent = json.loads((REVIEW / PARENT_CHECK[(v, k)]).read_text())
            require(parent['status'] == 'VALID_OPTIMAL_CPCW' and (parent['v'], parent['k'], parent['codewords']) == (v, k, n)
                    and parent['sha256'] == sha256(raw), f'Parent check receipt disagrees for {v}')
            inputs[TAGS[(v, k)]] = {'path': f'review/{RAW[(v, k)]}', 'sha256': sha256(raw), 'bytes': raw.stat().st_size,
                                    'parent_check_receipt': f'review/{PARENT_CHECK[(v, k)]}',
                                    'parent_check_sha256': sha256(REVIEW / PARENT_CHECK[(v, k)]),
                                    'parent_status': parent['status'], 'leave': parent['uncovered_differences']}
        result['inputs'] = inputs
        inventory = json.loads((HERE / INVENTORY).read_text())
        require({name: entry['source'] for name, entry in inventory['target_definitions'].items()} == target_definitions(),
                'Target definitions differ from the frozen inventory')
        require(inventory['root_statements_in_source'] == root_statements(), 'Root statements differ from the inventory')
        scanner = load_scanner()
        pins = toolchain_pins(scanner)
        require(pins == manifest['toolchain'], 'Toolchain or Mathlib cache pins changed')
        result['toolchain'] = pins
        # 2. source scan
        scan = {'scanner_sha256': sha256(HERE / 'lean_source_scan.py'), 'controls': scanner.controls(), 'files': {}}
        require(scan['controls']['positive_ok'] and scan['controls']['negative_ok'], 'Scanner controls failed')
        for module in MODULES:
            path = HERE / 'CpcwKernel' / f'{module}.lean'
            hits, _, imports = scanner.scan_text(path.read_text())
            require(not hits, f'Forbidden Lean construct in {module}: {hits}')
            scan['files'][module] = {'sha256': sha256(path), 'hits': hits, 'imports': imports}
        require(import_graph(scanner) == manifest['import_graph'], 'Import graph changed')
        require(scan['files']['Target']['imports'] == ['Mathlib.Data.Fintype.Prod'], 'Target imports changed')
        require(all(scan['files'][f'Data{t}']['imports'] == [] for t in TAGS.values()), 'Data modules must import nothing')
        result['source_scan'] = scan
        version, _, _ = run(['sh', '-c', '. ./lean_env.sh; exec "$LEAN" --version'], 'lean-version', out,
                            result['steps'], env)
        require(version.strip() == pins['lean_version'], 'lean --version differs')
        # 3. raw -> Lean binding
        binding = {}
        for (v, k), n in CASES.items():
            tag_vk = TAGS[(v, k)]
            raw = REVIEW / RAW[(v, k)]
            leave = ','.join(str(x) for x in inputs[tag_vk]['leave'])
            run([sys.executable, '-B', 'gen_lean.py', str(raw), str(out / 'regenerated'), '--v', str(v), '--k', str(k),
                 '--expect-sha256', inputs[tag_vk]['sha256'], '--label', f'review/{RAW[(v, k)]}', '--leave', leave],
                f'generate{tag_vk}', out, result['steps'], env)
            for kind in ['Data', 'Cert']:
                require((out / 'regenerated' / f'{kind}{tag_vk}.lean').read_bytes() ==
                        (HERE / 'CpcwKernel' / f'{kind}{tag_vk}.lean').read_bytes(),
                        f'{kind}{tag_vk}.lean is not regenerated byte-identically')
            lean_sha, lean_head, lean_rows = read_lean_data(HERE / 'CpcwKernel' / f'Data{tag_vk}.lean', tag_vk)
            raw_head, raw_rows = read_raw(raw)
            require(lean_sha == inputs[tag_vk]['sha256'], f'SHA string mismatch for {tag_vk}')
            require(lean_head == raw_head == (v, k), f'Header mismatch for {tag_vk}')
            require(lean_rows == raw_rows and len(raw_rows) == n and all(len(r) == k for r in raw_rows),
                    f'Codeword literal mismatch for {tag_vk}')
            cert = (HERE / 'CpcwKernel' / f'Cert{tag_vk}.lean').read_text()
            require(f'theorem exists_cpcw{tag_vk} : ∃ B : Fin {n} → Fin {k} → Fin {v}, Cpcw.IsOptimalCPCW B :=' in cert,
                    f'Root statement text for {tag_vk}')
            binding[tag_vk] = {'regenerated_byte_identical': ['Data', 'Cert'], 'independent_reader_match': True,
                               'codewords': len(raw_rows), 'data_lean_sha256': sha256(HERE / 'CpcwKernel' / f'Data{tag_vk}.lean'),
                               'cert_lean_sha256': sha256(HERE / 'CpcwKernel' / f'Cert{tag_vk}.lean')}
        controls_out, _, _ = run([sys.executable, '-B', 'gen_controls.py', str(out / 'regenerated')],
                                 'generate-controls', out, result['steps'], env)
        for name in ['ControlsFixtures', 'ControlsPinned']:
            require((out / 'regenerated' / f'{name}.lean').read_bytes() ==
                    (HERE / 'CpcwKernel' / f'{name}.lean').read_bytes(), f'{name}.lean is not regenerated byte-identically')
        result['data_binding'] = binding
        result['generator_controls'] = json.loads(controls_out)
        # 4.-5. build and axioms
        builds, axioms, printed = {}, {}, {}
        for module in MODULES:
            run(['sh', 'build_module.sh', f'CpcwKernel/{module}.lean'], f'build-{module}', out, result['steps'], env)
            log = (out / 'logs' / f'{module}.build.log').read_text()
            timing = (out / 'logs' / f'{module}.build.time').read_text()
            require(not re.search(r':\d+:\d+: error', log), f'Error message in build log of {module}')
            builds[module] = {**time_metrics(timing), 'warnings': len(re.findall(r':\d+:\d+: warning', log)),
                              'olean_sha256': sha256(out / 'build' / 'CpcwKernel' / f'{module}.olean')}
            found = parse_axioms(log)
            for name, listed in found.items():
                require(set(listed) <= ALLOWED_AXIOMS, f'Unexpected axiom for {name}: {listed}')
            if found:
                axioms[module] = found
            if module in ('Audit', 'Bridge'):
                printed[module] = log
        flat = {name: listed for found in axioms.values() for name, listed in found.items()}
        for name, listed in manifest['expected_axioms'].items():
            require(flat.get(name) == listed, f'Axioms of {name} differ from the frozen ones: {flat.get(name)}')
        for (v, k), n in CASES.items():
            root, audit = root_names(v, k)
            cert_log = (out / 'logs' / f'Cert{TAGS[(v, k)]}.build.log').read_text()
            require(f'{root} : {root_type(v, k)}' in cert_log, f'Missing root type for {v}')
            require(f'{audit} : Cpcw.OptimalTarget {v} {k}' in printed['Audit'], f'Missing audit type for {v}')
        require('Cpcw.Audit.allEight : ' in printed['Audit'], 'Missing conjunction type')
        result['builds'] = builds
        result['axioms'] = axioms
        result['printed_audit_output'] = printed
        # 6. fresh kernel replay
        fresh = {}
        for module in FRESH:
            stdout, stderr, item = run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v "$1"',
                                        'fresh', module], f'fresh-{module}', out, result['steps'], env, timeout=3600)
            require(f'replaying {module} with --fresh' in stdout, f'No replay marker for {module}')
            fresh[module] = {**time_metrics(stderr), 'exit_code': item['exit_code'], 'wall_seconds': item['wall_seconds'],
                             'stdout_tail': stdout.strip().split('\n')[-1]}
        result['fresh_replay'] = fresh
        # 7. controls
        controls = {'generator': run_generator_controls(out, result['steps']),
                    'statement': run_statement_controls(out, env, result['steps']),
                    'data': run_data_controls(out, result['steps']),
                    'overwrite': run_overwrite_controls(out, tag, result['steps'])}
        result['controls'] = controls
        result['roots'] = {TAGS[(v, k)]: {'root': root_names(v, k)[0], 'type': root_type(v, k),
                                          'audit': f'{root_names(v, k)[1]} : Cpcw.OptimalTarget {v} {k}',
                                          'axioms': flat[root_names(v, k)[0]],
                                          'audit_axioms': flat[root_names(v, k)[1]],
                                          'leave_kernel_checked': inputs[TAGS[(v, k)]]['leave'],
                                          'fresh_replay_module': 'CpcwKernel.Audit'} for v, k in CASES}
        failed = [f'{group}/{name}' for group, entries in controls.items() for name, entry in entries.items()
                  if not entry['intended']]
        require(not failed, f'Controls not as intended: {failed}')
        result['status'] = 'REBUILD_FRESH_KERNEL_REPLAY_AND_CONTROLS_PASS'
    except Exception as exc:
        result['error'] = f'{type(exc).__name__}: {exc}'
    finally:
        result['peak_max_rss_bytes'] = max(max_rss_values(result), default=None)
        result['finished_at_pt'] = stamp()
        with result_path.open('x') as stream:
            json.dump(result, stream, indent=2, ensure_ascii=False)
            stream.write('\n')
        print(json.dumps({'status': result['status'], 'result': str(result_path), 'error': result.get('error')},
                         indent=2), flush=True)
    return 0 if result['status'] == 'REBUILD_FRESH_KERNEL_REPLAY_AND_CONTROLS_PASS' else 1


if __name__ == '__main__':
    if sys.argv[1:] == ['--write-manifest']:
        write_manifest()
        raise SystemExit(0)
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1]))
