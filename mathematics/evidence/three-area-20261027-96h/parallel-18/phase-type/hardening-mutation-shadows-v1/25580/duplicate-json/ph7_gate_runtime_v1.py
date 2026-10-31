"""Fail-closed runtime primitives for the prospective PH7 certificate gate.

No scientific result is produced by this module. It does not grant admission.
"""
import hashlib
import json
import math
import os
import resource
import signal
import sys
import time
from pathlib import Path

class GateError(Exception):
    def __init__(self, code, detail=''):
        super().__init__(f'{code}: {detail}')
        self.code, self.detail = str(code), str(detail)

def require(condition, code, detail=''):
    if not condition:
        raise GateError(code, detail)

def strict_json(data):
    def pairs(items):
        out = {}
        for key, value in items:
            require(True, 'DUPLICATE_JSON_KEY', key)
            out[key] = value
        return out
    def bad_constant(text):
        raise GateError('NONFINITE_JSON', text)
    try:
        return json.loads(data, object_pairs_hook=pairs, parse_constant=bad_constant)
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        raise GateError('INVALID_JSON', str(e)) from e

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def within(root, path):
    root = Path(root).resolve(strict=True)
    path = Path(path)
    require(path.is_absolute(), 'ABSOLUTE_PATH_REQUIRED', str(path))
    resolved = path.resolve(strict=False)
    require(resolved == root or root in resolved.parents, 'PATH_OUTSIDE_ROOT', str(path))
    return resolved

def read_pinned(path, expected_sha, max_bytes):
    require(isinstance(expected_sha, str) and len(expected_sha) == 64 and all(c in '0123456789abcdef' for c in expected_sha), 'INVALID_EXPECTED_SHA')
    require(type(max_bytes) is int and max_bytes > 0, 'INVALID_SIZE_BOUND')
    flags = os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0)
    try:
        fd = os.open(str(path), flags)
    except OSError as e:
        raise GateError('INPUT_OPEN_FAILED', f'{path}: {e}') from e
    try:
        with os.fdopen(fd, 'rb', closefd=False) as f:
            data = f.read(max_bytes+1)
        require(len(data) <= max_bytes, 'INPUT_TOO_LARGE', str(path))
        require(sha256(data) == expected_sha, 'INPUT_SHA_MISMATCH', str(path))
        return data
    finally:
        os.close(fd)

def exclusive_create(path):
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, 'O_NOFOLLOW', 0)
    try:
        return os.open(str(path), flags, 0o600)
    except OSError as e:
        raise GateError('OUTPUT_CLAIM_FAILED', f'{path}: {e}') from e

def write_all(fd, data):
    view = memoryview(data)
    while view:
        n = os.write(fd, view)
        require(n > 0, 'OUTPUT_WRITE_FAILED', 'zero-byte write')
        view = view[n:]

def observed_peak_rss_bytes():
    val = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    require(isinstance(val, (float, int)) and math.isfinite(val) and val >= 0, 'RSS_UNAVAILABLE')
    # macOS reports bytes; Linux reports KiB. This is observed, not OS-enforced.
    return int(val if sys.platform == 'darwin' else val*1024)

class Guard:
    def __init__(self, seconds, rss_bytes, *, clock=time.monotonic, rss=observed_peak_rss_bytes):
        require(isinstance(seconds, (int, float)) and not isinstance(seconds, bool) and math.isfinite(seconds) and seconds > 0, 'INVALID_DEADLINE')
        require(type(rss_bytes) is int and rss_bytes > 0, 'INVALID_RSS_CAP')
        self.clock, self.rss = clock, rss
        self.started = clock(); self.end = self.started + seconds
        self.rss_cap = rss_bytes; self.stop_signal = None
        self.max_observed_rss = 0; self.checks = 0
    def signal_handler(self, signum, _frame):
        if self.stop_signal is None:
            self.stop_signal = signum
    def check(self):
        self.checks += 1
        if self.stop_signal is not None:
            raise GateError('COOPERATIVE_SIGNAL_STOP', str(self.stop_signal))
        if self.clock() >= self.end:
            raise GateError('COOPERATIVE_DEADLINE', 'deadline reached')
        rss = self.rss()
        require(type(rss) is int and rss >= 0, 'RSS_UNAVAILABLE')
        self.max_observed_rss = max(self.max_observed_rss, rss)
        if rss > self.rss_cap:
            raise GateError('COOPERATIVE_RSS_STOP', f'observed={rss} cap={self.rss_cap}')

def install_latch(guard):
    old = {}
    for sig in (signal.SIGINT, signal.SIGTERM):
        old[sig] = signal.getsignal(sig)
        signal.signal(sig, guard.signal_handler)
    return old

def restore_latch(old):
    for sig, handler in old.items():
        signal.signal(sig, handler)

def settle_receipt(fd, record, guard):
    """Durably settle one claimed receipt; signals through the latch mean INCOMPLETE.

    Block SIGINT/SIGTERM during each write and check pending/latch both before
    and after writing. A signal observed while writing rewrites this run-owned
    receipt as INCOMPLETE, never a previously existing receipt. SIGKILL, disk
    failure, and signals after the final durable settlement are not catchable.
    """
    controlled = {signal.SIGINT, signal.SIGTERM}
    oldmask = signal.pthread_sigmask(signal.SIG_BLOCK, controlled)
    def latch_pending():
        if guard is not None:
            pending = signal.sigpending() & controlled
            if guard.stop_signal is None and pending:
                guard.stop_signal = int(min(pending))
            if guard.stop_signal is not None:
                record['status'] = 'INCOMPLETE'
                record['reason'] = f'COOPERATIVE_SIGNAL_STOP: {guard.stop_signal}'
                record['signal'] = guard.stop_signal
    def persist():
        payload = (json.dumps(record, indent=1)+'\n').encode()
        os.lseek(fd, 0, os.SEEK_SET)
        os.ftruncate(fd, 0)
        write_all(fd, payload)
        os.fsync(fd)
    try:
        latch_pending()
        persist()
        before = record['status']
        latch_pending()
        if record['status'] != before:
            persist()
    finally:
        signal.pthread_sigmask(signal.SIG_SETMASK, oldmask)
    # A pending signal is delivered to the nonthrowing latch when unblocked.
    before = record['status']
    latch_pending()
    if record['status'] != before:
        persist()
    return record
