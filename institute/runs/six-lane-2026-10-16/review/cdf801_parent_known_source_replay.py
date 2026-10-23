"""Rebuild/replay the KNOWN frozen CDF801 source, not the unavailable original discovery snapshot."""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / 'information-science/evidence/six-lane-20261016/cdf-k5/evidence/v801/cdf_mq4.frozen-2026-10-16.c'
SOURCE_SHA = '68028470d65cbfb450c84a6ba354dd7bc68c3a9d9de919cc91f92adb34e1da16'
WITNESS_SHA = '0a75e7d93920415f04a51967bd5a4033765f040f3b19af9f603d16b6d616186c'
OUT = HERE / 'cdf801-known-source-parent-replay-v1'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args, label, timeout):
    started = time.monotonic()
    proc = subprocess.run(args, cwd=OUT, capture_output=True, text=True, timeout=timeout)
    (OUT / (label + '.stdout.txt')).write_text(proc.stdout)
    (OUT / (label + '.stderr.txt')).write_text(proc.stderr)
    data = {'args': args, 'returncode': proc.returncode, 'duration_seconds': time.monotonic() - started}
    with (OUT / (label + '.execution.json')).open('x') as stream:
        json.dump(data, stream, indent=2)
        stream.write('\n')
    if proc.returncode:
        raise RuntimeError(f'{label} exited {proc.returncode}')
    return data


def main():
    OUT.mkdir(exist_ok=False)
    result = {'status': 'INCOMPLETE', 'started_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'driver_sha256': sha(Path(__file__)), 'source': str(SOURCE),
              'caveat': 'Original discovery source not preserved. This checks reproducibility from the later frozen known source only; raw witness validity is independently checked.'}
    try:
        payload = SOURCE.read_bytes()
        result['source_sha256'] = hashlib.sha256(payload).hexdigest()
        if result['source_sha256'] != SOURCE_SHA:
            raise ValueError('frozen source hash mismatch')
        src = OUT / 'cdf_mq4.c'
        with src.open('xb') as stream:
            stream.write(payload)
        run(['cc', '--version'], 'compiler-version', 30)
        binary = OUT / 'cdf_mq4'
        result['build'] = run(['cc', '-O3', '-march=native', '-o', str(binary), str(src)], 'build', 120)
        result['binary_sha256'] = sha(binary)
        prefix = OUT / 'regenerated-801'
        result['replay'] = run([str(binary), '801', '9', '21', '600', str(prefix),
                                '30', '0', '30000000', '5000000', '1'], 'replay', 720)
        generated = prefix.with_suffix('.sol')
        pinned = HERE / 'cdf801-parent-inputs-v1/cdf_801.txt'
        result['generated_sha256'] = sha(generated)
        result['pinned_sha256'] = sha(pinned)
        result['byte_identical'] = generated.read_bytes() == pinned.read_bytes()
        if not result['byte_identical'] or result['pinned_sha256'] != WITNESS_SHA:
            raise ValueError('generated or pinned witness does not match the frozen certificate')
        result['check'] = run([sys.executable, '-B', str(HERE / 'check_cdf_independent.py'), str(generated),
                               '801', WITNESS_SHA, str(OUT / 'regenerated-parent-check.json')], 'check', 180)
        result['status'] = 'KNOWN_SOURCE_REBUILD_SEED_REPLAY_BYTE_IDENTICAL_AND_VALID'
    except Exception as exc:
        result['status'] = 'FAILED'
        result['error'] = f'{type(exc).__name__}: {exc}'
    finally:
        result['finished_at_pt'] = datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
        with (OUT / 'parent-result.json').open('x') as stream:
            json.dump(result, stream, indent=2)
            stream.write('\n')
        print(json.dumps(result, indent=2))
    return int(result['status'] != 'KNOWN_SOURCE_REBUILD_SEED_REPLAY_BYTE_IDENTICAL_AND_VALID')


if __name__ == '__main__':
    raise SystemExit(main())
