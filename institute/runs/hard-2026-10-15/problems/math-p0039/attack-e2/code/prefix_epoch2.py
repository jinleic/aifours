#!/usr/bin/env python3
"""Recompute 256 completed blocks using two Python workers, only after the
faster two-thread scanner has finished. No process discovery/signals are used.
Every group is <=300 s; no producing source or binary is imported/executed.
"""
import concurrent.futures
import argparse
import datetime
import json
from pathlib import Path
import subprocess
import sys
import time


def group(number):
    ids=','.join(map(str,range(32*number,32*(number+1))))
    command=[sys.executable,'code/check_epoch2.py','blocks','--task','main','--blocks',ids]
    begin=time.monotonic();run=subprocess.run(command,capture_output=True,text=True,timeout=295)
    row=dict(group=number,command=command,returncode=run.returncode,seconds=time.monotonic()-begin,
             stdout=run.stdout,stderr=run.stderr)
    Path('evidence/epoch2/prefix-groups/%02d-run.json'%number).write_text(json.dumps(row,indent=2)+'\n')
    if run.returncode:raise RuntimeError(row)
    parsed=json.loads(run.stdout)
    Path('evidence/epoch2/prefix-groups/%02d.json'%number).write_text(json.dumps(parsed,indent=2)+'\n')
    print('group',number,'PASS','%.3fs'%row['seconds'],flush=True)
    return row


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--no-pause',action='store_true')
    args=parser.parse_args()
    Path('evidence/epoch2/prefix-groups').mkdir(exist_ok=True)
    rows=[json.loads(s) for s in Path('logs/e2-main-scan128_digest.blocks.jsonl').read_text().splitlines()]
    assert rows[-1]['kind']=='footer','wait for the faster scanner before adding two workers'
    started=datetime.datetime.now(datetime.timezone.utc).isoformat();begin=time.monotonic()
    record=dict(started_utc=started,finished_scanner_threads=0,other_scanner_threads=2,python_workers=2,no_signals_sent=True)
    Path('evidence/epoch2/resource-prefix.json').write_text(json.dumps(record,indent=2)+'\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        futures=[pool.submit(group,n) for n in range(8)]
        rows=[f.result() for f in futures]
    Path('evidence/epoch2/prefix-runs.json').write_text(json.dumps(rows,indent=2)+'\n')
    record.update(finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),seconds=time.monotonic()-begin)
    Path('evidence/epoch2/resource-prefix.json').write_text(json.dumps(record,indent=2)+'\n')
    print('Prefix replay complete.',flush=True)


if __name__=='__main__':main()
