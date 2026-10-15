#!/usr/bin/env python3
"""Run the remaining degree-222 parameter cells in one process at a time.

Existing successful cell files are preserved and not recomputed. Every failure
or timeout is recorded; no skipped cell is called proved. Run inside the same
isolated SymPy environment as interior_minor.py.
"""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds-per-cell', type=int, default=180)
    args=parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    records=[]
    start=time.monotonic()
    with (args.output/'remaining-cells.log').open('w') as log:
        for mask in range(1,64):
            cell=args.output/f'mask-{mask}.json.gz'
            if cell.exists():
                records.append({'mask':mask,'execution':'preserved-existing-output'})
                continue
            command=[sys.executable,'work/interior_minor.py','--mask',str(mask),'--output',str(args.output)]
            begin=time.monotonic()
            try:
                done=subprocess.run(command,stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,timeout=args.seconds_per_cell)
                record={'mask':mask,'exit_code':done.returncode,'seconds':round(time.monotonic()-begin,3),'output_exists':cell.exists()}
            except subprocess.TimeoutExpired:
                record={'mask':mask,'execution':'timeout','seconds':args.seconds_per_cell,'output_exists':cell.exists()}
            records.append(record)
            print(json.dumps(record),flush=True)
            (args.output/'remaining-cells-run.json').write_text(json.dumps({'records':records,'complete_mask_range':False},indent=2))
    (args.output/'remaining-cells-run.json').write_text(json.dumps({'records':records,'complete_mask_range':len(records)==63,'elapsed_seconds':round(time.monotonic()-start,3),'processes_at_a_time':1},indent=2))


if __name__=='__main__':
    main()
