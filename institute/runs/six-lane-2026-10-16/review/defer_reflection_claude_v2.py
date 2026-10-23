import os,json,time,hashlib
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
R=Path(__file__).resolve().parent
D=R/'olson-reflection-reduction-review-v1'
target=datetime(2026,10,18,3,31,tzinfo=ZoneInfo('America/Los_Angeles')).timestamp()
time.sleep(max(0,target-time.time()))
s=os.statvfs(R);free=s.f_bavail*s.f_frsize
rec={'at':datetime.now().astimezone().isoformat(timespec='seconds'),'free_bytes':free,'required_bytes':12200000000+10485760,'reason':'v1 provider session-limit reset announced03:30 PT; one new-version attempt after03:31, no API fallback','status':'PASS' if free>=12200000000+10485760 else 'DEFERRED_RESOURCE','wrapper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
with (D/'PRE-LAUNCH-v2.json').open('x') as f:json.dump(rec,f,indent=2);f.write('\n')
print(json.dumps(rec),flush=True)
if rec['status']!='PASS':raise SystemExit(3)
os.chdir(R)
os.environ['TMPDIR']=str(D/'tmp-claude-v2')+'/'
os.execv('/usr/bin/python3',['/usr/bin/python3','-B',str(R/'run_claude_note_coop.py'),'olson-reflection-reduction-claude-v2'])
