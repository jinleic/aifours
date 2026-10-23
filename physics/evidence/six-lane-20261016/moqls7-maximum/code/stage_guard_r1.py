#!/usr/bin/env python3
"""stage_guard_r1.py: cooperative guard for one stage of the calling process and all its descendants.

Written for the parent source review of the C311+cuts appender (2026-10-18), items 2 and 3.
- install_process_handlers() must be called once from the main thread. SIGTERM then trips the active guard ("external
  SIGTERM"); outside any guarded stage it raises StageTrip directly. SIGUSR1 is internal: a guard that trips in its
  sampler thread uses it to stop the main thread, so blocking calls are interrupted too.
- A StageGuard covers one stage: the calling process plus every descendant. Descendants are the children started
  through guard.popen()/guard.run() and anything they start, found recursively through libproc PROC_PPID_ONLY.
  Every `period` seconds a sampler thread checks aggregate RSS (process + live descendants) <= rss_cap, free bytes
  >= floor, and elapsed <= wall_seconds. An exception inside the sampler is itself a trip (fail closed).
- On a trip, the guard records the first reason, sends SIGTERM to every live descendant, waits at most `grace`
  seconds, and then raises StageTrip in the main thread. stop_all() does the same SIGTERM + bounded wait for normal
  stage ends. Any descendant still alive after the grace period is listed in an exclusive-create quarantine record.
  Callers must refuse admission while that record exists, and the record is never removed by code.
No SIGKILL is sent and no subprocess timeout argument is used.
"""
import ctypes
import json
import os
import signal
import subprocess
import threading
import time

from gram_certify_r4 import LIBPROC, now, rss

PROC_PPID_ONLY = 6
LIBPROC.proc_listpids.argtypes = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_int)
LIBPROC.proc_listpids.restype = ctypes.c_int
_ACTIVE = []
_HANDLERS_INSTALLED = []


class StageTrip(BaseException):
    """Raised in the main thread when a guard trips or the process receives SIGTERM."""


def children(pid):
    buf = (ctypes.c_int * 4096)()
    n = LIBPROC.proc_listpids(PROC_PPID_ONLY, pid, buf, ctypes.sizeof(buf))
    if n < 0:
        raise OSError(ctypes.get_errno(), "proc_listpids failed for %d" % pid)
    return [p for p in buf if p > 0 and p != pid]


def descendants(pid):
    found, frontier = [], [pid]
    while frontier:
        nxt = []
        for parent in frontier:
            for child in children(parent):
                if child not in found and child != pid:
                    found.append(child)
                    nxt.append(child)
        frontier = nxt
    return found


def tree_rss(pid):
    return rss(pid) + sum(rss(d) for d in descendants(pid))


def _on_sigterm(signum, frame):
    if not _ACTIVE:
        raise StageTrip("external SIGTERM outside a guarded stage")
    guard = _ACTIVE[-1]
    if guard._claim("external SIGTERM"):
        guard.stop_all()
        guard._raised = True
        raise StageTrip(guard.reason)


def _on_sigusr1(signum, frame):
    if _ACTIVE:
        guard = _ACTIVE[-1]
        if guard.reason is not None and not guard._raised:
            guard._raised = True
            raise StageTrip(guard.reason)


def install_process_handlers():
    if threading.current_thread() is not threading.main_thread():
        raise RuntimeError("install_process_handlers must run in the main thread")
    signal.signal(signal.SIGTERM, _on_sigterm)
    signal.signal(signal.SIGUSR1, _on_sigusr1)
    _HANDLERS_INSTALLED.append(True)


