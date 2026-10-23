#!/usr/bin/env python3
"""stability_gate_v2: 300 s disk-stability runway rule on the parent's observer v3 stream (stdlib only).

Stream schema (pinned to RUN/control/resource_observer_v3.py, sha256 given on the command line and re-hashed here):
 line 1: {"event": "observer_start", "at", "pid", "pgid", "cwd", "source_sha256"} with source_sha256 == pinned sha;
 then samples {"t", "free", "floor_bytes", "scope"} exactly (t timezone-aware ISO 8601, free int >= 0,
 floor_bytes == 12000000000, scope str); an {"event": "observer_end", ...} line means the monitor ended -> REFUSE.
 Any other complete line refuses; only an unterminated final line is ignored. Sample timestamps strictly increasing.
Rule (control/resource-stability-addendum-v1.json): window = samples with now-300 <= t <= now (now = /bin/date +%s);
 >= 25 samples; span >= 290 s; 0 <= last age <= 30 s; no future-dated sample; last free >= 13.5e9 + projected;
 max peak-to-later drop in window <= max(3e8, (last_free - 13.5e9) // 12); fresh statvfs(lane) >= 12.2e9 + projected.
Usage: stability_gate_v2.py MONITOR LANE PROJECTED_BYTES RECEIPT OBSERVER_SOURCE OBSERVER_SHA256
Writes RECEIPT exclusively; exit 0 PASS, 1 REFUSE.
"""
import datetime, hashlib, json, os, subprocess, sys

START_KEYS = {"event", "at", "pid", "pgid", "cwd", "source_sha256"}
SAMPLE_KEYS = {"t", "free", "floor_bytes", "scope"}


def main():
    monitor, lane, projected, receipt, obs_src, obs_sha = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6]
    rec = {"monitor": monitor, "projected_new_disk_bytes": projected, "observer_source": obs_src, "observer_sha256_pinned": obs_sha, "reasons": []}
    rec["now_date"] = subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True).stdout.strip()
    now_s = subprocess.run(["/bin/date", "+%s"], capture_output=True, text=True).stdout.strip()
    now = float(now_s) if now_s.isdigit() else None
    if now is None:
        rec["reasons"].append("DATE_UNREADABLE")
    try:
        actual = hashlib.sha256(open(obs_src, "rb").read()).hexdigest()
    except OSError as ex:
        actual = None
        rec["reasons"].append("OBSERVER_SOURCE_UNREADABLE %r" % ex)
    rec["observer_sha256_actual"] = actual
    if actual is not None and actual != obs_sha:
        rec["reasons"].append("OBSERVER_SOURCE_SHA_MISMATCH")
    try:
        raw = open(monitor, "rb").read()
    except OSError as ex:
        raw = b""
        rec["reasons"].append("MONITOR_UNREADABLE %r" % ex)
    parts = raw.split(b"\n")
    rec["ignored_unterminated_final_line"] = bool(parts and parts[-1] != b"")
    complete = parts[:-1]
    samples = []
    for k, ln in enumerate(complete):
        try:
            d = json.loads(ln.decode("utf-8"))
            if not isinstance(d, dict):
                raise ValueError("not an object")
        except Exception as ex:
            rec["reasons"].append("MALFORMED_LINE %d %r" % (k + 1, ex))
            break
        if k == 0:
            if set(d) != START_KEYS or d.get("event") != "observer_start":
                rec["reasons"].append("FIRST_LINE_NOT_OBSERVER_START")
                break
            if d.get("source_sha256") != obs_sha:
                rec["reasons"].append("START_EVENT_SOURCE_SHA_MISMATCH")
                break
            rec["observer_start"] = d
            continue
        if "event" in d:
            if d.get("event") == "observer_end":
                rec["reasons"].append("OBSERVER_ENDED line %d" % (k + 1))
            else:
                rec["reasons"].append("UNKNOWN_EVENT line %d" % (k + 1))
            break
        try:
            if set(d) != SAMPLE_KEYS:
                raise ValueError("sample keys %s" % sorted(d))
            t = datetime.datetime.fromisoformat(d["t"])
            if t.tzinfo is None:
                raise ValueError("naive timestamp")
            if not isinstance(d["free"], int) or isinstance(d["free"], bool) or d["free"] < 0:
                raise ValueError("free not a non-negative int")
            if d["floor_bytes"] != 12000000000 or not isinstance(d["scope"], str):
                raise ValueError("floor/scope")
            samples.append((t.timestamp(), d["free"]))
        except Exception as ex:
            rec["reasons"].append("MALFORMED_SAMPLE line %d %r" % (k + 1, ex))
            break
    if not complete:
        rec["reasons"].append("EMPTY_MONITOR")
    for i in range(1, len(samples)):
        if not samples[i][0] > samples[i - 1][0]:
            rec["reasons"].append("NON_INCREASING_TIMESTAMPS sample %d" % (i + 1))
            break
    rec["samples_total"] = len(samples)
    if now is not None and samples:
        fut = sum(1 for s in samples if s[0] > now)
        rec["future_samples"] = fut
        if fut:
            rec["reasons"].append("FUTURE_DATED_SAMPLE")
        win = [s for s in samples if now - 300 <= s[0] <= now]
        rec["window_samples"] = len(win)
        if len(win) < 25:
            rec["reasons"].append("TOO_FEW_SAMPLES")
        if win:
            span = win[-1][0] - win[0][0]
            age = now - samples[-1][0]
            last_free = win[-1][1]
            drop = max(win[i][1] - min(f for _, f in win[i:]) for i in range(len(win)))
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
        rec["fresh_free"] = st.f_bavail * st.f_frsize
        if rec["fresh_free"] < 12200000000 + projected:
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
