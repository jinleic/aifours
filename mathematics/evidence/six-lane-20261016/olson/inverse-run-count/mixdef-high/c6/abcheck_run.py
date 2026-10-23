#!/usr/bin/env python3
"""abcheck_run.py -- [F] driver: ./abcheck on every all-single-letter item-(iii) class with B >= 4 (only those can have anti-heavy
intervals) for p = 11 (k <= 19) and p = 13 (k <= 20); prints per-class lines and totals."""
import subprocess, json, time
print('== abcheck_run.py start', time.strftime('%Y-%m-%dT%H:%M:%S'), flush=True)
tot = {'classes': 0, 'words': 0, 'heavy_intervals': 0, 'violations': 0, 'thr_plus1_intervals': 0, 'thr_plus1_certified': 0}
for p, kmax in ((11, 19), (13, 20)):
    for k in range(p + 2, kmax + 1):
        for B in range(4, k - p):
            if k - p - B < 1: continue
            out = subprocess.run(['./abcheck', str(p), str(k), str(B)], capture_output=True, text=True, check=True).stdout.strip()
            print(out, flush=True)
            d = json.loads(out); tot['classes'] += 1
            for key in ('words', 'heavy_intervals', 'violations', 'thr_plus1_intervals', 'thr_plus1_certified'): tot[key] += d[key]
print(json.dumps(tot), flush=True)
print('== abcheck_run.py end', time.strftime('%Y-%m-%dT%H:%M:%S'), flush=True)
