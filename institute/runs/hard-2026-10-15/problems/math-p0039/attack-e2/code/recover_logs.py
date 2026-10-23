#!/usr/bin/env python3
"""Recover snapshot-safe gzip parts using only stdlib, never producer code.

Checks each compressed and decompressed part and the concatenation against
the recovery manifest, and cross-checks original file hashes against the
previous delivery manifest. Hashes establish integrity, not correctness.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import tempfile


def require(condition, message):
    if not condition:
        raise ValueError(message)


def safe_path(path):
    candidate = Path(path)
    require(not candidate.is_absolute() and '..' not in candidate.parts,
            'path escapes current directory')
    require(candidate.resolve().is_relative_to(Path.cwd().resolve()),
            'resolved path escapes current directory')
    return candidate


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest', default='selection-inputs/first-attempt-logs/MANIFEST.json')
    ap.add_argument('--prior-manifest', default='evidence/previous-delivery/manifest.json')
    ap.add_argument('--check-only', action='store_true')
    ap.add_argument('--output')
    args = ap.parse_args()
    path = safe_path(args.manifest)
    manifest = json.loads(path.read_text())
    previous = json.loads(safe_path(args.prior_manifest).read_text())
    originals = {r['path']: r for r in previous['files']}
    results = []
    for source in manifest['sources']:
        target = safe_path(source['source_relative_path'])
        old = originals[str(target)]
        require(old['sha256'] == source['source_sha256'] and
                old['bytes'] == source['source_bytes'], 'original manifests disagree')
        digest, size = hashlib.sha256(), 0
        temporary = None
        stream = None
        try:
            if not args.check_only:
                target.parent.mkdir(parents=True, exist_ok=True)
                stream = tempfile.NamedTemporaryFile(prefix=target.name+'.recovering-',
                                                     dir=target.parent, delete=False)
                temporary = Path(stream.name)
            for part in source['parts']:
                compressed = safe_path(path.parent / part['file']).read_bytes()
                require(len(compressed) == part['compressed_bytes'], 'compressed size mismatch')
                require(hashlib.sha256(compressed).hexdigest() == part['compressed_sha256'],
                        'compressed hash mismatch: '+part['file'])
                raw = gzip.decompress(compressed)
                require(len(raw) == part['raw_bytes'], 'decompressed size mismatch')
                require(hashlib.sha256(raw).hexdigest() == part['raw_sha256'],
                        'decompressed hash mismatch')
                require(raw.endswith(b'\n'), 'part does not end at a complete line')
                digest.update(raw)
                size += len(raw)
                if stream:
                    stream.write(raw)
            require(size == source['source_bytes'] and digest.hexdigest() == source['source_sha256'],
                    'reconstructed file integrity mismatch')
            if stream:
                stream.close()
                stream = None
                temporary.replace(target)
            stored = hashlib.sha256()
            stored_size = 0
            with target.open('rb') as data:
                for chunk in iter(lambda: data.read(1 << 20), b''):
                    stored.update(chunk)
                    stored_size += len(chunk)
            require(stored.hexdigest() == digest.hexdigest() and stored_size == size,
                    'stored file differs from reconstructed content')
        finally:
            if stream:
                stream.close()
            if temporary is not None and temporary.exists():
                temporary.unlink()
        results.append(dict(path=str(target), bytes=size, sha256=digest.hexdigest(),
                            parts=len(source['parts'])))
    report = dict(files=results, limitation='Integrity only; no arithmetic or decisions verified.')
    output = json.dumps(report, indent=2)+'\n'
    if args.output:
        safe_path(args.output).write_text(output)
    print(output, end='')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError) as error:
        print('RECOVERY FAILED: '+str(error), file=sys.stderr)
        sys.exit(1)
