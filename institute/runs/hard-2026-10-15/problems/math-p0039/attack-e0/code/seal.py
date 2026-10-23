#!/usr/bin/env python3
"""Create/check file hashes for preserved evidence; never execute local binaries."""
import argparse
import hashlib
import json
from pathlib import Path
import sys


def paths():
    return sorted(p for p in Path('.').rglob('*') if p.is_file() and
                  '.tmp' not in p.parts and '__pycache__' not in p.parts and
                  p.as_posix() != 'evidence/manifest.json')


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('create', 'check'))
    args = parser.parse_args()
    target = Path('evidence/manifest.json')
    if args.mode == 'create':
        rows = [dict(path=p.as_posix(), bytes=p.stat().st_size, sha256=digest(p)) for p in paths()]
        data = dict(files=rows, total_bytes=sum(r['bytes'] for r in rows),
                    meaning='File integrity only. Hashes do not independently certify computations.')
        if data['total_bytes'] >= 1000000000:
            raise ValueError('evidence exceeds the 1 GB disk allocation')
        target.write_text(json.dumps(data, indent=2)+'\n')
    else:
        data = json.loads(target.read_text())
        for row in data['files']:
            p = Path(row['path'])
            if not p.is_file() or p.stat().st_size != row['bytes'] or digest(p) != row['sha256']:
                raise ValueError('file integrity mismatch: '+str(p))
    print('PASS: %d files, %d bytes. Integrity hashes only, not computational certification.' % (len(data['files']), data['total_bytes']))


if __name__ == '__main__':
    try:
        main()
    except ValueError as error:
        print('CHECK FAILED: '+str(error), file=sys.stderr)
        sys.exit(1)
