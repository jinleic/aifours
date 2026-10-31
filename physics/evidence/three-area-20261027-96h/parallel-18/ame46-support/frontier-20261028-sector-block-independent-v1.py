#!/usr/bin/env python3
"""Independent exact I,J,X,Z block classification for the public 60-state."""
import argparse
import collections
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys


class CertificateError(ValueError): pass


def parse(path):
    raw=path.read_bytes();out={};cells=[]
    for no,line in enumerate(raw.decode('utf-8').splitlines(),1):
        if not line or line.startswith('#'):continue
        p=line.split()
        if len(p)<3 or not re.fullmatch('[0-5]',p[0]) or not re.fullmatch('[0-5]',p[1]):
            raise CertificateError(f'bad cell record {no}')
        a,b=int(p[0]),int(p[1]);cells.append((a,b))
        for t in p[2:]:
            if not re.fullmatch(r'[+\-s][0-5][0-5]',t):raise CertificateError(f'bad term {no}')
            k=(a,b,int(t[1]),int(t[2]))
            if k in out:raise CertificateError('duplicate term')
            out[k]=(0,1) if t[0]=='s' else ((1 if t[0]=='+' else -1),0)
    if cells!=list(itertools.product(range(6),repeat=2)) or len(out)!=60:
        raise CertificateError('bad source table coverage')
    return out,hashlib.sha256(raw).hexdigest()


def classify(data):
    shapes={'I':(1,0,0,1),'J':(0,1,-1,0),'X':(0,1,1,0),'Z':(1,0,0,-1)}
    groups=collections.defaultdict(dict);outside=0
    for idx,coef in data.items():
        active=tuple(i for i in range(4) if idx[i] in (1,2))
        if len(active)==0:
            outside+=1
            if coef!=(0,1):raise CertificateError('unexpected outside coefficient')
            continue
        if len(active)!=2 or coef not in ((1,0),(-1,0)):
            raise CertificateError('unexpected active sector')
        spectator=tuple(idx[i] for i in range(4) if i not in active)
        ij=tuple(idx[i]-1 for i in active)
        if ij in groups[(active,spectator)]:raise CertificateError('duplicate block entry')
        groups[(active,spectator)][ij]=coef[0]
    if outside!=12 or len(groups)!=24:raise CertificateError('bad sector count')
    bypair=collections.defaultdict(list);records=[]
    for (pair,spectator),entries in sorted(groups.items()):
        m=tuple(entries.get((i,j),0) for i in range(2) for j in range(2))
        matches=[(name,sgn) for name,base in shapes.items() for sgn in (1,-1)
                 if m==tuple(sgn*v for v in base)]
        if len(matches)!=1 or m[0]*m[3]-m[1]*m[2]==0:
            raise CertificateError('block is not signed I,J,X,Z')
        name,sgn=matches[0];bypair[pair].append(name)
        records.append({'active_pair':pair,'spectator_levels':spectator,
                        'matrix_entries':m,'type':name,'overall_sign':sgn,
                        'determinant':m[0]*m[3]-m[1]*m[2]})
    for pair in itertools.combinations(range(4),2):
        if sorted(bypair[pair])!=['I','J','X','Z']:
            raise CertificateError(f'pair type imbalance {pair}: {bypair[pair]}')
    return records


def main():
    p=argparse.ArgumentParser();p.add_argument('table',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
    data,sha=parse(a.table);records=classify(data)
    mutant=dict(data);key=(0,0,1,2);x,y=mutant[key];mutant[key]=(-x,-y)
    try:classify(mutant)
    except CertificateError as exc:
        if not str(exc).startswith('pair type imbalance'):raise
        negative=str(exc)
    else:raise CertificateError('sign-flip mutation incorrectly accepted')
    result={'table_sha256':sha,'outside_terms':12,'blocks':records,
            'active_pairs':6,'types_once_per_pair':['I','J','X','Z'],
            'sign_flip_control':negative,
            'scope':'Independent finite source-block classification; written group/rank proof separate.'}
    with a.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    json.dump({k:v for k,v in result.items() if k!='blocks'},sys.stdout,indent=2);print()


if __name__=='__main__':main()
