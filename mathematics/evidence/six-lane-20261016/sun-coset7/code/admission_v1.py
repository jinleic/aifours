#!/usr/bin/env python3
"""admission_v1 -- long-job admission check for Stage C (lane sun-coset7), per the parent rule of 13:47 PDT.

Reads the parent disk monitor read-only, takes a fresh statvfs reading of the lane's filesystem, and
writes one exclusive JSON receipt. Exit status 0 = PASS, 1 = FAIL. Never retries.

Rule implemented (all must hold):
  - latest monitor sample age in [0, 30] s (negative age = future-dated sample = FAIL);
  - window = samples with t in [t_last - 300 s, t_last]: at least 25 samples, span >= 290 s;
  - last monitor free >= 13.5e9 + projected growth;
  - max peak-to-later drop inside the window <= max(300e6, (last free - 13.5e9) / 12);
  - fresh statvfs free >= 12.2e9 + projected growth.
Fail-closed parsing: only an unterminated final line is ignored; a malformed complete line, a missing
t/free field, a timezone-naive timestamp, or non-increasing timestamps make the check FAIL.
Lines carrying an "event" key (start/restart records) are skipped.
Usage: python3 admission_v1.py MONITOR_JSONL RECEIPT_JSON PROJECTED_GROWTH_BYTES
"""
import datetime
import hashlib
import json
import os
import sys
import time


def main():
    mon, receipt, growth = sys.argv[1], sys.argv[2], int(sys.argv[3])
    lane = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    t_read = time.time()
    with open(mon, 'rb') as f:
        data = f.read()
    last_nl = data.rfind(b'\n')
    prefix = data[:last_nl + 1] if last_nl >= 0 else b''
    reasons = []
    samples = []
    for ln, raw in enumerate(prefix.split(b'\n')[:-1]):
        try:
            obj = json.loads(raw)
        except Exception:
            reasons.append('malformed complete line %d' % ln)
            break
        if not isinstance(obj, dict):
            reasons.append('non-object line %d' % ln)
            break
        if 'event' in obj:
            continue
        if 't' not in obj or 'free' not in obj:
            reasons.append('line %d lacks t/free' % ln)
            break
        try:
            dt = datetime.datetime.fromisoformat(obj['t'])
        except Exception:
            reasons.append('bad timestamp on line %d' % ln)
            break
        if dt.tzinfo is None:
            reasons.append('timezone-naive timestamp on line %d' % ln)
            break
        if not isinstance(obj['free'], int) or obj['free'] < 0:
            reasons.append('bad free value on line %d' % ln)
            break
        ts = dt.timestamp()
        if samples and ts <= samples[-1][0]:
            reasons.append('non-increasing timestamp on line %d' % ln)
            break
        samples.append((ts, obj['free']))
    st = os.statvfs(lane)
    fresh = st.f_bavail * st.f_frsize
    out = {'checker': 'admission_v1', 'checker_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
           'monitor': mon, 'monitor_prefix_bytes': len(prefix), 'monitor_prefix_sha256': hashlib.sha256(prefix).hexdigest(),
           'monitor_unterminated_tail_bytes': len(data) - len(prefix), 'read_epoch': t_read,
           'read_local': datetime.datetime.fromtimestamp(t_read).astimezone().isoformat(),
           'projected_growth_bytes': growth, 'fresh_statvfs_free': fresh, 'reasons': reasons}
    checks = {}
    if samples and not reasons:
        t_last, f_last = samples[-1]
        age = t_read - t_last
        win = [(t, f) for t, f in samples if t >= t_last - 300]
        span = t_last - win[0][0]
        run_max = -1
        maxdrop = 0
        for _, f in win:
            run_max = max(run_max, f)
            maxdrop = max(maxdrop, run_max - f)
        drop_limit = max(300e6, (f_last - 13.5e9) / 12)
        out.update({'last_sample_epoch': t_last, 'last_sample_free': f_last, 'age_s': age, 'window_samples': len(win),
                    'window_span_s': span, 'window_max_peak_to_later_drop': maxdrop, 'drop_limit': drop_limit})
        checks = {
            'age_in_0_30': 0 <= age <= 30,
            'window_count_ge_25': len(win) >= 25,
            'window_span_ge_290': span >= 290,
            'last_free_ge_13p5e9_plus_growth': f_last >= 13.5e9 + growth,
            'max_drop_le_limit': maxdrop <= drop_limit,
            'fresh_statvfs_ge_12p2e9_plus_growth': fresh >= 12.2e9 + growth,
        }
    elif not samples and not reasons:
        reasons.append('no samples')
    out['checks'] = checks
    out['result'] = 'PASS' if (not reasons and checks and all(checks.values())) else 'FAIL'
    with open(receipt, 'x') as f:
        json.dump(out, f, indent=1)
    print(json.dumps({'receipt': receipt, 'result': out['result'], 'checks': checks, 'reasons': reasons}))
    sys.exit(0 if out['result'] == 'PASS' else 1)


if __name__ == '__main__':
    main()
