#!/usr/bin/env python3
"""admission_wait_r1.py: read-only wait for the parent's operational admission rule (route A attempt 5).

Parent decision (message after the 07:10:39 floor stop): launch attempt 5 only when the parent's disk monitor
(institute/runs/six-lane-2026-10-16/review/disk-monitor-v1-20261018T0700.jsonl, one {"t", "free"} sample every 10 s)
shows free >= 13.5e9 B AND no drop larger than 300 MB in the preceding 5 minutes. This is in addition to the frozen
launch gate (fresh statvfs >= 12.2e9 B + growth), which the worker and the driver still apply at launch.

This script only reads the monitor file. It writes nothing, signals nothing and launches nothing. Every 10 s it
evaluates the rule on the latest sample L and the window W of samples with t in [t_L - 300 s, t_L]:
  - fresh:     host time - t_L <= 30 s;
  - covered:   W has at least 25 samples and its earliest sample is at or before t_L - 290 s;
  - level:     free_L >= 13,500,000,000 B;
  - no drop:   max over samples i before j in W of (free_i - free_j) <= 300,000,000 B.
Freshness and coverage are conservative additions, so that a stale or short monitor never admits. A malformed line
makes that evaluation fail (not admitted); monitor event records without a sample (for example {"event": "start"})
are skipped. On admission it prints one JSON line with the evidence and exits 0. At the deadline (16:10:00 PDT, the
latest start that leaves the 8400 s supervisor wall before 18:31:43) it prints one JSON line and exits 2. If the
monitor's announced end_epoch has passed and its last sample is stale, it prints one JSON line and exits 3.
Admission is advice to the worker; it is not a gate result and not a certificate predicate.
"""
import datetime
import json
import sys
import time

MONITOR = ("/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/"
           "disk-monitor-v1-20261018T0700.jsonl")
LEVEL = 13500000000
MAX_DROP = 300000000
WINDOW = 300.0
MIN_SPAN = 290.0
MIN_SAMPLES = 25
FRESH = 30.0
PERIOD = 10.0
DEADLINE = datetime.datetime.fromisoformat("2026-10-18T16:10:00-07:00")


def now():
    return datetime.datetime.now(datetime.timezone.utc).astimezone()


def evaluate():
    with open(MONITOR, "rb") as f:
        raw = f.read()
    samples, end_epoch = [], None
    for line in raw.split(b"\n"):
        if not line.strip():
            continue
        rec = json.loads(line.decode("utf-8"))
        if "t" not in rec or "free" not in rec:
            if rec.get("event") == "start" and "end_epoch" in rec:
                end_epoch = float(rec["end_epoch"])
            continue  # monitor event records carry no sample
        samples.append((datetime.datetime.fromisoformat(rec["t"]), int(rec["free"])))
    if not samples:
        return False, {"reason": "no samples"}
    t_last, free_last = samples[-1]
    window = [(t, v) for t, v in samples if (t_last - t).total_seconds() <= WINDOW]
    age = (now() - t_last).total_seconds()
    span = (t_last - window[0][0]).total_seconds()
    drop, peak = 0, None
    for _, v in window:
        peak = v if peak is None else max(peak, v)
        drop = max(drop, peak - v)
    facts = {"t_last": t_last.isoformat(), "free_last": free_last, "age_s": round(age, 1),
             "window_samples": len(window), "window_span_s": span, "max_drop_in_window": drop,
             "window_min_free": min(v for _, v in window), "monitor_end_epoch": end_epoch}
    ok = (age <= FRESH and len(window) >= MIN_SAMPLES and span >= MIN_SPAN
          and free_last >= LEVEL and drop <= MAX_DROP)
    return ok, facts


def main():
    while True:
        try:
            ok, facts = evaluate()
        except (OSError, ValueError, KeyError, TypeError) as exc:
            ok, facts = False, {"reason": "evaluation failed: %r" % (exc,)}
        if ok:
            print(json.dumps({"admitted": True, "at": now().isoformat(timespec="seconds"), "evidence": facts,
                              "rule": {"level": LEVEL, "max_drop": MAX_DROP, "window_s": WINDOW,
                                       "fresh_s": FRESH, "min_span_s": MIN_SPAN, "min_samples": MIN_SAMPLES}}),
                  flush=True)
            return 0
        if now() >= DEADLINE:
            print(json.dumps({"admitted": False, "at": now().isoformat(timespec="seconds"),
                              "reason": "deadline", "last": facts}), flush=True)
            return 2
        end = facts.get("monitor_end_epoch")
        if end is not None and time.time() > end + FRESH and facts.get("age_s", 0) > FRESH:
            print(json.dumps({"admitted": False, "at": now().isoformat(timespec="seconds"),
                              "reason": "monitor ended", "last": facts}), flush=True)
            return 3
        time.sleep(PERIOD)


if __name__ == "__main__":
    sys.exit(main())
