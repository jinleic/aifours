#!/usr/bin/env python3
"""Finite, metadata-only checkpoint clock for the already-authorized run.

No research dispatch, model calls, configuration edits, child processes or signals.
Append-only metadata is not a scientific-progress claim. The clock exits at the
frozen deadline and does not replace the parent's substantive checkpoints.
"""
import argparse
import hashlib
import os
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path('/Users/jinleic/repos/aifours')
RUN = ROOT / 'institute/runs/six-lane-2026-10-16'
ZONE = ZoneInfo('America/Los_Angeles')
DEADLINE = datetime.fromisoformat('2026-10-18T18:31:43-07:00')
INTERVAL_SECONDS = 900


def append_metadata():
    now = datetime.now(ZONE)
    fs = os.statvfs(ROOT)
    free = fs.f_bavail * fs.f_frsize
    ledger = RUN / 'outcomes.md'
    digest = hashlib.sha256(ledger.read_bytes()).hexdigest()
    ledger_mtime = datetime.fromtimestamp(ledger.stat().st_mtime, ZONE).isoformat(timespec='seconds')
    message = (
        f'\n## Metadata-only clock — {now.isoformat(timespec="seconds")}\n\n'
        f'- Free space: {free:,} bytes; frozen floor: 12,000,000,000 bytes. '
        'This is an observation, not admission approval.\n'
        f'- Last saved ledger: `{digest}`; mtime {ledger_mtime}. '
        'No research result or process status was rechecked by this clock. '
        'No stage launched, signal sent or configuration changed.\n'
    )
    with (RUN / 'checkpoints.md').open('a', encoding='utf-8') as handle:
        handle.write(message)
    print(f'{now.isoformat(timespec="seconds")} METADATA_ONLY free_bytes={free} ledger_sha256={digest}', flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--once', action='store_true')
    args = parser.parse_args()
    append_metadata()
    if args.once:
        return
    while True:
        remaining = DEADLINE.timestamp() - time.time()
        if remaining <= 0:
            return
        time.sleep(min(INTERVAL_SECONDS, remaining))
        append_metadata()


if __name__ == '__main__':
    main()
