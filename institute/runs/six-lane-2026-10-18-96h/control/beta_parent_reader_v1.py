"""SOURCE ONLY, UNTESTED. Parent beta descriptor-anchored evidence reader.

Scope: beta-parent-reader-scope-v1.json. No file writes, process calls, or clock helper.
The supplied deadline_check returns None or raises; its original deadline must never renew.
A synchronous kernel call may stall. A late result is retained and refused, not certified timely.
Every caller must inspect report()['unresolved']; a read error never implies resource closure.
No receipt, capture, filesystem snapshot or empty report establishes process endedness or release.
"""
import hashlib
import os
import stat

MAX_CAP = 16 << 20
MAX_CALLS = 1024
MAX_RESOURCES = 32768
MAX_COMPONENTS = 128


class EvidenceRefusal(OSError):
    pass


def _path_parts(path):
    if type(path) is not str or not path.startswith('/') or '\x00' in path:
        raise EvidenceRefusal('normalized absolute path required')
    parts = path.split('/')[1:]
    if not parts or len(parts) > MAX_COMPONENTS or any(p in ('', '.', '..') for p in parts):
        raise EvidenceRefusal('normalized path/component limit')
    return parts


def _metadata(info):
    return {'dev': info.st_dev, 'ino': info.st_ino, 'mode': info.st_mode, 'nlink': info.st_nlink,
            'size': info.st_size, 'mtime_ns': info.st_mtime_ns, 'ctime_ns': info.st_ctime_ns}


def _same_file(before, after):
    return all(before[k] == after[k] for k in ('dev', 'ino', 'mode', 'nlink', 'size', 'mtime_ns', 'ctime_ns'))


