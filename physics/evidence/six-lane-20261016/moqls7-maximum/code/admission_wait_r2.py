#!/usr/bin/env python3
"""admission_wait_r2.py: read-only wait for the parent's operational admission rule (long route-A launches).

Successor of admission_wait_r1.py (d0374f5c...6141), which the parent put on HOLD after a Codex review (the r1 watcher
must not be reused). r2 fixes every listed defect:
  1. the deadline is checked before success, and every sleep is capped by the time remaining;
  2. the last sample's age must satisfy 0 <= age <= 30 s, and every timestamp must be timezone-aware and strictly
     increasing (otherwise the evaluation fails: not admitted);
  3. the window is bounded on both sides: samples with t_last - 300 s <= t <= t_last;
  4. tail parsing is tolerant: an unterminated final line (a write in progress) is ignored and the earlier complete
     samples are kept; a malformed complete line still fails the evaluation;
  5. a stale or dead monitor ends the wait without relying on end metadata: if the last sample is older than 120 s,
     or no valid sample has been read for 120 s, it exits 3.

Rule (parent decision, in addition to the frozen launch gate): the parent monitor
institute/runs/six-lane-2026-10-16/review/disk-monitor-v1-20261018T0722-to-1810.jsonl (one {"t", "free"} sample every
10 s; event records without a sample are skipped) must show free_last >= 13.5e9 B and no drop larger than 300 MB in the
preceding 5 minutes, read as: the window holds at least 25 samples spanning at least 290 s, and the largest decline
from any sample to a later sample in the window is at most 300,000,000 B.

Deadline 15:37:00 PDT: the latest start whose 8400 s supervisor wall ends by the 17:57 end of native work. Exit codes:
0 admitted (one JSON line with the evidence), 2 deadline, 3 stale or dead monitor. The script only reads the monitor
file: it writes nothing, signals nothing and launches nothing. Admission is advice to the worker, not a gate result and
not a certificate predicate.
"""
import datetime
import json
import sys
import time

MONITOR = ("/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/"
           "disk-monitor-v1-20261018T0722-to-1810.jsonl")
LEVEL = 13500000000
MAX_DROP = 300000000
WINDOW = 300.0
MIN_SPAN = 290.0
MIN_SAMPLES = 25
FRESH = 30.0
DEAD = 120.0
PERIOD = 10.0
DEADLINE = datetime.datetime.fromisoformat("2026-10-18T15:37:00-07:00")
RULE = {"level": LEVEL, "max_drop": MAX_DROP, "window_s": WINDOW, "min_span_s": MIN_SPAN,
        "min_samples": MIN_SAMPLES, "fresh_s": FRESH, "dead_s": DEAD, "deadline": DEADLINE.isoformat()}


def now():
    return datetime.datetime.now(datetime.timezone.utc).astimezone()


def parse(raw):
    """Complete lines only; an unterminated tail is ignored. Raises ValueError on any malformed complete line."""
    lines = raw.split(b"\n")[:-1]          # the last element is b"" or an unterminated tail
    samples = []
    for line in lines:
        if not line.strip():
            continue
        rec = json.loads(line.decode("utf-8"))
        if not isinstance(rec, dict):
            raise ValueError("record is not an object")
        if "t" not in rec and "free" not in rec:
            continue                        # event record (for example {"event": "start", ...})
        t = datetime.datetime.fromisoformat(rec["t"])
        if t.tzinfo is None or t.utcoffset() is None:
            raise ValueError("timestamp without time zone: %r" % rec["t"])
        free = rec["free"]
        if isinstance(free, bool) or not isinstance(free, int) or free < 0:
            raise ValueError("bad free value: %r" % (free,))
        samples.append((t, free))
    for (t0, _), (t1, _) in zip(samples, samples[1:]):
        if not t1 > t0:
            raise ValueError("timestamps not strictly increasing at %s" % t1.isoformat())
    return samples


def evaluate():
    with open(MONITOR, "rb") as f:
        samples = parse(f.read())
    if not samples:
        return False, None, {"reason": "no complete samples"}
    t_last, free_last = samples[-1]
    age = (now() - t_last).total_seconds()
    low = t_last - datetime.timedelta(seconds=WINDOW)
    window = [(t, v) for t, v in samples if low <= t <= t_last]
    span = (t_last - window[0][0]).total_seconds()
    drop, peak = 0, None
    for _, v in window:
        peak = v if peak is None else max(peak, v)
        drop = max(drop, peak - v)
    facts = {"t_last": t_last.isoformat(), "free_last": free_last, "age_s": round(age, 1),
             "window_samples": len(window), "window_span_s": span, "max_drop_in_window": drop,
             "window_min_free": min(v for _, v in window)}
    ok = (0.0 <= age <= FRESH and len(window) >= MIN_SAMPLES and span >= MIN_SPAN
          and free_last >= LEVEL and drop <= MAX_DROP)
    return ok, age, facts


def emit(obj):
    print(json.dumps(obj), flush=True)


def main():
    last_good = time.monotonic()
    while True:
        if now() >= DEADLINE:
            emit({"admitted": False, "at": now().isoformat(timespec="seconds"), "reason": "deadline", "rule": RULE})
            return 2
        try:
            ok, age, facts = evaluate()
            if age is not None:
                last_good = time.monotonic()
        except (OSError, ValueError, KeyError, TypeError) as exc:
            ok, age, facts = False, None, {"reason": "evaluation failed: %r" % (exc,)}
        if now() >= DEADLINE:
            emit({"admitted": False, "at": now().isoformat(timespec="seconds"), "reason": "deadline", "last": facts,
                  "rule": RULE})
            return 2
        if ok:
            emit({"admitted": True, "at": now().isoformat(timespec="seconds"), "evidence": facts, "rule": RULE})
            return 0
        if (age is not None and age > DEAD) or time.monotonic() - last_good > DEAD:
            emit({"admitted": False, "at": now().isoformat(timespec="seconds"), "reason": "stale or dead monitor",
                  "last": facts, "rule": RULE})
            return 3
        remaining = (DEADLINE - now()).total_seconds()
        time.sleep(max(0.0, min(PERIOD, remaining)))


if __name__ == "__main__":
    sys.exit(main())
