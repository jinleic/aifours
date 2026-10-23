#!/usr/bin/env python3
"""stability_gate_v1: evaluate the frozen 300 s disk-stability runway rule on the parent's metadata monitor.

Rule source: institute/runs/six-lane-2026-10-18-96h/control/resource-stability-addendum-v1.json (rule) and -v2.json
(monitor path control/resource-observer-live-v3.jsonl). Checks, all required for PASS:
 - every complete line parses as JSON with keys t (timezone-aware ISO 8601) and free (int); only an unterminated
   final line may be ignored; timestamps strictly increasing over all complete lines;
 - window = samples with now-300 <= t <= now (now from /bin/date +%s); >= 25 samples; span >= 290 s;
   0 <= age of last sample <= 30 s (a future-dated sample refuses);
 - last free >= 13.5e9 + projected new disk bytes;
 - maximum peak-to-later drop inside the window <= max(3e8, (last_free - 13.5e9) // 12);
 - fresh statvfs(lane) available >= 12.2e9 + projected new disk bytes.
Usage: stability_gate_v1.py MONITOR LANE PROJECTED_BYTES RECEIPT_PATH ; writes the receipt (exclusive) and exits 0 on
PASS, 1 on REFUSE. Standard library only.
"""
import datetime, json, os, subprocess, sys


def main():
    monitor, lane, projected, receipt = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
    rec = {"monitor": monitor, "projected_new_disk_bytes": projected, "reasons": []}
    now_s = subprocess.run(["/bin/date", "+%s"], capture_output=True, text=True).stdout.strip()
    rec["now_date"] = subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True).stdout.strip()
    try:
        now = float(now_s)
    except ValueError:
        now = None
        rec["reasons"].append("DATE_UNREADABLE")
    try:
        raw = open(monitor, "rb").read()
    except OSError as ex:
        raw = b""
        rec["reasons"].append("MONITOR_UNREADABLE %r" % ex)
    lines = raw.split(b"\n")
    if lines and lines[-1] != b"":
        rec["ignored_unterminated_final_line"] = True
    complete = lines[:-1]
    samples = []
    for k, ln in enumerate(complete):
        try:
            d = json.loads(ln.decode("utf-8"))
            t = datetime.datetime.fromisoformat(d["t"])
            if t.tzinfo is None:
                raise ValueError("naive timestamp")
            fr = d["free"]
            if not isinstance(fr, int):
                raise ValueError("free not int")
            samples.append((t.timestamp(), fr))
        except Exception as ex:
            rec["reasons"].append("MALFORMED_LINE %d %r" % (k + 1, ex))
            break
    for i in range(1, len(samples)):
        if not samples[i][0] > samples[i - 1][0]:
            rec["reasons"].append("NON_INCREASING_TIMESTAMPS at line %d" % (i + 1))
            break
    if now is not None and samples:
        win = [s for s in samples if now - 300 <= s[0] <= now]
        rec["window_samples"] = len(win)
        rec["future_samples"] = sum(1 for s in samples if s[0] > now)
        if rec["future_samples"]:
            rec["reasons"].append("FUTURE_DATED_SAMPLE")
        if len(win) < 25:
            rec["reasons"].append("TOO_FEW_SAMPLES")
        if win:
            span = win[-1][0] - win[0][0]
            age = now - win[-1][0]
            last_free = win[-1][1]
            drop = max((win[i][1] - min(f for _, f in win[i:])) for i in range(len(win)))
            allowed = max(300000000, (last_free - 13500000000) // 12)
            rec.update({"span_s": span, "last_age_s": age, "last_free": last_free, "max_peak_to_later_drop": drop, "allowed_drop": allowed})
            if span < 290:
                rec["reasons"].append("SPAN_TOO_SHORT")
            if not (0 <= age <= 30):
                rec["reasons"].append("LAST_SAMPLE_AGE")
            if last_free < 13500000000 + projected:
                rec["reasons"].append("LAST_FREE_LOW")
            if drop > allowed:
                rec["reasons"].append("DROP_TOO_LARGE")
        else:
            rec["reasons"].append("EMPTY_WINDOW")
    elif not samples:
        rec["reasons"].append("NO_SAMPLES")
    try:
        st = os.statvfs(lane)
        fresh = st.f_bavail * st.f_frsize
        rec["fresh_free"] = fresh
        if fresh < 12200000000 + projected:
            rec["reasons"].append("FRESH_FREE_LOW")
    except OSError as ex:
        rec["reasons"].append("STATVFS_FAILED %r" % ex)
    rec["verdict"] = "PASS" if not rec["reasons"] else "REFUSE"
    with open(receipt, "x") as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps({k: rec.get(k) for k in ("verdict", "reasons", "window_samples", "span_s", "last_age_s", "last_free", "max_peak_to_later_drop", "allowed_drop", "fresh_free")}))
    return 0 if rec["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
