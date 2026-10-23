#!/usr/bin/env python3
"""Resume the interrupted metadata stream without changing any prior byte.

Verify an exact frozen prefix under an exclusive lock, append a restart record,
then append fresh statvfs observations until the original 18:10 end. No children,
signals, deletions, scientific dispatch or retroactive observations. A five-minute
observation gap remains visible; consumers still enforce their unchanged gates.
"""
import fcntl
import hashlib
import json
import os
from pathlib import Path
import sys
import time
from datetime import datetime

ROOT = Path('/Users/jinleic/repos/aifours')
REVIEW = ROOT / 'institute/runs/six-lane-2026-10-16/review'
TARGET = REVIEW / 'disk-monitor-v1-20261018T0722-to-1810.jsonl'
EXPECTED_SHA = '6f7c5732e1ace2d8c1e63179ea61c10c4723f3a6b00c9a62880de1511cadac6b'
EXPECTED_BYTES = 48247
END = datetime.fromisoformat('2026-10-18T18:10:00-07:00').timestamp()


def append(fd, record):
    data = (json.dumps(record, sort_keys=True) + '\n').encode()
    view = memoryview(data)
    while view:
        n = os.write(fd, view)
        if n <= 0:
            raise OSError('monitor append made no progress')
        view = view[n:]


def main():
    fd = os.open(TARGET, os.O_RDWR | os.O_APPEND | os.O_NOFOLLOW)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        chunks = []
        while True:
            part = os.read(fd, 65536)
            if not part:
                break
            chunks.append(part)
        prefix = b''.join(chunks)
        if len(prefix) != EXPECTED_BYTES or hashlib.sha256(prefix).hexdigest() != EXPECTED_SHA:
            raise ValueError('monitor prefix changed; refusing append')
        if not prefix.endswith(b'\n'):
            raise ValueError('monitor has an incomplete final record; refusing append')
        records = [json.loads(line) for line in prefix.splitlines()]
        last = datetime.fromisoformat([r['t'] for r in records if 't' in r and 'free' in r][-1])
        append(fd, {'event': 'restart', 'at': datetime.now().astimezone().isoformat(),
                    'pid': os.getpid(), 'interval': 10, 'end_epoch': END,
                    'prefix_bytes': EXPECTED_BYTES, 'prefix_sha256': EXPECTED_SHA,
                    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    'note': '09:25:51 SIGTERM interruption; no missing samples reconstructed'})
        print('MONITOR_RESUMED ' + str(TARGET), flush=True)
        while time.time() < END:
            current = datetime.now().astimezone().replace(microsecond=0)
            if current <= last:
                raise ValueError('clock did not advance; refusing nonmonotone sample')
            st = os.statvfs(ROOT)
            append(fd, {'t': current.isoformat(), 'free': st.f_bavail * st.f_frsize})
            last = current
            time.sleep(min(10, max(0, END - time.time())))
        append(fd, {'event': 'end', 'at': datetime.now().astimezone().isoformat()})
    finally:
        os.close(fd)


if __name__ == '__main__':
    main()
