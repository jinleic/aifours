#!/usr/bin/env python3
"""Read complete live log lines; report only a common consecutive prefix.
This audits preserved block digests/structure, never individual arithmetic.
No completion footer is invented or written into the production logs.
"""
import argparse
import json
from pathlib import Path


def rows(path):
    text=Path(path).read_text()
    return [json.loads(s) for s in text.splitlines(keepends=True) if s.endswith('\n')]


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--task',default='main');args=parser.parse_args()
    sets=[]
    for exe in ('scan128_digest','scan32'):
        data=rows('logs/e2-'+args.task+'-'+exe+'.blocks.jsonl')
        h=data[0];b={x['id']:x for x in data[1:] if x['kind']=='block'}
        sets.append((h,b))
    size=sets[0][0]['block_size'];start=sets[0][0]['start'];step=sets[0][0]['step']
    common=[];i=0
    keys=('id','index','start','end','count','sieved','tested','hits','survivors','decision_sha256')
    while all(i in x[1] for x in sets):
        a,b=(x[1][i] for x in sets)
        assert all(a[k]==b[k] for k in keys), 'different block digest at '+str(i)
        assert a['index']==i*size and a['start']==start+step*i*size
        assert a['end']==a['start']+step*a['count'] and a['sieved']+a['tested']==a['count']
        common.append(a);i+=1
    out=dict(task=args.task,observed_blocks=[len(x[1]) for x in sets],common_blocks=i,
             common_end=common[-1]['end'] if common else start,
             common_members=sum(x['count'] for x in common),
             logged_common_survivors=[n for x in common for n in x['survivors']],
             limitation='Live common digest/structure prefix only; not a completed plan or Python arithmetic certification.')
    Path('evidence/epoch2/live-'+args.task+'.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
