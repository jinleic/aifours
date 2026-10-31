#!/usr/bin/env python3
"""Standard rational determinant record from ONE exact bounded multimodular
table plus a completed disjoint-prime opposite-orientation residue replay of
that SAME table. Refuses unless all pins and orientations agree."""
import argparse
import gzip
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def raw(name,sha):
    assert Path(name).name==name
    data=(ROOT/name).read_bytes();assert hashlib.sha256(data).hexdigest()==sha,name
    return data


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser()
    ap.add_argument('--exact',required=True);ap.add_argument('--exact-sha256',required=True)
    ap.add_argument('--replay',required=True);ap.add_argument('--replay-sha256',required=True)
    ap.add_argument('--output-tag',default='v1')
    args=ap.parse_args()
    R=json.loads(raw(args.exact,args.exact_sha256));V=json.loads(raw(args.replay,args.replay_sha256))
    assert R['status']=='EXACT_MULTIMODULAR_PENCIL_DETERMINANT'
    assert V['status']=='PASS_DISJOINT_PRIME_OPPOSITE_ORIENTATION_RESIDUE_REPLAY'
    assert V['verified_table']=={'file':args.exact,'sha256':args.exact_sha256} and V['pencil']==R['pencil']
    assert V['orientation']!=R['orientation'] and not set(V['disjoint_primes'])&set(R['primes'])
    serial=gzip.decompress(raw(R['coefficient_file']['file'],R['coefficient_file']['sha256']))
    assert hashlib.sha256(serial).hexdigest()==R['coefficient_file']['uncompressed_serialization_sha256']
    table={(i,j):int(c) for i,j,c in json.loads(serial)}
    a,b,n=R['degree'];m=R['dimension']
    out=ROOT/f'frontier-20261029-level{n}-{a}{b}-canonical-determinant-{args.output_tag}.json'
    if out.exists():raise FileExistsError(out)
    scale=math.prod(int(s) for s in R['row_scales'])
    record={'degree':[a,b,n],'variables':R['variables'],'pencil':R['pencil']['file'],'pencil_sha256':R['pencil']['sha256'],
            'entire_source_endomorphism':True,'size':m,
            'coefficients':[{'x_power':i,'y_power':j,'coefficient':str(Q(c,scale))} for (i,j),c in sorted(table.items())],
            'determinant_backend':'one exact bounded multimodular charpoly table plus disjoint-prime opposite-orientation residue replay',
            'multimodular_sources':[{'file':args.exact,'sha256':args.exact_sha256},{'file':args.replay,'sha256':args.replay_sha256}],
            'positive_coefficients':sum(c>0 for c in table.values()),'negative_coefficients':sum(c<0 for c in table.values()),
            'constant_coefficient':str(Q(table.get((0,0),0),scale)),
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'status':'CERTIFIED_WHOLE_CLOSED_QUADRANT_CANONICAL_NONZERO' if table.get((0,0),0) and (all(c>0 for c in table.values()) or all(c<0 for c in table.values())) else 'MIXED_OR_ZERO_CANONICAL_MINOR_NO_GLOBAL_VERDICT',
            'scope':'entire canonical primitive endomorphism determinant in x=r-7,y=s-7; pencil, D3-kernel containment and actual quotient transport are separate obligations'}
    with out.open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
    print('WROTE',out.name,'terms',len(table),record['status'],flush=True)


if __name__=='__main__':main()
