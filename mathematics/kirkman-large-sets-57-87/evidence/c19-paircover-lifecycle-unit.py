#!/usr/bin/env python3
"""Unit-only regression: virtual clock and fake native child; launches no child."""
import argparse
import io
import json
from pathlib import Path
import signal
import sys
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "work"))
import c19_staged_completion as subject


class Clock:
    def __init__(self):
        self.now = 0.0

    def monotonic(self):
        return self.now


class FakeChild:
    pid = 424242

    def __init__(self, clock, stop_at=None, response_delay=None, normal_exit=None):
        self.clock = clock
        self.stop_at = stop_at
        self.response_delay = response_delay
        self.normal_exit = normal_exit
        self.term_at = None
        self.returncode = None
        self.waits = 0

    def poll(self):
        return self.returncode

    def wait(self, timeout=None):
        self.waits += 1
        if self.returncode is not None:
            return self.returncode
        assert timeout is not None, "unbounded wait on a live fake child"
        end = self.clock.now + timeout
        if self.stop_at is not None and not subject.STOP.is_set() and self.stop_at <= end:
            self.clock.now = self.stop_at
            subject.cancel("UNIT_PEER_VERIFIED_TARGET")
        if self.normal_exit is not None and self.normal_exit <= end:
            self.clock.now = self.normal_exit
            self.returncode = 10
            return self.returncode
        if self.term_at is not None and self.response_delay is not None and self.term_at + self.response_delay <= end:
            self.clock.now = self.term_at + self.response_delay
            self.returncode = -signal.SIGTERM
            return self.returncode
        self.clock.now = end
        raise subject.subprocess.TimeoutExpired("unit-only-fake-child", timeout)


class MemoryLog:
    def open(self, mode="r"):
        return io.BytesIO() if "b" in mode else io.StringIO("")


def one_case(name, *, stop_at=None, response_delay=None, normal_exit=None, caller=False, precancel=False):
    subject.STOP.clear()
    subject.STOP_REASON = None
    subject.CANCELLED_AT = None
    subject.TERM_REQUESTED_PROCESS = None
    subject.ACTIVE_PROCESS = None
    subject.ACTIVE_SOLVER = None
    clock = Clock()
    child = FakeChild(clock, stop_at, response_delay, normal_exit)
    signals = []

    def fake_killpg(pid, sig):
        assert pid == child.pid and sig == signal.SIGTERM, "only SIGTERM is authorized"
        signals.append([clock.now, int(sig)])
        child.term_at = clock.now

    with patch.object(subject.time, "monotonic", clock.monotonic), patch.object(subject.os, "killpg", fake_killpg):
        if precancel:
            subject.cancel("UNIT_PRESTART_CANCEL")
        if caller:
            with patch.object(subject.subprocess, "Popen", return_value=child), \
                 patch.object(subject, "Path", return_value=MemoryLog()), \
                 patch.object(subject, "digest", return_value="unit-only-not-a-real-log-hash"):
                selected, info = subject.native_solve("unit-only.cnf", "kissat", "sat", 1, 7200, 1, "memory-log")
            code = info["exit_code"]
        else:
            subject.ACTIVE_PROCESS = child
            code = subject.wait_native(child, 7200)
            info = None
    if normal_exit is not None:
        assert code == 10 and clock.now == normal_exit and not signals
    elif response_delay is None:
        assert code is None and clock.now == 35.0
        assert subject.CANCELLED_AT == 5.0 and subject.ACTIVE_PROCESS is child
        assert signals == [[5.0, int(signal.SIGTERM)]]
        if caller:
            assert info["status"] == "UNRESPONSIVE_CHILD" and not info["cleanup_complete"]
            assert info["unresponsive_child_pid"] == child.pid
    else:
        expected = (0.0 if precancel else 5.0) + response_delay
        assert code == -signal.SIGTERM and clock.now == expected
        assert len(signals) == 1
        if caller:
            assert subject.ACTIVE_PROCESS is None and info["cleanup_complete"]
    result = {"name": name, "status": "PASS", "simulated_exit_time": clock.now,
              "simulated_returncode": code, "signals": signals,
              "handle_retained": subject.ACTIVE_PROCESS is child,
              "caller_cleanup_complete": info.get("cleanup_complete") if info else None}
    subject.ACTIVE_PROCESS = None
    subject.STOP.clear()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("refusing to overwrite a prior unit receipt")
    source_hash = subject.digest(subject.__file__)
    results = [
        one_case("normal_exit_is_reaped", normal_exit=3.0),
        one_case("early_cancel_responsive", stop_at=5.0, response_delay=0.2),
        one_case("early_cancel_unresponsive_grace_at35", stop_at=5.0),
        one_case("native_caller_retains_unresponsive_handle", stop_at=5.0, caller=True),
        one_case("native_caller_clears_reaped_handle", stop_at=5.0, response_delay=0.2, caller=True),
        one_case("cancel_before_spawn_still_signals_child", response_delay=0.2, precancel=True),
    ]
    result = {"status": "PASS", "scope": "unit-only virtual clock and fake child; no solver or operating-system child launched",
              "source_sha256": source_hash, "unit_source_sha256": subject.digest(__file__),
              "command": sys.argv, "cases": results, "real_children_launched": 0, "SIGKILL_calls": 0}
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
