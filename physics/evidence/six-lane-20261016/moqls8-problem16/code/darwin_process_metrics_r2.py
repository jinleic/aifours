"""In-process Darwin metrics/selection: NO subprocess, helper, retry or signal.
RSS is the real pinned0ee libproc probe, unchanged and fail-closed on unknown or
zero-resident state. UID PID enumeration and KERN_PROCARGS2 select declared
Python/CaDiCaL/drat-trim worker roots; libproc expands descendants. Argv/env bytes
are never logged. Disk accounting is an allocated-block walk, not du.
ABI constants: MacOSX26.0.sdk sys/proc_info.h51–56; sys/sysctl.h184,216,261,796.
"""
from __future__ import annotations

import ctypes
import errno
import hashlib
import importlib.util
import os
from pathlib import Path
import stat
import struct
import sys

SUPERVISOR = Path('/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code/supervise_r3.py')
SUP_SHA = '0ee8f39496fa3d6051639e99f10d907b8adadcb5d3446f2bb6242c924a83ec4d'
PROC_UID_ONLY = 4
CTL_KERN, KERN_ARGMAX, KERN_PROCARGS2 = 1, 8, 49
_supervisor = None
_libc = None


def supervisor():
    global _supervisor
    if _supervisor is None:
        if hashlib.sha256(SUPERVISOR.read_bytes()).hexdigest() != SUP_SHA:
            raise RuntimeError('pinned libproc source changed')
        spec = importlib.util.spec_from_file_location('n8_readonly_libproc_source_r2', SUPERVISOR)
        m = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = m
        spec.loader.exec_module(m)
        _supervisor = m
    return _supervisor


def libc():
    global _libc
    if _libc is None:
        _libc = ctypes.CDLL(None, use_errno=True)
        _libc.sysctl.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_uint, ctypes.c_void_p,
                                ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p, ctypes.c_size_t)
        _libc.sysctl.restype = ctypes.c_int
    return _libc


def parse_procargs2(raw):
    """Read ONLY argc argv entries; environment tail is neither returned nor logged."""
    if len(raw) < 6:
        raise RuntimeError('short KERN_PROCARGS2 reply')
    argc = struct.unpack_from('=i', raw, 0)[0]
    if not 1 <= argc <= len(raw) - 4:
        raise RuntimeError('invalid KERN_PROCARGS2 argc')
    end = raw.find(b'\0', 4)
    if end < 0:
        raise RuntimeError('unterminated executable path')
    pos = end + 1
    while pos < len(raw) and raw[pos] == 0:
        pos += 1
    argv = []
    for _ in range(argc):
        end = raw.find(b'\0', pos)
        if end < 0:
            raise RuntimeError('truncated KERN_PROCARGS2 argv')
        argv.append(raw[pos:end])
        pos = end + 1
    if not argv[0]:
        raise RuntimeError('empty argv0 is outside declared worker scope')
    return tuple(argv)


def argument_buffer():
    value = ctypes.c_int()
    size = ctypes.c_size_t(ctypes.sizeof(value))
    mib = (ctypes.c_int * 2)(CTL_KERN, KERN_ARGMAX)
    if libc().sysctl(mib, 2, ctypes.byref(value), ctypes.byref(size), None, 0) != 0:
        raise OSError(ctypes.get_errno(), 'KERN_ARGMAX failed')
    if size.value != ctypes.sizeof(value) or not 4096 <= value.value <= 16 * 1024 * 1024:
        raise RuntimeError('invalid/beyond-bounded KERN_ARGMAX')
    return ctypes.create_string_buffer(value.value)


def read_argv(pid, buffer):
    size = ctypes.c_size_t(len(buffer))
    mib = (ctypes.c_int * 3)(CTL_KERN, KERN_PROCARGS2, pid)
    if libc().sysctl(mib, 3, buffer, ctypes.byref(size), None, 0) != 0:
        raise OSError(ctypes.get_errno(), 'KERN_PROCARGS2 failed for pid %d' % pid)
    if not 0 < size.value <= len(buffer):
        raise RuntimeError('invalid KERN_PROCARGS2 reply length')
    return parse_procargs2(ctypes.string_at(buffer, size.value))


def bsd_identity(pid):
    """Selection identity ONLY, not an RSS read of unrelated user processes."""
    S = supervisor()
    n, err, raw = S._read(S.LIBPROC.proc_pidinfo, pid, S.PROC_PIDTBSDINFO, S.BSD_SIZE)
    if n == S.BSD_SIZE:
        ident = S._identity(raw)
        return ('zombie' if ident['status'] == S.SZOMB else 'alive'), ident
    if n == 0 and err == errno.ESRCH:
        return 'gone', {'pid': pid, 'errno': err}
    raise RuntimeError('unknown BSD selection identity for pid %d (bytes%d errno%d)' % (pid, n, err))


