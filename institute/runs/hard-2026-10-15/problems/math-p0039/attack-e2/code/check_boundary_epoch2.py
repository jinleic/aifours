#!/usr/bin/env python3
"""Python-only complete replay of the two blocks around the stage join.
No producing code or local executable is imported/executed. Factor records
have exact proper factors; every unsieved member has a full ordinary power.
This is a separated window, never a continuation of the small exact prefix.
"""
import argparse
import gzip
import json
from pathlib import Path
import subprocess
import sys
import time


def need(ok,message):
    if not ok:raise ValueError(message)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--produce',action='store_true')
    parser.add_argument('--broken',action='store_true');args=parser.parse_args()
    path=Path('evidence/epoch2/boundary-window.json');begin=time.monotonic()
    fixed=dict(start=1999859732480,middle=2000000000000,stop=2000201326592,step=24,count=14233088)
    stored=dict(fixed) if args.produce else json.loads(path.read_text())
    if args.broken:stored['middle']+=24
    need(all(stored[k]==v for k,v in fixed.items()),'boundary endpoint/count mismatch')
    if not args.produce:
        need(stored['base_two_survivors']==[] and stored['middle_proper_factor']==7,'stored boundary witness')
    results=[]
    for task,block in (('main',8940),('extension',0)):
        command=[sys.executable,'code/check_epoch2.py','blocks','--task',task,'--blocks',str(block)]
        run=subprocess.run(command,capture_output=True,text=True,timeout=110)
        need(run.returncode==0,'boundary arithmetic replay failed: '+run.stderr)
        result=json.loads(run.stdout)
        need(result['base_two_survivors']==[] and len(result['blocks'])==1,'boundary survivor/block count')
        results.append(result['blocks'][0])
    left,right=results
    need(left['start']==fixed['start'] and left['end']==right['start']==fixed['middle']
         and right['end']==fixed['stop'],'boundary gap or overlap')
    need(left['count']+right['count']==fixed['count'],'boundary arithmetic-class count')
    p=fixed['middle']**2+fixed['middle']+1;residue=pow(2,fixed['middle']+1,p)
    need(1<7<p and p%7==0,'middle proper-factor witness')
    for exe in ('scan128_digest','scan32'):
        source=Path('logs/e2-extension-'+exe+'.records.jsonl')
        if Path(str(source)+'.gz').exists():
            with gzip.open(str(source)+'.gz','rt') as stream:row=json.loads(next(stream))
        else:
            with source.open() as stream:row=json.loads(next(stream))
        need(row['n']==fixed['middle'] and int(row['p'])==p and row['factor']==7
             and int(row['residue'])==residue,'middle full residue/actual factor mismatch')
    result=dict(fixed,block_results=results,middle_modulus=str(p),middle_proper_factor=7,
                middle_full_base_two_residue=str(residue),base_two_survivors=[],
                seconds=time.monotonic()-begin,
                limitation='This separated 14233088-member window does not enlarge the contiguous prefix.')
    if args.produce:path.write_text(json.dumps(result,indent=2)+'\n')
    else:
        need(stored['block_results']==result['block_results'],'boundary complete-decision hashes differ')
        need(stored['middle_modulus']==result['middle_modulus'] and
             stored['middle_full_base_two_residue']==result['middle_full_base_two_residue'],
             'stored middle witness differs')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    try:main()
    except (ValueError,AssertionError,KeyError,IndexError) as error:
        print('CHECK FAILED: '+str(error),file=sys.stderr);sys.exit(1)
