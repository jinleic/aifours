#!/usr/bin/env python3
"""Write the standard rational determinant record from TWO agreeing exact
multimodular computations (different prime sets and opposite charpoly
orientations). Refuses unless both integer tables are identical."""
import argparse
import gzip
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def load(name,sha):
    assert Path(name).name==name
    raw=(ROOT/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
    R=json.loads(raw)
    craw=(ROOT/R['coefficient_file']['file']).read_bytes()
    assert hashlib.sha256(craw).hexdigest()==R['coefficient_file']['sha256']
    serial=gzip.decompress(craw)
    assert hashlib.sha256(serial).hexdigest()==R['coefficient_file']['uncompressed_serialization_sha256']
    return R,{(i,j):int(c) for i,j,c in json.loads(serial)}


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser()
    ap.add_argument('--first',required=True);ap.add_argument('--first-sha256',required=True)
    ap.add_argument('--second',required=True);ap.add_argument('--second-sha256',required=True)
    args=ap.parse_args()
    R1,C1=load(args.first,args.first_sha256);R2,C2=load(args.second,args.second_sha256)
    assert R1['pencil']==R2['pencil'] and R1['degree']==R2['degree'] and R1['row_scales']==R2['row_scales']
    assert R1['orientation']!=R2['orientation'] and not set(R1['primes'])&set(R2['primes'])
    assert C1==C2,'independent multimodular determinant tables differ'
    a,b,n=R1['degree'];m=R1['dimension']
    out=ROOT/f'frontier-20261029-level{n}-{a}{b}-canonical-determinant-v1.json'
    if out.exists():raise FileExistsError(out)
    scale=math.prod(int(s) for s in R1['row_scales'])
    coefficients=[{'x_power':i,'y_power':j,'coefficient':str(Q(c,scale))} for (i,j),c in sorted(C1.items())]
    record={'degree':[a,b,n],'variables':R1['variables'],'pencil':R1['pencil']['file'],'pencil_sha256':R1['pencil']['sha256'],
            'entire_source_endomorphism':True,'size':m,'coefficients':coefficients,
            'determinant_backend':'two exact multimodular charpoly computations, disjoint prime sets and opposite orientations, identical integer tables',
            'multimodular_sources':[{'file':args.first,'sha256':args.first_sha256},{'file':args.second,'sha256':args.second_sha256}],
            'positive_coefficients':sum(c>0 for c in C1.values()),'negative_coefficients':sum(c<0 for c in C1.values()),
            'constant_coefficient':str(Q(C1.get((0,0),0),scale)),
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'status':'CERTIFIED_WHOLE_CLOSED_QUADRANT_CANONICAL_NONZERO' if C1.get((0,0),0) and (all(c>0 for c in C1.values()) or all(c<0 for c in C1.values())) else 'MIXED_OR_ZERO_CANONICAL_MINOR_NO_GLOBAL_VERDICT',
            'scope':'entire canonical primitive endomorphism determinant in x=r-7,y=s-7; pencil, D3-kernel containment and actual quotient transport are separate obligations'}
    with out.open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
    print('WROTE',out.name,'terms',len(coefficients),record['status'],flush=True)


if __name__=='__main__':main()
