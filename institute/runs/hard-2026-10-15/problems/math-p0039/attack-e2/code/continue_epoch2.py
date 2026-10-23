#!/usr/bin/env python3
"""Bound the optional second production stage by the frozen delivery deadline.
This is a foreground continuation of the current task, not a scheduled revisit.
Two scanner CPU threads leave room for exact arithmetic checks. All final claim
commands remain Python-only and never invoke this production orchestrator.
"""
import datetime
import json
from pathlib import Path
import subprocess
import sys


def main():
    p=Path('evidence/epoch2')
    result=json.loads((p/'main-comparison.json').read_text())
    assert result['end']==2000000000000 and result['hits']==[]
    session=json.loads((p/'session.json').read_text())
    deadline=datetime.datetime.fromisoformat(session['deliver_utc'])
    now=datetime.datetime.now(datetime.timezone.utc)
    remaining=int((deadline-now).total_seconds())
    first_stage=max(json.loads((p/('main-'+exe+'-run.json')).read_text())['seconds']
                    for exe in ('scan128_digest','scan32'))
    cap=min(2700,remaining-1800-600,int(9000-first_stage))
    command=[sys.executable,'code/run_epoch2.py','extension','--cap',str(cap)]
    plan=dict(started_utc=now.isoformat(),deliver_utc=deadline.isoformat(),
              remaining_seconds=remaining,first_stage_seconds=first_stage,
              replay_reserve_seconds=1800,final_margin_seconds=600,
              cap_seconds=cap,command=command,scanner_threads=2,
              note='Only the last common complete block boundary may become a reported endpoint.')
    (p/'extension-plan.json').write_text(json.dumps(plan,indent=2)+'\n')
    if cap<60:
        print('No extension: preserve the replay/delivery reserve.');return
    print(json.dumps(plan,indent=2),flush=True)
    subprocess.run(command,check=True,timeout=cap+150)


if __name__=='__main__':main()
