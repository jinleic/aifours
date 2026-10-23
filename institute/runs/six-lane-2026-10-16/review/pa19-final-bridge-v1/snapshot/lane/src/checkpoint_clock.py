#!/usr/bin/env python3
"""Metadata-only checkpoint clock for this lane. Appends a host-clock receipt every 15 min so a long blocked tool/token
wait cannot delay the <=30-min checkpoint cadence. No research work, helper/solver/checker start, signals, or token/config
changes. Reads only the latest watchdog sample and current free bytes; reports STATUS11 counts explicitly as the last
saved snapshot (not current coverage). Runs indefinitely until the owner stops it.
"""
import json
import os
import time
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent


def receipt():
    now = time.strftime('%Y-%m-%dT%H:%M:%S%z')
    st = os.statvfs(str(LANE))
    free = st.f_bavail * st.f_frsize
    try:
        count = (LANE / 'cycle2/tokens/COUNT').read_text().strip()
    except OSError:
        count = 'unreadable'
    try:
        rows = (LANE / 'cycle2/watchdog4-samples.log').read_text().splitlines()
        last = next((row for row in reversed(rows) if row and not row.startswith('#')), 'none')
        sample_age = round(time.time() - (LANE / 'cycle2/watchdog4-samples.log').stat().st_mtime, 1)
    except OSError:
        last, sample_age = 'unreadable', None
    try:
        status = LANE / 'STATUS11.json'
        saved = json.loads(status.read_text())
        sclock = time.strftime('%Y-%m-%dT%H:%M:%S%z', time.localtime(status.stat().st_mtime))
        counts = 'last saved STATUS11 snapshot %s: M1 open %s; M2 open %s; NOT a live recount' % (sclock, saved.get('M1_open'), saved.get('M2_open'))
    except (OSError, ValueError):
        counts = 'STATUS11 unavailable; no coverage claim'
    text = ('\n## %s (automatic host-clock checkpoint; metadata only)\n'
            '* COUNT=%s; filesystem free %d bytes (floor 12000000000).\n'
            '* Latest watchdog4 sample: `%s`; sample-file age %s seconds. Samples are observations, not a cap proof.\n'
            '* %s.\n') % (now, count, free, last, sample_age, counts)
    with (LANE / 'checkpoints.md').open('a') as f:
        f.write(text)
    print(now, 'metadata checkpoint appended', flush=True)


def main():
    while True:
        receipt()
        time.sleep(900)


if __name__ == '__main__':
    main()
