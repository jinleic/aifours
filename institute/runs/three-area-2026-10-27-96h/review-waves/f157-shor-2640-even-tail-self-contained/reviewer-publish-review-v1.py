#!/usr/bin/env python3
"""Exclusive publication of the completed review; no evidence overwrites."""
import datetime, hashlib, json, pathlib
ROOT=pathlib.Path(__file__).resolve().parent
TARGET=ROOT/'review-v1.md'
RECEIPT=ROOT/'reviewer-review-publication-v1.json'
assert not TARGET.exists() and not RECEIPT.exists()
text=(ROOT/'reviewer-review-prepublication-v1.md').read_text()
# Correct the prepublication draft's upper requested range to the actual LF count.
needle='covering its full 1–1455 lines'
assert text.count(needle)==1
text=text.replace(needle,'covering all 1–1434 actual lines (the final requested range ended at 1455)')
assert len((ROOT/'reviewer-pinned-dependency-render-v1.txt').read_bytes().splitlines())==1434
clock=datetime.datetime.now(datetime.timezone.utc).isoformat()
with TARGET.open('x') as f:
    f.write(text)
files={}
for p in sorted(ROOT.iterdir()):
    if p.is_file() and (p.name.startswith('reviewer-') or p.name=='review-v1.md'):
        b=p.read_bytes()
        files[p.name]={'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'LF':b.count(b'\n')}
receipt={'observed_utc_immediately_before_review_write':clock,
         'review':files['review-v1.md'],'files':files,
         'prepublication_metadata_correction':'Source rendering has 1434 actual LF; final read request extended through 1455. Corrected draft description before first publication, no mathematical payload changed.',
         'overall_correctness':'correct','FATAL':0,'MAJOR':0,'MINOR':0,
         'unresolved_inconclusive_items':0,'scope':'same-D order2640 even-tail only',
         'excluded_scopes':['odd-|Q|','other orders','original all-order finite-completion problem'],
         'author_code_executed':False}
with RECEIPT.open('x') as f:
    json.dump(receipt,f,indent=2,sort_keys=True);f.write('\n')
print('observed_utc_before_write',clock)
print('review-v1.md',files['review-v1.md'])
print(RECEIPT.name,hashlib.sha256(RECEIPT.read_bytes()).hexdigest())
