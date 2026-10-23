"""Parent K3 replay using pinned compressed proofs and in-memory regenerated CNFs.

  python3 -B replay_proofs.py pin LEDGER EXPECTED_LEDGER_SHA PROOF_ROOT
  python3 -B replay_proofs.py replay TAG START END [JOBS]

pin is invoked only after the worker freezes complete coverage of all 2165 nets (4330 A/B rows).
Each replay chunk has at most 200 nets, at most two workers, and drat-trim's native 60s limit per proof.
No regenerated CNFs or uncompressed proofs are written; only input pins and receipts are retained.
The independent B encoding's solver statuses are recorded as redundancy, not proof evidence.
"""
import concurrent.futures
import hashlib
import importlib.util
import io
import json
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PARENT_DT = HERE.parent / 'moqls7-parent-proofcheck-v1/drat-trim'
PARENT_DT_SHA = 'a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37'


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def now():
    return subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip()


def load(name, p):
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def write_json(p, obj):
    with open(p, 'x') as f:
        json.dump(obj, f, indent=1)
        f.write('\n')


def clone(src, dst):
    if dst.exists():
        raise ValueError('Refusing overwrite ' + str(dst))
    dst.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(['cp', '-c', str(src), str(dst)], capture_output=True, text=True)
    if r.returncode:
        raise ValueError('Pin failed ' + str(src) + ': ' + r.stderr)


def pin(ledger, expected_sha, proof_root):
    ledger, proof_root = Path(ledger).resolve(), Path(proof_root).resolve()
    raw = ledger.read_bytes()
    h = hashlib.sha256(raw).hexdigest()
    if h != expected_sha:
        raise ValueError('Worker ledger SHA mismatch')
    rows = [json.loads(line) for line in raw.decode().split('\n') if line.strip()]
    tags = [item['tag'] for item in json.loads((HERE / 'nets.json').read_text())]
    required = {(tag, enc) for tag in tags for enc in ('a', 'b')}
    keys = [(r['net'], r['encoder']) for r in rows]
    if len(rows) != 4330 or len(set(keys)) != 4330 or set(keys) != required:
        raise ValueError('Complete 2165x2 coverage is not frozen')
    if any(r.get('status') != 'UNSAT' or r.get('exit') != 20 for r in rows):
        raise ValueError('Ledger has non-UNSAT producer statuses (UNKNOWN until settled)')
    arows = [r for r in rows if r['encoder'] == 'a']
    if any(r.get('verified') is not True or r.get('check_exit') != 0 for r in arows):
        raise ValueError('Worker A-check ledger is incomplete')
    dest = HERE / 'proof-inputs'
    dest.mkdir(exist_ok=False)
    with open(dest / 'RESULTS.jsonl', 'xb') as f:
        f.write(raw)
    rec = {'started': now(), 'worker_ledger_sha256': h, 'coverage_rows': len(rows), 'proofs': [], 'metadata': {}}
    for r in arows:
        name = r['proof']
        if name != Path(name).name or not re.fullmatch(r'[A-Za-z0-9_.-]+\.drat\.zst', name):
            raise ValueError('Proof basename outside pin: ' + name)
        src, dst = proof_root / name, dest / name
        if src.is_symlink() or not src.is_file():
            raise ValueError('Proof is not a regular file: ' + name)
        clone(src, dst)
        got = sha(dst)
        if got != r['proof_sha256']:
            raise ValueError('Proof SHA mismatch: ' + name)
        rec['proofs'].append({'net': r['net'], 'file': name, 'bytes': dst.stat().st_size, 'sha256': got})
    catalog = json.loads((HERE / 'catalogue-result.json').read_text())
    # The CNF bytes are bound row by row in the replay by in-memory regeneration from the pinned encoders, so
    # every run must have used the same encoder bytes; driver-script versions are recorded, not required equal.
    expected_meta = {'enc_a2_sha256': catalog['files']['code/enc8_a2.py'],
                     'enc_b2_sha256': catalog['files']['code/enc8_b2.py']}
    for src in sorted(proof_root.glob('META.*.json')):
        clone(src, dest / src.name)
        m = json.loads((dest / src.name).read_text())
        rec['metadata'][src.name] = {'sha256': sha(dest / src.name), 'script_sha256': m.get('script_sha256'),
                                    'argv': m.get('argv'),
                                    'encoder_binding': all(m.get(k) == v for k, v in expected_meta.items())}
    if not rec['metadata'] or not all(v['encoder_binding'] for v in rec['metadata'].values()):
        raise ValueError('Worker metadata does not match the pinned encoders')
    rec['ended'] = now()
    rec['verdict'] = 'PASS'
    write_json(HERE / 'proof-pin-result.json', rec)
    print(json.dumps({'verdict': rec['verdict'], 'coverage_rows': len(rows), 'proofs': len(rec['proofs']),
                      'proof_bytes': sum(x['bytes'] for x in rec['proofs'])}))


