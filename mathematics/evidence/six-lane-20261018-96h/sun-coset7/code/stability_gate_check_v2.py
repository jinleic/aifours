#!/usr/bin/env python3
"""Lane stability-gate check v2 (stdlib; v1 refused on the observer_start event record, v2 skips records that carry an "event" key and no "t"): reads the parent's resource observer v3 JSONL and applies
RUN/control/resource-stability-addendum-v1.json rule (window 300 s, >= 25 samples, span >= 290 s, last age <= 30 s,
last free >= 13.5e9 + projected, peak-to-later drop <= max(3e8, (last_free - 13.5e9)//12), timezone-aware strictly
increasing timestamps, malformed complete line refuses, only an unterminated final line ignored), plus a fresh
statvfs >= 12.2e9 + projected.  Prints one JSON verdict; exit 0 = PASS, 1 = REFUSE.  Read-only."""
import json, os, sys, datetime, subprocess

MON = '/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/resource-observer-live-v3.jsonl'


def main():
    projected = int(sys.argv[1])
    lane = sys.argv[2]
    now_s = subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True, check=True).stdout.strip()
    now = datetime.datetime.strptime(now_s, '%Y-%m-%dT%H:%M:%S%z')
    raw = open(MON, 'rb').read().decode('utf-8')
    lines = raw.split('\n')
    if raw.endswith('\n'):
        lines = lines[:-1]
        tail_ignored = False
    else:
        tail_ignored = True
        lines = lines[:-1]
    samples = []
    reasons = []
    prev = None
    for ln in lines:
        try:
            o = json.loads(ln)
            if 't' not in o and 'event' in o:
                continue  # observer event record (metadata), not a sample
            t = datetime.datetime.fromisoformat(o['t'])
            f = int(o['free'])
            if t.tzinfo is None:
                raise ValueError('naive timestamp')
        except Exception as e:
            reasons.append('malformed complete line: %r' % ln[:120])
            break
        if prev is not None and not (t > prev):
            reasons.append('timestamps not strictly increasing at %s' % o['t'])
            break
        prev = t
        samples.append((t, f))
    win = [(t, f) for t, f in samples if (now - t).total_seconds() <= 300]
    verdict = {'now': now_s, 'monitor': MON, 'samples_total': len(samples), 'window_samples': len(win),
               'tail_ignored': tail_ignored, 'projected_bytes': projected}
    if not win:
        reasons.append('no samples in window')
    else:
        span = (win[-1][0] - win[0][0]).total_seconds()
        age = (now - win[-1][0]).total_seconds()
        last_free = win[-1][1]
        drop = 0
        peak = -1
        for t, f in win:
            peak = max(peak, f)
            drop = max(drop, peak - f)
        allowed_drop = max(300000000, (last_free - 13500000000) // 12)
        verdict.update(span=span, last_age=age, last_free=last_free, max_peak_to_later_drop=drop, allowed_drop=allowed_drop)
        if len(win) < 25:
            reasons.append('fewer than 25 samples')
        if span < 290:
            reasons.append('span < 290 s')
        if not (0 <= age <= 30):
            reasons.append('last sample age outside [0,30] s')
        if last_free < 13500000000 + projected:
            reasons.append('last free below 13.5e9 + projected')
        if drop > allowed_drop:
            reasons.append('peak-to-later drop too large')
    st = os.statvfs(lane)
    fresh = st.f_bavail * st.f_frsize
    verdict['fresh_statvfs_free'] = fresh
    if fresh < 12200000000 + projected:
        reasons.append('fresh statvfs below 12.2e9 + projected')
    verdict['reasons'] = reasons
    verdict['status'] = 'PASS' if not reasons else 'REFUSE'
    print(json.dumps(verdict))
    return 0 if not reasons else 1


if __name__ == '__main__':
    sys.exit(main())