def declared_worker_name(comm):
    name = comm.lower()
    return name.startswith('python') or name in ('cadical', 'drat-trim')


def argv_matches(pid, markers, buffer, before):
    try:
        argv = read_argv(pid, buffer)
    except (OSError, RuntimeError):
        after_state, _ = bsd_identity(pid)
        if after_state in ('gone', 'zombie'):
            return False
        raise
    after_state, after = bsd_identity(pid)
    if after_state in ('gone', 'zombie'):
        return False
    if before['start'] != after['start'] or before['comm'] != after['comm']:
        raise RuntimeError('identity/exec transition during argv selection for pid %d' % pid)
    return any(marker in arg for marker in markers for arg in argv)


def read_facts(pids, own_group=None):
    S = supervisor()
    members = set(S.list_pids(S.PROC_PGRP_ONLY, own_group)) if own_group is not None else set()
    facts = {}
    for pid in sorted(set(int(p) for p in pids if p)):
        if pid in members:
            state, rss, identity = S.member_state(pid, own_group, S.probe)
        else:
            state, rss, identity = S.probe(pid)
        if state == 'unknown':
            raise RuntimeError('unknown RSS/identity for pid %s: %r' % (pid, identity))
        if state not in ('alive', 'zombie', 'gone'):
            raise RuntimeError('unrecognised libproc state: ' + str(state))
        facts[pid] = {'state': state, 'rss_bytes': rss if state == 'alive' else 0, 'identity': identity}
    return facts


def rss_kb(pids):
    facts = read_facts(pids, os.getpgrp())
    return (sum(f['rss_bytes'] for f in facts.values()) + 1023) // 1024


def descendants(S, roots):
    result, todo = set(roots), list(roots)
    while todo:
        for child in S.list_pids(S.PROC_PPID_ONLY, todo.pop()):
            if child not in result:
                result.add(child)
                todo.append(child)
    return result


def shared_snapshot(markers):
    if not markers or any(not isinstance(m, str) or not m for m in markers):
        raise ValueError('nonempty process markers required')
    S = supervisor()
    own_roots = {os.getpid()}
    owner = os.environ.get('K3_SUPERVISOR_PID')
    if owner and int(owner) == os.getppid():
        own_roots.add(int(owner))
    own = descendants(S, own_roots)
    selected = set(own)
    marker_bytes = tuple(os.fsencode(m) for m in markers)
    buffer = argument_buffer()
    # All declared phys1 workers are audited non-setuid processes of this UID.
    # Known owned/descendant PIDs are included regardless of name/UID; unrelated
    # user apps are not worker roots. Unknown candidate identities/argv fail closed.
    for pid in S.list_pids(PROC_UID_ONLY, os.geteuid()):
        if pid in own:
            continue
        state, ident = bsd_identity(pid)
        if state in ('gone', 'zombie') or not declared_worker_name(ident['comm']):
            continue
        if argv_matches(pid, marker_bytes, buffer, ident):
            selected.add(pid)
    selected = descendants(S, selected)
    facts = read_facts(selected, os.getpgrp())
    native = {pid for pid, f in facts.items() if f['state'] == 'alive'
              and f['identity'].get('comm') in ('cadical', 'drat-trim')}
    return {'selected_PIDs': sorted(selected), 'own_PIDs': sorted(own), 'native_PIDs': sorted(native),
            'joint_RSS_bytes': sum(f['rss_bytes'] for f in facts.values()),
            'foreign_RSS_bytes': sum(f['rss_bytes'] for pid, f in facts.items() if pid not in own),
            'foreign_native_count': len(native - own), 'joint_native_count': len(native),
            'measurement': 'in-process libproc UID/PPID and KERN_PROCARGS2; no helper processes',
            'unknown_as_zero': False}


def allocated_bytes(root):
    """lstat allocated blocks, no symlink traversal, hardlinks counted once; du-k rounding."""
    pending, seen, total = [Path(root)], set(), 0
    while pending:
        path = pending.pop()
        st = path.lstat()
        key = (st.st_dev, st.st_ino)
        if key in seen:
            continue
        seen.add(key)
        total += st.st_blocks * 512
        if stat.S_ISDIR(st.st_mode):
            with os.scandir(path) as entries:
                pending.extend(Path(entry.path) for entry in entries)
    return ((total + 1023) // 1024) * 1024
