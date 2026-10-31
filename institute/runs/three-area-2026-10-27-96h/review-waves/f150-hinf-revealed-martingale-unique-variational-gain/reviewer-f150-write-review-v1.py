#!/usr/bin/env python3
"""Exclusive creation of the completed review with an observed native-clock header."""
from pathlib import Path
import hashlib, json, subprocess
r=Path(__file__).resolve().parent
body=r/'reviewer-f150-review-body-v1.md'
out=r/'review-v1.md'
receipt=r/'reviewer-f150-review-write-receipt-v1.json'
for p in (out,receipt):
    if p.exists(): raise SystemExit('Refuse overwrite: '+str(p))
clock=subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()
text=body.read_text()
first,rest=text.split('\n',1)
text=first+'\n\nObserved native clock immediately before review creation: '+clock+'.\n'+rest
with out.open('x') as f:f.write(text)
def meta(p):
    b=p.read_bytes()
    return {'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'LF':b.count(b'\n')}
clock2=subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()
data={'kind':'INDEPENDENT_SAME_HARNESS_REVIEW_CREATION_RECEIPT','observed_before_review_write':clock,
      'observed_after_review_write_before_receipt_write':clock2,'review':meta(out),
      'reviewer_body':meta(body),'control_run_receipt_v2':meta(r/'reviewer-f150-run-receipt-v2.json'),
      'writer':meta(Path(__file__).resolve()),'overall_correctness':'correct',
      'fatal':0,'major':0,'minor':0,'confidence':0.95,
      'limits':'Assigned law only; not parent acceptance, human/cross-family/formal/kernel/novelty verification. Original epsilon-log and optional alternative assessed separately.'}
with receipt.open('x') as f:json.dump(data,f,indent=2);f.write('\n')
print(json.dumps(data,indent=2))
