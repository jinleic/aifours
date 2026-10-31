#!/usr/bin/env python3
"""Verify the 48 source structural zeros needed to repair mixed contraction rank."""
import argparse
import importlib.util
import itertools
import json
from pathlib import Path
import sys

H=(1,2);K=(0,3,4,5)


class CertificateError(ValueError):pass


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def active_pair(q):return tuple(j for j in range(4) if q[j] in H)


def one_spectator_value(tensor,active,fixed_axis,fixed_value,other_axis):
    values={q[other_axis] for q in tensor if active_pair(q)==tuple(sorted(active)) and q[fixed_axis]==fixed_value}
    if len(values)!=1:raise CertificateError('spectator map not unique')
    return next(iter(values))


def certify(tensor):
    p=[q for q in tensor if not active_pair(q)]
    records=[]
    for c in range(4):
        for b in range(4):
            if c==b:continue
            a,d=tuple(j for j in range(4) if j not in (c,b))
            checks=[]
            for level in K:
                dval=one_spectator_value(tensor,(a,b),c,level,d)
                aval=one_spectator_value(tensor,(b,d),c,level,a)
                if any(q[a]==aval and q[d]==dval for q in p):
                    raise CertificateError('structural P zero violated')
                matching={(q[a],q[d]) for q in tensor if active_pair(q)==tuple(sorted((b,c)))}
                if (aval,dval) not in matching:raise CertificateError('cross-sector matching missing')
                checks.append({'C_level':level,'A_K_row':aval,'D_K_column':dval,'P_entry':'zero'})
            records.append({'C':c,'B':b,'A':a,'D':d,'checks':checks})
    if len(p)!=12:raise CertificateError('P count mismatch')
    if len(records)!=12 or sum(len(x['checks']) for x in records)!=48:
        raise CertificateError('orientation coverage mismatch')
    return records


def main():
    p=argparse.ArgumentParser();p.add_argument('table',type=Path);p.add_argument('parser',type=Path);p.add_argument('out',type=Path);args=p.parse_args()
    parser=load('structure',args.parser);tensor,sha=parser.parse(args.table)
    records=certify(tensor)
    # Insert a coefficient precisely at a certified structural-zero P location.
    first=records[0];check=first['checks'][0];coord=[0]*4
    coord[first['C']]=check['C_level'];coord[first['B']]=K[0]
    coord[first['A']]=check['A_K_row'];coord[first['D']]=check['D_K_column']
    mutation=dict(tensor);mutation[tuple(coord)]=(0,1)
    try:certify(mutation)
    except CertificateError as exc:
        if str(exc)!='structural P zero violated':raise
        negative=str(exc)
    else:raise CertificateError('structural-zero mutation incorrectly accepted')
    result={'table_sha256':sha,'ordered_C_B_choices':12,'checked_structural_zero_locations':48,
            'records':records,'inserted_P_coefficient_control':negative,
            'scope':'Finite source-pattern certificate; complex rank implication must be proved separately.'}
    with args.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    json.dump({k:v for k,v in result.items() if k!='records'},sys.stdout,indent=2);print()


if __name__=='__main__':main()