class StageGuard:
    def __init__(self, name, wall_seconds, rss_cap, floor, lane, quarantine_path, grace=30.0, period=0.25,
                 sampler=tree_rss):
        self.name, self.wall, self.rss_cap, self.floor, self.lane = name, wall_seconds, rss_cap, floor, lane
        self.quarantine_path, self.grace, self.period, self.sampler = quarantine_path, grace, period, sampler
        self.owned, self.reason, self.peak, self.survivors, self.quarantine_record = [], None, 0, [], None
        self.started_at = self.finished_at = None
        self._raised = False
        self._lock = threading.RLock()
        self._stop_lock = threading.RLock()
        self._stop = threading.Event()
        self._thread = None
        self._t0 = None

    def _claim(self, reason):
        with self._lock:
            if self.reason is not None:
                return False
            self.reason = reason
            return True

    def __enter__(self):
        if not _HANDLERS_INSTALLED or threading.current_thread() is not threading.main_thread():
            raise RuntimeError("StageGuard needs install_process_handlers() and the main thread")
        self.started_at, self._t0 = now(), time.monotonic()
        _ACTIVE.append(self)
        self._thread = threading.Thread(target=self._sample, name="stage-guard-" + self.name, daemon=True)
        self._thread.start()
        return self

    def _sample(self):
        while not self._stop.is_set():
            try:
                current = self.sampler(os.getpid())
                self.peak = max(self.peak, current)
                st = os.statvfs(self.lane)
                elapsed = time.monotonic() - self._t0
                if current > self.rss_cap:
                    reason = "aggregate RSS above %d bytes" % self.rss_cap
                elif st.f_bavail * st.f_frsize < self.floor:
                    reason = "free-space floor %d bytes" % self.floor
                elif elapsed > self.wall:
                    reason = "stage wall cap %s s" % self.wall
                else:
                    reason = None
            except Exception as exc:
                reason = "sampler exception: %r" % (exc,)
            if reason is not None:
                if self._claim(reason):
                    self.stop_all()
                    if self in _ACTIVE:
                        os.kill(os.getpid(), signal.SIGUSR1)
                return
            self._stop.wait(self.period)

    def _live(self):
        """Live = has a task (RSS > 0); a dead unreaped child (zombie) has none. Never calls Popen.poll(), so a stop
        run from a signal handler that interrupted Popen.wait() cannot mistake a zombie for a survivor."""
        with self._lock:
            owned = list(self.owned)
        pids = {child.pid for child in owned if child.returncode is None and rss(child.pid) > 0}
        try:
            pids.update(d for d in descendants(os.getpid()) if rss(d) > 0)
        except Exception:
            pass
        return sorted(pids)

    def stop_all(self):
        """SIGTERM every live descendant, wait at most `grace` seconds, quarantine survivors; returns survivors."""
        with self._stop_lock:
            for pid in self._live():
                try:
                    os.kill(pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
            end = time.monotonic() + self.grace
            while self._live() and time.monotonic() < end:
                time.sleep(0.1)
            survivors = self._live()
            with self._lock:
                owned = list(self.owned)
            for child in owned:
                child.poll()
            if survivors:
                self.survivors = sorted(set(self.survivors) | set(survivors))
                record = {"at": now(), "stage": self.name, "reason": self.reason or "survivors at stage end",
                          "survivor_pids": self.survivors, "grace_seconds": self.grace,
                          "rule": "no SIGKILL sent; refuse every later admission while this record exists"}
                try:
                    with open(self.quarantine_path, "x") as f:
                        json.dump(record, f, indent=2)
                        f.write("\n")
                except FileExistsError:
                    pass
                self.quarantine_record = self.quarantine_path
            return survivors

    def popen(self, *args, **kwargs):
        with self._lock:
            if self.reason is not None:
                self._raised = True
                raise StageTrip(self.reason)
            child = subprocess.Popen(*args, **kwargs)
            self.owned.append(child)
        return child

    def run(self, command, input_bytes=None):
        stdin = subprocess.PIPE if input_bytes is not None else subprocess.DEVNULL
        child = self.popen(command, stdin=stdin, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = child.communicate(input_bytes)
        if self.reason is not None:
            self._raised = True
            raise StageTrip(self.reason)
        if child.returncode != 0:
            raise RuntimeError("guarded child %r failed: rc %d: %r" % (command[:3], child.returncode, err[-300:]))
        return out

    def record(self):
        return {"stage": self.name, "started_at": self.started_at, "finished_at": self.finished_at,
                "wall_cap_seconds": self.wall, "rss_cap_bytes": self.rss_cap, "floor_bytes": self.floor,
                "grace_seconds": self.grace, "peak_sampled_tree_rss_bytes": self.peak, "trip_reason": self.reason,
                "owned_children": [{"pid": c.pid, "args": [str(a) for a in c.args][:3], "returncode": c.returncode}
                                   for c in self.owned],
                "survivors": self.survivors, "quarantine_record": self.quarantine_record}

    def __exit__(self, exc_type, exc, tb):
        self._raised = True  # from here on __exit__ reports a trip itself; no asynchronous SIGUSR1 raise
        try:
            self._stop.set()
            if self._thread is not None:
                self._thread.join()
            if self._live():
                self._claim("stage ended with live descendants")
                self.stop_all()
        finally:
            if self in _ACTIVE:
                _ACTIVE.remove(self)
            self.finished_at = now()
        if self.reason is not None and exc_type is None:
            raise StageTrip(self.reason)
        return False
