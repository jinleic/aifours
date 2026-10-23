"""Parent rebuild/replay of the four finite point-cyclic table producers, sequentially, from pinned copies.
No lane outputs are modified. Each seed must match pinned bytes, then the independently written parent
expander must match the pinned certificate, and the parent definition-first checker must accept it.
A time limit or nonzero exit never counts as a reproduced witness.
Usage: python3 -B point_cyclic_table_producer_replay.py NEW_OUTPUT_DIR
"""
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LANE = ROOT / 'information-science/evidence/six-lane-20261016/point-cyclic-table200'
CASES = [
    (112, 'pc112_t1', 'pc_tabu', ['112', '1', '7,1,1', '1', '1800'], 1860),
    (136, 'pc136_t3', 'pc_tabu', ['136', '17', '1,1,1,1,1,1,1', '1', '1800'], 1860),
    (160, 'pc160_t3', 'pc_tabu', ['160', '5', '10,2', '1', '900'], 960),
    (196, 'pc196_t2', 't2_twostage', ['49', '1', '3500'], 3560),
]
PC_TABU_SHA = 'b9f0bf98c9d6de50e3427b2bdfbb8b46f8bbbe2b66b53f18a7a0e421b960ae35'


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def save(path, data):
    with Path(path).open('x') as f:
        json.dump(data, f, indent=2)
        f.write('\n')


def main():
    out = Path(sys.argv[1]).resolve()
    out.mkdir(exist_ok=False)
    srcdir = out / 'sources'
    srcdir.mkdir()
    tmp = out / 'tmp'
    tmp.mkdir()
    env = dict(os.environ, TMPDIR=str(tmp), PYTHONDONTWRITEBYTECODE='1')
    receipt = {'started_at_pt': stamp(), 'status': 'FAILED', 'driver_sha256': sha(__file__), 'builds': [], 'cases': []}
    try:
        compiler = subprocess.run(['cc', '--version'], capture_output=True, text=True, check=True)
        receipt['compiler'] = compiler.stdout.splitlines()[0]
        for name in ['pc_tabu', 't2_twostage']:
            original = LANE / 'code' / (name + '.c')
            digest = sha(original)
            if name == 'pc_tabu' and digest != PC_TABU_SHA:
                raise ValueError('pc_tabu source differs from worker replay source')
            if name == 't2_twostage' and not (digest.startswith('1667f1ef') and digest.endswith('15c9')):
                raise ValueError('two-stage source differs from reported candidate producer')
            source = srcdir / original.name
            shutil.copyfile(original, source)
            if sha(source) != digest or sha(original) != digest:
                raise ValueError('source changed while pinning')
            obj, binary = out / (name + '.o'), out / name
            commands = [['cc', '-O2', '-pipe', '-c', str(source), '-o', str(obj)],
                        ['cc', str(obj), '-o', str(binary)]]
            for cmd in commands:
                p = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=120)
                if p.returncode:
                    raise ValueError('compile failed: ' + p.stderr)
            receipt['builds'].append({'name': name, 'source_sha256': digest, 'commands': commands,
                                      'object_sha256': sha(obj), 'binary_sha256': sha(binary)})
        for name in ['point_cyclic_seed_parent_expand.py']:
            shutil.copyfile(HERE / name, out / name)
        shutil.copyfile(HERE / 'point-cyclic160-parent-check-v1/checkers/parent.py', out / 'parent_checker.py')
        for v, stem, producer, args, timeout in CASES:
            case = out / ('v' + str(v))
            case.mkdir()
            pin = HERE / f'point-cyclic{v}-parent-inputs-v1'
            source_pin = json.loads((pin / 'pin-receipt.json').read_text())['files']
            seed_expected, cert_expected = source_pin[stem + '.seed']['sha256'], source_pin[stem + '.cert']['sha256']
            if sha(pin / (stem + '.seed')) != seed_expected or sha(pin / (stem + '.cert')) != cert_expected:
                raise ValueError('pinned input changed')
            prefix = case / 'producer'
            cmd = [str(out / producer), *args, str(prefix)]
            started = time.monotonic()
            with (case / 'producer.log').open('x') as log:
                p = subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT, cwd=case, env=env, timeout=timeout)
            row = {'v': v, 'producer_command': cmd, 'returncode': p.returncode,
                   'seconds': round(time.monotonic() - started, 2), 'seed_byte_identical': False}
            receipt['cases'].append(row)
            if p.returncode != 0:
                raise ValueError(f'producer v{v} returned {p.returncode}, not a reproduced witness')
            seed = case / 'producer.seed'
            row['seed_sha256'] = sha(seed)
            row['seed_byte_identical'] = seed.read_bytes() == (pin / (stem + '.seed')).read_bytes()
            if not row['seed_byte_identical']:
                raise ValueError('producer seed differs from pinned seed')
            expcmd = [sys.executable, '-B', str(out / 'point_cyclic_seed_parent_expand.py'), str(seed), seed_expected,
                      str(pin / (stem + '.cert')), cert_expected, str(case / 'parent-expansion')]
            p = subprocess.run(expcmd, capture_output=True, text=True, env=env, timeout=300)
            with (case / 'expand.log').open('x') as f:
                f.write(p.stdout + p.stderr)
            row['expansion_command'] = expcmd
            if p.returncode:
                raise ValueError('parent expansion failed')
            expanded = case / 'parent-expansion/own-expanded.cert'
            row['certificate_sha256'] = sha(expanded)
            chkcmd = [sys.executable, '-B', str(out / 'parent_checker.py'), str(expanded), str(v), cert_expected,
                      str(case / 'parent-check.json')]
            p = subprocess.run(chkcmd, capture_output=True, text=True, env=env, timeout=300)
            row['checker_command'], row['checker_returncode'] = chkcmd, p.returncode
            if p.returncode:
                raise ValueError('regenerated certificate rejected: ' + p.stdout + p.stderr)
            row['status'] = 'PARENT_REBUILT_PRODUCER_SEED_AND_CERTIFICATE_BYTE_REPLAY_PASS'
            save(case / 'receipt.json', row)
            print(json.dumps({'v': v, 'status': row['status'], 'seconds': row['seconds']}), flush=True)
        receipt['status'] = 'ALL_FOUR_TABLE_PRODUCER_REPLAYS_PASS'
    except Exception as exc:
        receipt['error'] = type(exc).__name__ + ': ' + str(exc)
    receipt['finished_at_pt'] = stamp()
    save(out / 'parent-result.json', receipt)
    print(receipt['status'], receipt.get('error', ''), flush=True)
    return 0 if receipt['status'].endswith('PASS') else 1


if __name__ == '__main__':
    raise SystemExit(main())
