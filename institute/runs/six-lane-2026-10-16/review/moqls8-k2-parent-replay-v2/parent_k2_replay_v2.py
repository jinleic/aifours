"""Parent replay v2 of the MOQLS(8) K1/K2 certificate package (six-lane run, phys-1).

v2 change: drat-trim (upstream 2e3b2dc0) prefixes its output lines with a carriage return
("\\rs VERIFIED"); v1 compared lines after stripping only "\\n" and so recorded 0/78 although every
run exited 0. v2 strips surrounding whitespace before requiring the exact line "s VERIFIED".
Phase regen_ref replaces regen: it requires the v2-pinned CNFs to equal the CNFs that v1 rebuilt.

Phases (each writes its own receipt with mode "x"; nothing is deleted or overwritten):
  pin      APFS-clone (cp -c) every file named in the worker manifest plus code, catalogue sources and
           the written proof into inputs/, then hash every clone and compare with the manifest and the
           worker RECEIPT.
  catalog  Independently parse the Egan-Wanless species files, check every triple (Latin, mutually
           orthogonal), canonically label the 5-net point-line incidence graphs with nauty's labelg
           (not pynauty), and check that the worker's 39 nets are exactly the 39 source classes,
           pairwise non-isomorphic; check every <tag>.squares.json equals the worker's nets file.
  regen    Rebuild all 78 FIXED CNFs with the pinned encoders under /usr/bin/python3 and compare bytes.
  drat     Check all 78 zstd-compressed binary DRAT proofs against the pinned CNFs by streaming them into
           the parent's own drat-trim build; require exit 0 and the exact line "s VERIFIED".
Runs at most 4 children at once; children are never killed (native drat-trim time limit only).
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import time
from collections import deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
LANE = Path('/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16')
WORKER_ALL = LANE / 'evidence/k2_fixed/all_v1'
MANIFEST_NAME = 'MANIFEST_K2_ARTIFACTS_v2_1105.sha256'
MANIFEST_SHA = '3beb5f2636458458e13127cecfa01d00e821c01aae079691230fb4766b452149'
PROOF_SHA = '094dab60c7972c956f90c8cf0984c47f79376d0018192457c84adab6e224ff3c'
PARENT_DRAT = Path('/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/'
                   'moqls7-parent-proofcheck-v1/drat-trim')
PARENT_DRAT_SHA = 'a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37'
ZSTD = Path('/opt/homebrew/bin/zstd')
LABELG = Path('/opt/homebrew/Cellar/nauty/2.9.3/bin/labelg')
PY_REGEN = '/usr/bin/python3'
INP = HERE / 'inputs'
EXTRA = [
    'code/enc8_a2.py', 'code/enc8_b2.py', 'code/run_fixed_k2.py', 'code/proof_run.py',
    'code/relaxed_squares_control.py', 'code/ew_nets.py', 'code/ew_nets2.py', 'code/ew_nets_nauty.py',
    'code/k1_analytic_checks_v2.py', 'evidence/k1_analytic/checks_v2.json',
    'evidence/k2_fixed/ew_nets.json', 'evidence/k2_fixed/nauty.json',
    'evidence/' + MANIFEST_NAME, 'review/PROOF_K1_K2.r1.md',
    'sources/ew_data/maxMOLS8.3.txt', 'sources/ew_data/nmaxMOLS8.3.txt', 'sources/ew_data/LSformat.html',
    'sources/1406.3681v2.layout.txt', 'sources/2607.12933v2.raw.txt',
    'evidence/k2_fixed/relaxed_ctrl_v1/RECEIPT.json', 'evidence/k2_fixed/relaxed_ctrl_v1/nmax00.squares.json',
    'evidence/k2_fixed/relaxed_ctrl_v1/a_nmax00_noP4.cnf', 'evidence/k2_fixed/relaxed_ctrl_v1/a_nmax00_noP4.cnf.map.json',
    'evidence/k2_fixed/relaxed_ctrl_v1/a_nmax00_noP4_fixedclassical.cnf',
    'evidence/k2_fixed/relaxed_ctrl_v1/b_nmax00_noP4.cnf', 'evidence/k2_fixed/relaxed_ctrl_v1/b_nmax00_noP4.cnf.map.json',
    'evidence/k2_fixed/relaxed_ctrl_v1/b_nmax00_noP4_fixedclassical.cnf',
]


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def now() -> str:
    return subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip()


def write_x(path: Path, obj) -> None:
    with open(path, 'x') as f:
        json.dump(obj, f, indent=1)
        f.write('\n')


def manifest_entries():
    out = []
    for line in (INP / 'evidence' / MANIFEST_NAME).read_text().split('\n'):
        if not line.strip():
            continue
        h, p = line.split('  ', 1)
        assert p.startswith('./') and '/' not in p[2:], p
        out.append((h, p[2:]))
    return out


def phase_pin():
    INP.mkdir(exist_ok=False)
    rec = {'phase': 'pin', 'started': now(), 'cloned': 0, 'mismatch': [], 'extra': {}}
    for rel in EXTRA:
        dst = INP / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        r = subprocess.run(['cp', '-c', str(LANE / rel), str(dst)], capture_output=True, text=True)
        assert r.returncode == 0, (rel, r.stderr)
        rec['extra'][rel] = sha(dst)
    assert rec['extra']['evidence/' + MANIFEST_NAME] == MANIFEST_SHA
    assert rec['extra']['review/PROOF_K1_K2.r1.md'] == PROOF_SHA
    allv = INP / 'all_v1'
    allv.mkdir(exist_ok=False)
    ents = manifest_entries()
    for h, name in ents:
        src = WORKER_ALL / name
        assert src.is_file() and not src.is_symlink(), name
        r = subprocess.run(['cp', '-c', str(src), str(allv / name)], capture_output=True, text=True)
        assert r.returncode == 0, (name, r.stderr)
        got = sha(allv / name)
        rec['cloned'] += 1
        if got != h:
            rec['mismatch'].append({'file': name, 'manifest': h, 'clone': got})
    receipt = json.loads((allv / 'RECEIPT.json').read_text())
    rec['receipt_binding'] = {
        'script': receipt['script_sha256'] == rec['extra']['code/run_fixed_k2.py'],
        'enc_a': receipt['enc_a_sha256'] == rec['extra']['code/enc8_a2.py'],
        'enc_b': receipt['enc_b_sha256'] == rec['extra']['code/enc8_b2.py'],
        'nets': receipt['nets_sha256'] == rec['extra']['evidence/k2_fixed/ew_nets.json'],
    }
    rows = receipt['results']
    names = {n for _, n in ents}
    row_ok = []
    for r in rows:
        stem = '%s_%s.cnf' % (r['encoder'], r['net'])
        ok = (r.get('status') == 'UNSAT' and r.get('verified') is True and stem in names
              and stem + '.drat.zst' in names
              and sha(allv / stem) == r['cnf_sha256'] and sha(allv / (stem + '.drat.zst')) == r['proof_sha256'])
        row_ok.append(ok)
    rec['receipt_rows'] = len(rows)
    rec['receipt_rows_ok'] = sum(row_ok)
    rec['receipt_flags'] = {k: receipt.get(k) for k in ('all_unsat', 'all_verified', 'count')}
    rec['manifest_entries'] = len(ents)
    rec['ended'] = now()
    rec['verdict'] = 'PASS' if (not rec['mismatch'] and all(rec['receipt_binding'].values())
                                and rec['receipt_rows'] == 78 and rec['receipt_rows_ok'] == 78) else 'FAIL'
    write_x(HERE / 'pin-receipt.json', rec)
    print(json.dumps({k: rec[k] for k in ('cloned', 'receipt_rows_ok', 'verdict')}))


# ---------- catalogue ----------
def parse_ew(path: Path):
    lines = path.read_text().split('\n')
    head = lines[0].split()
    n, k, m = int(head[0]), int(head[1]), int(head[2])
    rows = [l.strip() for l in lines[1:] if l.strip()]
    assert len(rows) == k * m, (path, len(rows), k * m)
    squares = []
    for s in range(m):
        sq = [[ord(ch) - ord('a') for ch in rows[s * k + i]] for i in range(k)]
        assert all(len(r) == n for r in sq)
        squares.append(sq)
    assert m % 3 == 0
    return [squares[3 * t:3 * t + 3] for t in range(m // 3)]


def is_latin(L):
    n = len(L)
    return all(sorted(r) == list(range(n)) for r in L) and all(sorted(L[i][j] for i in range(n)) == list(range(n)) for j in range(n))


def orth(L, M):
    n = len(L)
    return len({(L[i][j], M[i][j]) for i in range(n) for j in range(n)}) == n * n


def graph6(n, edges):
    adj = set()
    for a, b in edges:
        adj.add((min(a, b), max(a, b)))
    bits = []
    for j in range(1, n):
        for i in range(j):
            bits.append(1 if (i, j) in adj else 0)
    while len(bits) % 6:
        bits.append(0)
    out = []
    if n <= 62:
        out.append(chr(n + 63))
    else:
        out.append('~')
        out += [chr(((n >> s) & 63) + 63) for s in (12, 6, 0)]
    for t in range(0, len(bits), 6):
        v = 0
        for b in bits[t:t + 6]:
            v = (v << 1) | b
        out.append(chr(v + 63))
    return ''.join(out)


def net_graph(triple):
    n = 8
    # points 0..63 (i*8+j); lines 64.. : class 0 rows, 1 columns, 2..4 symbols of the three squares
    edges = []
    for i in range(n):
        for j in range(n):
            p = i * n + j
            edges.append((p, 64 + 0 * n + i))
            edges.append((p, 64 + 1 * n + j))
            for s in range(3):
                edges.append((p, 64 + (2 + s) * n + triple[s][i][j]))
    return graph6(64 + 5 * n, edges)


def canon(g6s):
    data = ''.join(g + '\n' for g in g6s).encode()
    r = subprocess.run([str(LABELG), '-q'], input=data, capture_output=True)
    assert r.returncode == 0, r.stderr
    out = r.stdout.decode().split('\n')
    out = [x for x in out if x]
    assert len(out) == len(g6s)
    return out


def phase_catalog():
    rec = {'phase': 'catalog', 'started': now(), 'labelg_sha256': sha(LABELG)}
    src = parse_ew(INP / 'sources/ew_data/maxMOLS8.3.txt') + parse_ew(INP / 'sources/ew_data/nmaxMOLS8.3.txt')
    rec['source_triples'] = len(src)
    rec['source_valid'] = all(is_latin(L) for t in src for L in t) and all(
        orth(t[a], t[b]) for t in src for a in range(3) for b in range(a + 1, 3))
    nets = json.loads((INP / 'evidence/k2_fixed/ew_nets.json').read_text())['nets']
    rec['worker_nets'] = len(nets)
    tri = [item['squares'] for item in nets]
    rec['worker_valid'] = all(is_latin(L) for t in tri for L in t) and all(
        orth(t[a], t[b]) for t in tri for a in range(3) for b in range(a + 1, 3))
    rec['worker_row0_identity'] = all(L[0] == list(range(8)) for t in tri for L in t)
    cs = canon([net_graph(t) for t in src])
    cw = canon([net_graph(t) for t in tri])
    rec['source_distinct_classes'] = len(set(cs))
    rec['worker_distinct_classes'] = len(set(cw))
    rec['worker_equals_source_as_sets'] = sorted(cs) == sorted(cw)
    # each worker tag matches the source triple with the same index
    rec['tag_order_matches_source'] = [cw[i] == cs[i] for i in range(min(len(cs), len(cw)))].count(True)
    sq_ok = 0
    for item in nets:
        p = INP / 'all_v1' / (item['tag'] + '.squares.json')
        if p.read_text() == json.dumps(item['squares']):
            sq_ok += 1
    rec['squares_json_equal'] = sq_ok
    # mutation: swap two symbols in one cell of a square -> must break Latin property
    t0 = [[r[:] for r in L] for L in tri[0]]
    t0[0][1][1], t0[0][1][2] = t0[0][1][2], t0[0][1][1]
    rec['mutation_cell_swap_rejected'] = not (all(is_latin(L) for L in t0) and all(
        orth(t0[a], t0[b]) for a in range(3) for b in range(a + 1, 3)))
    # relabelled copy reproduces its canonical form (control for labelg use)
    import random
    rnd = random.Random(20261017)
    perm_r = list(range(8)); rnd.shuffle(perm_r)
    perm_c = list(range(8)); rnd.shuffle(perm_c)
    t1 = [[[L[perm_r[i]][perm_c[j]] for j in range(8)] for i in range(8)] for L in tri[5]]
    t1 = [t1[2], t1[0], t1[1]]
    rec['relabel_control'] = canon([net_graph(t1)])[0] == cw[5]
    rec['ended'] = now()
    rec['verdict'] = 'PASS' if (rec['source_triples'] == 39 and rec['source_valid'] and rec['worker_nets'] == 39
                                and rec['worker_valid'] and rec['worker_row0_identity']
                                and rec['source_distinct_classes'] == 39 and rec['worker_distinct_classes'] == 39
                                and rec['worker_equals_source_as_sets'] and rec['squares_json_equal'] == 39
                                and rec['mutation_cell_swap_rejected'] and rec['relabel_control']) else 'FAIL'
    write_x(HERE / 'catalog-receipt.json', rec)
    print(json.dumps({k: rec[k] for k in ('source_distinct_classes', 'worker_distinct_classes',
                                          'worker_equals_source_as_sets', 'verdict')}))


# ---------- pool helper ----------
def run_pool(jobs, width=4):
    """jobs: list of (key, argv, stdin_from_argv_or_None, out_path_or_None). Returns dict key->(rc, info)."""
    res = {}
    pending = deque(jobs)
    active = []
    while pending or active:
        while pending and len(active) < width:
            key, starter = pending.popleft()
            active.append((key, starter()))
        time.sleep(0.2)
        still = []
        for key, h in active:
            done = h['poll']()
            if done is None:
                still.append((key, h))
            else:
                res[key] = done
        active = still
    return res


def phase_regen():
    out = HERE / 'regen'
    out.mkdir(exist_ok=False)
    nets = json.loads((INP / 'evidence/k2_fixed/ew_nets.json').read_text())['nets']
    jobs = []
    for item in nets:
        tag = item['tag']
        sq = INP / 'all_v1' / (tag + '.squares.json')
        for enc in ('a', 'b'):
            cnf = out / ('%s_%s.cnf' % (enc, tag))
            if enc == 'a':
                argv = [PY_REGEN, '-B', str(INP / 'code/enc8_a2.py'), '--mode', 'fixed', '--slopes', '', '--squares',
                        str(sq), '--quantum', '12', '--p4', '12', '--cnf', str(cnf), '--map', str(cnf) + '.map.json']
            else:
                argv = [PY_REGEN, '-B', str(INP / 'code/enc8_b2.py'), '--mode', 'fixed', '--slopes', '', '--squares',
                        str(sq), '--quantum', '12', '--p4', '12', '--cnf', str(cnf)]

            def starter(argv=argv, cnf=cnf):
                errp = open(str(cnf) + '.stderr', 'x')
                p = subprocess.Popen(argv, stdout=subprocess.DEVNULL, stderr=errp)

                def poll():
                    rc = p.poll()
                    if rc is None:
                        return None
                    errp.close()
                    return {'rc': rc}
                return {'poll': poll}
            jobs.append(('%s_%s' % (enc, tag), starter))
    t0 = time.time()
    res = run_pool(jobs)
    rec = {'phase': 'regen', 'python': PY_REGEN, 'wall_s': round(time.time() - t0, 1), 'rows': []}
    for key in sorted(res):
        cnf = out / (key + '.cnf')
        pinned = INP / 'all_v1' / (key + '.cnf')
        row = {'case': key, 'rc': res[key]['rc'], 'regen_sha256': sha(cnf) if cnf.exists() else None,
               'pinned_sha256': sha(pinned)}
        row['equal'] = row['regen_sha256'] == row['pinned_sha256']
        rec['rows'].append(row)
    rec['equal_count'] = sum(r['equal'] and r['rc'] == 0 for r in rec['rows'])
    rec['ended'] = now()
    rec['verdict'] = 'PASS' if rec['equal_count'] == 78 and len(rec['rows']) == 78 else 'FAIL'
    write_x(HERE / 'regen-receipt.json', rec)
    print(json.dumps({k: rec[k] for k in ('equal_count', 'wall_s', 'verdict')}))


def phase_drat():
    assert sha(PARENT_DRAT) == PARENT_DRAT_SHA
    ents = manifest_entries()
    cases = sorted(n[:-4] for _, n in ents if n.endswith('.cnf'))
    assert len(cases) == 78
    jobs = []
    for case in cases:
        cnf = INP / 'all_v1' / (case + '.cnf')
        proof = INP / 'all_v1' / (case + '.cnf.drat.zst')

        def starter(cnf=cnf, proof=proof):
            z = subprocess.Popen([str(ZSTD), '-dc', str(proof)], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            d = subprocess.Popen([str(PARENT_DRAT), str(cnf), '-i', '-t', '50000'], stdin=z.stdout,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            z.stdout.close()
            h = hashlib.sha256()
            tail = deque(maxlen=40)
            s_lines = []
            nlines = [0]
            t0 = time.time()
            import threading

            def reader():
                for line in d.stdout:
                    h.update(line)
                    nlines[0] += 1
                    s = line.decode('utf-8', 'replace').strip()
                    tail.append(s)
                    if s.startswith('s '):
                        s_lines.append(s)
            th = threading.Thread(target=reader, daemon=True)
            th.start()

            def poll():
                rc = d.poll()
                if rc is None:
                    return None
                th.join()
                zrc = z.wait()
                return {'drat_rc': rc, 'zstd_rc': zrc, 's_lines': s_lines, 'out_lines': nlines[0],
                        'out_sha256': h.hexdigest(), 'tail': list(tail)[-8:], 'secs': round(time.time() - t0, 1)}
            return {'poll': poll}
        jobs.append((case, starter))
    t0 = time.time()
    res = run_pool(jobs)
    rows = []
    for case in cases:
        r = res[case]
        r['case'] = case
        r['verified'] = (r['drat_rc'] == 0 and r['zstd_rc'] == 0 and r['s_lines'] == ['s VERIFIED'])
        rows.append(r)
    rec = {'phase': 'drat', 'drat_trim': str(PARENT_DRAT), 'drat_trim_sha256': PARENT_DRAT_SHA,
           'zstd_sha256': sha(ZSTD.resolve()), 'wall_s': round(time.time() - t0, 1), 'rows': rows,
           'verified_count': sum(r['verified'] for r in rows), 'ended': now()}
    rec['verdict'] = 'PASS' if rec['verified_count'] == 78 else 'FAIL'
    write_x(HERE / 'drat-receipt.json', rec)
    print(json.dumps({k: rec[k] for k in ('verified_count', 'wall_s', 'verdict')}))


def phase_controls():
    """Negative controls for the streaming check: they must NOT produce 's VERIFIED'."""
    assert sha(PARENT_DRAT) == PARENT_DRAT_SHA
    out = {}
    cnf = INP / 'all_v1' / 'a_max00.cnf'
    proof = INP / 'all_v1' / 'a_max00.cnf.drat.zst'
    raw = subprocess.run([str(ZSTD), '-dc', str(proof)], capture_output=True).stdout
    def check(stdin_bytes, cnf_path):
        d = subprocess.run([str(PARENT_DRAT), str(cnf_path), '-i', '-t', '600'], input=stdin_bytes,
                           capture_output=True)
        lines = [l.strip() for l in d.stdout.decode('utf-8', 'replace').split('\n')]
        return {'rc': d.returncode, 's_lines': [l for l in lines if l.startswith('s ')]}
    out['full_proof_positive'] = check(raw, cnf)
    out['truncated_half'] = check(raw[:len(raw) // 2], cnf)
    out['empty_proof'] = check(b'', cnf)
    out['proof_of_other_case'] = check(raw, INP / 'all_v1' / 'b_max00.cnf')
    rec = {'phase': 'controls', 'decompressed_bytes': len(raw), 'controls': out, 'ended': now()}
    neg = [k for k in out if k != 'full_proof_positive']
    rec['verdict'] = 'PASS' if (out['full_proof_positive']['s_lines'] == ['s VERIFIED']
                                and all(out[k]['s_lines'] != ['s VERIFIED'] for k in neg)) else 'FAIL'
    write_x(HERE / 'controls-receipt.json', rec)
    print(json.dumps({'verdict': rec['verdict'], **{k: v['s_lines'] for k, v in out.items()}}))


def phase_regen_ref():
    v1 = HERE.parent / 'moqls8-k2-parent-replay-v1' / 'regen-receipt.json'
    R1 = json.loads(v1.read_text())
    rows = []
    for row in R1['rows']:
        pinned = INP / 'all_v1' / (row['case'] + '.cnf')
        got = sha(pinned)
        rows.append({'case': row['case'], 'v1_regen_sha256': row['regen_sha256'], 'v2_pinned_sha256': got,
                     'equal': row['rc'] == 0 and got == row['regen_sha256']})
    rec = {'phase': 'regen_ref', 'v1_regen_receipt_sha256': sha(v1), 'v1_verdict': R1['verdict'],
           'rows': rows, 'equal_count': sum(r['equal'] for r in rows), 'ended': now()}
    rec['verdict'] = 'PASS' if rec['equal_count'] == 78 and R1['verdict'] == 'PASS' else 'FAIL'
    write_x(HERE / 'regen-ref-receipt.json', rec)
    print(json.dumps({k: rec[k] for k in ('equal_count', 'verdict')}))


if __name__ == '__main__':
    {'pin': phase_pin, 'catalog': phase_catalog, 'regen': phase_regen, 'regen_ref': phase_regen_ref,
     'drat': phase_drat, 'controls': phase_controls}[sys.argv[1]]()