def replay(tag, start, end, jobs):
    if not re.fullmatch('[A-Za-z0-9_-]+', tag) or not 1 <= jobs <= 2:
        raise ValueError('Invalid receipt tag or worker count')
    if not 0 <= start < end <= 2165 or end - start > 200:
        raise ValueError('A replay chunk must cover 1..200 of the 2165 nets')
    if sha(PARENT_DT) != PARENT_DT_SHA:
        raise ValueError('Parent checker binary mismatch')
    pinrec = json.loads((HERE / 'proof-pin-result.json').read_text())
    if pinrec['verdict'] != 'PASS':
        raise ValueError('Input pin did not pass')
    cat = json.loads((HERE / 'catalogue-result.json').read_text())
    if cat['verdict'] != 'PASS':
        raise ValueError('Catalogue did not pass')
    for rel in ('code/enc8_a2.py', 'code/enc8_b2.py'):
        if sha(HERE / 'inputs' / rel) != cat['files'][rel]:
            raise ValueError('Pinned code changed')
    nets_path = HERE / 'nets.json'
    if sha(nets_path) != cat['nets_sha256']:
        raise ValueError('Pinned net list changed')
    ledger = HERE / 'proof-inputs/RESULTS.jsonl'
    if sha(ledger) != pinrec['worker_ledger_sha256']:
        raise ValueError('Pinned ledger changed')
    rows = [json.loads(line) for line in ledger.read_text().split('\n') if line.strip()]
    amap = {r['net']: r for r in rows if r['encoder'] == 'a'}
    nets = json.loads(nets_path.read_text())
    A = load('k3_encoder_a', HERE / 'inputs/code/enc8_a2.py')
    pipe = load('k3_parent_pipe', HERE / 'proof_pipe.py')
    out = HERE / 'replays' / tag
    out.mkdir(parents=True, exist_ok=False)
    started = now()

    def one(idx):
        item = nets[idx]
        r = amap[item['tag']]
        f = A.build('fixed', (), (1, 2, 3), p3=True, p4=(1, 2, 3), squares=item['squares'])
        buf = io.BytesIO()
        buf.write(('p cnf %d %d\n' % (f.nv, len(f.clauses))).encode())
        for clause in f.clauses:
            buf.write((' '.join(map(str, clause)) + ' 0\n').encode())
        data = buf.getvalue()
        del f, buf
        got = hashlib.sha256(data).hexdigest()
        row = {'index': idx, 'net': item['tag'], 'rebuilt_cnf_sha256': got, 'worker_cnf_sha256': r['cnf_sha256'],
               'cnf_equal': got == r['cnf_sha256'], 'cnf_bytes': len(data)}
        if not row['cnf_equal'] or len(data) != r['cnf_bytes']:
            row['verdict'] = 'CNF-MISMATCH'
            return row
        proof = HERE / 'proof-inputs' / r['proof']
        if sha(proof) != r['proof_sha256']:
            row['verdict'] = 'PROOF-MISMATCH'
            return row
        row['check'] = pipe.check(data, proof, PARENT_DT, seconds=60)
        row['verdict'] = 'VERIFIED' if row['check']['verified'] else 'UNKNOWN'
        return row

    complete = []
    with open(out / 'per-case.jsonl', 'x') as f:
        with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as pool:
            for row in pool.map(one, range(start, end)):
                f.write(json.dumps(row) + '\n')
                f.flush()
                complete.append(row)
    count = sum(r['verdict'] == 'VERIFIED' for r in complete)
    rec = {'started': started, 'ended': now(), 'start': start, 'end': end, 'jobs': jobs,
           'driver_sha256': sha(Path(__file__)), 'pipe_sha256': sha(HERE / 'proof_pipe.py'),
           'drat_trim_sha256': PARENT_DT_SHA, 'verified': count,
           'bad': [r['net'] for r in complete if r['verdict'] != 'VERIFIED'],
           'verdict': 'PASS' if count == end - start else 'UNKNOWN'}
    write_json(out / 'result.json', rec)
    print(json.dumps(rec))


if __name__ == '__main__':
    if sys.argv[1] == 'pin':
        pin(*sys.argv[2:5])
    elif sys.argv[1] == 'replay':
        replay(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]) if len(sys.argv) > 5 else 2)
    else:
        raise ValueError('Unknown phase')
