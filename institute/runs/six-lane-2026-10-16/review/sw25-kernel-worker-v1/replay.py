#!/usr/bin/env python3
"""Single-run driver for the SW(25,16) Lean kernel proof (stdlib only; writes only inside a NEW output dir).

Usage: python3 -B replay.py SRC_DIR OUT_DIR
  SRC_DIR  Lean package root holding SW25/{Data,Main}.lean and SW25Flip/{Data,Facts,GramFails}.lean
  OUT_DIR  must not exist; it is created (exist_ok=False) and receives build/, logs/ and result.json

Steps, strictly sequential (never more than one Lean process of ours at a time):
  1. preconditions: free disk >= 12e9 bytes; other running lean/leanchecker processes are recorded.
  2. pins: raw witness SHA-256/size; toolchain binaries and shared libraries; scripts; reviewed scanner.
  3. generator binding: `gen_lean.py --check data|flip|twin` (byte-exact regeneration) and `--facts`.
  4. independent literal parse: a separate reader re-parses the raw file and the Lean `rows` literals; the
     witness literal must equal the raw matrix, the fixture must equal it except the two declared negated
     entries at the first strictly-upper-triangular nonzero position and its transpose.
  5. reviewed lexical source scan of every Lean source, plus statement-identity checks: the Gram theorem
     block of SW25/Main.lean occurs verbatim in the twin, and Facts negates exactly that proposition.
  6. builds (`lean -j 1 -M 3072`, tree RSS sampled every 0.25 s, SIGTERM above 3.75 GiB or 3600 s):
     SW25/Data, SW25/Main and SW25Flip/Data, SW25Flip/Facts must pass; SW25Flip/GramFails must FAIL with
     exactly one error, at the `decide +kernel` of W_gram, saying `decide` proved the proposition false.
  7. axiom audit of the `#print axioms` output: only propext, Classical.choice, Quot.sound allowed.
  8. `leanchecker --fresh -v SW25.Main` (the documented single-module interface; never `--help`).
  9. result.json, created exclusively.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_limited  # noqa: E402

TC = Path('/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1')
TOOL_FILES = ['bin/lean', 'bin/leanchecker', 'lib/lean/libleanshared.dylib', 'lib/lean/libleanshared_1.dylib',
              'lib/lean/libleanshared_2.dylib', 'lib/lean/libInit_shared.dylib', 'lib/lean/libLake_shared.dylib',
              'lib/lean/Init.olean', 'src/lean/LeanChecker.lean']
REVIEW = Path(os.environ.get('SW25_REVIEW', HERE.parent))
RAW = REVIEW / 'sw25-parent-inputs-v1/sw25-16-witness-v1.sw'
RAW_SHA256, RAW_BYTES = 'bfadf44596bc5138106432690bf507a8ff9c36cd3c40eb8eeb08195a9b2d4ab0', 1459
SCANNER_SHA256 = '8e9eb834f6bafa282c42ad793d71d82539d206c941e6d72fe5c4c2c8c8baf5bb'
RSS_CAP = 4026531840
LEAN_MEM_MB = 3072
WALL_CAP = 3600.0
DISK_FLOOR = 12_000_000_000
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
ROOT = 'SW25.exists_symmetric_weighing_matrix'
MODULES = [('SW25/Data.lean', 'pass'), ('SW25/Main.lean', 'pass'), ('SW25Flip/Data.lean', 'pass'),
           ('SW25Flip/Facts.lean', 'pass'), ('SW25Flip/GramFails.lean', 'fail')]
W_DEF = 'def W : Fin 25 → Fin 25 → Int := fun i j => (rows.getD i.val []).getD j.val 0'
GRAM_PROP = ('∀ i j : Fin 25,\n    ((List.finRange 25).map (fun k => W i k * W j k)).sum = '
             'if i = j then 16 else 0 := by')
GRAM_BLOCK = 'theorem W_gram : ' + GRAM_PROP + '\n  decide +kernel\n'
NOT_GRAM = 'theorem not_W_gram : ¬ ' + GRAM_PROP + '\n  decide +kernel\n'
ROOT_BLOCK = '''theorem exists_symmetric_weighing_matrix :
    ∃ W : Fin 25 → Fin 25 → Int,
      (∀ i j : Fin 25, W i j = -1 ∨ W i j = 0 ∨ W i j = 1) ∧
      (∀ i j : Fin 25, W i j = W j i) ∧
      (∀ i j : Fin 25,
        ((List.finRange 25).map (fun k => W i k * W j k)).sum = if i = j then 16 else 0) :=
  ⟨W, W_entries, W_symm, W_gram⟩
'''
MSG_RE = re.compile(r'^(?P<file>[^\s:]+\.lean):(?P<line>\d+):(?P<col>\d+): (?P<sev>error|warning)\b', re.M)
AXIOMS_RE = re.compile(r"^'(?P<name>[^']+)' (?:depends on axioms: \[(?P<ax>[^\]]*)\]|does not depend on any axioms)",
                       re.M)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def now():
    return run_limited.host_time()


def parse_raw_independently(data):
    text = data.decode('ascii')
    lines = text.split('\n')
    if lines[0] != 'SW 25 16' or len(lines) != 27 or lines[-1] != '':
        raise ValueError('raw layout')
    rows = [[int(t) for t in line.split(' ')] for line in lines[1:26]]
    if any(len(r) != 25 or any(x not in (-1, 0, 1) for x in r) for r in rows):
        raise ValueError('raw row layout')
    return rows


def parse_lean_rows(text, namespace):
    if text.count(f'\nnamespace {namespace}\n') != 1 or text.count(f'\nend {namespace}\n') != 1:
        raise ValueError('namespace lines')
    if text.count('\n' + W_DEF + '\n') != 1:
        raise ValueError('W definition line')
    m = re.search(r'^def rows : List \(List Int\) := \[\n(.*?)\n\]\n', text, re.S | re.M)
    if not m:
        raise ValueError('rows literal not found')
    rows = []
    for line in m.group(1).split('\n'):
        s = line.strip()
        if s.startswith('--'):
            continue
        mm = re.fullmatch(r'\[((?:-?\d+, )*-?\d+)\],?', s)
        if not mm:
            raise ValueError(f'unparsed literal line {s!r}')
        rows.append([int(x) for x in mm.group(1).split(', ')])
    return rows


def axioms_of(text):
    out = {}
    for m in AXIOMS_RE.finditer(text):
        out[m.group('name')] = [a.strip() for a in m.group('ax').split(',')] if m.group('ax') else []
    return out


def messages(text):
    found = []
    for m in MSG_RE.finditer(text):
        nxt = MSG_RE.search(text, m.end())
        found.append({'file': m.group('file'), 'line': int(m.group('line')), 'col': int(m.group('col')),
                      'severity': m.group('sev'), 'text': text[m.start():nxt.start() if nxt else len(text)]})
    return found


def main(argv):
    if len(argv) != 3:
        raise SystemExit(__doc__)
    src = Path(argv[1]).resolve()
    out = Path(argv[2]).resolve()
    out.mkdir(exist_ok=False)
    (out / 'build').mkdir(exist_ok=False)
    (out / 'logs').mkdir(exist_ok=False)
    res = {'started_at': now(), 'src': str(src), 'out': str(out), 'root_symbol': ROOT, 'failures': []}
    fail = res['failures'].append

    # 1. preconditions
    st = os.statvfs(str(out))
    res['free_disk_bytes_at_start'] = st.f_bavail * st.f_frsize
    if res['free_disk_bytes_at_start'] < DISK_FLOOR + 512 * 2**20:
        fail('free disk below floor')
    ps = subprocess.run(['ps', '-A', '-o', 'pid=,rss=,command='], capture_output=True, text=True).stdout
    res['other_lean_processes_at_start'] = [l.strip() for l in ps.splitlines()
                                            if re.search(r'/bin/(lean|leanchecker)\b', l)]

    # 2. pins
    raw = RAW.read_bytes()
    res['raw'] = {'path': str(RAW), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}
    if res['raw']['sha256'] != RAW_SHA256 or len(raw) != RAW_BYTES:
        fail('raw pin')
    res['tools'] = {rel: sha(TC / rel) for rel in TOOL_FILES}
    res['lean_version'] = subprocess.run([str(TC / 'bin/lean'), '--version'], capture_output=True,
                                         text=True).stdout.strip()
    res['scripts'] = {name: sha(HERE / name) for name in
                      ('gen_lean.py', 'replay.py', 'run_limited.py', 'lean_source_scan.py')}
    if res['scripts']['lean_source_scan.py'] != SCANNER_SHA256:
        fail('scanner is not the reviewed copy')
    res['sources'] = {rel: sha(src / rel) for rel, _ in MODULES}

    # 3. generator binding
    genv = dict(os.environ, SW25_REVIEW=str(REVIEW))
    res['generator_checks'] = {}
    for mode, rel in (('data', 'SW25/Data.lean'), ('flip', 'SW25Flip/Data.lean'), ('twin', 'SW25Flip/GramFails.lean')):
        p = subprocess.run([sys.executable, '-B', str(HERE / 'gen_lean.py'), '--check', mode, str(src / rel)],
                           capture_output=True, text=True, env=genv)
        res['generator_checks'][mode] = {'exit_code': p.returncode, 'stdout': p.stdout.strip(), 'stderr': p.stderr}
        if p.returncode != 0 or not p.stdout.startswith('MATCH'):
            fail(f'generator check {mode}')
    p = subprocess.run([sys.executable, '-B', str(HERE / 'gen_lean.py'), '--facts'], capture_output=True, text=True,
                       env=genv)
    res['generator_facts'] = json.loads(p.stdout) if p.returncode == 0 else {'error': p.stderr}

    # 4. independent literal parse
    lit = {}
    try:
        m = parse_raw_independently(raw)
        a, b = next((i, j) for i in range(25) for j in range(i + 1, 25) if m[i][j] != 0)
        expected_flip = [list(r) for r in m]
        expected_flip[a][b], expected_flip[b][a] = -m[a][b], -m[b][a]
        wit = parse_lean_rows((src / 'SW25/Data.lean').read_text(), 'SW25')
        fix = parse_lean_rows((src / 'SW25Flip/Data.lean').read_text(), 'SW25Flip')
        diffs = [(i, j) for i in range(25) for j in range(25) if fix[i][j] != m[i][j]]
        lit = {'witness_literal_equals_raw': wit == m, 'fixture_flip_position': [a, b],
               'fixture_equals_raw_with_declared_flip': fix == expected_flip, 'fixture_differences': diffs,
               'entries_compared_each': sum(len(r) for r in wit)}
    except (ValueError, StopIteration) as e:
        lit = {'error': repr(e)}
    res['independent_literal_parse'] = lit
    if not (lit.get('witness_literal_equals_raw') and lit.get('fixture_equals_raw_with_declared_flip')
            and lit.get('fixture_differences') == [(0, 2), (2, 0)] and lit.get('entries_compared_each') == 625):
        fail('independent literal parse')

    # 5. source scan and statement identity
    p = subprocess.run([sys.executable, '-B', str(HERE / 'lean_source_scan.py')] + [str(src / r) for r, _ in MODULES],
                       capture_output=True, text=True)
    res['source_scan'] = json.loads(p.stdout) if p.stdout.strip().startswith('{') else {'raw': p.stdout}
    res['source_scan_exit_code'] = p.returncode
    if p.returncode != 0 or not res['source_scan'].get('clean'):
        fail('source scan')
    main_text = (src / 'SW25/Main.lean').read_text()
    twin_text = (src / 'SW25Flip/GramFails.lean').read_text()
    facts_text = (src / 'SW25Flip/Facts.lean').read_text()
    ident = {'gram_block_in_main': main_text.count(GRAM_BLOCK), 'gram_block_in_twin': twin_text.count(GRAM_BLOCK),
             'negated_gram_in_facts': facts_text.count(NOT_GRAM), 'root_block_in_main': main_text.count(ROOT_BLOCK),
             'root_block_in_twin': twin_text.count(ROOT_BLOCK)}
    res['statement_identity'] = ident
    if any(v != 1 for v in ident.values()):
        fail('statement identity')
    gram_decide_line = twin_text[:twin_text.index(GRAM_BLOCK)].count('\n') + 3

    # 6. builds
    env = dict(os.environ, PATH=str(TC / 'bin') + ':' + os.environ.get('PATH', ''), LEAN_PATH=str(out / 'build'))
    res['builds'] = {}
    for rel, expect in MODULES:
        stem = rel[:-len('.lean')]
        olean, ilean = out / 'build' / (stem + '.olean'), out / 'build' / (stem + '.ilean')
        olean.parent.mkdir(parents=True, exist_ok=True)
        tag = stem.replace('/', '.')
        rec = run_limited.run([str(TC / 'bin/lean'), '-j', '1', '-M', str(LEAN_MEM_MB), '-R', str(src),
                               '-o', str(olean), '-i', str(ilean), rel], src, out / 'logs' / f'{tag}.stdout',
                              out / 'logs' / f'{tag}.stderr', RSS_CAP, WALL_CAP, env)
        log = Path(rec['stdout']).read_text() + Path(rec['stderr']).read_text()
        rec.update({'expect': expect, 'olean_written': olean.exists(), 'ilean_written': ilean.exists(),
                    'messages': messages(log), 'axioms': axioms_of(log)})
        if olean.exists():
            rec['olean_sha256'] = sha(olean)
        res['builds'][rel] = rec
        if expect == 'pass':
            if rec['exit_code'] != 0 or rec['terminated_by_guard'] or not olean.exists() or rec['messages']:
                fail(f'build {rel}')
            for name, axs in rec['axioms'].items():
                if not set(axs) <= ALLOWED_AXIOMS:
                    fail(f'axioms {name}: {axs}')
            if rel == 'SW25/Main.lean':
                res['root_print'] = log[:log.index("'" + ROOT + "'")] if ("'" + ROOT + "'") in log else log
                if ROOT not in rec['axioms']:
                    fail('root axioms not printed')
                if not re.match(r'theorem ' + re.escape(ROOT) + r' :\s+∃ W,', res['root_print']):
                    fail('root #print missing')
        else:
            msgs = rec['messages']
            errs = [x for x in msgs if x['severity'] == 'error']
            intended = (len(errs) == 1 and errs[0]['file'] == rel and errs[0]['line'] == gram_decide_line
                        and errs[0]['col'] == 2 and 'Tactic `decide` proved that the proposition' in errs[0]['text']
                        and 'is false' in errs[0]['text'] and 'if i = j then 16 else 0' in errs[0]['text'])
            rec['expected_error_line'] = gram_decide_line
            rec['intended_failure'] = bool(intended and rec['exit_code'] not in (0, None)
                                           and not rec['terminated_by_guard'] and not olean.exists())
            if not rec['intended_failure']:
                fail(f'negative {rel} did not fail for the intended reason')
        if res['failures'] and expect == 'pass':
            break

    # 7. axiom audit summary
    main_ax = res['builds'].get('SW25/Main.lean', {}).get('axioms', {})
    res['axiom_audit'] = {'allowed': sorted(ALLOWED_AXIOMS), 'root_axioms': main_ax.get(ROOT),
                          'all_printed': main_ax,
                          'root_ok': main_ax.get(ROOT) is not None and set(main_ax[ROOT]) <= ALLOWED_AXIOMS}
    if not res['axiom_audit']['root_ok']:
        fail('root axiom audit')

    # 8. fresh kernel replay
    if not res['failures']:
        rec = run_limited.run([str(TC / 'bin/leanchecker'), '--fresh', '-v', 'SW25.Main'], src,
                              out / 'logs' / 'leanchecker-fresh.stdout', out / 'logs' / 'leanchecker-fresh.stderr',
                              RSS_CAP, WALL_CAP, env)
        log = Path(rec['stdout']).read_text() + Path(rec['stderr']).read_text()
        rec['output'] = log[-2000:]
        rec['ok'] = (rec['exit_code'] == 0 and not rec['terminated_by_guard']
                     and 'replaying SW25.Main with --fresh' in log)
        res['fresh_replay'] = rec
        if not rec['ok']:
            fail('leanchecker --fresh')
    else:
        res['fresh_replay'] = 'skipped because of earlier failures'

    # 9. receipt
    procs = [r for r in res['builds'].values()] + ([res['fresh_replay']] if isinstance(res['fresh_replay'], dict) else [])
    res['resources'] = {
        'max_ru_maxrss_bytes': max((r.get('ru_maxrss_bytes') or 0) for r in procs),
        'max_sampled_tree_rss_bytes': max(r['sampled_peak_tree_rss_bytes'] for r in procs),
        'max_cpu_seconds_per_wall_second': max((r.get('cpu_seconds_per_wall_second') or 0) for r in procs),
        'lean_processes_run_sequentially': len(procs),
        'bytes_in_out_dir_before_receipt': sum(f.stat().st_size for f in out.rglob('*') if f.is_file()),
    }
    res['outputs'] = {str(f.relative_to(out)): sha(f) for f in sorted(out.rglob('*')) if f.is_file()}
    res['finished_at'] = now()
    res['status'] = 'SW25_KERNEL_PROOF_PASS' if not res['failures'] else 'FAIL'
    with open(out / 'result.json', 'x') as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
        f.write('\n')
    print(res['status'], res['failures'])
    return 0 if not res['failures'] else 1


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
