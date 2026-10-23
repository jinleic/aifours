#!/usr/bin/env python3
"""admission_v2 -- long-job admission check for Stage C (lane sun-coset7), parent rule of 13:47 PDT 2026-10-18.

v2 = v1 with: the monitor file is read FIRST and the fresh clock and statvfs are read AFTER it, so a sample
written during the check can never look future-dated; duplicate JSON keys and non-int/boolean 'free'
values fail closed.

Reads the parent disk monitor read-only, then the clock, then a fresh statvfs of the lane's filesystem, and
writes one exclusive JSON receipt. Exit status 0 = PASS, 1 = FAIL. Never retries. Any exception (including
an existing receipt path) exits non-zero, which every caller treats as FAIL.

Rule (all must hold):
  - age = now - t_last in [0, 30] s, where now is read after the monitor (negative age = FAIL);
  - window = samples with t in [t_last - 300 s, t_last]: at least 25 samples, span >= 290 s;
  - last monitor free >= 13.5e9 + projected growth;
  - max peak-to-later drop inside the window <= max(300e6, (last free - 13.5e9) / 12);
  - fresh statvfs free >= 12.2e9 + projected growth.
Fail-closed parsing: only an unterminated final line is ignored; a malformed complete line, a duplicate
key, a missing or ill-typed t/free field, a timezone-naive timestamp, or a non-increasing timestamp makes
the check FAIL. Lines carrying an "event" key (start/restart/end records) are skipped.
Usage: python3 admission_v2.py MONITOR_JSONL RECEIPT_JSON PROJECTED_GROWTH_BYTES
"""
import datetime
import hashlib
import json
import os
import sys
import time


class DuplicateKey(ValueError):
    pass


def _no_dupes(pairs):
    out = {}
    for k, v in pairs:
        if k in out:
            raise DuplicateKey(k)
        out[k] = v
    return out


def main():
    mon, receipt, growth = sys.argv[1], sys.argv[2], int(sys.argv[3])
    lane = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 1. monitor first
    with open(mon, 'rb') as f:
        data = f.read()
    # 2. then the fresh clock, then the fresh statvfs
    t_now = time.time()
    st = os.statvfs(lane)
    fresh = st.f_bavail * st.f_frsize
    last_nl = data.rfind(b'\n')
    prefix = data[:last_nl + 1] if last_nl >= 0 else b''
    reasons = []
    samples = []
    for ln, raw in enumerate(prefix.split(b'\n')[:-1]):
        try:
            obj = json.loads(raw, object_pairs_hook=_no_dupes)
        except Exception as e:
            reasons.append('malformed or duplicate-key complete line %d (%s)' % (ln, type(e).__name__))
            break
        if not isinstance(obj, dict):
            reasons.append('non-object line %d' % ln)
            break
        if 'event' in obj:
            continue
        t, free = obj.get('t'), obj.get('free')
        if not isinstance(t, str) or type(free) is not int or free < 0:
            reasons.append('line %d lacks a string t or a non-negative int free' % ln)
            break
        try:
            dt = datetime.datetime.fromisoformat(t)
        except Exception:
            reasons.append('bad timestamp on line %d' % ln)
            break
        if dt.tzinfo is None:
            reasons.append('timezone-naive timestamp on line %d' % ln)
            break
        ts = dt.timestamp()
        if samples and ts <= samples[-1][0]:
            reasons.append('non-increasing timestamp on line %d' % ln)
            break
        samples.append((ts, free))
    out = {'checker': 'admission_v2',
           'checker_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
           'read_order': 'monitor file, then clock, then statvfs',
           'monitor': mon, 'monitor_prefix_bytes': len(prefix), 'monitor_prefix_sha256': hashlib.sha256(prefix).hexdigest(),
           'monitor_unterminated_tail_bytes': len(data) - len(prefix), 'now_epoch': t_now,
           'now_local': datetime.datetime.fromtimestamp(t_now).astimezone().isoformat(),
           'projected_growth_bytes': growth, 'fresh_statvfs_free': fresh, 'reasons': reasons}
    checks = {}
    if samples and not reasons:
        t_last, f_last = samples[-1]
        age = t_now - t_last
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
