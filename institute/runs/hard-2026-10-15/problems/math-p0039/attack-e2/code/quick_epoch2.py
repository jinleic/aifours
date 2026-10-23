#!/usr/bin/env python3
"""Sequential small checks with explicit expected failures; one CPU at a time."""
import json
from pathlib import Path
import subprocess
import sys
import time


def main():
    jobs=[(['vectors'],0),(['vectors','--broken'],1),
          (['compare','--task','tiny'],0),(['compare','--task','tiny','--broken'],1),
          (['blocks','--task','tiny','--blocks','0'],0),
          (['blocks','--task','tiny','--blocks','0','--broken'],1),
          (['samples','--task','tiny'],0),(['samples','--task','tiny','--broken'],1),
          (['compare','--task','benchmark'],0),
          (['blocks','--task','benchmark','--blocks','0','--backend','manual'],0)]
    results=[]
    for args,expected in jobs:
        command=[sys.executable,'code/check_epoch2.py']+args;begin=time.monotonic()
        run=subprocess.run(command,capture_output=True,text=True,timeout=290)
        passed=run.returncode==0 if expected==0 else run.returncode!=0
        row=dict(command=command,expected='success' if expected==0 else 'nonzero failure',
                 returncode=run.returncode,passed=passed,seconds=time.monotonic()-begin,
                 stdout=run.stdout,stderr=run.stderr)
        results.append(row);print(args,run.returncode,row['seconds'],flush=True)
        Path('evidence/epoch2/quick-checks.json').write_text(json.dumps(results,indent=2)+'\n')
        if not passed:raise SystemExit(1)


if __name__=='__main__':main()
