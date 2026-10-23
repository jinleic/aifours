#!/usr/bin/env python3
"""Exercise a size-capped snapshot with the three oversized logs absent.

Only explicit task files are copied to a temporary subdirectory of the current
directory. It is removed on exit. The subprocess uses Python only and invokes
the actual main-metadata replay entry point, including automatic log recovery.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', default='evidence/recovery-snapshot-test.json')
    args = p.parse_args()
    begin = time.monotonic()
    originals = json.loads(Path('selection-inputs/first-attempt-logs/MANIFEST.json').read_text())['sources']
    missing = {r['source_relative_path'] for r in originals}
    files = [Path(f) for f in ('REPORT.md', 'claims.json', 'claims.schema.json', 'contract.json')]
    for directory in ('code', 'evidence', 'logs', 'selection-inputs'):
        files.extend(f for f in Path(directory).rglob('*')
                     if f.is_file() and not f.is_symlink() and
                     '__pycache__' not in f.parts and f.stat().st_size < 5000000 and
                     not any(part.endswith('.tmp') for part in f.parts))
    with tempfile.TemporaryDirectory(prefix='snapshot-replay-', suffix='.tmp', dir='evidence') as temporary:
        root = Path(temporary)
        for path in files:
            if str(path) in missing:
                continue
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
        assert all(not (root / f).exists() for f in missing)
        run = subprocess.run([sys.executable, 'code/recheck.py', 'main-metadata'],
                             cwd=root, capture_output=True, text=True, timeout=870)
        if run.returncode:
            sys.stderr.write(run.stderr)
            raise SystemExit(run.returncode)
        for row in originals:
            path = root / row['source_relative_path']
            assert path.stat().st_size == row['source_bytes']
            assert digest(path) == row['source_sha256']
        result = dict(returncode=run.returncode, raw_logs_initially_absent=sorted(missing),
                      recovered_files=len(missing), seconds=time.monotonic()-begin,
                      stdout=run.stdout,
                      scope='Snapshot packaging/reconstruction and metadata only; not exhaustive main arithmetic.')
    Path(args.output).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
