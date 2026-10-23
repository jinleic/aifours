#!/usr/bin/env python3
"""allsing_run.py -- [F] EXPLORATORY driver (c5 README Sec. 7): runs ./allsing on
  p = 11: every all-singleton item-(iii) class (k = 13..19, 1 <= B <= kappa - 1), every word up to rotation;
  p = 13: every class with k <= 20, every word up to rotation;
  p = 17: the classes with B >= 2 and k <= 24 that Theorem IND*'s hypotheses do not cover (c4/out/ind_star3.txt list).
and prints the per-word lines for words where (H) or (H^s) fails plus per-class summaries.  Sequential, one process."""
import subprocess, sys, json, time
def run(p, k, B):
    out = subprocess.run(['./allsing', str(p), str(k), str(B)], capture_output=True, text=True, check=True).stdout
    for line in out.splitlines(): print(line, flush=True)
print('== allsing_run.py start', time.strftime('%Y-%m-%dT%H:%M:%S'), flush=True)
for p, kmax in ((11, 19), (13, 20)):
    for k in range(p + 2, kmax + 1):
        kappa = k - p
        for B in range(1, kappa):
            if k > 2 * p - 3 or 2 * kappa > k - 3: continue
            run(p, k, B)
for (k, B) in ((21, 2), (22, 2), (23, 2), (23, 3), (24, 2), (24, 3)):
    run(17, k, B)
print('== allsing_run.py end', time.strftime('%Y-%m-%dT%H:%M:%S'), flush=True)
