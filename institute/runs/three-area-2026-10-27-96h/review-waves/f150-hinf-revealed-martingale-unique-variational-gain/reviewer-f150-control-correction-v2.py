#!/usr/bin/env python3
"""Additive reviewer correction only; originals remain immutable.
The original candidate claims >c for sufficiently small epsilon, not for .1.
v1 control accidentally required >c also at epsilon=.1. It observed F-c<0,
while every exact certificate and every actual stated chain inequality passed.
v2 separates the valid lower-bound chain from the small-e sign condition and
uses .1 as an intended-reason negative control. No mathematical source edited.
"""
from pathlib import Path
import subprocess
r=Path(__file__).resolve().parent
p=r/'reviewer-f150-independent-controls-v1.py'
s=p.read_text()
s=s.replace("check('D2 original epsilon-log chain e='+text,\n          l1>=1-e and l2>=e*(1-e)/4 and f>=low1 and increment>=C*s*s*mp.log(1/s) and f>c,\n          'F-c='+mp.nstr(f-c,12))",
"check('D2 original epsilon-log chain e='+text,\n          l1>=1-e and l2>=e*(1-e)/4 and f>=low1 and increment>=C*s*s*mp.log(1/s),\n          'F-c='+mp.nstr(f-c,12))\n    check(('ND3 negative: epsilon=.1 is not sufficiently small' if text=='0.1' else 'D2b strict improvement at epsilon='+text),\n          f<c if text=='0.1' else f>c)")
assert s!=p.read_text()
with (r/'reviewer-f150-independent-controls-v2.py').open('x') as f: f.write(s)
s=(r/'reviewer-f150-run-controls-v1.py').read_text()
s=s.replace("control=root/'reviewer-f150-independent-controls-v1.py'","control=root/'reviewer-f150-independent-controls-v2.py'")
s=s.replace("log=root/'reviewer-f150-independent-controls-v1.log'","log=root/'reviewer-f150-independent-controls-v2.log'")
s=s.replace("receipt=root/'reviewer-f150-run-receipt-v1.json'","receipt=root/'reviewer-f150-run-receipt-v2.json'")
s=s.replace("'child_start':start,'child_end':end,'returncode':p.returncode,", "'child_start':start,'child_end':end,'returncode':p.returncode,\n      'prior_run':meta(root/'reviewer-f150-run-receipt-v1.json'),\n      'reviewer_correction':meta(root/'reviewer-f150-control-correction-v2.py'),\n      'correction_reason':'v1 erroneously demanded F(nu_e)>c at e=.1; candidate claims only sufficiently small e. v2 retains the chain at .1 and treats F<c there as a negative control.',")
with (r/'reviewer-f150-run-controls-v2.py').open('x') as f: f.write(s)
print('Created additive v2 controls/runner; v1 files and receipts preserved. Clock:',subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip())
