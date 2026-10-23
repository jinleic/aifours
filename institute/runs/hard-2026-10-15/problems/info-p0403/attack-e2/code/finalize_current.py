"""Finalize after a real limited-copy replay, preserving all load evidence."""
import datetime
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
from delivery_replay import visible_files


root=Path.cwd()
claims=json.loads(Path('claims.json').read_text())
replay=json.loads(Path('results/delivery-replay.json').read_text())
assert claims['outcome']=='partial' and replay['status']=='PASS'
assert replay['claims_sha256']==hashlib.sha256(Path('claims.json').read_bytes()).hexdigest()
expected=[(c['cid'],field,c[field]) for c in claims['claims'] for field in
          ('verify_command','check_command','control_command') if c[field]]
assert expected==[(r['cid'],r['field'],r['command']) for r in replay['commands']]
assert all(r['passed'] and r['seconds']<300 for r in replay['commands'])
assert replay['seconds']<1800
evidence={name for c in claims['claims'] for name in c['evidence']}
for name in evidence:
    path=Path(name)
    assert path.is_file() and path.stat().st_size<=5000000
    assert path.read_bytes()==(Path('.delivery-replay')/name).read_bytes(),('changed tested evidence',name)
subprocess.run(['python3','code/validate_claims.py'],check=True)
subprocess.run(['python3','code/check_syntax.py'],check=True)
now=datetime.datetime.now(datetime.timezone.utc)
start=datetime.datetime(2026,10,15,21,23,54,tzinfo=datetime.timezone.utc)
deadline=start+datetime.timedelta(minutes=141)
assert now<deadline
summary={'outcome':'partial','headline_question_resolved':False,'claim_count':len(claims['claims']),
         'claims_sha256':replay['claims_sha256'],'limited_copy_replay_status':'PASS',
         'commands_passed':len(replay['commands']),
         'intentional_negative_controls_rejected':sum(r['expected_nonzero'] for r in replay['commands']),
         'aggregate_replay_seconds':replay['seconds'],
         'longest_command_seconds':max(r['seconds'] for r in replay['commands']),
         'tested_copy_bytes':replay['snapshot_bytes'],'tested_copy_skipped_files':replay['skipped'],
         'all_claimed_evidence_unchanged_since_test':True,'all_claimed_evidence_preserved':True,
         'completed_utc':now.isoformat(),'elapsed_minutes':(now-start).total_seconds()/60,
         'delivery_ready_before_minute141':True,'novelty':'unknown',
         'gap':'No balanced 512-bit NL>=242 witness and no global nonexistence proof.'}
Path('results/final-delivery.json').write_text(json.dumps(summary,indent=2)+'\n')
# Preserve the tested manifest before describing the smaller final delivery.
old=Path('results/delivery-manifest.json')
tested=Path('results/tested-snapshot-manifest.json')
if not tested.exists():
    shutil.copyfile(old,tested)
Path('SKIPPED.json').write_text('[]\n')
files=[]
for path in visible_files(root):
    relative=path.relative_to(root).as_posix()
    if relative=='results/delivery-manifest.json':
        continue
    raw=path.read_bytes()
    assert len(raw)<=5000000,('oversize final file',relative,len(raw))
    files.append({'path':relative,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
                  'claimed_evidence':relative in evidence})
manifest={'scope':'Final visible delivery; manifest itself omitted from its checksum list to avoid self-reference.',
          'files_excluding_manifest':len(files),'bytes_excluding_manifest':sum(r['bytes'] for r in files),
          'largest_file_bytes':max(r['bytes'] for r in files),'claimed_evidence_files':len(evidence),
          'claimed_evidence_all_included':True,'skipped':[],'files':files}
old.write_text(json.dumps(manifest,indent=2)+'\n')
actual=visible_files(root)
total=sum(p.stat().st_size for p in actual)
assert len(actual)<=2000 and total<50000000
assert all(p.stat().st_size<=5000000 for p in actual)
assert not list(Path('results').glob('*.cnf')),'temporary solver input remains'
print(json.dumps({'status':'READY','visible_files':len(actual),'bytes':total,
                  'largest_file':max(p.stat().st_size for p in actual),
                  'claims':len(claims['claims']),'tested_commands':len(replay['commands']),
                  'completed_utc':now.isoformat()},sort_keys=True))
