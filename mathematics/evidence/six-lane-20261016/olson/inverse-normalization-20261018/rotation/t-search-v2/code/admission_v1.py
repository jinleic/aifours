#!/usr/bin/env python3
"""Admission check for one native launch (no launch itself).  Fails closed.
Usage: admission_v1.py MONITOR.jsonl PROJECTED_BYTES
Rules, as the parent restated them in its audit of 2026-10-18 about 12:40:
  (A1) monitor samples are lines {"t": tz-aware ISO time, "free": int}.  Other complete JSON lines (event metadata
       without "t" / "free") are ignored.  A complete line that is not JSON fails.  Only an unterminated last line may
       be ignored.  Sample timestamps must be strictly increasing.
  (A2) freshness: 0 <= now - t_last <= 30 s (a negative age is a future-dated sample: fail).
  (A3) 300 s stability: over the samples with t in [t_last - 300 s, t_last] (at least 25 samples), the largest drop
       from a peak to any later sample must be <= max(300e6, (free_last - 13.5e9)/12).
  (A4) floor: free_last >= 12.2e9 + PROJECTED_BYTES, and a fresh os.statvfs('.') also >= 12.2e9 + PROJECTED_BYTES.
Prints one JSON object with every number used and "verdict": "PASS" or "FAIL"; exit 0 on PASS, 97 on FAIL.
"""
import json, os, sys, datetime


def main():
    mon, projected = sys.argv[1], int(sys.argv[2])
    out = dict(monitor=mon, projected=projected, checked_at=datetime.datetime.now().astimezone().isoformat())
    fails = []
    raw = open(mon, "rb").read().decode("utf-8")
    lines = raw.split("\n")
    complete = lines[:-1]                      # the text after the last newline is unterminated (possibly empty)
    out["unterminated_tail_bytes"] = len(lines[-1])
    samples = []
    for ln in complete:
        if not ln.strip():
            continue
        try:
            r = json.loads(ln)
        except Exception:
            fails.append("A1: malformed complete line"); break
        if "t" in r and "free" in r:
            t = datetime.datetime.fromisoformat(r["t"])
            if t.tzinfo is None:
                fails.append("A1: naive timestamp"); break
            samples.append((t, int(r["free"])))
    if not samples:
        fails.append("A1: no samples")
    else:
        if any(samples[i][0] >= samples[i + 1][0] for i in range(len(samples) - 1)):
            fails.append("A1: timestamps not strictly increasing")
        t_last, free_last = samples[-1]
        now = datetime.datetime.now(datetime.timezone.utc)
        age = (now - t_last).total_seconds()
        out.update(t_last=t_last.isoformat(), free_last=free_last, age_s=round(age, 1))
        if not (0 <= age <= 30):
            fails.append("A2: sample age %.1f s" % age)
        win = [(t, f) for (t, f) in samples if 0 <= (t_last - t).total_seconds() <= 300]
        peak, drop = -1, 0
        for _, f in win:
            peak = max(peak, f)
            drop = max(drop, peak - f)
        allowed = max(300e6, (free_last - 13.5e9) / 12)
        out.update(window_samples=len(win), window_first=win[0][0].isoformat(), window_first_free=win[0][1],
                   max_peak_to_later_drop=drop, allowed_drop=int(allowed))
        if len(win) < 25:
            fails.append("A3: only %d samples in the 300 s window" % len(win))
        if drop > allowed:
            fails.append("A3: drop %d > allowed %d" % (drop, int(allowed)))
        need = 12.2e9 + projected
        st = os.statvfs(".")
        fresh = st.f_bavail * st.f_frsize
        out.update(need=int(need), statvfs_free=fresh)
        if free_last < need:
            fails.append("A4: monitor free below floor")
        if fresh < need:
            fails.append("A4: statvfs free below floor")
    out["fails"] = fails
    out["verdict"] = "PASS" if not fails else "FAIL"
    print(json.dumps(out, sort_keys=True))
    sys.exit(0 if not fails else 97)


if __name__ == "__main__":
    main()
