#!/usr/bin/env python3
"""Append exact support/sign assignments from the published Pandya tensor.

Purpose: positive-control a candidate CNF encoding, not discover a new witness.
Relabel H={1,2} to {0,1}, K={0,3,4,5} to {2,3,4,5}; choose one published P word
and map each of its local K symbols to 2 so the optional p2222 symmetry fits.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path


def main():
    ap=argparse.ArgumentParser();ap.add_argument('cnf',type=Path);ap.add_argument('table',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    if a.out.exists():raise SystemExit('output exists')
    coeff={}
    for line in a.table.read_text().splitlines():
        if not line or line.startswith('#'):continue
        x,y,*ts=line.split()
        for t in ts:coeff[(int(x),int(y),int(t[1]),int(t[2]))]=t[0]
    if len(coeff)!=60:raise ValueError('source support')
    first=sorted(q for q,v in coeff.items() if v=='s')[0]
    maps=[]
    for j in range(4):
        d={1:0,2:1,first[j]:2}
        for k,v in zip([x for x in (0,3,4,5) if x!=first[j]],(3,4,5)):d[k]=v
        maps.append(d)
    image={tuple(maps[i][q[i]] for i in range(4)):v for q,v in coeff.items()}
    if image.get((2,2,2,2))!='s':raise ValueError('fixed P not mapped')
    assignment=[]
    for idx,q in enumerate(itertools.product(range(6),repeat=4)):
        c=image.get(q)
        assignment.extend([1+idx if c in ('+','-') else -(1+idx),
                           1297+idx if c=='s' else -(1297+idx),
                           2593+idx if c=='-' else -(2593+idx)])
    h=hashlib.sha256()
    with a.cnf.open('rb') as src,a.out.open('xb') as dst:
        header=src.readline();tag,fmt,nv,nc=header.decode().split()
        if (tag,fmt)!=('p','cnf'):raise ValueError('bad header')
        new=f'p cnf {nv} {int(nc)+len(assignment)}\n'.encode();dst.write(new);h.update(new)
        for chunk in iter(lambda:src.read(1024*1024),b''):dst.write(chunk);h.update(chunk)
        for lit in assignment:
            b=f'{lit} 0\n'.encode();dst.write(b);h.update(b)
    meta={'source_table_sha256':hashlib.sha256(a.table.read_bytes()).hexdigest(),
      'base_cnf_sha256':hashlib.sha256(a.cnf.read_bytes()).hexdigest(),'assigned_cnf_sha256':h.hexdigest(),
      'unit_assignments':len(assignment),'first_P_word':first,'local_relabelings':maps,
      'scope':'Encoding positive control only; witness itself is published source material.'}
    with Path(str(a.out)+'.meta.json').open('x',encoding='utf-8') as f:json.dump(meta,f,indent=2);f.write('\n')
    print(json.dumps(meta,indent=2))


if __name__=='__main__':main()
