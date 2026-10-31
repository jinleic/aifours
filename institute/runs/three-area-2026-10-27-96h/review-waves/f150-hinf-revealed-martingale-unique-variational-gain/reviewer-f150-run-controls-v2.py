#!/usr/bin/env python3
"""Exclusive-creation runner for the independent f150 control, not author code."""
from pathlib import Path
import hashlib, json, subprocess, sys

root=Path(__file__).resolve().parent
control=root/'reviewer-f150-independent-controls-v2.py'
log=root/'reviewer-f150-independent-controls-v2.log'
receipt=root/'reviewer-f150-run-receipt-v2.json'
for p in (log,receipt):
    if p.exists(): raise SystemExit('Refuse overwrite: '+str(p))

def meta(p):
    b=Path(p).read_bytes()
    return {'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'LF':b.count(b'\n'),'CR':b.count(b'\r')}

def clock():
    return subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()

m1=root/'manifest-v1.json'; m2=root/'manifest-v2.json'
assert meta(m1)['sha256']=='af53e4c3bc55b46b90186b15293e57cfd2404bd0875532bd9fb7eecff0a62221'
assert meta(m2)['sha256']=='04b3e2fd0f81456070c150e5ca358c126bc9b758bf267cb2901bd7d8bed9730c'
j1=json.loads(m1.read_text()); j2=json.loads(m2.read_text())
assert j1['inputs_in_read_order']==j2['inputs_in_read_order']
inputs=[]
for item in j1['inputs_in_read_order']+j2['optional_alternative_inputs']:
    got=meta(item['path'])
    for k in ('sha256','bytes','LF'): assert got[k]==item[k], (k,got,item)
    assert got['CR']==0
    inputs.append(got)
start=clock()
p=subprocess.run([sys.executable,'-u',str(control)],cwd=root,capture_output=True,text=True,stdin=subprocess.DEVNULL)
end=clock()
with log.open('x') as f:
    f.write('Native clock immediately before child: '+start+'\n')
    f.write(p.stdout)
    if p.stderr: f.write('\nSTDERR:\n'+p.stderr)
    f.write('\nActual child returncode: '+str(p.returncode)+'\nNative clock after child: '+end+'\n')
observed=clock()
body={'kind':'INDEPENDENT_SAME_HARNESS_REVIEWER_EXACT_CONTROL_RECEIPT',
      'observed_native_clock_before_receipt_write':observed,
      'child_start':start,'child_end':end,'returncode':p.returncode,
      'prior_run':meta(root/'reviewer-f150-run-receipt-v1.json'),
      'reviewer_correction':meta(root/'reviewer-f150-control-correction-v2.py'),
      'correction_reason':'v1 erroneously demanded F(nu_e)>c at e=.1; candidate claims only sufficiently small e. v2 retains the chain at .1 and treats F<c there as a negative control.',
      'command':[sys.executable,'-u',str(control)],
      'manifests':[meta(m1),meta(m2)],'inputs_verified':inputs,
      'reviewer_original_assessment':meta(root/'reviewer-f150-original-assessment-v1.txt'),
      'control':meta(control),'runner':meta(Path(__file__).resolve()),'log':meta(log),
      'no_author_code_executed_or_imported':True,
      'optional_control_method':'Fixed projective mesh right-Darboux sum, rational/integer rounded-down contributions. Not author adaptive checker.',
      'scope':'Exact controls are finite checks; analytic theorem independently reconstructed in review-v1.md. mpmath numerical results diagnostic only; no optimum kappa computed.'}
with receipt.open('x') as f: json.dump(body,f,indent=2);f.write('\n')
print(p.stdout)
if p.stderr: print(p.stderr,file=sys.stderr)
print('RECEIPT',str(receipt),'CHILD_RETURN_CODE',p.returncode)
raise SystemExit(p.returncode)
