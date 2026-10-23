#!/usr/bin/env python3
"""Runner-local conservative budget overlay; immutable guard15 source/proof/cap logic is unchanged.
One3h chunk reserves90s for receipt shutdown. Every guard15 admission (including post-token/post-BigLock) needs
2400s left, deliberately conservative for native600/check1200 plus existing grace/TERM/reader-feed margins.
Token-count polling also checks it, so token wait defers before consuming the allowance. A single runner alarm at
the reserved cutoff breaks token/BigLock waits only when no owned child is alive/starting. With a live/starting
child it merely sets ABORT, never signals it; guard15's existing native limits/owned-child quarantine remain in
force and no further stage is admitted. Survivor quarantine is not an instantaneous wall/RSS hard-cap claim.
Timer is armed ONLY around an existing staged call, not while writing outer receipts. No extra process/thread.
"""
import signal
import time


class ChunkBudget:
    def __init__(self, guard, run_deadline_wall, chunk_seconds=10800, reserve_seconds=90, allowance_seconds=2400):
        self.guard = guard
        self.allowance = allowance_seconds
        self.deadline = min(time.monotonic()+chunk_seconds-reserve_seconds,
                            time.monotonic()+run_deadline_wall-time.time()-reserve_seconds)
        self.base_reason = guard.admitted_reason
        self.base_count = guard.token_count
        self.alarm_fired = False
        self.active = False

    def reason(self):
        why = self.base_reason()
        if why:
            return why
        if self.alarm_fired or time.monotonic()+self.allowance > self.deadline:
            return 'chunk/run budget: conservative next-stage allowance does not fit'
        return None

    def _count(self):
        why = self.reason()
        if why:
            raise self.guard.AdmissionDenied(why)
        return self.base_count()

    def _alarm(self, signum, frame):
        self.alarm_fired = True
        self.guard.ABORT[0] = True
        with self.guard._alock:
            live = any(p.poll() is None for p in self.guard.ACTIVE)
        if not live and not self.guard.SPAWNING[0]:
            raise self.guard.AdmissionDenied('chunk/run reserved cutoff while waiting; no child started')
        # Do not send an extra signal to an owned native/quarantined child. The immutable guard retains capacity.

    def __enter__(self):
        why = self.reason()
        if why:
            raise self.guard.AdmissionDenied(why)
        assert not self.active and self.guard.admitted_reason is self.base_reason and self.guard.token_count is self.base_count
        if signal.getitimer(signal.ITIMER_REAL) != (0.0,0.0):
            raise RuntimeError('refuse to replace a pre-existing runner timer')
        self.old_handler = signal.getsignal(signal.SIGALRM)
        self.guard.admitted_reason = self.reason
        self.guard.token_count = self._count
        try:
            signal.signal(signal.SIGALRM,self._alarm)
            signal.setitimer(signal.ITIMER_REAL,max(0.001,self.deadline-time.monotonic()))
        except BaseException:
            self.guard.admitted_reason = self.base_reason
            self.guard.token_count = self.base_count
            signal.signal(signal.SIGALRM,self.old_handler)
            raise
        self.active = True
        return self

    def __exit__(self,*exc):
        signal.setitimer(signal.ITIMER_REAL,0)
        self.guard.admitted_reason = self.base_reason
        self.guard.token_count = self.base_count
        signal.signal(signal.SIGALRM,self.old_handler)
        self.active = False