class EvidenceReader:
    """One parent-owned audit snapshot, with durable in-memory acquisition and close history.

    Ledger entries are retained before the operation and never removed. NOT_ACQUIRED is reserved
    for an os.open/scandir OSError return; an unexpected acquisition exception stays UNKNOWN.
    A close exception is UNKNOWN even when the number later disappears or is reused. No retry.
    This is not a process supervisor. Passing bytes into consumers remains a separate parent act.
    """
    def __init__(self, deadline_check):
        if not callable(deadline_check):
            raise ValueError('deadline_check must be callable')
        self._check = deadline_check
        self._resources = []
        self._observations = []
        self._last = {}
        self._calls = 0

    def _tick(self):
        if self._check() is not None:
            raise EvidenceRefusal('deadline_check must return None or raise')

    def _begin(self, kind, path):
        if len(self._resources) >= MAX_RESOURCES:
            raise EvidenceRefusal('retained resource ledger cap')
        rec = {'id': len(self._resources) + 1, 'kind': kind, 'path': path,
               'state': 'ACQUIRING', 'fd': None, 'close_attempted': False,
               'acquisition_error': None, 'close_error': None}
        self._resources.append(rec)
        return rec

    def _open(self, path, flags, parent=None, display=None):
        rec = self._begin('fd', display if display is not None else path)
        try:
            fd = os.open(path, flags) if parent is None else os.open(path, flags, dir_fd=parent)
        except OSError as exc:
            rec['state'], rec['acquisition_error'] = 'NOT_ACQUIRED', repr(exc)
            raise
        except BaseException as exc:
            rec['state'], rec['acquisition_error'] = 'UNKNOWN', repr(exc)
            raise
        rec['fd'], rec['state'] = fd, 'OWNED'  # no observation or clock may precede this retention
        return rec

    def _close(self, rec):
        if rec['state'] != 'OWNED' or rec['close_attempted']:
            return
        rec['close_attempted'] = True
        try:
            if rec['kind'] == 'fd':
                os.close(rec['fd'])
            else:
                rec['handle'].close()
        except BaseException as exc:
            rec['state'], rec['close_error'] = 'UNKNOWN', repr(exc)
        else:
            rec['state'] = 'CLOSED'  # destructive close result is retained before any next operation

    def _finish(self, owned):
        for rec in reversed(owned):
            self._close(rec)
        if any(r['state'] not in ('CLOSED', 'NOT_ACQUIRED') for r in owned):
            raise EvidenceRefusal('unresolved acquisition/close; inspect reader report')
        self._tick()

    def _start(self):
        self._calls += 1
        if self._calls > MAX_CALLS:
            raise EvidenceRefusal('snapshot call limit')
        self._tick()

    def _directory(self, parts, owned):
        root = self._open('/', os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        owned.append(root)
        current = root['fd']
        location = ''
        for part in parts:
            self._tick()
            location += '/' + part
            rec = self._open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                             current, location)
            owned.append(rec)
            current = rec['fd']
            self._tick()
        return current

    def read_bytes(self, path, cap):
        parts = _path_parts(path)
        if type(cap) is not int or not 0 <= cap <= MAX_CAP:
            raise EvidenceRefusal('exact integer cap in [0,16MiB] required')
        self._start()
        observation = {'path': path, 'kind': 'file', 'cap': cap, 'bytes_seen': 0,
                       'eof': False, 'before': None, 'after': None, 'sha256': None,
                       'completed': False, 'error': None, 'resource_ids': []}
        self._observations.append(observation)
        owned = []
        try:
            parent = self._directory(parts[:-1], owned)
            rec = self._open(parts[-1], os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW,
                             parent, path)
            owned.append(rec)
            before = os.fstat(rec['fd'])
            observation['before'] = _metadata(before)
            self._tick()
            if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1 or before.st_size > cap:
                raise EvidenceRefusal('regular one-link file within cap required')
            chunks = []
            while True:
                self._tick()
                block = os.read(rec['fd'], min(65536, cap + 1 - observation['bytes_seen']))
                observation['bytes_seen'] += len(block)
                if not block:
                    observation['eof'] = True
                else:
                    chunks.append(block)
                self._tick()
                if observation['bytes_seen'] > cap:
                    raise EvidenceRefusal('actual byte cap exceeded')
                if not block:
                    break
            after = os.fstat(rec['fd'])
            observation['after'] = _metadata(after)
            self._tick()
            if not _same_file(observation['before'], observation['after']) or after.st_size != observation['bytes_seen']:
                raise EvidenceRefusal('file identity/link/size/time changed while read')
            data = b''.join(chunks)
            observation['sha256'] = hashlib.sha256(data).hexdigest()
            self._tick()
        except BaseException as exc:
            observation['error'] = repr(exc)
            raise
        finally:
            observation['resource_ids'] = [r['id'] for r in owned]
            self._finish(owned)
        observation['completed'] = True
        self._last[path] = observation
        return data

    def directory_names(self, path, cap=256):
        parts = _path_parts(path)
        if type(cap) is not int or not 0 <= cap <= 256:
            raise EvidenceRefusal('exact directory entry cap in [0,256] required')
        self._start()
        observation = {'path': path, 'kind': 'directory', 'cap': cap, 'names': [],
                       'before': None, 'after': None, 'completed': False, 'error': None,
                       'resource_ids': []}
        self._observations.append(observation)
        owned = []
        try:
            fd = self._directory(parts, owned)
            before = os.fstat(fd)
            observation['before'] = _metadata(before)
            self._tick()
            rec = self._begin('scandir', path)
            owned.append(rec)
            try:
                iterator = os.scandir(fd)
            except OSError as exc:
                rec['state'], rec['acquisition_error'] = 'NOT_ACQUIRED', repr(exc)
                raise
            except BaseException as exc:
                rec['state'], rec['acquisition_error'] = 'UNKNOWN', repr(exc)
                raise
            rec['handle'], rec['state'] = iterator, 'OWNED'
            self._tick()
            for entry in iterator:
                observation['names'].append(entry.name)
                self._tick()
                if len(observation['names']) > cap:
                    raise EvidenceRefusal('directory entry cap exceeded')
            after = os.fstat(fd)
            observation['after'] = _metadata(after)
            self._tick()
            if not _same_file(observation['before'], observation['after']):
                raise EvidenceRefusal('directory changed during census')
        except BaseException as exc:
            observation['error'] = repr(exc)
            raise
        finally:
            observation['resource_ids'] = [r['id'] for r in owned]
            self._finish(owned)
        observation['completed'] = True
        return sorted(observation['names'])

    def last_file(self, path):
        """Return a copy of the latest successful actual metadata; never a failed observation or guessed inode."""
        import copy
        return copy.deepcopy(self._last.get(path))

    def report(self):
        """JSON-shaped snapshot; handles stay owned in this instance, never serialized as success evidence."""
        import copy
        rows = [{k: v for k, v in r.items() if k != 'handle'} for r in self._resources]
        unresolved = [r['id'] for r in rows if r['state'] not in ('CLOSED', 'NOT_ACQUIRED')]
        return copy.deepcopy({'resources': rows, 'observations': self._observations,
                              'unresolved': unresolved, 'calls': self._calls})
