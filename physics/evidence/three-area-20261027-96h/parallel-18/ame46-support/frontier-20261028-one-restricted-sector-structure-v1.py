#!/usr/bin/env python3
"""Certify P-complement matching and Pauli sectors for all ordered (C,B)."""
import argparse
import collections
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys

H=(1,2); K=(0,3,4,5)
SHAPES={'I':(1,0,0,1),'J':(0,1,-1,0),'X':(0,1,1,0),'Z':(1,0,0,-1)}


class CertificateError(ValueError):pass


def parse(path):
    raw=path.read_bytes();data={};cells=[]
    for line in raw.decode('utf-8').splitlines():
        if not line or line.startswith('#'):continue
        v=line.split()
        if len(v)<3 or not all(re.fullmatch('[0-5]',x) for x in v[:2]):raise CertificateError('bad cell')
        a,b=map(int,v[:2]);cells.append((a,b))
        for token in v[2:]:
            if not re.fullmatch(r'[+\-s][0-5][0-5]',token):raise CertificateError('bad term')
            key=(a,b,int(token[1]),int(token[2]))
            if key in data:raise CertificateError('duplicate')
            data[key]=(0,1) if token[0]=='s' else (1 if token[0]=='+' else -1,0)
    if cells!=list(itertools.product(range(6),repeat=2)) or len(data)!=60:raise CertificateError('bad table')
    return data,hashlib.sha256(raw).hexdigest()


def eblocks(data,active):
    active=tuple(sorted(active));spectators=tuple(j for j in range(4) if j not in active)
    groups=collections.defaultdict(dict)
    for x,(r,s) in data.items():
        actual=tuple(j for j in range(4) if x[j] in H)
        if actual!=active:continue
        if s or r not in (-1,1):raise CertificateError('unexpected E coefficient')
        fixed=tuple(x[j] for j in spectators);cell=tuple(x[j]-1 for j in active)
        if cell in groups[fixed]:raise CertificateError('duplicate active block')
        groups[fixed][cell]=r
    if len(groups)!=4 or len({a for a,b in groups})!=4 or len({b for a,b in groups})!=4:
        raise CertificateError('spectator matching fails')
    types=[];details=[]
    for fixed,mat in sorted(groups.items()):
        flat=tuple(mat.get((r,c),0) for r in range(2) for c in range(2))
        hits=[(name,sign) for name,v in SHAPES.items() for sign in (-1,1) if flat==tuple(sign*q for q in v)]
        if len(hits)!=1:raise CertificateError('not signed Pauli block')
        types.append(hits[0][0]);details.append({'spectator_levels':fixed,'matrix':flat,'type':hits[0][0]})
    if sorted(types)!=['I','J','X','Z']:raise CertificateError('Pauli types incomplete')
    return spectators,details


def certify(data):
    p=[x for x in data if all(x[j] not in H for j in range(4))]
    if len(p)!=12 or any(data[x]!=(0,1) for x in p):raise CertificateError('P sector invalid')
    if any(sum(x[j] in H for j in range(4)) not in (0,2) for x in data):raise CertificateError('unexpected sector')
    records=[]
    for c in range(4):
        for b in range(4):
            if c==b:continue
            a,d=tuple(j for j in range(4) if j not in (c,b))
            rows=[(x[c],x[b]) for x in p];cols=[(x[a],x[d]) for x in p]
            if len(set(rows))!=12 or len(set(cols))!=12:raise CertificateError('P flattened matching fails')
            missing=set(itertools.product(K,repeat=2))-set(rows)
            spectator,blocks=eblocks(data,(a,d))
            matching={(x['spectator_levels'][spectator.index(c)],x['spectator_levels'][spectator.index(b)]) for x in blocks}
            if matching!=missing:raise CertificateError('P complement does not equal E matching')
            # Check all three C-active/free-pair sectors and their spectator matchings.
            other=[]
            for j in (a,b,d):
                sp,bl=eblocks(data,(c,j))
                other.append({'active_pair':tuple(sorted((c,j))),'spectator_axes':sp,'blocks':bl})
            records.append({'restricted_C':c,'contracted_B':b,'remaining_A_D':(a,d),
                            'P_flattening_rank':12,'P_missing_pairs':sorted(missing),
                            'matched_E_AD_blocks':blocks,'C_active_E_blocks':other})
    return records


def main():
    p=argparse.ArgumentParser();p.add_argument('table',type=Path);p.add_argument('out',type=Path);a=p.parse_args()
    data,sha=parse(a.table);records=certify(data)
    mutant=dict(data);del mutant[(0,0,1,2)]
    try:certify(mutant)
    except CertificateError as exc:negative=str(exc)
    else:raise CertificateError('deleted coefficient mutation accepted')
    result={'table_sha256':sha,'ordered_restricted_contracted_choices':len(records),
            'P_complement_matching_all':'PASS','Pauli_types_per_E_pair_all':'PASS',
            'cases':records,'deleted_E_coefficient_control':negative,
            'scope':'Exact finite source structure; uniform-complex rank argument is in the written proof.'}
    with a.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    json.dump({k:v for k,v in result.items() if k!='cases'},sys.stdout,indent=2);print()


if __name__=='__main__':main()
