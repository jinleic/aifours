#!/usr/bin/env python3
"""Read-only one-shot receipt notification using a Darwin directory event.
No scientific dispatch, polling loop, subprocess, signal or file mutation.
"""
import hashlib
import json
import os
from pathlib import Path
import select
import sys
import time
from datetime import datetime

ROOT = Path('/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review')
DEADLINE = datetime.fromisoformat('2026-10-18T17:57:00-07:00').timestamp()


def main():
    if len(sys.argv) != 2:
        raise SystemExit('usage: notify_receipt_v1.py ABSOLUTE_RECEIPT')
    path = Path(sys.argv[1]).resolve()
    if not path.is_relative_to(ROOT) or path.suffix != '.json':
        raise ValueError('receipt must be a JSON inside this run review directory')
    fd = os.open(path.parent, os.O_RDONLY)
    queue = select.kqueue()
    file_fd = None
    try:
        change = select.kevent(fd, filter=select.KQ_FILTER_VNODE,
                               flags=select.KQ_EV_ADD | select.KQ_EV_CLEAR,
                               fflags=select.KQ_NOTE_WRITE)
        queue.control([change], 0, 0)
        while True:
            if path.is_file():
                if file_fd is None:
                    file_fd = os.open(path, os.O_RDONLY)
                    file_change = select.kevent(file_fd, filter=select.KQ_FILTER_VNODE,
                                                flags=select.KQ_EV_ADD | select.KQ_EV_CLEAR,
                                                fflags=select.KQ_NOTE_WRITE | select.KQ_NOTE_EXTEND)
                    queue.control([file_change], 0, 0)
                raw = path.read_bytes()
                try:
                    obj = json.loads(raw)
                except json.JSONDecodeError:
                    obj = None
                if obj is not None:
                    print(json.dumps({'at': datetime.now().astimezone().isoformat(),
                                      'file': str(path), 'sha256': hashlib.sha256(raw).hexdigest(),
                                      'verdict': obj.get('verdict'), 'kind': obj.get('kind'),
                                      'id': obj.get('id'), 'scope': 'notification only; not parent acceptance'}), flush=True)
                    return
            remaining = DEADLINE - time.time()
            if remaining <= 0:
                raise SystemExit('native-end deadline reached without a complete receipt')
            queue.control(None, 1, remaining)
    finally:
        queue.close()
        if file_fd is not None:
            os.close(file_fd)
        os.close(fd)


if __name__ == '__main__':
    main()
