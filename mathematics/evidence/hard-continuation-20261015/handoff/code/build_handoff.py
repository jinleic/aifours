#!/usr/bin/env python3
"""Assemble handoff/: a compact, hash-pinned bundle for a later engine selection input.

Copies the load-bearing code, proof, evidence and the pinned attack-e2 inputs the
checkers read, consolidates per-chunk receipts into one deterministic gzip JSONL
per task (verified by reading back), and writes MANIFEST.json with every file's
size and SHA-256.  Refuses files of 4 MB or more and a total of 25 MB or more.
handoff/README.md and handoff/claims-candidates.json are authored separately and
must already exist.  Source files are only read, never modified or removed.
"""
import gzip
import hashlib
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
OUT = BASE / 'handoff'
ATTACK = HERE.parents[3] / 'institute/runs/hard-2026-10-15/problems/math-p0039/attack-e2'
CODE = ['certify.py', 'receipt_checks.py', 'check_coverage.py', 'controls.py', 'regressions.py', 'run_batch.py',
        'structure.py', 'fermat_power_two.py', 'fermat_gmp_check.py', 'build_handoff.py']
ARCHIVE = ['certify-f6eaa1a8.py', 'check_coverage-d4949917.py', 'certify-f3da25a6.py', 'check_coverage-8dee2782.py',
           'certify-d66fdcf0.py', 'check_coverage-fe4d6e49.py', 'MANIFEST.json']
EVIDENCE = ['coverage.json', 'coverage-v2.json', 'coverage-v3.json', 'coverage-v4.json', 'controls.json', 'controls-v2-tiny.json',
            'controls-v2-coverage.json', 'controls-v3-all.json', 'regressions-validation-fix.json',
            'regressions-validation-fix-v2.json', 'regressions-validation-fix-v3.json', 'receipts-sha256.json',
            'structure.json', 'replay-spot.json', 'fermat-t10.json',
            'fermat-t10-gmp.json', 'fermat-controls.json', 'fermat-t10-stages-run2.log',
            'benchmark-low-993.json', 'benchmark-main-256.json', 'batch-log.jsonl']
LOGS = ['e2-%s-%s.blocks.jsonl' % (t, e) for t in ('tiny', 'main', 'extension') for e in ('scan32', 'scan128_digest')]
FILE_LIMIT, TOTAL_LIMIT = 4 * 1024 * 1024, 25 * 1024 * 1024


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def copy(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    if sha(src) != sha(dst):
        sys.exit('copy differs: %s' % dst)


def consolidate(task):
    """Concatenate the original receipt files' exact bytes (one JSON line each), ordered by first block."""
    paths = sorted((BASE / 'receipts' / task).glob('*.json'), key=lambda p: json.loads(p.read_text())['first'])
    raw = b''.join(p.read_bytes() for p in paths)
    if not all(p.read_bytes().endswith(b'\n') and p.read_bytes().count(b'\n') == 1 for p in paths):
        sys.exit('a receipt file is not exactly one JSON line')
    dst = OUT / 'receipts' / (task + '.jsonl.gz')
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))
    if gzip.decompress(dst.read_bytes()) != raw:
        sys.exit('consolidated receipts do not read back: %s' % dst)
    return dict(task=task, receipts=len(paths), raw_sha256=hashlib.sha256(raw).hexdigest(), raw_bytes=len(raw),
                note='byte-identical concatenation of the original receipt files')


def main():
    for name in ('README.md', 'claims-candidates.json'):
        if not (OUT / name).is_file():
            sys.exit('author handoff/%s first' % name)
    for name in CODE:
        copy(HERE / name, OUT / 'code' / name)
    for name in ARCHIVE:
        copy(HERE / 'archive' / name, OUT / 'code' / 'archive' / name)
    copy(BASE / 'proofs' / 'FORCED-SUBGROUP.md', OUT / 'proofs' / 'FORCED-SUBGROUP.md')
    for name in EVIDENCE:
        if (BASE / 'evidence' / name).is_file():
            copy(BASE / 'evidence' / name, OUT / 'evidence' / name)
    for path in sorted((BASE / 'evidence' / 'fermat').glob('*.gz')):
        copy(path, OUT / 'evidence' / 'fermat' / path.name)
    for name in LOGS:
        copy(ATTACK / 'logs' / name, OUT / 'inputs' / 'logs' / name)
    for path in sorted((ATTACK / 'evidence/epoch2/prefix-groups').glob('0?-run.json')):
        copy(path, OUT / 'inputs' / 'evidence/epoch2/prefix-groups' / path.name)
    consolidated = [consolidate(t) for t in ('low', 'main', 'extension')]
    files = sorted(p for p in OUT.rglob('*') if p.is_file() and p != OUT / 'MANIFEST.json')
    entries = [dict(path=str(p.relative_to(OUT)), bytes=p.stat().st_size, sha256=sha(p)) for p in files]
    big = [e for e in entries if e['bytes'] >= FILE_LIMIT]
    total = sum(e['bytes'] for e in entries)
    if big or total >= TOTAL_LIMIT:
        sys.exit('size limits violated: %s total=%d' % (big, total))
    manifest = dict(files=entries, file_count=len(entries), total_bytes=total, consolidated_receipts=consolidated,
                    limits=dict(per_file_bytes_below=FILE_LIMIT, total_bytes_below=TOTAL_LIMIT))
    (OUT / 'MANIFEST.json').write_text(json.dumps(manifest, indent=1) + '\n')
    print(json.dumps(dict(file_count=len(entries), total_bytes=total, consolidated=consolidated)))


if __name__ == '__main__':
    main()
