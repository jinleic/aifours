#!/usr/bin/env python3
"""stability_gate_v2_selftest_v2 (v1 never ran; v1 fixture F09 could not trip the drop rule): retained fixtures + real-stream smoke for stability_gate_v2 (stdlib, no science).

Creates fixture streams (exclusive files) in FIXDIR with timestamps relative to /bin/date now, runs the frozen gate on
each as a subprocess and on the REAL observer stream, and records expected vs actual verdict and reason keywords.
Usage: stability_gate_v2_selftest_v1.py GATE_PY FIXDIR LANE REAL_MONITOR OBSERVER_SOURCE OBSERVER_SHA256 SUMMARY_JSON
Exit 0 iff every fixture matches its expectation (the real-stream verdict is recorded; its expectation is PASS).
"""
import datetime, json, os, subprocess, sys, time

T0 = time.monotonic()
GATE, FIX, LANE, REAL, OBS, OSHA, SUMMARY = sys.argv[1:8]
os.makedirs(FIX, exist_ok=False)
now = int(subprocess.run(["/bin/date", "+%s"], capture_output=True, text=True).stdout.strip())
tz = datetime.timezone(datetime.timedelta(hours=-7))


def iso(ts):
    return datetime.datetime.fromtimestamp(ts, tz).isoformat(timespec="seconds")


def start_line(sha=OSHA):
    return json.dumps({"event": "observer_start", "at": iso(now - 400), "pid": 1, "pgid": 1, "cwd": "/fixture", "source_sha256": sha})


def sample(ts, free):
    return json.dumps({"t": iso(ts), "free": free, "floor_bytes": 12000000000, "scope": "metadata only; not scientific checkpoint or launch admission"})


def good_samples(end_offset=5, n=31, free=190000000000, step=10, drift=None):
    out = []
    for k in range(n):
        ts = now - end_offset - (n - 1 - k) * step
        f = free if drift is None else free - drift * k
        out.append(sample(ts, f))
    return out


F = {}
F["F01_positive_synthetic"] = ([start_line()] + good_samples(), True, "PASS", [])
s = good_samples()
s[15] = "{bad json"
F["F02_malformed_line"] = ([start_line()] + s, True, "REFUSE", ["MALFORMED"])
s = good_samples()
s[-1] = sample(now + 60, 190000000000)
F["F03_future_sample"] = ([start_line()] + s, True, "REFUSE", ["FUTURE_DATED_SAMPLE"])
F["F04_stale_stream"] = ([start_line()] + good_samples(end_offset=120), True, "REFUSE", ["LAST_SAMPLE_AGE"])
F["F05_observer_end"] = ([start_line()] + good_samples() + [json.dumps({"event": "observer_end", "at": iso(now - 1), "sigterm_or_sigint": True})], True, "REFUSE", ["OBSERVER_ENDED"])
F["F06_no_start_event"] = (good_samples(), True, "REFUSE", ["FIRST_LINE_NOT_OBSERVER_START"])
F["F07_wrong_source_sha"] = ([start_line("0" * 64)] + good_samples(), True, "REFUSE", ["START_EVENT_SOURCE_SHA_MISMATCH"])
F["F08_unterminated_final_line"] = ([start_line()] + good_samples() + ['{"t": "garb'], False, "PASS", [])
F["F09_drop_too_large"] = ([start_line()] + good_samples(free=20000000000, drift=200000000), True, "REFUSE", ["DROP_TOO_LARGE"])
s = good_samples()
s[20], s[21] = s[21], s[20]
F["F10_non_increasing"] = ([start_line()] + s, True, "REFUSE", ["NON_INCREASING"])
F["F11_too_few_samples"] = ([start_line()] + good_samples(n=20), True, "REFUSE", ["TOO_FEW_SAMPLES"])
F["F12_low_free"] = ([start_line()] + good_samples(free=13000000000), True, "REFUSE", ["LAST_FREE_LOW"])

results = {}
ok_all = True
for name, (lines, terminated, expect, keys) in F.items():
    path = os.path.join(FIX, name + ".jsonl")
    with open(path, "x") as fh:
        fh.write("\n".join(lines) + ("\n" if terminated else ""))
    rcpt = os.path.join(FIX, name + ".gate-receipt.json")
    r = subprocess.run([sys.executable, "-I", "-B", GATE, path, LANE, "10485760", rcpt, OBS, OSHA], capture_output=True, text=True)
    got = json.load(open(rcpt))
    match = (got["verdict"] == expect) and all(any(k in reason for reason in got["reasons"]) for k in keys)
    ok_all &= match
    results[name] = {"expect": expect, "keys": keys, "verdict": got["verdict"], "reasons": got["reasons"], "exit": r.returncode, "match": match}
real_rcpt = os.path.join(FIX, "REAL_stream.gate-receipt.json")
r = subprocess.run([sys.executable, "-I", "-B", GATE, REAL, LANE, "10485760", real_rcpt, OBS, OSHA], capture_output=True, text=True)
got = json.load(open(real_rcpt))
results["REAL_stream"] = {"expect": "PASS", "verdict": got["verdict"], "reasons": got["reasons"], "exit": r.returncode,
                          "window_samples": got.get("window_samples"), "span_s": got.get("span_s"), "last_age_s": got.get("last_age_s"),
                          "last_free": got.get("last_free"), "max_peak_to_later_drop": got.get("max_peak_to_later_drop")}
out = {"selftest": "stability_gate_v2_selftest_v2", "now_epoch": now, "fixtures_all_match": ok_all, "results": results,
       "elapsed_s": round(time.monotonic() - T0, 3)}
with open(SUMMARY, "x") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({"fixtures_all_match": ok_all, "real": results["REAL_stream"]["verdict"], "elapsed_s": out["elapsed_s"]}))
sys.exit(0 if ok_all else 1)
