#!/usr/bin/env python3
"""One-shot bounded runner; writes immutable per-mode stdout/stderr and receipt."""
import hashlib
import json
import pathlib
import subprocess
import sys
import time

ROOT=pathlib.Path(__file__).resolve().parent
MANIFEST=ROOT/'manifest-v1.json'
SCRIPT=ROOT/'reviewer-exact-controls-v1.py'
EXPECTED='6c6db7ff3b1e8da7b6eb50ba07dc54329a6bf8e92829886e7b8cf0810e9d9700'


def digest(path):
    b=path.read_bytes()
    return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'LF':b.count(b'\n')}


def date():
    return subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()


def exclusive(path,data):
    with path.open('xb') as f:
        f.write(data)


def main():
    manifest_pin=digest(MANIFEST)
    if manifest_pin['sha256']!=EXPECTED:
        raise SystemExit('manifest hash mismatch')
    manifest=json.loads(MANIFEST.read_bytes())
    context=[]
    for item in manifest['inputs_in_read_order']:
        actual=digest(pathlib.Path(item['path']))
        expected={'sha256':item['sha256'],'bytes':item['bytes'],'LF':item['LF']}
        if actual!=expected:
            raise SystemExit('input pin mismatch: '+item['path'])
        context.append({'path':item['path'],**actual})
    script_pin=digest(SCRIPT)
    runner_pin=digest(pathlib.Path(__file__).resolve())
    modes=['positive','wrong-minus-sign','cyclotomic-nonprimitive','item11-missing-factor',
           'item11-f4-valuation-one','repeated-unit','symplectic-factor-two']
    receipts=[]
    for mode in modes:
        before=date()
        t0=time.monotonic()
        command=[sys.executable,'-B',str(SCRIPT),mode]
        try:
            proc=subprocess.run(command,capture_output=True,timeout=90,check=False)
            outcome='COMPLETED'
            rc=proc.returncode
            stdout,stderr=proc.stdout,proc.stderr
        except subprocess.TimeoutExpired as e:
            outcome='UNKNOWN_TIMEOUT'
            rc=None
            stdout=e.stdout or b''
            stderr=e.stderr or b''
        elapsed=time.monotonic()-t0
        after=date()
        op=ROOT/('reviewer-control-'+mode+'-stdout-v1.json')
        ep=ROOT/('reviewer-control-'+mode+'-stderr-v1.txt')
        exclusive(op,stdout); exclusive(ep,stderr)
        expected_rc=0 if mode=='positive' else 1
        expected_status='PASS' if mode=='positive' else 'REJECT_EXPECTED_MUTATION'
        try:
            parsed=json.loads(stdout)
            actual_status=parsed.get('status')
            reason=parsed.get('reason')
        except (ValueError,AttributeError):
            actual_status=None; reason=None
        valid=(outcome=='COMPLETED' and rc==expected_rc and actual_status==expected_status)
        receipts.append({'mode':mode,'actual_command':command,'clock_before':before,'clock_after':after,
                         'elapsed_seconds':elapsed,'timeout_seconds':90,'outcome':outcome,'exit_code':rc,
                         'expected_exit_code':expected_rc,'expected_status':expected_status,'status':actual_status,
                         'reason':reason,'match':valid,'stdout':{'path':str(op),**digest(op)},
                         'stderr':{'path':str(ep),**digest(ep)}})
    payload={'clock_before_receipt':date(),'nature':'reviewer-authored diagnostic only; finite checks are not proof',
             'run_context_manifest':manifest_pin,'run_context_inputs':context,'script':{'path':str(SCRIPT),**script_pin},
             'runner':{'path':str(pathlib.Path(__file__).resolve()),**runner_pin},
             'script_inputs':'mode argument and literal control constants; source inputs are context pins, not program inputs',
             'per_run_timeout_seconds':90,'runs':receipts,'all_expected_outcomes':all(x['match'] for x in receipts)}
    dest=ROOT/'reviewer-control-receipt-v1.json'
    exclusive(dest,(json.dumps(payload,indent=2,sort_keys=True)+'\n').encode())
    print(json.dumps({'receipt':str(dest),'receipt_sha256':digest(dest)['sha256'],
                      'all_expected_outcomes':payload['all_expected_outcomes'],
                      'runs':[{'mode':r['mode'],'outcome':r['outcome'],'exit':r['exit_code'],'match':r['match']} for r in receipts]},indent=2))
    return 0 if payload['all_expected_outcomes'] else 1


if __name__=='__main__':
    raise SystemExit(main())
