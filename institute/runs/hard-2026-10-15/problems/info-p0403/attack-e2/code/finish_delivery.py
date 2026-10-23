"""Finalize only after every claim command and control has actually passed."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess


claims=json.loads(Path('claims.json').read_text())
path=Path('results/final-verification.json')
result=json.loads(path.read_text())
assert result['status']=='PASS' and all(r['passed'] for r in result['commands'])
assert result['claims_sha256']==hashlib.sha256(Path('claims.json').read_bytes()).hexdigest()
expected=[(c['cid'],field,c[field]) for c in claims['claims'] for field in ('verify_command','check_command','control_command') if c[field]]
assert expected==[(r['cid'],r['field'],r['command']) for r in result['commands']]
subprocess.run(['python3','code/validate_claims.py'],check=True)
subprocess.run(['python3','code/check_syntax.py'],check=True)
result['schema_validation_passed']=True
result['syntax_check_passed']=True
result['completed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
temp=Path('results/final-verification.json.tmp'); temp.write_text(json.dumps(result,indent=2)+'\n'); temp.replace(path)
subprocess.run(['python3','code/write_report.py'],check=True)
final={'outcome':claims['outcome'],'headline_question_resolved':False,'claim_count':len(claims['claims']),'commands_passed':len(result['commands']),'negative_controls_rejected':sum(r['expected_nonzero'] for r in result['commands']),'completed_utc':result['completed_utc'],'claims_sha256':hashlib.sha256(Path('claims.json').read_bytes()).hexdigest(),'report_sha256':hashlib.sha256(Path('REPORT.md').read_bytes()).hexdigest(),'final_verification_status':'PASS'}
Path('results/delivery.json').write_text(json.dumps(final,indent=2)+'\n')
print(json.dumps(final,sort_keys=True))
