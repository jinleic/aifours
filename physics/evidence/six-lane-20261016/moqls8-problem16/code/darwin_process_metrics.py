"""RSS via the pinned supervisor's real libproc probe, NEVER ps/top/lsof.
Selection uses audited NON-setuid /usr/bin/pgrep; descendant enumeration uses
libproc. No process ownership/signalling is implemented here. Unknown readings
raise; an EPERM is never called zero, gone or zombie. The approved supervisor
alone supplies its narrow fresh-listed ESRCH zombie rule.
"""
from __future__ import annotations

import hashlib
import importlib.util
import os
from pathlib import Path
import re
import stat
import subprocess
import sys

SUPERVISOR = Path('/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code/supervise_r3.py')
SUP_SHA = '0ee8f39496fa3d6051639e99f10d907b8adadcb5d3446f2bb6242c924a83ec4d'
PGREP = Path('/usr/bin/pgrep')
PGREP_SHA = 'eb4d311747498ac6f97ac7fd6c4d0bc8f2dbe77d6a427d645b263760f0fbd027'
_supervisor = None


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def supervisor():
    global _supervisor
    if _supervisor is None:
        if sha(SUPERVISOR) != SUP_SHA:
            raise RuntimeError('pinned libproc implementation changed')
        spec = importlib.util.spec_from_file_location('n8_readonly_libproc_source', SUPERVISOR)
        m = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = m
        spec.loader.exec_module(m)
        _supervisor = m
    return _supervisor


def checked_selector():
    mode = PGREP.stat().st_mode
    if mode & (stat.S_ISUID | stat.S_ISGID) or sha(PGREP) != PGREP_SHA:
        raise RuntimeError('selector is privileged or changed; refusing exec')
    return str(PGREP)


def read_facts(pids, own_group=None):
    S = supervisor()
    fresh_members = set(S.list_pids(S.PROC_PGRP_ONLY, own_group)) if own_group is not None else set()
    facts = {}
    for pid in sorted(set(int(p) for p in pids if p)):
        if pid in fresh_members:
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
    result = set(roots)
    todo = list(roots)
    while todo:
        pid = todo.pop()
        for child in S.list_pids(S.PROC_PPID_ONLY, pid):
            if child not in result:
                result.add(child)
                todo.append(child)
    return result


def shared_snapshot(markers):
    if not markers or any(not isinstance(m, str) or not m for m in markers):
        raise ValueError('nonempty process markers required')
    S = supervisor()
    pattern = '(' + '|'.join(re.escape(m) for m in markers) + ')'
    selected = subprocess.run([checked_selector(), '-f', pattern], capture_output=True, text=True, check=False)
    if selected.returncode not in (0, 1):
        raise RuntimeError('nonprivileged selector failed: ' + selected.stderr)
    matches = set()
    if selected.returncode == 0:
        for line in selected.stdout.splitlines():
            if not line.isdecimal():
                raise RuntimeError('malformed PID selector output')
            matches.add(int(line))
    elif selected.stdout.strip():
        raise RuntimeError('selector rc1 with unexpected output')
    own_roots = {os.getpid()}
    parent_owner = os.environ.get('K3_SUPERVISOR_PID')
    if parent_owner and int(parent_owner) == os.getppid():
        own_roots.add(int(parent_owner))
    own = descendants(S, own_roots)
    all_selected = descendants(S, own | matches)
    facts = read_facts(all_selected, os.getpgrp())
    native = {pid for pid, f in facts.items() if f['state'] == 'alive'
              and f['identity'].get('comm') in ('cadical', 'drat-trim')}
    return {'selected_PIDs': sorted(all_selected), 'own_PIDs': sorted(own), 'native_PIDs': sorted(native),
            'joint_RSS_bytes': sum(f['rss_bytes'] for f in facts.values()),
            'foreign_RSS_bytes': sum(f['rss_bytes'] for pid, f in facts.items() if pid not in own),
            'foreign_native_count': len(native - own), 'joint_native_count': len(native),
            'measurement': 'pinned real libproc; non-setuid selector and libproc PPID expansion',
            'unknown_as_zero': False}
